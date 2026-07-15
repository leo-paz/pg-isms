# Baseline Review: competing-and-positioning

Reviewer ID: positioning-baseline-002

Scorer ID: positioning-baseline-scorer-002

## Blindness declaration

Scoring was performed from only `evals/competing-and-positioning/cases.json`, `evals/competing-and-positioning/baseline/manifest.json`, and the five frozen `evals/competing-and-positioning/baseline/scenario-0N.md` responses. No skill package, source evidence, intended answer, forward, micro, heldout, other skill evaluation, or prior review was accessed. The rejected attempt at `.superpowers/sdd/positioning-baseline-attempt-001` was not accessed.

## Integrity checks

The cases hash check passed:

- Expected SHA-256: `ccaf269056f8e1edb7aacb753bbfc66e0b6f5e3303aed59ba3298dea4f35ddc2`
- Actual SHA-256: `ccaf269056f8e1edb7aacb753bbfc66e0b6f5e3303aed59ba3298dea4f35ddc2`

The response hash check passed for all five frozen responses:

- `scenario-01`: expected and actual `39a6e382776652fd337895a6961946c5701a5da61be1b43c08e3a5b1bfadc7b6`
- `scenario-02`: expected and actual `36bc9140de3154a2436854e376a99ed2d1c1674af7b1d062c78f6d507159ce36`
- `scenario-03`: expected and actual `0a2ff6e1970a772a9e6f8150b50f4ebb6fa34a5d01afd3c6282f29ef31ee84ba`
- `scenario-04`: expected and actual `4e9cd4a9ba4b6961455076abf78164406ab393b892972640073abed3acb81b8b`
- `scenario-05`: expected and actual `72a8f12344a3625f7d0705d1cd6316673294d91a202f90a99a49f5d48400df54`

The raw responses and frozen inputs were not edited.

## Strict scoring method

All 25 criteria were scored independently and as strict binary 0 or 1. A point was awarded only when the complete criterion was explicit. Omitted named workflows, actors, thresholds, branches, evidence types, and distinction between observation and inference were not inferred from adjacent prose.

Score vector: `[3, 2, 1, 3, 1]`

Total: `10/25`

Normalized score: `0.4`

## Exact misses

1. `scenario-01`, criterion 4: The response rejects parity work and bounds the current scan, but does not explicitly defer a detailed comparison until user evidence identifies a consequential comparison or require the later scan to cover mechanism and tradeoff.
2. `scenario-01`, criterion 5: The response supplies dated activity and a final gate but does not assign evidence collection, prototype exposure, alternative mapping, and later differentiation to the required named workflows.
3. `scenario-02`, criterion 2: The response tests deployment and approval claims but does not explicitly examine incumbent incentives or installed-base advantage, and it does not distinguish observed evidence from inference.
4. `scenario-02`, criterion 4: The response protects and tests the wedge and gives escalation triggers, but it does not precommit explicit keep, adapt, reposition, and stop branches with thresholds.
5. `scenario-02`, criterion 5: The response does not route differentiation, interviews, product experiments, channel execution, and pricing decisions to the required named workflows.
6. `scenario-03`, criterion 1: The response covers partner, supplier, competitor, policy, native-product, revenue-share, access, and user-relationship concerns but does not explicitly examine the platform's incentives as a testable hypothesis.
7. `scenario-03`, criterion 2: The response does not create a complete dependency register spanning switching cost and observed-versus-inferred status in addition to acquisition, APIs, identity, billing, portability, and timing.
8. `scenario-03`, criterion 4: The response gives dated decisions and several metrics but does not precommit all double-down, diversify, redesign, migrate, and stop branches or a concentration threshold.
9. `scenario-03`, criterion 5: The response does not route platform strategy, channel experiments, architecture, product migration, and pricing consequences to the required named workflows.
10. `scenario-04`, criterion 2: The response routes work to trust and safety or community governance but does not name governing-platforms-and-communities or explicitly cover enforcement proportionality.
11. `scenario-04`, criterion 4: The response mentions communications review and process-controlled publication but does not route publication to communicating-clearly or explicitly bar communications from rewriting the governance outcome.
12. `scenario-05`, criterion 2: The response discusses transition risks and several durable assets but does not explicitly examine buyer switching cost, entrant and incumbent incentives, or the durability of distribution and learning loops.
13. `scenario-05`, criterion 3: The response proposes bounded cost, quality, and workflow tests plus renewal and loss analysis but omits an explicit willingness-to-switch experiment and affected-segment usage evidence.
14. `scenario-05`, criterion 4: The response gives dated integration and repositioning work plus a conditional training reconsideration, but it does not precommit the full integrate, reposition, rebuild, partner, and pivot branch set with adoption and defensibility thresholds.
15. `scenario-05`, criterion 5: The response does not route transition interpretation, customer evidence, implementation, and economic-model changes to the required named workflows.

## Issue counts

- Integrity issues: 0
- Blindness violations: 0
- Rejected-attempt accesses: 0
- Raw-input modifications: 0
- Missed criteria: 15
- Misses by scenario: `scenario-01` 2, `scenario-02` 3, `scenario-03` 4, `scenario-04` 2, `scenario-05` 4
- Passed criteria: 10
