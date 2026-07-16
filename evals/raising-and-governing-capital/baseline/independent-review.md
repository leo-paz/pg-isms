# Independent no-skill RED audit: raising-and-governing-capital

Auditor: `capital-baseline-auditor-001`
Result: **3 / 25** (`0.12`)
Vector: `00000 01000 10000 00000 01000`
Integrity: **pass**
`red_valid`: **true**
`ready_to_freeze_red`: **true**

## Integrity

- `cases.json` matches the SHA-256 recorded by the generation plan, attestation, and freeze manifest. The generation-plan hash also matches both downstream records.
- All five prompt files are byte-exact ID-and-prompt projections from `cases.json`; their hashes match the frozen plan.
- All five response SHA-256 hashes, word counts, and byte counts match the attestation and freeze manifest. Counts are 1,140/7,747; 957/6,233; 1,038/6,961; 1,067/7,498; and 1,119/7,512. Every response is within 1,200 words.
- The five generator task IDs, prompt hashes, response hashes, and response bodies are unique. One first completion per case and no quality resampling are attested.
- Chronology is coherent: case content precedes prompt projection and plan freeze; the generation plan precedes all response births; every final response mtime precedes the attestation/freeze; and the prior scoring artifacts were created after the freeze.
- Scenario 04 is the sole birth/mtime mismatch (`04:43:48Z` versus `04:44:08Z`). The attestation transparently records length-only staging before one canonical move. Equality is therefore not imposed for this exception; the current 7,498 bytes and SHA-256 match both frozen records.
- No target skill package exists. The only same-named directory is this evaluation fixture. No source essay, taxonomy, intended source material, target package, or unrelated skill artifact was consulted.

## Independent strict score

The vector was frozen before any prior score, review, or scorecard was opened. A criterion earned 1 only when every clause was judged explicit.

| Case | Vector | Score |
|---|---:|---:|
| scenario-01 | `00000` | 0 / 5 |
| scenario-02 | `01000` | 1 / 5 |
| scenario-03 | `10000` | 1 / 5 |
| scenario-04 | `00000` | 0 / 5 |
| scenario-05 | `01000` | 1 / 5 |

Passing judgments:

- Scenario 02 criterion 2: the response supplies both ownership calculations and explicitly connects pool placement, participation, anti-dilution, and fully diluted capitalization inputs to the headline's insufficiency.
- Scenario 03 criterion 1: the response makes survival primary, establishes the default-dead condition from the supplied burn/runway/flat-revenue/churn facts, sequences the July 22 survival envelope before late-July capital materials, bounds fundraising as supporting work, and excludes nonbinding interest from cash.
- Scenario 05 criterion 2: the response immediately stops, verifies, corrects, synchronizes, and audits the GMV disclosure before acceptance, with investor-response branches and no manufactured urgency.

All other criteria fail at least one conjunctive clause. Full per-criterion evidence and omissions are in `independent-review.json`.

## Prior comparison

The prior score is **1 / 25**, vector `00000 00000 00000 00000 01000`. Agreement is 23/25 bits. Changed-bit count: **2**.

| Criterion | Independent | Prior | Difference |
|---|---:|---:|---|
| scenario-02 criterion 2 | 1 | 0 | The independent reading treats the requested/current pool and fully diluted cap table as the explicit capitalization inputs; the prior scorer requires separately named governing capitalization definitions and a tighter causal statement. |
| scenario-03 criterion 1 | 1 | 0 | The independent reading treats the dated July 22 survival plan before late-July capital work as an explicit survival-first sequence; the prior scorer requires the exact workflow/default-dead labels and reads capital permission as immediate. |

The frozen independent bits are retained. Both readings still establish a valid RED baseline: every case misses at least one criterion, the independent audit finds 22/25 misses, frozen-blind integrity passes, and the responses remain untouched.
