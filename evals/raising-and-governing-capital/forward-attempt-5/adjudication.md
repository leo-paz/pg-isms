# Attempt 5 adjudication

Adjudicator: `capital-forward5-adjudicator-001`  
Adjudicated: `2026-07-16T07:19:01Z`  
Rule: binary and conjunctive; a criterion receives 1 only when every clause is explicit in the frozen response, with no inference or generic-prose credit.

The immutable adjudication vector was frozen before `baseline/summary.json` was opened. Its SHA-256 is `4e917b235ef5827e6f6613e23c444b62ca8fc8b3c33e659c732f8480ac85892f`; it was not revised.

## Disputed-bit decisions

| Criterion | Strict scorer | Independent auditor | Adjudicated | Decision |
|---|---:|---:|---:|---|
| `scenario-03.criterion-2` | 0 | 1 | **0** | `scenario-03.md:11-17` expressly labels the supplied cash, receipts, expense, churn, hires, renewal date, and retention date as `claimed`; `scenario-03.md:18` labels protected-obligation amounts and timing `unknown`. Lines 25-34 do provide the floor, default-alive test, switch, scenarios, and net-burn calculations, but the required observed-operating-facts conjunct is not explicit. |
| `scenario-04.criterion-1` | 0 | 1 | **0** | `scenario-04.md:5,19,26,50` explicitly reject the software-seed comparison and unsupported amount/date, and line 17 gives the letters and discussions zero cash and committed-demand credit. No passage explicitly refuses the ramen-profitability default or the weekly-evidence default. Dated gates do not substitute for those named refusals under the no-inference rule. |

The adjudication changes none of the 23 agreed bits.

## Authoritative result

| Case | Vector | Score |
|---|---:|---:|
| scenario-01 | `11111` | 5/5 |
| scenario-02 | `11111` | 5/5 |
| scenario-03 | `10111` | 4/5 |
| scenario-04 | `01111` | 4/5 |
| scenario-05 | `11111` | 5/5 |

Authoritative 25-bit vector: `1111111111101110111111111`  
Authoritative total: **23/25 (0.92)**

## Baseline comparison

Only `baseline/summary.json` was opened, after the adjudication vector freeze. Its adjudicated baseline is `00000 00000 00000 00000 01000`, or **1/25 (0.04)**.

Attempt 5 improves by **22 points**, from 1/25 to 23/25, an **88-percentage-point** normalized gain and a **23×** score multiple. Case gains are +5, +5, +4, +4, and +4 respectively.

## Integrity and readiness

Integrity passes with non-blocking generation-band deviations. Artifact and response identities match the frozen hashes, every response is within the 1,200-word hard limit, and the adjudicator edited no responses, package files, or reviewer freezes. Scenario 02 is 27 words above the 800-950 instruction band; scenarios 04 and 05 are 38 and 125 words below it.

The result materially improves the baseline, but it is **not ready for final all-criteria acceptance**. The blocking criteria remain `scenario-03.criterion-2` and `scenario-04.criterion-1`.
