Primary owner: Designing business models

Handoffs, in order:

1. `managing-runway-and-survival`, only if the Day 5 cash review shows the company is default-dead or the proposed commitments would cross its cash switch date.
2. `learning-from-users` to separate value, churn, workflow, and willingness-to-pay evidence by pharmacy size and actor.
3. `engineering-for-leverage` to meter cost and performance by site and put courier providers behind a replaceable interface.
4. `acquiring-and-growing-users` to execute the direct and wholesaler channel tests after the offers are fixed.
5. `shipping-and-iterating-products` to implement packages, billing, deployment, support limits, and safe rollout.
6. `competing-and-positioning` to assess dependence on the wholesaler and courier platforms.
7. `raising-and-governing-capital` and `building-and-evolving-organizations` only if a later build decision passes its economic gate and creates a financing or staffing need.
8. `communicating-clearly` to turn the settled economics into owner-facing sales claims without overstating the pilot evidence.

## Decision for the next 90 days

- Change pricing for new sales from one flat price to a platform-plus-delivery metric; test both a metered bill and a predictable committed-volume version of the same economics. Grandfather the 12 renewed sites only through the test period, with earlier renegotiation for any materially loss-making account.
- Continue founder-led direct sales as the control channel. Reject the wholesaler's 25%-of-all-revenue, two-year-exclusive offer as written. Counter with a non-exclusive, performance-gated 90-day pilot in which the wholesaler funds a tightly scoped integration.
- Continue using the courier API. Do not authorize the $600,000 build. Instrument supplier performance, negotiate the SLA and volume pricing, and qualify an alternate provider. Reconsider building only after contracted volume, three-year total cost, control risk, compliance capability, and runway all cross precommitted thresholds.

## Business-model record

### Product and stage

| Field | Current record and 90-day requirement |
|---|---|
| Product type | Capital-light enterprise/integration software embedded in a regulated, potentially high-harm prescription-delivery workflow. It also depends on a transaction-priced dispatch supplier. |
| State | Eighteen paid deployments completed a ten-week pilot at $500 per month; 12 renewed and 6 did not, a 66.7% aggregate renewal rate. This is real payment and deployment evidence, but not evidence that $500 is the optimal price. No expansion evidence is supplied. |
| Effects | Renewed sites improved on-time delivery from 86% to 95%. Treat this as an observed association at the selected renewed sites, not a causal claim for all pharmacies: the six non-renewers, mix of delivery volumes, operational changes, seasonality, and courier performance could confound it. |
| Binding constraint | Unit economics and capture are unresolved. Sites above 2,500 monthly deliveries generate 60% of compute and support cost yet pay the same price, while the courier API alone costs $0.40 per delivery. Channel access and the dispatch boundary should not be scaled until this is fixed. |
| Evidence latency | Price acceptance can be observed at signed order and first payment; deployment within 21 days and 60-day paid retention fit inside the plan. A two-year exclusive deal and a six-month internal build have much longer evidence latency. |
| Reversibility and error cost | A new-customer price test and a 90-day non-exclusive channel pilot are reversible. Broad exclusivity, a bespoke code fork, unsafe delivery interruption, and a $600,000 build are high-cost or difficult to reverse. |
| Facts to verify by Day 15 | Delivery distribution and cost by site; renewal by size; compute, implementation, support hours, and incident cost by site; courier invoices and SLA history; direct sales hours and cycle; reasons for all six non-renewals; owner budget and alternatives; security/procurement requirements; current cash runway; wholesaler lead commitment and integration scope. |

Before expanding either channel, counsel and the accountable operations leader must verify current privacy and pharmacy-delivery requirements, permissions and data sharing, patient consent where applicable, chain of custody, restricted-medication handling, driver controls, proof of delivery, human override, monitoring, rollback, incident response, and responsibility among pharmacy, software company, wholesaler, and courier. A material safety, privacy, or legal failure pauses rollout regardless of revenue.

### Actors, segments, and evidence

