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

### Checkpoint 1 third review remediation

A focused regression proved the plain-scalar parser still accepted a colon at end-of-string:

```text
$ python3 -m unittest -v \
  tests.test_validate_repository.ValidateRepositoryTests.test_rejects_unquoted_skill_scalar_ending_in_colon
Ran 1 test
FAILED (failures=1)
AssertionError: ValidationError not raised
```

The delimiter rule now rejects colon followed by whitespace or end-of-string. The focused GREEN run included the new regression, the existing colon-space regression, and the canonical valid final fixture:

```text
Ran 3 tests
OK
```

Full discovery then reported `Ran 27 tests` and `OK`.

### Checkpoint 1 canonical boundary remediation

Comparison with the official `quick_validate.py` frontmatter matcher exposed four remaining boundary cases. Focused tests were written first for indented opening and closing delimiters, an internal tab in a plain description, and a non-printable control character in a quoted interface scalar.

```text
$ python3 -m unittest -v <four focused canonical-boundary tests>
Ran 4 tests
FAILED (failures=4)
AssertionError: ValidationError not raised
```

The local final gate now requires exact column-zero delimiters and YAML-printable scalar characters, with literal tabs outside the accepted canonical subset. The same four regressions plus the valid final fixture then passed:

```text
Ran 5 tests
OK
```

Full discovery reported `Ran 31 tests` and `OK`; Python compilation, the manifest gate, and `git diff --check` also passed.

### Checkpoint 1 published

- Independent diff review: spec compliant; task quality approved; zero Critical, Important, or Minor findings remaining.
- Fresh controller verification: `31` tests passed, Python compilation exited `0`, manifest validation reported `223` corpus files, `223` unique batch assignments, `12` batches, `0` gaps, and `0` overlaps, and `git diff --check` exited `0`.
- Reviewed implementation head: `71292b1` (`fix: align skill metadata boundaries`).
- Published branch: `origin/codex/pg-isms-library`.
- Remaining work: complete all 12 audit batches, independent overlap/gap review, evidence-led taxonomy, sequential skill RED-GREEN-REFACTOR loops, final independent review, README, and final repository gate.
- Blockers: none.

## Checkpoint 2 progress: audit wave 1

- Primary coverage: batches `batch-01` through `batch-03`, articles `001-057`, with `57` ordered audit records and one full-document read per essay.
- Retrieval proof: every batch includes both BM25 and semantic QMD queries plus full-document evidence; no classification was made from snippets alone.
- Corrected classification counts: `14` core startup, `37` supporting startup, `6` excluded.
- Independent full-source review initially found `8` Important issues and no Critical issues. The batch reviewers corrected one core/supporting classification, one technical over-inclusion, and six missing/overstated evidence conditions. Re-review approved the wave with `0` Critical, `0` Important, and `0` Minor findings.
- Source limitation: article `004` is substantively stored on source line `10`; exact provenance is necessarily `10-10` and is documented in `research/batches/source-limitations-batch-01.md` without redistributing source text.
- Assembly infrastructure: `scripts/assemble_audit.py` was developed RED-GREEN and rejects article-set mismatches, reviewer/batch inconsistencies, missing BM25/vector evidence, or incomplete full-document coverage. It writes canonical outputs only when all 12 assignments exist.
- Remaining work: finish and review batches `04-12`, assemble the canonical audit, run the cumulative audit gate, and complete the cross-corpus overlap/gap review.
- Blockers: none.

## Checkpoint 2 progress: audit wave 2

- Primary coverage: batches `batch-04` through `batch-06`, articles `058-114`, with `57` ordered audit records and complete BM25, semantic, and full-document evidence.
- Classification counts: `28` core startup, `28` supporting startup, `1` excluded.
- Independent full-source review found `1` Critical, `5` Important, and `2` Minor issues: an equity-equation ambiguity; missing opportunity, location, platform, founder-sales, acquisition, risk, product-capital, and fundraising conditions; and two provenance overstatements.
- The original batch reviewers corrected all eight findings without changing classifications. Targeted re-review approved the wave with `0` Critical, `0` Important, and `0` Minor findings.
- Remaining work: finish/review batches `07-12`, assemble all `223` records, run the cumulative audit gate, and complete the cross-corpus overlap/gap review.
- Blockers: none.

