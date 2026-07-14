# 90-day business-model decision plan

## Decisions to make now

1. **Keep selling route optimization, not courier operations.** Continue using the courier API for the next 90 days and defer the proposed $600,000 dispatch build. The API converts dispatch into a variable cost, includes an SLA, and preserves scarce engineering capacity. At $0.40 per delivery, the build cost alone equals 1.5 million API-delivered orders, before maintenance, operations staff, carrier coverage, reliability, and opportunity cost. In-house dispatch should be reconsidered only if partner dependence is harming sales or service, or if measured volume and gross-margin savings support a compelling full-cost payback.
2. **Replace flat pricing with a base fee plus usage tiers.** Large pharmacies should not pay the same amount while producing most of the cost. Preserve a simple entry point for smaller sites, but charge for delivery volume and high-touch service.
3. **Treat the wholesaler as a testable channel, not a company-defining commitment.** Do not accept two-year exclusivity on the proposed terms. Offer a short, nonexclusive, performance-gated launch with clear integration economics.

The pilot produced a promising but incomplete signal: 12 of 18 customers renewed, and renewed sites improved on-time delivery by nine percentage points, from 86% to 95%. The next 90 days should identify why six customers left, prove whether that result is reproducible, and establish profitable acquisition and servicing before pursuing broad distribution.

## Pricing plan

During the first two weeks, calculate contribution margin for every pilot site. Include courier API usage, compute, implementation, support time, and any customer-specific work. Segment sites by monthly deliveries, especially above and below 2,500, and interview all six non-renewers plus a representative set of renewers. Distinguish failures of value, price, usability, delivery-partner performance, and owner approval. Technicians are users, but the commercial case must be written for owners.

Use those findings to test a three-part price:

- A platform fee of roughly **$400-$500 per location per month**, covering the core product and a defined support allowance.
- A delivery allowance suited to smaller pharmacies, followed by a **per-delivery charge or volume tier**. The exact rate should target at least a 70% gross margin after all variable service costs rather than merely marking up compute.
- Separate charges for onboarding, custom integrations, premium support, and SLA requirements that create material work.

For example, quote a small tier through 1,500 deliveries, a growth tier through 2,500, and an enterprise tier above 2,500 with usage-based overage. The thresholds are more important initially than perfect list prices: they make cost-to-serve visible and prevent the largest sites from being subsidized by the smallest. Grandfather current renewals at $500 for 60-90 days, then offer migration choices so a sudden price change does not contaminate retention learning.

Run pricing tests on new prospects rather than renegotiating every renewal at once. Alternate two or three approved packages, record close rate and objections, and require founder approval for discounts. Each proposal should show owner-facing value: on-time rate, staff time saved, failed deliveries avoided, and patient-service impact. Do not claim the 95% result as universal; present it as pilot evidence and establish a baseline and target for each new customer.

By day 45, select the structure that produces the best combination of conversion, expected annual contract value, and contribution margin. By day 90, require every new contract to use that structure. Success means no new account is knowingly below the gross-margin floor, large accounts contribute more gross profit than small ones, and price-related losses are understood rather than hidden in ad hoc discounts.

## Direct sales and channel plan

Build a focused direct-sales motion before scaling access to 600 pharmacies. The ideal initial account is an independent pharmacy with enough same-day deliveries to feel the routing problem, an identifiable technician champion, an owner willing to review an economic case, and an existing courier relationship compatible with the product.

For each qualified prospect, use a two-thread sale:

- With technicians, demonstrate route creation, exception handling, and reduced manual work.
- With owners, agree in advance on baseline metrics and a purchase decision date. Report on-time delivery, cost per completed delivery, technician time, redeliveries, and patient complaints.

Offer a standardized paid evaluation, not open-ended custom work: 30 days, a defined delivery-volume allowance, standard onboarding, explicit success criteria, and automatic conversion to an annual or month-to-month paid plan unless either side opts out at review. Ask renewed pilot customers for references and introductions, contingent on their actual satisfaction.

For the six non-renewers, complete structured loss interviews by day 15. Attempt a rescue only when a specific correctable issue exists; discounts alone would obscure product-market evidence. For the twelve renewers, schedule owner reviews and seek longer commitments after demonstrating site-level return, not merely operational usage.

