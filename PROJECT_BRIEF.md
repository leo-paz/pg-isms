# Project brief: build the pg-isms skill library

## Objective

Create a thorough, evidence-backed collection of reusable Codex skills for building startups, derived from every startup-relevant essay in the local Paul Graham corpus.

## Source corpus

- Corpus: `/Users/leopaz/dev/opensource/graham-essays/corpus`
- QMD collection: `graham-essays`
- QMD invocation on this machine:
  `PATH=/Users/leopaz/.nvm/versions/node/v22.23.0/bin:$PATH qmd --index graham-essays ...`
- The corpus contains 223 Markdown essays with title, article number, source URL, and line-addressable text.

Use both BM25 full-text and semantic search, but do not reason from snippets alone. Retrieve and read the relevant essay text before using it as evidence.

## Required research artifacts

Create an auditable inventory covering all 223 essays. For each essay record:

- Article number, title, source URL, and corpus path
- Classification: core startup, supporting startup, or excluded
- A specific exclusion reason when excluded
- Startup themes and candidate reusable workflows
- Which final skill or skills incorporate it
- Relevant line ranges for incorporated essays
- Independent reviewer or review batch

The inventory must make it mechanically checkable that every essay was considered and that every startup-relevant essay is represented in the final synthesis.

## Taxonomy requirements

Derive the skill taxonomy after the essay audit. Do not make one skill per essay and do not force essays into an arbitrary preset list. Create a distinct skill only when it represents a reusable workflow, decision, or mental model that an agent should apply across startup situations.

Merge overlapping principles. Preserve genuine tensions and conditions—for example, advice that changes by stage, product type, or urgency—rather than flattening everything into slogans.

## Skill quality contract

For every final skill:

1. Define realistic trigger prompts and non-trigger counterexamples.
2. Run a fresh-context baseline without the skill and record the failure or gap.
3. Initialize the package with the official `skill-creator` tooling.
4. Write concise imperative guidance with progressive disclosure.
5. Put detailed essay provenance in `references/`, not a bloated `SKILL.md`.
6. Generate `agents/openai.yaml` from the completed skill.
7. Run structural validation.
8. Forward-test with fresh-context subagents on realistic startup scenarios.
9. Revise and re-test until the skill materially improves the baseline.
10. Commit the verified skill before moving to the next one.

Do not claim a skill is complete merely because its prose sounds persuasive.

## Team workflow

Use subagents extensively and keep their assignments independent:

- Divide the 223-essay inventory into explicit, non-overlapping batches.
- Have at least one independent synthesis pass look for missed themes and wrongly excluded essays.
- Use separate fresh-context agents for baseline and post-skill evaluations so conclusions are not leaked.
- Keep one primary agent responsible for the canonical inventory, taxonomy, validation, and integration.

## Repository shape

The exact taxonomy should emerge from research, but the completed repository should include:

- `skills/<skill-name>/SKILL.md`
- `skills/<skill-name>/agents/openai.yaml`
- `skills/<skill-name>/references/` when detailed provenance is needed
- `research/essay-audit.*`
- `research/theme-synthesis.md`
- `evals/` containing reusable baseline and forward-test cases and results
- A root validation or coverage script when useful
- A root README cataloging the final skills, triggers, and installation/use instructions

## Completion criteria

Stop only when all of the following are true:

- All 223 essays have an explicit audited classification.
- Every core or supporting startup essay maps to at least one synthesized theme or final skill, with source evidence.
- Every final skill has passed its baseline/forward-test loop and structural validator.
- A repository-wide check reports no unaudited essays, no uncovered relevant essays, and no invalid skill packages.
- The final taxonomy has received an independent fresh-context review for overlap, gaps, contradictions, and triggering quality.
- The README accurately catalogs the verified skills.
- The git worktree is clean and all verified work is committed and pushed to GitHub.

## Pause conditions

Pause for guidance if source licensing would require redistributing essay text, if the skill taxonomy requires a substantive product choice rather than a research judgment, or if credentials or destructive external actions beyond this repository are required.
