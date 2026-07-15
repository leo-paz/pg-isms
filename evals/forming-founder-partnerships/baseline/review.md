# Frozen Baseline Review

Reviewer ID: founder-partnership-baseline-002

Scorer ID: founder-partnership-baseline-scorer-002

## Blindness declaration

This score used only `evals/forming-founder-partnerships/cases.json`, `evals/forming-founder-partnerships/baseline/manifest.json`, and the five frozen `evals/forming-founder-partnerships/baseline/scenario-01.md` through `scenario-05.md` responses. No skill, source or corpus, project brief, synthesis, design, prompt projection, report, forward, micro, heldout, other-skill evaluation, or git history/status was read. The rejected attempt at `.superpowers/sdd/founder-partnerships-baseline-attempt-001` was explicitly excluded and was not read.

## Integrity

Integrity passed. Every required SHA-256 value matched the frozen manifest:

- cases.json: `d3db98aaad816b55986056563960501744fa24c05497fc715c437413797030bc`
- scenario-01.md: `7509805f00f3c3f71580f5877638d9b1de5823497416cf82d8e6d96b08c4ecd1`
- scenario-02.md: `f578d0c272146f58bca03617fa4e58515687abc2cb20f74013c363569bbd89b7`
- scenario-03.md: `ecdaa28fce507c1934c00a96259636190d1c924bb4b2b85e6cd71c832fefcef4`
- scenario-04.md: `4810de0628542d5342ae1b4ac2be3c12ba169d8c644b18dc4c43fdff74765a0b`
- scenario-05.md: `12a0af42156b423da6d89128d3b40c9a52f9bba486fab733b32e7d6f747bfa60`

## Result

Score vector: `[1, 2, 1, 1, 1]`

Total: `6/25`

Normalized score: `0.24`

Passed criteria: `6`

Missed criteria: `19`

Cases with at least one miss: `5/5`

Baseline ready: `true` because integrity passed and the baseline contains at least one exact miss.

## Exact misses

### scenario-01 — 4 misses

- Criterion 2 — The response omits the complete explicit observed, claimed, and unknown classification.
- Criterion 3 — The trial omits complete dependencies, artifacts, and predeclared pass, change, extend, and stop thresholds.
- Criterion 4 — Material symmetry and the complete founder-status and ownership-intent record are not explicit.
- Criterion 5 — The filled July 14 decision record, complete accountability map, and full decision branches are absent.

### scenario-02 — 3 misses

- Criterion 2 — Several required observations and the full claimed and unknown taxonomy are absent.
- Criterion 4 — The response does not explicitly compare every materially different input or record runway and all required intents.
- Criterion 5 — The filled July 14 record, specified owners, August 14 review, and full switch conditions are absent.

### scenario-03 — 4 misses

- Criterion 2 — The full observed, claimed, and unknown classification, including motive and legal consequences, is not explicit.
- Criterion 3 — Complete evidence-linked conditions for expanding safeguards and confrontation constraints are not explicit.
- Criterion 4 — The founder, ownership, asset, and legal-routing record is incomplete, including fiduciary and tax routing.
- Criterion 5 — The filled July 14 record, complete ownership map, review gate, and counsel-linked conditions are absent.

### scenario-04 — 4 misses

- Criterion 1 — The response does not explicitly reserve founder-partnership work for a later genuinely unsettled founder issue.
- Criterion 2 — The pending work sample and all company-specific unknowns are not explicitly classified.
- Criterion 4 — Decision domains, evolution, and complete qualified-HR-and-counsel routing are absent.
- Criterion 5 — The filled dated handoff, explicit evidence owners, unknowns, all branches, and founder-reopening condition are absent.

### scenario-05 — 4 misses

- Criterion 2 — The complete observed, claimed, and unknown classification, especially Bo's required unknown behaviors, is absent.
- Criterion 3 — The Bo trial lacks a specific real-clinic outcome, dated review, and complete refusal-or-failure switch conditions.
- Criterion 4 — The complete input record, explicit ownership insufficiency, and qualified-current-counsel routing are absent.
- Criterion 5 — The filled July 14 record, complete accountabilities, August 31 review, and all decision branches are absent.

## Verdict

RED — This is a valid failing baseline: integrity and blindness passed, but 19 of 25 criteria were missed across all five cases.
