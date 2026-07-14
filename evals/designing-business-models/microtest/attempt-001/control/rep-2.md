# 90-day decision plan

The founders should make three decisions now, subject to explicit 90-day gates:

1. Stop offering the $500 flat price to new customers. It is a pilot price, not a viable commercial price for high-volume sites.
2. Do not accept the wholesaler's proposal as written. Counter with a nonexclusive, time-boxed channel test; make any later exclusivity contingent on minimum customer and revenue commitments.
3. Continue partnering for dispatch. Do not authorize the $600,000 build during these 90 days. First establish contracted volume, negotiate the partner's unit price, and calculate the fully loaded cost and reliability burden of owning dispatch.

## What the evidence says

The pilot produced a useful but incomplete signal. Twelve of eighteen sites renewed, a 67% logo renewal rate, and renewed sites improved on-time delivery by nine percentage points. At 2,500 deliveries per month, that improvement corresponds to 225 additional on-time deliveries per month if volume and route mix are comparable. That is a credible value hypothesis, but it is not yet proof that the product caused the improvement or that owners will pay the price needed for healthy margins.

The stakeholder roles also call for a two-part sales story. Pharmacy technicians need a faster, lower-exception workflow; owners need an economic case and predictable bill; couriers need reliable integration and clear handoffs. Patients benefit from reliability but are not the buyer. Sales should therefore demonstrate the technician workflow, then give the owner an ROI case based on fewer late-delivery incidents, technician time saved, fewer support calls or redeliveries, and any retention effect the pharmacy can substantiate.

The pricing problem is urgent. If the startup bears the stated $0.40 partner fee, 2,500 deliveries cost at least $1,000 in API fees before compute and support, twice the current $500 revenue. Week-one diligence must confirm who actually bears that charge, but the company should assume the adverse case until proven otherwise.

## Days 1-15: establish account economics and the ideal customer

Put every pilot account into a one-page cohort table containing monthly deliveries, revenue, partner fees, compute, support hours, implementation effort, technician adoption, on-time performance before and after, renewal outcome, and renewal or churn reason. Separate the twelve renewals from the six nonrenewals, and separate sites below and above 2,500 deliveries. The purpose is to learn whether renewal and measurable value rise fast enough with volume to offset the cost concentration.

Conduct structured interviews with all six nonrenewing owners, six renewing owners, and eight to ten technicians. Owners should be asked about the operational and financial cost of late deliveries and the actual approval threshold for software; technicians should be asked about time, exceptions, workarounds, and courier handoffs. Do not ask whether a hypothetical price "sounds reasonable." Show a concrete package and ask for a renewal, letter of intent, or paid start.

The founders should define the initial ideal-customer profile from observed behavior, not just size. A likely hypothesis is an independent pharmacy with meaningful same-day volume, an owner who feels the cost of delivery exceptions, a technician champion, and a compatible courier workflow. High volume is attractive only after pricing makes it contribution-positive.

At the end of day 15, calculate contribution margin per account as:

`revenue - partner/API cost - compute - support labor - other delivery-variable cost`

Set a commercial target of at least 65% contribution margin after those costs, with no volume band allowed to be structurally loss-making. Also document the confidence interval and confounders behind the 86%-to-95% result so sales does not overstate causality.

## Days 16-30: put a commercial price in market

Use a two-part price rather than a flat tier with a sharp volume cliff. A reasonable opening offer to test is a $750 monthly platform fee plus $1.25 per routed delivery, with a $1,250 monthly minimum. Offer a lower unit price only in exchange for an annual committed volume. The precise figures are hypotheses, but they are economically grounded: at 2,500 deliveries the price is $3,875, against $1,000 of known partner cost, leaving room for compute, support, and margin. The price floor for any account should be calculated from its fully loaded variable cost; for a 65% margin target, price cannot be lower than cost divided by 0.35.

Test a second structure with the same expected economics, such as committed monthly volume bands with overage, because owners may value budget certainty. Do not disguise high-volume cost with "unlimited" usage. Keep courier charges or other true pass-through costs visible, and do not allow channel revenue share to apply to taxes, refunds, or pass-through expenses.

Honor the existing twelve customers' agreed pilot or current-term price. Tell them by day 30 how the commercial plan will change at their next renewal, offer a time-limited migration credit, and give them a predictable usage estimate. Do not abruptly reprice them midterm. For new prospects, stop using $500 as the reference price. A paid proof period should use the intended commercial unit economics, perhaps with an implementation credit that is earned when the customer signs an annual agreement.

Present written offers to at least eight qualified owners across two volume bands. Advance a price only if at least three accept a paid start or place a deposit, the expected account-level margin reaches the target, and the loss reasons do not reveal that the product's demonstrable value is below the required price. If acceptance is weak, first distinguish a value/ICP problem from a packaging problem; do not automatically discount below the cost floor.

## Days 16-60: run direct sales and channel tests in parallel

