#!/usr/bin/env python3
"""Validate audited-theme normalization and build its deterministic essay projection."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence


class ProjectionError(ValueError):
    """Raised when normalization or projection evidence is invalid."""


RELEVANT_CLASSIFICATIONS = {"core startup", "supporting startup"}
PROJECTION_KEYS = {
    "article_no",
    "raw_themes",
    "canonical_themes",
    "review_batch",
    "reviewer",
}


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ProjectionError(f"cannot read JSON {path}: {error}") from error


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise ProjectionError(f"cannot read JSONL {path}: {error}") from error
    records: List[Dict[str, Any]] = []
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ProjectionError(f"invalid JSONL {path}:{line_number}: {error}") from error
        if not isinstance(value, dict):
            raise ProjectionError(f"JSONL record must be an object: {path}:{line_number}")
        records.append(value)
    return records


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _duplicates(values: Sequence[str]) -> List[str]:
    counts = Counter(values)
    return sorted(value for value, count in counts.items() if count > 1)


def _validate_audit(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    article_nos = [record.get("article_no") for record in records]
    if not all(_nonempty_string(value) for value in article_nos):
        raise ProjectionError("audit records require nonempty article_no values")
    duplicate_articles = _duplicates(article_nos)
    if duplicate_articles:
        raise ProjectionError(f"duplicate audit article numbers: {duplicate_articles}")
    if article_nos != sorted(article_nos):
        raise ProjectionError("audit records are not sorted by article_no")

    relevant: List[Dict[str, Any]] = []
    for record in records:
        classification = record.get("classification")
        themes = record.get("themes")
        if not isinstance(themes, list) or not all(_nonempty_string(theme) for theme in themes):
            raise ProjectionError(f"audit {record['article_no']} has invalid themes")
        if classification in RELEVANT_CLASSIFICATIONS:
            if not themes:
                raise ProjectionError(f"relevant audit {record['article_no']} has no themes")
            if not _nonempty_string(record.get("review_batch")) or not _nonempty_string(
                record.get("reviewer")
            ):
                raise ProjectionError(
                    f"relevant audit {record['article_no']} lacks review provenance"
                )
            relevant.append(record)
        elif classification == "excluded":
            if themes:
                raise ProjectionError(f"excluded audit {record['article_no']} has themes")
        else:
            raise ProjectionError(
                f"audit {record['article_no']} has unsupported classification: {classification!r}"
            )
    return relevant


def _validate_targets(
    targets: Any, canonical_set: set[str], context: str
) -> List[str]:
    if not isinstance(targets, list) or not 1 <= len(targets) <= 3:
        raise ProjectionError(f"{context} must have one to three canonical themes")
    if not all(_nonempty_string(target) for target in targets):
        raise ProjectionError(f"{context} has an empty canonical target")
    duplicate_targets = _duplicates(targets)
    if duplicate_targets:
        raise ProjectionError(
            f"{context} has duplicate canonical targets: {duplicate_targets}"
        )
    undefined = sorted(set(targets) - canonical_set)
    if undefined:
        raise ProjectionError(f"{context} uses undefined canonical theme: {undefined}")
    if targets != sorted(targets):
        raise ProjectionError(f"{context} canonical targets are not sorted")
    return targets


def _validate_normalization(
    value: Any,
    audited_raw_themes: set[str],
    relevant_occurrences: set[tuple[str, str]],
) -> tuple[Dict[str, List[str]], Dict[tuple[str, str], List[str]], List[str]]:
    if not isinstance(value, dict):
        raise ProjectionError("theme normalization must be a JSON object")
    allowed_keys = {"schema_version", "method_notes", "canonical_themes", "mappings"}
    if set(value) != allowed_keys:
        raise ProjectionError(
            "theme normalization keys must be exactly " + ", ".join(sorted(allowed_keys))
        )
    schema_version = value.get("schema_version")
    if type(schema_version) is not int or schema_version != 1:
        raise ProjectionError("theme normalization schema_version must be the integer 1")
    method_notes = value.get("method_notes")
    if (
        not isinstance(method_notes, list)
        or not method_notes
        or not all(_nonempty_string(note) for note in method_notes)
    ):
        raise ProjectionError("method_notes must be a nonempty list of nonempty strings")

    canonical_records = value.get("canonical_themes")
    if not isinstance(canonical_records, list) or not canonical_records:
        raise ProjectionError("canonical_themes must be a nonempty list")
    canonical_names: List[str] = []
    for index, record in enumerate(canonical_records):
        if not isinstance(record, dict) or set(record) != {"name", "definition"}:
            raise ProjectionError(f"canonical theme {index} must contain name and definition")
        if not _nonempty_string(record.get("name")) or not _nonempty_string(
            record.get("definition")
        ):
            raise ProjectionError(f"canonical theme {index} has an empty name or definition")
        canonical_names.append(record["name"])
    duplicate_canonical = _duplicates(canonical_names)
    if duplicate_canonical:
        raise ProjectionError(f"duplicate canonical theme names: {duplicate_canonical}")
    if canonical_names != sorted(canonical_names):
        raise ProjectionError("canonical themes must be sorted by name")
    canonical_set = set(canonical_names)

    mapping_records = value.get("mappings")
    if not isinstance(mapping_records, list):
        raise ProjectionError("mappings must be a list")
    raw_names: List[str] = []
    mapping: Dict[str, List[str]] = {}
    overrides: Dict[tuple[str, str], List[str]] = {}
    used_targets: set[str] = set()
    for index, record in enumerate(mapping_records):
        required_mapping_keys = {"raw_theme", "canonical_themes", "reviewer"}
        allowed_mapping_keys = required_mapping_keys | {"article_overrides"}
        if (
            not isinstance(record, dict)
            or not required_mapping_keys <= set(record)
            or not set(record) <= allowed_mapping_keys
        ):
            raise ProjectionError(
                f"mapping {index} must contain raw_theme, canonical_themes, and reviewer"
            )
        raw_theme = record.get("raw_theme")
        targets = record.get("canonical_themes")
        if not _nonempty_string(raw_theme) or not _nonempty_string(record.get("reviewer")):
            raise ProjectionError(f"mapping {index} has empty raw theme or reviewer")
        targets = _validate_targets(targets, canonical_set, f"mapping {raw_theme!r}")
        raw_names.append(raw_theme)
        mapping[raw_theme] = targets
        used_targets.update(targets)

        override_records = record.get("article_overrides", [])
        if not isinstance(override_records, list):
            raise ProjectionError(f"mapping {raw_theme!r} article_overrides must be a list")
        override_article_nos: List[str] = []
        for override_index, override in enumerate(override_records):
            context = f"mapping {raw_theme!r} override {override_index}"
            if not isinstance(override, dict) or set(override) != {
                "article_no",
                "canonical_themes",
                "reviewer",
            }:
                raise ProjectionError(
                    f"{context} must contain article_no, canonical_themes, and reviewer"
                )
            article_no = override.get("article_no")
            if not _nonempty_string(article_no) or not _nonempty_string(
                override.get("reviewer")
            ):
                raise ProjectionError(f"{context} has empty article_no or reviewer")
            override_targets = _validate_targets(
                override.get("canonical_themes"), canonical_set, context
            )
            if (article_no, raw_theme) not in relevant_occurrences:
                raise ProjectionError(
                    f"{context} is not a relevant audit occurrence of {raw_theme!r}"
                )
            override_article_nos.append(article_no)
            overrides[(article_no, raw_theme)] = override_targets
            used_targets.update(override_targets)
        duplicate_override_articles = _duplicates(override_article_nos)
        if duplicate_override_articles:
            raise ProjectionError(
                f"mapping {raw_theme!r} has duplicate article override: "
                f"{duplicate_override_articles}"
            )
        if override_article_nos != sorted(override_article_nos):
            raise ProjectionError(f"mapping {raw_theme!r} article overrides are not sorted")

    duplicate_raw = _duplicates(raw_names)
    if duplicate_raw:
        raise ProjectionError(f"duplicate raw theme mapping: {duplicate_raw}")
    if raw_names != sorted(raw_names):
        raise ProjectionError("raw theme mappings must be sorted by raw_theme")
    unmapped = sorted(audited_raw_themes - set(raw_names))
    if unmapped:
        raise ProjectionError(f"unmapped raw themes: {unmapped}")
    extra = sorted(set(raw_names) - audited_raw_themes)
    if extra:
        raise ProjectionError(f"extra raw theme mappings: {extra}")
    unused = sorted(canonical_set - used_targets)
    if unused:
        raise ProjectionError(f"unused canonical themes: {unused}")
    return mapping, overrides, canonical_names


def _build_projection(
    relevant: Iterable[Dict[str, Any]],
    mapping: Mapping[str, List[str]],
    overrides: Mapping[tuple[str, str], List[str]],
) -> List[Dict[str, Any]]:
    projection: List[Dict[str, Any]] = []
    for audit in relevant:
        raw_themes = sorted(set(audit["themes"]))
        article_no = audit["article_no"]
        canonical_themes = sorted(
            {
                canonical
                for raw in raw_themes
                for canonical in overrides.get((article_no, raw), mapping[raw])
            }
        )
        if not canonical_themes:
            raise ProjectionError(f"relevant audit {audit['article_no']} has no canonical themes")
        projection.append(
            {
                "article_no": audit["article_no"],
                "raw_themes": raw_themes,
                "canonical_themes": canonical_themes,
                "review_batch": audit["review_batch"],
                "reviewer": audit["reviewer"],
            }
        )
    return projection


def _serialize_projection(records: Iterable[Dict[str, Any]]) -> bytes:
    text = "".join(
        json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records
    )
    return text.encode("utf-8")


def _validate_existing_projection(
    path: Path, expected: List[Dict[str, Any]], expected_bytes: bytes
) -> None:
    actual = _load_jsonl(path)
    article_nos = [record.get("article_no") for record in actual]
    if not all(_nonempty_string(article_no) for article_no in article_nos):
        raise ProjectionError("projection records require nonempty article_no strings")
    duplicate_articles = _duplicates(article_nos)
    if duplicate_articles:
        raise ProjectionError(f"duplicate projection article: {duplicate_articles}")
    expected_ids = [record["article_no"] for record in expected]
    missing = sorted(set(expected_ids) - set(article_nos))
    if missing:
        raise ProjectionError(f"missing projection records: {missing}")
    extra = sorted(set(article_nos) - set(expected_ids))
    if extra:
        raise ProjectionError(f"extra projection records: {extra}")
    if article_nos != sorted(article_nos):
        raise ProjectionError("projection records are not sorted by article_no")
    for record in actual:
        article_no = record.get("article_no")
        if set(record) != PROJECTION_KEYS:
            raise ProjectionError(f"projection {article_no} has invalid fields")
        if not _nonempty_string(record.get("review_batch")) or not _nonempty_string(
            record.get("reviewer")
        ):
            raise ProjectionError(f"projection {article_no} has invalid review provenance")
        for field in ("raw_themes", "canonical_themes"):
            values = record.get(field)
            if not isinstance(values, list) or not all(_nonempty_string(value) for value in values):
                raise ProjectionError(
                    f"projection {article_no} {field} must contain nonempty strings"
                )
            if values != sorted(set(values)):
                raise ProjectionError(f"projection {article_no} lacks sorted unique {field}")
    try:
        actual_bytes = path.read_bytes()
    except OSError as error:
        raise ProjectionError(f"cannot read projection {path}: {error}") from error
    if actual != expected or actual_bytes != expected_bytes:
        raise ProjectionError("projection is stale relative to audit or normalization")


def build(repo: Path, check: bool = False) -> Dict[str, int]:
    """Validate inputs, then write or byte-check the deterministic projection."""
    research = repo.resolve() / "research"
    audit = _load_jsonl(research / "essay-audit.jsonl")
    relevant = _validate_audit(audit)
    raw_assignment_count = sum(len(record["themes"]) for record in relevant)
    raw_counts = Counter(theme for record in relevant for theme in record["themes"])
    normalization = _load_json(research / "theme-normalization.json")
    relevant_occurrences = {
        (record["article_no"], theme) for record in relevant for theme in record["themes"]
    }
    mapping, overrides, canonical_names = _validate_normalization(
        normalization, set(raw_counts), relevant_occurrences
    )
    projection = _build_projection(relevant, mapping, overrides)
    expected_bytes = _serialize_projection(projection)
    projection_path = research / "essay-theme-map.jsonl"
    if check:
        _validate_existing_projection(projection_path, projection, expected_bytes)
    else:
        projection_path.write_bytes(expected_bytes)
    return {
        "raw_assignments": raw_assignment_count,
        "distinct_raw": len(raw_counts),
        "singleton_raw": sum(count == 1 for count in raw_counts.values()),
        "canonical": len(canonical_names),
        "article_overrides": len(overrides),
        "relevant_essays": len(relevant),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        proof = build(args.repo, check=args.check)
    except ProjectionError as error:
        print(f"theme projection failed: {error}", file=sys.stderr)
        return 1
    action = "check passed" if args.check else "written"
    print(
        f"theme projection {action}: "
        + " ".join(f"{key}={value}" for key, value in proof.items())
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
