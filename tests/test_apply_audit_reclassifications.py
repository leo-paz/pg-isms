import json
import tempfile
import unittest
from pathlib import Path

from scripts.apply_audit_reclassifications import ReclassificationError, apply
from scripts.assemble_audit import AssemblyError


class ApplyAuditReclassificationsTests(unittest.TestCase):
    def test_missing_correction_does_not_partially_rewrite_batches(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo = Path(tempdir)
            batches = repo / "research/batches"
            batches.mkdir(parents=True)
            record = {
                "article_no": "001",
                "classification": "excluded",
                "exclusion_reason": "Not startup relevant.",
                "themes": [],
                "candidate_workflows": [],
                "evidence_line_ranges": [],
                "final_skills": ["existing-skill"],
            }
            batch_path = batches / "batch-01.jsonl"
            batch_path.write_text(json.dumps(record, sort_keys=True) + "\n", encoding="utf-8")
            correction = {
                "article_no": "001",
                "previous_classification": "excluded",
                "classification": "supporting startup",
                "exclusion_reason": "",
                "themes": ["startup judgment"],
                "candidate_workflows": ["test a startup choice"],
                "evidence_line_ranges": ["10-20"],
            }
            missing = dict(correction)
            missing["article_no"] = "999"
            (repo / "research/audit-reclassifications.json").write_text(
                json.dumps({"schema_version": 1, "corrections": [correction, missing]}, indent=2) + "\n",
                encoding="utf-8",
            )
            before = batch_path.read_bytes()

            with self.assertRaisesRegex(ReclassificationError, "not found"):
                apply(repo)

            self.assertEqual(before, batch_path.read_bytes())

    def test_assembly_preflight_failure_does_not_rewrite_batches(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo = Path(tempdir)
            batches = repo / "research/batches"
            batches.mkdir(parents=True)
            record = {
                "article_no": "001",
                "classification": "excluded",
                "exclusion_reason": "Not startup relevant.",
                "themes": [],
                "candidate_workflows": [],
                "evidence_line_ranges": [],
                "final_skills": ["existing-skill"],
            }
            batch_path = batches / "batch-01.jsonl"
            batch_path.write_text(json.dumps(record, sort_keys=True) + "\n", encoding="utf-8")
            correction = {
                "article_no": "001",
                "previous_classification": "excluded",
                "classification": "supporting startup",
                "exclusion_reason": "",
                "themes": ["startup judgment"],
                "candidate_workflows": ["test a startup choice"],
                "evidence_line_ranges": ["10-20"],
            }
            (repo / "research/audit-reclassifications.json").write_text(
                json.dumps({"schema_version": 1, "corrections": [correction]}, indent=2) + "\n",
                encoding="utf-8",
            )
            before = batch_path.read_bytes()

            with self.assertRaises(AssemblyError):
                apply(repo)

            self.assertEqual(before, batch_path.read_bytes())


if __name__ == "__main__":
    unittest.main()
