# pg-isms Skill Library Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a compact Codex skill library derived from every startup-relevant essay in the 223-document local Paul Graham corpus.

**Architecture:** Keep source research separate from runtime skill packages. Store one mechanically validated JSONL audit record per essay, synthesize the final taxonomy only after audit completion, and keep concise skill instructions linked to one-level-deep provenance references. Use a cumulative repository validator with explicit `manifest`, `audit`, `taxonomy`, and `final` gates so each checkpoint proves progressively stronger invariants without weakening the final acceptance criteria.

**Tech Stack:** Markdown and YAML skill packages, JSON/JSONL research records, Python 3 standard-library validation and tests, QMD BM25/vector retrieval, git, and fresh-context Codex subagents.

## Global Constraints

- Treat `PROJECT_BRIEF.md` as the source of truth.
- Audit exactly 223 corpus Markdown files from `/Users/leopaz/dev/opensource/graham-essays/corpus`.
- Invoke QMD as `PATH=/Users/leopaz/.nvm/versions/node/v22.23.0/bin:$PATH qmd --index graham-essays ...`.
- Use both BM25 `qmd search` and semantic `qmd vsearch`; retrieve full relevant passages with `qmd get` or the corpus file before recording evidence.
- Never redistribute full essays or long passages; store paraphrase, source URL, essay identifier, and exact line ranges.
- Derive taxonomy only after the audit; prefer a compact set of distinct startup workflows and mental models.
- Initialize every skill with official `skill-creator` tooling, generate `agents/openai.yaml`, structurally validate it, and keep `SKILL.md` concise.
- Run a fresh-context failing baseline before authoring every behavior-shaping skill and use different fresh-context agents for forward tests.
- Complete, validate, commit, and push one skill before starting the next.
- Use subagents for non-overlapping essay audits, fresh-context evaluation, and independent synthesis/final review.
- Commit and push meaningful verified milestones; finish only with a clean worktree and local HEAD equal to `origin/codex/pg-isms-library`.

---

## File Map

- `research/audit-schema.json`: machine-readable audit record contract.
- `research/corpus-manifest.json`: canonical 223-file metadata inventory generated from corpus frontmatter.
- `research/audit-batches.json`: explicit non-overlapping article-number assignments and reviewer identities.
- `research/batches/*.jsonl`: isolated subagent batch results.
- `research/essay-audit.jsonl`: canonical article-number-sorted audit assembled from batches.
- `research/retrieval-log.jsonl`: BM25/vector queries and full-document reads used during audit and synthesis.
- `research/theme-synthesis.md`: merged principles, tensions, stage conditions, exclusions, and taxonomy rationale.
- `research/taxonomy.json`: final skills, trigger/non-trigger cases, themes, and covered essay identifiers.
- `research/progress.md`: checkpoint evidence, exact validation commands/results, commits, pushes, and remaining work.
- `scripts/build_research_scaffold.py`: deterministic corpus metadata, batch, and empty audit-scaffold generator.
- `scripts/validate_repository.py`: cumulative `manifest`, `audit`, `taxonomy`, and `final` validation.
- `tests/test_build_research_scaffold.py`: generator behavior tests.
- `tests/test_validate_repository.py`: validator behavior and regression tests.
- `evals/<skill-name>/cases.json`: trigger, non-trigger, application, edge, and pressure scenarios.
- `evals/<skill-name>/baseline/*.md`: raw fresh-context outputs without the skill and scored gaps.
- `evals/<skill-name>/forward/*.md`: raw fresh-context outputs with the skill and comparative scores.
- `skills/<skill-name>/SKILL.md`: concise imperative runtime workflow.
- `skills/<skill-name>/agents/openai.yaml`: generated UI metadata.
- `skills/<skill-name>/references/provenance.md`: incorporated essays, paraphrased principles, conditions, and exact line ranges.
- `README.md`: verified catalog, triggers, non-triggers, installation, and use.

### Task 1: Research Scaffold and Cumulative Validator

**Files:**
- Create: `tests/test_build_research_scaffold.py`
- Create: `tests/test_validate_repository.py`
- Create: `scripts/build_research_scaffold.py`
- Create: `scripts/validate_repository.py`
- Create: `research/audit-schema.json`
- Create: `research/corpus-manifest.json`
- Create: `research/audit-batches.json`
- Create: `research/retrieval-log.jsonl`
- Create: `research/progress.md`

