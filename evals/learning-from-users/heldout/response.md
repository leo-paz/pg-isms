# Raw held-out output
Case ID: pediatric-infusion-operations
Generator ID: learning-heldout-generator-003

# Decision memo — July 14, 2026

To: Niveo founders
Subject: Earn the right to interrupt care

## Decision

Do not put autopause into live patient care this summer, and do not promise it for the September pilot. Offer the hospital a bounded eight-week learning pilot: retrospective adjudication, high-fidelity simulation, and prospective silent mode, with no pump control and no model output used for treatment. Use the proposed three engineering weeks to build the reversible test apparatus—complete-context ingestion, an audit trail, a clinician review screen, and a pump emulator—not a production interrupt.

Stay focused on pediatric oncology through October 31. Adult infusion and veterinary oncology are untested opportunities, not easier pivots; observing neither workflow means moving now would discard the learning Niveo has already paid for. Revisit them only if the pediatric stop rule is triggered.

The interviews establish an important problem and a vocabulary clinicians use, but not the solution. Thirteen requests, six pump add-on requests, two urgency letters, one hypothetical price, and an unpaid pilot offer are interest. The stronger behavioral evidence points elsewhere: 31 of 36 alerts were overridden, and 22 overrides led to a pharmacist or physician call. That suggests the job may be obtaining missing context and authorized disposition, not automatically stopping a pump. The current model also has no live-use evidence. If the 47 extra alerts are all non-actionable, only 9 of 56 flags corresponded to known discrepancies. That is not yet a defensible basis for autonomous interruption.

## Learning record

**Product, stage, segment, and sample.** This is pre-live, high-harm enterprise clinical software for pediatric oncology infusion centers. The primary workflow segment is bedside nurses administering chemotherapy and pharmacists verifying it; medication-safety leaders own the policy, while IT/security, procurement, and an economic buyer determine whether the product can actually deploy. Recruit three pediatric centers: the two already observed plus one center not introduced through an enthusiastic innovation sponsor. At each, include at least three nurses across shifts and seniority, two current oncology pharmacists, one safety leader, and the relevant IT/security, procurement, and budget owners. Workflow participants must have administered or verified pediatric chemotherapy in the preceding 30 days. Innovation staff do not substitute for users, safety owners, or buyers. Include reluctant users and a site that declines; do not sample only champions.

**Claim to test.** When an order, patient state, protocol, and pump setting conflict, a nurse and pharmacist with complete same-day context and a clear escalation path can reach the correct disposition before infusion continues, without an unsafe delay or a flood of non-actionable interruptions. The initial product hypothesis is therefore clinician-reviewed discrepancy resolution, not autonomous control.

Competing explanations are that the true failure is missing weight or renal data, an undocumented physician-approved exception, unclear authority, slow notification, or process delay. Autopause is disconfirmed if clinicians still need off-system context to decide, routinely override a context-complete flag, make more incorrect dispositions, or experience clinically meaningful delays. The broader opportunity is disconfirmed if hospitals will praise the idea but will not supply data, name deployment owners, start security/procurement, or commit budget.

**Known evidence and contradiction.** Leaders explicitly request interruption and describe severe consequences. In observed behavior, however, existing interruptions are mostly bypassed because the alert lacks facts or an approved exception; many bypasses appropriately initiate expert consultation. The retrospective model found nine of ten known discrepancies but raised 47 additional alerts in 600 infusions. Those 47 must be blindly adjudicated: some may be previously unrecognized discrepancies, while others may be alert burden. No live use, EHR integration, pump integration, signed multidisciplinary ownership, or payment exists. Therefore performance, workflow safety, deployability, and willingness to pay remain four separate uncertainties.

**Recruitment, consent, and exclusions.** The CEO owns institutional recruitment and signed commercial commitments. The clinical product lead owns observation and the case log. The medical adviser and an independent pediatric oncology safety reviewer own adjudication and harm review; engineering does not label its own outputs. Obtain the institution's written privacy, research/quality-review, and safety approvals as applicable, plus participant consent for observation and simulation. Use deidentified data through an approved transfer path. Log confusion, delay, overrides, escalation, and potential harms, including harms from stopping treatment.