## Checkpoint 2 progress: audit wave 3

- Primary coverage: batches `batch-07` through `batch-09`, articles `115-169`, with `55` ordered records and complete per-batch retrieval/full-read proof.
- Classification counts: `34` core startup, `18` supporting startup, `3` excluded.
- Independent review found `6` Important and `1` Minor issue, all involving applicability, stage, product-type, adoption-friction, launch-risk, or fundraising-phase conditions; no classification changes were requested.
- The batch reviewers corrected all seven findings. Targeted re-review approved the wave with `0` Critical, `0` Important, and `0` Minor findings and no new issues.
- Remaining work: close wave `04`, assemble all `223` records, run the cumulative audit gate, and perform the independent cross-corpus overlap/gap review.
- Blockers: none.

## Checkpoint 2 progress: audit wave 4

- Primary coverage: batches `batch-10` through `batch-12`, articles `170-223`, with `54` ordered records and complete per-batch retrieval/full-read proof.
- Final classification counts for the wave: `7` core startup, `36` supporting startup, `11` excluded.
- Independent review found `8` Important and `6` Minor issues plus one classification correction (`172`, core to supporting). Findings covered biographical overreach, ecosystem and supplier preconditions, stage/visibility scope, unsupported workflow extrapolations, and missing low-end-disruption, compounding-work, and young-founder conditions.
- The three batch reviewers corrected all `14` findings. Targeted re-review approved the wave with `0` Critical, `0` Important, and `0` Minor findings.
- Primary audit status: all `223` essays have now been read in full, explicitly classified in non-overlapping batches, and independently wave-reviewed.
- Remaining work: assemble the canonical audit/retrieval records, run the cumulative audit gate, and perform the separate full-corpus overlap/gap review for suspicious exclusions, inconsistent themes, and missed principles.
- Blockers: none.

## Checkpoint 2 progress: full-corpus reconciliation

- Canonical assembly covers all `12` non-overlapping batches and all `223` essays, with per-batch BM25, semantic, and full-document proof. A second assembly produced byte-identical canonical audit, reviewer, and retrieval artifacts.
- Independent classification-boundary review re-read every exclusion and challenged adjacent classifications. Five source-verified corrections were applied: `003`, `162`, and `208` moved from excluded to supporting; `060` moved from supporting to excluded; and `201` moved from supporting to core. Final counts are `84` core startup, `120` supporting startup, and `19` excluded.
- Independent theme/workflow review found ten article-level or cross-source issues (`I2-I8`, `M1-M3`). The original batch reviewers corrected all ten, preserving error-cost, evidence-latency, spending-state, luck, investor-truth, historical, product-type, and venture-type conditions. Fresh re-review reports `0` open article-level findings.
- Strict source-grounding follow-up also trimmed unsupported composition language from `003` and separated the editorial legal-freshness guardrail from the source-derived workflow for `162`.
- Current audit measures: `204` relevant essays, `712` candidate workflows, `616` evidence ranges, `1,041` raw theme assignments, `947` distinct raw theme labels, and `876` singleton labels.
- Verification:

  ```text
  audit assembly passed: batches=12 essays=223 bm25_batches=12 vector_batches=12 full_documents=223
  audit validation passed: corpus_files=223 manifest_essays=223 unique_assignments=223 batches=12 gaps=0 overlaps=0 classified=223 unaudited=0 audit_duplicates=0 core_startup=84 supporting_startup=120 excluded=19
  python3 -m unittest discover -s tests -v
  Ran 37 tests
  OK
  ```

- Independent boundary verdict: pass, with no remaining relabeling or source-grounding finding.
- Independent article-level theme verdict: pass for `I2-I8` and `M1-M3`; the sole remaining audit-phase blocker is `I1`, controlled normalization of the fragmented raw theme vocabulary before taxonomy synthesis.
- Remaining work in Checkpoint 2: complete and independently review the non-destructive raw-to-canonical theme normalization, then run the separate full-corpus identity/retrieval/copyright integrity pass.
- Blockers: none.
