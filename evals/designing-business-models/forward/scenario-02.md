Case ID: scenario-02
Reviewer ID: business-model-forward-004

Primary owner: `designing-business-models` — this is a company-boundary and supplier-optionality decision, not a declaration about what is “core.”

Handoffs:

1. `engineering-for-leverage` owns the interface implementation, test fixtures, instrumentation, and failure attribution.
2. `shipping-and-iterating-products` owns the controlled production rollout and installation rollback.
3. `learning-from-users` collects distributor impact evidence from delayed and pilot installations under this plan.
4. `raising-and-governing-capital` is consulted only if the integration branch later passes the capability and $2.4 million capital gate.

## Business-Model Record

| Field | Current record |
|---|---|
| Product and state | Validated cold-chain hardware sold to regional food distributors; 14-person company. Survival/runway is unknown. Hardware gates require current inventory, tooling, fabrication, certification, reliability, working-capital, physical-risk, supplier-qualification, component, and channel economics before irreversible investment. |
| Binding constraint | One calibration-module supplier creates eight-week delays, 7% rework, and missed installation dates. Specialized tooling produces dependency, but the company lacks internal-line capabilities. |
| Latency / reversibility / error cost | Second-source qualification takes six weeks and a standard interface ten engineering weeks; both are reversible and preserve options. An internal line costs $2.4 million, takes about twelve months, and is difficult to reverse. Calibration failure can spoil product, invalidate compliance, or harm customer inventory, so certification and reliability gates override schedule. |
| Facts to verify by day 10 | Runway; weekly demand and forecast; inventory and missed-install contribution loss; incumbent service terms and tooling rights; current certification-change requirements; field-failure history; $180/$230 quotes, lead times, minimum orders, warranty and escalation terms; internal yield, staffing, floor space, calibration traceability, working capital, and three-year volume. Use dated supplier quotes and current legal/certification sources. |

| Boundary | Ownership and coordination | Capability / fixed cost / maturity | Interface, switching, and failure attribution |
|---|---|---|---|
| Incumbent-only partner | Company retains customer, installation data, acceptance standard, and system architecture; supplier owns specialized tooling. Current dependency yields eight-week delays and 7% rework. | $180/module; mature enough to ship but current performance is unacceptable. Fixed tooling exposure and contractual remedies are unknown. | Proprietary fit creates switching cost. Require lot IDs, calibration traces, promised/actual dates, and root-cause coding so module failure is not mislabeled as architecture failure. |
| Second qualified partner | Same customer/data/standard ownership stays with the company; no exclusivity. Coordination adds qualification and dual planning but reduces dependency. | $230/module and six-week qualification. Maturity, volume capacity, certification evidence, and replaceability must be demonstrated. | Without the standard interface it is an alternate with some integration cost; acceptance tests separate supplier calibration, interface, sensor, and installation failures. |
| Standard interface plus dual source | Company owns/publishes the internal module specification and conformance suite; suppliers retain fabrication/tooling. This is the strongest replaceability path. | $70,000 and ten engineering weeks. It consumes scarce engineering time but avoids acquiring factory operations. | Either conforming supplier can be switched by purchase order and validated lot. Versioned connector, calibration protocol, and test fixture bound switching cost and expose whether supplier or architecture failed. |
| Internal line | Company would own tooling, process, quality system, and production schedule, but also all yield, staffing, certification, inventory, and maintenance risk. | $2.4 million, roughly twelve months, and capabilities the 14-person team does not have. Internal per-unit cost, utilization, hiring, and payback are unknown. | It removes vendor switching but creates an internal factory dependency. A separate module interface is still valuable for validation and future external backup. |

Customer value is an installed, reliable, traceable sensor on the promised date. The buyer/payer is the distributor through the validated hardware sale; budget, price, revenue timing, channel margin, concentration, switching, support, and expansion are not supplied and must be preserved in the existing model. The 90-day decision must measure missed-install revenue and support cost rather than assuming the $50 module premium dominates. No partner receives customer data beyond what calibration requires.

## Ninety-day boundary test

- **Days 0–10:** COO freezes a baseline of on-time delivery, rework, first-pass calibration, field failure, missed installs, expedite/support cost, inventory, and contribution lost. Send the incumbent a corrective-action request with weekly promised-versus-actual reporting. Engineering freezes a versioned conformance specification and checks whether the interface change affects certification.
- **Days 1–42:** Qualify a 30-module lot from the $230 supplier. The lot must achieve at least 98% first-pass calibration, no more than 2% rework, at least 95% delivery within the contracted window, complete traceability, and zero critical reliability or safety failures. No unqualified module goes to a customer.
- **Days 1–70:** Spend the quoted $70,000 to implement the standard interface and automated conformance fixture. It must accept both suppliers without product-board redesign, complete a supplier swap in no more than four engineering hours, and produce supplier-versus-interface fault codes on 100% of test failures.
- **Days 43–90:** If qualification passes, run 50 controlled production modules, split 25/25 where supply permits, and install only after the existing release/certification process. Require at least 95% on-time availability, at most 2% rework per supplier, no critical field failure, and no more than one noncritical module failure per supplier. A known-good module and rollback procedure remain available for every installation.

The COO owns the decision; engineering owns technical acceptance and quality may veto release. Incremental exposure is capped at $120,000: the $70,000 interface, the 30-unit $6,900 qualification lot, and no more than $43,100 of test labor, fixtures, freight, and certification review. Ordinary production inventory remains separately reported. Review on day 42, day 70, and day 90. Confounders include lot mix, demand swings, shipping delays, installer error, sensor-board changes, and certification review; all are coded before comparing suppliers.

Precommitted boundary branches:

- **dual-source:** Select this on day 90 if the second supplier and interface meet every qualification, reliability, traceability, and switching threshold. Allocate initially 60% to the better on-time supplier and 40% to the other, with no supplier above 70% for the next quarter; rebalance monthly using quality and delivery, not unit price alone.
- **partner:** If the second supplier passes but the standard interface misses only the four-hour switching or automated-attribution target, use the second supplier for bounded overflow while repairing the interface for at most 30 more days and $25,000.
- **repair:** If neither supplier meets the thresholds but failures are noncritical and attributable, retain only enough incumbent volume to meet validated installs, invoke corrective terms, and qualify a new replaceable specialist against the same interface. Do not hide supplier failure by lowering acceptance standards.
- **integrate:** Authorize an internal-line plan only if external options fail the thresholds for two consecutive quarters, supplier-caused misses exceed 5% of scheduled installs, a current demand model supports a risk-adjusted payback within 36 months, the company can fund $2.4 million plus 25% contingency while retaining 18 months of runway, and named manufacturing/quality leaders can be hired before tooling commitment. Capital, governance, and hiring then move to their specialist owners.
- **stop:** Stop the pilot and quarantine affected lots on any critical calibration, certification, food-safety, or traceability failure; stop interface work if the certification path or spend cap is breached. Resume only through the accountable release process.

Selected branch now: qualify the second supplier and build the standard interface, aiming for dual-source. Immediate vertical integration is rejected because “core” does not show that control benefits exceed twelve months, $2.4 million, management load, delay, working capital, and missing capability. Incumbent-only sourcing is also rejected. Preserve internal integration as a priced option with a quantified switch condition. Delay costs are tracked as missed contribution and customer installations; the next owner per result is engineering/shipping for dual-source, business models for a repaired partner test, or capital and organization specialists after an integration gate passes.
