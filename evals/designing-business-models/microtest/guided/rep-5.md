# 90-day business-model decision plan

**Primary owner:** designing-business-models
**Handoffs:** 1. learning-from-users for renewal and willingness-to-pay evidence; 2. shipping-and-iterating-products for packages, billing, and rollout; 3. acquiring-and-growing-users for direct and wholesaler cohorts; 4. engineering-for-leverage for cost instrumentation and partner interfaces; 5. competing-and-positioning for partner dependence and claims; 6. communicating-clearly for owner, technician, courier, and patient messaging; 7. raising-and-governing-capital only if a later build clears the capability and return gates; 8. managing-runway-and-survival first if a current cash forecast shows that a $600,000 commitment or the 90-day tests would make time-to-zero binding.

## Decision now

For the next 90 days, keep selling directly, replace the flat price with a tested base-plus-volume offer for new customers, and keep the twelve renewing pilot customers on $500 while collecting comparable usage and cost data. Counter the wholesaler with a non-exclusive, limited cohort rather than accepting two-year exclusivity. Keep the courier API and SLA; do not authorize the proposed $600,000 dispatch build. Preserve the option to build by instrumenting partner performance, defining a vendor-neutral interface, and qualifying an alternate.

This is justified by the evidence available today:

- The paid-pilot renewal rate is 12/18, or 66.7%; nonrenewal is 33.3%. That is promising payment evidence, but not yet stable retention because renewal duration, usage depth, later churn, and expansion are unknown.
- Renewed sites improved on-time delivery from 86% to 95%, a nine-percentage-point gain. Late deliveries fell from 14% to 5%, about 64% relative. This is an observed association in the renewing subset, not a causal promise for all pharmacies; seasonality, route mix, courier performance, staffing, and selection of successful sites may explain part of it.
- Sites above 2,500 deliveries create 60% of compute and support cost. A single flat price therefore cross-subsidizes the expensive segment and hides whether growth improves or worsens gross margin.
- “Access to 600 pharmacies” is not paid deployment. At the current $500 price, a 25% share leaves $375 per site per month before compute, support, implementation, and any courier expense. Exclusivity would surrender the direct channel and bargaining leverage before the wholesaler has demonstrated activation or retention.
- The API is variable-cost and covered by an SLA; the build is a six-month, fixed-cost product expansion. The theoretical break-even is 1.5 million deliveries ($600,000 / $0.40) before counting internal variable cost, maintenance, on-call coverage, compliance, opportunity cost, or the API's SLA value. Current scale does not establish that case.

## Business-model record

| Field | Pharmacies at or below 2,500 monthly deliveries | Pharmacies above 2,500 monthly deliveries |
|---|---|---|
| Product and value event | Capital-light route-optimization software; value occurs when a paid, deployed site completes routes more reliably without unsafe workflow changes | Same product, but greater workload and support exposure; test whether volume is repeatable product value or service-heavy scaffolding |
| Actors | Patient benefits; pharmacy technician uses; owner buys and pays; outside courier executes; startup supports; direct sales or wholesaler introduces | Same actors; identify who controls courier selection, dispatch data, and integration approval at each account |
| Alternative and budget | Manual route planning, courier tooling, or status quo; exact delivery-operations budget and avoided late-delivery cost are unknown | Same alternatives, with potentially higher avoided labor and failed-delivery cost; verify rather than infer willingness to pay from volume |
| Actual evidence | Eighteen paid pilots at $500/month across ten weeks; segment split is unknown | High-volume sites cause 60% of compute/support cost; count of such sites and their renewal rate are unknown |
| Retention and effects | Overall first renewal is 12/18; later retention, deployment depth, expansion, and segment-specific outcomes are unknown | Same unknowns; report the 86% to 95% result only for renewed sites until matched results exist |
| Proposed new-customer offer | **Core:** $500/month including 2,500 optimized deliveries, month-to-month after a 60-day initial paid term | **Volume:** $500/month plus $0.20 per optimized delivery above 2,500; quote a capped first-60-day exposure of $1,250/month while measuring cost and value |
| Courier expense | If the startup incurs the $0.40 API charge, show it separately; do not bury it in the platform allowance | Same: customer contracts directly where practical, otherwise test a transparent $0.50-$0.60 per dispatched-delivery line item and reject any package below the measured cost-to-serve floor |
| Revenue and sales | Monthly advance billing; owner signature; technician workflow check; target no more than two sales calls and four implementation hours per site | Monthly advance billing; owner signature; technical discovery; preapprove no more than eight implementation hours without a paid services change order |
| Economic gate | At least 75% gross margin after API, compute, support, implementation amortized over six months, refunds, and channel share | At least 65% gross margin initially and a path to 70%; support below two hours/site/month after onboarding |
| Interpretation | Paid activation plus day-60 continuation supports keeping the package; objections without a purchase do not | Acceptance of a capped trial but rejection at uncapped usage means revise the cap/metric, not claim high-volume willingness to pay |

