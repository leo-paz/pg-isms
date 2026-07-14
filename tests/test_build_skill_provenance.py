import json
import tempfile
import unittest
from pathlib import Path

from scripts.build_skill_provenance import ProvenanceError, build


class BuildSkillProvenanceTests(unittest.TestCase):
    def _write_fixture(self, repo: Path) -> None:
        (repo / "research").mkdir()
        (repo / "skills/test-skill/references").mkdir(parents=True)
        taxonomy = {
            "skills": [{
                "skill_name": "test-skill",
                "purpose": "Make a test decision.",
                "triggers": ["Make the decision."],
                "non_triggers": ["Do unrelated work."],
                "themes": ["test-theme"],
                "essay_ids": ["001"],
                "stage_conditions": ["Use at the test stage."],
                "tensions": ["Speed versus evidence."],
            }]
        }
        audit = {
            "article_no": "001", "title": "A Test Essay",
            "source_url": "https://example.com/test", "corpus_path": "001_test.md",
            "review_batch": "batch-01", "reviewer": "audit-reviewer",
            "final_skills": ["test-skill"], "evidence_line_ranges": ["10-20", "30-40"],
        }
        projection = {"article_no": "001", "canonical_themes": ["test-theme", "other-theme"]}
        evidence = {
            "schema_version": 1, "skill_name": "test-skill",
            "records": [{
                "skill_name": "test-skill", "article_no": "001",
                "reviewer": "skill-evidence-reviewer",
                "theme_evidence": [{
                    "canonical_theme": "test-theme", "line_ranges": ["12-14"],
                    "claim": "A narrow source claim supports this exact test workflow.",
                }],
            }],
        }
        (repo / "research/taxonomy.json").write_text(json.dumps(taxonomy), encoding="utf-8")
        (repo / "research/essay-audit.jsonl").write_text(json.dumps(audit) + "\n", encoding="utf-8")
        (repo / "research/essay-theme-map.jsonl").write_text(json.dumps(projection) + "\n", encoding="utf-8")
        (repo / "skills/test-skill/references/evidence.json").write_text(
            json.dumps(evidence, indent=2) + "\n", encoding="utf-8"
        )

    def test_builds_exact_skill_specific_provenance_and_checks_staleness(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo = Path(tempdir)
            self._write_fixture(repo)

            self.assertEqual({"essays": 1, "themes": 1}, build(repo, "test-skill"))
            output_path = repo / "skills/test-skill/references/provenance.md"
            output = output_path.read_text()
            self.assertIn("[A Test Essay](https://example.com/test)", output)
            self.assertIn("`12-14`", output)
            self.assertNotIn("`10-20`", output)
            self.assertNotIn("`30-40`", output)
            self.assertIn("`test-theme`", output)
            self.assertNotIn("`other-theme`", output)
            self.assertIn("`001_test.md`", output)
            self.assertIn("audit-reviewer / batch-01", output)

            build(repo, "test-skill", check=True)
            output_path.write_text("stale\n")
            with self.assertRaisesRegex(ProvenanceError, "stale"):
                build(repo, "test-skill", check=True)

    def test_rejects_duplicate_canonical_audit_rows(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo = Path(tempdir)
            self._write_fixture(repo)
            audit_path = repo / "research/essay-audit.jsonl"
            audit_path.write_text(audit_path.read_text() * 2)
            with self.assertRaisesRegex(ProvenanceError, "duplicate article numbers"):
                build(repo, "test-skill")

    def test_rejects_skill_range_outside_audited_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo = Path(tempdir)
            self._write_fixture(repo)
            evidence_path = repo / "skills/test-skill/references/evidence.json"
            evidence = json.loads(evidence_path.read_text())
            evidence["records"][0]["theme_evidence"][0]["line_ranges"] = ["21-22"]
            evidence_path.write_text(json.dumps(evidence))
            with self.assertRaisesRegex(ProvenanceError, "outside audited evidence"):
                build(repo, "test-skill")

    def test_rejects_nonreciprocal_skill_assignment(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo = Path(tempdir)
            self._write_fixture(repo)
            audit_path = repo / "research/essay-audit.jsonl"
            audit = json.loads(audit_path.read_text())
            audit["final_skills"] = ["another-skill"]
            audit_path.write_text(json.dumps(audit) + "\n")
            with self.assertRaisesRegex(ProvenanceError, "not reciprocal"):
                build(repo, "test-skill")


if __name__ == "__main__":
    unittest.main()
