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

## Checkpoint 2 progress: controlled theme normalization

- RED: the initial 17 focused projection tests all failed before
  `scripts/build_theme_projection.py` existed; later focused regressions also exposed
  nonstring projection identity handling and the `True == 1` schema-version bug.
- GREEN: 36 focused standard-library tests now cover exact schemas, strict types,
  complete raw-theme coverage, mapping arity/targets, deterministic projection,
  malformed/stale/missing/extra/duplicate/unsorted records, and byte-current
  read-only `--check` behavior.
- Two independent non-overlapping semantic partitions supplied exact mappings:
  `473` distinct labels for essays `001-112` and `499` for essays `113-223`, with
  `25` overlapping raw labels explicitly reconciled into `947` global mappings.
- Projection proof: `1,041` raw assignments, `947` distinct raw labels, `876`
  singleton raw labels, `112` canonical research themes, and `204` relevant essays.
  Raw audit labels remain unchanged, and the canonical vocabulary is explicitly not
  a skill taxonomy.
- Verification: default generation and `--check` both passed; full discovery
  reported `Ran 78 tests` and `OK`; Python compilation and `git diff --check` exited
  `0`.
- Remaining work in Checkpoint 2: independent semantic over/under-merge and compound/
  condition-loss re-review of the frozen map, followed by the full-corpus identity,
  retrieval, and copyright integrity pass.
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

## Checkpoint 2 progress: override-aware semantic remediation

- Override RED: six focused tests failed against the old global-only mapping schema
  (`Ran 6 tests`, `FAILED (failures=11)`). GREEN passed all six after implementing
  replacement article overrides; the complete focused projection suite now reports
  `48` passing tests.
- The non-destructive schema now permits a sorted article override only for a relevant
  essay that actually contains the raw label. Exact fields, reviewer, one-to-three
  targets, target sorting/uniqueness/definition, duplicate articles, deterministic
  replacement, override-inclusive canonical usage, and stale byte checks are enforced.
- Every exact finding in the integrated review and semantic red team was applied,
  including originality/writing boundaries, peer/team/maker concepts, bias and trust,
  investor direction, source-specific launch safety, venture/scaling semantics,
  urgency, historical qualifiers, role/adjective collisions, and evidence latency.
- Twelve article overrides disambiguate five recurrent labels: `talent attraction`,
  `founder support`, `owned projects`, `incentive alignment`, and `intellectual
  honesty`. Raw audit labels and the exact one-row-per-raw invariant are unchanged.
- Current proof: `1,041` assignments, `947` distinct raw labels, `876` singletons,
  `118` canonical research themes, `12` overrides, and `204` relevant essay
  projections. Default generation and `--check` pass with stable normalization hash
  `17628b5e...d9adcbb` and projection hash `470149c4...de88c13`.
- Full verification: `90` tests passed; Python compilation, audit validation, and
  `git diff --check` exited `0`.
- A fresh red-team pass narrowed its hold to nine rows. Updated production semantic
  expectations failed all nine old mappings before the exact source-specific repairs;
  the focused suite returned to `48` passing tests and full discovery returned to
  `90` passing tests. No other semantic mappings changed in this residual pass.
- Final re-review: both independent semantic reviewers approved the hash-pinned
  artifact with no open findings. The independent integrity reviewer separately
  reconfirmed corpus/audit/batch identity, retrieval/full-read proof, evidence-line
  validity, deterministic assembly/projection, override mechanics, and copyright
  hygiene.
- Remaining work: publish Checkpoint 2, then synthesize and independently challenge
  the minimal workflow taxonomy before authoring any skill.
- Blockers: none.

## Checkpoint 2 verified

- Corpus audit: `223` exact essays, `84` core startup, `120` supporting startup,
  `19` specifically excluded, `0` gaps or overlaps, and `223` recorded full reads.
- Retrieval: all `12` batches have successful BM25 and semantic QMD evidence; every
  assigned essay has a full-document retrieval record.
- Evidence: `616` relevant line ranges were independently checked against source
  bounds; canonical assembly is byte-idempotent.
