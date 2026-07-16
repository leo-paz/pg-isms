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
  git diff --cached --check outside immutable generated/review Markdown: passed
  hash-bound evaluation Markdown retains original CommonMark hard breaks and EOF bytes
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

## Checkpoint 4 skill 3 verified: `choosing-startup-opportunities`

- RED froze five no-skill cases before initialization: fashionable idea search, a
  selected-direction non-trigger, a weak-demand pivot, ambition versus urgency, and
  the required opportunity-to-learning-to-growth composition. Independent scoring
  reports `20/25` (`0.80`), leaving a demanding `0.90` forward threshold.
- Three non-overlapping source agents read all `76` assigned essays in full and used
  both BM25 and semantic QMD retrieval. Their exact combined evidence contains `76`
  records and `105` owned essay-theme pairs across all `7` themes. Generated
  provenance is byte-current and all ranges remain audit-contained.
- The official initializer created the package. Routing and source reviews corrected
  channel ownership, the residual calibrated-decision route, product-type evidence,
  and four overbroad source claims. The final `SKILL.md` is `498` words with SHA-256
  `9c0a4b40025c646bbb494d4159fbf8b4b3e2861a6361f498544f435baacfa49a`;
  official validation and regenerated `agents/openai.yaml` pass.
- Five blind wording controls scored `[3, 2, 2, 2, 2]` (`0.44`). Five distinct
  guided contexts at the frozen hash scored `[4, 4, 4, 4, 5]` (`0.84`), a `+0.40`
  improvement with ten unique tasks and exact response hashes. Four guided answers
  fully documented only the chosen candidate; that disclosed residual is retained
  as a regression target.
- The blind five-case forward run scored `23/25` (`0.92`), improving `+0.12` over
  the high baseline. Points were withheld for an implicit rather than explicit
  learning-stage growth boundary and for omitting a concrete market-timing
  hypothesis in the pivot record.
- A new offshore-wind hardware pivot case was authored after the final skill hash,
  generated blind, and independently scored `4/5` PASS. It preserves prior learning
  and correct workflow ownership; the missing complete bench-to-onshore-to-offshore
  sequence and resource cap remain failed.
- Independent final review reports `0` Critical, `0` Important, three documented
  Minor residuals, and `Ready to commit: Yes`.
- Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=76 themes=7
  taxonomy validation passed: corpus_files=223 classified=223 relevant_essays=209 uncovered_relevant=0 orphan_skills=0
  baseline normalized_score=0.80; forward normalized_score=0.92
  microtest control=11/25; guided=21/25; normalized_delta=0.40
  heldout offshore-inspection-pivot-transfer=4/5 PASS
  python3 -m unittest discover -s tests
  Ran 120 tests
  OK
  copyright scan: normalized 40-token corpus matches=0
  git diff --check: passed
  ```

- Remaining work: publish this verified milestone, then build the remaining `18`
  skills sequentially beginning with `learning-from-users`; finish the cross-skill
  final review, README catalog, and clean/pushed repository-wide gate.
- Blockers: none.

## Checkpoint 4 skill 4 verified: `learning-from-users`

- RED froze five no-skill cases before authoring: praise without commitment, a
  validated-channel non-trigger, request-versus-observation diagnosis, a long-latency
  high-harm product, and the learning-to-growth composition boundary. Independent
  scoring reports `18/25` (`0.72`).
- Three source agents read all `54` assigned essays in full and used both BM25 and
  semantic QMD retrieval. Their exact combined evidence contains `54` records and
  `72` essay-theme pairs across all `8` owned themes. Final source remediation
  narrowed five noisy paraphrases, preserved exact batch lineage, and added a
  standalone reference for the inherited product-type and evidence-latency runtime
  contract. Provenance and 20/30/40-token copyright checks pass.
- The official initializer created the package. Source and route reviews corrected
  high-harm procurement scope and restored qualified expert review. The final
  `SKILL.md` is exactly `500` words with SHA-256
  `19dba2988470b9b2ac69025531765359a5d36838b2bb0d000db131dbe853bee9`;
  official validation and regenerated `agents/openai.yaml` pass.
- The first frozen forward run honestly failed at `19/25` (`0.76`), only `+0.04`
  above baseline. Its omissions drove a refactor requiring filled scenario-specific
  records, calendar dates, concrete actor-workflow-consequence claims, notification
  rivals, and separate high-harm hypotheses. All skill-dependent artifacts were then
  regenerated at the final hash. The final blind forward run scored `25/25` (`1.00`),
  a `+0.28` improvement, with exact case-payload hashes and canonical validation.
- Five blind no-guidance microtest controls scored `[0, 1, 2, 2, 1]` (`0.24`). Five
  distinct final-hash guided contexts scored `[5, 5, 5, 5, 5]` (`1.00`), a `+0.76`
  improvement with zero guided variance. All ten manifests now use one exact schema,
  ten unique tasks and response hashes, byte-current skill states, and a frozen
  rubric hash.
- A replacement pediatric-infusion case was authored only after the final skill
  freeze. Its plain decision-memo prompt does not repeat the skill recipe; prompt,
  criteria, full case, and response payloads are independently hashed. Blind
  generation and independent strict scoring produced `4/5` PASS. The retained miss
  is explicit: the memo did not assign pricing design to its downstream owner.
- A fresh final review reports `0` Critical, `0` Important, one nonblocking Minor,
  and `Ready: Yes`. The Minor is discoverability only: `runtime-contract.md` is not
  linked from the 500-word `SKILL.md`, while all operative guards remain inline and
  the reference citations are exact.
- Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=54 themes=8
  taxonomy validation passed: corpus_files=223 classified=223 relevant_essays=209 uncovered_relevant=0 orphan_skills=0
  baseline normalized_score=0.72; forward normalized_score=1.00; delta=0.28
  microtest control=6/25; guided=25/25; normalized_delta=0.76
  heldout pediatric-infusion-operations=4/5 PASS
  python3 -m unittest discover -s tests -p 'test_*.py'
  Ran 120 tests
  OK
  copyright scan: normalized 40-token corpus matches=0
  git diff --check: passed
  ```

