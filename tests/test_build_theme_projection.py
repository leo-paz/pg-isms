"""Tests for the deterministic audited-theme normalization projection."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_theme_projection.py"


class ThemeProjectionTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.repo = Path(self.temporary_directory.name)
        (self.repo / "research").mkdir()
        self.audit = [
            {
                "article_no": "001",
                "classification": "core startup",
                "themes": ["beta", "alpha"],
                "review_batch": "batch-01",
                "reviewer": "audit-one",
            },
            {
                "article_no": "002",
                "classification": "supporting startup",
                "themes": ["compound"],
                "review_batch": "batch-01",
                "reviewer": "audit-one",
            },
            {
                "article_no": "003",
                "classification": "excluded",
                "themes": [],
                "review_batch": "batch-01",
                "reviewer": "audit-one",
            },
        ]
        self.normalization = {
            "schema_version": 1,
            "method_notes": [
                "Raw labels remain authoritative and compounds may retain multiple targets."
            ],
            "canonical_themes": [
                {"name": "alpha concept", "definition": "The recurring alpha concept."},
                {"name": "beta concept", "definition": "The recurring beta concept."},
            ],
            "mappings": [
                {
                    "raw_theme": "alpha",
                    "canonical_themes": ["alpha concept"],
                    "reviewer": "normalizer-one",
                },
                {
                    "raw_theme": "beta",
                    "canonical_themes": ["beta concept"],
                    "reviewer": "normalizer-one",
                },
                {
                    "raw_theme": "compound",
                    "canonical_themes": ["alpha concept", "beta concept"],
                    "reviewer": "normalizer-one",
                },
            ],
        }
        self.write_inputs()

    def tearDown(self):
        self.temporary_directory.cleanup()

    def write_inputs(self):
        audit_text = "".join(json.dumps(record) + "\n" for record in self.audit)
        (self.repo / "research" / "essay-audit.jsonl").write_text(
            audit_text, encoding="utf-8"
        )
        (self.repo / "research" / "theme-normalization.json").write_text(
            json.dumps(self.normalization, indent=2) + "\n", encoding="utf-8"
        )

    def run_script(self, *arguments):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--repo", str(self.repo), *arguments],
            text=True,
            capture_output=True,
            check=False,
        )

    def assert_rejected(self, fragment):
        self.write_inputs()
        result = self.run_script()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(fragment, result.stderr)

    def test_default_writes_sorted_unique_projection_and_omits_excluded_essays(self):
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        records = [
            json.loads(line)
            for line in (self.repo / "research" / "essay-theme-map.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
        ]
        self.assertEqual([record["article_no"] for record in records], ["001", "002"])
        self.assertEqual(records[0]["raw_themes"], ["alpha", "beta"])
        self.assertEqual(records[0]["canonical_themes"], ["alpha concept", "beta concept"])
        self.assertEqual(records[1]["canonical_themes"], ["alpha concept", "beta concept"])
        self.assertEqual(records[0]["review_batch"], "batch-01")
        self.assertEqual(records[0]["reviewer"], "audit-one")

    def test_check_accepts_byte_current_projection(self):
        self.assertEqual(self.run_script().returncode, 0)
        before = (self.repo / "research" / "essay-theme-map.jsonl").read_bytes()
        result = self.run_script("--check")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            (self.repo / "research" / "essay-theme-map.jsonl").read_bytes(), before
        )

    def test_rejects_unmapped_raw_theme(self):
        self.normalization["mappings"] = self.normalization["mappings"][1:]
        self.assert_rejected("unmapped raw themes")

    def test_rejects_extra_raw_theme_mapping(self):
        self.normalization["mappings"].append(
            {
                "raw_theme": "not audited",
                "canonical_themes": ["alpha concept"],
                "reviewer": "normalizer-one",
            }
        )
        self.assert_rejected("extra raw theme mappings")

    def test_rejects_duplicate_raw_theme_mapping(self):
        self.normalization["mappings"].append(dict(self.normalization["mappings"][0]))
        self.assert_rejected("duplicate raw theme mapping")

    def test_rejects_duplicate_canonical_name(self):
        self.normalization["canonical_themes"].append(
            {"name": "alpha concept", "definition": "A duplicate."}
        )
        self.assert_rejected("duplicate canonical theme")

    def test_rejects_undefined_canonical_target(self):
        self.normalization["mappings"][0]["canonical_themes"] = ["undefined"]
        self.assert_rejected("undefined canonical theme")

    def test_rejects_unused_canonical_theme(self):
        self.normalization["canonical_themes"].append(
            {"name": "unused concept", "definition": "Never mapped."}
        )
        self.assert_rejected("unused canonical themes")

    def test_rejects_empty_target_mapping(self):
        self.normalization["mappings"][0]["canonical_themes"] = []
        self.assert_rejected("one to three canonical themes")

    def test_rejects_more_than_three_targets(self):
        for name in ("delta", "gamma"):
            self.normalization["canonical_themes"].append(
                {"name": name, "definition": f"The {name} concept."}
            )
        self.normalization["mappings"][0]["canonical_themes"] = [
            "alpha concept",
            "beta concept",
            "gamma",
            "delta",
        ]
        self.assert_rejected("one to three canonical themes")

    def test_rejects_malformed_top_level_normalization(self):
        self.normalization = []
        self.assert_rejected("must be a JSON object")

    def test_rejects_wrong_schema_version(self):
        self.normalization["schema_version"] = 2
        self.assert_rejected("schema_version must be the integer 1")

    def test_rejects_boolean_schema_version(self):
        self.normalization["schema_version"] = True
        self.assert_rejected("schema_version must be the integer 1")

    def test_rejects_unexpected_or_missing_normalization_keys(self):
        self.normalization["unexpected"] = "value"
        self.assert_rejected("keys must be exactly")
        self.normalization = {
            key: value
            for key, value in self.normalization.items()
            if key not in {"unexpected", "method_notes"}
        }
        self.assert_rejected("keys must be exactly")

    def test_rejects_unexpected_or_missing_canonical_record_keys(self):
        del self.normalization["canonical_themes"][0]["definition"]
        self.assert_rejected("must contain name and definition")
        self.normalization["canonical_themes"][0] = {
            "name": "alpha concept",
            "definition": "The alpha concept.",
            "unexpected": True,
        }
        self.assert_rejected("must contain name and definition")

    def test_rejects_unexpected_or_missing_mapping_record_keys(self):
        del self.normalization["mappings"][0]["reviewer"]
        self.assert_rejected("must contain raw_theme, canonical_themes, and reviewer")

    def test_article_override_applies_only_to_the_matching_relevant_occurrence(self):
        self.audit[0]["themes"] = ["alpha"]
        self.audit[1]["themes"] = ["alpha"]
        self.normalization["canonical_themes"] = [
            {"name": "alpha concept", "definition": "The recurring alpha concept."},
            {"name": "override only", "definition": "An article-scoped target."},
        ]
        self.normalization["mappings"] = [self.normalization["mappings"][0]]
        self.normalization["mappings"][0]["article_overrides"] = [
            {
                "article_no": "002",
                "canonical_themes": ["override only"],
                "reviewer": "override-reviewer",
            }
        ]
        self.write_inputs()
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        records = [
            json.loads(line)
            for line in (self.repo / "research" / "essay-theme-map.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
        ]
        self.assertEqual(records[0]["canonical_themes"], ["alpha concept"])
        self.assertEqual(records[1]["canonical_themes"], ["override only"])

    def test_rejects_override_article_without_relevant_raw_theme_occurrence(self):
        for article_no in ("002", "003", "999"):
            with self.subTest(article_no=article_no):
                self.normalization["mappings"][0]["article_overrides"] = [
                    {
                        "article_no": article_no,
                        "canonical_themes": ["beta concept"],
                        "reviewer": "override-reviewer",
                    }
                ]
                self.assert_rejected("is not a relevant audit occurrence")

    def test_rejects_duplicate_article_overrides(self):
        override = {
            "article_no": "001",
            "canonical_themes": ["beta concept"],
            "reviewer": "override-reviewer",
        }
        self.normalization["mappings"][0]["article_overrides"] = [override, dict(override)]
        self.assert_rejected("duplicate article override")

    def test_rejects_unsorted_or_nonlist_article_overrides(self):
        self.audit[1]["themes"] = ["alpha", "compound"]
        self.normalization["mappings"][0]["article_overrides"] = [
            {
                "article_no": "002",
                "canonical_themes": ["beta concept"],
                "reviewer": "override-reviewer",
            },
            {
                "article_no": "001",
                "canonical_themes": ["beta concept"],
                "reviewer": "override-reviewer",
            },
        ]
        self.assert_rejected("article overrides are not sorted")
        self.normalization["mappings"][0]["article_overrides"] = {}
        self.assert_rejected("article_overrides must be a list")

    def test_rejects_invalid_override_targets(self):
        invalid_targets = (
            ([], "one to three canonical themes"),
            (["alpha concept", "alpha concept"], "duplicate canonical targets"),
            (["beta concept", "alpha concept"], "canonical targets are not sorted"),
            (["undefined"], "undefined canonical theme"),
        )
        for targets, expected in invalid_targets:
            with self.subTest(targets=targets):
                self.normalization["mappings"][0]["article_overrides"] = [
                    {
                        "article_no": "001",
                        "canonical_themes": targets,
                        "reviewer": "override-reviewer",
                    }
                ]
                self.assert_rejected(expected)

    def test_rejects_invalid_override_reviewer_or_fields(self):
        self.normalization["mappings"][0]["article_overrides"] = [
            {
                "article_no": "001",
                "canonical_themes": ["beta concept"],
                "reviewer": "",
            }
        ]
        self.assert_rejected("empty article_no or reviewer")
        self.normalization["mappings"][0]["article_overrides"] = [
            {
                "article_no": "001",
                "canonical_themes": ["beta concept"],
                "reviewer": "override-reviewer",
                "unexpected": True,
            }
        ]
        self.assert_rejected("must contain article_no, canonical_themes, and reviewer")

    def test_override_targets_count_as_canonical_usage(self):
        self.normalization["canonical_themes"].append(
            {"name": "override only", "definition": "Used only by an article override."}
        )
        self.normalization["mappings"][0]["article_overrides"] = [
            {
                "article_no": "001",
                "canonical_themes": ["override only"],
                "reviewer": "override-reviewer",
            }
        ]
        self.write_inputs()
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        record = json.loads(
            (self.repo / "research" / "essay-theme-map.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()[0]
        )
        self.assertIn("override only", record["canonical_themes"])

    def test_check_detects_stale_override_projection_without_rewriting(self):
        self.audit[1]["themes"] = ["alpha"]
        self.normalization["canonical_themes"] = self.normalization["canonical_themes"][:2]
        self.normalization["mappings"] = self.normalization["mappings"][:2]
        self.normalization["mappings"][0]["article_overrides"] = [
            {
                "article_no": "002",
                "canonical_themes": ["beta concept"],
                "reviewer": "override-reviewer",
            }
        ]
        self.write_inputs()
        self.assertEqual(self.run_script().returncode, 0)
        projection_path = self.repo / "research" / "essay-theme-map.jsonl"
        before = projection_path.read_bytes()
        self.normalization["mappings"][0]["article_overrides"][0][
            "canonical_themes"
        ] = ["alpha concept"]
        self.write_inputs()
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("projection is stale", result.stderr)
        self.assertEqual(projection_path.read_bytes(), before)
        self.normalization["mappings"][0] = {
            "raw_theme": "alpha",
            "canonical_themes": ["alpha concept"],
            "reviewer": "normalizer-one",
            "unexpected": True,
        }
        self.assert_rejected("must contain raw_theme, canonical_themes, and reviewer")

    def test_rejects_malformed_canonical_and_mapping_lists(self):
        self.normalization["canonical_themes"] = "not-a-list"
        self.assert_rejected("canonical_themes must be a nonempty list")
        self.normalization = {
            "schema_version": 1,
            "method_notes": ["A method."],
            "canonical_themes": [
                {"name": "alpha concept", "definition": "The alpha concept."}
            ],
            "mappings": {"alpha": ["alpha concept"]},
        }
        self.assert_rejected("mappings must be a list")

    def test_rejects_empty_canonical_name_or_definition(self):
        self.normalization["canonical_themes"][0]["definition"] = ""
        self.assert_rejected("empty name or definition")

    def test_rejects_empty_mapping_reviewer(self):
        self.normalization["mappings"][0]["reviewer"] = ""
        self.assert_rejected("empty raw theme or reviewer")

    def test_rejects_unsorted_canonical_theme_records(self):
        self.normalization["canonical_themes"].reverse()
        self.assert_rejected("canonical themes must be sorted")

    def test_rejects_unsorted_mapping_records(self):
        self.normalization["mappings"].reverse()
        self.assert_rejected("raw theme mappings must be sorted")

    def test_rejects_duplicate_audit_article_ids(self):
        self.audit.append(dict(self.audit[1]))
        self.assert_rejected("duplicate audit article numbers")

    def test_rejects_relevant_audit_without_themes(self):
        self.audit[0]["themes"] = []
        self.assert_rejected("has no themes")

    def test_rejects_excluded_audit_with_themes(self):
        self.audit[2]["themes"] = ["alpha"]
        self.assert_rejected("excluded audit 003 has themes")

    def test_reports_all_requested_counts(self):
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        for expected in (
            "raw_assignments=3",
            "distinct_raw=3",
            "singleton_raw=3",
            "canonical=2",
            "relevant_essays=2",
        ):
            self.assertIn(expected, result.stdout)

    def test_rejects_duplicate_targets(self):
        self.normalization["mappings"][0]["canonical_themes"] = [
            "alpha concept",
            "alpha concept",
        ]
        self.assert_rejected("duplicate canonical targets")

    def test_check_rejects_missing_projection_record(self):
        self.assertEqual(self.run_script().returncode, 0)
        path = self.repo / "research" / "essay-theme-map.jsonl"
        path.write_text(path.read_text(encoding="utf-8").splitlines()[0] + "\n", encoding="utf-8")
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing projection records", result.stderr)

    def test_check_rejects_extra_projection_record(self):
        self.assertEqual(self.run_script().returncode, 0)
        path = self.repo / "research" / "essay-theme-map.jsonl"
        extra = {
            "article_no": "999",
            "raw_themes": ["alpha"],
            "canonical_themes": ["alpha concept"],
            "review_batch": "batch-99",
            "reviewer": "audit-extra",
        }
        path.write_text(path.read_text(encoding="utf-8") + json.dumps(extra) + "\n", encoding="utf-8")
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("extra projection records", result.stderr)

    def test_check_rejects_duplicate_projection_record(self):
        self.assertEqual(self.run_script().returncode, 0)
        path = self.repo / "research" / "essay-theme-map.jsonl"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join([lines[0], lines[0], lines[1]]) + "\n", encoding="utf-8")
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate projection article", result.stderr)

    def test_check_rejects_unsorted_projection_records(self):
        self.assertEqual(self.run_script().returncode, 0)
        path = self.repo / "research" / "essay-theme-map.jsonl"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(reversed(lines)) + "\n", encoding="utf-8")
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("projection records are not sorted", result.stderr)

    def test_check_rejects_unsorted_theme_lists(self):
        self.assertEqual(self.run_script().returncode, 0)
        path = self.repo / "research" / "essay-theme-map.jsonl"
        records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        records[0]["raw_themes"] = ["beta", "alpha"]
        path.write_text(
            "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
            encoding="utf-8",
        )
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("sorted unique raw_themes", result.stderr)

    def test_check_rejects_stale_projection_values(self):
        self.assertEqual(self.run_script().returncode, 0)
        path = self.repo / "research" / "essay-theme-map.jsonl"
        records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        records[0]["reviewer"] = "stale-reviewer"
        path.write_text(
            "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
            encoding="utf-8",
        )
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("projection is stale", result.stderr)

    def test_check_rejects_semantically_equal_byte_different_projection_without_rewriting(self):
        self.assertEqual(self.run_script().returncode, 0)
        path = self.repo / "research" / "essay-theme-map.jsonl"
        records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        path.write_text(
            "".join(
                json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
                for record in records
            ),
            encoding="utf-8",
        )
        byte_different = path.read_bytes()
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("projection is stale", result.stderr)
        self.assertEqual(path.read_bytes(), byte_different)

    def test_check_rejects_unexpected_or_missing_projection_record_keys(self):
        self.assertEqual(self.run_script().returncode, 0)
        path = self.repo / "research" / "essay-theme-map.jsonl"
        records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        records[0]["unexpected"] = True
        path.write_text(
            "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
            encoding="utf-8",
        )
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid fields", result.stderr)

        self.assertEqual(self.run_script().returncode, 0)
        records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        del records[0]["reviewer"]
        path.write_text(
            "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
            encoding="utf-8",
        )
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid fields", result.stderr)

    def test_check_rejects_nonstring_projection_theme_without_rewriting(self):
        self.assertEqual(self.run_script().returncode, 0)
        path = self.repo / "research" / "essay-theme-map.jsonl"
        records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        records[0]["raw_themes"] = [1]
        path.write_text(
            "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
            encoding="utf-8",
        )
        invalid_bytes = path.read_bytes()
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("nonempty strings", result.stderr)
        self.assertEqual(path.read_bytes(), invalid_bytes)

    def test_check_rejects_nonstring_projection_identity_and_provenance(self):
        self.assertEqual(self.run_script().returncode, 0)
        path = self.repo / "research" / "essay-theme-map.jsonl"
        records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        records[0]["article_no"] = 1
        path.write_text(
            "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
            encoding="utf-8",
        )
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("nonempty article_no strings", result.stderr)

        self.assertEqual(self.run_script().returncode, 0)
        records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        records[0]["reviewer"] = []
        path.write_text(
            "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
            encoding="utf-8",
        )
        result = self.run_script("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid review provenance", result.stderr)


class ProductionSemanticRemediationTests(unittest.TestCase):
    """Locks reviewed correction tables into the production research artifact."""

    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[1]
        normalization = json.loads(
            (root / "research" / "theme-normalization.json").read_text(encoding="utf-8")
        )
        cls.canonical_names = {record["name"] for record in normalization["canonical_themes"]}
        cls.mappings = {record["raw_theme"]: record for record in normalization["mappings"]}
        cls.projection = {
            record["article_no"]: record
            for record in (
                json.loads(line)
                for line in (root / "research" / "essay-theme-map.jsonl")
                .read_text(encoding="utf-8")
                .splitlines()
            )
        }

    def assert_targets(self, raw_theme, expected):
        self.assertEqual(self.mappings[raw_theme]["canonical_themes"], sorted(expected))

    def test_originality_and_writing_boundaries_match_both_reviews(self):
        originality = {
            "breadth and depth", "creative persistence", "cultivating originality",
            "curiosity", "discovery risk", "diverse inputs", "early-version judgment",
            "exploration risk", "frontier gaps", "generality", "idea branching",
            "idea output over intelligence", "idea suppression", "insight quality",
            "iterative idea development", "maker persistence", "novelty",
            "possibility-first critique", "rate of improvement", "support for innovators",
            "writing as idea development",
        }
        for raw_theme in originality:
            targets = self.mappings[raw_theme]["canonical_themes"]
            self.assertIn("originality-and-idea-development", targets)
            self.assertNotIn("startup-idea-selection-and-pivots", targets)

        discovery = {
            "discovery writing", "idea branching", "idea compression", "idea validation",
            "ill-defined problem solving", "question selection", "question-led reasoning",
            "reading-writing loop", "surprise-driven research", "tacit knowledge",
            "writing as discovery", "writing as idea development", "writing as thinking",
            "writing practice", "writing to discover", "writing to think", "written reasoning",
        }
        clarity = {
            "claim calibration", "communication accessibility", "conversational tone",
            "draft transparency", "iterative editing", "loose-then-tight revision",
            "misinterpretation handling", "neutral-reader revision", "plain language",
            "plain-language writing", "progressive drafting", "read-aloud revision",
            "reader cognitive load", "reader comprehension", "revision workflow",
            "simple language", "strict revision", "structured communication",
            "subtractive editing", "useful writing",
        }
        for raw_theme in discovery:
            self.assertIn("writing-as-discovery-and-thinking", self.mappings[raw_theme]["canonical_themes"])
        for raw_theme in clarity:
            self.assertIn("writing-clarity-and-revision", self.mappings[raw_theme]["canonical_themes"])
        self.assertNotIn("writing-and-reasoning", self.canonical_names)

    def test_exact_bias_launch_scaling_role_and_investor_corrections(self):
        exact = {
            "competence bias": ["learning-and-skill-development", "status-prestige-and-bias"],
            "ex-ante judgment": ["decision-quality-and-noise", "risk-and-error-management"],
            "hindsight bias": ["decision-quality-and-noise", "risk-and-error-management"],
            "wishful thinking": ["acquisition-and-exit", "decision-quality-and-noise"],
            "investor selection": ["funding-stage-fit", "investor-incentives-and-selection"],
            "investor lag": ["funding-market-conditions", "market-timing-and-transitions", "venture-type-and-capital-model"],
            "error-cost gating": ["launch-safety-and-reversibility", "risk-and-error-management", "stage-and-state-conditions"],
            "fast launch and iteration": ["launch-safety-and-reversibility", "launch-strategy", "product-iteration-and-redesign"],
            "scalable growth": ["business-models-and-channel-power", "runway-survival-and-profitability", "venture-type-and-capital-model"],
            "scalable startup definition": ["startup-economics-and-risk", "venture-type-and-capital-model"],
            "fast-growth economics": ["compounding-and-power-law-returns", "startup-economics-and-risk", "venture-type-and-capital-model"],
            "software iteration": ["platform-and-ecosystem-strategy", "product-iteration-and-redesign", "release-and-deployment"],
            "technical founder assessment": ["founder-evaluation-and-potential", "hiring-and-talent"],
            "technical identity": ["hiring-and-talent", "team-culture-and-cohesion", "team-structure-and-ownership"],
            "innovation culture": ["independent-and-contrarian-judgment", "team-culture-and-cohesion"],
            "purposeful team culture": ["mission-and-user-benefit", "team-culture-and-cohesion"],
            "early office location": ["collaboration-and-peer-support", "location-and-mobility"],
            "anomaly detection": ["learning-and-skill-development", "originality-and-idea-development", "startup-idea-selection-and-pivots"],
            "contrarian discovery": ["independent-and-contrarian-judgment", "originality-and-idea-development"],
            "imaginative judgment": ["founder-evaluation-and-potential", "originality-and-idea-development"],
            "localized innovation": ["startup-ecosystems-and-hubs"],
            "urgency": ["attention-and-priority-control", "urgency-and-demand-intensity"],
            "founder-led customer work": ["manual-and-scrappy-operations", "team-structure-and-ownership", "user-acquisition-and-distribution"],
            "builder leadership": ["founder-evaluation-and-potential", "organizational-leadership-and-role-evolution", "public-visibility-and-reputation-defense"],
            "support for innovators": ["collaboration-and-peer-support", "originality-and-idea-development"],
            "founder peer clusters": ["accelerators-and-advising", "collaboration-and-peer-support"],
            "hacker culture": ["hiring-and-talent", "team-culture-and-cohesion"],
            "weekly growth": ["evidence-latency-and-cadence", "growth-measurement-and-phases"],
            "Series A governance": ["financing-terms-equity-and-control", "historical-and-source-context", "stage-and-state-conditions"],
        }
        for raw_theme, targets in exact.items():
            with self.subTest(raw_theme=raw_theme):
                self.assert_targets(raw_theme, targets)

    def test_required_article_overrides_are_exact(self):
        expected = {
            "talent attraction": {
                "063": ["hiring-and-talent", "location-and-mobility"],
                "158": ["hiring-and-talent", "team-culture-and-cohesion"],
                "176": ["hiring-and-talent", "location-and-mobility"],
            },
            "founder support": {
                "109": ["investor-incentives-and-selection"],
                "118": ["collaboration-and-peer-support"],
            },
            "owned projects": {
                "206": ["owned-projects-and-maker-autonomy", "team-structure-and-ownership"],
                "218": ["motivation-and-work-fit", "owned-projects-and-maker-autonomy"],
            },
            "incentive alignment": {
                "033": ["incentives-and-behavior"],
                "052": ["investor-incentives-and-selection", "risk-and-error-management"],
            },
            "intellectual honesty": {
                "200": ["integrity-truth-and-calibration", "writing-clarity-and-revision"],
                "218": ["integrity-truth-and-calibration", "motivation-and-work-fit"],
                "220": ["integrity-truth-and-calibration", "writing-clarity-and-revision"],
            },
        }
        for raw_theme, overrides in expected.items():
            actual = {
                override["article_no"]: override["canonical_themes"]
                for override in self.mappings[raw_theme]["article_overrides"]
            }
            self.assertEqual(actual, {key: sorted(value) for key, value in overrides.items()})

    def test_urgency_and_all_explicit_h_flagged_essays_are_projected(self):
        for raw_theme in {"urgency", "urgent early demand", "urgent first users", "truthful urgency"}:
            self.assertIn("urgency-and-demand-intensity", self.mappings[raw_theme]["canonical_themes"])
        for article_no in {"131", "136", "145", "156", "172", "185", "191", "196"}:
            with self.subTest(article_no=article_no):
                self.assertIn("historical-and-source-context", self.projection[article_no]["canonical_themes"])

    def test_runtime_routing_splits_replace_broad_canonical_themes(self):
        removed = {
            "adversarial-robustness-and-abuse",
            "equity-and-ownership",
            "network-effects-and-critical-mass",
            "policy-regulation-and-immigration",
        }
        added = {
            "abuse-and-moderation-controls",
            "adversarial-system-robustness",
            "ecosystem-policy-and-institutions",
            "employee-equity-and-compensation",
            "product-network-effects-and-critical-mass",
            "regional-ecosystem-density",
            "regulatory-and-legal-constraints",
            "technology-ecosystem-adoption",
        }

        self.assertTrue(removed.isdisjoint(self.canonical_names))
        self.assertTrue(added <= self.canonical_names)
        self.assert_targets("employee equity", ["employee-equity-and-compensation", "hiring-and-talent"])
        self.assert_targets("adversarial robustness", ["adversarial-system-robustness"])
        self.assert_targets("critical mass", ["regional-ecosystem-density", "startup-ecosystems-and-hubs"])
        self.assert_targets("referral networks", ["investor-incentives-and-selection", "portfolio-investing"])
        self.assert_targets(
            "startup-hub formation", ["regional-ecosystem-density", "startup-ecosystems-and-hubs"]
        )

    def test_reopened_essays_have_semantic_theme_projections(self):
        expected = {
            "060": {"decision-quality-and-noise", "status-prestige-and-bias"},
            "144": {"business-models-and-channel-power", "technology-transitions-and-disruption"},
            "189": {"evidence-latency-and-cadence", "integrity-truth-and-calibration"},
            "199": {"accelerators-and-advising", "decision-quality-and-noise"},
            "210": {"product-design-and-taste", "product-quality-and-behavioral-feedback"},
        }
        for article_no, themes in expected.items():
            with self.subTest(article_no=article_no):
                self.assertTrue(themes <= set(self.projection[article_no]["canonical_themes"]))


if __name__ == "__main__":
    unittest.main()