Exclude patient-facing alerts, live pump commands, and care decisions based on Niveo output. Exclude adult and veterinary cases from the pediatric evidence base. Separate an enriched set of known discrepancies from consecutive, unselected infusions so the rare-event base rate is not hidden. Do not expose protected data or create a manual workaround outside hospital approval.

## Tests, thresholds, and calendar

**July 14–24: explain current behavior.** Blinded reviewers classify all 36 observed alert episodes and all 47 extra retrospective flags: data absent, genuine mismatch, authorized exception, duplicate/irrelevant rule, or unresolved. Reconstruct who knew what, who had authority, what call occurred, how long resolution took, and whether continuing or stopping was correct. Deliverable: an agreed taxonomy and a complete-data specification. Do not code around an unclassified alert.

**July 27–August 14: earn a pilot.** The September site must name accountable pharmacy, bedside nursing, safety, IT/security, and procurement owners; approve the data path and study mode; agree on escalation, override, rollback, incident review, and success measures; and sign the pilot scope. If any of these are missing on August 14, cancel the September start and continue only deidentified retrospective work. An innovation director's invitation is not authorization.

**August 17–September 4: compare workflows safely.** In randomized-order tabletop simulations, compare current workflow, a context-complete advisory with human acknowledgement, and simulated autopause. Use at least 60 adjudicated cases spanning known mismatches, valid exceptions, missing data, and normal infusions, with at least 18 frontline participants across the three-site sample. Measure correct disposition, time to disposition, appropriate escalation, non-actionable interruption, unsafe continuation, and unsafe delay. Do not optimize for fewer calls: a call is beneficial when policy requires expert authority.

Advance the advisory workflow only if participants reach the adjudicated disposition in at least 95% of scenarios, it creates no unsafe continuation or unsafe delay in the simulation, and median resolution time is no more than two minutes worse than current workflow. Autopause does not advance to live care under this study; it requires a subsequent clinician-led safety, regulatory, and deployment review regardless of simulation results.

**September 8–October 30: silent prospective test.** If the August gate passes, run Niveo alongside care without displaying outputs. Evaluate at least 600 consecutive eligible infusions across at least two sites, or report the smaller achieved sample without upgrading the claim. Independent reviewers adjudicate every flag and a sampled set of unflagged cases. The predeclared technical/workflow bar is detection of every protocol-significant discrepancy present in this sample and no more than 1% of infusions generating a non-actionable alert. A pass supports a monitored, human-in-the-loop advisory pilot; it does not establish that rare catastrophic errors are prevented.

For cases enrolled after September 18, a full 42-day toxicity window extends past October 31. Preserve that follow-up and label it pending. Niveo cannot honestly claim clinical-outcome efficacy by Demo Day or October 31.

**Demand test by October 15.** Ask each qualified site to sign a design-partner agreement specifying data access, named clinical and deployment owners, security/procurement milestones, scope, schedule, and dollars. The commercial threshold is two such agreements at an explicit price, with at least one paid pilot or non-refundable deployment commitment. Test the CFO's $180,000 statement by putting an agreement in front of an authorized buyer. A price-page visit, a waitlist entry, an urgency letter, or a subsidized pilot does not pass. A 20-hospital waitlist may recruit the sample, but the accelerator must not be told it validates demand.

## October 31 decision and ownership

- If the workflow, silent-mode, deployment, and commercial thresholds all pass, hand the context-complete, clinician-reviewed product to engineering for a monitored build and hand the evidenced segment to growth. Keep autopause behind a separate safety gate.
- If safety/workflow passes but contracting or deployment remains incomplete, continue enterprise learning with a fixed next review date; do not scale acquisition.
- If sites will commit but alert quality misses the bar, keep the customer relationship and return the specification to engineering only for a bounded correction and retest.
- If Niveo cannot secure two real deployment paths and one monetary commitment, or cannot reduce non-actionable alert burden by October 31, stop pediatric product build and return the preserved evidence to an explicit opportunity-choice review. Only then compare pediatric, adult, and veterinary segments using fresh workflow observation and the same commitment standard.

This plan preserves runway while testing the irreversible assumption first: not whether Niveo can make a pump stop in three weeks, but whether stopping—or even alerting—is correct, usable, deployable, and worth paying for in the actual care system.
