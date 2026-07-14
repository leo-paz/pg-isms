Case ID: scenario-03
Reviewer ID: business-model-forward-004

Primary owner: `designing-business-models` — stable paid renewals exist, so the task is to tune value metric, package, price, and sales effort against account economics.

Handoffs:

1. `learning-from-users` verifies value events, alternatives, budgets, and reasons for acceptance, discounting, or churn in the renewal test.
2. `engineering-for-leverage` instruments compute, storage, support, audit activity, and entitlements by account.
3. `shipping-and-iterating-products` implements package limits, metering, invoices, and grandfathering.
4. `acquiring-and-growing-users` owns the assisted sales cohorts only after the renewal package passes; self-serve acquisition remains closed.

## Business-Model Record

| Field | Current record |
|---|---|
| Product and state | Enterprise/integration compliance software, 24 annual customers at $18,000 each, with two renewal cycles. Buyer, annual pricing, and deployment exist; there is no stated survival constraint. |
| Binding constraint | One price hides materially different value and cost. Four accounts create 68% of compute/support cost; small accounts consume procurement effort. A seat is not shown to cause value or cost, and “unlimited” would remove the cost guard precisely where concentration is highest. |
| Latency / reversibility / error cost | Evidence arrives at annual renewal and deployment, not at a pricing-page click. Quotes are reversible before signature; broad contract changes are sticky. Compliance failure, misleading limits, and migration loss have high customer cost. |
| Facts to verify before quoting | Join account-level usage and cost rather than assuming the four heavy accounts are among the twelve weekly users. Measure current compute, storage, implementation, support, sales/procurement hours, security/assurance work, renewal timing, discount history, deployment status, switching cost, concentration, and expansion. Verify current competitor terms only as context, not WTP evidence. |

| Behavioral segment | Actors, value, alternative, and evidence | Economic record and unknowns |
|---|---|---|
| Twelve weekly audit users | Distributor is beneficiary/user/buyer/payer through an annual direct contract. The observed event is completing an audit while avoiding $120,000–$400,000 of remediation. Alternatives, budget owner, audited-facility count, and expansion trigger are unknown. | $18,000 annually; weekly deployed use; two-cycle renewal exists at portfolio level. Account-specific renewal, margin, implementation, support, switching, and expansion must be separated. Avoided remediation is value evidence, not proof of a particular price. |
| Eight monthly users | Same actor chain; likely periodic compliance work, but the exact event and alternative are unverified. | $18,000 annually; monthly use. Payment exists; paid renewal, retention, support, and margin by account must be joined. Low frequency may be efficient value or weak adoption. |
| Four archive users | Same actor chain; observed event is document retention/retrieval rather than active audit work. Alternative may be a repository, but that and the compliance value are unverified. | $18,000 annually; little active use. Archive value, procurement burden, switching, paid renewal, and cost must be measured. Low use is not automatically low willingness to pay. |
| Four highest-cost accounts | Their behavioral segment is not given and must not be inferred. They generate 68% of compute/support cost. | Calculate account contribution after compute, support, implementation, security, and sales. Determine whether load represents valuable audit volume, bad architecture, unusual deployment, or service failure before charging for it. |

The leading value metric is annual audit workload—preferably audited facilities or completed audit events—because it is closer to the value event than seats. Compute/support is a package guard or overage basis, not automatically the headline metric. The metric is adopted only if account interviews and historical data show it is understandable, forecastable, and correlated with value. Procurement, security, switching, deployment, implementation, support, sales effort, and evidence latency are included in every account margin.

## Renewal package to test

| Package | Bounded offer | Sales and service boundary |
|---|---|---|
| Records | $15,000–$18,000 annually, one deployment, retention/retrieval, standard support, and explicit storage/activity limits | Assisted annual contract with a standard security packet; no audit workflow promise and no self-serve claim until five consecutive customers deploy without bespoke procurement work |
| Audit Operations | $24,000–$30,000 annually with an agreed annual audited-facility/event allowance, standard implementation and support, and disclosed overages | Account-assisted annual sale and renewal; overage unit fixed in the order form, with 80% and 100% usage notices |
| Audit Intensive | $36,000–$54,000 annually with a larger agreed activity allowance, named implementation/support scope, and metered compute/support overages | Direct enterprise sale, implementation plan, quarterly usage review, and expansion order rather than an unlimited promise |

