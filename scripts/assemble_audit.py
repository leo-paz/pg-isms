#!/usr/bin/env python3
"""Assemble independently written audit batches into canonical research files."""

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List


class AssemblyError(ValueError):
    """Raised when a batch cannot be integrated without weakening audit evidence."""


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise AssemblyError(f"cannot read JSON {path}: {error}") from error


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise AssemblyError(f"cannot read JSONL {path}: {error}") from error
    records: List[Dict[str, Any]] = []
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise AssemblyError(f"invalid JSONL {path}:{line_number}: {error}") from error
        if not isinstance(value, dict):
            raise AssemblyError(f"JSONL record must be an object: {path}:{line_number}")
        records.append(value)
    return records


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, records: Iterable[Dict[str, Any]]) -> None:
    text = "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records)
    path.write_text(text, encoding="utf-8")


def _validate_audit_batch(batch: Dict[str, Any], records: List[Dict[str, Any]]) -> str:
    batch_id = batch.get("batch_id")
    assigned = batch.get("article_nos")
    if not isinstance(batch_id, str) or not isinstance(assigned, list):
        raise AssemblyError("invalid batch assignment")
    article_nos = [record.get("article_no") for record in records]
    if article_nos != assigned:
        raise AssemblyError(f"{batch_id} article set mismatch: expected {assigned}, got {article_nos}")
    reviewers = {record.get("reviewer") for record in records}
    if len(reviewers) != 1 or not all(isinstance(value, str) and value.strip() for value in reviewers):
        raise AssemblyError(f"{batch_id} must have one nonempty reviewer")
    reviewer = next(iter(reviewers))
    for record in records:
        if record.get("review_batch") != batch_id:
            raise AssemblyError(f"{batch_id} record has wrong review_batch")
    return reviewer


def _validate_retrieval_batch(
    batch: Dict[str, Any], reviewer: str, records: List[Dict[str, Any]]
) -> Dict[str, int]:
    batch_id = batch["batch_id"]
    assigned = batch["article_nos"]
    for record in records:
        if record.get("batch_id") != batch_id:
            raise AssemblyError(f"{batch_id} retrieval record has wrong batch_id")
        if record.get("reviewer") != reviewer:
            raise AssemblyError(f"{batch_id} retrieval record has wrong reviewer")
    modes = [record.get("mode") for record in records]
    for mode in ("bm25", "vector"):
        queries = [record for record in records if record.get("mode") == mode]
        if not queries:
            raise AssemblyError(f"{batch_id} retrieval log is missing {mode}")
        for query in queries:
            required = ("date", "query", "collection", "limit", "results")
            if not all(key in query for key in required) or not isinstance(query.get("results"), list):
                raise AssemblyError(f"{batch_id} has invalid {mode} query evidence")
    full_documents = [record for record in records if record.get("mode") == "full_document"]
    full_ids = [record.get("article_no") for record in full_documents]
    if full_ids != assigned:
        raise AssemblyError(
            f"{batch_id} full_document article set mismatch: expected {assigned}, got {full_ids}"
        )
    for record in full_documents:
        retrieved_lines = record.get("retrieved_lines")
        valid_line_proof = isinstance(retrieved_lines, int) and retrieved_lines > 0
        if isinstance(retrieved_lines, str):
            parts = retrieved_lines.split("-", maxsplit=1)
            valid_line_proof = (
                len(parts) == 2
                and all(part.isdigit() for part in parts)
                and int(parts[0]) == 1
                and int(parts[1]) >= 1
            )
        valid = (
            record.get("full_text_read") is True
            and valid_line_proof
            and isinstance(record.get("document"), str)
            and bool(record["document"].strip())
            and isinstance(record.get("purpose"), str)
            and bool(record["purpose"].strip())
        )
        if not valid:
            raise AssemblyError(f"{batch_id} has invalid full_document evidence")
    unexpected = set(modes) - {"bm25", "vector", "full_document"}
    if unexpected:
        raise AssemblyError(f"{batch_id} has unsupported retrieval modes: {sorted(unexpected)}")
    return {
        "bm25": 1,
        "vector": 1,
        "full_documents": len(full_documents),
    }