- Normalization: `1,041` assignments, `947` exact raw labels, `876` singletons,
  `118` canonical research themes, `12` article overrides across five homonyms, and
  `204` relevant projections with `0` excluded projections.
- Stable hashes: normalization
  `17628b5e5349c93e22219807e44374121f5237c7988cae819232b7d07d9adcbb`;
  projection `470149c4a26eacd92ebf0bae344df664b668a407271744d023730fc54de88c13`.
- Review: the classification boundary, article-level theme/workflow corrections,
  integrated normalization, semantic red team, and non-semantic integrity checks
  all pass. The final semantic reviewers found no remaining over/under merge,
  compound loss, condition loss, or taxonomy leakage.
- Verification:

  ```text
  theme projection check passed: raw_assignments=1041 distinct_raw=947 singleton_raw=876 canonical=118 article_overrides=12 relevant_essays=204
  python3 -m unittest discover -s tests -v
  Ran 90 tests
  OK
  audit validation passed: corpus_files=223 manifest_essays=223 unique_assignments=223 batches=12 gaps=0 overlaps=0 classified=223 unaudited=0 audit_duplicates=0 core_startup=84 supporting_startup=120 excluded=19
  ```

- Copyright hygiene: independent broad and validator-style 40-token scans found
  `0` corpus matches in publishable repository artifacts.
- Remaining work: derive and review the minimal complete taxonomy, then execute the
  sequential per-skill RED-GREEN-REFACTOR, metadata, validation, forward-test,
  commit, and push loop.
- Blockers: none.

## Checkpoint 3 verified: evidence-led skill taxonomy

- Checkpoint 3 reopened five Checkpoint 2 exclusions after independent full-passage
  review. Articles `060`, `144`, `189`, `199`, and `210` are now supporting startup
  evidence. This deliberately supersedes the earlier `84/120/19`, `204`, and `118`
  counts while preserving the earlier checkpoint record as historical evidence.
- Corrected audit proof: `223` exact essays, `84` core startup, `125` supporting
  startup, `14` specifically excluded, `209` relevant, `223` recorded full reads,
  `622` relevant evidence ranges, and `0` gaps, overlaps, or uncovered relevant
  essays.
- Revised normalization proof: `1,059` raw assignments, `964` exact raw labels,
  `892` singletons, `122` canonical themes, `12` article overrides, and `209`
  relevant projections. Broad equity, adversarial, network, and policy labels were
  split by actor and runtime job before taxonomy ownership was assigned.
- The minimal complete taxonomy has `21` distinct reusable skill jobs and `831`
  reciprocal essay-skill pairings. Every canonical theme has exactly one primary
  owner; every final skill has source evidence; no essay-to-skill links are manually
  maintained outside deterministic derivation.
- Runtime conditions are explicit and checkable: `7` inherited decision invariants,
  a `6`-row product-type matrix, `9` cross-skill routing rules, and `42` structured
  two-sided branches covering all `42` named tensions across the `21` skills. The
  source declares exact `21/42/42` skill, stage-condition, and decision-branch
  totals; the validator rejects missing, duplicated, mismatched, empty, one-sided,
  or lockstep-deleted contract elements.
- Three independent fresh-context reviews all pass after RED remediation:
  coverage/gaps, routing/overlap, and conditions/contradictions. The routing review
  classified `54` adversarial prompts (`32` primary routes, `17` ordered
  compositions, and `5` non-triggers) without finding a duplicate primary job.
  Three non-blocking composition cases are carried forward as mandatory skill eval
  seeds: governance policy to anti-abuse engineering to rollout; unsettled writing
  to domain validation to communication; and ecosystem-level relocation policy to
  each team's location decision.
- Canonical assembly, theme projection, and taxonomy synchronization are byte-stable
  across a write cycle. The audit gate also byte-compares canonical audit output to
  all `12` primary batches, and taxonomy validation requires all three human-authored
  correction, normalization-revision, and taxonomy sources. Stable hashes:
  `b8e053c3...6c781be` (audit), `87a8c873...368598` (projection),
  `ac0c006e...847755` (normalization), `c4935a41...1a9f2a5` (taxonomy source), and
  `9459c8a3...ff1c3a` (derived taxonomy).
