# 90-day decision plan

The company has enough evidence to keep selling, but not enough to scale the current model unchanged. A 67% paid-pilot renewal rate is encouraging, and the renewed sites improved on-time delivery by 9 percentage points—from 86% to 95%. But that outcome is measured only at renewed sites, while the six nonrenewals and the cost concentration among large pharmacies are warning signs. The next 90 days should prove three things: which pharmacies have repeatable willingness to pay, whether a volume-based price restores healthy contribution margin, and whether the wholesaler can acquire customers without controlling the company’s route to market.

The default make-or-partner decision should be to retain the dispatch partner during this period. Do not authorize the $600,000 build yet.

## Decisions to reach by day 90

1. Adopt a pricing structure that separates software value from delivery-dependent third-party cost and prevents large sites from being subsidized by small ones.
2. Select an initial ideal customer profile and a repeatable, owner-led sales motion, while accepting a wholesaler deal only if it passes a limited, nonexclusive test.
3. Continue partnering for dispatch unless a measured volume, product-differentiation, and reliability case clears an explicit investment gate.

## Days 1–15: establish the facts

Build a site-level economics and behavior table for all 18 pilot pharmacies. For each site, capture monthly delivery volume, baseline and ending on-time rate, technician usage, support hours, compute cost, partner-API transactions, courier mix, implementation effort, renewal outcome, and stated reason for renewing or leaving. Separate recurring support from onboarding work.

Interview the owner and primary technician at every nonrenewed site and a representative set of renewed sites. The nonrenewal interviews should distinguish among weak product value, workflow friction, courier incompatibility, missing functionality, poor implementation, and price. Ask renewed owners what operating or financial result justified the purchase and what would make them cancel. Also interview several courier operators to identify which dispatch capabilities are genuinely unavailable through partners.

Two analytical cautions matter:

- Do not treat the 95% result as the effect for the entire cohort until the same measure is calculated for nonrenewed sites and adjusted for delivery mix or seasonality.
- Confirm exactly when the $0.40 partner fee is incurred and who pays it. If the startup bears it on every delivery, 2,500 deliveries alone cost $1,000 per month before compute and support, so a $500 all-inclusive subscription is structurally unprofitable.

The CEO should own customer and buyer interviews, the operating/finance owner should own site contribution margins, and the CTO should own API usage, reliability, and dispatch requirements.

## Days 16–30: design the commercial tests

### Pricing

Replace “one price for every site” with a transparent two-part structure for new proposals:

- A platform subscription covering route optimization, standard integrations, reporting, and a defined support level.
- A metered delivery/connectivity charge covering any per-delivery partner expense, with that expense excluded from unlimited usage. If the startup pays $0.40 per delivery, test a charge of at least $0.40 plus a modest operations margin rather than absorbing it.

Test three platform tiers rather than committing immediately to exact permanent prices. A practical starting proposal is:

| Tier | Monthly deliveries | Platform price to test | Service boundary |
|---|---:|---:|---|
| Core | Up to 2,500 | $500/month | Standard onboarding and support |
| Growth | 2,501–5,000 | $800–$1,000/month | Higher usage and scheduled operational review |
| High-volume | Above 5,000 | Custom, with a stated minimum | Priced from measured compute, support, integration, and SLA needs |

The ranges are test prices, not conclusions. Quote them to new buyers and use structured choice interviews with current owners. Track acceptance, objections, discount requests, and contribution margin by tier. Keep the 12 renewed customers on their agreed terms during the 90-day test, but show them the prospective structure and give advance notice that any change would occur at their next renewal. Do not retroactively surprise the customers who supplied the strongest evidence.

Set a pricing gate before testing: every tier must cover measured variable compute, recurring support, and third-party delivery expense while meeting a company-approved contribution-margin floor. A useful initial floor is 70%; if a segment cannot support it at a price owners accept, narrow the product or stop targeting that segment.

### Direct sales motion

Continue founder-led direct selling so the company does not lose customer learning to a channel. Prioritize pharmacies with enough delivery volume and lateness pain to value the product, but do not exclude high-volume sites merely because the old price made them expensive. Reprice them.

The sales sequence should explicitly serve the three parties involved:

1. Validate technician workflow and courier compatibility with the daily user.
2. Present the owner with a site-specific business case: deliveries affected, technician time, failed-delivery or complaint costs, and expected service improvement. The claim can be framed concretely as 90 additional on-time deliveries per 1,000 if a site reproduces the observed 9-point improvement, without promising that every site will do so.
3. Confirm operational responsibilities and API/SLA coverage with the outside courier.

Replace the open-ended ten-week pilot with a paid, time-boxed proof of value for new accounts: baseline measurement, implementation deadline, usage threshold, on-time target, and a pre-scheduled owner decision. The proof should convert to a clearly priced subscription only after those terms are acknowledged up front.

