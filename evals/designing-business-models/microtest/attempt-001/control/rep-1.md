# 90-day decision plan

The immediate recommendation is to stop treating the $500 pilot price as the production business model, keep selling directly while the company learns why pharmacies renew, run only a tightly bounded wholesaler test, and continue partnering for courier dispatch. The next 90 days should turn those recommendations into measured decisions rather than lock the company into a price, an exclusive channel, or a six-month build on incomplete evidence.

## What the current evidence does—and does not—show

The paid pilots establish real interest, and 12 of 18 renewals are encouraging, but a 67% pilot-to-renewal rate is not yet repeatable product-market fit. The improvement from 86% to 95% on-time delivery at renewed sites is a strong proof point, but it may be selected evidence: the six nonrenewers may have achieved less value, had weaker adoption, or simply had lower willingness to pay. Before extrapolating, the founders need the same outcome, usage, cost, and workflow data for all 18 sites.

The buying system has four distinct participants:

- Owners are the economic buyers. The sales case must translate the nine-point on-time improvement into fewer refunds and complaints, lower technician labor, higher patient retention, and more delivery capacity.
- Pharmacy technicians are the daily users. Their adoption, time saved, and exceptions handled will predict renewal.
- Couriers are an operational dependency. Integration reliability and handoff quality matter even if they do not buy the product.
- Patients receive the outcome. Delivery reliability, failed-delivery rates, and complaints are useful evidence, but patient satisfaction alone does not pay the invoice.

Within the first two weeks, interview the owner and lead technician at every pilot site, including all six nonrenewers. Ask nonrenewers what failed and at what price they would have stayed; do not reduce every loss to price. Build a site-level table containing deliveries, active users, routes, on-time rate before and after, failed deliveries, technician hours, support hours, compute, partner API expense, monthly revenue, and renewal reason. This will reveal whether volume, workflow complexity, courier mix, or realized value defines the best initial customer profile.

## Pricing: move to a base fee plus a metered delivery component

The present flat price is structurally wrong. Sites above 2,500 monthly deliveries consume 60% of compute and support cost while paying no more, and the dispatch partner alone costs $0.40 per delivery. At 2,500 deliveries, that API expense is $1,000 before compute or support, already twice the current monthly price. A production price must scale with both customer value and cost to serve.

Test a two-part price:

1. A monthly platform fee pays for workflow software, reporting, onboarding, and a defined support level. Create no more than three tiers based on operational complexity or delivery volume.
2. A per-completed-delivery charge covers dispatch/API and other volume-driven costs, with a visible rate and committed-volume discounts. As an initial test—not a permanent promise—quote roughly $500–$750 per location plus $0.55–$0.70 per delivery. The exact rate should be reset after site-level costs and owner willingness-to-pay are measured.

Do not hide a $0.40 variable cost inside a low flat subscription. If customers already contract and pay the courier independently, separate the route-optimization platform fee from any optional dispatch pass-through so that the company is not assuming a cost it cannot control. Price exceptions should require a written contribution-margin calculation.

During days 15–45, present three offer designs in owner interviews: base plus usage, fixed volume bands with overages, and an annual commitment with a usage allowance. Ask owners to choose and explain, then test actual quotes rather than relying only on stated preferences. New prospects should receive the new structure immediately. Give the 12 renewed customers a short, explicit transition period—such as through their current term or 90 days—rather than retroactively changing a paid agreement. In return for temporary grandfathering, seek annual commitments, reference participation, and complete usage data.

The pricing decision at day 90 should require:

- Positive contribution margin at every volume band after API, compute, onboarding amortization, and support.
- A credible path to at least 70% blended gross margin as volume and operations mature.
- Evidence that owner willingness to pay increases with measured operational value.
- Quote-to-close and renewal intent that are not being sustained by repeated discounts.

If high-volume sites remain unattractive after usage pricing, either raise their platform/support tier, constrain the service level, or decline them. High usage is valuable only when gross profit grows with it.

## Sales and channel: learn directly, then earn the right to scale

For the next 90 days, the primary motion should remain direct and founder-led. Focus on an initial customer profile derived from the pilot data, likely independent pharmacies with meaningful same-day volume, a technician who owns delivery operations, fragmented courier workflows, and measurable failed or late deliveries. The owner is the buyer; the technician should be included in discovery and the operational proof.

Turn renewal into a short sales proof: baseline the pharmacy's on-time rate and technician effort, launch with an agreed adoption plan, and report value to the owner at weeks two, six, and ten. The sale should culminate in an annual production agreement, not another indefinite cheap pilot. Use the renewed sites to develop two or three quantified case studies, but report the sample and conditions honestly.