| Row | Beneficiary, user, buyer, payer, and channel | Value event, alternative, and current evidence | Economics and open questions |
|---|---|---|---|
| Pharmacies at or below 2,500 monthly deliveries | Patients and the pharmacy benefit; technicians use routing; owners buy and the pharmacy pays. Direct sales and a bounded wholesaler referral are candidate channels. | Value occurs when a promised delivery arrives on time with less technician intervention. Alternatives include manual routing, courier-provided tools, or another routing product. Aggregate paid-pilot and renewal evidence exists, but this segment's use, deployment, renewal, retention, support, and expansion must be backfilled separately. | Measure delivery count, API cost, compute, support, implementation, gross margin, sales effort, switching concerns, and owner budget. Do not assume low-volume sites are cheap until support data confirms it. |
| Pharmacies above 2,500 monthly deliveries | Same actors, but likely more operational exposure and a larger potential benefit and budget. | Their segment-specific renewal and on-time effect are unknown. They generate 60% of compute and support cost; the number of sites responsible is also unknown. | At 2,500 deliveries, the courier API alone costs $1,000 per month, twice the current flat price, before compute or support. Continuing the $500 offer for this segment is not viable unless the pharmacy pays the dispatch API separately or metering reveals a different cost allocation. |
| Pharmacy technicians | User and workflow expert, but not the presumed payer. | Technician time saved, override rate, routing time, and exception-handling burden are value evidence. Satisfaction alone is not purchase evidence. | Interview separately from owners; a technician request should not be treated as owner willingness to pay. |
| Owners | Buyer and payer on current evidence. | A signed order, first payment, paid deployment, renewal, and expansion are the acceptance sequence. Verbal interest is not acceptance. | Record budget source, alternative spend, procurement, discount request, and who can terminate the purchase. |
| Patients | End beneficiary, not a payer in the current model. | On-time, accurate, private, safe delivery and complaint/incident rates are accountable effects. | Do not introduce patient fees or sell patient data in this test. Preserve human recourse and pharmacy accountability. |
| Outside couriers | Delivery performer and supplier; not the buyer. | They execute most routes, so courier operations can confound product effects. | Attribute late deliveries among routing recommendation, API availability, dispatcher action, driver execution, pharmacy readiness, and patient availability. |
| Regional wholesaler | Proposed channel and integration counterparty, not automatically the customer or payer. | Access to 600 pharmacies is not distribution evidence. Qualified owner introductions, paid deployments, retention, and collected revenue are. | Measure share, integration cost, channel sales effort, concentration, customer ownership, data rights, switching, and exclusivity opportunity cost. |

### Unit economics and price package

For every pharmacy and every channel, calculate monthly contribution before allocating company overhead:

`collected revenue - ($0.40 × completed deliveries) - metered compute - loaded support - implementation amortization - channel share - refunds/service credits`

Gross margin is that contribution divided by collected revenue. Sales efficiency must include founder or salesperson hours at a loaded rate, travel, onboarding effort, integration effort, and revenue share; it must not treat the wholesaler's introductions as free acquisition.

For new customers, test one economic price expressed in two purchasing forms:

- **Metered:** $500 per month platform fee plus $1.00 per completed delivery, standard onboarding and support included within documented limits.
- **Committed volume:** a monthly minimum based on forecast deliveries at the same expected annual price, with a 10% volume corridor and $1.00 per-delivery overage. This tests budget predictability, not a hidden discount.
- **Scale floor:** above 2,500 forecast monthly deliveries, do not quote below $3,000 per month or the instrumented cost floor required for 65% projected gross margin, whichever is higher. Priority support, custom reporting, and integrations are separately priced.

The $1.00 usage price is a test, not a claim about final willingness to pay. Its purpose is to put the $0.40 supplier cost, variable compute, and value exposure on the same metric. If actual metered costs show that 65% margin requires a higher price, the sales team may not discount below the cost floor to manufacture acceptance.

The 12 renewed pharmacies receive a shadow invoice showing deliveries and full unit economics by Day 30. Their $500 price is preserved through Day 90 while the company seeks a signed transition effective at the next renewal. If any account is projected to lose more than $1,000 per month, the CEO must renegotiate it within 30 days or contractually limit company-funded usage without interrupting patient care; silence is not a reason to keep subsidizing it.

### Pricing test and precommitted interpretations

The CEO owns the test; the finance/operations lead owns cost certification; product/customer success owns deployment and effects. Between Days 31 and 60, present 12 qualified owner-level proposals, stratified as six at or below 2,500 deliveries and six above it. Alternate metered and committed-volume forms within each segment. Cap aggregate test exposure at 12 deployments, a 10% discount, and standard integration only. A positive result is a signed order, first payment, and deployment scheduled within 21 days—not a letter of intent.

By Day 90:

- **Keep:** keep the price form for a segment if at least 3 of its 6 qualified owners pay, no accepted deal exceeds a 10% discount, each accepted deal projects at least 65% gross margin, at least 80% deploy within 21 days, and 60-day paid retention among those old enough to observe is at least 75%.
- **Change:** if owners accept the economics but consistently reject bill variability, use the committed-volume form; if they understand the package but the cost floor misses 65% margin, raise price or reduce included support rather than scale it.
- **Segment:** if only one volume segment meets the gates, sell that segment and redesign or decline the other. Do not average good small-site economics with bad large-site economics.
- **Grandfather:** if at least 8 of the 12 renewed accounts sign a dated transition that meets the margin floor, implement it and give the remainder a defined wind-down or separately funded package. A temporary grandfather is an option-preserving bridge, not a permanent plan.
- **Stop:** if fewer than 3 of 12 qualified owners pay after one package revision, stop scaling paid acquisition under this offer and return to owner/technician evidence. If no legal, safe, positive-contribution package exists, stop serving the affected workflow or segment.

Price decisions also require an effects gate: on-time performance at repriced or newly deployed sites must reach at least 93% or improve at least 4 percentage points from that site's measured baseline by week six, without a material safety/privacy incident. This prevents apparent margin improvement through degraded service.

## Sales and channel plan

### Direct control motion

From Days 16 through 75, the CEO runs a founder-led control motion aimed at 40 independent pharmacies split evenly by volume segment. Targets are 15 owner-qualified meetings, 12 price proposals, 6 paid starts, and measured hours from first contact through deployment. No free pilot counts as a start. Customer success records technician use, owner acceptance, deployment, and early retention separately.

### Wholesaler counteroffer

Do not sign the proposed deal. Offer instead:

- a 90-day, non-exclusive pilot with named success and termination dates;
- at least 30 warm owner introductions, with a target of 15 qualified owner meetings and 8 paid deployments;
- a 15% share of collected platform revenue for partner-sourced new accounts for 12 months, excluding taxes, refunds, existing accounts, custom work, and the portion of usage revenue needed to pay third-party delivery/API cost;
- startup ownership of pricing, pharmacy contracts, product telemetry, routing logic, support standards, and portable customer data; the wholesaler receives only the minimum data needed for its role;
- a generalized integration capped at four engineer-weeks, with no wholesaler-specific product fork; before work starts, the wholesaler pays a fixed fee equal to 120% of estimated fully loaded build cost; and
- no minimum-price discount, most-favored-nation clause, broad data right, or restriction on direct sales and other channels.

If the wholesaler insists on 25%, it applies only to eligible collected platform revenue and only if pricing still produces at least 65% gross margin after the share and the wholesaler guarantees the paid-site threshold. If it insists on two-year exclusivity, decline. Limited regional exclusivity can be reconsidered after six months only if the wholesaler has produced at least 50 paid, list-price sites, 60-day paid retention is at least 75%, channel gross margin is at least 65%, the agreement is reviewable quarterly, and missed minimums terminate exclusivity automatically.

At Day 90, expand the wholesaler path only if it has delivered at least 8 paid deployments, at least 80% deployed within 21 days, projected gross margin after share and support is at least 65%, no material compliance incident occurred, and company sales hours per paid deployment are at most half the direct control. If economics work but introductions are below target, revise the lead commitment without exclusivity. If the wholesaler will not fund the integration, permit portable customer contracts, or meet the gates, stop the pilot and preserve direct sales. Access to 600 names by itself earns neither exclusivity nor a share.

## Make-or-partner record

| Boundary | Ownership and dependency record | Selected 90-day branch and switching path |
|---|---|---|
| Pharmacy/customer | The startup must own the pharmacy contract, price, product relationship, routing telemetry, data portability, and service truth. Pharmacies retain their patient relationship and accountable clinical/operational decisions. | Preserve direct contracting under both channels. Do not let the wholesaler become the only route to customers or data. |
| Wholesaler integration | The wholesaler may own its source system and lead relationship. A custom fork would create coordination, switching, and roadmap cost. | Build only a paid, documented, generalized adapter behind a stable interface. Retain IP and an off-ramp. Stop if the integration cannot stay within four engineer-weeks. |
| Courier dispatch | The startup owns route optimization, provider-selection logic, observability, and failure attribution. The courier partner currently owns dispatch execution and supplies an SLA. Its $0.40 transaction price is variable and currently avoids a large fixed commitment. | Partner now, negotiate, and dual-source. Put the current API behind an adapter, preserve data export, test an alternate provider, and make pharmacy operations able to fall back safely. |

The proposed $600,000 build must not be justified by calling dispatch "core." At $0.40 per delivery, saving the entire external fee would require 1.5 million deliveries merely to recover $600,000, before internal infrastructure, maintenance, 24/7 response, insurance, compliance, support, or the cost of delayed roadmap work. A 24-month payback needs at least 62,500 deliveries per month even under that impossible zero-operating-cost assumption; the real threshold is higher.

