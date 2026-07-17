# Attempt-2 forward adjudication

Adjudicator: `capital-forward-adjudicator-001`  
Skill: `raising-and-governing-capital`  
Rule: award `1` only when every criterion clause is explicit; otherwise award `0`.

## Verdicts

### Scenario 03, criterion 2: `0`

The scorer's `0` is sustained; the independent auditor's `1` is overruled.

The response records the route-away inputs: cash, collected receipts, expense, net burn, obligations, churn, dated renewal and retention evidence, planned hires, claims, controlled unknowns, a cash floor, three cash scenarios, and early survival branches (response lines 9, 13-34, 44, and 58-61).

The missing conjunct is an explicit dated default-alive or operating-equilibrium test. Line 44 requires that a “no-financing downside forecast remains at or above $300,000 through 12/31,” but that is a cash-floor condition. It never requires recurring receipts to cover recurring outflow. Line 50 merely opens the capital workflow after the gate. A capital handoff predicate is not the required default-alive/equilibrium test, so the complete route-away handoff is absent.

### Scenario 04, criterion 3: `0`

The independent auditor's `0` is sustained; the scorer's `1` is overruled.

The August 15 review and supplier-quote coverage gate provisional amount and timing (response lines 26, 31, and 62). The response also provides provisional full/staged ranges and dated milestone scenarios (lines 31 and 33-37), identifies re-scope, nonexclusive partnering, cost reduction, and orderly preservation as alternatives (line 31), and labels the `$18m`/next-summer proposal unsupported and rejected (line 19).

The downside funding range is not derived. Its gap/raise cell says only “unknown; pause” (line 35), while base and upside have numeric ranges (lines 36-37). Because the required downside/base/upside funding ranges are conjunctive, the missing downside range forces `0`.

## Authoritative result

| Case | Vector | Score |
|---|---:|---:|
| scenario-01 | `11111` | 5/5 |
| scenario-02 | `11011` | 4/5 |
| scenario-03 | `10111` | 4/5 |
| scenario-04 | `00010` | 1/5 |
| scenario-05 | `11111` | 5/5 |

Authoritative vector: `1111111011101110001011111`  
SHA-256: `d66d29fe5f1cf07b0a91f9ee311df1c691ba87885c74c0f7c0a74539401cbe6f`  
Score: **19/25 (76%)**

The scorer and independent auditor each reported 20/25 but disagreed at two positions. This adjudication keeps the scorer's `0` at global position 12 and the auditor's `0` at global position 18, reducing each prior vector by one unsupported bit.

Against the frozen 1/25 baseline, the authoritative raw improvement is 18 criteria and the normalized improvement is 0.72. Case improvements are `+5, +4, +4, +1, +4`; every case improves by at least one criterion.

## Integrity and readiness

Integrity passes with the disclosed attestation and chronology limits already recorded in the allowed review artifacts. The cases hash is `fc56ebe94279acb5b1091df1fba26e4152f1798f0936e9c58e75d7196d89f372`; the scenario-03 and scenario-04 response hashes match the generation freeze manifest. Freeze manifests were used only for identity. Skill/package contents, source essays, evidence/provenance, baseline response bodies, forward-attempt-1, and other feedback were not opened.

Attempt 2 is **ready to freeze green** at the adjudicated 19/25 result. The two disputes are resolved, integrity passes with disclosed limits, material improvement remains, and every case still improves. The authoritative vector above has not itself been written into a replacement score-freeze artifact.
