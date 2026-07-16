# Strict no-skill baseline review: raising-and-governing-capital

Scorer/reviewer: `capital-baseline-scorer-001`
Model: `Codex (GPT-5)`

## Result

The frozen baseline earns **1 / 25**, normalized **0.04** (4%). The aggregate vector, in scenario and criterion order, is:

`00000 00000 00000 00000 01000`

`red_valid` is **true**: frozen blind no-skill integrity passes, every case has at least one miss, and 24 of 25 criteria remain unsatisfied, leaving material room.

| Case | Vector | Score | Normalized | Misses |
|---|---:|---:|---:|---:|
| scenario-01 | `00000` | 0 / 5 | 0.00 | 5 |
| scenario-02 | `00000` | 0 / 5 | 0.00 | 5 |
| scenario-03 | `00000` | 0 / 5 | 0.00 | 5 |
| scenario-04 | `00000` | 0 / 5 | 0.00 | 5 |
| scenario-05 | `01000` | 1 / 5 | 0.20 | 4 |

## Integrity

The case, generation-plan, prompt, response, attestation, and freeze records form a matching chain. All five prompts are exact ID-and-prompt projections from `cases.json`. All response hashes, byte counts, word counts, and attested file times match; each response is below the 1,200-word cap. The target skill package is absent, the five task IDs and response hashes are unique, the scorer is distinct from the generators, and the responses were preserved byte-for-byte.

| Case | Words | SHA-256 match | Within cap |
|---|---:|---:|---:|
| scenario-01 | 1,140 | yes | yes |
| scenario-02 | 957 | yes | yes |
| scenario-03 | 1,038 | yes | yes |
| scenario-04 | 1,067 | yes | yes |
| scenario-05 | 1,119 | yes | yes |

## Strict scoring notes

- Scenario 01 provides a strong general financing process, but it does not name the workflow, fully classify inputs, complete consequential-unknown records, fix a complete thesis, or return the required four branches and closing gate.
- Scenario 02 gets the headline ownership arithmetic right, but strict criterion 2 still fails because capitalization definitions are not identified or tied explicitly to the headline's insufficiency. The response also lacks the complete owner/date/threshold structure and branch set.
- Scenario 03 correctly routes toward survival in substance, excludes uncommitted financing from cash, and pauses hiring, but it omits the exact workflow/default-dead diagnosis, survival envelope and action tuples, distraction cap, handoff predicate, and four survival branches.
- Scenario 04 correctly rejects software comparables and unsupported demand or timing claims, but it does not name the target workflow, complete the capital model and unknown controls, derive staged funding ranges, cover confidentiality/IP review, or return four complete branches.
- Scenario 05 earns criterion 2 because it immediately verifies, corrects, synchronizes, and audits the GMV disclosure before acceptance and branches on investor response without manufactured urgency. The workflow/status record, full comparison controls, weighted matrix, operating protection, and branch contract remain incomplete.

Every binary decision and its evidence is recorded in `strict-score.json` and the five files under `baseline/scorecards/`.
