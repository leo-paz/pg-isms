# 90-day decision plan

The next 90 days should answer three questions with evidence: what customers will pay at each delivery volume, whether the wholesaler creates profitable incremental demand, and whether owning dispatch would beat a partner after all operating costs and risks. The company should not accept the exclusivity offer or authorize the $600,000 build during this period.

## Starting diagnosis

The pilot shows real promise, but not yet a complete business model. Renewal is 12 of 18, or 67%. At renewed sites, on-time performance rose nine percentage points, from 86% to 95%; equivalently, the late-delivery rate fell from 14% to 5%, a roughly 64% reduction. That is a strong sales proof point, but it is evidence from the sites that renewed, not proof that every pharmacy will get the same result.

The flat $500 price is almost certainly misallocating value and cost. Large pharmacies generate 60% of compute and support cost, while the courier API alone can cost $1,000 per month at 2,500 deliveries if it is invoked for every delivery. Third-party transaction cost therefore cannot remain hidden inside a $500 subscription. The six non-renewals also need to be separated into product failure, weak ROI, poor onboarding, courier incompatibility, and price or budget objections before changing the offer.

## Days 1–15: establish the economic baseline

Assign one founder to own a single account-level dataset for all 18 pilot customers. For each account, record monthly delivery volume, subscription revenue, API transactions, compute expense, support hours, onboarding effort, courier provider, baseline and current on-time rate, renewal outcome, and owner and technician feedback. Interview the owner and lead technician at every site, and the relevant courier operator where possible. Ask the six non-renewers what would have changed their decision; do not infer their reasons from usage data alone.

Calculate two margins separately:

- Platform contribution = subscription revenue minus compute, allocated support, and onboarding amortization.
- Dispatch contribution = delivery fees collected minus the $0.40 API charge and dispatch-specific support.

Use a 70% platform contribution-margin target and a positive dispatch contribution target as initial guardrails. For any tier, the minimum sustainable platform price is direct monthly platform cost divided by 30%. Channel economics must be tested after the revenue share, not before it. Freeze new high-volume contracts at the current flat price until the new pricing test begins; give existing renewed customers advance notice and one billing cycle of transition protection.

This work should also produce a defensible ROI calculator. For example, at 2,500 monthly deliveries, a nine-point on-time improvement represents 225 more on-time deliveries. Convert that improvement into each owner's actual avoided redeliveries, technician time, complaints, refunds, and patient-service risk rather than assigning a generic dollar value.

## Days 16–30: put a testable price and sales motion in market

Use the following as a provisional price card, then adjust its thresholds using the cost analysis:

| Plan | Monthly routed deliveries | Platform price | Dispatch/API charge |
|---|---:|---:|---:|
| Starter | Up to 1,000 | $500/month | Separate usage charge |
| Growth | 1,001–2,500 | $900/month | Separate usage charge |
| Scale | 2,501–5,000 | $1,500/month | Separate usage charge; custom quote above 5,000 |

Charge the partner dispatch service separately at the greater of $0.50 per API delivery or the amount required to maintain the chosen dispatch margin. Alternatively, let the pharmacy contract directly with the courier provider. Make usage definitions, overages, and annual price adjustments explicit. Do not discount Scale back to $500; if the measured cost cannot support the proposed price at the margin guardrail, raise the price or narrow the included service.

Offer annual contracts with a modest incentive, such as one month free, only after the customer has demonstrated success. Replace the ten-week generic pilot with a 30–45 day paid deployment at the intended tier price. Before launch, agree on a baseline, an on-time target, required data access, the technician workflow, and an owner decision meeting already scheduled for the end of the pilot.

Focus direct sales on independent pharmacies with meaningful same-day volume, on-time performance below roughly 92%, outsourced courier operations that the product supports, and an owner who can quantify the cost of late delivery. The sales sequence should reflect the buying system:

1. A technician workflow session establishes usability and internal advocacy.
2. A courier compatibility review prevents an integration surprise.
3. An owner meeting presents the site-specific ROI, price, and success criteria.
4. The close uses measured operational results, not patient benefit alone.

Market the observed result accurately: renewed pilot sites improved from 86% to 95%. Avoid implying that all 18 sites achieved it. Track proposal-to-paid conversion, time to launch, support hours, gross margin by tier, and conversion from paid deployment to contract.

## Days 16–45: counter the wholesaler offer

Access to 600 pharmacies is not equivalent to 600 customers, so two years of exclusivity should not be exchanged for a prospect list. Counter with a 90-day, non-exclusive market test involving 30–50 named pharmacies. Require the wholesaler to provide qualified introductions, a co-selling owner, funnel data, and a campaign schedule.