def validate_batch(repo: Path, batch_id: str) -> Dict[str, Any]:
    """Validate one isolated batch without requiring the other batch files."""
    repo = repo.resolve()
    research = repo / "research"
    config = _load_json(research / "audit-batches.json")
    batches = config.get("batches") if isinstance(config, dict) else None
    if not isinstance(batches, list):
        raise AssemblyError("invalid audit batch configuration")
    matches = [batch for batch in batches if batch.get("batch_id") == batch_id]
    if len(matches) != 1:
        raise AssemblyError(f"unknown or duplicate batch_id: {batch_id}")
    batch = matches[0]
    audit_records = _load_jsonl(research / "batches" / f"{batch_id}.jsonl")
    reviewer = _validate_audit_batch(batch, audit_records)
    retrieval_records = _load_jsonl(research / "batches" / f"retrieval-{batch_id}.jsonl")
    proof = _validate_retrieval_batch(batch, reviewer, retrieval_records)
    return {
        "batch_id": batch_id,
        "reviewer": reviewer,
        "essays": len(audit_records),
        **proof,
    }


def assemble(repo: Path) -> Dict[str, int]:
    """Validate all assigned batches and write deterministic canonical outputs."""
    repo = repo.resolve()
    research = repo / "research"
    config = _load_json(research / "audit-batches.json")
    batches = config.get("batches") if isinstance(config, dict) else None
    if not isinstance(batches, list) or config.get("batch_count") != len(batches):
        raise AssemblyError("invalid audit batch configuration")

    all_audit: List[Dict[str, Any]] = []
    all_retrieval: List[Dict[str, Any]] = []
    bm25_batches = 0
    vector_batches = 0
    full_documents = 0
    for batch in batches:
        batch_id = batch.get("batch_id")
        audit_path = research / "batches" / f"{batch_id}.jsonl"
        retrieval_path = research / "batches" / f"retrieval-{batch_id}.jsonl"
        audit_records = _load_jsonl(audit_path)
        reviewer = _validate_audit_batch(batch, audit_records)
        retrieval_records = _load_jsonl(retrieval_path)
        retrieval_proof = _validate_retrieval_batch(batch, reviewer, retrieval_records)
        batch["reviewer"] = reviewer
        all_audit.extend(audit_records)
        all_retrieval.extend(retrieval_records)
        bm25_batches += retrieval_proof["bm25"]
        vector_batches += retrieval_proof["vector"]
        full_documents += retrieval_proof["full_documents"]

    article_nos = [record["article_no"] for record in all_audit]
    if article_nos != sorted(article_nos):
        raise AssemblyError("canonical audit is not numerically sorted")
    if len(article_nos) != len(set(article_nos)):
        raise AssemblyError("canonical audit contains duplicate article numbers")

    base_log_path = research / "retrieval-log.jsonl"
    base_records = _load_jsonl(base_log_path) if base_log_path.exists() else []
    unbatched = [record for record in base_records if "batch_id" not in record]
    _write_json(research / "audit-batches.json", config)
    _write_jsonl(research / "essay-audit.jsonl", all_audit)
    _write_jsonl(base_log_path, unbatched + all_retrieval)
    return {
        "batches": len(batches),
        "essays": len(all_audit),
        "bm25_batches": bm25_batches,
        "vector_batches": vector_batches,
        "full_documents": full_documents,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--batch-id", help="validate one batch without assembling canonical outputs")
    args = parser.parse_args()
    if args.batch_id:
        proof = validate_batch(args.repo, args.batch_id)
        print("batch validation passed: " + " ".join(f"{key}={value}" for key, value in proof.items()))
        return 0
    proof = assemble(args.repo)
    print(
        "audit assembly passed: "
        + " ".join(f"{key}={value}" for key, value in proof.items())
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
