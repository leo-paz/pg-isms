#!/usr/bin/env python3
"""Apply or verify independently reviewed audit reclassifications in primary batches."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping

try:
    from .assemble_audit import assemble, validate_assembly_inputs
except ImportError:  # Direct script execution.
    from assemble_audit import assemble, validate_assembly_inputs


class ReclassificationError(ValueError):
    """Raised when a correction is missing, stale, or would overwrite unexpected evidence."""


UPDATE_FIELDS = {
    "classification",
    "exclusion_reason",
    "themes",
    "candidate_workflows",
    "evidence_line_ranges",
}


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ReclassificationError(f"cannot read JSON {path}: {exc}") from exc


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    try:
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    except (OSError, json.JSONDecodeError) as exc:
        raise ReclassificationError(f"cannot read JSONL {path}: {exc}") from exc


def _write_jsonl(path: Path, records: Iterable[Mapping[str, Any]]) -> None:
    path.write_text(
        "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
        encoding="utf-8",
    )


def _expected(record: Mapping[str, Any], correction: Mapping[str, Any]) -> Dict[str, Any]:
    expected = dict(record)
    for field in UPDATE_FIELDS:
        if field not in correction:
            raise ReclassificationError(f"correction {correction.get('article_no')} is missing {field}")
        expected[field] = correction[field]
    expected["final_skills"] = record.get("final_skills", [])
    return expected


def apply(repo: Path, *, check: bool = False) -> Dict[str, int]:
    repo = repo.resolve()
    research = repo / "research"
    document = _load_json(research / "audit-reclassifications.json")
    corrections = document.get("corrections") if isinstance(document, dict) else None
    if not isinstance(corrections, list) or not corrections:
        raise ReclassificationError("audit reclassifications must contain corrections")
    by_id: Dict[str, Dict[str, Any]] = {}
    for correction in corrections:
        article_no = correction.get("article_no") if isinstance(correction, dict) else None
        if not isinstance(article_no, str) or article_no in by_id:
            raise ReclassificationError(f"invalid or duplicate correction article: {article_no!r}")
        if correction.get("previous_classification") == correction.get("classification"):
            raise ReclassificationError(f"correction {article_no} does not change classification")
        by_id[article_no] = correction

    found: set[str] = set()
    changed = 0
    batch_paths = sorted((research / "batches").glob("batch-*.jsonl"))
    outputs: Dict[Path, List[Dict[str, Any]]] = {}
    for path in batch_paths:
        records = _load_jsonl(path)
        output: List[Dict[str, Any]] = []
        for record in records:
            article_no = record.get("article_no")
            correction = by_id.get(article_no)
            if correction is None:
                output.append(record)
                continue
            found.add(article_no)
            expected = _expected(record, correction)
            desired = all(record.get(field) == expected.get(field) for field in UPDATE_FIELDS)
            if check:
                if not desired:
                    raise ReclassificationError(f"audit correction is stale for article {article_no}")
                output.append(record)
                continue
            if not desired and record.get("classification") != correction.get("previous_classification"):
                raise ReclassificationError(
                    f"article {article_no} has unexpected classification {record.get('classification')!r}"
                )
            if record != expected:
                changed += 1
            output.append(expected)
        outputs[path] = output

    missing = set(by_id) - found
    if missing:
        raise ReclassificationError(f"corrections not found in primary audit batches: {sorted(missing)}")
    if not check:
        validate_assembly_inputs(repo)
        for path, output in outputs.items():
            _write_jsonl(path, output)
        assemble(repo)
    return {"corrections": len(by_id), "changed": changed if not check else 0}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        proof = apply(args.repo, check=args.check)
    except ReclassificationError as exc:
        print(f"audit reclassification failed: {exc}")
        return 1
    action = "check" if args.check else "apply"
    print(f"audit reclassification {action} passed: " + " ".join(f"{k}={v}" for k, v in proof.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