**Interfaces:**
- `build_research_scaffold.py --corpus PATH --output-root PATH --batch-count 12` reads corpus frontmatter and emits a sorted manifest plus 12 explicit contiguous, non-overlapping batches whose sizes differ by at most one.
- `validate_repository.py --phase {manifest,audit,taxonomy,final} --repo PATH --corpus PATH` exits 0 only when all invariants through the requested phase pass and prints count-based proof.
- Audit records contain `article_no`, `title`, `source_url`, `corpus_path`, `classification`, `exclusion_reason`, `themes`, `candidate_workflows`, `final_skills`, `evidence_line_ranges`, `review_batch`, `reviewer`, and `full_text_read`.

- [ ] **Step 1: Write failing scaffold tests**

  Test corpus metadata parsing, deterministic numeric sorting, exact 223-document count, twelve batches, full set equality, no duplicate assignments, no gaps, and balanced batch sizes.

- [ ] **Step 2: Run scaffold tests and verify RED**

  Run: `python3 -m unittest tests.test_build_research_scaffold -v`

  Expected: `FAIL` or `ERROR` because the generator does not exist.

- [ ] **Step 3: Write failing validator tests**

  Use temporary repositories to prove the validator rejects: a missing essay, duplicate article number, invalid classification, excluded essay without a specific reason, relevant essay without themes/evidence, taxonomy coverage gaps, missing skill package metadata, missing evaluation evidence, stale README catalog entries, and unexpected long source excerpts.

- [ ] **Step 4: Run validator tests and verify RED**

  Run: `python3 -m unittest tests.test_validate_repository -v`

  Expected: `FAIL` or `ERROR` because the validator does not exist.

- [ ] **Step 5: Implement the minimum generator and validator**

  Use only the Python standard library. Treat phase gates cumulatively: `manifest` proves exact corpus identity and batch partition; `audit` adds complete classifications and research evidence; `taxonomy` adds theme/final-skill coverage; `final` adds independent review evidence, packages, evaluations, README catalog consistency, copyright-hygiene heuristics, and a clean/pushed git check when run in the real repository.

- [ ] **Step 6: Verify GREEN and generate checkpoint artifacts**

  Run:

  ```bash
  python3 -m unittest discover -s tests -v
  python3 scripts/build_research_scaffold.py \
    --corpus /Users/leopaz/dev/opensource/graham-essays/corpus \
    --output-root . \
    --batch-count 12
  python3 scripts/validate_repository.py \
    --phase manifest \
    --repo . \
    --corpus /Users/leopaz/dev/opensource/graham-essays/corpus
  ```

  Expected: all tests pass; manifest validation reports 223 corpus files, 223 unique assignments, 12 batches, zero gaps, and zero overlaps.

- [ ] **Step 7: Record and publish checkpoint 1**

  Append commands, results, QMD index proof (`223 files`, `1582 vectors`), BM25/vector query examples, one full-document retrieval, remaining work, and blockers to `research/progress.md`.

  Run:

  ```bash
  git add docs scripts tests research
  git commit -m "research: add corpus audit scaffold"
  git push -u origin codex/pg-isms-library
  ```

  Expected: commit succeeds and `git status --short --branch` shows `codex/pg-isms-library...origin/codex/pg-isms-library` with no changes.

### Task 2: Complete the 223-Essay Audit

**Files:**
- Create: `research/batches/audit-001-019.jsonl` through the exact ranges emitted in `research/audit-batches.json`
- Modify: `research/retrieval-log.jsonl`
- Create: `research/essay-audit.jsonl`
- Modify: `research/progress.md`

**Interfaces:**
- Each batch writer may edit only its assigned batch JSONL and a uniquely named retrieval-log fragment.
- Each record must represent a full essay read, not a snippet judgment; relevant claims require exact line ranges.
- Classification vocabulary is exactly `core startup`, `supporting startup`, or `excluded`.

- [ ] **Step 1: Dispatch three fresh-context batch reviewers concurrently**

  Give each reviewer one explicit range from `research/audit-batches.json`, the schema, QMD invocation, corpus path, classification definitions, copyright constraint, and required output path. Require direct full-file reads plus at least one BM25 and one semantic discovery query per batch. Do not pass intended classifications.

- [ ] **Step 2: Validate and integrate the first wave**

  Check JSON parsing, article-number set equality to assignment, `full_text_read: true`, specific exclusions, relevant evidence ranges, and retrieval-log entries before accepting a batch.