Reject the proposed $29-per-seat tier for this cycle: no seat-value relationship, self-serve deployment, or low-touch procurement has been demonstrated. Reject unlimited enterprise because four accounts already dominate costs. Competitor menus are not payment evidence. Preserve the current $18,000 contract as a one-cycle, capped grandfather option only under the branch below.

## Bounded renewal test

- **Sample and timing:** Test the next eight renewals, stratified where the calendar permits across at least two high-cost, two weekly non-high-cost, two monthly, and two archive accounts. If the groups overlap or renewal order prevents that mix, report the actual mix and do not pool it. Review after eight decisions or 2026-12-15, whichever comes first.
- **Owner, cost, and exposure:** VP Sales owns quotes; Finance owns account margin; Product owns packaging. Maximum discretionary discount is 15%, with no more than one annual renewal at a grandfathered price per account. No feature removal occurs during an active term. Implementation and migration work is capped at 40 staff hours per account unless separately paid.
- **Metrics and gates:** Signed annual renewal and collected invoice, deployment, net paid ACV, discount, procurement/sales hours, implementation time, account and cohort gross margin, support/compute, usage against allowance, expansion, churn reason, and compliance incidents. Require projected cohort gross margin at least 70%, each account at least 55%, and zero loss of records, undisclosed limit, or missed compliance workflow caused by packaging.
- **Confounders:** Audit season, distributor size, facility count, regulatory change, unrelated product outages, account consolidation, discount timing, and the unknown overlap between activity and cost cohorts.

A signed renewal at net price is WTP evidence. A verbal acceptance, pricing-page visit, usage, or unsigned order is not. A discount above 10% is evidence for the net price and triggers a reason code. Procurement delay is “pending” until the buyer’s stated decision deadline, then rejection if unsigned. Churn is classified as price/package, missing value, deployment failure, service failure, business closure/consolidation, or competitor switch. Renewal without deployment is reported separately; expansion requires a paid order.

Precommitted pricing branches:

- **keep:** Roll the package to the next cohort if at least 6 of 8 sign, at least 5 pay within terms, aggregate net ACV rises at least 20%, projected cohort margin is at least 70%, no account falls below 55%, and the effects gate holds.
- **change:** If 4–5 sign, or more than half require discounts above 10%, change only the metric, allowance, service scope, or price implicated by recorded objections; retest on the next four renewals.
- **segment:** Use distinct Records and Audit packages if at least 3 of 4 accounts in an observed behavior group accept one package while fewer than half of another group do, and the split also improves measured cost-to-serve. Do not infer a segment from usage alone.
- **grandfather:** Keep $18,000 for at most one additional annual term when a positive-contribution account would otherwise churn specifically because of migration shock. Include a usage cap, a dated migration plan, and no automatic renewal at the old terms. Grandfathering is not counted as acceptance of the new package.
- **stop:** Stop new-package quotes if fewer than 4 of 8 sign, test-cohort net revenue retention would fall below 90%, either margin gate fails, or any compliance/record-integrity guard fails. Honor signed contracts and return the next cohort to the current offer while diagnosing the failed assumption.

Selected branch now: run assisted, annual, usage-bounded renewal packages; do not launch the seat self-serve or unlimited plans. Retention and record-integrity gates precede expansion. Preserve a narrow grandfather path and the option to standardize low-touch sales only after five deployments prove procurement and implementation are actually repeatable. Delay costs are one renewal cycle of mispriced high-cost accounts versus the much larger cost of irreversible broad repricing. After a keep/segment result, growth owns the proven sales cohort; after change/stop, business models retains the decision and learning executes the diagnosed evidence task.