During Days 1–60, the CTO must instrument API availability and latency, cost per delivery, SLA credits, dispatch failures, manual interventions, engineering/support hours, and the portion of late deliveries attributable to the routing product, partner API, courier operations, pharmacy readiness, and patient availability. By Day 45, request tiered volume pricing and stronger service terms from the current partner. By Day 75, complete a paper and sandbox qualification of at least one alternate provider, including data portability, security, operational fallback, and a priced migration estimate.

Use these Day 90 boundary branches:

- **Partner:** continue the current provider if it meets the contracted SLA, projected gross margin passes the pricing gate, and no must-have customer requirement is blocked.
- **Repair:** if failures come from the startup's adapter, observability, or routing logic, fix that interface rather than misclassifying a supplier problem as a reason to build dispatch.
- **Dual-source:** move bounded traffic to the alternate if the incumbent has two material uncured SLA failures in 60 days, affects more than 1% of deliveries through attributable failures, or will not provide acceptable portability and incident terms.
- **Integrate/build:** authorize discovery—not the full build—only if contracted volume produces a payback under 24 months and a three-year total-cost model remains at least 20% cheaper than the best qualified partner after adding internal engineering, infrastructure, operations, compliance, insurance, support, and a 25% cost overrun. It must also solve a documented control or customer requirement that two qualified suppliers cannot meet.
- **Stop:** do not build, or stop offering company-mediated dispatch, if the company cannot establish lawful operation, human override, monitoring, rollback, incident response, and accountable ownership.

The capital and capability gate is separate from the economic gate: after reserving $750,000 for the stated build plus 25% overrun, the company must retain at least 18 months of runway, fund an accountable 24/7 operational owner, and avoid delaying the validated pricing and sales roadmap. If any gate fails, remain partnered. Customer funding or supplier competition preserves the option without committing scarce capital now.

## 90-day operating calendar

| Date | Actions, owner, cost/exposure, and output |
|---|---|
| Days 1–15 | CEO/finance: certify runway and the site-level contribution ledger. CTO: add cost, delivery, SLA, and attribution telemetry. Product/customer success: interview all 6 non-renewers, at least 6 renewers, technicians, and courier operators; separate price, workflow, outcome, implementation, and support reasons. Counsel/operations: complete the regulated-workflow gate. Freeze the internal build and wholesaler exclusivity. |
| Days 16–30 | CEO and finance: finalize the two price forms and cost floor. Customer success: issue shadow invoices and transition proposals to the 12 renewed sites. CEO: begin the 40-account direct control and deliver the channel counteroffer. CTO: scope the generalized wholesaler adapter and current-provider SLA negotiation. |
| Days 31–60 | Sales: complete 12 qualified price proposals and accept only paid, margin-qualified deployments. Wholesaler: produce warm introductions under a non-exclusive pilot or receive no integration work. CTO: run supplier telemetry, negotiate volume tiers, and identify an alternate. Review Day 60 deployment, effect, margin, and compliance results; pause any unsafe path. |
| Days 61–90 | Customer success: observe activation and available 60-day retention. Finance: compare direct and wholesaler acquisition cost and site-level margin. CTO: finish alternate-provider qualification and three-year partner/build model. On Day 90, founders select the precommitted pricing, channel, and boundary branches and assign the next owner for each result. |

## Day 90 decision memo

| Decision | Selected branch now | Rejected alternative | Preserved option and switch condition | Next owner |
|---|---|---|---|---|
| Pricing | Change and segment: test platform plus completed-delivery pricing with a 65% margin floor. | Permanent $500 flat pricing for every volume level. | Grandfather only through the dated transition; keep, change, segment, or stop according to paid acceptance, retention, effects, and margin thresholds. | CEO and finance, then shipping for billing rollout. |
| Sales/channel | Run direct as control and a non-exclusive, paid-integration wholesaler pilot. | 25% of all revenue plus two-year exclusivity on promised access alone. | Revisit narrow, performance-terminable exclusivity only after 50 paid sites and all six-month gates. | CEO, then growth for the winning motion. |
| Dispatch boundary | Partner and prepare to dual-source. | Spending $600,000 now on a six-month internal build. | Begin build discovery only after contracted-volume payback, 20% three-year TCO advantage, unmet control need, regulatory capability, and runway gates all pass. | CTO for supplier/interface work; capital and organization owners only after a passed gate. |

Delay has asymmetric cost: every month of flat pricing can deepen losses at high-volume sites, so pricing instrumentation and transition start immediately. In contrast, delaying the internal dispatch build preserves $600,000, six months, supplier optionality, and management attention while the company obtains the volume and failure evidence needed to make that boundary decision responsibly.
