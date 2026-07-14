#!/usr/bin/env python3
"""Generate concise, exact essay provenance for one synthesized skill package."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping


class ProvenanceError(ValueError):
    """Raised when a skill provenance file cannot be derived exactly."""


LINE_RANGE = re.compile(r"^(\d+)-(\d+)$")


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ProvenanceError(f"cannot read JSON {path}: {exc}") from exc


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
        return [json.loads(line) for line in lines if line.strip()]
    except (OSError, json.JSONDecodeError) as exc:
        raise ProvenanceError(f"cannot read JSONL {path}: {exc}") from exc


def _string_list(value: Any, field: str) -> List[str]:
    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
        raise ProvenanceError(f"skill provenance requires non-empty {field}")
    return value


def _bullets(values: Iterable[str]) -> str:
    return "\n".join(f"- {value}" for value in values)


def _cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def _indexed(rows: List[Dict[str, Any]], label: str) -> Dict[str, Dict[str, Any]]:
    article_ids = [row.get("article_no") for row in rows]
    if not all(isinstance(article_no, str) for article_no in article_ids):
        raise ProvenanceError(f"{label} has an invalid article number")
    if len(article_ids) != len(set(article_ids)):
        raise ProvenanceError(f"{label} has duplicate article numbers")
    return {row["article_no"]: row for row in rows}


def _bounds(value: str, article_no: str) -> tuple[int, int]:
    match = LINE_RANGE.fullmatch(value) if isinstance(value, str) else None
    if match is None:
        raise ProvenanceError(f"skill provenance has invalid line range for {article_no}: {value!r}")
    start, end = (int(part) for part in match.groups())
    if start < 1 or end < start:
        raise ProvenanceError(f"skill provenance has invalid line range for {article_no}: {value!r}")
    return start, end


def _render(
    skill: Mapping[str, Any],
    audit: Mapping[str, Mapping[str, Any]],
    projection: Mapping[str, Mapping[str, Any]],
    evidence_document: Mapping[str, Any],
) -> str:
    name = skill.get("skill_name")
    if not isinstance(name, str):
        raise ProvenanceError("skill provenance has no skill name")
    purpose = skill.get("purpose")
    if not isinstance(purpose, str) or not purpose.strip():
        raise ProvenanceError(f"skill provenance requires purpose for {name}")
    themes = _string_list(skill.get("themes"), "themes")
    essay_ids = _string_list(skill.get("essay_ids"), "essay_ids")
    missing_audit = set(essay_ids) - set(audit)
    missing_projection = set(essay_ids) - set(projection)
    if missing_audit or missing_projection:
        raise ProvenanceError(
            f"skill provenance has missing essays: audit={sorted(missing_audit)} projection={sorted(missing_projection)}"
        )
    records = evidence_document.get("records")
    if evidence_document.get("schema_version") != 1 or evidence_document.get("skill_name") != name:
        raise ProvenanceError(f"skill evidence metadata mismatch for {name}")
    if not isinstance(records, list) or not all(isinstance(record, dict) for record in records):
        raise ProvenanceError(f"skill evidence records are invalid for {name}")
    evidence_by_id = _indexed(records, "skill evidence")
    if list(evidence_by_id) != essay_ids or set(evidence_by_id) != set(essay_ids):
        raise ProvenanceError(f"skill evidence does not cover the exact ordered essay set for {name}")

    title = name.replace("-", " ").title()
    lines = [
        f"# Provenance: {title}",
        "",
        "This file is generated from the canonical audit, theme projection, and taxonomy. It records concise provenance rather than reproducing source prose.",
        "",
        "## Contents",
        "",
        "- Runtime scope, triggers, non-triggers, and stage conditions",
        "- Canonical themes owned by this skill",
        "- Skill-specific essay claims and exact local corpus ranges",
        "- Source-use and revalidation rule",
        "",
        "## Runtime scope",
        "",
        purpose,
        "",
        "### Triggers",
        "",
        _bullets(_string_list(skill.get("triggers"), "triggers")),
        "",
        "### Non-triggers",
        "",
        _bullets(_string_list(skill.get("non_triggers"), "non_triggers")),
        "",
        "### Stage conditions",
        "",
        _bullets(_string_list(skill.get("stage_conditions"), "stage_conditions")),
        "",
        "### Preserved tensions",
        "",
        _bullets(_string_list(skill.get("tensions"), "tensions")),
        "",
        "## Canonical themes",
        "",
        _bullets(f"`{theme}`" for theme in themes),
        "",
        "## Essay evidence inventory",
        "",
        "Each range below was independently reviewed for this exact skill and canonical theme. Ranges address the committed local corpus path; audit-wide ranges supporting other skills are intentionally omitted.",
        "",
        "| ID | Essay | Corpus path | Skill-specific claim and evidence | Review lineage |",
        "|---|---|---|---|---|",
    ]
    theme_set = set(themes)
    for article_no in essay_ids:
        record = audit[article_no]
        projected = projection[article_no]
        title_value = record.get("title")
        source_url = record.get("source_url")
        corpus_path = record.get("corpus_path")
        audit_reviewer = record.get("reviewer")
        review_batch = record.get("review_batch")
        final_skills = record.get("final_skills")
        audit_ranges = record.get("evidence_line_ranges")
        canonical = projected.get("canonical_themes")
        if not all(isinstance(value, str) and value.strip() for value in (title_value, source_url, corpus_path, audit_reviewer, review_batch)):
            raise ProvenanceError(f"skill provenance has invalid source metadata for {article_no}")
        if not isinstance(final_skills, list) or name not in final_skills:
            raise ProvenanceError(f"skill provenance is not reciprocal for {article_no}/{name}")
        if not isinstance(audit_ranges, list) or not audit_ranges:
            raise ProvenanceError(f"skill provenance has no evidence ranges for {article_no}")
        if not isinstance(canonical, list):
            raise ProvenanceError(f"skill provenance has no theme projection for {article_no}")
        incorporated = sorted(theme_set & set(canonical))
        if not incorporated:
            raise ProvenanceError(f"skill provenance has no owned theme for {article_no}")
        evidence_record = evidence_by_id[article_no]
        if evidence_record.get("skill_name") != name or not isinstance(evidence_record.get("reviewer"), str):
            raise ProvenanceError(f"skill evidence identity mismatch for {article_no}")
        entries = evidence_record.get("theme_evidence")
        if not isinstance(entries, list) or not entries or not all(isinstance(entry, dict) for entry in entries):
            raise ProvenanceError(f"skill evidence themes are invalid for {article_no}")
        entry_themes = [entry.get("canonical_theme") for entry in entries]
        if len(entry_themes) != len(set(entry_themes)) or set(entry_themes) != set(incorporated):
            raise ProvenanceError(f"skill evidence themes do not exactly match projection for {article_no}")
        audited_bounds = [_bounds(value, article_no) for value in audit_ranges]
        evidence_parts: List[str] = []
        for entry in entries:
            claim = entry.get("claim")
            ranges = entry.get("line_ranges")
            if not isinstance(claim, str) or len(claim.split()) < 6:
                raise ProvenanceError(f"skill evidence claim is incomplete for {article_no}")
            if not isinstance(ranges, list) or not ranges:
                raise ProvenanceError(f"skill evidence range is missing for {article_no}")
            for line_range in ranges:
                start, end = _bounds(line_range, article_no)
                if not any(audit_start <= start <= end <= audit_end for audit_start, audit_end in audited_bounds):
                    raise ProvenanceError(
                        f"skill evidence range {line_range} is outside audited evidence for {article_no}"
                    )
            range_text = ", ".join(f"`{value}`" for value in ranges)
            evidence_parts.append(
                f"`{entry['canonical_theme']}` — {_cell(claim)} ({range_text})"
            )
        evidence = "<br>".join(evidence_parts)
        essay_link = f"[{_cell(title_value)}]({_cell(source_url)})"
        lineage = f"{_cell(audit_reviewer)} / {_cell(review_batch)}; {_cell(evidence_record['reviewer'])}"
        lines.append(
            f"| `{article_no}` | {essay_link} | `{_cell(corpus_path)}` | {evidence} | {lineage} |"
        )

    lines.extend(
        [
            "",
            "## Source-use rule",
            "",
            "Resolve each range against the listed file in the local corpus snapshot. Use the linked source when deeper context is needed. Revalidate time-sensitive claims before applying them, and paraphrase the principle instead of copying long passages.",
            "",
        ]
    )
    return "\n".join(lines)


def build(repo: Path, skill_name: str, *, check: bool = False) -> Dict[str, int]:
    repo = Path(repo).resolve()
    taxonomy = _load_json(repo / "research/taxonomy.json")
    skills = taxonomy.get("skills") if isinstance(taxonomy, dict) else None
    if not isinstance(skills, list):
        raise ProvenanceError("taxonomy has no skills")
    matches = [skill for skill in skills if isinstance(skill, dict) and skill.get("skill_name") == skill_name]
    if len(matches) != 1:
        raise ProvenanceError(f"unknown or duplicate taxonomy skill: {skill_name}")
    audit_rows = _load_jsonl(repo / "research/essay-audit.jsonl")
    projection_rows = _load_jsonl(repo / "research/essay-theme-map.jsonl")
    audit = _indexed(audit_rows, "canonical audit")
    projection = _indexed(projection_rows, "theme projection")
    evidence_path = repo / "skills" / skill_name / "references/evidence.json"
    evidence_document = _load_json(evidence_path)
    if not isinstance(evidence_document, dict):
        raise ProvenanceError(f"skill evidence must be an object: {evidence_path}")
    expected = _render(matches[0], audit, projection, evidence_document)
    output = repo / "skills" / skill_name / "references/provenance.md"
    if check:
        try:
            actual = output.read_text(encoding="utf-8")
        except OSError as exc:
            raise ProvenanceError(f"missing skill provenance: {output}") from exc
        if actual != expected:
            raise ProvenanceError(f"skill provenance is stale: {output}")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(expected, encoding="utf-8")
    return {"essays": len(matches[0]["essay_ids"]), "themes": len(matches[0]["themes"])}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_name")
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        proof = build(args.repo, args.skill_name, check=args.check)
    except ProvenanceError as exc:
        print(f"skill provenance failed: {exc}")
        return 1
    action = "check" if args.check else "written"
    print(f"skill provenance {action}: " + " ".join(f"{key}={value}" for key, value in proof.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