- [ ] **Step 3: Repeat fresh-context waves until all 12 batches are complete**

  Never assign an essay to two primary batch reviewers. Re-dispatch only rejected batch records, preserving the original reviewer field and adding a revision reviewer.

- [ ] **Step 4: Assemble the canonical audit deterministically**

  Concatenate validated batch records, numeric-sort by `article_no`, and reject duplicates rather than silently overwriting them.

- [ ] **Step 5: Run the audit gate**

  Run:

  ```bash
  python3 -m unittest discover -s tests -v
  python3 scripts/validate_repository.py \
    --phase audit \
    --repo . \
    --corpus /Users/leopaz/dev/opensource/graham-essays/corpus
  ```

  Expected: 223 classified, zero unaudited, zero duplicate, every exclusion has a specific reason, and every relevant essay has themes and line-addressable evidence.

- [ ] **Step 6: Run an independent overlap/gap review**

  Give a fresh-context reviewer the canonical audit, manifest, corpus, and QMD access. Ask it to identify suspicious exclusions, inconsistent classifications, duplicated/missing themes, and evidence ranges that do not support their paraphrases. Apply only findings verified against full essay text and log reviewer identity/disposition.

- [ ] **Step 7: Re-run the audit gate and publish checkpoint 2**

  Record classification counts, reviewer coverage, corrected findings, exact command output, remaining work, and blockers in `research/progress.md`.

  Run:

  ```bash
  git add research scripts tests
  git commit -m "research: complete 223-essay startup audit"
  git push origin codex/pg-isms-library
  ```

### Task 3: Synthesize Themes and Freeze the Minimal Taxonomy

**Files:**
- Create: `research/theme-synthesis.md`
- Create: `research/taxonomy.json`
- Modify: `research/essay-audit.jsonl`
- Modify: `research/progress.md`

**Interfaces:**
- Taxonomy records contain `skill_name`, `purpose`, `triggers`, `non_triggers`, `themes`, `essay_ids`, `stage_conditions`, `tensions`, and `candidate_eval_cases`.
- Every core/supporting audit record maps to one or more synthesized themes and final skill names.
- Theme coverage uses normalized exact labels: case-fold each label, replace punctuation/underscores with spaces, and collapse whitespace. Every normalized audited theme for a relevant essay must occur in the taxonomy themes of at least one of that essay's mapped `final_skills`; unrelated nonempty placeholders do not count.
- Every final skill must represent an actionable workflow, decision, or mental model distinct from its neighbors.

- [ ] **Step 1: Use brainstorming to cluster audited evidence without preset categories**

  Cluster all relevant essay themes and candidate workflows, merge synonyms, identify stage/product/urgency conditions, and preserve genuine tensions. Use BM25 and semantic queries to challenge each cluster, then retrieve full passages before changing evidence.

- [ ] **Step 2: Draft the minimal taxonomy and coverage map**

  For each proposed skill, state a distinct job, realistic trigger prompts, non-trigger counterexamples, covered themes/essays, stage conditions, and overlap boundary. Reject essay-summary-only categories and mechanically enforce that every relevant essay is covered.

- [ ] **Step 3: Dispatch independent fresh-context taxonomy critics**

  Assign separate critics to: missing principles/wrong exclusions; overlap/merge opportunities; contradictions/stage conditions; and trigger/non-trigger quality. Give only the audit, synthesis, taxonomy, and corpus/QMD access—not intended conclusions.

- [ ] **Step 4: Verify findings against full passages and revise**

  Record accepted and rejected findings with evidence. Update `final_skills` in the canonical audit and numeric-sort deterministically.

- [ ] **Step 5: Run the taxonomy gate and publish checkpoint 3**

  Run:

  ```bash
  python3 -m unittest discover -s tests -v
  python3 scripts/validate_repository.py \
    --phase taxonomy \
    --repo . \
    --corpus /Users/leopaz/dev/opensource/graham-essays/corpus
  git add research scripts tests
  git commit -m "research: synthesize startup skill taxonomy"
  git push origin codex/pg-isms-library
  ```

  Expected: zero uncovered relevant essays, no orphan taxonomy skill, and explicit trigger/non-trigger/stage-condition records for every skill.

### Task 4: Build and Verify Each Skill Sequentially

**Files:**
- Create one package at a time under `skills/<taxonomy skill_name>/`
- Create matching evidence under `evals/<taxonomy skill_name>/`
- Modify: `research/progress.md`

