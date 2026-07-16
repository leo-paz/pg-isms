# Strict no-skill baseline review: managing-runway-and-survival

Scorer/reviewer: `runway-baseline-scorer-001`

## Result

The frozen baseline earns **5 / 25**, normalized **0.20** (20%). The aggregate vector, in scenario and criterion order, is:

`00000 00000 10000 01000 11010`

`red_valid` is **true** because every case has at least one miss.

| Case | Vector | Score | Normalized | Misses |
|---|---:|---:|---:|---:|
| scenario-01 | `00000` | 0 / 5 | 0.00 | 5 |
| scenario-02 | `00000` | 0 / 5 | 0.00 | 5 |
| scenario-03 | `10000` | 1 / 5 | 0.20 | 4 |
| scenario-04 | `01000` | 1 / 5 | 0.20 | 4 |
| scenario-05 | `11010` | 3 / 5 | 0.60 | 2 |

## Integrity

All response hashes and word counts match the generation attestation and freeze manifest. Each response remains below the 1,200-word cap.

| Case | Words | SHA-256 match | Within cap |
|---|---:|---:|---:|
| scenario-01 | 1,032 | yes | yes |
| scenario-02 | 974 | yes | yes |
| scenario-03 | 946 | yes | yes |
| scenario-04 | 994 | yes | yes |
| scenario-05 | 1,050 | yes | yes |

No `managing-runway-and-survival` skill package exists. The only directory with that name is the evaluation fixture at `evals/managing-runway-and-survival`.

## Strict scoring notes

- Scenario 01 has good survival prose and arithmetic but misses explicit workflow/default-dead routing, a complete observed-input record, three fully formed scenarios, complete action tuples, and the required branch set.
- Scenario 02 proposes a sensible reversible expansion test but omits the explicit default-alive/rescue-fundraising clause, complete unknown records, a cash floor and segment, core-product safeguards, and four complete branches.
- Scenario 03 earns only the diagnosis bit. It correctly rejects the two-month default-alive extrapolation and unbanked cash claims, but its cash calendar, milestone ownership, safeguards, and branch/routing structure remain incomplete.
- Scenario 04 earns only the observed-input/runway bit. It calculates 26.7 months without treating that static number as proof, but does not name the target financing workflow and invents round, valuation, dilution, governance, and terms rather than routing them.
- Scenario 05 earns the survival-state, 13-week-calendar, and qualified-adviser bits. It still lacks complete per-action tuples and four explicit non-overlapping dated branches.

Every binary decision and its evidence is recorded in `strict-score.json` and the five files under `baseline/scorecards/`.
