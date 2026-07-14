import json
import tempfile
import unittest
from pathlib import Path

from scripts.build_theme_projection import build as build_theme_projection
from scripts.build_research_scaffold import build_research_scaffold
from scripts.validate_repository import ValidationError, validate_repository


CLASSIFICATIONS = {"core startup", "supporting startup", "excluded"}


class RepositoryFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.repo = root / "repo"
        self.corpus = root / "corpus"
        self.repo.mkdir()
        self.corpus.mkdir()
        for article_no in range(1, 224):
            tokens = " ".join(f"unique{article_no}token{index}" for index in range(1, 71))
            (self.corpus / f"{article_no:03d}_essay-{article_no}.md").write_text(
                "\n".join(
                    [
                        "---",
                        f'title: "Essay {article_no}"',
                        f'article_no: "{article_no:03d}"',
                        f'source_url: "https://example.com/{article_no}"',
                        "---",
                        "",
                        f"# Essay {article_no}",
                        "",
                        tokens,
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
        build_research_scaffold(self.corpus, self.repo, batch_count=12)

    def add_valid_audit(self) -> None:
        batch_data = json.loads((self.repo / "research/audit-batches.json").read_text())
        batch_for_article = {
            article_no: batch["batch_id"]
            for batch in batch_data["batches"]
            for article_no in batch["article_nos"]
        }
        records = []
        for article_no in range(1, 224):
            relevant = article_no == 1
            records.append(
                {
                    "article_no": f"{article_no:03d}",
                    "title": f"Essay {article_no}",
                    "source_url": f"https://example.com/{article_no}",
                    "corpus_path": f"{article_no:03d}_essay-{article_no}.md",
                    "classification": "core startup" if relevant else "excluded",
                    "exclusion_reason": "" if relevant else "Focuses on a non-startup subject without a reusable startup decision.",
                    "themes": ["testing startup judgment"] if relevant else [],
                    "candidate_workflows": ["evaluate a startup choice"] if relevant else [],
                    "final_skills": ["test-startup-judgment"] if relevant else [],
                    "evidence_line_ranges": ["7-9"] if relevant else [],
                    "review_batch": batch_for_article[f"{article_no:03d}"],
                    "reviewer": "fixture-reviewer",
                    "full_text_read": True,
                }
            )
        path = self.repo / "research/essay-audit.jsonl"
        path.write_text(
            "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
            encoding="utf-8",
        )
        (self.repo / "research/batches").mkdir(exist_ok=True)
        records_by_batch = {batch["batch_id"]: [] for batch in batch_data["batches"]}
        for record in records:
            records_by_batch[record["review_batch"]].append(record)
        for batch_id, batch_records in records_by_batch.items():
            batch_path = self.repo / "research/batches" / f"{batch_id}.jsonl"
            batch_path.write_text(
                "".join(json.dumps(record, sort_keys=True) + "\n" for record in batch_records),
                encoding="utf-8",
            )

    def audit_records(self) -> list[dict]:
        path = self.repo / "research/essay-audit.jsonl"
        return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]

    def write_audit_records(self, records: list[dict]) -> None:
        path = self.repo / "research/essay-audit.jsonl"
        path.write_text(
            "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
            encoding="utf-8",
        )

    def add_valid_taxonomy(self) -> None:
        self.add_valid_audit()
        audit_records = self.audit_records()
        article_002 = next(record for record in audit_records if record["article_no"] == "002")
        audit_reclassifications = {
            "schema_version": 1,
            "corrections": [
                {
                    "article_no": "002",
                    "previous_classification": "supporting startup",
                    **{
                        field: article_002[field]
                        for field in (
                            "classification",
                            "exclusion_reason",
                            "themes",
                            "candidate_workflows",
                            "evidence_line_ranges",
                        )
                    },
                }
            ],
        }
        (self.repo / "research/audit-reclassifications.json").write_text(
            json.dumps(audit_reclassifications, indent=2) + "\n", encoding="utf-8"
        )
        revision_note = (
            "Checkpoint 3 semantic routing review split broad equity, adversarial, network-effect, "
            "and policy labels by actor or mechanism and added mappings for five reopened essays."
        )
        normalization = {
            "schema_version": 1,
            "method_notes": [
                "Raw audit labels remain intact while taxonomy uses canonical research themes.",
                revision_note,
            ],
            "canonical_themes": [
                {
                    "name": "startup judgment",
                    "definition": "Evidence-guided judgment for consequential startup choices.",
                }
            ],
            "mappings": [
                {
                    "raw_theme": "testing startup judgment",
                    "canonical_themes": ["startup judgment"],
                    "reviewer": "normalization-reviewer",
                }
            ],
        }
        (self.repo / "research/theme-normalization.json").write_text(
            json.dumps(normalization, indent=2) + "\n", encoding="utf-8"
        )
        normalization_revisions = {
            "schema_version": 1,
            "remove_canonical_themes": [],
            "add_canonical_themes": [],
            "replace_mappings": [],
            "replace_article_overrides": [],
            "add_mappings": [],
        }
        (self.repo / "research/normalization-revisions.json").write_text(
            json.dumps(normalization_revisions, indent=2) + "\n", encoding="utf-8"
        )
        build_theme_projection(self.repo)
        skill = {
            "skill_name": "test-startup-judgment",
            "purpose": "Apply evidence to a startup decision.",
            "triggers": ["Choose between startup approaches."],
            "non_triggers": ["Summarize an unrelated essay."],
            "themes": ["startup judgment"],
            "essay_ids": [],
            "stage_conditions": [
                "Use before committing scarce resources.",
                "Raise the evidence gate when the choice is irreversible.",
            ],
            "tensions": ["Speed versus confidence.", "Action versus preserving options."],
            "candidate_eval_cases": ["Compare two launch strategies."],
        }
        invariant_ids = [
            "stage-and-state",
            "reversibility-and-error-cost",
            "evidence-latency",
            "product-and-venture-type",
            "truth-character-and-user-effects",
            "historical-revalidation",
            "preserve-optionality",
        ]
        product_types = [
            "capital-light-software",
            "enterprise-and-integration",
            "hardware",
            "biotech-energy-and-capital-heavy",
            "marketplace-and-community",
            "high-harm-regulated-product",
        ]
        routing_ids = [
            "opportunity-learning-growth",
            "marketplace-cold-start",
            "survival-before-capital",
            "domain-before-communication",
            "writing-before-persuasion",
            "location-versus-ecosystem",
            "selection-versus-support",
            "technical-structure-versus-release",
            "residual-calibration",
        ]
        taxonomy_source = {
            "expected_counts": {
                "skills": 1,
                "stage_conditions": 2,
                "decision_branches": 2,
            },
            "global_invariants": [
                {
                    "id": invariant_id,
                    "rule": "Apply the invariant before choosing the branch.",
                    "source_themes": ["startup judgment"],
                }
                for invariant_id in invariant_ids
            ],
            "product_type_matrix": [
                {
                    "type": product_type,
                    "evidence_latency": "Match the observation interval to credible evidence.",
                    "launch_gate": "Match the release gate to expected harm.",
                    "manual_test": "Use the smallest discriminating bounded test.",
                    "capital_runway": "Model the runway implied by this product type.",
                    "acquisition": "Choose acquisition only after defining the evidence state.",
                    "invalid_default_advice": "Do not apply a context-free default.",
                }
                for product_type in product_types
            ],
            "routing_rules": [
                {
                    "id": routing_id,
                    "predicate": "Route the decision to its primary owner before composing another skill.",
                    "primary_sequence": ["test-startup-judgment"],
                }
                for routing_id in routing_ids
            ],
            "evaluation_branch_contract": [
                "Test both sides of every tension.",
                "Include triggers, non-triggers, conditions, applications, and edges.",
                "Use fresh evaluators for baseline and forward evidence.",
            ],
            "decision_branches": {
                "test-startup-judgment": [
                    {
                        "tension": "Speed versus confidence.",
                        "predicate": "If the choice is cheap and reversible, then act quickly; otherwise require stronger evidence before committing.",
                        "true_case": "A reversible internal experiment can produce evidence within one working day.",
                        "false_case": "An irreversible customer migration needs stronger evidence and a rollback plan.",
                    },
                    {
                        "tension": "Action versus preserving options.",
                        "predicate": "If one option dominates on current evidence, then commit deliberately; otherwise preserve alternatives while running a discriminating test.",
                        "true_case": "A tested branch clearly dominates and delay now destroys meaningful value.",
                        "false_case": "Evidence remains ambiguous and a short test can preserve both options.",
                    },
                ]
            },
            "skills": [
                skill
            ]
        }
        (self.repo / "research/taxonomy-source.json").write_text(
            json.dumps(taxonomy_source, indent=2) + "\n", encoding="utf-8"
        )
        taxonomy = json.loads(json.dumps(taxonomy_source))
        taxonomy["skills"][0]["essay_ids"] = ["001"]
        (self.repo / "research/taxonomy.json").write_text(json.dumps(taxonomy, indent=2) + "\n")
        (self.repo / "research/theme-synthesis.md").write_text(
            "# Theme synthesis\n\nEvidence-backed startup judgment is the initial test theme.\n"
        )

    def add_valid_final(self) -> None:
        self.add_valid_taxonomy()
        skill = self.repo / "skills/test-startup-judgment"
        (skill / "agents").mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            "---\nname: test-startup-judgment\ndescription: Use when comparing consequential startup choices.\n---\n\n# Test Startup Judgment\n\nCompare evidence before committing.\n"
        )
        (skill / "agents/openai.yaml").write_text(
            'interface:\n  display_name: "Test Startup Judgment"\n  short_description: "Compare consequential startup choices"\n  default_prompt: "Use $test-startup-judgment to compare these choices."\n'
        )
        eval_dir = self.repo / "evals/test-startup-judgment"
        (eval_dir / "baseline").mkdir(parents=True)
        (eval_dir / "forward").mkdir()
        cases = [
            {"id": "trigger", "type": "trigger", "prompt": "Compare two launch strategies.", "criteria": ["Recognizes the skill applies."]},
            {"id": "non-trigger", "type": "non-trigger", "prompt": "Summarize an unrelated essay.", "criteria": ["Does not force the workflow."]},
            {"id": "application", "type": "application", "prompt": "Apply the workflow to a launch choice.", "criteria": ["Uses relevant evidence."]},
            {"id": "condition", "type": "condition", "prompt": "Decide under a severe time constraint.", "criteria": ["Handles the stated condition."]},
            {"id": "edge", "type": "edge", "prompt": "Handle contradictory customer evidence.", "criteria": ["Addresses contradictory evidence."]},
        ]
        (eval_dir / "cases.json").write_text(json.dumps({"schema_version": 1, "cases": cases}, indent=2) + "\n")
        case_ids = [case["id"] for case in cases]
        for phase, reviewer, score in (("baseline", "baseline-agent", 1), ("forward", "forward-agent", 4)):
            for case_id in case_ids:
                (eval_dir / phase / f"{case_id}.md").write_text(
                    f"# Raw evaluation output\n\nCase ID: {case_id}\n\nReviewer ID: {reviewer}\n\n"
                    f"This is the complete raw agent response captured for the {case_id} evaluation scenario.\n"
                )
            summary = {
                "schema_version": 1,
                "skill_name": "test-startup-judgment",
                "phase": phase,
                "reviewer_id": reviewer,
                "case_results": [
                    {"case_id": case_id, "score": score, "max_score": 5, "raw_output": f"{case_id}.md"}
                    for case_id in case_ids
                ],
            }
            (eval_dir / phase / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
        final_review_sections = [
            "Missing principles",
            "Overlap/gaps",
            "Contradictions",
            "Stage-dependent advice",
            "Triggering quality",
            "Copyright hygiene",
        ]
        review = "# Independent final review\n\nReviewer: independent-agent\n\nStatus: complete\n"
        for category in final_review_sections:
            review += (
                f"\n## {category}\n\n"
                "Severity: none\n\n"
                "Disposition: no-findings\n\n"
                "Evidence: The reviewer inspected the canonical research and skill artifacts for this category.\n\n"
                "Affected essays/skills: none\n\n"
                "Proposed remedy: none required\n\n"
                "Verification: The applicable repository evidence was checked independently.\n"
            )
        (self.repo / "research/final-review.md").write_text(review)
        (self.repo / "README.md").write_text(
            "# Skills\n\n- [Test Startup Judgment](skills/test-startup-judgment/)\n"
        )


class ValidateRepositoryTests(unittest.TestCase):
    def fixture(self) -> tuple[tempfile.TemporaryDirectory, RepositoryFixture]:
        temp_dir = tempfile.TemporaryDirectory()
        return temp_dir, RepositoryFixture(Path(temp_dir.name))

    def assert_invalid(self, fixture: RepositoryFixture, phase: str, expected: str) -> None:
        with self.assertRaisesRegex(ValidationError, expected):
            validate_repository(fixture.repo, fixture.corpus, phase)

    def test_valid_manifest_prints_count_based_proof(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)

        proof = validate_repository(fixture.repo, fixture.corpus, "manifest")

        self.assertEqual(223, proof["corpus_files"])
        self.assertEqual(223, proof["unique_assignments"])
        self.assertEqual(12, proof["batches"])
        self.assertEqual(0, proof["gaps"])
        self.assertEqual(0, proof["overlaps"])

    def test_rejects_missing_essay(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        manifest_path = fixture.repo / "research/corpus-manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["essays"].pop()
        manifest["document_count"] -= 1
        manifest_path.write_text(json.dumps(manifest))

        self.assert_invalid(fixture, "manifest", "missing.*essay|manifest.*corpus")

    def test_rejects_duplicate_article_number(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        manifest_path = fixture.repo / "research/corpus-manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["essays"].append(dict(manifest["essays"][0]))
        manifest["document_count"] += 1
        manifest_path.write_text(json.dumps(manifest))

        self.assert_invalid(fixture, "manifest", "duplicate article")

    def test_rejects_invalid_classification(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_audit()
        records = fixture.audit_records()
        records[0]["classification"] = "maybe relevant"
        fixture.write_audit_records(records)

        self.assert_invalid(fixture, "audit", "invalid classification")

    def test_rejects_excluded_essay_without_specific_reason(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_audit()
        records = fixture.audit_records()
        records[1]["exclusion_reason"] = ""
        fixture.write_audit_records(records)

        self.assert_invalid(fixture, "audit", "specific exclusion reason")

    def test_rejects_relevant_essay_without_themes_or_evidence(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_audit()
        records = fixture.audit_records()
        records[0]["themes"] = []
        records[0]["evidence_line_ranges"] = []
        fixture.write_audit_records(records)

        self.assert_invalid(fixture, "audit", "themes.*evidence|evidence.*themes")

    def test_audit_phase_does_not_require_theme_projection(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_audit()

        proof = validate_repository(fixture.repo, fixture.corpus, "audit")

        self.assertEqual(223, proof["classified"])
        self.assertFalse((fixture.repo / "research/essay-theme-map.jsonl").exists())

    def test_rejects_taxonomy_coverage_gap(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_taxonomy()
        taxonomy_path = fixture.repo / "research/taxonomy.json"
        taxonomy = json.loads(taxonomy_path.read_text())
        taxonomy["skills"][0]["essay_ids"] = []
        taxonomy_path.write_text(json.dumps(taxonomy))

        self.assert_invalid(fixture, "taxonomy", "coverage gap|not covered|essay_ids are stale")

    def test_rejects_taxonomy_when_primary_batch_mapping_is_stale(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_taxonomy()
        batch_path = fixture.repo / "research/batches/batch-01.jsonl"
        records = [json.loads(line) for line in batch_path.read_text().splitlines()]
        records[0]["final_skills"] = []
        batch_path.write_text("".join(json.dumps(record) + "\n" for record in records))

        self.assert_invalid(fixture, "taxonomy", "batch.*stale|stale.*batch|canonical audit.*batch")

    def test_rejects_canonical_audit_drift_from_primary_batch(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_taxonomy()
        records = fixture.audit_records()
        records[0]["candidate_workflows"] = ["canonical-only drift"]
        fixture.write_audit_records(records)

        self.assert_invalid(fixture, "taxonomy", "canonical audit.*batch|batch.*canonical audit")

    def test_rejects_taxonomy_without_required_taxonomy_source(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_taxonomy()
        (fixture.repo / "research/taxonomy-source.json").unlink()

        self.assert_invalid(fixture, "taxonomy", "taxonomy source|taxonomy-source")

    def test_rejects_taxonomy_without_audit_reclassification_source(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_taxonomy()
        (fixture.repo / "research/audit-reclassifications.json").unlink()

        self.assert_invalid(fixture, "taxonomy", "audit reclassification.*missing|missing.*audit reclassification")

    def test_rejects_taxonomy_without_normalization_revision_source(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_taxonomy()
        (fixture.repo / "research/normalization-revisions.json").unlink()

        self.assert_invalid(fixture, "taxonomy", "normalization revision.*missing|missing.*normalization revision")

    def test_taxonomy_uses_canonical_projection_themes_instead_of_raw_audit_labels(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_taxonomy()

        proof = validate_repository(fixture.repo, fixture.corpus, "taxonomy")

        self.assertEqual(1, proof["skills"])

    def test_rejects_taxonomy_themes_missing_a_canonical_projection_theme(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_taxonomy()
        taxonomy_path = fixture.repo / "research/taxonomy.json"
        taxonomy = json.loads(taxonomy_path.read_text())
        taxonomy["skills"][0]["themes"] = ["unrelated placeholder"]
        taxonomy_path.write_text(json.dumps(taxonomy))

        self.assert_invalid(
            fixture,
            "taxonomy",
            "canonical themes|theme coverage|taxonomy synchronization|essay_ids are stale",
        )

    def test_rejects_taxonomy_when_theme_projection_is_absent(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_taxonomy()
        (fixture.repo / "research/essay-theme-map.jsonl").unlink()

        self.assert_invalid(fixture, "taxonomy", "theme projection.*missing|missing.*essay-theme-map")

    def test_rejects_taxonomy_when_theme_projection_is_stale(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_taxonomy()
        normalization_path = fixture.repo / "research/theme-normalization.json"
        normalization = json.loads(normalization_path.read_text())
        normalization["canonical_themes"][0]["name"] = "startup decision quality"
        normalization["mappings"][0]["canonical_themes"] = ["startup decision quality"]
        normalization_path.write_text(json.dumps(normalization, indent=2) + "\n")

        self.assert_invalid(fixture, "taxonomy", "theme projection.*stale|stale.*projection")

    def test_rejects_taxonomy_when_theme_projection_is_corrupt(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_taxonomy()
        (fixture.repo / "research/essay-theme-map.jsonl").write_text("{not-json}\n")

        self.assert_invalid(fixture, "taxonomy", "theme projection.*invalid|invalid JSONL")

    def test_rejects_missing_skill_package_metadata(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        (fixture.repo / "skills/test-startup-judgment/agents/openai.yaml").unlink()

        self.assert_invalid(fixture, "final", "openai.yaml")

    def test_rejects_malformed_skill_frontmatter(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        skill = fixture.repo / "skills/test-startup-judgment/SKILL.md"
        skill.write_text(
            '---\nname: test-startup-judgment\ndescription: "Use when comparing choices.\n---\n\n# Test Startup Judgment\n\nCompare evidence.\n'
        )

        self.assert_invalid(fixture, "final", "invalid YAML|frontmatter")

    def test_rejects_indented_opening_frontmatter_delimiter(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        skill = fixture.repo / "skills/test-startup-judgment/SKILL.md"
        skill.write_text(
            "  ---\nname: test-startup-judgment\ndescription: Use when comparing choices.\n---\n\n"
            "# Test Startup Judgment\n\nCompare evidence.\n"
        )

        self.assert_invalid(fixture, "final", "frontmatter|opening delimiter")

    def test_rejects_indented_closing_frontmatter_delimiter(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        skill = fixture.repo / "skills/test-startup-judgment/SKILL.md"
        skill.write_text(
            "---\nname: test-startup-judgment\ndescription: Use when comparing choices.\n  ---\n\n"
            "# Test Startup Judgment\n\nCompare evidence.\n"
        )

        self.assert_invalid(fixture, "final", "frontmatter|closing delimiter")

    def test_rejects_internal_tab_in_plain_skill_scalar(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        skill = fixture.repo / "skills/test-startup-judgment/SKILL.md"
        skill.write_text(
            "---\nname: test-startup-judgment\ndescription: Use when comparing\tchoices.\n---\n\n"
            "# Test Startup Judgment\n\nCompare evidence.\n"
        )

        self.assert_invalid(fixture, "final", "tab|non-printable|invalid YAML")

    def test_rejects_unquoted_skill_scalar_containing_colon_space(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        skill = fixture.repo / "skills/test-startup-judgment/SKILL.md"
        skill.write_text(
            "---\nname: test-startup-judgment\ndescription: Use when comparing: choices.\n---\n\n"
            "# Test Startup Judgment\n\nCompare evidence.\n"
        )

        self.assert_invalid(fixture, "final", "invalid YAML|quote.*colon")

    def test_rejects_unquoted_skill_scalar_ending_in_colon(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        skill = fixture.repo / "skills/test-startup-judgment/SKILL.md"
        skill.write_text(
            "---\nname: test-startup-judgment\ndescription: Use when comparing:\n---\n\n"
            "# Test Startup Judgment\n\nCompare evidence.\n"
        )

        self.assert_invalid(fixture, "final", "invalid YAML|quote.*colon")

    def test_rejects_malformed_openai_yaml(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        metadata = fixture.repo / "skills/test-startup-judgment/agents/openai.yaml"
        metadata.write_text(
            'interface:\n display_name: "Test Startup Judgment"\n short_description: "Compare consequential startup choices"\n default_prompt: "Use $test-startup-judgment to compare these choices."\n'
        )

        self.assert_invalid(fixture, "final", "invalid.*openai.yaml|openai.yaml.*invalid")

    def test_rejects_single_quoted_scalar_with_unescaped_apostrophe(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        metadata = fixture.repo / "skills/test-startup-judgment/agents/openai.yaml"
        metadata.write_text(
            "interface:\n"
            "  display_name: 'Founder's Choice'\n"
            "  short_description: \"Compare consequential startup choices\"\n"
            "  default_prompt: \"Use $test-startup-judgment to compare these choices.\"\n"
        )

        self.assert_invalid(fixture, "final", "invalid YAML|unescaped.*apostrophe")

    def test_rejects_non_printable_control_character_in_quoted_scalar(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        metadata = fixture.repo / "skills/test-startup-judgment/agents/openai.yaml"
        metadata.write_text(
            "interface:\n"
            "  display_name: 'Founder\x01Choice'\n"
            "  short_description: \"Compare consequential startup choices\"\n"
            "  default_prompt: \"Use $test-startup-judgment to compare these choices.\"\n"
        )

        self.assert_invalid(fixture, "final", "non-printable|control character|invalid YAML")

    def test_rejects_missing_evaluation_evidence(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        (fixture.repo / "evals/test-startup-judgment/baseline/summary.json").unlink()

        self.assert_invalid(fixture, "final", "baseline evaluation")

    def test_rejects_evaluations_without_material_improvement(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        summary_path = fixture.repo / "evals/test-startup-judgment/forward/summary.json"
        summary = json.loads(summary_path.read_text())
        for case_result in summary["case_results"]:
            case_result["score"] = 1
        summary_path.write_text(json.dumps(summary))

        self.assert_invalid(fixture, "final", "material improvement")

    def test_rejects_reused_baseline_and_forward_reviewer_ids(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        summary_path = fixture.repo / "evals/test-startup-judgment/forward/summary.json"
        summary = json.loads(summary_path.read_text())
        summary["reviewer_id"] = "baseline-agent"
        summary_path.write_text(json.dumps(summary))
        for raw_path in (fixture.repo / "evals/test-startup-judgment/forward").glob("*.md"):
            raw_path.write_text(raw_path.read_text().replace("Reviewer ID: forward-agent", "Reviewer ID: baseline-agent"))

        self.assert_invalid(fixture, "final", "fresh reviewer|reuse.*reviewer")

    def test_rejects_evaluation_summary_with_missing_raw_artifact(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        summary_path = fixture.repo / "evals/test-startup-judgment/forward/summary.json"
        summary = json.loads(summary_path.read_text())
        summary["case_results"][0]["raw_output"] = "missing.md"
        summary_path.write_text(json.dumps(summary))

        self.assert_invalid(fixture, "final", "raw output")

    def test_rejects_unsupported_extra_evaluation_case_type(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        cases_path = fixture.repo / "evals/test-startup-judgment/cases.json"
        cases = json.loads(cases_path.read_text())
        cases["cases"].append(
            {
                "id": "unsupported",
                "type": "surprise",
                "prompt": "Run an unsupported evaluation type.",
                "criteria": ["This type must be rejected."],
            }
        )
        cases_path.write_text(json.dumps(cases))

        self.assert_invalid(fixture, "final", "unsupported evaluation case type|invalid.*case type")

    def test_rejects_incomplete_final_review_categories(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        review_path = fixture.repo / "research/final-review.md"
        review = review_path.read_text()
        review = review.replace("## Copyright hygiene", "## Other review")
        review_path.write_text(review)

        self.assert_invalid(fixture, "final", "final review.*categories|missing.*copyright hygiene")

    def test_rejects_stale_readme_catalog_entries(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        readme = fixture.repo / "README.md"
        readme.write_text(readme.read_text() + "- [Stale](skills/stale-skill/)\n")

        self.assert_invalid(fixture, "final", "README.*stale|stale.*README")

    def test_rejects_duplicate_readme_catalog_entries(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        readme = fixture.repo / "README.md"
        readme.write_text(readme.read_text() + "- [Duplicate](skills/test-startup-judgment/)\n")

        self.assert_invalid(fixture, "final", "README.*duplicate|duplicate.*README")

    def test_rejects_unexpected_long_source_excerpt(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        reference = fixture.repo / "skills/test-startup-judgment/references/provenance.md"
        reference.parent.mkdir()
        source_text = (fixture.corpus / "001_essay-1.md").read_text().splitlines()[-1]
        reference.write_text("# Provenance\n\n" + source_text + "\n")

        self.assert_invalid(fixture, "final", "long source excerpt")

    def test_valid_final_fixture_passes_without_git_checkout(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()

        proof = validate_repository(fixture.repo, fixture.corpus, "final")

        self.assertEqual(1, proof["skills"])
        self.assertEqual(1, proof["baseline_evaluations"])
        self.assertEqual(1, proof["forward_evaluations"])
        self.assertEqual(0, proof["long_source_excerpts"])


if __name__ == "__main__":
    unittest.main()
