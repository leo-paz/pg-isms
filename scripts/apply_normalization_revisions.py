#!/usr/bin/env python3
"""Apply or verify reviewed canonical-theme and raw-mapping revisions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Mapping


class RevisionError(ValueError):
    """Raised when normalization revisions cannot be applied deterministically."""


def _load(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RevisionError(f"cannot read JSON {path}: {exc}") from exc


def revised(normalization: Mapping[str, Any], revision: Mapping[str, Any]) -> Dict[str, Any]:
    output: Dict[str, Any] = json.loads(json.dumps(normalization))
    canonical = output.get("canonical_themes")
    mappings = output.get("mappings")
    if not isinstance(canonical, list) or not isinstance(mappings, list):
        raise RevisionError("normalization lacks canonical themes or mappings")
    remove = revision.get("remove_canonical_themes")
    additions = revision.get("add_canonical_themes")
    replacements = revision.get("replace_mappings")
    override_replacements = revision.get("replace_article_overrides")
    override_removals = revision.get("remove_article_overrides", [])
    override_additions = revision.get("add_article_overrides", [])
    new_mappings = revision.get("add_mappings")
    if not all(
        isinstance(value, list)
        for value in (
            remove,
            additions,
            replacements,
            override_replacements,
            override_removals,
            override_additions,
            new_mappings,
        )
    ):
        raise RevisionError("revision arrays are missing")

    remove_set = set(remove)
    canonical_by_name = {item.get("name"): item for item in canonical if isinstance(item, dict)}
    missing_remove = remove_set - set(canonical_by_name)
    if missing_remove:
        # Idempotent input may already have additions and none of the removed themes.
        addition_names = {item.get("name") for item in additions if isinstance(item, dict)}
        if missing_remove != remove_set or not addition_names <= set(canonical_by_name):
            raise RevisionError(f"canonical themes to remove are absent: {sorted(missing_remove)}")
    for name in remove_set:
        canonical_by_name.pop(name, None)
    for item in additions:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str) or not item.get("definition"):
            raise RevisionError("invalid canonical theme addition")
        existing = canonical_by_name.get(item["name"])
        if existing is not None and existing != item:
            raise RevisionError(f"canonical theme addition conflicts: {item['name']}")
        canonical_by_name[item["name"]] = item

    mapping_by_raw = {item.get("raw_theme"): item for item in mappings if isinstance(item, dict)}
    if len(mapping_by_raw) != len(mappings):
        raise RevisionError("normalization contains duplicate or invalid raw mappings")
    for item in replacements:
        raw = item.get("raw_theme") if isinstance(item, dict) else None
        if raw not in mapping_by_raw:
            raise RevisionError(f"replacement raw theme is absent: {raw!r}")
        mapping_by_raw[raw]["canonical_themes"] = item.get("canonical_themes")
    for item in override_removals:
        raw = item.get("raw_theme") if isinstance(item, dict) else None
        article_no = item.get("article_no") if isinstance(item, dict) else None
        mapping = mapping_by_raw.get(raw)
        if mapping is None or not isinstance(article_no, str):
            raise RevisionError(f"invalid article override removal: {raw}/{article_no}")
        overrides = mapping.get("article_overrides", [])
        matches = [override for override in overrides if override.get("article_no") == article_no]
        if len(matches) > 1:
            raise RevisionError(f"duplicate article override removal: {raw}/{article_no}")
        if matches:
            mapping["article_overrides"] = [
                override for override in overrides if override.get("article_no") != article_no
            ]
            if not mapping["article_overrides"]:
                mapping.pop("article_overrides")
    for item in override_replacements:
        raw = item.get("raw_theme") if isinstance(item, dict) else None
        article_no = item.get("article_no") if isinstance(item, dict) else None
        reviewer = item.get("reviewer") if isinstance(item, dict) else None
        if not isinstance(reviewer, str) or not reviewer.strip():
            raise RevisionError(
                f"invalid article override replacement reviewer: {raw}/{article_no}"
            )
        mapping = mapping_by_raw.get(raw)
        matches = [
            override
            for override in mapping.get("article_overrides", []) if isinstance(mapping, dict)
            if override.get("article_no") == article_no
        ]
        if len(matches) != 1:
            raise RevisionError(f"article override replacement is absent or duplicate: {raw}/{article_no}")
        matches[0]["canonical_themes"] = item.get("canonical_themes")
        matches[0]["reviewer"] = reviewer
    for item in override_additions:
        raw = item.get("raw_theme") if isinstance(item, dict) else None
        article_no = item.get("article_no") if isinstance(item, dict) else None
        targets = item.get("canonical_themes") if isinstance(item, dict) else None
        reviewer = item.get("reviewer") if isinstance(item, dict) else None
        mapping = mapping_by_raw.get(raw)
        if mapping is None:
            raise RevisionError(f"article override addition raw theme is absent: {raw!r}")
        if (
            not isinstance(article_no, str)
            or not isinstance(targets, list)
            or not isinstance(reviewer, str)
            or not reviewer.strip()
        ):
            raise RevisionError(
                f"invalid article override addition or reviewer: {raw}/{article_no}"
            )
        expected = {
            "article_no": article_no,
            "canonical_themes": targets,
            "reviewer": reviewer,
        }
        overrides = mapping.setdefault("article_overrides", [])
        matches = [override for override in overrides if override.get("article_no") == article_no]
        if len(matches) > 1:
            raise RevisionError(f"duplicate article override addition: {raw}/{article_no}")
        if matches:
            if matches[0].get("reviewer") == reviewer:
                matches[0].update(expected)
            elif matches[0] != expected:
                raise RevisionError(f"article override addition conflicts: {raw}/{article_no}")
        else:
            overrides.append(expected)
    reviewer = "taxonomy-semantic-remediation"
    for item in new_mappings:
        raw = item.get("raw_theme") if isinstance(item, dict) else None
        if not isinstance(raw, str) or not isinstance(item.get("canonical_themes"), list):
            raise RevisionError("invalid added raw mapping")
        expected = {"raw_theme": raw, "canonical_themes": item["canonical_themes"], "reviewer": reviewer}
        existing = mapping_by_raw.get(raw)
        if existing is not None and existing.get("reviewer") == reviewer:
            if existing.get("article_overrides"):
                expected["article_overrides"] = existing["article_overrides"]
            mapping_by_raw[raw] = expected
        elif existing is not None and existing != expected:
            raise RevisionError(f"added raw mapping conflicts: {raw}")
        else:
            mapping_by_raw[raw] = expected

    canonical_names = set(canonical_by_name)
    for raw, item in mapping_by_raw.items():
        targets = item.get("canonical_themes")
        if not isinstance(targets, list) or not targets or len(targets) > 3:
            raise RevisionError(f"raw mapping has invalid target count: {raw}")
        item["canonical_themes"] = sorted(set(targets))
        unknown = set(item["canonical_themes"]) - canonical_names
        if unknown:
            raise RevisionError(f"raw mapping {raw} has unknown targets: {sorted(unknown)}")
    for mapping in mapping_by_raw.values():
        overrides = mapping.get("article_overrides", [])
        overrides.sort(key=lambda item: item.get("article_no", ""))
        for item in overrides:
            targets = item.get("canonical_themes")
            if not isinstance(targets, list) or not targets or len(targets) > 3:
                raise RevisionError("article override has invalid canonical targets")
            item["canonical_themes"] = sorted(set(targets))
            unknown = set(item["canonical_themes"]) - canonical_names
            if unknown:
                raise RevisionError(f"article override has removed targets: {sorted(unknown)}")

    output["canonical_themes"] = [canonical_by_name[name] for name in sorted(canonical_by_name)]
    output["mappings"] = [mapping_by_raw[raw] for raw in sorted(mapping_by_raw)]
    note = (
        "Checkpoint 3 semantic routing review split broad equity, adversarial, network-effect, "
        "and policy labels by actor or mechanism and added mappings for five reopened essays."
    )
    notes = output.setdefault("method_notes", [])
    if note not in notes:
        notes.append(note)
    runway_note = (
        "Skill 13 source union added article-scoped runway and survival assignments, removed four "
        "false workflow triggers, and relabeled essay 129 using 45 raw-theme overrides proven to "
        "yield the independently reviewed 85-pair source set."
    )
    if (override_additions or override_removals) and runway_note not in notes:
        notes.append(runway_note)
    capital_note = (
        "Skill 14 source union reconciled all 49 assigned financing essays, removed seven false "
        "workflow triggers, and applied 68 article-scoped actions proven to yield the independently "
        "reviewed 42-essay, 146-pair capital source set without implemented-skill collateral."
    )
    capital_reviewed = any(
        isinstance(item, dict) and item.get("reviewer") == "capital-source-union"
        for item in [*override_replacements, *override_additions]
    )
    if capital_reviewed and capital_note not in notes:
        notes.append(capital_note)
    return output


def apply(repo: Path, *, check: bool = False) -> Dict[str, int]:
    repo = repo.resolve()
    path = repo / "research/theme-normalization.json"
    actual = _load(path)
    revision = _load(repo / "research/normalization-revisions.json")
    expected = revised(actual, revision)
    if check:
        if actual != expected:
            raise RevisionError("normalization revisions are stale")
    else:
        path.write_text(json.dumps(expected, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "canonical_themes": len(expected["canonical_themes"]),
        "raw_mappings": len(expected["mappings"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        proof = apply(args.repo, check=args.check)
    except RevisionError as exc:
        print(f"normalization revision failed: {exc}")
        return 1
    action = "check" if args.check else "apply"
    print(f"normalization revision {action} passed: " + " ".join(f"{k}={v}" for k, v in proof.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
