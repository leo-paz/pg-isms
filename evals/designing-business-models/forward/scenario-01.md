Case ID: scenario-01
Reviewer ID: business-model-forward-004

Primary owner: `designing-business-models` — product value is established, but payer and willingness to pay are not.

Handoffs:

1. `learning-from-users` executes the interviews and observes purchase/deployment behavior under the economic test below; it does not choose the payer or price.
2. `shipping-and-iterating-products` implements the three bounded offers, billing, entitlements, and rollback.
3. `engineering-for-leverage` measures account-level hosting/support cost and implements data permissions and audit logs.
4. `acquiring-and-growing-users` remains paused on ads and scalable acquisition until a paid branch is selected; it then owns channel cohorts.

## Business-Model Record

| Field | Current record |
|---|---|
| Product and state | Capital-light cash-flow software; 42,000 weekly active independent-restaurant owners, 61% twelve-week retention, and repeated evidence that invoice forecasting prevents missed payroll. The company/survival state is not supplied, so cash runway must be verified before spend; no default-dead condition may be assumed. |
| Binding constraint | Capture, not product value or top-of-funnel growth: no payer, buyer, price, or discriminating commitment has been tested. |
| Latency and error cost | Restaurant payment can be observed inside six weeks; accountant deployment may take several weeks; lender procurement is likely slower and must be recorded rather than interpreted as rejection early. Pricing is reversible for a closed cohort. Lender data access has high privacy, power, and regulatory error cost. |
| Facts to verify by 2026-07-18 | Runway; current hosting, support, acquisition, assurance, and compliance costs; retention by account and value event; payroll-miss outcome definition; current law and permissions for sharing forecasts; restaurant, accountant, and lender budgets and procurement paths; channel conflicts. Each current fact gets a dated source. |

| Candidate segment | Beneficiary / user / buyer / payer / channel | Value event, alternative, budget, effects | Actual behavior and confounders |
|---|---|---|---|
| Restaurant owner | Owner is known user and beneficiary; owner as buyer/payer is untested. Channel is the existing in-product relationship. | Value event is a forecast used to avoid a missed payroll. Alternatives are spreadsheet, bank balance, bookkeeper, or reacting late; budget is unknown. Intended effect is fewer payroll misses without deceptive urgency or loss of access to essential history. | Aggregate weekly activity and twelve-week retention are known, but payment, paid renewal, expansion, and segment-level deployment are zero/unknown. Seasonality, restaurant size, payroll cadence, and novelty may confound use. |
| Accountant/bookkeeper | Accountant may be user and buyer; restaurants remain beneficiaries; firm or client may pay. Channel is direct outreach to firms already connected to consenting active owners. | Value event is managing several clients before cash shortfalls. Alternatives are spreadsheets/accounting-suite alerts; budget and client pass-through are unknown. Effects include better advice but also duty, permission, and data-separation risk. | No firm use, payment, deployment, renewal, retention, or expansion evidence exists. Existing client relationships and bundled services could confound adoption. |
| Lender | Lender may buy/pay; restaurant remains beneficiary and data subject; lender staff may use an aggregate risk workflow. Channel is six direct pilot invitations. | Value event is a consented forecast used for early assistance, not automated adverse credit action. Alternatives are statements and underwriting tools; budget is unknown. Effects may include help or discriminatory/opaque credit treatment, so permission and human review bind. | No lender use or payment evidence exists. Procurement, security review, and portfolio size confound latency. Investor or lender enthusiasm is not a paid deployment. |

