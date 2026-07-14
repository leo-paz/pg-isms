import copy
import json
import unittest
from pathlib import Path

from scripts.sync_taxonomy import SyncError, derive, validate_runtime_contract


class SyncTaxonomyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.taxonomy = {
            "skills": [
                {
                    "skill_name": "learn-from-users",
                    "themes": ["user discovery", "demand validation"],
                    "essay_ids": [],
                },
                {
                    "skill_name": "ship-products",
                    "themes": ["product iteration"],
                    "essay_ids": [],
                },
            ]
        }
        self.projection = [
            {
                "article_no": "001",
                "canonical_themes": ["user discovery", "product iteration"],
            },
            {
                "article_no": "002",
                "canonical_themes": ["demand validation"],
            },
        ]

    def test_derives_reciprocal_essay_and_skill_mappings(self) -> None:
        taxonomy, essay_skills = derive(
            self.taxonomy,
            self.projection,
            {"user discovery", "demand validation", "product iteration"},
        )

        self.assertEqual(["001", "002"], taxonomy["skills"][0]["essay_ids"])
        self.assertEqual(["001"], taxonomy["skills"][1]["essay_ids"])
        self.assertEqual(
            {
                "001": ["learn-from-users", "ship-products"],
                "002": ["learn-from-users"],
            },
            essay_skills,
        )

    def test_rejects_unassigned_canonical_theme(self) -> None:
        with self.assertRaisesRegex(SyncError, "unassigned canonical themes"):
            derive(
                self.taxonomy,
                self.projection,
                {"user discovery", "demand validation", "product iteration", "runway"},
            )

    def test_rejects_theme_assigned_to_multiple_skills(self) -> None:
        self.taxonomy["skills"][1]["themes"].append("user discovery")

        with self.assertRaisesRegex(SyncError, "assigned to multiple skills"):
            derive(
                self.taxonomy,
                self.projection,
                {"user discovery", "demand validation", "product iteration"},
            )

    def test_rejects_projected_theme_outside_normalization(self) -> None:
        self.projection[0]["canonical_themes"].append("unknown theme")

        with self.assertRaisesRegex(SyncError, "projection contains unknown themes"):
            derive(
                self.taxonomy,
                self.projection,
                {"user discovery", "demand validation", "product iteration"},
            )

    def test_production_taxonomy_source_has_complete_runtime_contract(self) -> None:
        source = json.loads(Path("research/taxonomy-source.json").read_text())

        proof = validate_runtime_contract(source)

        self.assertEqual(7, proof["global_invariants"])
        self.assertEqual(6, proof["product_types"])
        self.assertEqual(9, proof["routing_rules"])
        self.assertEqual(42, proof["decision_branches"])

    def test_runtime_contract_rejects_missing_global_invariant(self) -> None:
        source = json.loads(Path("research/taxonomy-source.json").read_text())
        broken = copy.deepcopy(source)
        broken["global_invariants"].pop()

        with self.assertRaisesRegex(SyncError, "global invariants"):
            validate_runtime_contract(broken)

    def test_runtime_contract_rejects_missing_decision_branch(self) -> None:
        source = json.loads(Path("research/taxonomy-source.json").read_text())
        broken = copy.deepcopy(source)
        broken["decision_branches"]["learning-from-users"].pop()

        with self.assertRaisesRegex(SyncError, "decision branches do not match tensions"):
            validate_runtime_contract(broken)

    def test_runtime_contract_rejects_mismatched_decision_branch_tension(self) -> None:
        source = json.loads(Path("research/taxonomy-source.json").read_text())
        broken = copy.deepcopy(source)
        broken["decision_branches"]["learning-from-users"][0]["tension"] = broken[
            "decision_branches"
        ]["learning-from-users"][1]["tension"]

        with self.assertRaisesRegex(SyncError, "branch tensions do not match"):
            validate_runtime_contract(broken)

    def test_runtime_contract_rejects_one_sided_decision_branch_predicate(self) -> None:
        source = json.loads(Path("research/taxonomy-source.json").read_text())
        broken = copy.deepcopy(source)
        broken["decision_branches"]["learning-from-users"][0]["predicate"] = (
            "If requests conflict with behavior, then investigate the problem."
        )

        with self.assertRaisesRegex(SyncError, "predicate is not two-sided"):
            validate_runtime_contract(broken)

    def test_runtime_contract_rejects_missing_branch_side(self) -> None:
        source = json.loads(Path("research/taxonomy-source.json").read_text())
        broken = copy.deepcopy(source)
        broken["decision_branches"]["learning-from-users"][0]["false_case"] = ""

        with self.assertRaisesRegex(SyncError, "false_case is incomplete"):
            validate_runtime_contract(broken)

    def test_runtime_contract_rejects_coordinated_tension_and_branch_deletion(self) -> None:
        source = json.loads(Path("research/taxonomy-source.json").read_text())
        broken = copy.deepcopy(source)
        broken["skills"][0]["tensions"].pop()
        broken["decision_branches"][broken["skills"][0]["skill_name"]].pop()

        with self.assertRaisesRegex(SyncError, "exactly two tensions|42 decision branches"):
            validate_runtime_contract(broken)

    def test_runtime_contract_rejects_empty_stage_conditions(self) -> None:
        source = json.loads(Path("research/taxonomy-source.json").read_text())
        broken = copy.deepcopy(source)
        broken["skills"][0]["stage_conditions"] = []

        with self.assertRaisesRegex(SyncError, "stage conditions"):
            validate_runtime_contract(broken)

    def test_runtime_contract_rejects_malformed_evaluation_branch_contract(self) -> None:
        source = json.loads(Path("research/taxonomy-source.json").read_text())
        broken = copy.deepcopy(source)
        broken["evaluation_branch_contract"] = [{}, {}, {}]

        with self.assertRaisesRegex(SyncError, "evaluation branch contract"):
            validate_runtime_contract(broken)


if __name__ == "__main__":
    unittest.main()
