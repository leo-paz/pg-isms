# 90-day decision plan

The next 90 days should optimize for learning and cash discipline, not for locking the company into a channel or a new operating business. The evidence is promising but still thin: 12 of 18 paid-pilot customers renewed, and renewed sites improved on-time delivery by nine percentage points. That supports continued selling and pricing experiments. It does not yet justify two-year exclusivity or a $600,000 courier-dispatch build.

## Decisions to make now

1. **Keep route optimization as the core product.** Continue partnering for courier execution during this period. The API is variable-cost, comes with an SLA, and avoids consuming roughly six months of engineering capacity.
2. **Replace flat pricing with a base-plus-usage model.** Larger pharmacies should no longer pay the same amount while causing most compute and support cost.
3. **Do not accept the wholesaler proposal as written.** Explore a short, nonexclusive, measurable distribution pilot with no bespoke integration until the channel proves incremental demand and workable economics.

## Pricing plan

### Days 1–30: establish willingness to pay and unit economics

Interview all 18 pilot customers, separating renewed and non-renewed accounts. Speak with both technicians and owners: technicians can explain adoption and workflow friction, while owners can explain purchase criteria, budget, and renewal decisions. Ask the six non-renewers what failed—value, implementation, reliability, price, delivery volume, or organizational readiness—without treating their answers as a request for immediate feature work.

Build an account-level contribution model that includes monthly deliveries, compute, support time, partner API charges, implementation effort, gross revenue, and renewal status. Segment customers by delivery volume and operational complexity. The current fact that accounts above 2,500 monthly deliveries produce 60% of compute and support cost is enough to end uniform pricing, but not enough to choose tier boundaries blindly.

Test a simple offer with new prospects:

- A monthly platform fee covering software access, standard support, and a defined delivery allowance.
- A per-delivery fee above the allowance, or volume tiers whose prices rise with usage while the effective per-delivery rate falls modestly.
- A one-time implementation fee for data setup and workflow configuration.
- Separately priced premium support or complex integrations.

Use the existing $500 monthly price as the smallest-plan reference, not as a universal price. For example, the team could test $500 for up to 1,000 deliveries, $900 for up to 2,500, and $1,500 plus overage above 2,500. These are test prices, not final commitments. Quote at least two price variants across comparable prospects and record close rate, objections, expected usage, and projected gross margin. Do not retroactively reprice renewed pilot customers during the first 30 days; give them notice and a migration path after the structure is validated.

### Days 31–60: run paid pricing experiments

Sell five to ten new paid implementations using the new structure. Avoid free pilots. If risk reduction is needed, offer a 60-day paid trial with explicit baseline metrics, activation requirements, and a conversion date.

Anchor the sales case on owner economics rather than the abstract routing algorithm: on-time delivery, technician time saved, fewer patient complaints or redeliveries, and delivery cost per completed order. Instrument these outcomes at every site. The nine-point on-time improvement is useful proof, but it comes only from renewed locations and may reflect selection effects; use it as a case study, not a universal promise.

### Days 61–90: choose and roll out the pricing architecture

Adopt the price structure only if the new accounts show acceptable projected contribution margins after partner API, compute, support, and onboarding costs. A practical gate is at least 70% gross margin at normal usage, with no tier becoming less profitable as delivery volume rises. Adjust allowances and overages if large sites still compress margins.

Offer existing renewed customers a grandfathered transition, such as their current price through the next renewal and then migration to the appropriate tier. Publish clear limits so customers understand what drives the bill.

## Direct sales and wholesaler channel plan

### Direct sales motion

For 90 days, focus outbound work on independent pharmacies with enough same-day delivery volume to feel the pain but enough margin under the new pricing model to be attractive. The buying group should be explicit:

- Pharmacy technician: workflow user and operational champion.
- Owner: economic buyer and contract approver.
- Courier service: implementation stakeholder, not the primary buyer.
- Patient: beneficiary whose service outcomes help demonstrate value.