- Remaining work: publish this verified milestone, then build the remaining `17`
  skills sequentially beginning with `shipping-and-iterating-products`; finish the
  cross-skill final review, README catalog, and clean/pushed repository-wide gate.
- Blockers: none.

## Checkpoint 4 skill 5 verified: `shipping-and-iterating-products`

- RED froze five no-skill cases before package initialization: a reversible first
  release, a high-harm fintech gate, a pure-architecture non-trigger, an
  installed-workflow redesign, and the shipping/engineering/learning/growth
  composition boundary. A canonical growth-ownership error in scenario 05 was
  corrected transparently after generation without changing any prompt or frozen
  response. The exact old and new criteria, cases hashes, identical prompt
  projections, and one-point stricter score effect are mechanically reconstructable.
  The independently rescored baseline is `14/25` (`0.56`).
- Three non-overlapping source agents read all `64` assigned essays in full and used
  both BM25 and semantic QMD retrieval. Their exact combined evidence contains `64`
  essay records, `101` essay-theme pairs, and `129` cited range occurrences across
  all `8` owned themes. Generated provenance is byte-current and every range remains
  audit-contained.
- The official initializer created the package. Source, route, and behavior reviews
  corrected overbroad source claims, exact workflow slugs, internal architecture
  ownership, and the distinction between a paid-segment growth handoff and
  permission to scale. The final `SKILL.md` is exactly `500` words with SHA-256
  `a627063ae70644a5c9d3d3c1c4b224d13b7f5573ce81293b28fac8fc8e2b0ffe`;
  official validation and regenerated `agents/openai.yaml` pass.
- Five blind no-guidance microtest controls scored `[2, 2, 2, 2, 3]` (`0.44`).
  Five distinct final-hash guided contexts received the strict fresh-context scores
  `[4, 4, 4, 5, 4]` (`0.84`), a `+0.40` improvement. A final evaluation review
  caught and corrected three initially over-credited ownership handoffs without
  changing the rubric, skill, prompts, responses, or hashes. All ten manifests use
  one exact schema, ten unique tasks, and byte-matching response hashes.
- The blind five-case forward run scored `23/25` (`0.92`), improving `+0.36` over
  baseline. The retained misses are a missing calendar release date and delayed
  growth ownership in scenario 05 despite paid pilots; broad-scaling restraint was
  correctly preserved.
- A new connected-irrigation hardware case was authored after the final skill hash,
  generated blind, and independently scored `4/5` PASS. It exercises installed
  workflows, offline recovery, firmware/API migration, and irreversible crop and
  water harm. The missing explicit shipping and business-model owner labels remain
  failed.
- Three final fresh-context reviews covered package behavior, evaluation integrity,
  and source/provenance/copyright. After the scoped scoring and reconstruction fixes,
  they report `0` Critical and `0` Important findings. Remaining notes concern
  transfer reliability, proportional middle-risk controls, standalone reference
  portability, and sidecar-bound scorer identity; none blocks this milestone.
- Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=64 themes=8
  taxonomy validation passed: corpus_files=223 classified=223 relevant_essays=209 uncovered_relevant=0 orphan_skills=0
  baseline normalized_score=0.56; forward normalized_score=0.92; delta=0.36
  microtest control=11/25; guided=21/25; normalized_delta=0.40
  heldout connected-irrigation-release-memo=4/5 PASS
  criterion correction: original cases hash and unchanged prompt projection reconstructed exactly
  python3 -m unittest discover -s tests -v
  Ran 120 tests
  OK
  copyright scan: normalized 40-token corpus matches=0
  git diff --check: passed
  ```

- Remaining work: publish this verified milestone, then build the remaining `16`
  skills sequentially beginning with `engineering-for-leverage`; finish the
  cross-skill final review, README catalog, and clean/pushed repository-wide gate.
- Blockers: none.

## Checkpoint 4 skill 6 verified: `engineering-for-leverage`

- RED froze five no-skill cases before package initialization: a familiar versus
  unusual runtime choice, stable versus speculative abstraction, a routine shipping
  non-trigger, coupled code ownership, and high-harm adversarial ingestion. The
  independent baseline is `3/25` (`0.12`).
- Three non-overlapping source agents read all `29` assigned essays in full and used
  both BM25 and semantic QMD retrieval. Their exact combined evidence contains `29`
  essay records, `47` essay-theme pairs, and `71` audit-contained range occurrences
  across all `7` owned themes. Generated provenance is byte-current with no gaps,
  extras, or duplicate pairs.
- The official initializer created the package. Repeated source, routing, and
  behavior reviews tightened the global survival and current-condition gates,
  growth handoff, representative workload, abstraction migration, end-to-end
  ownership, and high-harm assurance contract. The final `SKILL.md` is exactly
  `500` words with SHA-256
  `0caf290e03e05e10d7f83b10522e37930deea13f74b7b18d7ccc242be142cbb2`;
  official validation and regenerated `agents/openai.yaml` pass.
- Five blind no-skill microtest controls scored `[0, 0, 0, 0, 0]` (`0.00`). Five
  distinct final-hash guided contexts scored `[4, 3, 3, 5, 4]` (`0.76`), a `+0.76`
  normalized improvement. An independent audit reproduced all criterion vectors,
  means, population variances, prompt and response hashes, and ten unique tasks.
- The blind forward run is canonically `23/25` (`0.92`), improving `+0.80` over
  baseline. A first scorer had already announced `22/25` before a schema search
  exposed the baseline; its files are preserved as contaminated evidence and are
  not canonical. A path-restricted replacement scorer read no baseline or earlier
  scores and retained two explicit misses: a shipping handoff and a decision log.
- The first post-freeze warehouse-robot held-out attempt scored `3/5` FAIL and also
  exposed trailing whitespace in its frozen response; the complete attempt remains
  preserved. A genuinely new enterprise factory-edge case then used distinct
  author, generator, and scorer contexts and scored `5/5` PASS with exact prompt,
  criteria, case, skill, and response hashes.
- Final fresh-context source and evaluation audits report `0` Critical and `0`
  Important findings and `Ready to commit: Yes`. One nonblocking Minor records that
  non-held-out scorer provenance is stable-ID-bound rather than absolute-task-bound.
  The source audit independently reports `0` normalized 20/30/40-token matches; the
  longest source overlap is a seven-token essay title.
- Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=29 themes=7
  taxonomy validation passed: corpus_files=223 classified=223 relevant_essays=209 uncovered_relevant=0 orphan_skills=0
  baseline normalized_score=0.12; forward normalized_score=0.92; delta=0.80
  microtest control=0/25; guided=19/25; normalized_delta=0.76
  heldout enterprise-factory-edge-foundation=5/5 PASS
  preserved heldout warehouse-robot-production-control-foundation=3/5 FAIL
  python3 -m unittest discover -s tests -v
  Ran 120 tests
  OK
  copyright scan: normalized 40-token corpus matches=0
  git diff --check: passed
  ```

- Remaining work: publish this verified milestone, then build the remaining `15`
  skills sequentially beginning with `acquiring-and-growing-users`; finish the
  cross-skill final review, README catalog, and clean/pushed repository-wide gate.
- Blockers: none.

## Checkpoint 4 skill 7 verified: `acquiring-and-growing-users`

- RED froze five no-skill cases before package initialization: learning-owned
  recruitment, a paid marketplace cold start, an activation/retention collapse, an
  unvalidated waitlist non-trigger, and marketplace interaction governance. A final
  independent audit caught one overcredited placeholder activation event in scenario
  03. The frozen cases, responses, and manifest did not change; the corrected strict
  baseline is `12/25` (`0.48`).
- Three non-overlapping source agents read all `31` assigned essays in full and used
  both BM25 and semantic QMD retrieval. Their exact combined evidence contains `31`
  essay records, `44` unique essay-theme pairs, and `58` audit-contained range
  occurrences across all `7` owned themes. Independent overlap and final source
  reviews verified all prior claim-scope remediations, exact generated provenance,
  current-context conditions, and no gaps or extras.
- The official initializer created the package. Repeated behavior, routing, and source
  reviews tightened the learning handoff, business-model/channel split, governance
  sequence, support burden, and complete threshold/owner record. The final `SKILL.md`
  is `498` words with SHA-256
  `8d0a3145d9957bd16cfcd1130f9bb64af84f7ee7535ce1516b39d8530a981da4`;
  official validation and regenerated `agents/openai.yaml` pass.
