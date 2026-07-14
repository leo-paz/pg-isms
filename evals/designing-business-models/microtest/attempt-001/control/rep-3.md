# 90-day decision plan

The company has promising evidence of value, but not yet enough evidence to make either large commitment. Treat the next 90 days as a set of controlled commercial tests. The goals are to identify the segment with the strongest willingness to pay, replace the flat price with economics that scale, learn whether the wholesaler can be a productive channel without surrendering the market, and compare courier partners against in-house dispatch on total cost and strategic value.

## Starting diagnosis

- A 67% pilot-to-renewal rate (12 of 18) is encouraging, and the nine-point improvement in on-time delivery at renewed sites is a credible outcome to sell. It is not yet proof of broad product-market fit: the six losses must be understood by size, usage, owner priorities, courier arrangement, and reason for non-renewal.
- The pharmacy technician is the user, the owner is the economic buyer, patients benefit, and couriers are operational partners. Sales and product discovery must cover all four perspectives rather than treating “the pharmacy” as one customer.
- Flat pricing is structurally wrong if high-volume pharmacies generate 60% of compute and support cost. Price should track a value or usage variable while remaining predictable enough for an owner to budget.
- The wholesaler could accelerate distribution, but two-year exclusivity, a 25% share, and custom work place three risks on the startup at once. Access to 600 accounts has little value unless it becomes qualified introductions, active selling, and measurable conversions.
- Spending $600,000 now to recreate an API with an SLA would consume roughly $100,000 per month for six months before proving that dispatch is a differentiator. At the current partner price, $600,000 equals 1.5 million deliveries, before counting ongoing engineering, operations, carrier coverage, support, insurance, and reliability costs for an internal system.

## Days 1–30: establish the facts and design the tests

### Pricing and retention

Interview all 18 pilot owners and a technician from each site. For the six non-renewals, classify the primary cause as insufficient value, price, implementation friction, missing feature, weak courier performance, or organizational timing. For renewed sites, document monthly deliveries, active users, support hours, compute cost, delivery improvement, avoided staff time, failed-delivery reduction, and owner willingness to recommend.

Build contribution-margin cohorts by monthly delivery volume. Include direct compute, support, the $0.40 partner fee where applicable, onboarding, channel fees, and an allocation for customer success. The immediate guardrail is that no newly sold account should have negative contribution margin at normal usage.

Offer new prospects three simple packages, while grandfathering the 12 renewals for 90 days:

- **Starter:** up to 1,000 deliveries per month, core optimization and standard support, at approximately $500 per month.
- **Growth:** 1,001–2,500 deliveries, analytics and priority support, at a higher fixed fee such as $900–$1,200 per month.
- **Scale:** more than 2,500 deliveries, a platform fee plus a per-delivery charge or committed volume band, with a minimum price based on measured cost to serve.

The dollar points are hypotheses, not permanent list prices. Test them in sales conversations without broadly publishing them. Keep courier charges visibly separate if pharmacies can choose or bring a courier, so routing software value is not confused with pass-through delivery cost. Tie the sales narrative to measurable outcomes—on-time rate, technician time saved, and fewer exceptions—not to compute consumption.

### Direct sales

Define the initial ideal customer profile using the renewal data. A likely starting hypothesis is independently owned pharmacies with meaningful same-day volume, an existing outside courier relationship, an owner who can decide quickly, and poor visibility or on-time performance—but the cohort analysis should confirm it.

Create a short owner-facing ROI calculator and a technician-facing workflow demo. Use the renewed sites to develop three permissioned case studies with baseline, result, volume, implementation time, and quotation. Ask satisfied owners for introductions to peer pharmacies. The founders should continue selling directly during this learning period; handing sales entirely to a channel would hide objections and weaken pricing discovery.

### Wholesaler negotiation

Do not accept the current offer. Counter with a 90-day, non-exclusive market-development pilot covering a named subset of 50–100 pharmacies. Require the wholesaler to supply a jointly agreed campaign, a minimum number of qualified owner introductions, sales participation, and access to funnel data. Pay the 25% share only on net software revenue from accounts the wholesaler sourced, for a limited attribution period such as 12 months; exclude delivery pass-through charges, existing prospects, and direct accounts.

Scope the integration as a paid, reusable, milestone-based project. No exclusivity should begin during the test. If the wholesaler insists on future exclusivity, limit it by geography or named account list, make it contingent on minimum annual recurring revenue and quarterly pipeline targets, include price freedom and data ownership for the startup, and add termination rights when targets are missed.

### Courier decision baseline

Freeze the proposed $600,000 build except for lightweight discovery and prototyping. Create a make-or-partner scorecard covering five-year total cost, delivery volume, SLA performance, geographic coverage, integration reliability, unit cost, roadmap control, customer demand for courier choice, compliance exposure, operational staffing, and strategic differentiation.

Ask the existing courier API provider for volume discounts, incident history, SLA remedies, data portability, and an exit clause. Benchmark at least two alternative partners or a multi-provider abstraction. Instrument current delivery count, error rate, latency, downtime, support incidents, and gross margin so the 60-day decision uses observed data.

## Days 31–60: run bounded market experiments

