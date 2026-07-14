# Research progress

## Checkpoint 1: research scaffold and cumulative validator

Date: 2026-07-13

### TDD evidence

Both production modules were absent when their tests were first run.

```text
$ python3 -m unittest tests.test_build_research_scaffold -v
ImportError: Failed to import test module: test_build_research_scaffold
ModuleNotFoundError: No module named 'scripts'
FAILED (errors=1)

$ python3 -m unittest tests.test_validate_repository -v
ImportError: Failed to import test module: test_validate_repository
ModuleNotFoundError: No module named 'scripts'
FAILED (errors=1)
```

After implementation, the focused suites passed. A later README exactness regression was also developed RED/GREEN. Final discovery passed 16 tests total: 3 scaffold tests and 13 cumulative-validator tests.

```text
$ python3 -m unittest discover -s tests -v
Ran 16 tests
OK
```

### Generated corpus scaffold

Command:

```bash
python3 scripts/build_research_scaffold.py \
  --corpus /Users/leopaz/dev/opensource/graham-essays/corpus \
  --output-root . \
  --batch-count 12
```

Result:

```text
generated research scaffold from 223 corpus files
```

The manifest contains 223 numerically sorted metadata records. The batch plan contains 12 explicit contiguous assignments: seven batches of 19 essays and five batches of 18 essays.

### QMD access and retrieval proof

Status command:

```bash
PATH=/Users/leopaz/.nvm/versions/node/v22.23.0/bin:$PATH \
  qmd --index graham-essays status
```

Status reported `223 files indexed`, `1582 embedded` vectors, and the `graham-essays` collection with 223 files.

BM25 example:

```bash
PATH=/Users/leopaz/.nvm/versions/node/v22.23.0/bin:$PATH \
  qmd --index graham-essays search \
  "talk to users launch startup" -c graham-essays -n 3 --format json
```

The top three results were articles 153, 069, and 222, with scores 0.79, 0.79, and 0.78.

Vector example:

```bash
PATH=/Users/leopaz/.nvm/versions/node/v22.23.0/bin:$PATH \
  qmd --index graham-essays vsearch \
  "founders learning directly from early users before scaling" \
  -c graham-essays -n 3 --format json
```

The top three results were articles 153, 169, and 039, with scores 0.64, 0.60, and 0.55.

Full-document retrieval proof:

```bash
PATH=/Users/leopaz/.nvm/versions/node/v22.23.0/bin:$PATH \
  qmd --index graham-essays get \
  qmd://graham-essays/153-do-things-that-don-t-scale.md | wc -l
```

The complete retrieval streamed successfully and contained 169 output lines. This was a retrieval-path check only; no essay was classified and no taxonomy was selected.

### Manifest gate

```bash
python3 scripts/validate_repository.py \
  --phase manifest \
  --repo . \
  --corpus /Users/leopaz/dev/opensource/graham-essays/corpus
```

```text
manifest validation passed: corpus_files=223 manifest_essays=223 unique_assignments=223 batches=12 gaps=0 overlaps=0
```

### Remaining work and blockers

- Remaining: independent review of all 12 non-overlapping essay batches, canonical audit assembly, taxonomy synthesis, per-skill baseline/forward evaluation, independent final review, and README catalog.
- Delivery state: checkpoint push is pending clean controller review; no push or completion claim is made here.
- Blockers: none.

### Checkpoint 1 review remediation

The first independent implementation review found four validator gaps. Focused regression tests were added before production changes for:

- normalized exact coverage of every audited theme by the essay's mapped taxonomy skills;
- malformed `SKILL.md` frontmatter and malformed `agents/openai.yaml` indentation/quoting;
- evaluation summaries that show no material improvement, reuse reviewer IDs, or reference missing raw output;
- final-review files missing a required evidence category.

Focused RED command:

```bash
python3 -m unittest -v \
  tests.test_validate_repository.ValidateRepositoryTests.test_rejects_taxonomy_themes_unrelated_to_audited_themes \
  tests.test_validate_repository.ValidateRepositoryTests.test_rejects_malformed_skill_frontmatter \
  tests.test_validate_repository.ValidateRepositoryTests.test_rejects_malformed_openai_yaml \
  tests.test_validate_repository.ValidateRepositoryTests.test_rejects_evaluations_without_material_improvement \
  tests.test_validate_repository.ValidateRepositoryTests.test_rejects_reused_baseline_and_forward_reviewer_ids \
  tests.test_validate_repository.ValidateRepositoryTests.test_rejects_evaluation_summary_with_missing_raw_artifact \
  tests.test_validate_repository.ValidateRepositoryTests.test_rejects_incomplete_final_review_categories
```

Before the fixes, all seven tests failed with `AssertionError: ValidationError not raised` (`Ran 7 tests`, `FAILED (failures=7)`). After the minimum validator changes, the same command reported `Ran 7 tests` and `OK`.

Evaluation artifact schema v1 is defined in the implementation plan. It uses versioned `cases.json`, versioned per-phase `summary.json`, one scored result and raw Markdown artifact per case, distinct stable reviewer IDs, identical scoring scales, and a minimum normalized forward-minus-baseline delta of `0.10`.

Post-remediation discovery:

```text
$ python3 -m unittest discover -s tests -v
Ran 23 tests
OK
```

### Checkpoint 1 second review remediation

The second review found two remaining schema-boundary gaps. Three focused tests were added first: an unquoted frontmatter value containing colon-space, a single-quoted interface string with an unescaped apostrophe, and an unsupported evaluation type added alongside all five required types.

Focused RED:

```text
$ python3 -m unittest -v \
  tests.test_validate_repository.ValidateRepositoryTests.test_rejects_unquoted_skill_scalar_containing_colon_space \
  tests.test_validate_repository.ValidateRepositoryTests.test_rejects_single_quoted_scalar_with_unescaped_apostrophe \
  tests.test_validate_repository.ValidateRepositoryTests.test_rejects_unsupported_extra_evaluation_case_type
Ran 3 tests
FAILED (failures=3)
```

The first two failed because no `ValidationError` was raised. The third exposed only a later summary/case mismatch rather than rejecting the unsupported type at the cases schema boundary.

Focused GREEN:

```text
Ran 4 tests
OK
```

The GREEN run included the three regressions plus the valid final fixture, proving canonical generated `agents/openai.yaml` and valid plain SKILL frontmatter still pass. The accepted standard-library scalar subset and closed case-type vocabulary are now explicit in the implementation plan.