- The blind forward run scored `20/25` (`0.80`), improving `+0.32` over the corrected
  baseline. Its five retained misses concern fully explicit marketplace thresholds
  and governance/shipping owners, an actual activation event and complete measure
  thresholds, and an intermediate shipping handoff. These remain failed rather than
  inferred; the frozen skill itself states each required behavior.
- Five blind no-skill microtest controls scored `[2, 1, 0, 1, 0]` (`0.16`). Five
  distinct final-hash guided contexts scored `[3, 3, 4, 4, 3]` (`0.68`), a `+0.52`
  improvement with lower population variance (`0.56` to `0.24`). The recurring miss
  is the rubric's compound founder-person/manual-owner requirement; final review
  distinguishes that scenario-specific conjunction from the canonical no-hidden-
  rescue rule and preserves it as a regression target.
- The first post-freeze hardware held-out response scored `4/5` on transfer but failed
  integrity because its frozen bytes contain trailing whitespace; it remains archived
  exactly and now exposes separate transfer-PASS/integrity-FAIL fields. A second,
  genuinely new walking-pod case scored `2/5` FAIL with clean integrity and is also
  preserved. A third B2B proposal-workflow case used another distinct author,
  generator, and scorer triple and scored `5/5` PASS with full integrity.
- Fresh final source and evaluation audits report `0` Critical, `0` Important, and
  `0` Minor findings. The final behavior review reports `0` Critical, `0` Important,
  and two accepted Minors for generated-answer completeness and the narrower
  founder-person microtest requirement. All three reviews say `Ready to commit: Yes`.
- Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=31 themes=7
  taxonomy validation passed: corpus_files=223 classified=223 relevant_essays=209 uncovered_relevant=0 orphan_skills=0
  baseline normalized_score=0.48; forward normalized_score=0.80; delta=0.32
  microtest control=4/25; guided=17/25; normalized_delta=0.52
  heldout growth-heldout-003=5/5 PASS integrity=PASS
  preserved hardware-regional-channel-versus-national-inventory-commitment=4/5 transfer PASS, integrity FAIL
  preserved walking-pod-consumer-channel-scale=2/5 transfer FAIL, integrity PASS
  python3 -m unittest discover -s tests -p 'test_*.py'
  Ran 120 tests
  OK
  copyright scan: normalized 20/30/40-token corpus matches=0/0/0
  git diff --check: passed
  ```

- Remaining work: publish this verified milestone, then build the remaining `14`
  skills sequentially beginning with `designing-business-models`; finish the
  cross-skill final review, README catalog, and clean/pushed repository-wide gate.
- Blockers: none.

## Checkpoint 4 skill 8 verified: `designing-business-models`

- RED froze five no-skill cases before package initialization: a useful free product
  with no payer, a hardware make-or-partner boundary, segment pricing and sales,
  a term-sheet non-trigger, and a durable consultancy under venture pressure. The
  independently scored baseline is `6/25` (`0.24`).
- Three non-overlapping source agents read all `29` assigned essays in full and used
  both BM25 and semantic QMD retrieval. Their exact combined evidence contains `29`
  essay records, `35` unique essay-theme pairs, and `56` audit-contained range
  occurrences across all `7` owned themes. Independent overlap and source reviews
  verified every range, exact generated provenance, both canonical tensions, all
  applicable routes and product rows, and zero gaps or extras.
- The official initializer created the package. Repeated behavior and routing reviews
  tightened post-value evidence execution, per-segment economic actors, marketplace
  liquidity ownership, complete venture paths, product-row factors, numeric branch
  thresholds, and all specialist handoffs. The final `SKILL.md` is `498` words with
  SHA-256
  `fe50d245ee40ee68ee7e722089d83797f76ce62e3fd0a0e9a26608b933397ad0`;
  official validation and regenerated `agents/openai.yaml` pass.
- Four blind forward attempts remain visible. Attempt 001 scored `14/25` and drove
  the first output-contract revision. Attempt 002 scored `21/25` but is explicitly
  rejected as evaluator-invalid because of missing response headers and schema/path
  drift. Attempt 003 was mechanically valid but scored `17/25`. The canonical fourth
  attempt scored `23/25` (`0.92`), improving `+0.68` over baseline. Its two retained
  misses are an incomplete heavy-cost-account row and a missing settled-offer
  communication handoff; both requirements remain explicit in the frozen skill.
- The first five-plus-five microtest scored `0.00` control versus `0.76` guided but
  lacked pre-generation proof that criteria were hidden, so it is retained as an
  integrity-incomplete attempt. A full fresh rerun used a frozen pre-generation plan,
  prompt-only projection, per-response isolation/freeze manifests, and a batch
  attestation. After formatting-only normalization and a fresh rescore, canonical
  control scores are `[0, 1, 0, 1, 0]` (`0.08`); guided scores are
  `[5, 5, 5, 5, 5]` (`1.00`), a `+0.92` normalized improvement with ten unique
  tasks and response hashes.
- The first post-freeze energy-infrastructure held-out case used distinct author,
  generator, and scorer contexts and scored `2/5` FAIL with full integrity; it is
  preserved unchanged. A genuinely new pre-clearance diagnostics case used another
  distinct triple and scored `5/5` PASS at a `4/5` threshold with exact prompt,
  criteria, case, skill, generation-manifest, and response hashes.
- Final source, behavior, routing, package, and evaluation-integrity reviews report
  `0` Critical and `0` Important findings and `Ready: Yes`. Accepted Minors concern
  generated-answer variance, held-out schema vocabulary drift, and chronology that
  becomes immutable at this commit; none weakens the canonical evidence.
- Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=29 themes=7
  taxonomy validation passed: corpus_files=223 classified=223 relevant_essays=209 uncovered_relevant=0 orphan_skills=0
  baseline normalized_score=0.24; forward normalized_score=0.92; delta=0.68
  microtest control=2/25; guided=25/25; normalized_delta=0.92
  heldout business-model-heldout-002=5/5 PASS integrity=PASS
  preserved business-model-heldout-001=2/5 FAIL integrity=PASS
  python3 -m unittest discover -s tests -p 'test_*.py'
  Ran 120 tests
  OK
  copyright scan: normalized 20/30/40-token corpus matches=0/0/0
  git diff --check: passed
  ```

