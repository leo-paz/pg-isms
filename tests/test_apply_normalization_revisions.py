import unittest

from scripts.apply_normalization_revisions import RevisionError, revised


class ApplyNormalizationRevisionsTests(unittest.TestCase):
    def normalization(self):
        return {
            "schema_version": 1,
            "canonical_themes": [
                {"name": "alpha", "definition": "Alpha theme."},
                {"name": "beta", "definition": "Beta theme."},
                {"name": "gamma", "definition": "Gamma theme."},
            ],
            "mappings": [
                {
                    "raw_theme": "raw-alpha",
                    "canonical_themes": ["alpha"],
                    "reviewer": "initial",
                    "article_overrides": [
                        {
                            "article_no": "001",
                            "canonical_themes": ["alpha"],
                            "reviewer": "initial-override",
                        }
                    ],
                },
                {
                    "raw_theme": "raw-beta",
                    "canonical_themes": ["beta"],
                    "reviewer": "initial",
                },
            ],
            "method_notes": [],
        }

    def revision(self, **updates):
        value = {
            "remove_canonical_themes": [],
            "add_canonical_themes": [],
            "replace_mappings": [],
            "replace_article_overrides": [],
            "remove_article_overrides": [],
            "add_article_overrides": [],
            "add_mappings": [],
        }
        value.update(updates)
        return value

    def test_add_override_uses_item_reviewer_and_is_idempotent(self):
        revision = self.revision(
            add_article_overrides=[
                {
                    "raw_theme": "raw-beta",
                    "article_no": "002",
                    "canonical_themes": ["beta", "gamma"],
                    "reviewer": "source-review-b",
                }
            ]
        )

        first = revised(self.normalization(), revision)
        second = revised(first, revision)

        self.assertEqual(first, second)
        override = next(
            mapping for mapping in first["mappings"] if mapping["raw_theme"] == "raw-beta"
        )["article_overrides"][0]
        self.assertEqual(override["reviewer"], "source-review-b")

    def test_add_override_rejects_missing_item_reviewer(self):
        revision = self.revision(
            add_article_overrides=[
                {
                    "raw_theme": "raw-beta",
                    "article_no": "002",
                    "canonical_themes": ["gamma"],
                }
            ]
        )

        with self.assertRaisesRegex(RevisionError, "reviewer"):
            revised(self.normalization(), revision)

    def test_add_override_rejects_conflict_with_other_reviewer(self):
        revision = self.revision(
            add_article_overrides=[
                {
                    "raw_theme": "raw-alpha",
                    "article_no": "001",
                    "canonical_themes": ["gamma"],
                    "reviewer": "different-review",
                }
            ]
        )

        with self.assertRaisesRegex(RevisionError, "conflicts"):
            revised(self.normalization(), revision)

    def test_remove_override_is_idempotent_and_drops_empty_array(self):
        revision = self.revision(
            remove_article_overrides=[
                {"raw_theme": "raw-alpha", "article_no": "001"}
            ]
        )

        first = revised(self.normalization(), revision)
        second = revised(first, revision)

        self.assertEqual(first, second)
        mapping = next(
            mapping for mapping in first["mappings"] if mapping["raw_theme"] == "raw-alpha"
        )
        self.assertNotIn("article_overrides", mapping)


if __name__ == "__main__":
    unittest.main()