Before using these packages broadly, finance must reconstruct site-level contribution margin from invoices and logs. Track optimized and dispatched deliveries separately, because the $0.40 API fee may apply to a different event than route optimization. Allocate cloud usage, support time, implementation time, refunds, and channel share to each site. Do not call a tier profitable until those costs are included.

Because prescription delivery can affect patients, the COO must confirm current applicable pharmacy, privacy, courier, and data-processing requirements with qualified counsel before widening exposure. Require permissioned data access, least-privilege roles, audit logs, human override, rollback, incident response, and an accountable escalation path. Track missed/late delivery, patient complaint, privacy, and safety incidents by site. Do not market “95% on time” as a guaranteed or general result.

## The bounded tests

### Pricing and direct sales

From days 16-60, the CEO will quote the same disclosed menu to twelve qualified new prospects: six at or below 2,500 monthly deliveries and six above it. Maximum test exposure is twelve accounts, $15,000 in capped monthly invoices, 72 implementation hours, and no annual commitment or automatic conversion. Finance records quote, owner acceptance, paid activation, actual volume, acquisition effort, deployment time, support, unit cost, and contribution margin. Product records technician weekly use and on-time delivery using an agreed baseline.

At day 60 and again at day 90:

- **Keep** the Core price if at least 4/6 small prospects pay, at least 3 are live by day 30, day-60 paid continuation is at least 75%, and cohort gross margin is at least 75%.
- **Segment** on volume if at least 3/6 high-volume prospects accept the overage, at least 2 are live, day-60 paid continuation is at least 75%, and gross margin is at least 65% with support below two hours/site/month.
- **Change** the value metric or price once if buyers consistently cannot predict optimized-delivery volume, or if at least four otherwise-qualified prospects reject specifically because of the metric while confirming budget and need. Test one alternative—three volume bands—rather than individual discounts.
- **Grandfather** the twelve renewals at $500 through day 90, then give 60 days' notice of any tier change. Do not retroactively bill usage.
- **Stop** the high-volume package if fewer than 2/6 pay, gross margin remains below 50%, a material safety/compliance condition is unresolved, or implementation exceeds eight hours/site without paid services. Preserve the smaller-site offer if it clears its own gates.

Confounders to record are prospect source, pharmacy volume, courier, baseline on-time rate, route density, staffing changes, seasonality, sales rep, discount, integration type, and whether the owner or technician initiated the sale. No unlogged discount counts as price acceptance.

### Wholesaler channel

By day 15, counter with a 90-day, non-exclusive proof: 30 named qualified introductions; the startup retains customer and product-usage data rights subject to customer permission; standard integration only; 15% of collected first-year subscription revenue for wholesaler-sourced accounts; no share on existing or independently sourced accounts. The wholesaler funds its custom work or pays a non-refundable integration fee based on a scoped estimate. No ranking, clinical, dispensing, or patient-control authority transfers to the wholesaler.