Counter the wholesaler with a **90-day, nonexclusive channel pilot** covering perhaps 25-50 named pharmacies. A workable agreement would include:

- Revenue share only on customers sourced and actively supported by the wholesaler, ideally 15%-20%, or 25% only if the wholesaler performs meaningful sales, onboarding, and first-line support.
- No general exclusivity. Any future exclusivity should be narrow by geography or named accounts, last no more than six months at a time, and activate only after minimum signed-customer and revenue targets are met.
- A paid integration or a nonrefundable minimum-revenue commitment that covers development and maintenance.
- Ownership of customer, usage, and performance data; direct access to pharmacy users and owners; no restriction on direct sales outside the defined cohort.
- Clear lead attribution, payment timing, support responsibilities, security obligations, termination rights, and continued service for acquired customers after termination.

The channel earns expansion only if it beats direct acquisition economics without weakening learning or control. By day 90, compare channel and direct cohorts on qualified-to-close conversion, sales-cycle length, acquisition cost, activation, support hours, revenue per site, gross margin, and early retention. Six hundred leads have little value if exclusivity blocks better routes to market or the integration consumes the team.

## Make-or-partner plan

Reject the six-month dispatch build as the current default, but use the next 90 days to reduce partner risk and collect evidence for a later decision.

In days 1-30, document actual API volume, cost, uptime, latency, failed dispatches, support incidents, and lost or delayed sales attributable to the partner. Review the SLA and remedies, data portability, rate-change terms, termination rights, and whether another courier API can serve as a fallback. Separate route-optimization failures from courier execution failures so product performance is not misdiagnosed.

In days 31-60, create a lightweight portability layer around the existing integration and evaluate one backup provider. This is not a dispatch product; it is limited insurance against lock-in. Negotiate volume discounts and better service terms with the current partner using forecasted volume, without promising exclusivity.

In days 61-90, write a make-or-partner investment case using full costs. Building becomes credible only if all of the following are true:

- Forecast delivery volume creates a strong payback, using avoided partner fees net of cloud, maps, messaging, support, insurance, compliance, carrier operations, and ongoing engineering.
- Owning dispatch materially improves customer value or unlocks sales that partners cannot serve.
- The company can meet or exceed the partner's reliability and geographic coverage.
- The work does not delay improvements to the route-optimization product that customers are already buying.

At present, those conditions have not been demonstrated. A $600,000 commitment would consume substantial capacity for an 11-person company and would shift it into an operationally different business.

## 90-day operating cadence

### Days 1-15: establish evidence

- Assign one founder as business-model owner and one analyst or operator to maintain a site-level economics dashboard.
- Interview all six non-renewers, at least six renewers, technicians, owners, and several courier operators.
- Calculate contribution margin and outcome changes by site and delivery-volume band.
- Freeze custom feature commitments while the wholesaler integration is scoped.
- Define standard pilot, pricing, discount, and success-measurement rules.

### Days 16-45: run controlled tests

- Put 10-15 qualified direct prospects through the standardized sales motion and test the new packages.
- Migrate no existing customer until it receives an owner-level value review.
- Negotiate the limited wholesaler pilot; walk away if exclusivity, minimum performance, data access, and integration funding cannot be resolved.
- Instrument partner performance and scope a backup integration path.

### Days 46-75: choose and expand

- Select one list-price architecture and document exception rules.
- Launch the wholesaler cohort only if its contract passes the stated gates.
- Convert successful direct evaluations and request annual commitments where value has been proven.
- Negotiate courier API economics and test operational failover with a backup provider.

### Days 76-90: make the gates explicit

Hold a board-level decision review using a single scorecard. Adopt the new pricing if it sustains the gross-margin floor and does not create an unacceptable conversion decline. Expand the wholesaler channel only if it produces activated customers with competitive acquisition cost, margin, and support load; otherwise end the pilot without broader exclusivity. Continue partnering for dispatch unless the full-cost analysis demonstrates a realistic payback within roughly 18-24 months and a strategic advantage that outweighs execution risk.

The 90-day target is not maximum logo count. It is a repeatable model in which the technician adopts the product, the owner can see and approve the return, each account pays in proportion to its cost and value, and distribution does not surrender strategic flexibility.
