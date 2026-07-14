# Theme Normalization Design

## Goal

Make cross-corpus recurrence mechanically visible before selecting skill taxonomy, without erasing the article-specific language and conditions already captured in the audit.

## Options considered

1. **Rewrite every audit record to a small canonical list.** Simple downstream joins, but destructive: nuanced reviewer labels disappear and later corrections become hard to trace.
2. **Preserve raw labels and add an explicit many-to-many normalization map.** Chosen. It keeps provenance intact, supports compound labels, and gives taxonomy a stable canonical projection.
3. **Fuzzy-match labels during taxonomy validation.** Rejected because similarity thresholds are unstable, non-auditable, and can silently merge distinct concepts.

## Chosen data model

Create `research/theme-normalization.json` with:

- `schema_version`;
- canonical theme records containing a concise `name` and `definition`;
- one mapping for every distinct raw theme label, containing `raw_theme`, one to three `canonical_themes`, and `reviewer`;
- an optional `article_overrides` list on a mapping for a recurrent homonym whose
  meaning differs by essay; each override contains `article_no`, one to three
  replacement `canonical_themes`, and `reviewer`;
- method notes stating that only synonyms, spelling variants, and genuinely compound labels are normalized; stage/product/urgency conditions remain in candidate workflows unless they are themselves the recurring concept.

An override replaces that raw label's base targets only for the named relevant
essay. It does not union the base and override targets. The base mapping must remain
semantically useful for the raw label, every override article must actually contain
that raw label in a relevant audit record, and raw-label coverage remains exactly one
global mapping row per distinct raw label. This preserves the non-destructive audit
boundary while preventing recurrent homonyms from polluting individual projections.

Allow a raw compound label to map to multiple canonical themes so normalization does not force unrelated concepts into one bucket. Do not create skill names or workflow taxonomy in this artifact.

Generate `research/essay-theme-map.jsonl` from the canonical audit plus normalization map. Each relevant essay record contains:

- `article_no`;
- sorted unique `raw_themes`;
- sorted unique `canonical_themes`;
- `review_batch` and `reviewer` from the audit.

Excluded essays contain no projection record because their audit themes are empty.

## Deterministic tooling

Add `scripts/build_theme_projection.py` with two modes:

- default: validate the normalization artifact against the canonical audit and write the deterministic essay projection;
- `--check`: validate that the existing projection is byte-for-byte current without rewriting it.

The tool must reject:

- an unmapped or duplicate raw theme;
- a mapping to an undefined canonical theme;
- an empty mapping, more than three targets, or duplicate targets;
- an override for an excluded, missing, or non-occurring article/raw-label pair;
- duplicate or unsorted article overrides, empty override reviewers, malformed
  override fields, or empty, undefined, unsorted, duplicate, or more-than-three
  override targets;
- duplicate canonical names or unused canonical themes;
- mappings that do not cover the exact distinct raw-theme set in the audit;
- missing, extra, duplicate, unsorted, or stale essay projection records.

Add standard-library unit tests before implementation and retain RED/GREEN evidence in `research/progress.md`.

## Synthesis boundary

Canonical research themes are evidence-navigation labels, not final skills. Taxonomy work may merge several themes into one workflow skill, keep one theme across several stage-specific skills, or reject a canonical theme as reference-only. Detailed candidate workflows and source ranges remain the authority for those decisions.

## Verification

Before taxonomy:

1. Prove every distinct raw theme maps exactly once.
2. Prove every relevant essay projects to at least one canonical theme.
3. Report raw assignment count, distinct raw count, singleton count, canonical count, and relevant essay count.
4. Report article-override count and prove that every override replaces the base only
   for its named relevant occurrence while non-overridden occurrences retain the base.
5. Run an independent review for over-merging, under-merging, compound-label loss,
   homonym leakage, and accidental skill-taxonomy leakage.
