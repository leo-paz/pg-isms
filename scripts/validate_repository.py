#!/usr/bin/env python3
"""Validate cumulative pg-isms research and skill-library phase invariants."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Set, Tuple

try:
    from .assemble_audit import AssemblyError, check_canonical_audit
    from .apply_audit_reclassifications import ReclassificationError, apply as check_audit_reclassifications
    from .apply_normalization_revisions import RevisionError, apply as check_normalization_revisions
    from .build_research_scaffold import AUDIT_FIELDS, read_corpus
    from .build_theme_projection import ProjectionError, build as check_theme_projection
    from .sync_taxonomy import SyncError, sync as check_taxonomy_sync
except ImportError:  # Direct script execution.
    from assemble_audit import AssemblyError, check_canonical_audit
    from apply_audit_reclassifications import ReclassificationError, apply as check_audit_reclassifications
    from apply_normalization_revisions import RevisionError, apply as check_normalization_revisions
    from build_research_scaffold import AUDIT_FIELDS, read_corpus
    from build_theme_projection import ProjectionError, build as check_theme_projection
    from sync_taxonomy import SyncError, sync as check_taxonomy_sync


PHASES = ("manifest", "audit", "taxonomy", "final")
CLASSIFICATIONS = {"core startup", "supporting startup", "excluded"}
TAXONOMY_FIELDS = {
    "skill_name",
    "purpose",
    "triggers",
    "non_triggers",
    "themes",
    "essay_ids",
    "stage_conditions",
    "tensions",
    "candidate_eval_cases",
}
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINE_RANGE = re.compile(r"^(\d+)-(\d+)$")
FINAL_REVIEW_CATEGORIES = {
    "missing principles",
    "overlap gaps",
    "contradictions",
    "stage dependent advice",
    "triggering quality",
    "copyright hygiene",
}
EVALUATION_CASE_TYPES = {"trigger", "non-trigger", "application", "condition", "edge"}


class ValidationError(ValueError):
    """Raised when a cumulative repository invariant is not satisfied."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def _load_json(path: Path) -> Any:
    _require(path.is_file(), f"missing required file: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"invalid JSON in {path}: {exc}") from exc


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    _require(path.is_file(), f"missing required file: {path}")
    records: List[Dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValidationError(f"invalid JSONL in {path}:{line_number}: {exc}") from exc
        _require(isinstance(record, dict), f"audit record {line_number} must be an object")
        records.append(record)
    return records


def _duplicates(values: Sequence[str]) -> Set[str]:
    seen: Set[str] = set()
    duplicates: Set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def _validate_manifest(repo: Path, corpus: Path, proof: Dict[str, int]) -> Tuple[List[Dict[str, str]], Dict[str, str]]:
    try:
        corpus_essays = read_corpus(corpus)
    except (OSError, ValueError) as exc:
        raise ValidationError(str(exc)) from exc
    _require(len(corpus_essays) == 223, f"expected exactly 223 corpus files, found {len(corpus_essays)}")
    manifest = _load_json(repo / "research/corpus-manifest.json")
    _require(isinstance(manifest, dict), "corpus manifest must be an object")
    essays = manifest.get("essays")
    _require(isinstance(essays, list), "corpus manifest essays must be an array")
    _require(manifest.get("document_count") == len(essays), "manifest document_count does not match essays")
    _require(all(isinstance(item, dict) for item in essays), "manifest essays must be objects")
    manifest_ids = [item.get("article_no") for item in essays]
    _require(all(isinstance(item, str) for item in manifest_ids), "manifest article numbers must be strings")
    duplicate_ids = _duplicates(manifest_ids)
    _require(not duplicate_ids, f"duplicate article number in manifest: {sorted(duplicate_ids)}")
    numeric_order = [int(article_no) for article_no in manifest_ids]
    _require(numeric_order == sorted(numeric_order), "manifest essays are not in numeric article order")
    corpus_by_id = {essay["article_no"]: essay for essay in corpus_essays}
    manifest_by_id = {essay["article_no"]: essay for essay in essays}
    missing_ids = sorted(set(corpus_by_id) - set(manifest_by_id))
    extra_ids = sorted(set(manifest_by_id) - set(corpus_by_id))
    _require(
        not missing_ids and not extra_ids,
        f"manifest does not match corpus; missing essay article IDs={missing_ids}, extra={extra_ids}",
    )
    for article_no, expected in corpus_by_id.items():
        actual = manifest_by_id[article_no]
        for field in ("article_no", "title", "source_url", "corpus_path"):
            _require(actual.get(field) == expected[field], f"manifest metadata mismatch for {article_no}: {field}")

    batch_data = _load_json(repo / "research/audit-batches.json")
    _require(isinstance(batch_data, dict), "audit batches must be an object")
    batches = batch_data.get("batches")
    _require(isinstance(batches, list), "audit batches must contain a batches array")
    _require(batch_data.get("batch_count") == len(batches), "batch_count does not match batches")
    _require(len(batches) == 12, f"expected exactly 12 audit batches, found {len(batches)}")
    assigned: List[str] = []
    batch_for_article: Dict[str, str] = {}
    sizes: List[int] = []
    previous_end: Optional[int] = None
    for index, batch in enumerate(batches, start=1):
        _require(isinstance(batch, dict), f"batch {index} must be an object")
        batch_id = batch.get("batch_id")
        _require(batch_id == f"batch-{index:02d}", f"unexpected batch id at position {index}: {batch_id}")
        article_nos = batch.get("article_nos")
        _require(isinstance(article_nos, list) and article_nos, f"{batch_id} has no assignments")
        _require(all(isinstance(item, str) for item in article_nos), f"{batch_id} article numbers must be strings")
        numbers = [int(item) for item in article_nos]
        _require(numbers == list(range(numbers[0], numbers[-1] + 1)), f"{batch_id} is not contiguous")
        if previous_end is not None:
            _require(numbers[0] == previous_end + 1, f"gap between audit batches before {batch_id}")
        previous_end = numbers[-1]
        _require(batch.get("start_article_no") == article_nos[0], f"{batch_id} start does not match assignments")
        _require(batch.get("end_article_no") == article_nos[-1], f"{batch_id} end does not match assignments")
        assigned.extend(article_nos)
        sizes.append(len(article_nos))
        for article_no in article_nos:
            batch_for_article.setdefault(article_no, batch_id)
    assignment_duplicates = _duplicates(assigned)
    assignment_set = set(assigned)
    gaps = set(corpus_by_id) - assignment_set
    extras = assignment_set - set(corpus_by_id)
    _require(not assignment_duplicates, f"overlapping audit batch assignments: {sorted(assignment_duplicates)}")
    _require(not gaps and not extras, f"audit batch assignment gaps={sorted(gaps)}, extras={sorted(extras)}")
    _require(max(sizes) - min(sizes) <= 1, "audit batch sizes differ by more than one")
    proof.update(
        corpus_files=len(corpus_essays),
        manifest_essays=len(essays),
        unique_assignments=len(assignment_set),
        batches=len(batches),
        gaps=len(gaps),
        overlaps=len(assignment_duplicates),
    )
    return corpus_essays, batch_for_article


def _specific_exclusion_reason(value: Any) -> bool:
    if not isinstance(value, str) or len(value.strip()) < 20:
        return False
    generic = {"not relevant", "irrelevant", "excluded", "n/a", "not startup related"}
    return value.strip().lower() not in generic


def _string_list(value: Any, *, allow_empty: bool = True) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and all(isinstance(item, str) and bool(item.strip()) for item in value)
    )


def _validate_line_ranges(value: Any, line_count: int, article_no: str) -> None:
    _require(isinstance(value, list), f"essay {article_no} evidence_line_ranges must be an array")
    for line_range in value:
        match = LINE_RANGE.fullmatch(line_range) if isinstance(line_range, str) else None
        _require(match is not None, f"essay {article_no} has invalid evidence line range: {line_range!r}")
        start, end = (int(part) for part in match.groups())
        _require(1 <= start <= end <= line_count, f"essay {article_no} evidence line range is outside the source file")


def _validate_audit(
    repo: Path,
    corpus: Path,
    corpus_essays: List[Dict[str, str]],
    batch_for_article: Mapping[str, str],
    proof: Dict[str, int],
) -> List[Dict[str, Any]]:
    if (repo / "research/audit-reclassifications.json").is_file():
        try:
            correction_proof = check_audit_reclassifications(repo, check=True)
        except ReclassificationError as exc:
            raise ValidationError(f"audit reclassification validation failed: {exc}") from exc
        proof["reviewed_reclassifications"] = correction_proof["corrections"]
    records = _load_jsonl(repo / "research/essay-audit.jsonl")
    record_ids = [record.get("article_no") for record in records]
    _require(all(isinstance(item, str) for item in record_ids), "audit article numbers must be strings")
    duplicates = _duplicates(record_ids)
    _require(not duplicates, f"duplicate article number in audit: {sorted(duplicates)}")
    corpus_by_id = {essay["article_no"]: essay for essay in corpus_essays}
    record_set = set(record_ids)
    missing = set(corpus_by_id) - record_set
    extra = record_set - set(corpus_by_id)
    _require(not missing and not extra, f"audit coverage mismatch; missing={sorted(missing)}, extra={sorted(extra)}")
    counts = {classification: 0 for classification in CLASSIFICATIONS}
    for record in records:
        article_no = record["article_no"]
        missing_fields = set(AUDIT_FIELDS) - set(record)
        _require(not missing_fields, f"essay {article_no} missing audit fields: {sorted(missing_fields)}")
        expected = corpus_by_id[article_no]
        for field in ("article_no", "title", "source_url", "corpus_path"):
            _require(record.get(field) == expected[field], f"audit metadata mismatch for {article_no}: {field}")
        classification = record.get("classification")
        _require(classification in CLASSIFICATIONS, f"invalid classification for essay {article_no}: {classification!r}")
        counts[classification] += 1
        _require(record.get("full_text_read") is True, f"essay {article_no} was not marked full_text_read")
        _require(
            isinstance(record.get("reviewer"), str) and bool(record["reviewer"].strip()),
            f"essay {article_no} is missing a reviewer",
        )
        _require(
            record.get("review_batch") == batch_for_article[article_no],
            f"essay {article_no} has the wrong review_batch",
        )
        for field in ("themes", "candidate_workflows", "final_skills"):
            _require(_string_list(record.get(field)), f"essay {article_no} {field} must be an array of strings")
        source = corpus / expected["corpus_path"]
        line_count = len(source.read_text(encoding="utf-8").splitlines())
        _validate_line_ranges(record.get("evidence_line_ranges"), line_count, article_no)
        if classification == "excluded":
            _require(
                _specific_exclusion_reason(record.get("exclusion_reason")),
                f"excluded essay {article_no} needs a specific exclusion reason",
            )
        else:
            _require(not str(record.get("exclusion_reason", "")).strip(), f"relevant essay {article_no} has an exclusion reason")
            has_themes = _string_list(record.get("themes"), allow_empty=False)
            has_evidence = bool(record.get("evidence_line_ranges"))
            _require(has_themes and has_evidence, f"relevant essay {article_no} requires themes and evidence line ranges")
            _require(
                _string_list(record.get("candidate_workflows"), allow_empty=False),
                f"relevant essay {article_no} requires candidate workflows",
            )
    try:
        check_canonical_audit(repo)
    except AssemblyError as exc:
        raise ValidationError(f"canonical audit batch validation failed: {exc}") from exc
    proof.update(
        classified=len(records),
        unaudited=len(missing),
        audit_duplicates=len(duplicates),
        core_startup=counts["core startup"],
        supporting_startup=counts["supporting startup"],
        excluded=counts["excluded"],
    )
    return records


def _taxonomy_entries(value: Any) -> List[Dict[str, Any]]:
    entries = value.get("skills") if isinstance(value, dict) else value
    _require(isinstance(entries, list), "taxonomy must be an array or contain a skills array")
    _require(all(isinstance(entry, dict) for entry in entries), "taxonomy skills must be objects")
    return entries


def _normalized_theme(value: str) -> str:
    """Normalize theme labels for case/punctuation-insensitive exact matching."""
    return " ".join(re.sub(r"[\W_]+", " ", value.casefold()).split())


def _load_current_theme_projection(repo: Path) -> List[Dict[str, Any]]:
    """Require the deterministic theme projection to match its current inputs."""
    projection_path = repo / "research/essay-theme-map.jsonl"
    _require(projection_path.is_file(), f"theme projection missing: {projection_path}")
    if (repo / "research/normalization-revisions.json").is_file():
        try:
            check_normalization_revisions(repo, check=True)
        except RevisionError as exc:
            raise ValidationError(f"normalization revision validation failed: {exc}") from exc
    try:
        check_theme_projection(repo, check=True)
    except ProjectionError as exc:
        raise ValidationError(f"theme projection validation failed: {exc}") from exc
    return _load_jsonl(projection_path)


def _validate_taxonomy(repo: Path, audit: List[Dict[str, Any]], proof: Dict[str, int]) -> List[Dict[str, Any]]:
    required_sources = {
        "audit reclassification": repo / "research/audit-reclassifications.json",
        "normalization revision": repo / "research/normalization-revisions.json",
        "taxonomy source": repo / "research/taxonomy-source.json",
    }
    for label, path in required_sources.items():
        _require(path.is_file(), f"missing required {label} source: {path}")
    projection = _load_current_theme_projection(repo)
    try:
        sync_proof = check_taxonomy_sync(repo, check=True)
    except SyncError as exc:
        raise ValidationError(f"taxonomy synchronization failed: {exc}") from exc
    projection_by_id = {record["article_no"]: record for record in projection}
    synthesis = repo / "research/theme-synthesis.md"
    _require(synthesis.is_file() and len(synthesis.read_text(encoding="utf-8").split()) >= 5, "missing theme synthesis")
    entries = _taxonomy_entries(_load_json(repo / "research/taxonomy.json"))
    names = [entry.get("skill_name") for entry in entries]
    _require(all(isinstance(name, str) and SKILL_NAME.fullmatch(name) for name in names), "taxonomy has invalid skill names")
    duplicate_names = _duplicates(names)
    _require(not duplicate_names, f"duplicate taxonomy skill names: {sorted(duplicate_names)}")
    relevant_ids = {record["article_no"] for record in audit if record["classification"] != "excluded"}
    audit_by_id = {record["article_no"]: record for record in audit}
    covered_ids: Set[str] = set()
    pairings: Set[Tuple[str, str]] = set()
    for entry in entries:
        name = entry["skill_name"]
        missing_fields = TAXONOMY_FIELDS - set(entry)
        _require(not missing_fields, f"taxonomy skill {name} missing fields: {sorted(missing_fields)}")
        _require(isinstance(entry.get("purpose"), str) and entry["purpose"].strip(), f"taxonomy skill {name} needs a purpose")
        for field in ("triggers", "non_triggers", "themes", "candidate_eval_cases"):
            _require(_string_list(entry.get(field), allow_empty=False), f"taxonomy skill {name} needs non-empty {field}")
        _require(
            _string_list(entry.get("essay_ids"), allow_empty=False),
            f"taxonomy coverage gap: skill {name} needs non-empty essay_ids",
        )
        for field in ("stage_conditions", "tensions"):
            _require(
                _string_list(entry.get(field), allow_empty=False),
                f"taxonomy skill {name} needs non-empty {field}",
            )
        essay_ids = set(entry["essay_ids"])
        unknown = essay_ids - relevant_ids
        _require(not unknown, f"taxonomy skill {name} cites excluded or unknown essays: {sorted(unknown)}")
        _require(essay_ids, f"orphan taxonomy skill {name} covers no essays")
        covered_ids.update(essay_ids)
        pairings.update((article_no, name) for article_no in essay_ids)
    uncovered = relevant_ids - covered_ids
    _require(not uncovered, f"taxonomy coverage gap; relevant essays not covered: {sorted(uncovered)}")
    taxonomy_names = set(names)
    taxonomy_by_name = {entry["skill_name"]: entry for entry in entries}
    for article_no in relevant_ids:
        final_skills = set(audit_by_id[article_no]["final_skills"])
        _require(final_skills, f"taxonomy coverage gap; essay {article_no} has no final_skills")
        unknown_skills = final_skills - taxonomy_names
        _require(not unknown_skills, f"essay {article_no} maps to unknown taxonomy skills: {sorted(unknown_skills)}")
        missing_pairings = {(article_no, name) for name in final_skills} - pairings
        _require(not missing_pairings, f"taxonomy does not reciprocally cover essay {article_no}")
        taxonomy_only = {name for paired_id, name in pairings if paired_id == article_no} - final_skills
        _require(not taxonomy_only, f"audit does not reciprocally map essay {article_no}: {sorted(taxonomy_only)}")
        canonical_themes = {
            _normalized_theme(theme) for theme in projection_by_id[article_no]["canonical_themes"]
        }
        mapped_themes = {
            _normalized_theme(theme)
            for skill_name in final_skills
            for theme in taxonomy_by_name[skill_name]["themes"]
        }
        missing_themes = canonical_themes - mapped_themes
        _require(
            not missing_themes,
            f"taxonomy theme coverage for essay {article_no} omits canonical themes: {sorted(missing_themes)}",
        )
    proof.update(
        skills=len(entries),
        relevant_essays=len(relevant_ids),
        projected_essays=len(projection),
        canonical_themes=sync_proof["themes"],
        essay_skill_pairings=sync_proof["essay_skill_pairings"],
        global_invariants=sync_proof["global_invariants"],
        product_types=sync_proof["product_types"],
        routing_rules=sync_proof["routing_rules"],
        decision_branches=sync_proof["decision_branches"],
        uncovered_relevant=len(uncovered),
        orphan_skills=0,
    )
    return entries


def _yaml_printable(value: str) -> bool:
    return all(
        character == "\t"
        or 0x20 <= ord(character) <= 0x7E
        or ord(character) == 0x85
        or 0xA0 <= ord(character) <= 0xD7FF
        or 0xE000 <= ord(character) <= 0xFFFD
        or 0x10000 <= ord(character) <= 0x10FFFF
        for character in value
    )


def _yaml_scalar(value: str, path: Path, line_number: int, *, require_quoted: bool = False) -> str:
    _require(_yaml_printable(value), f"invalid YAML scalar in {path}:{line_number}: non-printable control character")
    _require("\t" not in value, f"invalid YAML scalar in {path}:{line_number}: tab characters are not supported")
    value = value.strip()
    _require(bool(value), f"invalid YAML scalar in {path}:{line_number}")
    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            raise ValidationError(f"invalid YAML scalar in {path}:{line_number}: {exc}") from exc
        _require(isinstance(parsed, str), f"invalid YAML scalar in {path}:{line_number}")
        _require(_yaml_printable(parsed), f"invalid YAML scalar in {path}:{line_number}: non-printable control character")
        return parsed
    if value.startswith("'"):
        _require(len(value) >= 2 and value.endswith("'"), f"invalid YAML scalar in {path}:{line_number}")
        inner = value[1:-1]
        index = 0
        while index < len(inner):
            if inner[index] == "'":
                _require(
                    index + 1 < len(inner) and inner[index + 1] == "'",
                    f"invalid YAML scalar in {path}:{line_number}: unescaped apostrophe",
                )
                index += 2
            else:
                index += 1
        return inner.replace("''", "'")
    _require(not require_quoted, f"invalid YAML in {path}:{line_number}: string values must be quoted")
    _require(value[0] not in "[{&*!|>@`", f"invalid YAML scalar in {path}:{line_number}")
    _require(
        re.search(r":(?:\s|$)", value) is None,
        f"invalid YAML scalar in {path}:{line_number}: quote colon-delimited values",
    )
    return value


def _frontmatter(text: str, path: Path) -> Dict[str, str]:
    lines = text.splitlines()
    _require(lines and lines[0] == "---", f"{path} has invalid YAML frontmatter opening delimiter")
    metadata: Dict[str, str] = {}
    closing_index: Optional[int] = None
    for line_number, line in enumerate(lines[1:], start=2):
        if line == "---":
            closing_index = line_number - 1
            break
        if not line.strip():
            continue
        _require(line == line.lstrip(), f"{path} has invalid YAML frontmatter indentation at line {line_number}")
        if ":" not in line:
            raise ValidationError(f"{path} has invalid YAML frontmatter at line {line_number}")
        key, value = line.split(":", 1)
        key = key.strip()
        _require(re.fullmatch(r"[a-z][a-z0-9_-]*", key) is not None, f"{path} has invalid YAML frontmatter key")
        _require(key not in metadata, f"{path} has duplicate YAML frontmatter key: {key}")
        metadata[key] = _yaml_scalar(value, path, line_number)
    _require(closing_index is not None, f"{path} has unterminated YAML frontmatter")
    _require(set(metadata) == {"name", "description"}, f"{path} frontmatter must contain only name and description")
    body = "\n".join(lines[closing_index + 1 :]).strip()
    _require(bool(body) and any(line.startswith("# ") for line in body.splitlines()), f"{path} has no skill body heading")
    return metadata


def _validate_openai_yaml(path: Path, skill_name: str) -> None:
    _require(path.is_file(), f"missing skill package metadata: {path}")
    lines = path.read_text(encoding="utf-8").splitlines()
    _require(lines and lines[0] == "interface:", f"invalid agents/openai.yaml structure: {path}")
    values: Dict[str, str] = {}
    allowed = {"display_name", "short_description", "default_prompt", "icon_small", "icon_large", "brand_color"}
    for line_number, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        _require("\t" not in line and line.startswith("  ") and not line.startswith("   "), f"invalid agents/openai.yaml indentation: {path}:{line_number}")
        entry = line[2:]
        _require(":" in entry, f"invalid agents/openai.yaml entry: {path}:{line_number}")
        key, raw_value = entry.split(":", 1)
        _require(key in allowed, f"invalid agents/openai.yaml key {key!r}: {path}:{line_number}")
        _require(key not in values, f"duplicate agents/openai.yaml key {key!r}: {path}:{line_number}")
        values[key] = _yaml_scalar(raw_value, path, line_number, require_quoted=True)
    required = {"display_name", "short_description", "default_prompt"}
    _require(required <= set(values), f"invalid agents/openai.yaml; missing fields: {sorted(required - set(values))}")
    _require(bool(values["display_name"].strip()), f"invalid agents/openai.yaml display_name: {path}")
    _require(25 <= len(values["short_description"]) <= 64, f"invalid agents/openai.yaml short_description length: {path}")
    _require(f"${skill_name}" in values["default_prompt"], f"{path} default_prompt does not invoke ${skill_name}")


def _evaluation_cases(path: Path, skill_name: str) -> Set[str]:
    document = _load_json(path)
    _require(isinstance(document, dict) and document.get("schema_version") == 1, f"invalid evaluation cases schema for {skill_name}")
    cases = document.get("cases")
    _require(isinstance(cases, list), f"evaluation cases for {skill_name} must be an array")
    case_ids: List[str] = []
    case_types: Set[str] = set()
    for index, case in enumerate(cases, start=1):
        _require(isinstance(case, dict), f"evaluation case {index} for {skill_name} must be an object")
        case_id = case.get("id")
        _require(isinstance(case_id, str) and SKILL_NAME.fullmatch(case_id), f"evaluation case {index} for {skill_name} has an invalid id")
        _require(isinstance(case.get("prompt"), str) and case["prompt"].strip(), f"evaluation case {case_id} has no prompt")
        _require(_string_list(case.get("criteria"), allow_empty=False), f"evaluation case {case_id} has no scoring criteria")
        _require(isinstance(case.get("type"), str), f"evaluation case {case_id} has no type")
        _require(
            case["type"] in EVALUATION_CASE_TYPES,
            f"unsupported evaluation case type for {case_id}: {case['type']!r}",
        )
        case_ids.append(case_id)
        case_types.add(case["type"])
    duplicates = _duplicates(case_ids)
    _require(not duplicates, f"duplicate evaluation case ids for {skill_name}: {sorted(duplicates)}")
    _require(EVALUATION_CASE_TYPES <= case_types, f"evaluation cases for {skill_name} are incomplete")
    return set(case_ids)


def _number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _evaluation_summary(eval_dir: Path, skill_name: str, phase: str, case_ids: Set[str]) -> Dict[str, Any]:
    summary_path = eval_dir / phase / "summary.json"
    _require(summary_path.is_file(), f"missing {phase} evaluation summary for {skill_name}")
    summary = _load_json(summary_path)
    _require(isinstance(summary, dict) and summary.get("schema_version") == 1, f"invalid {phase} evaluation summary for {skill_name}")
    _require(summary.get("skill_name") == skill_name, f"{phase} evaluation summary skill mismatch for {skill_name}")
    _require(summary.get("phase") == phase, f"{phase} evaluation summary phase mismatch for {skill_name}")
    reviewer_id = summary.get("reviewer_id")
    _require(
        isinstance(reviewer_id, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", reviewer_id) is not None,
        f"{phase} evaluation summary lacks a stable reviewer_id for {skill_name}",
    )
    case_results = summary.get("case_results")
    _require(isinstance(case_results, list), f"{phase} evaluation summary case_results must be an array for {skill_name}")
    result_ids: List[str] = []
    raw_outputs: List[str] = []
    scores: Dict[str, float] = {}
    maxima: Dict[str, float] = {}
    for index, result in enumerate(case_results, start=1):
        _require(isinstance(result, dict), f"{phase} evaluation result {index} must be an object for {skill_name}")
        case_id = result.get("case_id")
        _require(isinstance(case_id, str), f"{phase} evaluation result {index} has no case_id for {skill_name}")
        score = result.get("score")
        max_score = result.get("max_score")
        _require(_number(score) and _number(max_score), f"{phase} evaluation result {case_id} has non-numeric scores")
        _require(max_score > 0 and 0 <= score <= max_score, f"{phase} evaluation result {case_id} has an invalid score")
        raw_output = result.get("raw_output")
        _require(isinstance(raw_output, str) and Path(raw_output).name == raw_output and raw_output.endswith(".md"), f"{phase} evaluation result {case_id} has an invalid raw output path")
        raw_path = eval_dir / phase / raw_output
        _require(raw_path.is_file(), f"missing raw output for {phase} case {case_id}: {raw_path}")
        raw_text = raw_path.read_text(encoding="utf-8")
        _require(len(raw_text.split()) >= 12, f"raw output is empty or abbreviated for {phase} case {case_id}")
        _require(f"Case ID: {case_id}" in raw_text, f"raw output does not identify {phase} case {case_id}")
        _require(f"Reviewer ID: {reviewer_id}" in raw_text, f"raw output reviewer does not match {phase} summary for {case_id}")
        result_ids.append(case_id)
        raw_outputs.append(raw_output)
        scores[case_id] = float(score)
        maxima[case_id] = float(max_score)
    result_duplicates = _duplicates(result_ids)
    _require(not result_duplicates, f"duplicate {phase} evaluation case results for {skill_name}: {sorted(result_duplicates)}")
    _require(set(result_ids) == case_ids, f"{phase} evaluation summary does not cover the exact case set for {skill_name}")
    raw_duplicates = _duplicates(raw_outputs)
    _require(not raw_duplicates, f"{phase} evaluation cases must have distinct raw output artifacts for {skill_name}")
    normalized_score = sum(scores.values()) / sum(maxima.values())
    return {
        "reviewer_id": reviewer_id,
        "normalized_score": normalized_score,
        "maxima": maxima,
        "raw_outputs": len(raw_outputs),
    }


def _normalized_tokens(text: str) -> List[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _window_hashes(tokens: Sequence[str], size: int) -> Iterable[bytes]:
    for index in range(0, len(tokens) - size + 1):
        yield hashlib.sha256(" ".join(tokens[index : index + size]).encode("utf-8")).digest()


def _copyright_violations(repo: Path, corpus: Path, window_size: int = 40) -> List[Path]:
    corpus_hashes: Set[bytes] = set()
    for source in corpus.glob("*.md"):
        tokens = _normalized_tokens(source.read_text(encoding="utf-8"))
        corpus_hashes.update(_window_hashes(tokens, window_size))
    candidates: List[Path] = []
    roots = [repo / "skills", repo / "evals", repo / "research"]
    for root in roots:
        if root.is_dir():
            candidates.extend(path for path in root.rglob("*") if path.suffix in {".md", ".json", ".jsonl", ".yaml", ".yml"})
    if (repo / "README.md").is_file():
        candidates.append(repo / "README.md")
    ignored_names = {"corpus-manifest.json", "audit-batches.json", "audit-schema.json"}
    violations: List[Path] = []
    for path in candidates:
        if path.name in ignored_names:
            continue
        tokens = _normalized_tokens(path.read_text(encoding="utf-8"))
        if any(digest in corpus_hashes for digest in _window_hashes(tokens, window_size)):
            violations.append(path)
    return sorted(set(violations))


def _git(args: Sequence[str], repo: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    _require(result.returncode == 0, f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def _review_category(value: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", value.casefold()).split())


def _review_field(section: str, field: str, category: str) -> str:
    match = re.search(rf"(?im)^{re.escape(field)}:\s*(\S.*?)\s*$", section)
    _require(match is not None, f"final review category {category!r} is missing {field}")
    return match.group(1).strip()


def _validate_final_review(path: Path) -> str:
    _require(path.is_file(), "missing independent final review evidence")
    text = path.read_text(encoding="utf-8")
    reviewer_match = re.search(r"(?im)^reviewer:\s*([A-Za-z0-9][A-Za-z0-9._-]*)\s*$", text)
    _require(reviewer_match is not None, "final review lacks an independent reviewer ID")
    _require(re.search(r"(?im)^status:\s*complete\s*$", text) is not None, "independent final review is not complete")
    headings = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", text))
    sections: Dict[str, str] = {}
    for index, heading in enumerate(headings):
        category = _review_category(heading.group(1))
        _require(category not in sections, f"duplicate final review category: {category}")
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        sections[category] = text[heading.end() : end]
    missing_categories = FINAL_REVIEW_CATEGORIES - set(sections)
    _require(not missing_categories, f"final review is missing required categories: {sorted(missing_categories)}")
    allowed_severities = {"none", "minor", "important", "critical"}
    allowed_dispositions = {"no-findings", "accepted", "rejected", "remediated"}
    for category in sorted(FINAL_REVIEW_CATEGORIES):
        section = sections[category]
        severity = _review_field(section, "Severity", category).casefold()
        disposition = _review_field(section, "Disposition", category).casefold()
        evidence = _review_field(section, "Evidence", category)
        affected = _review_field(section, "Affected essays/skills", category)
        remedy = _review_field(section, "Proposed remedy", category)
        verification = _review_field(section, "Verification", category)
        _require(severity in allowed_severities, f"final review category {category!r} has invalid severity")
        _require(disposition in allowed_dispositions, f"final review category {category!r} has invalid disposition")
        _require(len(evidence.split()) >= 8, f"final review category {category!r} lacks specific evidence")
        _require(bool(affected.strip()), f"final review category {category!r} lacks affected essays/skills")
        _require(bool(remedy.strip()), f"final review category {category!r} lacks a proposed remedy")
        _require(len(verification.split()) >= 5, f"final review category {category!r} lacks verification")
    return reviewer_match.group(1)


def _validate_final(repo: Path, corpus: Path, taxonomy: List[Dict[str, Any]], proof: Dict[str, int]) -> None:
    final_review = repo / "research/final-review.md"
    _validate_final_review(final_review)

    baseline_count = 0
    forward_count = 0
    baseline_raw_outputs = 0
    forward_raw_outputs = 0
    taxonomy_names = {entry["skill_name"] for entry in taxonomy}
    for name in sorted(taxonomy_names):
        skill_dir = repo / "skills" / name
        skill_md = skill_dir / "SKILL.md"
        metadata_path = skill_dir / "agents/openai.yaml"
        _require(skill_md.is_file(), f"missing skill package SKILL.md for {name}")
        metadata = _frontmatter(skill_md.read_text(encoding="utf-8"), skill_md)
        _require(metadata.get("name") == name, f"skill frontmatter name mismatch for {name}")
        _require(metadata.get("description", "").startswith("Use when"), f"skill {name} needs a trigger-focused description")
        _validate_openai_yaml(metadata_path, name)

        eval_dir = repo / "evals" / name
        case_ids = _evaluation_cases(eval_dir / "cases.json", name)
        baseline = _evaluation_summary(eval_dir, name, "baseline", case_ids)
        forward = _evaluation_summary(eval_dir, name, "forward", case_ids)
        _require(
            baseline["reviewer_id"] != forward["reviewer_id"],
            f"baseline and forward evaluations must use distinct fresh reviewer IDs for {name}",
        )
        _require(
            baseline["maxima"] == forward["maxima"],
            f"baseline and forward evaluations use different scoring scales for {name}",
        )
        improvement = forward["normalized_score"] - baseline["normalized_score"]
        _require(
            improvement >= 0.10,
            f"forward evaluation does not prove material improvement for {name}: delta={improvement:.3f}, required=0.100",
        )
        baseline_count += 1
        forward_count += 1
        baseline_raw_outputs += baseline["raw_outputs"]
        forward_raw_outputs += forward["raw_outputs"]

    readme = repo / "README.md"
    _require(readme.is_file(), "missing README catalog")
    catalog_entries = re.findall(r"skills/([a-z0-9]+(?:-[a-z0-9]+)*)/", readme.read_text(encoding="utf-8"))
    catalog_duplicates = _duplicates(catalog_entries)
    _require(not catalog_duplicates, f"README has duplicate skill catalog entries: {sorted(catalog_duplicates)}")
    catalog_names = set(catalog_entries)
    stale = catalog_names - taxonomy_names
    missing = taxonomy_names - catalog_names
    _require(not stale, f"README has stale skill catalog entries: {sorted(stale)}")
    _require(not missing, f"README is missing skill catalog entries: {sorted(missing)}")

    violations = _copyright_violations(repo, corpus)
    _require(not violations, f"unexpected long source excerpt in: {[str(path.relative_to(repo)) for path in violations]}")

    git_checked = 0
    if (repo / ".git").exists():
        status = _git(["status", "--porcelain"], repo)
        _require(not status, "real repository worktree is not clean")
        head = _git(["rev-parse", "HEAD"], repo)
        upstream = _git(["rev-parse", "@{upstream}"], repo)
        _require(head == upstream, "real repository HEAD is not pushed to its upstream")
        git_checked = 1
    proof.update(
        baseline_evaluations=baseline_count,
        forward_evaluations=forward_count,
        baseline_raw_outputs=baseline_raw_outputs,
        forward_raw_outputs=forward_raw_outputs,
        readme_catalog_entries=len(catalog_names),
        long_source_excerpts=len(violations),
        git_sync_checked=git_checked,
    )


def validate_repository(repo: Path, corpus: Path, phase: str) -> Dict[str, int]:
    """Validate all invariants through *phase* and return count-based proof."""
    _require(phase in PHASES, f"unknown phase: {phase}")
    repo = Path(repo).resolve()
    corpus = Path(corpus).resolve()
    proof: Dict[str, int] = {}
    corpus_essays, batch_for_article = _validate_manifest(repo, corpus, proof)
    audit: List[Dict[str, Any]] = []
    taxonomy: List[Dict[str, Any]] = []
    if PHASES.index(phase) >= PHASES.index("audit"):
        audit = _validate_audit(repo, corpus, corpus_essays, batch_for_article, proof)
    if PHASES.index(phase) >= PHASES.index("taxonomy"):
        taxonomy = _validate_taxonomy(repo, audit, proof)
    if phase == "final":
        _validate_final(repo, corpus, taxonomy, proof)
    return proof


def _format_proof(phase: str, proof: Mapping[str, int]) -> str:
    ordered = [
        "corpus_files",
        "manifest_essays",
        "unique_assignments",
        "batches",
        "gaps",
        "overlaps",
        "classified",
        "unaudited",
        "audit_duplicates",
        "core_startup",
        "supporting_startup",
        "excluded",
        "reviewed_reclassifications",
        "skills",
        "relevant_essays",
        "canonical_themes",
        "essay_skill_pairings",
        "global_invariants",
        "product_types",
        "routing_rules",
        "decision_branches",
        "uncovered_relevant",
        "orphan_skills",
        "baseline_evaluations",
        "forward_evaluations",
        "readme_catalog_entries",
        "long_source_excerpts",
        "git_sync_checked",
    ]
    values = " ".join(f"{key}={proof[key]}" for key in ordered if key in proof)
    return f"{phase} validation passed: {values}"


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", required=True, choices=PHASES)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--corpus", required=True, type=Path)
    return parser


def main() -> int:
    args = _parser().parse_args()
    try:
        proof = validate_repository(args.repo, args.corpus, args.phase)
    except ValidationError as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        return 1
    print(_format_proof(args.phase, proof))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
