# 90-day decision plan

The company should use the next 90 days to prove a narrower business model: sell directly to pharmacies with enough delivery volume and operational pain to value the product, charge in proportion to volume and service burden, use the wholesaler only through a reversible pilot, and continue partnering for courier dispatch. The evidence is promising but not yet broad enough to justify exclusivity or a $600,000 build.

## Decisions to make now

1. **Keep the optimization product as the core.** A 67% paid-pilot renewal rate and a nine-point improvement in on-time delivery at renewed sites show real value, but the six non-renewals make the ideal customer profile and willingness to pay uncertain.
2. **Replace flat pricing for new customers.** The current $500 monthly price undercharges the sites that generate most of the cost. Do not abruptly reprice the twelve renewals; use them to test packaging and move them at a defined renewal date.
3. **Do not accept the wholesaler's current terms.** A 25% share may be acceptable as customer-acquisition cost if activation and retention are strong, but two-year exclusivity plus a custom integration transfers too much risk before the channel is proven.
4. **Do not build dispatch in-house now.** At $0.40 per delivery, $600,000 equals 1.5 million partner-processed deliveries before considering ongoing engineering, operations, uptime, compliance, or the value of the partner SLA. The startup should preserve six months of product capacity and capital unless dispatch is shown to be strategically differentiating and economically superior at demonstrated scale.

## Days 1-30: establish the facts and design tests

### Pricing and customer economics

- Interview the twelve renewed pharmacies and six that did not renew. Include the owner, who controls budget, and at least one technician, who experiences the workflow. Separate non-renewal causes into insufficient value, price, missing functionality, implementation friction, courier issues, and business closure or low delivery volume.
- Build a site-level contribution model using monthly deliveries, compute, support time, partner API charges, implementation effort, renewal status, and on-time improvement. Identify the delivery volume at which each account becomes unattractive under the current price.
- Define a simple three-part package for testing: a base platform fee, an included monthly delivery allowance, and a per-delivery overage. Keep features mostly consistent at first so the test measures willingness to pay and volume economics instead of confusion about feature gates. A reasonable test structure is:
  - Essential: $500 per month including up to 1,000 deliveries.
  - Growth: $900-$1,200 per month including up to 2,500 deliveries, with enhanced reporting and standard support.
  - Scale: starting around $1,500 per month above 2,500 deliveries, with a per-delivery overage or a contracted volume band and separately priced premium support.
- Treat those numbers as hypotheses, not a published final tariff. Test two price points within each relevant band. Track gross margin after compute, support, and the $0.40 partner fee, as well as sales acceptance.
- Give the twelve existing customers written price protection through the 90-day test. Ask them to choose among proposed packages in non-binding pricing interviews, then offer a migration incentive such as six months at a transitional rate in exchange for an annual commitment, reference call, or case study.

### Sales and channel

- Define the initial ideal customer profile around evidence rather than pharmacy count: independent or small regional pharmacies with meaningful same-day volume, an owner who can decide quickly, a technician champion, measurable lateness, and compatible courier operations. Use 1,000-3,000 monthly deliveries as the first segment to test, then tighten the threshold based on contribution margin and conversion.
- Turn the renewed-site result into a concise sales proof: baseline on-time rate, post-adoption rate, implementation time, and any measured reduction in technician workload, failed deliveries, or patient complaints. Obtain permission before naming customers or using patient-related metrics.
- Create a direct-sales funnel of 30-50 ICP accounts. The founder should run discovery and close the first cohort, because the company still needs learning more than sales headcount. Require owner participation before a proposal and technician participation before implementation.
- Counter the wholesaler with a 90-day, non-exclusive launch to 25-50 pharmacies. Offer the 25% share only on collected first-year revenue from customers the wholesaler sources, not on existing accounts, renewals forever, services, or pass-through usage charges. Require jointly defined lead commitments and access to customer-level funnel data.
- Scope the custom integration as a paid, reusable project with acceptance criteria. Prefer the wholesaler funding it; at minimum, credit part of the fee back only after agreed activated-account or revenue milestones. Reject broad exclusivity. If the wholesaler insists, limit it by geography, named segment, and channel, make it contingent on minimum activated customers or revenue each quarter, include termination rights, and keep direct sales and existing relationships outside it.

