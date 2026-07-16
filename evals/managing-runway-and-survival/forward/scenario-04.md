# Route and state

**State:** `2026-07-20 | route-away: raising-and-governing-capital | through 2027-12-31 | nine-person analytics SaaS, $2.4M ARR, repeatable enterprise channel | raising-and-governing-capital | managing-runway-and-survival | CEO, with finance lead/controller accountable for cash evidence | evidence close 2026-07-22; monthly checks beginning 2026-07-31 | route confirmed 2026-07-23`

**Decision today:** This is a default-alive investment case, not acute cash or ordinary survival. The primary workflow is `raising-and-governing-capital`, which decides round size, investor selection, dilution, governance, terms, and process timing; none is decided here. Financing remains zero. Only a two-business-day reconciliation gate precedes the capital process.

# Evidence ledger

| ID | classification | value and period/date | source/artifact | owner | status/uncertainty | decision use |
|---|---|---|---|---|---|---|
| E1 | observed | $3.2M cash at 2026-07-20 | bank-to-ledger reconciliation | finance lead | clearing confirmation pending | opening cash |
| E2 | observed | $2.4M ARR; 82% gross margin; 1.0% monthly revenue churn | billing, contracts, cohorts | revenue operations | definitions pending | trajectory durability |
| E3 | observed | $320,000 current monthly collected revenue; nine monthly rises | bank receipts and aging | finance lead | timing pattern pending | inflow and lag |
| E4 | observed | $440,000 current monthly cash expense; no planned hiring step | general ledger, payroll register, payables schedule | finance lead | whether every cash cost and commitment is included must be checked | current net burn and cost structure |
| E5 | observed | average net new ARR of $170,000 per month for nine months | CRM-to-contract-to-billing reconciliation | revenue operations | reported net of churn; conversion timing to cash remains uncertain | operating-history test |
| E6 | observed | no debt covenant, late obligation, or customer concentration above 9% | obligation and concentration schedules | finance lead and counsel | confirmation pending | acute-cash screen |
| E7 | claimed | founders intend a Series A to accelerate the enterprise channel; no signed offer | board/founder plan and financing data room | CEO | purpose claimed; financing certainty is zero | route only, never survival cash |

# Unknown controls required before handoff

| unknown | owner | artifact/source | due date | observable threshold | branch or action changed |
|---|---|---|---|---|---|
| Cash and expense reconciliation | finance lead | bank reconciliation, trailing-nine-month cash P&L, payroll, payables, tax and insurance schedules | 2026-07-22 | cleared cash at least $3.15M; normalized monthly cash expense no more than $460,000; no protected obligation due within 13 weeks that the forecast cannot pay | failure makes survival primary for a 13-week cash plan |
| ARR-to-collection lag and trend | revenue operations | monthly ARR bridge, invoices, receipts, aging, write-offs, and sales-cycle report | 2026-07-22 | nine complete months reconcile; at least six months cover the current enterprise sales/billing/collection cycle; no two consecutive monthly collection declines | failure makes state indeterminate and delays capital-process launch |
| Downside durability | CEO and finance lead | monthly scenario model using customer-level churn, renewal dates, pipeline excluded until contracted, and fixed commitments | 2026-07-22 | downside cash reaches equilibrium before the $1.50M floor, with financing zero | failure switches to `managing-runway-and-survival` |
| Unmodeled step-changes | CEO | approved hiring, vendor, commission, infrastructure, legal, and security commitments | 2026-07-22 | no new recurring step above $25,000 per month and no one-time commitment above the $75,000 financing-process cap | excess spend is paused for a separate runway gate |

# Cash model and default-alive test

Current net burn is `$440,000 - $320,000 = $120,000 per month`. Static runway to zero is `$3.2M / $120,000 = 26.7 months`; static time to the $1.50M cash floor is `($3.2M - $1.5M) / $120,000 = 14.2 months`, approximately 2027-09-30. These are sensitivities, not the default-alive proof.

The operating-history test uses financing of zero and treats ARR as non-cash until collected. For sensitivity, $170,000 monthly net new ARR represents $14,167 of potential additional monthly collections. Expense stays $440,000 with no hiring step.

| scenario | explicit assumption | dated cash consequence | equilibrium test |
|---|---|---|---|
| downside | only 50% of the reported ARR pace reaches collections, adding $7,083 of monthly collections each month after normal lag | cumulative burn to equilibrium is about $1.08M; minimum cash about $2.12M by 2027-12-31 | equilibrium in about 17 months, before the $1.50M floor |
| base | reported pace converts after reconciliation, adding $14,167 monthly | cumulative burn to equilibrium about $570,000; minimum cash about $2.63M by 2027-04-30 | equilibrium in about nine months |
| upside | 150% of reported pace converts, adding $21,250 monthly | cumulative burn to equilibrium about $401,000; minimum cash about $2.80M by 2027-01-31 | equilibrium in about six months |

The downside establishes default-alive only if the reconciliation confirms its lag and cost assumptions. Gross margin is a quality check, not added again to cash expense unless the ledger shows cost of revenue was excluded.

# Bounded runway handoff

| field | handoff |
|---|---|
| primary skill | `raising-and-governing-capital` |
| decision owner / handoff date | CEO / 2026-07-23 after finance lead signs the controls above |
| observed runway/state facts | $3.2M cash, $120,000 current net burn, nine months of rising collections and $170,000 average monthly net new ARR, 82% gross margin, 1.0% monthly revenue churn, no planned hiring step, and no stated acute obligation or concentration |
| static-runway sensitivity | 26.7 months to zero and 14.2 months to the $1.50M floor if revenue and expense stay flat |
| cash/runway floor | $1.50M cleared cash; do not commit spend that makes the reconciled downside cross it before equilibrium |
| financing/execution cap | no round proceeds assumed; maximum $75,000 one-time financing-process cash cost and no new recurring hire or vendor step before signed, cleared funds or a separate absorbability gate |
| maximum distraction envelope | at most 0.75 combined founder FTE for ten weeks; customer delivery, renewals, collections, product reliability, and enterprise-channel measurement retain named owners |
| protected obligations | payroll, taxes, insurance, existing customer and vendor commitments, security/data integrity, product reliability, and collection operations |
| plan-B switch date | 2026-09-30, reviewed monthly from 2026-07-31; switch earlier on the predicate below |
| preserved company-building option | continue compounding the repeatable enterprise channel without accepting financing from cash desperation; preserve the ability to raise later, reduce process intensity, or self-fund |
| exact survival switch-back predicate and owner | Finance lead immediately returns primary control to `managing-runway-and-survival` if any protected obligation may be missed within 13 weeks, or the reconciled downside forecasts cash below $1.50M before equilibrium. CEO does so if collected revenue declines for two consecutive completed months while expense exceeds $440,000, or an unmodeled recurring cost step above $25,000 is approved. |

**Completeness check:** Financing is zero; ARR is not cash; downside equilibrium precedes the floor; route-away omits survival actions and branches.

Case ID: scenario-04
Reviewer ID: runway-forward-001
