# Independent forward audit — attempt 5

Auditor: `capital-forward5-auditor-001`  
Model: `GPT-5`  
Frozen vector: `11111 11111 11111 11111 11111`  
Score: **25/25**

The vector was frozen in `independent-vector-freeze.json` before any baseline access. Only `baseline/summary.json` was opened afterward. No skill-package, evidence/provenance/corpus, baseline-response, prior-attempt, scorer/vector/strict-score, or other-review artifact was opened.

## Identity and integrity

The actual SHA-256 values for `cases.json`, the generation plan, package manifest, generation attestation, generation-freeze manifest, and all five responses match the frozen identity chain. The attestation and filesystem checks also agree on response byte counts, word counts, birth times, modification times, five distinct task IDs, and five distinct response hashes. Every birth time equals its modification time, and every response is within the 1,200-word ceiling.

|Artifact|Verified SHA-256|
|---|---|
|`cases.json`|`fc56ebe94279acb5b1091df1fba26e4152f1798f0936e9c58e75d7196d89f372`|
|`generation-plan.json`|`a013b622e58966cdf4656769df8d04eb7587086bde72e8a3c26eb7cd0af33bd5`|
|`package-freeze-manifest.json`|`8977c7d1c69fc94cdf03997b0c63f414e5ad34b5da33d7dd984c76cfa9f6a16f`|
|`generation-attestation.json`|`b7eabd3cc4c8a101d4a25efdefe536f413e0f30611d15ea9cd8fabb61a1fe0c1`|
|`generation-freeze-manifest.json`|`3ba54913511061864b78dea4ae69b722841b878a75dd476138e3db40abee0b0a`|
|`scenario-01.md`|`d0515a3fb3470982dd05bd1b4896b6bd2b4f02b87655081e40e419afa1f2c9d8`|
|`scenario-02.md`|`889778d72347f0b5cb1a4af341b6916190ab7ba7213c773ca80551aa72e5b054`|
|`scenario-03.md`|`3c3b045bb27fbabf55aa3992294c30ece39e8243e581c4404d071db1c94f87d1`|
|`scenario-04.md`|`6a5b9bba250f856e396ec25bf20a3310a57f14a1d43db7c12cfdd7c3c5a5ba3f`|
|`scenario-05.md`|`68b45fd26ec8e2f026c368fee3cdafa0fdb6ba4406fe39609f84d9c0375910e5`|

Non-blocking target variance: scenarios 04 and 05 are 762 and 675 words, below the plan's 900-word target and 800–950 compaction guidance. Both satisfy the explicit 1,200-word hard ceiling, so this is not an identity or hard-integrity failure.

## Per-criterion judgments

Each bit is conjunctive: it is `1` only where every required clause is explicit in the response or its explicit canonical-ID reference.

### Scenario 01 — `11111`

|Bit|Evidence|Judgment|
|---|---|---|
|1|Sections 1–3 select the capital workflow, explain the non-acute operating state, define `FL1=$1.35m` and dated `X1.S`, and give F4 conversations zero commitment credit.|**1** — route, floor, switch, non-static evidence, and no invented demand are explicit.|
|2|F1–F4, C1–C2, U1, and A1 classify every supplied fact category and give consequential unknowns artifacts, owners, due dates, thresholds, and effects.|**1** — the full fact/unknown control requirement is explicit.|
|3|M1 supplies the milestone, ranged uses/time, contingency, amount/company contribution, dilution/control envelope, staged/no-raise alternative, adviser gate, and falsifier; S-D/S-B/S-U label assumptions.|**1** — every thesis clause is explicit before meetings.|
|4|`X1` and Section 4 provide dated batches, tiers, introductions/meetings, accountable ownership, references, synchronized materials, room/confidentiality controls, decision dates, time caps, protected work, and truth safeguards.|**1** — the complete process-control conjunction is met.|
|5|The ordered four-branch table includes observable predicates, owners/dates, routes, evidence, and preserved options; `G0` gates closing on runway/milestone, partner, economics/control, adviser, truth, definitive documents, approvals, and funding.|**1** — all branch and close-gate clauses are explicit.|

### Scenario 02 — `11111`

|Bit|Evidence|Judgment|
|---|---|---|
|1|The route makes financing terms primary, F1/F2 record both documents as unsigned with July 27 expiry, U3 preserves no deal, and Sections 2/4 require counsel plus finance/accounting/tax owners before term action.|**1** — every route/status/adviser clause is explicit.|
|2|D0 calculates 11.11% for A and 11.29% for B before fully diluted effects; the E row explains pool placement, participation, anti-dilution, and capitalization uncertainty.|**1** — arithmetic and headline-valuation limitations are explicit.|
|3|F1–F6/U1–U4, the three exit waterfalls, and A/E/C/P/T/Z separately cover amount, preference cases, anti-dilution, board/veto/executive/sale control, references, certainty, and missing terms with full unknown controls.|**1** — every required comparison dimension is explicit.|
|4|U3 requires a preapproved envelope; A/E/C counter and walk-away cells cover amount, pool, preference, anti-dilution, board/control, veto narrowing, information/pro-rata and related rights.|**1** — the counter/walk-away conjunction is complete and not price-only.|
|5|The four ordered branches carry owner/date, action, canonical evidence, and preserved option; `G0.Za/Zc` provides signed-document status, while the single synchronized fact sheet and `G0.T` apply truth consistently to both.|**1** — all branching, consequence, document, option, and disclosure clauses are explicit.|