Keep founder-led direct sales active as the control. Use the renewed cohort to create a concise case study with permission, showing baseline, route volume, workflow change, on-time result, and caveats. The motion should be technician validation followed quickly by an owner business case, rather than a user-only product demonstration that later stalls in procurement.

Counter the wholesaler with a 60-day, nonexclusive pilot covering a named set of 20 to 30 pharmacies. Require warm introductions, agreed joint messaging, access to the actual owner decision-maker, and weekly pipeline reporting. Track introductions, qualified opportunities, demonstrations, paid starts, time to close, implementation burden, support load, realized revenue, and contribution margin. Compare these with the direct funnel.

The long-form channel agreement should be considered only after the test, and should include all of the following:

- Revenue share only on collected software revenue from net-new accounts sourced by the wholesaler, not existing accounts, direct accounts, taxes, refunds, or courier/API pass-throughs.
- A defined attribution window and an end to revenue share after a stated period, rather than an indefinite claim on the customer.
- A separately priced and prepaid custom integration, or a guaranteed net contribution at least sufficient to recover its fully loaded cost and ongoing maintenance.
- Customer-level usage and outcome data for the startup, direct support access, data portability, and clear ownership of the customer relationship.
- Exclusivity narrowly limited by geography and channel, earned quarterly through minimum activated-customer and net-revenue quotas, and automatically lapsing when a quota is missed. It should not prevent direct sales or other channels outside that scope.
- Termination rights for poor lead quality, delayed integration, nonpayment, or material SLA failure.

A 25% share can be acceptable when it replaces equivalent acquisition cost and produces real volume, but "access to 600 pharmacies" is not consideration for two years of exclusivity. To preserve the same net revenue after a 25% share, a channel price must be 1 / 0.75, or 1.33 times, the desired direct net price. Either gross up the channel price, obtain a lower share, or prove that the channel's lower sales cost and faster conversion compensate for the margin reduction. Do not sign exclusivity without a minimum guarantee that covers the custom integration and the opportunity cost of foreclosed channels.

By day 60, the channel should have produced at least 20 genuine introductions, eight qualified owner opportunities, and three paid starts to remain under consideration. These are test gates, not proof of scale. Any exclusive contract needs substantially stronger annual minimums based on the observed funnel, not on the wholesaler's addressable list.

## Days 1-75: make-versus-partner diligence

The simple build break-even is $600,000 / $0.40 = 1.5 million deliveries. That is only the one-time engineering comparison. It excludes six months of foregone roadmap work, internal hosting and variable costs, ongoing engineering, monitoring, courier integrations, 24/7 incident response, compliance and security work, and the cost of matching the partner's SLA. Those costs raise the actual break-even materially.

The CTO should spend no more than a small, time-boxed discovery effort during the 90 days. Produce a requirements and total-cost model, identify which dispatch capabilities are genuinely differentiating, and estimate internal cost per delivery and annual maintenance. In parallel, ask the current partner for volume discounts at committed thresholds, better data portability, incident remedies, and protection against sudden price changes. Benchmark at least one alternative provider and design a credible migration path so partnership does not become permanent dependency.

Use actual account volume in the model. For illustration, if all twelve renewed sites each sent 2,500 deliveries per month, total volume would be 30,000 and the avoided API spend would be $12,000 per month; the simple build payback would be 50 months before ongoing internal costs. The actual volume may differ, but this shows why an uncommitted 600-account channel promise should not be used to justify the build.

Authorize an in-house build only when contracted, not merely forecast, delivery volume makes the risk-adjusted payback acceptable within 18 to 24 months after all ongoing costs; the company can staff and operate an SLA at least as good as the partner's; dispatch is strategically differentiating rather than commodity plumbing; and the project no longer crowds out higher-value product and sales work. Until all four conditions hold, partner and negotiate.

## Days 61-90: decide and roll out

At day 75, review the direct and channel cohorts using one scorecard: paid conversion, sales cycle, acquisition effort, realized revenue per delivery, contribution margin, support hours, technician adoption, on-time change, and expected renewal. Use collected revenue and contracted commitments rather than verbal enthusiasm.

By day 90, the founders should:

- Publish the commercial price and margin floor, with a migration schedule for existing customers and no unprofitable unlimited tier.
- Narrow the sales motion to the ICP that shows both owner willingness to pay and repeatable technician adoption.
- Either reject the wholesaler, extend a nonexclusive test, or sign only the quota-backed version. The original 25%-share, two-year-exclusive, custom-integration offer should be rejected.
- Renew or renegotiate the dispatch partner and record the volume thresholds that would trigger another make-versus-partner review. The $600,000 build remains unfunded unless the stated gates are already met by signed business.

The governing principle is to buy learning without buying lock-in. In 90 days, the company should know whether the nine-point service improvement converts into owner willingness to pay, whether high-volume customers can be profitable, whether the wholesaler produces customers rather than introductions, and whether dispatch volume is real enough to justify owning a reliability-critical system.
