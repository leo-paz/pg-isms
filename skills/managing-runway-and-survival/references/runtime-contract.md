# Runtime contract

Return a decision record, not an essay. Hard maximum: **1,200 words**. Use compact tables, one item per row, and exact calendar dates. Never leave a cell blank or write `TBD`; write `unknown` with the evidence-control fields below. Do not let prose substitute for a required field.

## 1. Route and state header

State: `as of date | decision | horizon | company/product type and stage | primary skill | supporting skills in order | accountable decision owner | intermediate checks | final decision date`.

Apply these predicates before optimizing growth, hiring, or financing:

- **Acute cash:** cleared cash and the timing of protected obligations can bind within 13 weeks. Survival is primary.
- **Default-dead:** with financing set to zero, an evidence-bounded operating trajectory reaches the cash floor or time-to-zero before sustainable cash equilibrium or the product-type survival milestone. Survival is primary and needs a dated plan-B switch.
- **Default-alive:** sufficient reconciled history shows cash equilibrium before the cash floor under a stated downside, without an assumed round. History must span the relevant operating, sales, billing, and collection cycle; reflect the current cost structure; and contain no unmodeled step-change. A static runway calculation alone never establishes this state.
- **Indeterminate/sparse:** history is too short, pre-revenue, structurally changing, or mismatched to the product's evidence latency. Do not extrapolate default alive; use ranged calendar scenarios and funded milestones.

For capital-heavy, hardware, regulated, or long-latency products, select calendar milestones, current cost ranges, commitments, working capital, assurance, and qualified domain gates. Do not impose software ramen-profitability or weekly-result assumptions. For marketplaces, protect continuity and model liquidity without treating subsidized volume as durable demand.

If a healthy default-alive company asks for round design, output `route-away: raising-and-governing-capital` plus the runway handoff in section 6. Survival becomes primary again only when its predeclared switch-back predicate fires.

## 2. Evidence ledger

Fill one row per input:

`ID | observed / claimed / unknown | value and period/date | source or artifact | owner | status/uncertainty | decision use`.

- **Observed:** distinguish cleared cash, collected receipts, dated receivables, total outflow, net burn, revenue/MRR/ARR, gross margin, churn, payroll/tax/insurance/debt/contract obligations, commitments, and every planned cost step.
- **Claimed:** record unsigned financing, pipeline, nonbinding demand, forecasts, and stakeholder assertions without converting them to cash or fact. Pending financings count as zero in the survival base case; receivables enter only at scenario-weighted collection dates.
- **Unknown:** add `owner | artifact/source | due date | quantitative or directly observable threshold | branch or action changed`. Include collection timing, forecast sensitivity, cycle or saturation effects, costs, and current legal or regulatory facts when consequential.

## 3. Cash and milestone model

Show the arithmetic and label every assumption. Static runway is `cash / current average net burn`; if burn is non-positive, report that observation rather than “infinite runway.” Model planned hires, commitments, collections, churn, margin, and cost steps separately.

Select one mode:

1. **Acute cash:** daily cash through the next critical obligation or floor, then weekly through week 13. Reconcile opening and closing cleared cash, protected obligations, other commitments, scenario-weighted collections, recurring inflow and outflow, and variance on a named cadence.
2. **Operating history:** downside, base, and upside by month through the decision horizon, each with cash at review dates, time-to-floor or equilibrium, assumptions, and a dated default-alive test.
3. **Sparse/capital-heavy:** dated calendar through the next decision milestone, with cost and time ranges, technical, regulatory, customer, and financing evidence, latest safe commitment dates, cancellation or forfeiture effects, and cash remaining under each scenario.
4. **Healthy investment:** separate the proven engine from the proposed increment; state the affected segment, incremental spend cap, preserved cash or runway floor, marginal payback or return gate, evidence cadence, rival explanation, and falsifier.

## 4. Action register

One row per action:

`action | owner | start/deadline | expected cash effect and timing or hard cap | evidence artifact | protected obligation/safeguard | review date | continue/change/stop threshold`.

Sequence collections and protected obligations before hopeful pipeline. Prefer reversible reductions and focused revenue tests. Preserve customer continuity, core product and reliability, critical capability, study validity, compliance, data integrity, and dispatch or other essential operations as applicable. Do not cut all product work, expand commissions, place large orders, or hire merely because an investor or executive requests it.

Pause hires unless a precommitted evidence gate shows the company can absorb their full recurring cost without crossing the cash floor. Conversely, when sufficient history shows default alive and a proven engine has repeatable marginal returns, run a bounded investment test instead of blanket austerity. Compare delay, scope reduction, partner, deposit or revenue, cost, and bounded financing options when the venture type permits them.

Before deferring, changing, or missing payroll, taxes, insurance, debt, customer or vendor commitments, or regulated milestones—or making workforce, creditor, insolvency, shutdown, clinical, or other irreversible decisions—name the current qualified finance or accounting, tax, employment, legal, insurance, insolvency, regulatory, or clinical owner and the decision they must clear. Never invent priority, compliance, medical, legal, or investment conclusions.

## 5. Branch matrix

Choose the one branch family matching the state:

- ordinary default-dead: `continue`, `adapt`, `plan-B`, `shutdown-or-orderly-wind-down`;
- acute cash: `stabilize`, `adapt`, `plan-B`, `orderly-wind-down`;
- default-alive investment: `expand`, `hold`, `adapt`, `stop-expansion`;
- sparse/capital-heavy: `fund-and-proceed`, `reduce-or-stage`, `delay-milestone`, `orderly-stop`.

Fill every row:

`branch | non-overlapping observable predicate | cash/time consequence | next action | owner | decision date | primary route after branch | safeguard/handoff | preserved option`.

Make predicates exhaustive by ordered precedence or disjoint numeric intervals. Select today's branch. A plan-B or end branch must have a switch date early enough to preserve the stated option; do not wait for time-to-zero.

## 6. Route-away handoff

When survival is not primary, omit native actions and branches. Return:

`primary skill | decision owner | handoff date | observed runway/state facts | static-runway sensitivity | unknown controls | cash/runway floor | financing or execution budget/cap | maximum distraction envelope | protected obligations | plan-B switch date | preserved company-building option | exact survival switch-back predicate and owner`.

Route terms, dilution, control, investor selection, governance, and process design without answering them. For composed survival cases, establish this survival envelope first, then hand only a bounded financing branch to `raising-and-governing-capital`.

## 7. Completeness check

Before returning, verify: exact primary identifier; state supported by more than static runway; every input classified; every consequential unknown has five control fields; every scenario has a dated cash consequence; every action has cash or cap and safeguard fields; one complete state-specific branch family; qualified-owner gates before irreversible steps; no unsigned or nonbinding item counted as cash; no blanket austerity; and all owners, thresholds, handoffs, and dates explicit.
