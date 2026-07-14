import json
import tempfile
import unittest
from pathlib import Path

from scripts.build_research_scaffold import build_research_scaffold, read_corpus


REAL_CORPUS = Path("/Users/leopaz/dev/opensource/graham-essays/corpus")


def write_essay(corpus: Path, article_no: int, title: str) -> None:
    path = corpus / f"{article_no:03d}_essay-{article_no}.md"
    path.write_text(
        "\n".join(
            [
                "---",
                f'title: "{title}"',
                f'article_no: "{article_no:03d}"',
                f'source_url: "https://example.com/{article_no}"',
                "---",
                "",
                f"# {title}",
                "",
                "Essay body.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


class BuildResearchScaffoldTests(unittest.TestCase):
    def test_reads_frontmatter_metadata_and_sorts_numerically(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            corpus = Path(temp_dir) / "corpus"
            corpus.mkdir()
            write_essay(corpus, 10, "Tenth: A Test")
            write_essay(corpus, 2, "Second Essay")
            write_essay(corpus, 1, "First Essay")

            essays = read_corpus(corpus)

            self.assertEqual(["001", "002", "010"], [essay["article_no"] for essay in essays])
            self.assertEqual("Tenth: A Test", essays[-1]["title"])
            self.assertEqual("https://example.com/10", essays[-1]["source_url"])
            self.assertEqual("010_essay-10.md", essays[-1]["corpus_path"])

    def test_real_corpus_generates_exact_balanced_partition(self) -> None:
        self.assertTrue(REAL_CORPUS.is_dir(), f"missing test corpus: {REAL_CORPUS}")
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir)

            build_research_scaffold(REAL_CORPUS, output, batch_count=12)

            manifest = json.loads((output / "research/corpus-manifest.json").read_text())
            batch_data = json.loads((output / "research/audit-batches.json").read_text())
            essays = manifest["essays"]
            batches = batch_data["batches"]
            corpus_ids = {f"{number:03d}" for number in range(1, 224)}
            assigned = [article_no for batch in batches for article_no in batch["article_nos"]]

            self.assertEqual(223, manifest["document_count"])
            self.assertEqual(list(range(1, 224)), [int(essay["article_no"]) for essay in essays])
            self.assertEqual(12, len(batches))
            self.assertEqual(corpus_ids, set(assigned))
            self.assertEqual(len(assigned), len(set(assigned)), "duplicate batch assignment")
            self.assertEqual(223, len(assigned), "batch assignment gap")
            self.assertLessEqual(max(map(len, (batch["article_nos"] for batch in batches))) - min(map(len, (batch["article_nos"] for batch in batches))), 1)
            for batch in batches:
                numbers = list(map(int, batch["article_nos"]))
                self.assertEqual(list(range(numbers[0], numbers[-1] + 1)), numbers)
                self.assertEqual(batch["start_article_no"], batch["article_nos"][0])
                self.assertEqual(batch["end_article_no"], batch["article_nos"][-1])

    def test_output_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            corpus = root / "corpus"
            first = root / "first"
            second = root / "second"
            corpus.mkdir()
            for article_no in range(7, 0, -1):
                write_essay(corpus, article_no, f"Essay {article_no}")

            build_research_scaffold(corpus, first, batch_count=3)
            build_research_scaffold(corpus, second, batch_count=3)

            self.assertEqual(
                (first / "research/corpus-manifest.json").read_bytes(),
                (second / "research/corpus-manifest.json").read_bytes(),
            )
            self.assertEqual(
                (first / "research/audit-batches.json").read_bytes(),
                (second / "research/audit-batches.json").read_bytes(),
            )


if __name__ == "__main__":
    unittest.main()