**Interfaces:**
- The order is the stable order in `research/taxonomy.json`; do not scaffold the next package until the current package is committed and pushed.
- Official tools live under `/Users/leopaz/.codex/skills/.system/skill-creator/scripts/`.
- Every package contains only `SKILL.md`, `agents/openai.yaml`, and directly useful one-level resources such as `references/provenance.md`.
- The repository validator supports the canonical generated metadata subset: a flat `SKILL.md` frontmatter mapping containing only `name` and `description`, plus an `agents/openai.yaml` `interface` mapping with quoted `display_name`, `short_description`, and `default_prompt` strings. Double-quoted strings use JSON-compatible escapes; single-quoted strings double internal apostrophes (`''`); SKILL frontmatter may also use a plain scalar when it has no YAML-reserved prefix or colon followed by whitespace or end-of-string. Agent interface strings must be quoted. Malformed quoting, indentation, duplicate keys, or unsupported structure fails the final gate.

**Evaluation artifact schema v1:**

- `evals/<skill>/cases.json` is an object with `schema_version: 1` and `cases`. Every case has a unique lowercase hyphenated `id`, a type from the closed vocabulary `trigger`, `non-trigger`, `application`, `condition`, or `edge`, a nonempty `prompt`, and nonempty string `criteria`. All five types must be present and any unsupported extra type fails validation.
- `evals/<skill>/{baseline,forward}/summary.json` contains `schema_version`, `skill_name`, `phase`, `reviewer_id`, and one `case_results` record per exact case ID. Each result contains numeric `score`, positive `max_score`, and a unique same-directory Markdown `raw_output` filename.
- Every raw output names its `Case ID` and `Reviewer ID`, matches its summary, and contains the captured response rather than an abbreviated placeholder. Baseline and forward use distinct reviewer IDs and identical scoring scales.
- Material improvement means the forward aggregate normalized score (`sum(score) / sum(max_score)`) is at least `0.10` greater than baseline. Raw prose claims without these summaries do not pass.

- [ ] **Step 1: Create realistic evaluation cases for the first unbuilt taxonomy skill**

  Include at least one trigger, one non-trigger, one application/decision case, one condition/tension case, and one edge case. For discipline-shaped skills include combined pressure; for mental models score recognition, application, and counterexample handling.

- [ ] **Step 2: Run and record RED with a fresh-context agent**

  Give the agent the realistic startup scenario and only ordinary repository/user context—no proposed skill, expected answer, or audit conclusion. Save raw output, score it against explicit criteria, and require a material gap before authoring.

- [ ] **Step 3: Initialize the package with official tooling**

  Run `init_skill.py` with the exact taxonomy `skill_name`, repository `skills` path, required resources, and generated `display_name`, `short_description`, and `default_prompt` interface values.

- [ ] **Step 4: Author the minimal GREEN package**

  Write imperative guidance addressing observed baseline gaps. Keep trigger conditions only in frontmatter description; preserve conditions/tensions; link directly to `references/provenance.md`; cite essay identifier, source URL, paraphrased principle, and exact source line ranges without long quotations.

- [ ] **Step 5: Generate metadata and structurally validate**

  Read `skill-creator/references/openai_yaml.md`, regenerate `agents/openai.yaml` from the completed skill with `generate_openai_yaml.py`, then run `quick_validate.py skills/<skill-name>` and repository tests.

- [ ] **Step 6: Run forward tests with different fresh-context agents**

  Prompt as a real user task using the skill path, not as a review. Save raw outputs and comparative scores. If the skill does not materially improve baseline behavior, revise only after capturing the new failure, then re-test with another fresh context.

- [ ] **Step 7: Gate, commit, and push the single skill**

  Run package validation, repository tests, and the applicable taxonomy/final validator subset. Record baseline failure, forward improvement, validator output, commit, push, remaining skills, and blockers.

  Run:

  ```bash
  git add skills/<skill-name> evals/<skill-name> research/progress.md
  git commit -m "feat: add <skill-name> startup workflow"
  git push origin codex/pg-isms-library
  ```

  Expected: one verified skill per commit; worktree clean and synchronized before selecting the next taxonomy entry.

- [ ] **Step 8: Repeat Steps 1–7 for every taxonomy entry**

  Never reuse a baseline agent as that skill's forward-test agent and never begin a second skill while the first is unverified or unpushed.

### Task 5: Independent Final Review and Remediation

