# Independent no-skill baseline review: managing-runway-and-survival

Reviewer: `runway-baseline-auditor-001`

## Verdict

Integrity: **pass**. Independent audited score: **5 / 25** (20%).

`00000 00000 10000 01000 11010`

The audited vector exactly matches `strict-score.json`: **0 changed bits**. `red_valid` is **true**, and this baseline is **ready to freeze RED** because every scenario has at least one strict miss.

| Case | Audited vector | Score |
|---|---:|---:|
| scenario-01 | `00000` | 0 / 5 |
| scenario-02 | `00000` | 0 / 5 |
| scenario-03 | `10000` | 1 / 5 |
| scenario-04 | `01000` | 1 / 5 |
| scenario-05 | `11010` | 3 / 5 |

## Integrity audit

- The current `cases.json` and generation-plan bytes match all declared SHA-256 values.
- All five prompt projections exactly equal the corresponding `cases.json` prompt, and every prompt hash matches the frozen plan.
- All five response hashes, byte counts, and word counts match the attestation/freeze data; counts are 1,032, 974, 946, 994, and 1,050, all below 1,200.
- Each response birth epoch equals its mtime. The plan predates all responses; all responses predate the attestation/freeze files; scoring and scorecards postdate the freeze.
- Case IDs, generator task IDs, prompt paths, prompt hashes, and response hashes are one-to-one and unique.
- The scorer (`runway-baseline-scorer-001`) is distinct from all five generator tasks; this independent reviewer is distinct from both.
- No `skills/managing-runway-and-survival` package exists. The only same-named directory is the evaluation fixture.
- One-first-completion, no-resampling, and hidden-criteria status are attested controls; frozen bytes, unique generators, birth/mtime equality, exact prompt projection, and later scoring chronology corroborate them.

## Independent criterion audit

- Scenario 01: all five bits remain 0. The response omits the exact primary/default-dead and secondary-fundraising route; fails to record that payroll/taxes are current; lacks complete three-case unknown/default-alive structure; lacks complete hiring/action tuples; and lacks the four required branches plus adviser handoffs.
- Scenario 02: all five bits remain 0. It never explicitly records default alive or rejects rescue fundraising; omits cohort-comparability and complete unknown records; lacks a cash/runway floor and affected segment; omits core-product safeguards; and lacks four complete non-overlapping branches.
- Scenario 03: criterion 1 remains 1 because it rejects the two-month default-alive inference and unbanked pilot/Series A claims. Criteria 2–5 remain 0 for incomplete clearance/cash cases, ownership records, safeguards/options, and branch/financing routing.
- Scenario 04: criterion 2 remains 1 because all observed inputs and the 26.7-month static calculation are properly bounded. Criteria 1 and 3–5 remain 0 for missing exact route/default-alive record, invented financing conclusions, missing dated guardrails/switch, and no complete route-away handoff.
- Scenario 05: criteria 1, 2, and 4 remain 1 for the binding cash diagnosis, reconciled 13-week calendar, and pre-action adviser routing. Criteria 3 and 5 remain 0 for incomplete per-action tuples and missing consolidated non-overlapping branches.

Changed-bit evidence: **none; zero changes**.