### Wholesaler counterproposal

Do not accept 25% revenue share, two-year blanket exclusivity, and a custom integration as one untested package. Access to 600 pharmacies is not the same as qualified introductions or closed customers.

Offer a 90-day, nonexclusive channel validation covering a named cohort of roughly 30 pharmacies. Require the wholesaler to provide qualified owner introductions and co-run outreach. Avoid building the full custom integration until several cohort customers have signed contingent orders or the wholesaler funds the work.

The counterproposal should include:

- Revenue share only on collected software subscription revenue from accounts demonstrably sourced by the wholesaler, excluding taxes, refunds, implementation charges, and pass-through courier/API fees.
- A limited share period, such as 15%–20% for the first 12 months, or at most the requested 25% for the first 12 months if there is no exclusivity and the wholesaler takes meaningful selling and first-line support responsibility.
- No exclusivity during the test. Any later exclusivity must be narrow by geography and channel, earned through minimum paid-account or net-revenue commitments, and lost automatically when those commitments are missed.
- Clear ownership of customer relationships and data, permission for the startup to support users directly, integration acceptance criteria, security responsibilities, termination rights, and no restriction on direct sales or other courier relationships.

## Days 31–60: run the tests

Quote the tiered price and metered partner charge in at least 10–15 qualified direct opportunities spanning both sides of the 2,500-delivery boundary. The sample is for learning, not statistical proof. Review the funnel weekly: qualified owner meetings, technician validations, proofs started, time to activation, paid conversions, discounts, estimated contribution margin, and loss reason.

Run the wholesaler cohort in parallel only after the test terms are signed. A reasonable continuation gate is at least 30 qualified introductions, 15 owner demonstrations, and six paid contracts or an equivalently strong conversion rate, while preserving the same margin floor as direct sales. Compare channel acquisition cost, sales-cycle time, implementation load, retention signals, and data access against the direct funnel. Count wholesaler labor and revenue share as acquisition cost rather than treating the leads as free.

For dispatch, use this period to negotiate with the incumbent and obtain at least two alternative partner proposals. Ask for volume bands below $0.40, SLA remedies, data portability, termination rights, and a transition plan. Instrument API failures, latency, manual interventions, missed SLA events, and product requests blocked by the partner. The CTO may build a thin internal adapter or failover interface if it reduces lock-in, but should not begin the six-month dispatch platform.

## Days 61–90: decide and operationalize

Hold one decision review using a single scorecard.

For pricing, choose the simplest tested tier boundaries that keep conversion acceptable and clear the contribution-margin floor. Publish usage definitions, overage handling, support limits, and renewal terms. Migrate existing customers only at a normal renewal point with notice. If high-volume pharmacies accept higher platform prices and remain attractive after all costs, keep them in the ICP; if not, stop selling that segment until cost or willingness to pay changes.

For go-to-market, retain direct selling as the learning and benchmark channel. Expand the wholesaler relationship only if its cohort produces qualified, profitable customers faster than direct sales and the contract meets the redlines. If the wholesaler insists on blanket exclusivity without enforceable minimums, walk away. If exclusivity is later justified, make it conditional—for example, it activates only after the agreed paid-account threshold and terminates automatically if quarterly commitments are missed.

For dispatch, compare partner and build options over the same 24–36 month horizon. The $600,000 build cost alone equals 1.5 million deliveries at $0.40 each, before adding maintenance, on-call operations, carrier integrations, insurance or compliance work, and the opportunity cost of six months from an 11-person team. Amortized over 24 months, the up-front cost alone requires 62,500 deliveries per month to match the current API fee; over 36 months it requires about 41,700. Those are optimistic break-even volumes because they omit ongoing internal cost and the value of the partner SLA.

Approve a build only if all of the following are true:

- Credible contracted or near-contracted volume exceeds a recalculated break-even point that includes ongoing engineering and operations, not just the $600,000 estimate.
- Partner limitations are repeatedly causing material lost revenue, churn, or inability to deliver a capability customers will pay for.
- The company can meet or exceed the partner’s reliability, coverage, security, and incident-response obligations.
- The investment has an acceptable payback under a downside-volume case and does not displace higher-return work in route optimization and customer retention.

Otherwise, renew or renegotiate the partner agreement, add a second provider or abstraction layer to reduce dependency, and revisit the build decision when volume or strategic evidence changes.

At day 90 the founders should have a priced offer with visible unit economics, a buyer-and-user sales playbook, a measured answer to whether the wholesaler is a productive channel, and a dispatch decision grounded in observed constraints rather than the appeal of owning more of the stack.