- Verification:

  ```text
  audit reclassification check passed: corrections=5 changed=0
  normalization revision check passed: canonical_themes=122 raw_mappings=964
  theme projection check passed: raw_assignments=1059 distinct_raw=964 singleton_raw=892 canonical=122 article_overrides=12 relevant_essays=209
  taxonomy check passed: skills=21 themes=122 relevant_essays=209 essay_skill_pairings=831 global_invariants=7 product_types=6 routing_rules=9 decision_branches=42
  taxonomy validation passed: corpus_files=223 classified=223 core_startup=84 supporting_startup=125 excluded=14 uncovered_relevant=0 orphan_skills=0
  python3 -m unittest discover -s tests
  Ran 112 tests
  OK
  ```

- Copyright hygiene: the repository-wide normalized `40`-token scan found `0`
  corpus matches in publishable artifacts.
- Remaining work: build each of the `21` skills sequentially through fresh-context
  baseline, official initialization, concise implementation, metadata generation,
  structural validation, independent forward testing, revision, commit, and push;
  then run final independent review, finish the README, and pass the final repository
  gate.
- Blockers: none.

## Checkpoint 4 skill 1 verified: `preparing-to-found`

- RED was recorded before skill authoring with five fresh-context cases spanning a
  trigger, non-trigger, ordinary application, stage/location condition, and the A3
  accelerator-policy composition edge. The frozen no-skill baseline scored `17/25`
  (`0.68`). Response-only files, separate scorecards, exact hashes, dispatch
  manifests, hidden-criteria declarations, and the no-skill state make the control
  reconstructable.
- The package was initialized with the official `skill-creator` tool. The final
  `SKILL.md` is `497` words, keeps preparation-versus-beginning and hub-access-versus-
  relocation-cost conditions executable, routes the mixed A3 request ecosystem-first
  and team-by-team second, and has SHA-256
  `ff2f0ae1ea51b2bd587791a32de603977c2acc9d150948ec2f091d46957730ff`.
  `agents/openai.yaml` was regenerated from that final file and official
  `quick_validate.py` reports `Skill is valid!`.
- Exact skill provenance covers all `55` assigned essays and all `6` owned themes.
  Three independent source reviewers re-read the complete assigned corpus files and
  produced claim/theme/range evidence. The generated reference contains only ranges
  contained in the canonical audit, plus corpus paths and both audit and skill-review
  lineage. Standalone tests reject duplicates, nonreciprocal assignments, and
  out-of-audit ranges.
- GREEN used a distinct fresh-context agent and the final frozen skill. The five
  responses scored `24/25` (`0.96`), a `+0.28` normalized improvement. One point was
  deliberately withheld because the paying-user answer tested one design partner
  before all three prospects. The repository evaluation helper independently accepts
  both baseline and forward manifests and current hashes.
- A five-repetition no-guidance wording control scored `[2, 2, 3, 2, 2]` (`0.44`).
  The first guided iteration exposed a repeated omission of existing local customers
  or committed capital, so wording was revised and all skill-dependent tests were
  regenerated. Five new single-shot guided contexts then scored `[5, 5, 5, 5, 5]`
  (`1.00`), a `+0.56` improvement with ten unique agent tasks and exact response
  hashes.
- The original transfer prompt was quarantined after review showed it predated the
  last wording revision. A wholly new procurement/cofounder/unpaid-leave case was
  authored after the final skill hash, generated blind by a fresh agent, and scored
  by an independent agent. Strict re-review corrected an overstated actual-use point
  in v3, and staging then found trailing Markdown whitespace. Rather than mutate that
  frozen response, fresh v4 generation and scoring produced a clean, hash-verified
  `5/5` PASS that explicitly operationalizes buyer/user, use, payment, team, and gate
  evidence.
