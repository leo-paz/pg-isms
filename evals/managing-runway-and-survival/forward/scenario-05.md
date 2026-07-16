# Survival decision record

**State:** 2026-07-20 | acute-cash stabilization; financing assumed $0 | through 2026-09-30 | 19-person logistics marketplace, operating | **primary:** managing-runway-and-survival | **supporting:** building-and-evolving-organizations; designing-business-models; acquiring-and-growing-users; raising-and-governing-capital only within the cash envelope | CEO | daily through 2026-08-19, then Mondays and 2026-09-30 | final decision 2026-09-30.

Today's branch is **stabilize**. Dispatch and time-sensitive loads are protected.

## Evidence ledger

| ID | class | value/date | source/artifact | owner | status/uncertainty | decision use |
|---|---|---|---|---|---|---|
| E1 | observed | $620,000 cleared cash, 2026-07-20 | bank reconciliation | controller | opening balance stated; reverify daily | cash calendar |
| E2 | observed | $290,000 payroll, tax, insurance, hosting due by 2026-08-19 | AP/payroll/tax schedules | controller | exact daily dates unknown | protected-obligation reserve |
| E3 | observed | $115,000 other commitments due by 2026-08-19 | AP/contract register | controller | cancellation terms unknown | commitment reserve |
| E4 | observed | $78,000 monthly collected gross profit, current | receipts and margin ledger | controller | timing/churn history unknown | inflow sensitivity |
| E5 | observed | $235,000 other recurring monthly cash expense | cash ledger | controller | overlap with E2/E3 unknown | burn sensitivity |
| E6 | observed | $180,000 accepted invoices; solvent customers; due $90,000 assumed for modeling on 2026-08-05 and $90,000 on 2026-08-18 | invoices/acceptance | controller | split is an assumption; no cash cleared | scenario collections |
| E7 | claimed | $1.5m unsigned pipeline | CRM | CEO | no contracts; $0 base-case cash | excluded until signed and collected |
| E8 | observed | 46 active shippers; dispatch disruption could strand loads | dispatch system | operations lead | load-level exposure varies | continuity safeguard |
| E9 | claimed | wait, keep hiring, broad rebrand | CEO request | CEO | costs and returns unproved | paused pending gates |
| E10 | observed | 19 employees; qualified advice available | payroll/adviser engagement records | CEO | actual adviser names/scope need confirmation | irreversible-action gates |

**Unknown controls:** By 2026-07-21, controller supplies a dated 13-week bank/AP/payroll file, removes E2/E3/E5 overlap, and shows daily minima; threshold: no unexplained variance and ≥$150,000 closing cash; effect: spend/branch. By 2026-07-22, controller obtains written payer amount/date/dispute confirmations; threshold: cleared receipt by due date; effect: collection scenario. By 2026-07-22, CEO supplies hiring/rebrand contracts, cancellation and recurring costs; threshold: $0 commitment unless September downside exceeds $150,000; effect: freeze. By 2026-07-22, operations lead supplies critical-load/vendor/staff map and continuity budget; threshold: zero stranded loads; effect: protected spend. By 2026-07-21, CEO records the actual current qualified tax, employment, insurance, customer-contract and insolvency advisers and scope; threshold: written clearance; effect: any deferral, workforce, creditor or wind-down action.

## Acute-cash model

Provisional cash floor: **$150,000**, for continuity and an orderly option; controller validates it by 2026-07-22. Static sensitivity, excluding special commitments and assuming E5 is incremental: monthly net burn is $235,000 - $78,000 = **$157,000**, or 3.95 months. It is not a default-alive finding and understates the dated $405,000 burden.

| case and date | arithmetic/assumptions | cash consequence |
|---|---|---|
| downside, 2026-08-19 | $620k - $290k - $115k + $78k - $235k; no receivables | **$58k**, floor breached |
| base, 2026-08-19 | downside + $180k cleared on stated due dates | **$238k** |
| upside, 2026-08-19 | same as base; pipeline remains $0 until cash | **$238k** |
| unchanged base, 2026-09-30 | $238k + 1.4×($78k-$235k-$290k), assuming E2 recurs monthly and E3 does not | approximately **-$388k**; insolvency before horizon |

Controller reports opening cash, dated payments, cleared receipts, variance and closing cash daily at 17:00 through 2026-08-19, then weekly. Equal invoice split, even timing, E5 independence and recurring E2 are assumptions; reconciliation overrides them.

## Action register

| action | owner | deadline | cash effect/cap | artifact | safeguard | review | threshold |
|---|---|---|---|---|---|---|---|
| Ring-fence and schedule protected payments | controller | 2026-07-20 | reserve $290k; no unapproved change | daily cash file | payroll/tax/insurance/hosting; adviser clearance | daily | change only with qualified written clearance |
| Collect accepted invoices | controller | start 2026-07-20 | up to $180k on 08-05/08-18 | written confirmations/bank receipt | no service threat or false representation | daily | escalate contract counsel one business day after miss |
| Freeze hiring and rebrand | CEO | 2026-07-20 | $0 new commitment | PO/offer freeze log | retain essential dispatch capability | 2026-08-19 | resume only if Sep downside >$150k after full cost |
| Renegotiate/cancel E3 and noncritical E5 | CEO/controller | proposals by 2026-07-23 | target at least $250k cash retained through 09-30; no fee without approval | vendor schedule/amendments | no dispatch, data, insurance, tax or customer breach | twice weekly | execute only after contract/adviser review |
| Dispatch continuity plan | operations lead | 2026-07-22 | hard cap set by validated minimum budget | critical-load roster/runbook | zero stranded loads; named coverage | daily | protect minimum staffing/vendors first |
| Cash sales test to 46 shippers | CEO/operations lead | 2026-07-24 | $0 spend; contractually sound deposits/prepay | signed orders/cleared cash | capacity and existing terms | weekly | continue only for positive collected gross profit |
| Prepare workforce/creditor/wind-down options | CEO plus named advisers | 2026-07-24 | no execution before written clearance; preserve $150k floor | advice memos and contingency budget | employment, tax, insurance, contract, insolvency compliance | 2026-08-05 | activate per branches |

## Ordered branch matrix

Predicates apply top-to-bottom, using reconciled cash and signed reductions; pipeline never qualifies.

| branch | observable predicate | consequence | next action / owner | decision date | route | safeguard / preserved option |
|---|---|---|---|---|---|---|
| stabilize | projected minimum through 09-30 is ≥$150k | continuity funded | maintain freeze, collect, execute reviewed savings / CEO | daily through 2026-09-30 | survival | dispatch protected; later bounded growth |
| adapt | not stabilize, but contracted collections plus executable reductions keep minimum ≥$150k | survival requires changes | sign reviewed reductions and focused prepay plan / CEO | 2026-08-05 | survival then business model | no stranded loads; preserve marketplace core |
| plan-B | not above, and orderly continuity/wind-down can still be funded at ≥$150k | current model unfunded | activate adviser-cleared workforce/creditor contingency; seek only bounded financing / CEO | 2026-08-07, or immediately on missed 08-05 receipt | survival; bounded capital handoff | preserve service transfer or smaller operation |
| orderly-wind-down | projected cash falls below $150k despite immediately executable plan-B, or an adviser says delay destroys an orderly option | stop before disorderly default | cease new risky loads and execute adviser-approved plan / CEO and operations lead | no later than 2026-08-19; recheck weekly through 2026-09-30 | qualified wind-down owners | protect customers, staff, records and lawful creditor process |

Case ID: scenario-05
Reviewer ID: runway-forward-001
