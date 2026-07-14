# 90-day plan

## Recommendation

Use the next 90 days to prove a repeatable direct-sales offer, repair the pricing model, and test the wholesaler as a bounded acquisition channel. Do not accept the wholesaler's current terms and do not build courier dispatch now. The company should preserve scarce engineering capacity while it learns why one-third of paid pilots did not renew.

The present evidence is promising but incomplete: 12 of 18 paid-pilot customers renewed, a 67% renewal rate, and renewed sites improved on-time delivery by nine percentage points. That improvement is not yet a general causal claim because the outcome is reported only for the sites that renewed. The six losses may expose product, implementation, price, or customer-fit problems that matter more than the headline result.

## Pricing and packaging

Replace the single $500 price with a base subscription that includes a delivery allowance, followed by an overage or higher-volume tier. Monthly deliveries are observable, understandable to an owner, and reasonably aligned with both customer value and the company's compute and support burden. Do not expose internal compute units in the price.

During the first month, test three offer cards rather than immediately declaring a permanent rate card:

- An entry tier around $600-$700 per month for lower-volume pharmacies, with standard onboarding and a defined delivery allowance.
- A growth tier around $900-$1,100 per month through 2,500 monthly deliveries, with reporting and prioritized support.
- A scale tier starting around $1,500 per month above 2,500 deliveries, with volume bands or per-delivery overages. Final bands must produce the target contribution margin using actual compute, support, and partner-API costs.

These are test ranges, not conclusions. Quote half of qualified prospects the lower point and half the upper point, while holding scope constant. Record acceptance, time to close, objections, expected volume, and expected gross margin. A small implementation fee can also be tested where integration or data cleanup creates real work. Avoid unlimited custom work in any standard tier.

Give the 12 renewed customers a 90-day price hold in exchange for structured interviews, usage data, and permission to develop anonymized case studies. Then migrate them with advance notice and a loyalty discount, rather than surprising them mid-term. Interview all six non-renewers separately; founders should ask about the decision process, not try to win them back during the interview.

The product story should address each participant explicitly. Technicians need fewer manual interventions and an easy daily workflow; owners need an economic and service-quality case; patients benefit from more reliable delivery; and couriers need clean route handoffs. The buyer-facing proof should combine on-time performance with technician time saved, redelivery or complaint reduction, and delivery cost per stop.

## Direct sales and the wholesaler

For direct sales, initially target independent pharmacies with meaningful same-day volume, an owner who can participate in a short buying process, and a measurable reliability or labor problem. Do not avoid sites above 2,500 deliveries; make them profitable through the scale package. Use a founder-led motion: owner discovery, a technician workflow review, a baseline data check, then a paid, tightly scoped pilot with success criteria agreed before launch. A proposed success scorecard is on-time rate, technician hours per week, exceptions per 100 deliveries, weekly active use, and owner willingness to continue at the quoted post-pilot price.

Reject the wholesaler proposal as written. A 25% share, two-year exclusivity, and custom integration combine a permanent margin concession with channel lock-in and near-term engineering risk. Counter with a 90-day, nonexclusive market test covering a named group of 20-30 pharmacies. Revenue share should apply only to accounts the wholesaler sources and actively helps convert, and should expire or step down after the first contract year. If the wholesaler insists on 25%, require enough value to justify it: a minimum number of qualified introductions and paid conversions, participation in selling and onboarding, and a minimum revenue commitment.

Scope the integration separately. The wholesaler should pay for or co-fund it, it should use reusable interfaces, and delivery should follow a signed specification with acceptance criteria. Do not grant exclusivity merely for access to a list. If exclusivity is ultimately necessary, limit it to a narrow region or named accounts, make it short, and condition it on quarterly paid-customer and revenue minimums with automatic termination when they are missed. The startup must retain its customer relationships, product-usage data, pricing authority, and the right to serve existing and inbound direct accounts.

## Make-or-partner decision

Keep the courier API partner for this period and stop the proposed dispatch build at discovery. At $0.40 per delivery, $600,000 equals API fees on 1.5 million deliveries. Even if the build cost were the entire cost, the company would need 500,000 deliveries per year for three years merely to equal that upfront spend; that ignores maintenance, hosting, operational coverage, future feature work, implementation risk, and the value of the partner's SLA. It also ignores six months of diverted engineering work for an 11-person company.

Dispatch should be built only if it is strategically differentiating and the fully loaded economics are compelling, not simply because an API bill exists. Over the 90 days, instrument partner volume, latency, failures, support incidents, SLA credits, and cost per completed delivery. Ask the partner for volume discounts and better failure reporting. At the same time, design a thin provider abstraction and document a second-provider contingency so the company reduces dependency without recreating dispatch operations.

At day 75, compare three cases over a three-year horizon: remain with the current partner, use multiple partners, or build. The build case must include engineering opportunity cost, ongoing staffing, infrastructure, 24/7 incident ownership, migration, and a risk reserve. Approve a build only if contracted or highly probable volume yields a short payback under conservative assumptions, customers demonstrably value proprietary dispatch, and partner limitations are repeatedly blocking wins or service quality. Current evidence does not meet that bar.

## Calendar and decision gates

**Days 1-15: establish the facts.** Assign one founder to own the 90-day commercial test. Reconstruct unit economics by customer and volume band, including API, compute, onboarding, and support time. Interview the 12 renewals and six losses, map who influenced each purchase, instrument the outcome scorecard, and request a detailed wholesaler funnel and integration specification.

**Days 16-30: put offers into market.** Finalize the three test cards, a paid-pilot agreement, and two evidence-based case studies that clearly label the sample. Build a list of at least 30 qualified direct prospects and begin founder-led outreach. Deliver the bounded channel counterproposal. Negotiate API volume bands and SLA remedies; do no dispatch implementation beyond architecture and cost discovery.

**Days 31-60: run parallel experiments.** Start 8-12 direct sales conversations and seek at least six proposals across the price cells. If the wholesaler accepts the safeguards, launch its named-account test; otherwise continue direct sales without waiting. Review weekly activation, outcome, support burden, pipeline conversion, and forecast contribution margin. Fix onboarding friction that affects several customers, but decline one-off features without repeated demand.

**Days 61-90: convert and decide.** Seek at least four new paid starts or signed subscriptions, including representation from more than one volume band. Compare direct and channel cohorts on qualified-to-close conversion, sales cycle, acquisition effort, discounting, activation, retention intent, and contribution margin after revenue share. Complete the dispatch three-case analysis and decide whether to retain one partner or add redundancy. Publish the next two-quarter price card and sales playbook based on observed results.

At day 90, scale a price tier only if it has positive forecast contribution margin and prospects accept it without exceptional concessions. Expand the wholesaler relationship only if it produces incremental paid customers at acceptable margin and complies with the integration and account-ownership safeguards. Continue partnering on dispatch unless the explicit build gate is met. The goal is not to maximize logos in 90 days; it is to leave with a profitable customer definition, a repeatable buying path, and fewer irreversible commitments.
