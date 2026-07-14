#!/usr/bin/env python3
"""Build the deterministic metadata and review-batch scaffold for the essay audit."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Sequence


REQUIRED_FRONTMATTER = ("article_no", "title", "source_url")
AUDIT_FIELDS = (
    "article_no",
    "title",
    "source_url",
    "corpus_path",
    "classification",
    "exclusion_reason",
    "themes",
    "candidate_workflows",
    "final_skills",
    "evidence_line_ranges",
    "review_batch",
    "reviewer",
    "full_text_read",
)


def _parse_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid quoted frontmatter value: {value}") from exc
        if not isinstance(parsed, str):
            raise ValueError(f"frontmatter value must be a string: {value}")
        return parsed
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    return value


def parse_frontmatter(path: Path) -> Dict[str, str]:
    """Read the small scalar-only YAML frontmatter used by the source corpus."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: missing opening frontmatter delimiter")
    metadata: Dict[str, str] = {}
    for line_number, line in enumerate(lines[1:], start=2):
        if line.strip() == "---":
            break
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"{path}:{line_number}: invalid frontmatter entry")
        key, value = line.split(":", 1)
        key = key.strip()
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_-]*", key):
            raise ValueError(f"{path}:{line_number}: invalid frontmatter key {key!r}")
        if key in metadata:
            raise ValueError(f"{path}:{line_number}: duplicate frontmatter key {key!r}")
        metadata[key] = _parse_scalar(value)
    else:
        raise ValueError(f"{path}: missing closing frontmatter delimiter")
    missing = [key for key in REQUIRED_FRONTMATTER if not metadata.get(key)]
    if missing:
        raise ValueError(f"{path}: missing frontmatter fields: {', '.join(missing)}")
    return metadata


def read_corpus(corpus: Path) -> List[Dict[str, str]]:
    """Return canonical essay metadata sorted by numeric article number."""
    corpus = Path(corpus)
    if not corpus.is_dir():
        raise ValueError(f"corpus directory does not exist: {corpus}")
    essays: List[Dict[str, str]] = []
    seen: Dict[int, Path] = {}
    for path in corpus.glob("*.md"):
        metadata = parse_frontmatter(path)
        article_no = metadata["article_no"]
        if not re.fullmatch(r"\d+", article_no):
            raise ValueError(f"{path}: article_no must be numeric")
        number = int(article_no)
        if number in seen:
            raise ValueError(f"duplicate article number {article_no}: {seen[number]} and {path}")
        seen[number] = path
        essays.append(
            {
                "article_no": f"{number:03d}",
                "title": metadata["title"],
                "source_url": metadata["source_url"],
                "corpus_path": path.name,
            }
        )
    if not essays:
        raise ValueError(f"corpus contains no Markdown essays: {corpus}")
    essays.sort(key=lambda essay: int(essay["article_no"]))
    return essays


def make_batches(essays: Sequence[Dict[str, str]], batch_count: int) -> List[Dict[str, Any]]:
    if batch_count < 1:
        raise ValueError("batch_count must be positive")
    if batch_count > len(essays):
        raise ValueError("batch_count cannot exceed the essay count")
    base_size, larger_batches = divmod(len(essays), batch_count)
    batches: List[Dict[str, Any]] = []
    cursor = 0
    for index in range(batch_count):
        size = base_size + (1 if index < larger_batches else 0)
        article_nos = [essay["article_no"] for essay in essays[cursor : cursor + size]]
        batches.append(
            {
                "batch_id": f"batch-{index + 1:02d}",
                "start_article_no": article_nos[0],
                "end_article_no": article_nos[-1],
                "article_nos": article_nos,
                "reviewer": None,
            }
        )
        cursor += size
    return batches


def audit_schema() -> Dict[str, Any]:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "pg-isms essay audit record",
        "type": "object",
        "additionalProperties": False,
        "required": list(AUDIT_FIELDS),
        "properties": {
            "article_no": {"type": "string", "pattern": r"^\d{3}$"},
            "title": {"type": "string", "minLength": 1},
            "source_url": {"type": "string", "pattern": r"^https?://"},
            "corpus_path": {"type": "string", "minLength": 1},
            "classification": {
                "type": "string",
                "enum": ["core startup", "supporting startup", "excluded"],
            },
            "exclusion_reason": {"type": "string"},
            "themes": {"type": "array", "items": {"type": "string", "minLength": 1}},
            "candidate_workflows": {
                "type": "array",
                "items": {"type": "string", "minLength": 1},
            },
            "final_skills": {"type": "array", "items": {"type": "string", "minLength": 1}},
            "evidence_line_ranges": {
                "type": "array",
                "items": {"type": "string", "pattern": r"^\d+-\d+$"},
            },
            "review_batch": {"type": "string", "pattern": r"^batch-\d{2}$"},
            "reviewer": {"type": "string", "minLength": 1},
            "full_text_read": {"const": True},
        },
    }


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build_research_scaffold(corpus: Path, output_root: Path, batch_count: int = 12) -> None:
    essays = read_corpus(Path(corpus))
    batches = make_batches(essays, batch_count)
    research = Path(output_root) / "research"
    research.mkdir(parents=True, exist_ok=True)
    _write_json(
        research / "corpus-manifest.json",
        {"schema_version": 1, "document_count": len(essays), "essays": essays},
    )
    _write_json(
        research / "audit-batches.json",
        {"schema_version": 1, "batch_count": len(batches), "batches": batches},
    )
    _write_json(research / "audit-schema.json", audit_schema())
    retrieval_log = research / "retrieval-log.jsonl"
    if not retrieval_log.exists():
        retrieval_log.write_text("", encoding="utf-8")
    progress = research / "progress.md"
    if not progress.exists():
        progress.write_text(
            "# Research progress\n\nCheckpoint evidence is recorded here as the audit proceeds.\n",
            encoding="utf-8",
        )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--batch-count", default=12, type=int)
    return parser


def main() -> int:
    args = _parser().parse_args()
    try:
        build_research_scaffold(args.corpus, args.output_root, args.batch_count)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}")
        return 1
    print(f"generated research scaffold from {len(read_corpus(args.corpus))} corpus files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