Sell 10–15 new paid pilots across at least three volume bands. Avoid free pilots. Use a standard 30- to 45-day implementation and success plan with a pre-agreed baseline and renewal criteria. Randomly alternate credible package presentations or use sequential cohorts so the company can compare close rate, discount requests, expected margin, and perceived fairness. Founders should review every lost deal and every requested discount weekly.

For the 12 current customers, present usage statements and preview the new packaging. Offer a choice at the end of the grandfathering period: select the appropriate tier, sign an annual commitment for a modest discount, or remain monthly at the standard rate. Do not surprise them with retroactive usage charges. For large sites, test whether quantified value supports higher pricing; for small sites, confirm that the entry package remains easy to approve.

Launch the wholesaler pilot only after signing the non-exclusive test terms. Track each lead from introduction through discovery, paid pilot, activation, and renewal. Compare the channel cohort with direct sales on qualified-introduction rate, sales cycle, customer acquisition effort, average selling price, implementation burden, support load, and contribution margin after the revenue share. The wholesaler must not control the customer relationship: the startup should retain direct contact with owners and technicians and own product-usage data.

On dispatch, run a two-week technical spike capped at a small budget to map the actual functions hidden behind the current API: courier onboarding, assignment, status events, proof of delivery, exception handling, notifications, routing, payments, support, and SLA operations. Seek written estimates for building and operating each layer. In parallel, negotiate partner pricing at projected volumes and test a thin provider-neutral adapter if vendor lock-in is the concern. The adapter is a much smaller and more reversible investment than becoming a dispatch operator.

## Days 61–90: convert evidence into decisions

### Pricing decision gate

Choose the package structure that meets all of these conditions:

- At least 70% gross margin after direct compute, support, and partner costs, or a clearly documented near-term path to that margin.
- No volume cohort is systematically loss-making.
- Paid-pilot conversion and renewal intent are not materially worse than the original offer.
- Owners can understand the price from one page and forecast their bill.
- Higher-volume customers pay more in proportion to both value and cost to serve.

If per-delivery pricing creates buyer anxiety, use committed volume bands with overage charges. If value varies more with locations than deliveries, test a per-location platform fee plus usage. Publish the final structure for new customers at day 90 and migrate existing customers with notice and a time-limited annual-commitment incentive. Set discount authority and a price floor so sales cannot recreate flat, uneconomic contracts through exceptions.

### Sales and channel decision gate

Continue founder-led direct sales in the validated ideal-customer segment and hire or assign sales capacity only when a repeatable motion is visible: consistent qualified pipeline, a defined buyer and champion, comparable objections, a bounded implementation, and acceptable pilot-to-renewal economics.

Expand the wholesaler relationship only if the test produces enough qualified opportunities and paid conversions to beat direct acquisition economics after the 25% share and integration burden. A reasonable contract gate is a mutually agreed minimum first-year revenue commitment that repays integration and channel costs, plus quarterly performance minimums. Offer narrow exclusivity only in exchange for guaranteed revenue or paid minimums; never grant blanket two-year exclusivity merely for access. If the wholesaler will not accept measurable obligations, retain it as a non-exclusive referral source or walk away.

### Make-or-partner decision gate

The default day-90 decision should be **partner, with reduced dependency**, unless the evidence shows both strategic differentiation and superior economics from owning dispatch. Continue using the SLA-backed API, negotiate volume pricing, add monitoring and an alternate-provider path, and keep the internal product focused on routing and pharmacy workflow.

Authorize an internal dispatch build only if all of the following are true:

- Customers repeatedly identify dispatch control as a decisive buying or retention factor, not merely a nice-to-have.
- Credible committed volume makes the fully loaded internal cost lower than partner costs within an acceptable payback period.
- The company can fund the build without starving sales, onboarding, reliability, and the core optimization roadmap.
- The team has a plan and budget for 24/7 operations, courier supply, compliance, support, failure recovery, and ongoing maintenance—not just six months of software development.
- A staged prototype proves a differentiated capability the partners cannot supply under improved commercial terms.

At $0.40 per delivery, the current partner remains cheaper than the proposed build until aggregate volume is very large, and the build estimate omits ongoing operating cost. If volume reaches 250,000 deliveries per month, for example, the headline API expense is $100,000 per month and the $600,000 development cost appears to break even in six months only under the false assumption that internal operation is free. The board model should instead compare five-year cash flows, include headcount and uptime obligations, and apply risk-adjusted scenarios.

## Weekly dashboard and ownership

One founder should own commercial learning and another should own unit economics and partner diligence. Review a single dashboard each week: qualified leads by source, paid-pilot starts, time to activation, technician engagement, baseline and current on-time rate, owner-reported ROI, conversion, churn reason, revenue by tier, delivery volume, direct cost, support hours, gross margin, courier incidents, and wholesaler funnel performance.

By day 90, the founders should leave with three reversible, evidence-backed commitments: a tiered price with a margin floor, a repeatable direct-sales motion supplemented only by performance-bound channels, and an SLA-backed multi-partner dispatch strategy. Revisit building dispatch only when customer demand and scale—not engineering enthusiasm—cross the explicit decision gates.