- Remaining work: publish this verified milestone, then build the remaining `13`
  skills sequentially beginning with `competing-and-positioning`; finish the
  cross-skill final review, README catalog, and clean/pushed repository-wide gate.
- Blockers: none.

## Checkpoint 4 skill 9 verified: `competing-and-positioning`

- RED froze five no-skill cases before package initialization: an unvalidated AI
  demo distracted by funded rivals, an incumbent-suite bundle, a platform
  dependency, a community-governance non-trigger, and open-model commoditization.
  The independently scored baseline is `10/25` (`0.40`).
- Three non-overlapping source agents read all `31` assigned essays in full and used
  both BM25 and semantic QMD retrieval. Their exact combined evidence contains `31`
  essay records, `44` unique essay-theme pairs, and `70` audit-contained range
  occurrences across all `7` owned themes. Independent overlap and source reviews
  verified every range, generated provenance, current-condition qualifier, tension,
  and routing boundary with zero gaps or extras.
- The official initializer created the package. Repeated behavior, routing, source,
  and contract reviews tightened the user and outcome gates, wedge test, direct and
  adjacent substitute comparison, mechanism analysis, switching constraints,
  distribution leverage, stop/keep/learn decision record, and specialist handoffs.
  The final `SKILL.md` is exactly `500` words with SHA-256
  `e26c7880d81927bacdf441847e9b14d755616fad14ac3128430974800840ed53`;
  official validation and regenerated `agents/openai.yaml` pass.
- The canonical blind forward run scored `19/25` (`0.76`), improving `+0.36` over
  baseline. Its six retained misses concern competitor-scan mechanism and timing,
  an installed-base hypothesis, platform incentives and billing portability,
  enforcement proportionality and due process, and entrant/incumbent incentives;
  none is inferred or silently upgraded. Five isolated generation sessions and a
  separate strict scorer session are recorded with exact response hashes.
- The canonical microtest used ten unique fresh tasks. Blind controls scored
  `[0, 0, 0, 0, 0]` (`0.00`); final-hash guided responses scored
  `[5, 5, 5, 5, 4]` (`0.96`), a `+0.96` normalized improvement. Its integrity audit
  reproduces all vectors, sessions, prompt projections, and response hashes.
- Earlier forward and held-out attempts remain archived with their failure reasons,
  including behavior-hash invalidation, prompt leakage, mixed-rubric failure, and a
  held-out prompt that supplied the option taxonomy it was meant to elicit. The
  canonical post-freeze held-out case instead uses a natural vendor-security review
  prompt authored after the final skill hash, with distinct author, generator, and
  scorer contexts. It scored `4/5` PASS with exact case, prompt, response, skill,
  runtime, and manifest hashes; the sole retained miss is exact outcome-precedence
  wording.
- Final fresh-context source, behavior, and evaluation-contract reviews report `0`
  Critical, `0` Important, and `0` Minor findings and `Ready to commit: Yes`. The
  evaluation reviewer confirms that direct parsing succeeds, all five scorecards
  meet the literal schema, and repository final validation advances through every
  skill 9 artifact before stopping at the intentionally future independent final
  repository review.
- Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=31 themes=7
  taxonomy validation passed: corpus_files=223 classified=223 relevant_essays=209 uncovered_relevant=0 orphan_skills=0
  baseline normalized_score=0.40; forward normalized_score=0.76; delta=0.36
  microtest control=0/25; guided=24/25; normalized_delta=0.96
  heldout positioning-heldout-018=4/5 PASS integrity=PASS
  python3 -m unittest discover -s tests -p 'test_*.py'
  Ran 120 tests
  OK
  copyright scan: normalized 20/30/40-token corpus matches=0/0/0
  git diff --check: passed
  ```

- Remaining work: publish this verified milestone, then build the remaining `12`
  skills sequentially beginning with `forming-founder-partnerships`; finish the
  cross-skill final review, README catalog, and clean/pushed repository-wide gate.
- Blockers: none.

## Checkpoint 4 skill 10 verified: `forming-founder-partnerships`

- RED froze and independently scored five no-skill cases before package
  initialization: founder selection under weak prior collaboration, an ownership
  request before contribution evidence, an existing-team trust break, a role-only
  organization non-trigger, and a safety-sensitive separation. The baseline scored
  `6/25` (`0.24`).
- Independent source review read all `12` assigned essays in full, checked every
  cited range in context, and used both BM25 and semantic QMD retrieval to test for
  missing principles. The generated provenance covers exactly `12` essays and both
  owned themes; the article `069` relationship-durability override projects
  correctly, and no source, mapping, or copyright gap remains.
- The official initializer created the package. Repeated behavior, routing, source,
  and evaluation reviews tightened route precedence, candidate versus existing-team
  modes, observation-versus-claim labels, reversible trials, trust and safety gates,
  ownership restraint, and current legal handoff. The final `SKILL.md` is `474`
  words with SHA-256
  `a1bd8c331837d5e8a1177ab774b7d4f3e6a7a6d2d11b4293333fed445d77d584`;
  official validation and regenerated `agents/openai.yaml` pass.
- The blind forward run scored `18/25` (`0.72`), improving `+0.48` over baseline.
  Its seven retained misses remain explicit rather than inferred, including complete
  evidence classification, sharper branch ownership, and scenario-specific safety,
  legal, or decision-threshold fields.
- The accepted paired microtest is attempt `017`. Five isolated controls scored
  `[1, 1, 1, 1, 1]` (`0.20`); five distinct final-hash guided contexts scored
  `[3, 3, 3, 2, 3]` (`0.56`), a `+0.36` normalized improvement. A blind Stage A
  reviewer challenged one inferred guided bit; Stage B sustained the challenge, and
  the official scorer amended only that bit before the final exact-agreement review.
  All ten envelopes, traces, hashes, identities, lifecycle events, and forbidden-event
  checks reproduce. Earlier contract-invalid, contaminated, driver-failed, stderr,
  and envelope-invalid attempts remain archived outside the canonical evaluation.
- The post-freeze held-out case used distinct author, prompt reviewer, generator,
  scorer, and final reviewer contexts. It scored `[1, 1, 1, 1, 0]` (`4/5`) PASS with
  integrity and naturalness both PASS; the retained miss is the final continuity
  condition, not an inferred success.
- Fresh final source, behavior, and evaluation-integrity reviews each report `0`
  Critical, `0` Important, and `0` Minor findings and `Ready to commit: Yes`. The
  evaluation reviewer independently reproduced `280/280` assertions with zero
  failures.
- Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=12 themes=2
  theme projection check: canonical=122 article_overrides=17 relevant_essays=209
  taxonomy sync check: skills=21 themes=122 relevant_essays=209 essay_skill_pairings=832
  taxonomy validation passed: corpus_files=223 classified=223 relevant_essays=209 uncovered_relevant=0 orphan_skills=0
  baseline normalized_score=0.24; forward normalized_score=0.72; delta=0.48
  microtest control=5/25; guided=14/25; normalized_delta=0.36
  heldout founder-partnerships-heldout-attempt-028=4/5 PASS integrity=PASS
  python3 -m unittest discover -s tests -p 'test_*.py'
  Ran 120 tests
  OK
  copyright scan: normalized 20/30/40-token corpus matches=0/0/0
  git diff --check outside immutable microtest byte fixtures/responses: passed
  immutable microtest files retain hash-bound trailing-space and EOF probes
  ```

- Remaining work: publish this verified milestone, then build the remaining `11`
  skills sequentially beginning with `building-and-evolving-organizations`; finish
  the cross-skill final review, README catalog, and clean/pushed repository-wide gate.
- Blockers: none.

## Checkpoint 4 skill 11 verified: `building-and-evolving-organizations`

- RED froze five no-skill cases before package initialization: a premature
  management layer, ambiguous decision rights, a measurement-side-effects case, a
  continuity-sensitive role transition, and a specialist-routing non-trigger. A
  criteria-only remediation preserved every prompt and response byte and received a
  fresh blind rescore. The canonical baseline is `1/25` (`0.04`); an additive note
  corrects the historical manifest's contradictory rescore-required flag without
  mutating the committed RED evidence.
- Independent source agents read all `64` assigned essays in full and used both BM25
  and semantic QMD retrieval. The exact evidence contains `64` essay records, `100`
  theme entries, and `127` audit-contained ranges across all `9` owned themes.
  Generated provenance and the narrow 028/039/046 supplemental mappings reproduce
  exactly, with no uncovered source or theme.