**Files:**
- Create: `research/final-review.md`
- Modify affected `research/`, `evals/`, or one skill package at a time using the same failing-evaluation-first rule
- Modify: `research/progress.md`

**Interfaces:**
- Findings include category, severity, evidence, affected essays/skills, proposed remedy, disposition, and verification.
- `research/final-review.md` has a stable `Reviewer` ID, `Status: complete`, and `##` sections for `Missing principles`, `Overlap/gaps`, `Contradictions`, `Stage-dependent advice`, `Triggering quality`, and `Copyright hygiene`. Every required section records `Severity`, `Disposition`, specific `Evidence`, `Affected essays/skills`, `Proposed remedy`, and `Verification`; a reviewer/status stub does not pass.

- [ ] **Step 1: Dispatch fresh-context independent reviews**

  Cover missing principles/wrong exclusions, skill overlap, contradictions/stage-dependent advice, trigger/non-trigger behavior, provenance accuracy, copyright hygiene, and evaluation leakage.

- [ ] **Step 2: Verify every actionable finding**

  Re-read cited full passages and inspect raw evaluation artifacts. Reject unsupported findings explicitly.

- [ ] **Step 3: Remediate sequentially**

  For behavior changes, add a failing evaluation before editing the skill, revise, regenerate metadata if needed, structurally validate, and forward-test with fresh context. Commit and push each affected skill separately.

- [ ] **Step 4: Close the final review**

  Record reviewer identities, all findings and dispositions, exact verification outputs, remaining work, and blockers.

### Task 6: README Catalog and Repository-Wide Final Gate

**Files:**
- Modify: `README.md`
- Modify: `research/progress.md`
- Modify: `scripts/validate_repository.py` and tests only if the final gate exposes a previously untested invariant; add the failing regression test first.

**Interfaces:**
- README catalog names every taxonomy skill exactly once and describes triggers, non-triggers/boundaries, installation, and invocation.

- [ ] **Step 1: Write the README from verified taxonomy/package metadata**

  Do not claim unsupported capabilities or copy essay prose. Link to skills and research artifacts.

- [ ] **Step 2: Run the complete verification suite**

  Run:

  ```bash
  python3 -m unittest discover -s tests -v
  find skills -mindepth 1 -maxdepth 1 -type d -print0 | \
    sort -z | \
    xargs -0 -n1 /Users/leopaz/.codex/skills/.system/skill-creator/scripts/quick_validate.py
  python3 scripts/validate_repository.py \
    --phase final \
    --repo . \
    --corpus /Users/leopaz/dev/opensource/graham-essays/corpus
  ```

  Expected: zero unaudited essays, zero uncovered relevant essays, zero invalid packages, every skill has baseline/forward evidence, independent final review complete, and README catalog exact.

- [ ] **Step 3: Commit and push final documentation**

  Run:

  ```bash
  git add README.md research/progress.md scripts tests
  git commit -m "docs: complete verified pg-isms catalog"
  git push origin codex/pg-isms-library
  ```

- [ ] **Step 4: Prove clean synchronized delivery**

  Run:

  ```bash
  git fetch origin
  test -z "$(git status --porcelain)"
  test "$(git rev-parse HEAD)" = "$(git rev-parse origin/codex/pg-isms-library)"
  git status --short --branch
  ```

  Expected: every command exits 0 and status is exactly synchronized with no worktree changes.

- [ ] **Step 5: Mark the goal complete only after evidence is recorded**

  Append the final validator summary, skill count, audit classification counts, final review disposition counts, HEAD commit, remote equality proof, and `no blockers` to `research/progress.md`; re-run the final validator after that edit; commit and push the evidence update if it changes the file.

## Self-Review

- Spec coverage: Tasks 1–6 map to all six brief checkpoints plus clean/pushed delivery.
- Sequencing: taxonomy is not chosen until Task 2 validates all 223 classifications; skills are built one at a time only after taxonomy freeze.
- Evaluation integrity: baseline and forward agents are fresh and separate; prompts omit intended answers; raw outputs are retained.
- Coverage integrity: the validator compares canonical audit IDs to corpus IDs and relevant essay mappings to taxonomy/package IDs.
- Copyright hygiene: only metadata, paraphrases, URLs, and line ranges enter the public repository; long-source heuristics and independent review provide two checks.
- Pause conditions: pause only for licensing redistribution, substantive product choices beyond research judgment, credentials, or destructive actions outside this repository.