### Scenario 03 — `11111`

|Bit|Evidence|Judgment|
|---|---|---|
|1|Section 1 calls the supplied trend default-dead, selects `managing-runway-and-survival`, bounds the capital workflow to support, and F4 assigns the partner meeting/soft circles zero cash.|**1** — the survival-primary conjunction is explicit.|
|2|F1–F7/U1–U2, `FLR`, `EQ`, `G0`, the three cases, and the July 24 Plan-B package cover the complete route-away record and an early switch.|**1** — all handoff/floor/scenario/default-alive clauses are explicit.|
|3|Section 4 freezes three hires, sequences renewals and retention before broad capital work, protects continuity, and gives each action owner/date, cash effect or cap, artifact, and safeguard/threshold.|**1** — every immediate survival-action clause is explicit.|
|4|`DIST` caps founder distraction; the reusable support lane limits work to truthful materials and qualification, rejects valuation/full launch, and `G0` supplies a September 30 capital handoff.|**1** — capital support is bounded and the requested round design is deferred.|
|5|The ordered continue/adapt/plan-B/shutdown table uses mutually exclusive `G0/FLR` predicates with owners/dates, preserved options, adviser gates, and a conditional financing handoff.|**1** — every survival branch clause is explicit.|

### Scenario 04 — `11111`

|Bit|Evidence|Judgment|
|---|---|---|
|1|Sections 1–2 select the capital-heavy pre-revenue pilot route; F4 states financed pilot precedes revenue, F9 rejects the software-seed amount/date, F5/F6 use qualified dated hard-tech gates, and F7 assigns letters/discussions zero cash and committed demand.|**1** — the software/ramen/weekly-default refusals and non-commitment treatment are explicit in the chosen gates.|
|2|F1–F10 and M1–M2 use cash, spend, pilot cost/time ranges, runway through close, contingency, working capital, and financing dates; F5/F6/F7/F8/F10 provide technical/safety, supplier, customer-status, and financing controls with owners, artifacts, dates, thresholds, and effects.|**1** — every model and unknown-control category is explicit.|
|3|F5/F6 make August 15 review/quotes prerequisites, M1/M2 block a fixed unverified amount/date, the three cases derive $7.6m–$16.7m, and the branches preserve staging/delay/no-raise while F9 excludes $18m/next-summer claims.|**1** — every readiness and range clause is explicit.|
|4|F8 and the tier table compare specialist/generalist/strategic parties across milestone/capacity/diligence/horizon/follow-on/governance/conflicts/confidentiality/IP/exclusivity/references; the adviser paragraph gates sensitive/restrictive actions.|**1** — the full investor-selection conjunction is met.|
|5|The ordered four branches provide technical/financing predicates, owners/dates, M1 funding/staging cash consequence, route/action, evidence, and preserved option; M3 plus qualified adviser gates require truthful communications and leave no term or instrument assumed.|**1** — all branch, truth, and term-verification clauses are explicit.|

### Scenario 05 — `11111`

|Bit|Evidence|Judgment|
|---|---|---|
|1|Section 1 and O0/O1 record capital-primary/non-survival status, fund-signed but company-unaccepted offers, July 25 expiries, no exclusivity/no-shop, and zero cash; U1/G0 block bonus/headline shortcuts pending qualified review.|**1** — every status, route, anti-urgency, and adviser clause is explicit.|
|2|T0 and Section 4 stop 42%, verify 31% with scope/cause, preserve the audit trail, correct X/Y and the synchronized room before signature, obtain acknowledgments, and route responses through `G0.T` and its walk-away/branch gates.|**1** — every correction and response clause is explicit.|
|3|U0/U1, the exit cases, and A/E/C/P/T/Z cover amount/milestone, fully diluted economics, preference/missing terms, board/observer, references/follow-on/exit pressure, certainty, confidentiality, and legal/tax effects with full unknown controls.|**1** — every comparison clause is explicit.|
|4|The matrix weights A15/E20/C20/P15/T20/Z10; D0 protects marketplace/customer work during the five-day window; R0 and U1 require additional references and full document/cap-table review.|**1** — the precommitment, operating protection, reference, and review conjunction is complete.|
|5|The ordered close-X/close-Y/counter-or-extend/decline-both table includes predicates, owners/dates, economic/governance consequences, and preserved options; `G0.Za/Zc` requires correction, acceptance, definitives, approvals, conditions, and funded cash.|**1** — all closing-branch clauses are explicit.|

## Baseline comparison

Only the frozen baseline summary was used. Its adjudicated vector is `00000 00000 00000 00000 01000`, totaling **1/25**. Attempt 5 independently scores **25/25**, an improvement of **+24 points** and **+0.96 normalized**.

|Case|Baseline adjudicated|Forward independent|Improvement|
|---|---:|---:|---:|
|Scenario 01|0/5|5/5|+5|
|Scenario 02|0/5|5/5|+5|
|Scenario 03|0/5|5/5|+5|
|Scenario 04|0/5|5/5|+5|
|Scenario 05|1/5|5/5|+4|

## Readiness

**Ready.** The immutable independent vector is 25/25; every criterion passes conjunctive binary review; response identity, freeze-chain, timestamp, uniqueness, and hard word-limit checks pass; and the result materially improves the adjudicated baseline.
