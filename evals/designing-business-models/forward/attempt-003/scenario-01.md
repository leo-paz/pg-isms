Case ID: scenario-01
Reviewer ID: business-model-forward-003

Primary owner: `designing-business-models`.

Handoffs:

1. `shipping-and-iterating-products` implements the bounded offers and billing paths once the test design is fixed.
2. `acquiring-and-growing-users` resumes scalable channel work only after a payer and capture model survive the test.
3. `learning-from-users` takes any newly exposed product-value uncertainty; current evidence is already strong enough to test capture.

## Diagnosis

This is capital-light software with product-value evidence but no capture evidence. The restaurant owner is the observed user and beneficiary; the buyer and payer could be the owner, an accountant managing several restaurants, or a lender, but none is established. The value event is avoiding a missed payroll. The alternatives, budgets, purchasing authority, and effects on accountants and lenders remain facts to verify.

The 42,000 weekly active users, 61% twelve-week retention, and repeated avoided-payroll evidence support continued product value. They do not establish willingness to pay. Ads would introduce a fourth payer—advertisers—without evidence that ad economics work or that ads preserve the trust and attention required for cash-flow decisions. Pause the ad launch and any impression optimization for six weeks.

The binding constraint is payer discovery, followed by capture—not fine price optimization. The test is reversible and low-capital, with a six-week evidence latency. Before launch, calculate current hosting, support, acquisition, assurance, and compliance cost per retained restaurant and record whether a paid offer changes forecasting use or payroll outcomes.

## Six-week capture test

**Week 1 — map the economic actors.** Interview a stratified sample of retained restaurant owners, their accountants, and lenders that serve them. Confirm who acts on the forecast, who can authorize spend, what budget would fund it, what they do instead, and whether data sharing or lender involvement creates permission or trust constraints. Praise, stated price interest, clicks, and letters of intent are discovery evidence only.

**Weeks 2–5 — ask for real commitments.** Run three small, separately measured offers. The prices below are labeled test assumptions, not conclusions:

- Offer 100 retained restaurant owners a $99/month forecasting-and-alerts plan, with the existing free product preserved outside the cohort. Acceptance is a cleared first payment, not a trial click.
- Offer 20 accountants a $300/month portfolio plan for up to 20 restaurant clients. Acceptance is a cleared payment plus at least three client deployments with the required permissions.
- Offer 10 lenders a six-week, $7,500 paid pilot for an explicitly defined underwriting or portfolio-monitoring use. Acceptance is a signed order, paid invoice, authorized data access, and a deployed workflow; an undeployed pilot does not count.

`shipping-and-iterating-products` should make cancellation simple, avoid dark patterns, keep financial claims truthful, and expose only the data each role is permitted to see. The test owner is the business-model lead; product owns implementation. Cap direct test exposure at the named cohorts and the cash cost at the preapproved billing and research budget. Review interim safety and deployment evidence weekly and make the final branch decision on day 42.

For each offer, record exposure, eligible decision-makers reached, cleared payments, paid deployments, time to purchase, deployment effort, support and compute cost, discount requests, retained weekly use, forecast actions, and reported payroll outcomes. Separate rejection because the wrong actor was approached from rejection because the price, package, trust, timing, or product is wrong. Treat a discount as acceptance only at the discounted economics; treat cancellation or non-use after payment as churn, not success. Confounders include restaurant size, existing accountant relationships, payroll season, lender credit policy, and unusually acute cash-flow events.

Precommit these branches:

- **pay:** A role produces repeated cleared payments and paid deployments at tolerable delivery cost, while retained use and payroll effects remain intact. Continue that payer/package and run a narrower price test.
- **revise:** Decision-makers repeatedly identify a specific, fixable packaging, permission, or price obstacle and some make a lesser real commitment. Revise once and retest that role.
- **preserve-free:** Users retain the product's value but no tested beneficiary or adjacent actor pays. Keep the useful free product, stop revenue-dependent growth, and test a different capture mechanism rather than adding ads by default.
- **stop:** A payer path produces no real commitments, requires uneconomic implementation, damages trust or retention, or creates unacceptable user effects. Close that path.

The selected branch for now is **test capture while preserving the free base**. Reject immediate ads and premature price optimization. Preserve the option to test a paid direct, accountant-portfolio, or lender-funded model. The switch condition is real payment plus deployment and acceptable unit economics; the retention/effects gate is no material deterioration in weekly forecasting use or payroll outcomes. At day 42, business models selects the surviving payer branch; product implements the next package, and growth receives the handoff only after stable paid behavior exists.