- The first independent review's `4` Important and `3` Minor findings were all
  remediated: skill-specific provenance, canonical A3 order, honest scoring, durable
  freeze evidence, repeated/held-out transfer testing, sub-500-word guidance,
  standalone provenance lineage, and negative generator tests. A separate fresh
  final review reports `0` Critical, `0` Important, and Ready to commit: Yes. It notes
  only two nonblocking hardening opportunities: integrate extended-test/provenance
  freshness into the final repository gate and add a focused semantic assertion for
  the current A3 predicate.
- Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=55 themes=6
  taxonomy check passed: skills=21 themes=122 relevant_essays=209 essay_skill_pairings=831 global_invariants=7 product_types=6 routing_rules=9 decision_branches=42
  taxonomy validation passed: corpus_files=223 classified=223 unaudited=0 uncovered_relevant=0 orphan_skills=0
  python3 -m unittest discover -s tests
  Ran 120 tests
  OK
  extended evaluation integrity: micro_reps=10 unique_tasks=10 delta=0.56 heldout=5/5
  copyright scan: normalized 40-token corpus matches=0
  git diff --check: passed
  ```

- Remaining work: publish this verified skill milestone, then build the remaining
  `20` skills sequentially beginning with `building-startup-ecosystems`; finish the
  cross-skill final review, README catalog, and clean/pushed repository-wide final
  gate.
- Blockers: none.

## Checkpoint 4 skill 2 verified: `building-startup-ecosystems`

- RED used five fresh no-skill cases spanning a regional trigger, single-team
  non-trigger, university program, coercive residency condition, and the required
  A3 ecosystem-to-team composition. The frozen baseline scored `17/25` (`0.68`).
- Three independent source agents re-read all `19` assigned essays. Their `31`
  claim/theme records produce byte-current provenance for all `19` essays and all
  `3` owned themes. Source re-review corrected overstatements, separated voluntary
  attraction from coercive retention, and approved the final scope at SHA-256
  `9c90b05a4dc1c569fe63a03b5c41f7467b02d0b5872717d88f92badc3a000770`.
- The official initializer created the package. The final `SKILL.md` is `497` words;
  official validation passes, `agents/openai.yaml` was regenerated from the frozen
  file, and the provenance check reports `19` essays and `3` themes.
- RED-GREEN wording tests used five control and five guided single-shot contexts.
  Several hash-pinned iterations exposed an initially overbroad cohort gate and a
  repeated tendency to assume a cause. The final honest scores are control
  `[0, 0, 0, 0, 0]` and guided `[4, 4, 4, 4, 3]`, a normalized `+0.76`
  improvement with ten unique tasks and byte-matching responses. The systematic
  exact-three-hypothesis miss remains disclosed as a regression target; no score or
  rubric was weakened to hide it.
- The final blind five-case forward run used the frozen skill and hidden criteria.
  Independent scoring reports `24/25` (`0.96`), a `+0.28` improvement over the
  baseline. The only withheld point is an accelerator response lacking an actual
  revisit date and full relocation-cost accounting.
- A wholly new industrial-software case was authored after the final skill hash,
  generated blind, and scored by a third task. It passes `4/5`, exercising rival
  causal hypotheses and the population-wide-friction versus targeted-allocation
  boundary; the missing operational budget cap remains failed.
- Independent final review reports no Critical or Important findings and
  `Ready to commit: Yes`. It treats the disclosed wording variance as Minor because
  the skill explicitly requires discriminating hypotheses and both forward and
  held-out transfer evidence exercise the behavior without inflated scoring.
- Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=19 themes=3
  taxonomy validation passed: corpus_files=223 classified=223 relevant_essays=209 uncovered_relevant=0 orphan_skills=0
  baseline normalized_score=0.68; forward normalized_score=0.96
  microtest control=0/25; guided=19/25; normalized_delta=0.76
  heldout industrial-software-anchor-access=4/5 PASS
  python3 -m unittest discover -s tests
  Ran 120 tests
  OK
  copyright scan: normalized 40-token corpus matches=0
  git diff --check: passed
  ```

- Remaining work: publish this verified milestone, then build the remaining `19`
  skills sequentially beginning with `choosing-startup-opportunities`; finish the
  cross-skill final review, README catalog, and clean/pushed repository-wide gate.
- Blockers: none.
