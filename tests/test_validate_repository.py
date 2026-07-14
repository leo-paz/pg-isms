import json
import tempfile
import unittest
from pathlib import Path

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
        path.write_text("".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")

    def audit_records(self) -> list[dict]:
        path = self.repo / "research/essay-audit.jsonl"
        return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]

    def write_audit_records(self, records: list[dict]) -> None:
        path = self.repo / "research/essay-audit.jsonl"
        path.write_text("".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")

    def add_valid_taxonomy(self) -> None:
        self.add_valid_audit()
        taxonomy = {
            "skills": [
                {
                    "skill_name": "test-startup-judgment",
                    "purpose": "Apply evidence to a startup decision.",
                    "triggers": ["Choose between startup approaches."],
                    "non_triggers": ["Summarize an unrelated essay."],
                    "themes": ["testing startup judgment"],
                    "essay_ids": ["001"],
                    "stage_conditions": ["Use before committing scarce resources."],
                    "tensions": ["Speed versus confidence."],
                    "candidate_eval_cases": ["Compare two launch strategies."],
                }
            ]
        }
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
            'interface:\n  display_name: "Test Startup Judgment"\n  short_description: "Compare startup choices"\n  default_prompt: "Use $test-startup-judgment to compare these choices."\n'
        )
        eval_dir = self.repo / "evals/test-startup-judgment"
        (eval_dir / "baseline").mkdir(parents=True)
        (eval_dir / "forward").mkdir()
        (eval_dir / "cases.json").write_text(
            json.dumps(
                {
                    "cases": [
                        {"type": "trigger", "prompt": "Compare two launch strategies."},
                        {"type": "non-trigger", "prompt": "Summarize an unrelated essay."},
                        {"type": "application", "prompt": "Apply the workflow to a launch choice."},
                        {"type": "condition", "prompt": "Decide under a severe time constraint."},
                        {"type": "edge", "prompt": "Handle contradictory customer evidence."},
                    ]
                },
                indent=2,
            )
            + "\n"
        )
        (eval_dir / "baseline/result.md").write_text("# Baseline\n\nReviewer: baseline-agent\n\nGap observed.\n")
        (eval_dir / "forward/result.md").write_text("# Forward\n\nReviewer: forward-agent\n\nImprovement observed.\n")
        (self.repo / "research/final-review.md").write_text(
            "# Independent final review\n\nReviewer: independent-agent\n\nStatus: complete\n"
        )
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

    def test_rejects_taxonomy_coverage_gap(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_taxonomy()
        taxonomy_path = fixture.repo / "research/taxonomy.json"
        taxonomy = json.loads(taxonomy_path.read_text())
        taxonomy["skills"][0]["essay_ids"] = []
        taxonomy_path.write_text(json.dumps(taxonomy))

        self.assert_invalid(fixture, "taxonomy", "coverage gap|not covered")

    def test_rejects_missing_skill_package_metadata(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        (fixture.repo / "skills/test-startup-judgment/agents/openai.yaml").unlink()

        self.assert_invalid(fixture, "final", "openai.yaml")

    def test_rejects_missing_evaluation_evidence(self) -> None:
        temp_dir, fixture = self.fixture()
        self.addCleanup(temp_dir.cleanup)
        fixture.add_valid_final()
        (fixture.repo / "evals/test-startup-judgment/baseline/result.md").unlink()

        self.assert_invalid(fixture, "final", "baseline evaluation")

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