The commercial terms should include:

- The 25% share applies only to collected platform subscription revenue from accounts the wholesaler sourced, not taxes, pass-through courier/API charges, or professional services.
- The share steps down after the first contract year, or is replaced by a fixed acquisition fee once customer acquisition payback is known.
- The custom integration has a fixed scope and acceptance criteria and is paid for by an upfront integration fee or a non-cancellable minimum-revenue guarantee.
- The startup retains product IP, customer usage data rights needed to operate the service, pricing control, and direct access to users and owners.
- Any later exclusivity is regional and conditional on quarterly minimums for activated, paying, retained accounts. Missing a minimum automatically restores non-exclusivity.
- The agreement includes termination rights for poor lead delivery, slow integration approval, channel conflict, or economics below the margin floor.

At the current $500 price, the startup keeps only $375 before serving the account, which is especially unattractive for high-volume pharmacies. Channel accounts therefore use the same volume tiers and must clear the margin floor after the 25% share. If the wholesaler refuses a measured test, integration funding, performance minimums, or direct customer access, decline the offer and continue direct sales.

## Days 31–60: run the experiments

Sell the new price card directly to at least six new paid deployments across the three volume bands, including at least two Scale prospects. In parallel, run the wholesaler test only if the counterterms are accepted. Do not count introductions or demos as channel success; count paid activations that reach the agreed operational milestone.

Review results every week in a compact dashboard: qualified opportunities, proposals, wins and losses by reason, deployment time, on-time change, technician adoption, owner-stated ROI, revenue, direct cost, support time, and contribution margin. A founder should personally review every loss and any account below the margin guardrail. Use those findings to revise packaging once, around day 45, rather than changing prices for every prospect.

## Make-or-partner decision

Keep the courier API partner for the next 90 days and do not begin the six-month dispatch build. The proposed $600,000 build equals 1.5 million deliveries at $0.40 each before accounting for maintenance, on-call coverage, additional courier integrations, security, reliability, or the value of the partner SLA. Amortized over two years, build cost alone equals the current fee at about 62,500 deliveries per month; over three years, it equals the fee at about 41,700 per month. The true crossover volume is higher once ongoing costs and risk are included. For an 11-person company, the build would also displace work on the routing product that customers have already validated.

The CTO should instead spend a tightly limited effort on leverage and reversibility:

- Instrument API volume, failures, latency, support incidents, and SLA credits by customer.
- Negotiate volume tiers, service credits, data-export rights, and a termination-assistance clause with the current partner.
- Put a thin internal interface around partner-specific calls so another provider can be added without rewriting the product.
- Evaluate one backup provider against the same workflow and SLA, without building a complete dispatch system.
- Document which lost deals, churn events, or product limitations are actually caused by the partner.

Reopen a build decision only when sustained forecast volume clears a fully loaded break-even model, not the $600,000/$0.40 headline calculation. A build should require all of the following: partner cost exceeds the 24-month fully loaded internal cost by at least 30%; partner limitations are causing material churn or lost revenue; the company can fund development without endangering runway; and it has a credible plan to meet or beat the existing SLA. Until then, negotiate and preserve optionality.

## Days 61–90: make the decisions and roll out

At day 75, lock the price architecture for the next two quarters. Keep a tier only if signed customers accept it and the measured cohort clears the margin guardrail. If Scale customers value the outcome but miss the margin target, raise the Scale price, introduce a paid support package, or reduce included service. If customers reject the price despite documented ROI, investigate segment fit and value delivery before discounting.

At day 90, use explicit gates:

- **Pricing:** proceed if the company has multiple paid wins at the intended prices, positive dispatch contribution, and at least 70% forecast platform contribution by tier. Otherwise revise the affected tier, not the entire model.
- **Sales:** standardize the technician–courier–owner sequence if paid deployments convert and launch predictably. Retain the paid, measured pilot rather than returning to open-ended trials.
- **Channel:** expand only if the wholesaler produced paid, retained accounts with economics at least as attractive as direct sales after acquisition cost. Grant limited exclusivity only against enforceable quarterly minimums and a guaranteed integration return.
- **Make or partner:** remain with the partner unless the fully loaded decision gate is met. The available facts strongly favor partnering now.

The desired outcome after 90 days is not maximum pharmacy count. It is a repeatable offer whose price rises with cost and value, a channel that earns its share through measurable distribution, and a dispatch architecture that remains reliable without consuming the startup's capital and focus prematurely.
