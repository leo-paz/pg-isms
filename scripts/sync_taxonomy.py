#!/usr/bin/env python3
"""Synchronize taxonomy coverage with the canonical theme projection and audit batches."""

from __future__ import annotations

import argparse
import copy
import json
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Set, Tuple

try:
    from .assemble_audit import assemble
except ImportError:  # Direct script execution.
    from assemble_audit import assemble


class SyncError(ValueError):
    """Raised when taxonomy inputs cannot produce an exact reciprocal mapping."""


REQUIRED_GLOBAL_INVARIANTS = {
    "stage-and-state",
    "reversibility-and-error-cost",
    "evidence-latency",
    "product-and-venture-type",
    "truth-character-and-user-effects",
    "historical-revalidation",
    "preserve-optionality",
}
REQUIRED_PRODUCT_TYPES = {
    "capital-light-software",
    "enterprise-and-integration",
    "hardware",
    "biotech-energy-and-capital-heavy",
    "marketplace-and-community",
    "high-harm-regulated-product",
}
REQUIRED_ROUTING_RULES = {
    "opportunity-learning-growth",
    "marketplace-cold-start",
    "survival-before-capital",
    "domain-before-communication",
    "writing-before-persuasion",
    "location-versus-ecosystem",
    "selection-versus-support",
    "technical-structure-versus-release",
    "residual-calibration",
}
EXPECTED_COUNT_FIELDS = {"skills", "stage_conditions", "decision_branches"}


def _exact_ids(values: Any, field: str, required: Set[str]) -> List[Mapping[str, Any]]:
    if not isinstance(values, list) or not all(isinstance(value, dict) for value in values):
        raise SyncError(f"runtime contract {field} must be an array of objects")
    ids = [value.get("id") for value in values]
    if len(ids) != len(set(ids)) or set(ids) != required:
        raise SyncError(f"runtime contract {field} are incomplete or duplicated")
    return values