- The official initializer created the package. Repeated source, behavior, routing,
  and contract reviews tightened branch selection, observation/claim/unknown
  discipline, ownership and interface design, reversible operating tests, capacity
  gates, continuity, and specialist handoffs. The final `SKILL.md` is `431` words
  with SHA-256
  `2a1e0a27562aa3cfac61ce280a833bd538e4ad633267e238d8cf7bed695e572a`;
  official validation and regenerated `agents/openai.yaml` pass.
- Five isolated blind forward responses scored `14/25` (`0.56`), improving `+0.52`
  over baseline. The retained misses remain explicit rather than inferred, including
  route rejection, evidence-ledger completeness, operating-contract coverage, and
  result-specific closure ownership.
- The paired microtest froze its natural 365-word prompt, five strict criteria,
  package hashes, ten unique task identities, and the `+0.20` gate before generation.
  Five controls scored `2/25` (`0.08`); five guided responses scored `15/25`
  (`0.60`), a `+0.52` effect. A two-stage independent review corrected guided rep 4
  C5 from 1 to 0 because its Keep branch omitted the next owner. The initial score,
  immutable Stage A judgment, correction, and final score are all preserved with
  exact hashes; no response was edited or regenerated.
- Held-out attempts 001 and 002 scored `3/5` and `1/5` and remain byte-preserved as
  integrity-clean failures. Attempt 003 used another distinct author, prompt
  reviewer, generator, scorer, and final reviewer set and scored `5/5` PASS. An
  additive preservation index resolves the failed attempts' historical root paths
  without rewriting their frozen manifests.
- Fresh final package/source review reports `0` Critical, `0` Important, and one
  accepted Minor concerning conflicting upstream date metadata that no package
  chronology claim uses. The remediated final evaluation review reports `0`
  Critical, `0` Important, and `0` Minor findings and `Ready to commit: Yes`.
- Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=64 themes=9
  theme projection check: canonical=122 article_overrides=19 relevant_essays=209
  taxonomy sync check: skills=21 themes=122 relevant_essays=209 essay_skill_pairings=835
  taxonomy validation passed: corpus_files=223 classified=223 relevant_essays=209 uncovered_relevant=0 orphan_skills=0
  baseline normalized_score=0.04; forward normalized_score=0.56; delta=0.52
  microtest control=2/25; guided=15/25; normalized_delta=0.52
  heldout org-heldout-attempt-003=5/5 PASS integrity=PASS
  preserved org-heldout-attempt-001=3/5 FAIL integrity=PASS
  preserved org-heldout-attempt-002=1/5 FAIL integrity=PASS
  python3 -m unittest discover -s tests -p 'test_*.py'
  Ran 120 tests
  OK
  copyright scan: normalized 20/30/40-token corpus matches=0/0/0
  git diff --cached --check outside hash-bound generated/review Markdown: passed
  allowlisted generated/review Markdown retains exact response or review hashes and intentional CommonMark hard breaks
  ```

- Remaining work: publish this verified milestone, then build the remaining `10`
  skills sequentially beginning with `operating-with-focus-and-morale`; finish the
  cross-skill final review, README catalog, and clean/pushed repository-wide gate.
- Blockers: none.

## Checkpoint 4 skill 12 verified: `operating-with-focus-and-morale`

- Source audit: three independent partitions reconciled to `63` exact essays and
  `7` owned themes. Projection, canonical audit, taxonomy, evidence JSON, and
  generated provenance are reciprocal; article `159` remains only as a documented
  boundary source. Final package review found two theme-pair lineage gaps; a fresh
  BM25, semantic, and full-document re-audit removed unsupported article `126` →
  `resourcefulness-and-agency` while retaining and re-attributing article `147` →
  `attention-and-priority-control`.
- RED baseline: six fresh no-skill cases scored `14/30 = 0.466667` with frozen
  criteria and independent review.
- Package: official skill scaffold, `494`-word `SKILL.md`, generated
  `agents/openai.yaml`, `63`-record evidence map, generated provenance, and a
  progressive runtime contract. Final hashes are SKILL
  `8cb42d33741e49adfb6412bcedb88106491f0041324486115aa4ffdf362245cc`
  and runtime
  `24ec2d982c69da54dc1c6474032e898ee4da22e3f10a8b0bd2a7c4dadeeb2336`.
- GREEN forward: six final-hash fresh agents, hidden criteria, length-only staging,
  and frozen canonical responses scored `23/30 = 0.766667`; delta
  `+9/30 = +0.30` exceeds the required `+0.10`. A second reviewer rejudged all
  `30` bits with zero changes.
- Auxiliary paired transfer: a new educational card-game microtest generated `5`
  control and `5` guided responses. Its observed arithmetic was `0/25` versus
  `12/25`, but final integrity review invalidated it for confirmatory use: four
  guided outputs exceeded the hard word cap while every control conformed, and the
  promised second blind scorer was not executed. All outputs and raw scores remain
  unedited as failed-protocol exploratory evidence; the delta is not acceptance
  evidence.
- Auxiliary held-out stress evidence: invalid attempt `002` was excluded by independent
  design audit; valid attempt `003` motivated the final no-invented-backup and
  checkpoint refactor; attempt `004` was frozen unscored over the word cap;
  fairness-audited attempt `005` scored `4/5`, missing only separate IDs for two
  preserved same-speaker claims. It is retained as a non-passing limitation with
  no repair or resampling. The repository also records that this attempt lacks a
  reconstructable execution attestation, so it is not used for acceptance.
- The PROJECT_BRIEF quality contract relies on the separately frozen RED baseline
  and fresh-context forward evaluation, not either auxiliary test. Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=63 themes=7
  theme projection check: canonical=122 article_overrides=30 relevant_essays=209
  taxonomy sync check: skills=21 themes=122 relevant_essays=209 essay_skill_pairings=831
  taxonomy validation passed: corpus_files=223 classified=223 relevant_essays=209 uncovered_relevant=0 orphan_skills=0
  baseline normalized_score=0.466667; forward normalized_score=0.766667; delta=0.30
  python3 -m unittest discover -s tests -p 'test_*.py'
  Ran 120 tests
  OK
  copyright scan: normalized 20/30/40-token corpus matches=0/0/0
  git diff --check: passed
  ```