Accept a later 25% share only if the wholesaler delivers at least 20 paid activations in the proof, at least 80% remain paid at day 60, cohort gross margin after share is at least 70%, median implementation is under eight hours, and acquisition payback is under six months. Even then, offer at most segment- or territory-limited exclusivity with quarterly minimums, a data-portability right, SLA, termination for missed minimums, and a six-month exit—not blanket two-year exclusivity. If it insists on two years now, require a guaranteed minimum equal to at least 100 paid sites at the accepted package economics in year one; otherwise reject and continue direct sales.

Channel branches are precommitted: **pay** the agreed share only on collected revenue; **revise** targeting or enablement if introductions are qualified but activation is below 20; **preserve direct** if activation or retention misses; **stop** the channel for misleading claims, unsafe conduct, unauthorized data use, margin below 60%, or refusal of attribution and exit terms.

### Courier dispatch boundary

The CTO gets no six-month build authorization during this period. Instead, cap boundary-test work at two engineer-weeks plus legal/procurement review. Instrument delivery volume, API charges, latency, uptime, support incidents, SLA credits, failure ownership, and customer requests for dispatch features. Document who owns customer and delivery data, export rights, interface standards, termination assistance, and the ability to switch. Put the current partner behind a vendor-neutral adapter and complete a paper and sandbox qualification of one alternate supplier; do not migrate live patient deliveries without assurance and rollback review.

At day 90, choose among these branches:

- **Partner** by default if the provider meets its SLA, material incidents are rare and repairable, customers do not pay specifically for proprietary dispatch, and contribution margins clear the package gates.
- **Repair** the contract or integration if failures are attributable to interface, observability, data rights, or service terms rather than missing internal capability.
- **Dual-source** if concentration risk is material and an alternate passes security, compliance, data-portability, and rollback checks at acceptable economics.
- **Integrate/build** only if all of the following are true: customers demonstrate paid demand for startup-owned dispatch; the partner repeatedly fails a required SLA or blocks necessary customer/data control; the startup can staff 24/7 ownership without derailing route optimization; current compliance and safety requirements are satisfied; and measured monthly avoided cost satisfies
  `deliveries × ($0.40 − internal variable cost) − internal monthly operations > $33,333`
  for three consecutive months. That is merely an 18-month recovery of the $600,000 fixed build cost; approve only after adding risk, delay, and opportunity cost and confirming the cash plan.
- **Stop** the dispatch expansion if it is primarily an unvalidated feature request, if safety or permission gates fail, or if projected payback exceeds 18 months. Keep the replaceable API interface as the preserved option.

## 90-day operating cadence and final decision

**Days 1-15:** CEO owns all six nonrenewal interviews and six renewal interviews, split across owner and technician; finance builds site contribution margins; product validates delivery-event definitions and matched outcome baselines; CTO measures the partner boundary; COO closes current legal, security, incident, and human-review gaps. Freeze bespoke discounts, wholesaler exclusivity, custom integration, and dispatch hiring.

**Days 16-45:** launch the twelve-account pricing test; place at least ten of the thirty wholesaler introductions into owner qualification; implement usage/cost dashboards and the vendor adapter; review patient-effect and incident metrics weekly.

**Days 46-75:** collect paid activation and continuation evidence; compare direct and channel cohorts without mixing them; negotiate only from the precommitted channel thresholds; qualify the alternate API; publish truthful, cohort-labeled outcome language for sales.

**Days 76-90:** CEO, finance lead, CTO, and COO select each branch separately. Pricing does not pass because the channel grows, and the channel does not pass because the product has effects. Keep Core, segment Volume, preserve direct, and remain partnered only where their own payment, retention, margin, safety, and dependency gates clear. Record rejected alternatives—one flat price, immediate exclusivity, and immediate dispatch build—and assign the next 90-day owners: growth for a passing channel, product for a passing package rollout, engineering for a passing dual-source plan, and learning for any failed or ambiguous evidence gate.