### Make-or-partner analysis

- Freeze the proposed dispatch build other than discovery. Assign a small technical and product team to document what the partner supplies: dispatch functions, reliability, support, security, courier coverage, exception handling, and SLA remedies.
- Measure actual API volume, incident frequency, latency, failed requests, engineering time spent on the integration, and cost per completed delivery. Ask the partner for volume discounts and improved SLA terms. Investigate one credible backup provider or a manual fallback to reduce concentration risk without recreating the whole service.
- Write explicit build triggers: sustained volume at which fully loaded internal cost is lower; customer evidence that proprietary dispatch materially raises win rate, retention, or price; repeated partner failures that breach the SLA; and sufficient cash and staffing to operate a mission-critical service continuously. Include ongoing headcount and infrastructure, not just the $600,000 initial build, in the comparison.

## Days 31-60: run controlled market tests

Enroll 8-12 new direct prospects across the proposed volume bands. Quote the new packages, record which options customers reject or negotiate, and avoid ad hoc discounts. Where a discount is necessary, exchange it for something valuable such as annual prepayment, a longer term, narrower support, or reference participation. Instrument onboarding so the company can measure time to first live route, technician adoption, on-time delivery, support hours, and gross margin by account.

In parallel, launch the wholesaler pilot only after signing the bounded terms. Use the same qualification, pricing, onboarding, and success criteria as direct sales so channel quality can be compared fairly. The wholesaler should not own the customer relationship or obscure usage data. Hold weekly funnel reviews covering leads introduced, qualified-owner meetings, pilots started, sites activated, and paid conversions.

For the dispatch decision, negotiate a partner price schedule at higher volumes and validate a failover procedure. Conduct five to eight customer interviews specifically about dispatch. Determine whether customers want the software company to dispatch couriers, or simply want reliable integrations and better route performance. No production build should begin during this phase.

## Days 61-90: decide from pre-agreed thresholds

Adopt the new pricing if at least two volume bands show repeatable acceptance and positive contribution margin after all variable support, compute, and partner costs. As a starting gate, target at least 70% gross margin at normal usage, with no high-volume account below 50% without a strategic and time-limited exception. Publish clear usage measurement and overage rules. Migrate existing customers at their next renewal with advance notice and transitional terms; do not surprise them mid-contract.

Scale direct sales toward the segment with the best combination of win rate, activation speed, retention signal, and contribution margin. Continue the wholesaler pilot only if it produces qualified opportunities and activated paid accounts at an acquisition cost and payback competitive with direct sales. A practical 90-day channel gate is at least 25 qualified owner-level introductions, 10 activated evaluations, and five paid accounts, with complete customer data and no material increase in onboarding burden. Negotiate any longer agreement only after those results. Exclusivity should require a substantial guaranteed minimum that covers the opportunity cost, remain narrow, and terminate automatically if quarterly performance falls short.

Keep courier dispatch partnered unless the trigger analysis shows both strategic necessity and superior economics. The default 90-day outcome should be a renewed or renegotiated API agreement, a documented backup plan, and no $600,000 commitment. Reconsider building only when credible 24-month volume makes the fully loaded build-and-operate cost clearly lower than partner fees, proprietary dispatch is proven to improve revenue or retention, and the company can staff the service without slowing its validated core product.

## Weekly operating scorecard

The founders should review a single scorecard each week:

- paid conversion and renewal by delivery-volume band;
- owner-qualified pipeline, quote acceptance, sales-cycle length, and acquisition cost by direct versus wholesaler source;
- time to activation and technician weekly usage;
- on-time delivery improvement and customer-reported operational outcomes;
- revenue, compute, support time, partner fees, and contribution margin per pharmacy;
- wholesaler introductions, activations, paid accounts, and integration work remaining;
- partner API cost, reliability, SLA incidents, and internal engineering burden.

At day 90, the board-level decision should be explicit: select the winning price bands, name the ICP, continue or end the wholesaler pilot under performance-based terms, and maintain the dispatch partnership unless the pre-agreed build triggers have actually been met.