def validate_runtime_contract(taxonomy: Mapping[str, Any]) -> Dict[str, int]:
    """Validate inherited invariants, product-type routing, and cross-skill composition."""
    skills = taxonomy.get("skills")
    if not isinstance(skills, list) or not skills:
        raise SyncError("runtime contract has no skills")
    skill_names = {
        skill.get("skill_name") for skill in skills if isinstance(skill, dict) and isinstance(skill.get("skill_name"), str)
    }
    if len(skill_names) != len(skills):
        raise SyncError("runtime contract has invalid or duplicate skill names")
    expected_counts = taxonomy.get("expected_counts")
    if not isinstance(expected_counts, dict) or set(expected_counts) != EXPECTED_COUNT_FIELDS:
        raise SyncError("runtime contract expected counts are incomplete")
    if not all(
        isinstance(expected_counts[field], int) and expected_counts[field] > 0
        for field in EXPECTED_COUNT_FIELDS
    ):
        raise SyncError("runtime contract expected counts must be positive integers")
    if expected_counts["skills"] != len(skills):
        raise SyncError("runtime contract skill count does not match expected counts")

    stage_condition_count = 0
    for skill in skills:
        stage_conditions = skill.get("stage_conditions")
        tensions = skill.get("tensions")
        if not isinstance(stage_conditions, list) or len(stage_conditions) != 2 or not all(
            isinstance(value, str) and value.strip() for value in stage_conditions
        ):
            raise SyncError(
                f"runtime contract requires exactly two stage conditions for {skill.get('skill_name')}"
            )
        if not isinstance(tensions, list) or len(tensions) != 2 or not all(
            isinstance(value, str) and value.strip() for value in tensions
        ):
            raise SyncError(f"runtime contract requires exactly two tensions for {skill.get('skill_name')}")
        stage_condition_count += len(stage_conditions)
    if stage_condition_count != expected_counts["stage_conditions"]:
        raise SyncError("runtime contract stage condition count does not match expected counts")

    invariants = _exact_ids(
        taxonomy.get("global_invariants"), "global invariants", REQUIRED_GLOBAL_INVARIANTS
    )
    for invariant in invariants:
        if not isinstance(invariant.get("rule"), str) or not invariant["rule"].strip():
            raise SyncError("runtime contract global invariants need executable rules")
        sources = invariant.get("source_themes")
        if not isinstance(sources, list) or not sources or not all(isinstance(item, str) for item in sources):
            raise SyncError("runtime contract global invariants need source themes")

    product_types = taxonomy.get("product_type_matrix")
    if not isinstance(product_types, list) or not all(isinstance(value, dict) for value in product_types):
        raise SyncError("runtime contract product types must be an array of objects")
    types = [value.get("type") for value in product_types]
    if len(types) != len(set(types)) or set(types) != REQUIRED_PRODUCT_TYPES:
        raise SyncError("runtime contract product types are incomplete or duplicated")
    product_fields = {
        "evidence_latency", "launch_gate", "manual_test", "capital_runway", "acquisition", "invalid_default_advice"
    }
    for row in product_types:
        if not all(isinstance(row.get(field), str) and row[field].strip() for field in product_fields):
            raise SyncError(f"runtime contract product type {row.get('type')} is incomplete")

    routing = _exact_ids(taxonomy.get("routing_rules"), "routing rules", REQUIRED_ROUTING_RULES)
    allowed = skill_names | {"domain-owner"}
    for rule in routing:
        if not isinstance(rule.get("predicate"), str) or not rule["predicate"].strip():
            raise SyncError("runtime contract routing rules need predicates")
        sequence = rule.get("primary_sequence")
        if not isinstance(sequence, list) or not sequence or not set(sequence) <= allowed:
            raise SyncError(f"runtime contract routing rule {rule.get('id')} has unknown skills")

    branch_contract = taxonomy.get("evaluation_branch_contract")
    if not isinstance(branch_contract, list) or len(branch_contract) < 3 or not all(
        isinstance(value, str) and value.strip() for value in branch_contract
    ):
        raise SyncError("runtime contract lacks an evaluation branch contract")
    branches = taxonomy.get("decision_branches")
    if not isinstance(branches, dict) or set(branches) != skill_names:
        raise SyncError("runtime contract decision branches do not cover the exact skill set")
    skill_by_name = {skill["skill_name"]: skill for skill in skills}
    branch_count = 0
    for skill_name, values in branches.items():
        tensions = skill_by_name[skill_name].get("tensions")
        if not isinstance(values, list) or not isinstance(tensions, list) or len(values) != len(tensions):
            raise SyncError(f"runtime contract decision branches do not match tensions for {skill_name}")
        if not all(isinstance(value, dict) for value in values):
            raise SyncError(f"runtime contract decision branches must be structured for {skill_name}")
        branch_tensions = [value.get("tension") for value in values]
        if branch_tensions != tensions or len(branch_tensions) != len(set(branch_tensions)):
            raise SyncError(f"runtime contract decision branch tensions do not match for {skill_name}")
        for value in values:
            predicate = value.get("predicate")
            if not (
                isinstance(predicate, str)
                and predicate.startswith("If ")
                and ", then " in predicate
                and "otherwise" in predicate.lower()
            ):
                raise SyncError(f"runtime contract decision branch predicate is not two-sided for {skill_name}")
            for side in ("true_case", "false_case"):
                example = value.get(side)
                if not isinstance(example, str) or len(example.split()) < 8:
                    raise SyncError(f"runtime contract decision branch {side} is incomplete for {skill_name}")
        branch_count += len(values)
    if branch_count != expected_counts["decision_branches"]:
        raise SyncError("runtime contract decision branch count does not match expected counts")
    return {
        "global_invariants": len(invariants),
        "product_types": len(product_types),
        "routing_rules": len(routing),
        "decision_branches": branch_count,
    }


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SyncError(f"cannot read JSON {path}: {exc}") from exc


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise SyncError(f"cannot read JSONL {path}: {exc}") from exc
    records: List[Dict[str, Any]] = []
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SyncError(f"invalid JSONL {path}:{line_number}: {exc}") from exc
        if not isinstance(value, dict):
            raise SyncError(f"JSONL record must be an object: {path}:{line_number}")
        records.append(value)
    return records


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, records: Iterable[Mapping[str, Any]]) -> None:
    path.write_text(
        "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
        encoding="utf-8",
    )


def derive(
    taxonomy: Mapping[str, Any],
    projection: Sequence[Mapping[str, Any]],
    canonical_themes: Set[str],
) -> Tuple[Dict[str, Any], Dict[str, List[str]]]:
    """Return taxonomy essay IDs and reciprocal essay skills derived from theme membership."""
    skills = taxonomy.get("skills")
    if not isinstance(skills, list) or not skills:
        raise SyncError("taxonomy must contain a non-empty skills array")
    copied: Dict[str, Any] = copy.deepcopy(dict(taxonomy))
    copied_skills = copied["skills"]

    assignments: Counter[str] = Counter()
    skill_themes: List[Tuple[str, Set[str]]] = []
    for index, skill in enumerate(copied_skills, start=1):
        if not isinstance(skill, dict):
            raise SyncError(f"taxonomy skill {index} must be an object")
        name = skill.get("skill_name")
        themes = skill.get("themes")
        if not isinstance(name, str) or not name or not isinstance(themes, list) or not themes:
            raise SyncError(f"taxonomy skill {index} needs a name and non-empty themes")
        if not all(isinstance(theme, str) and theme for theme in themes):
            raise SyncError(f"taxonomy skill {name} has invalid themes")
        assignments.update(themes)
        skill_themes.append((name, set(themes)))

    assigned = set(assignments)
    unknown = assigned - canonical_themes
    missing = canonical_themes - assigned
    duplicates = sorted(theme for theme, count in assignments.items() if count > 1)
    if unknown:
        raise SyncError(f"taxonomy contains unknown canonical themes: {sorted(unknown)}")
    if missing:
        raise SyncError(f"unassigned canonical themes: {sorted(missing)}")
    if duplicates:
        raise SyncError(f"canonical themes assigned to multiple skills: {duplicates}")

    essay_skills: Dict[str, List[str]] = {}
    essay_ids_by_skill: Dict[str, List[str]] = {name: [] for name, _ in skill_themes}
    seen_ids: Set[str] = set()
    for record in projection:
        article_no = record.get("article_no")
        themes = record.get("canonical_themes")
        if not isinstance(article_no, str) or not isinstance(themes, list) or not themes:
            raise SyncError("projection records need an article_no and non-empty canonical_themes")
        if article_no in seen_ids:
            raise SyncError(f"duplicate projection article: {article_no}")
        seen_ids.add(article_no)
        projected = set(themes)
        projected_unknown = projected - canonical_themes
        if projected_unknown:
            raise SyncError(f"projection contains unknown themes: {sorted(projected_unknown)}")
        names = [name for name, owned_themes in skill_themes if projected & owned_themes]
        if not names:
            raise SyncError(f"projection article {article_no} maps to no skill")
        essay_skills[article_no] = names
        for name in names:
            essay_ids_by_skill[name].append(article_no)

    for skill in copied_skills:
        skill["essay_ids"] = essay_ids_by_skill[skill["skill_name"]]
        if not skill["essay_ids"]:
            raise SyncError(f"taxonomy skill {skill['skill_name']} covers no essays")
    return copied, essay_skills