The wholesaler's current proposal should be rejected as written. A 25% revenue share, two-year exclusivity, and custom integration combine three large concessions before the wholesaler has demonstrated sourced, activated, or retained customers. Access to 600 pharmacies is not the same as demand, and exclusivity could prevent direct learning or alternative partnerships.

Counter with a bounded channel experiment:

- Nonexclusive access to a named cohort of 30–50 pharmacies for 90–120 days.
- A referral or reseller fee of 10%–15% of first-year collected revenue, rising only if the wholesaler performs sales, onboarding, or support work that the startup would otherwise fund.
- No blanket exclusivity. If exclusivity is unavoidable, limit it to a defined region or named accounts, make it performance-based, and terminate it automatically unless minimum activated locations and revenue are reached each quarter.
- A paid or jointly funded integration with a written scope, reusable API boundaries, acceptance criteria, maintenance ownership, and no transfer of product roadmap control.
- Startup ownership of customer contracts, product usage data, pricing authority, customer access, and the right to contact pharmacies for implementation and research.

Suggested channel gates are at least 20 qualified owner conversations, 10 production conversions, implementation time no worse than direct accounts, and 12-month contribution economics no worse than the direct motion after revenue share and integration cost. If the wholesaler will not accept a test with measurable minimums, walk away and use the next quarter to strengthen direct evidence.

## Courier dispatch: partner now; investigate before building

Do not approve the $600,000 in-house build during this 90-day period. The simplest break-even comparison is $600,000 divided by $0.40, or 1.5 million deliveries. That is the number of partner fees required merely to equal the proposed build cost; it excludes ongoing engineering, courier integrations, monitoring, incident response, compliance, support, cloud expense, and the cost of replacing an existing SLA. It also ignores the six-month delay and the revenue-generating work the CTO's team would defer.

Dispatch should be built only if it is both economically justified at committed—not hypothetical—volume and strategically differentiating. The potential wholesaler population must not be counted until pharmacies are contracted and active.

For the next 90 days:

- Keep the current SLA-backed API and negotiate volume tiers, service credits, data portability, termination assistance, and a cap on price increases.
- Put a thin internal abstraction around the partner interface so another provider can be tested without rewriting the pharmacy product. Do not turn that abstraction into a hidden dispatch rebuild.
- Benchmark at least one alternative provider on coverage, reliability, courier network support, latency, security, total cost, and SLA.
- Have the CTO produce a scoped dispatch requirements document and a five-year build-versus-partner model. Include build cost, ongoing headcount, 24/7 operations, integration maintenance, insurance/compliance exposure, expected delivery volume by probability-weighted sales scenario, and the value of features the partner cannot provide.

At day 90, authorize a build only if signed or highly committed volume puts full lifecycle cost below partner cost within an agreed payback window, dispatch capability materially improves win rate or retention, and the company can meet or exceed the partner's SLA without endangering the core route-optimization roadmap. Otherwise renew or renegotiate the partnership and revisit at a predetermined volume threshold.

## Operating calendar and decision gates

**Days 1–15: establish the facts.** Instrument customer-level revenue and costs; interview all 18 owners and technician leads; analyze renewers versus nonrenewers; quantify the economic value of the on-time improvement; freeze any exclusive channel or dispatch-build commitment. Establish one accountable owner for pricing, one for direct/channel sales, and one for partner economics.

**Days 16–30: design controlled tests.** Select the initial customer profile; create the three pricing presentations and a standard value calculator; prepare a production agreement and renewal transition; give the wholesaler the bounded counterproposal; request partner volume pricing; document dispatch requirements and alternatives.

**Days 31–60: obtain behavioral evidence.** Issue real quotes to a small direct pipeline across low-, medium-, and high-volume sites; close several customers without bespoke pricing; publish owner-facing outcome reports for renewed sites; begin the wholesaler cohort only if the counterproposal is accepted; benchmark the alternate dispatch provider. Review contribution margin weekly.

**Days 61–90: decide and codify.** Choose the pricing structure using realized margin and quote outcomes, not interview enthusiasm. Write a clear discount policy and migration plan. Compare direct and channel acquisition cost, implementation burden, access to the buyer, and expected retained gross profit. Complete the full dispatch model and partner negotiation. At the final review, make three explicit decisions: adopt the scalable production price, continue direct sales with either a performance-gated channel pilot or no wholesaler deal, and partner for dispatch unless the predeclared build gates have actually been met.

The founders should review a single weekly dashboard: qualified owner conversations, quote conversion, activation, technician usage, on-time and failed-delivery change, support and compute per delivery, API cost per delivery, contribution margin by account and volume band, renewals, and channel-sourced activated locations. Ninety days is enough to correct the model and test the channel; it is not enough evidence to trade away distribution freedom or commit the engineering organization to owning a new operational business.
