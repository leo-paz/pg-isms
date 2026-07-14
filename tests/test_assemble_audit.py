import json
import tempfile
import unittest
from pathlib import Path

from scripts.assemble_audit import AssemblyError, assemble, validate_batch


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, records) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")


class AssembleAuditTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.repo = Path(self.tempdir.name)
        write_json(
            self.repo / "research/audit-batches.json",
            {
                "schema_version": 1,
                "batch_count": 2,
                "batches": [
                    {
                        "batch_id": "batch-01",
                        "start_article_no": "001",
                        "end_article_no": "002",
                        "article_nos": ["001", "002"],
                        "reviewer": None,
                    },
                    {
                        "batch_id": "batch-02",
                        "start_article_no": "003",
                        "end_article_no": "003",
                        "article_nos": ["003"],
                        "reviewer": None,
                    },
                ],
            },
        )
        write_jsonl(
            self.repo / "research/retrieval-log.jsonl",
            [{"date": "2026-07-13", "mode": "checkpoint", "purpose": "preserve"}],
        )
        self.write_batch("batch-01", ["001", "002"], "reviewer-01")
        self.write_batch("batch-02", ["003"], "reviewer-02")

    def tearDown(self):
        self.tempdir.cleanup()

    def write_batch(self, batch_id, article_nos, reviewer):
        write_jsonl(
            self.repo / f"research/batches/{batch_id}.jsonl",
            [
                {
                    "article_no": article_no,
                    "review_batch": batch_id,
                    "reviewer": reviewer,
                }
                for article_no in article_nos
            ],
        )
        retrieval = [
            {
                "date": "2026-07-13",
                "batch_id": batch_id,
                "reviewer": reviewer,
                "mode": "bm25",
                "query": "founder users",
                "collection": "graham-essays",
                "limit": 3,
                "results": [],
            },
            {
                "date": "2026-07-13",
                "batch_id": batch_id,
                "reviewer": reviewer,
                "mode": "vector",
                "query": "learning from users",
                "collection": "graham-essays",
                "limit": 3,
                "results": [],
            },
        ]
        retrieval.extend(
            {
                "date": "2026-07-13",
                "batch_id": batch_id,
                "reviewer": reviewer,
                "mode": "full_document",
                "document": f"corpus/{article_no}.md",
                "article_no": article_no,
                "retrieved_lines": 20,
                "full_text_read": True,
                "purpose": "batch audit",
            }
            for article_no in article_nos
        )
        write_jsonl(self.repo / f"research/batches/retrieval-{batch_id}.jsonl", retrieval)

    def test_assembles_sorted_audit_updates_reviewers_and_is_idempotent(self):
        proof = assemble(self.repo)
        self.assertEqual(
            proof,
            {"batches": 2, "essays": 3, "bm25_batches": 2, "vector_batches": 2, "full_documents": 3},
        )
        records = [json.loads(line) for line in (self.repo / "research/essay-audit.jsonl").read_text().splitlines()]
        self.assertEqual([record["article_no"] for record in records], ["001", "002", "003"])
        batches = json.loads((self.repo / "research/audit-batches.json").read_text())["batches"]
        self.assertEqual([batch["reviewer"] for batch in batches], ["reviewer-01", "reviewer-02"])
        first_log = (self.repo / "research/retrieval-log.jsonl").read_text()
        assemble(self.repo)
        self.assertEqual((self.repo / "research/retrieval-log.jsonl").read_text(), first_log)

    def test_validates_one_batch_without_requiring_other_batch_files(self):
        (self.repo / "research/batches/batch-02.jsonl").unlink()
        (self.repo / "research/batches/retrieval-batch-02.jsonl").unlink()
        proof = validate_batch(self.repo, "batch-01")
        self.assertEqual(
            proof,
            {
                "batch_id": "batch-01",
                "reviewer": "reviewer-01",
                "essays": 2,
                "bm25": 1,
                "vector": 1,
                "full_documents": 2,
            },
        )

    def test_accepts_line_addressed_full_document_range(self):
        path = self.repo / "research/batches/retrieval-batch-01.jsonl"
        records = [json.loads(line) for line in path.read_text().splitlines()]
        for record in records:
            if record["mode"] == "full_document":
                record["retrieved_lines"] = "1-20"
        write_jsonl(path, records)
        self.assertEqual(validate_batch(self.repo, "batch-01")["full_documents"], 2)

    def test_rejects_missing_or_extra_article(self):
        self.write_batch("batch-01", ["001", "009"], "reviewer-01")
        with self.assertRaisesRegex(AssemblyError, "article set mismatch"):
            assemble(self.repo)

    def test_rejects_inconsistent_reviewer_or_batch_marker(self):
        records = [
            {"article_no": "001", "review_batch": "batch-01", "reviewer": "reviewer-01"},
            {"article_no": "002", "review_batch": "batch-99", "reviewer": "reviewer-02"},
        ]
        write_jsonl(self.repo / "research/batches/batch-01.jsonl", records)
        with self.assertRaisesRegex(AssemblyError, "reviewer|review_batch"):
            assemble(self.repo)

    def test_rejects_missing_retrieval_mode_or_full_document(self):
        path = self.repo / "research/batches/retrieval-batch-02.jsonl"
        records = [json.loads(line) for line in path.read_text().splitlines()]
        write_jsonl(path, [record for record in records if record["mode"] != "vector"])
        with self.assertRaisesRegex(AssemblyError, "vector"):
            assemble(self.repo)


if __name__ == "__main__":
    unittest.main()
