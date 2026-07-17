# Independent forward audit — attempt 2

Reviewer: `capital-forward-auditor-001`

## Result

The pre-comparison independent vector was physically recorded before the prior score was opened:

`11111 11011 11111 00010 11111` = **20/25**

Canonical payload SHA-256: `c1aa6b05ec909454dd79c88f0edab964f37e15dfba79fbbfb76e0533d20fd5b5`.

The prior scorer also totals 20/25, but its vector is `11111 11011 10111 00110 11111`. The vectors differ at **2 bits**: scenario-03 criterion 2 and scenario-04 criterion 3. `ready_to_freeze_green` is therefore **false pending adjudication**.

## Evidence boundary and integrity

Before freezing the vector, this review opened only `cases.json`, the current forward generation plan/package freeze/attestation/generation freeze, the five exact prompt projections, and the five response bodies. Package files were hashed only. The prior strict score, scorecards, score-vector freeze, baseline, attempt 1, source evidence/provenance, and other review feedback were not opened.

The artifact chain passes with disclosed provenance limits:

- The cases hash matches the plan, package manifest, attestation, and generation freeze.
- All five prompts exactly equal their case prompt text and match the planned hashes.
- All six package hashes match the package freeze.
- All response hashes, words, bytes, task IDs, birth epochs, and mtimes match the attestation/freeze.
- Response counts are 1009, 1045, 1051, 1077, and 1050 words; all are within 1200.
- Five task IDs and five response hashes are unique; every response has birth=mtime.
- One-first-write and hidden-input controls are attested and corroborated by prompt projection and birth=mtime, but generator read history cannot be proven from frozen files alone.
- After vector freeze, attempt-1 separation was verified: task IDs, package hashes, and response hashes are distinct, with zero task/response overlap. Shared prompt hashes are expected because the cases were unchanged.

Chronology is pre-generation-safe: cases and package files precede all response writes, and all responses precede the scoring freeze. The declared `05:26:10Z` freeze predates physical prompt/manifest creation by 6–39 seconds, and post-generation manifests were physically written 34 seconds after their declared freeze. This does not create a content/hash mismatch, but the declared instants are attestations rather than proof that every hash-bearing file physically existed at that exact second.

## Strict per-criterion judgments

| Case | C | Bit | Judgment |
|---|---:|---:|---|
| 01 | 1 | 1 | Primary capital route, provisional rather than static-runway proof, $1.2m floor/survival switch, and zero invented demand are explicit. |
| 01 | 2 | 1 | Every supplied operating/conversation/founder fact is classified; consequential unknowns have owner, artifact, date, threshold, and effect. |
| 01 | 3 | 1 | Pre-meeting thesis includes milestone, ranged uses, time/contingency, amount, dilution/control, alternative, and adviser verification. |
| 01 | 4 | 1 | Dated batches, tiers, warm paths, owners, truthful materials, room controls, references, dates, time cap, and protected work are explicit. |
| 01 | 5 | 1 | Four ordered capital branches include required evidence and options; closing is gated by signed counsel-reviewed documents and all six threshold families. |
| 02 | 1 | 1 | Terms are primary; unsigned status, July 27, no-deal, and counsel/finance/tax gates are explicit. |
| 02 | 2 | 1 | 11.11% versus 11.29% is shown and headline inference is defeated by pool, preference, anti-dilution, and FD-capitalization effects. |
| 02 | 3 | 0 | The downside/base/upside table is an operating burn model, not preference economics across exit scenarios. |
| 02 | 4 | 1 | Counter/walk-away envelope covers pool, preference, anti-dilution, control/vetoes, information/pro-rata/tranches, and sufficient funding. |
| 02 | 5 | 1 | Four ordered offer branches include owners, dates, documents, consequences, preserved options, and synchronized facts. |
| 03 | 1 | 1 | Survival is primary from burn/flat revenue/churn/time-to-zero; bridge claims remain zero cash and capital support is bounded. |
| 03 | 2 | 1 | **Frozen judgment:** the route-away record contains all listed fields and treats the August 25 conjunctive switch as its default-alive test. See disagreement below. |
| 03 | 3 | 1 | Hires pause; renewal/test precede broad fundraising; every immediate action has owner/date/cash/artifact/safeguard/threshold. |
| 03 | 4 | 1 | Pre-gate capital work, counterparties, and CEO time are capped; valuation/full launch wait for the dated handoff. |
| 03 | 5 | 1 | Continue/adapt/plan-B/wind-down are ordered with owners, dates, options, adviser gates, and conditional financing handoff. |
| 04 | 1 | 0 | The response selects survival, not the required raising-and-governing-capital primary route. |
| 04 | 2 | 0 | Working capital is not explicit and no regulatory/safety unknown has its own complete control. |
| 04 | 3 | 0 | The downside funding cell says `unknown; pause`, so a downside funding range is not derived. |
| 04 | 4 | 1 | Specialist/generalist/strategic comparison covers the required fit, capacity, diligence, horizon/support, conflict, restriction, governance, reference, and review controls. |
| 04 | 5 | 0 | Survival branches replace the required launch/stage/delay/stop capital branches. |
| 05 | 1 | 1 | Primary route, offer status/expiry/no-shop, non-survival state, anti-urgency rule, and adviser owners are explicit. |
| 05 | 2 | 1 | The 42% deck is frozen; 31%/scope verification, pre-sign correction, audit trail, consistent room, and response branches are explicit. |
| 05 | 3 | 1 | Amount/need, FD economics, terms, access/control, references/conduct, certainty, confidentiality, adviser effects, and unknown controls are compared. |
| 05 | 4 | 1 | Weighted matrix/counter envelope, protected work, extra references, and document/cap-table review are explicit. |
| 05 | 5 | 1 | Four ordered branches have owners/dates, corrected disclosure and signed-document evidence, consequences, and preserved profitable-company options. |

## Scorer comparison and adjudication note

The scorer differs at:

- **Scenario-03 C2:** independent `1`, scorer `0`. On reconciliation, the scorer's zero is stronger: the switch never explicitly requires recurring receipts to cover recurring outflow or otherwise states a dated equilibrium/default-alive test.
- **Scenario-04 C3:** independent `0`, scorer `1`. The independent zero remains stronger: `unknown; pause` is not a derived downside funding range.

Preserving both physical seals, the strict adjudication recommendation is therefore `11111 11011 10111 00010 11111` = **19/25**. This recommendation does not rewrite the sealed independent vector.

## Baseline delta and readiness

The baseline summary was opened only after scorer comparison. It is 1/25, with case scores 0, 0, 0, 0, 1.

Against the sealed independent result, case improvements are **+5, +4, +5, +1, +4**, for **+19 raw / +0.76 normalized**; every case improves. Against the post-comparison adjudication recommendation, the raw delta is +18 / +0.72 normalized.

Artifact integrity: **pass with disclosed attestation/chronology limits**. Material behavior improvement: **yes**. Ready to freeze green: **no**, because the scorer and independent frozen vectors differ at two bits and require adjudication.