| Economics field | Restaurant owner | Accountant | Lender |
|---|---|---|---|
| WTP evidence | None | None | None |
| Test value metric | One protected restaurant using payroll-risk forecasts | Number of consented client restaurants actively monitored, with a cap | One consented, human-reviewed portfolio deployment; no credit-decision rights |
| Bounded offer | $49 for the first month, charged now, for forecast alerts and scenario planning; 90 qualified owners | $299 for the first month for up to 20 consented clients; 30 firms | Six-week $5,000 paid pilot, 50% due on signature; six lenders |
| Revenue timing / sales effort | Card payment before entitlement; in-product assisted conversion | Card/invoice before firm deployment; one onboarding call | Signed procurement-approved order and deposit; founder-led sale |
| Implementation / support / cost | Support and marginal compute measured per account | Onboarding, permission, support, and compute measured per active client | Security, legal, integration, human review, and support measured separately |
| Margin, concentration, switching, expansion | Unknown until cost instrumentation; require projected gross margin at least 70% before scaling. Report payer concentration and cancellation/export friction. Expansion is not inferred from more use; it requires a larger paid package or renewal. | Same 70% gate and firm concentration report | No margin conclusion within six weeks unless all assurance and sales effort is included; concentration and dependency are explicit |

Payment means collected, non-refunded cash tied to an activated entitlement; for a lender it means a signed order plus the non-refundable deposit and an approved deployment path. Praise, clicks, ad impressions, survey answers, bids, retained free use, and unsigned pilot interest are not payment. A paid but undeployed account is recorded separately. A renewal is a second collected payment after at least 30 days of usable deployment. Discounts count as evidence only at the net paid price. Churn is classified as price, missing value, deployment failure, closure/seasonality, or service failure before interpretation.

## Six-week capture test

- **Owner and dates:** Head of product owns the economic decision from 2026-07-15 through 2026-08-25. Research executes conversations; engineering ships gated billing by 2026-07-22. Offers open by 2026-07-25 so 30-day continuation is observable by the review.
- **Sample:** Randomize only qualified accounts that experienced the payroll-forecast value event in the prior 30 days: 90 restaurants, 30 accountant firms with consenting clients, and six lenders. Record nonresponse in the denominator. Keep the existing product unchanged for everyone else.
- **Cost and exposure:** Cap incremental implementation/research spend at $30,000 and invitations at the stated sample sizes. Do not sell or share restaurant data. No ads, impression optimization, automated credit action, public price change, annual contract, or silent downgrade is allowed.
- **Metrics:** First payments, activation within seven days, 30-day paid continuation, paid deployment, fully loaded marginal cost, gross margin, payroll-miss outcome, forecast error, support burden, permission incidents, complaints, and concentration. Report each segment separately.
- **Effects gate:** The paid cohort must not worsen forecast error or payroll-miss incidence relative to a matched free cohort by more than 2 percentage points; there must be zero unauthorized disclosures or automated adverse credit actions. Any such incident stops the affected offer and triggers rollback and incident review.

Precommitted payer branches at the 2026-08-25 review:

- **pay:** A segment qualifies if restaurants collect at least 27 of 90 first payments with at least 22 still paid at day 30; accountants collect at least 9 of 30 first payments with at least 7 firms deploying five or more client accounts; or lenders produce at least 2 of 6 signed pilots with deposits and approved consent/security paths. Select at most one primary payer using deployed paid conversion, evidence latency, fully loaded margin, concentration, and user-effects risk—not headline revenue. Then test a narrow range around that offer.
- **revise:** If a segment reaches at least 10% but misses its pay threshold, run one diagnosed revision to buyer, package, onboarding, or price; do not call generic interest validation. The revision must name the observed failure and keep the same effects gate.
- **preserve-free:** If no segment reaches 10% payment but retained use and payroll effects remain strong, keep the current core free for one more bounded cycle while testing a different funder or paid adjacent service. This branch requires a documented funding ceiling; it does not authorize ads by default.
- **stop:** Stop the affected monetization path if it gets no qualifying payment, cannot cover measured marginal cost at the tested price, or violates the effects/permission gate. Stop the whole experiment if survival requires a different owner or the tests exceed the spend cap.

Selected branch now: run the capture test and pause ads. Ads assume an attention-selling model, add privacy and incentive costs, and make impressions look like economic evidence. Rejected alternatives are optimizing ad inventory now, copying a competitor price, and treating engagement as willingness to pay. Preserve the free-core option outside the cohort. Switch to pricing optimization only after a pay branch; switch to growth only after deployed paid behavior and the 70% projected gross-margin gate. If survival becomes binding, hand the plan immediately to `managing-runway-and-survival`; otherwise the next owner follows the ordered handoffs above.