Create a repeatable sales process: qualify delivery volume and courier setup; establish a four-week operational baseline; agree on two or three success metrics; run a paid implementation; review results with the owner; and convert to an annual agreement. Track lead-to-paid conversion, activation time, technician weekly usage, performance improvement, renewal intent, and contribution margin by segment.

### Wholesaler negotiation

Reject two-year exclusivity at this stage. The wholesaler's reach is valuable, but access to 600 pharmacies is not the same as qualified pipeline, and a 25% revenue share plus custom engineering could erase the margin gained through better pricing. Exclusivity would also prevent the startup from learning through other wholesalers or direct sales before the channel is proven.

Counter with a 90-day, nonexclusive pilot covering 20–30 named pharmacies. Require the wholesaler to provide specific marketing placements, introductions, sales enablement, and a minimum number of qualified opportunities—not merely database access. Limit the integration to standard APIs or a narrowly scoped connector funded by an integration fee or shared development cost. Pay revenue share only on net-new accounts sourced and materially assisted by the wholesaler, ideally 15% during the first contract year rather than 25% indefinitely.

Compare the channel cohort with direct sales using customer acquisition cost, sales-cycle length, activation, revenue, support burden, gross margin after revenue share, and renewal intent. Consider broader distribution only if the wholesaler produces a materially lower acquisition cost or faster sales cycle while preserving target gross margin. Any later exclusivity should be narrow—defined territory or named accounts, short duration, minimum revenue commitments, performance escape clauses, ownership of customer data, and no restriction on existing direct customers.

## Make-or-partner plan for courier dispatch

Do not approve the $600,000 build during these 90 days. At the stated API price, $600,000 equals 1.5 million deliveries before considering maintenance, dispatch operations, insurance and compliance exposure, support, uptime engineering, or the lost opportunity cost of six months of product development. The current partner also bears SLA responsibility. The real comparison is therefore not $600,000 versus $0.40 per delivery; it is the full cost and strategic value of becoming a dispatch platform versus the full partner cost and risk.

In days 1–30, measure current and forecast delivery volume, partner API spend, SLA performance, outage impact, routing constraints, courier coverage, integration friction, and customer demand for dispatch features. Ask whether dispatch is actually a purchase blocker and whether customers would pay enough for it.

In days 31–60, negotiate partner economics using aggregate volume forecasts: volume discounts, service credits, data portability, termination assistance, and a nonexclusive contract. At the same time, scope the smallest internal alternative: a dispatch-control layer that can switch or add courier providers, rather than building a courier network or complete dispatch stack.

In days 61–90, make a written decision using three gates:

- **Economics:** credible three-year internal total cost is lower than partner costs at conservative volume, including ongoing engineering and operations.
- **Customer value:** dispatch is repeatedly a material purchase or retention driver, with validated willingness to pay.
- **Strategic control:** partner limitations materially block reliability, differentiation, geographic expansion, or bargaining power and cannot be solved through contract terms or a second provider.

If all three gates are met, fund a staged technical prototype with explicit milestones rather than the full $600,000 commitment. If they are not, retain the partner, negotiate better terms, and build provider abstraction only where it reduces concentration risk.

## Day-90 scorecard and decisions

At day 90, the founders should review one scorecard:

- Paid customer count, renewal and churn reasons.
- Contribution margin by delivery-volume tier.
- Direct and wholesaler-sourced acquisition cost and sales-cycle length.
- Activation time and technician adoption.
- Changes in on-time delivery, redeliveries, support burden, and owner-relevant savings.
- Partner API cost, SLA performance, and forecast volume.

The default day-90 outcome should be a validated usage-aware price, a repeatable owner-led direct sales motion, a small nonexclusive wholesaler experiment if acceptable terms are secured, and continued courier partnership with improved commercial terms. The company should reverse any of those defaults only when the measured cohort economics and customer evidence support doing so.