- Independent remediation reviews report `0` Critical, `0` Important, and `0`
  Minor findings for both package/source integrity and evaluation integrity; both
  conclude `ready_to_commit: true`. The source reviewer confirmed exact 126/147
  pair remediation, and the evaluation reviewer independently recomputed the valid
  required gate while confirming the auxiliary tests are excluded from acceptance.

- Library progress after the required quality-contract milestone: `12/21` planned
  skills implemented; skill `13` is next. Blockers under PROJECT_BRIEF: none.

## Checkpoint 4 skill 13 verified: `managing-runway-and-survival`

- Source audit: three independent, non-overlapping batches covered all `32`
  taxonomy-assigned essays with BM25 and semantic QMD retrieval plus complete local
  source reads. The union retained `28` essays and exactly `85` essay-theme pairs,
  removed false triggers `029`, `048`, `089`, and `117`, and relabeled `129` to
  startup economics and risk. The executable article-scoped reconciliation preserves
  prior cross-skill themes while reproducing the exact six-theme runway source set.
- RED baseline: five fresh no-skill cases scored `5/25 = 0.20`. The cases cover an
  assumed future round, a profitable company underinvesting in a proven engine, a
  sparse-history capital-heavy regulated product, a healthy financing non-trigger,
  and an acute cash/continuity state. A separate auditor rejudged every bit before
  the documented mechanical validator wrappers were added.
- Package: the official initializer created a `455`-word `SKILL.md`, progressive
  runtime contract, `agents/openai.yaml`, `28`-record/`85`-pair evidence map,
  generated provenance, and source re-audit. Final behavior hashes are SKILL
  `4d900b3e4b60b8f75dc4ecddf0be016030227c3c204928b8869931f621809d0d`
  and runtime
  `f7dd9dcd99144b59a3191c1e2cf2104ce61e66bfd891add83cb911a2ddb52b48`.
- GREEN forward: five distinct fresh-context agents received only one prompt plus
  the frozen SKILL/runtime, with hidden criteria and length-only staging. Strict
  scoring was `18/25 = 0.72`, a `+0.52` normalized improvement. An independent
  auditor re-scored all `25` bits with zero changes and verified both forward hashes
  and the baseline wrapper/body-hash chain.
- A fresh package review found no Critical or Important issues and one accepted Minor:
  some generated responses still omitted fields the runtime explicitly requires.
  All branch-family criteria passed, and the retained misses are recorded rather than
  inferred away. The same review confirmed no cross-skill provenance regression and
  `ready_to_commit: true`.
- Verification:

  ```text
  Skill is valid!
  skill provenance check: essays=28 themes=6
  all 13 implemented package provenance checks: passed
  theme projection check: canonical=122 article_overrides=75 relevant_essays=209
  taxonomy sync check: skills=21 themes=122 relevant_essays=209 essay_skill_pairings=827
  taxonomy validation passed: corpus_files=223 classified=223 relevant_essays=209 uncovered_relevant=0 orphan_skills=0
  baseline normalized_score=0.20; forward normalized_score=0.72; delta=0.52
  python3 -m unittest discover -s tests -p 'test_*.py'
  Ran 124 tests
  OK
  copyright scan: normalized 20/30/40-token corpus matches=0/0/0
  git diff --check: passed
  ```

- Library progress after the required quality-contract milestone: `13/21` planned
  skills implemented; skill `14` is next: `raising-and-governing-capital`.
  Blockers under PROJECT_BRIEF: none.