def _canonical_theme_names(normalization: Mapping[str, Any]) -> Set[str]:
    values = normalization.get("canonical_themes")
    if not isinstance(values, list):
        raise SyncError("normalization must contain canonical_themes")
    names = [value.get("name") for value in values if isinstance(value, dict)]
    if len(names) != len(values) or not all(isinstance(name, str) and name for name in names):
        raise SyncError("normalization has invalid canonical theme definitions")
    if len(set(names)) != len(names):
        raise SyncError("normalization has duplicate canonical theme names")
    return set(names)


def _expected_records(
    records: Sequence[Mapping[str, Any]], essay_skills: Mapping[str, List[str]]
) -> List[Dict[str, Any]]:
    expected: List[Dict[str, Any]] = []
    for source in records:
        record = dict(source)
        article_no = record.get("article_no")
        if not isinstance(article_no, str):
            raise SyncError("audit record has invalid article_no")
        record["final_skills"] = essay_skills.get(article_no, [])
        expected.append(record)
    return expected


def sync(repo: Path, *, check: bool = False) -> Dict[str, int]:
    """Synchronize or verify taxonomy essay coverage and audit final skill mappings."""
    repo = repo.resolve()
    research = repo / "research"
    taxonomy_path = research / "taxonomy.json"
    actual_taxonomy = _load_json(taxonomy_path)
    source_path = research / "taxonomy-source.json"
    if not source_path.is_file():
        raise SyncError(f"missing required taxonomy source: {source_path}")
    taxonomy = _load_json(source_path)
    contract_proof = validate_runtime_contract(taxonomy)
    projection = _load_jsonl(research / "essay-theme-map.jsonl")
    normalization = _load_json(research / "theme-normalization.json")
    expected_taxonomy, essay_skills = derive(
        taxonomy,
        projection,
        _canonical_theme_names(normalization),
    )

    batch_paths = sorted((research / "batches").glob("batch-*.jsonl"))
    if not batch_paths:
        raise SyncError("no primary audit batch files found")
    expected_batches: List[Tuple[Path, List[Dict[str, Any]], List[Dict[str, Any]]]] = []
    for path in batch_paths:
        actual = _load_jsonl(path)
        expected_batches.append((path, actual, _expected_records(actual, essay_skills)))
    canonical_path = research / "essay-audit.jsonl"
    actual_canonical = _load_jsonl(canonical_path)
    expected_canonical = _expected_records(actual_canonical, essay_skills)

    if check:
        if actual_taxonomy != expected_taxonomy:
            raise SyncError("taxonomy essay_ids are stale; run sync_taxonomy.py")
        stale_batches = [str(path) for path, actual, expected in expected_batches if actual != expected]
        if stale_batches:
            raise SyncError(f"audit batch final_skills are stale: {stale_batches}")
        if actual_canonical != expected_canonical:
            raise SyncError("canonical audit final_skills are stale; run sync_taxonomy.py")
    else:
        _write_json(taxonomy_path, expected_taxonomy)
        for path, _actual, expected in expected_batches:
            _write_jsonl(path, expected)
        assemble(repo)

    return {
        "skills": len(expected_taxonomy["skills"]),
        "themes": len(_canonical_theme_names(normalization)),
        "relevant_essays": len(essay_skills),
        "essay_skill_pairings": sum(len(names) for names in essay_skills.values()),
        **contract_proof,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        proof = sync(args.repo, check=args.check)
    except SyncError as exc:
        print(f"taxonomy synchronization failed: {exc}")
        return 1
    action = "check" if args.check else "sync"
    print(f"taxonomy {action} passed: " + " ".join(f"{key}={value}" for key, value in proof.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
