Case ID: org-heldout-attempt-003
Reviewer ID: org-heldout3-generator
Date: 2026-07-15
Decision deadline: 2026-07-18
Horizon: Four-site pilot from 2026-07-20 through 2026-08-14
Primary route and branch: `building-and-evolving-organizations` / `process-or-control`

# Decision

Do not hire a Head of QA or require a new executive to approve every release now. By July 18, authorize a four-site pilot that keeps Elena accountable from customer request through verified operation and adds the smallest control supported by the record: a unit-aware automated validation on every pilot change, plus an independent engineer check only when a defined risk trigger fires. Keep hardware interlocks, licensed-facility-operator release approval and physical override, the incident log, and the named 24/7 contact unchanged. The other 18 sites retain the current release path.

Elena is accountable for the pilot's safety, response time, customer continuity, and August 14 decision. Ravi owns validator implementation, replay evidence, and maintenance and remains Elena's backup. The author may not check their own triggered change: Ravi checks Elena-authored changes and Elena checks Ravi-authored changes. By July 18 Elena must record the four site identifiers, customer operator contacts, and a qualified alternate checker if anyone other than Elena or Ravi can author a pilot change. If independent coverage cannot be named, no novel high-risk configuration may bypass the check: the licensed operator chooses continued physical control or disabling our software, and Elena escalates to Ravi and the customer contact immediately.

Intermediate reviews: July 22 replay-readiness check; July 23 validator activation decision; July 27 first live review; August 3 and August 10 weekly reviews. Final review: August 14, owned by Elena, with Ravi supplying the evidence packet.

# State and gates

- Stage and shape: 13-person startup, one deployment lead with end-to-end ownership, one senior controls engineer maintaining the script and serving as secondary on-call, and 22 operating customer sites.
- Product state and type: live enterprise software sends configurations to physical refrigeration controllers. Evidence can appear within minutes for an unsafe setting and within 24 hours for recorded corrections; buyer-trust effects have longer, currently unknown latency.
- Survival: 17 months of cash at current spend is reported, so time-to-zero is not shown to bind this decision. The forecast and the full cost of a QA executive have not been verified.
- Reversibility and error cost: a process rule and validator can be removed, and the licensed operator can disable the software, but the June 27 excursion shows that a bad value can create material physical and customer-continuity risk before rollback. This is therefore a high-harm gate, not permission to trade away current protections for speed.
- Protected outcomes: safe refrigeration operation, customer response time, one end-to-end owner, operator authority, continuous operations, 24/7 contact coverage, incident evidence, and an immediate route to containment.
- Current-review gates: before live enforcement, the customer operator for each pilot site confirms the units and approved site limits used by the validator. By July 18 the CEO assigns a qualified owner to verify contract, safety, and incident-response obligations for the pilot; any required customer consent must be obtained before that site's first pilot change. No employment, compensation, title, or equity change is authorized.

# Evidence ledger

| Class | Material input | Owner, method, date, threshold | Decision effect |
|---|---|---|---|
| Observed | The June 2-July 11 deployment log records 38 changes, six corrections within 24 hours, and four corrections involving wrong unit conversions or copied site limits. | Ravi preserves the log and reproduces the six cases by July 22. | Establishes a recurring release-quality constraint and the replay set. |
| Observed | The June 27 ticket records 19 minutes of a bad compressor-staging value, operator override, a 7°C excursion in one zone, no food loss, and a two-hour investigation. | Elena includes the ticket and control timeline in the July 18 pilot artifact. | Makes physical safety and customer continuity non-negotiable gates. |
| Observed | Median request-to-release time was 5.5 hours; urgent changes took 44, 71, and 93 minutes. | Elena recomputes the same measures for pilot changes weekly and at final review. | Supplies response-time baselines and expansion limits. |
| Observed | Eleven changes had a recorded second-engineer request and no correction; six of the other 27 were corrected. | Elena audits Slack/check records against the deployment log by July 22. | Supports testing a check, but does not establish causation because check selection was not randomized. |
| Observed-as-scheduled | Four sites can pilot July 20-August 14; 26 scheduled changes are expected; historical configurations and corrections are due for replay July 22. | Elena records site IDs by July 18 and actual eligible/change counts weekly. | Bounds scope; a missed data or site-readiness gate keeps the validator in shadow mode. |
| Claimed | Ravi reconstructs that a unit-aware validator plus risk-triggered check would have caught five of six corrections. | Ravi runs blind replay by July 22: catch at least 5/6 known corrections and falsely block no more than 2/32 changes not recorded as corrections. Elena reviews results. | Pass permits July 23 live blocking; miss keeps it in shadow mode and triggers revision, not reliance. |
| Claimed | A Head of QA title and universal sign-off would increase enterprise trust; no customer has requested that title. | CEO records any dated customer/procurement request through August 14. | No hire now; reopen only on observed demand or a residual capability/capacity gap. |
| Claimed | Elena's workload is sustainable and cash lasts 17 months. | CEO verifies forecast by July 18; Elena records author/checker minutes, missed coverage, and after-hours load weekly. | A sustained residual load gap can open a prewritten role analysis; a title alone cannot. |
| Unknown | Validator generalization, false positives, correct risk-field set, and whether site units/limits are complete. | Ravi owns replay, shadow results, and operator-confirmed site schemas by July 23. | Failure revises or stops automation; it never removes operator approval or interlocks. |
| Unknown | Added urgent latency and 24/7 independent-check coverage. | Elena times dry runs of the three historical urgent paths by July 25 and every live urgent case; coverage roster is due July 18. | A latency or coverage miss revises the interface; unsafe inability to check triggers containment and rollback. |
| Unknown | Whether the control reduces live corrections without gaming or hidden rework. | Elena owns the August 14 log reconciliation, including corrections, validator events, checks, overrides, incidents, and author/checker time. | Determines keep, revise, expand, or stop; incomplete records prohibit expansion. |

# Bottleneck and alternatives

The outcome at risk is safe, correct configuration release without degrading customer response. The dated baseline is 6/38 corrections (15.8%) in 40 days, including one material near-harm incident; 4/6 corrections share a unit-or-site-limit mechanism. The proposed mechanism is preventable value-context error plus missing review. Rivals are incomplete site data, ambiguous customer requests, script defects, author workload, or correction-prone change complexity. The existing optional Slack check is the only recorded prior small intervention; it was not consistently applied and its apparent 0/11 result is confounded by selection.

Relief would reduce corrections, unsafe exposure, operator intervention, and customer investigation while preserving response time. The mechanism is falsified if blind replay does not catch at least 5/6 known corrections, live validator/check records do not intercept relevant errors, or correction and incident outcomes do not improve despite complete coverage.

The full cost includes Ravi's build and maintenance time, Elena's and Ravi's checking interruptions, customer-operator confirmation, audit artifacts, false blocks, urgent delay, a new handoff, after-hours coverage, two-person concentration and succession risk, and possible overreliance on incomplete rules. These costs will be measured in minutes and missed coverage; no new cash compensation, title, equity, recruiting, or management layer is approved.

Rejected branches:

- `keep-flat`: rejected because the recurring corrections and June 27 incident are observed, not merely an optics concern.
- `role-or-hire`: rejected now because no residual capacity or capability gap has been measured, Elena reports sustainable load, and the proposed title has no observed customer demand or frozen role charter.
- Universal executive sign-off: rejected because it adds a queue and single point of failure before urgent-latency effects are known.
- `decision-rights`: not primary because Elena's end-to-end ownership and operator safety authority are already clear; the missing mechanism is a bounded check, not a broad authority redesign.

# Smallest control and ownership design

Ravi documents by July 18 the proposed risk triggers: any unit conversion; value copied from another site; change to a site limit or compressor-staging value; value outside an operator-confirmed site bound; or any validator error/warning. Elena and the relevant licensed operator approve the site-specific unit/bound source by July 19. New triggers may enter the pilot only as a dated revision, not silently.

Every pilot change gets one release record containing site, request, author, changed fields, source units and destination units, source of any copied value, relevant site bounds, urgency, validator result, triggered-check result, operator approval, release time, verification, and containment route. A dimensional mismatch or out-of-bound value hard-blocks release. Other warnings require an independent check. The checker confirms request-to-value traceability, units, site limits, staging value when affected, and containment route; the record captures reviewer and timestamp before operator approval.

For ordinary triggered changes, the proposed checker service target is 60 minutes; for urgent changes it is 15 minutes. A missed target escalates immediately to Elena and then Ravi without transferring Elena's outcome ownership. If the author occupies one of those roles, the other must be the checker. If no independent checker is available for an urgent high-risk change, the customer operator retains physical control or disables the software; there is no unreviewed exception. The event is logged, Elena remains the customer-continuity owner, and Ravi restores technical coverage. Current interlocks, operator approval, incident logging, and the named 24/7 customer contact remain in force.

Ravi's validator documentation and rules repository are the maintenance artifact; Elena's release ledger is the decision artifact. Ravi is Elena's absence backup. By July 18 Ravi must document how enforcement is disabled without losing logs; by July 22 Elena must document how another qualified engineer could perform the check. Inability to name and enable that successor is a bus-factor failure that blocks expansion.

# Bounded test and thresholds

From July 20-22, use the release record and triggered independent check while the validator runs only in shadow mode. On July 22 Ravi replays all 38 historical configurations, with the six correction labels concealed until results are frozen. On July 23 Elena activates blocking only if replay catches at least 5/6 corrections, falsely blocks no more than 2/32 non-correction records, and each pilot site's units and limits have operator confirmation. Otherwise automation stays shadow-only.

From activation through August 14, all 26 expected pilot changes remain in scope. Elena owns live measures; Ravi owns validator measures. Compare with the stated historical baseline, while recording change mix and urgency as confounders. Safeguards are unchanged operator authority, interlocks, 24/7 contact, incident log, four-site isolation, 18-site current path, independent authorship/checking, evidence preservation, and immediate enforcement disablement.

Expansion thresholds require all of the following: 100% release-record and validator coverage after activation; 100% independent-check coverage on triggered changes; no configuration-attributable override, unsafe excursion, food-loss event, or other material safety/customer-continuity incident; at most 1/26 correction within 24 hours; median request-to-release no more than 5.5 hours; for at least two live urgent changes, median no more than 71 minutes and none more than 93 minutes; blind replay at least 5/6 caught with no more than 2/32 false blocks; no required contract/safety control gap; and a documented qualified successor. If fewer than two urgent live changes occur, timed dry runs of all three historical urgent paths must add no more than 15 minutes median and 20 minutes maximum, and live urgent performance remains an unresolved condition for broader emergency-path rollout.

At the August 14 review:

- `keep`: Keep the control only at the four sites through September 11 if safety, coverage, and ordinary latency pass but urgent evidence, site-schema confidence, or successor evidence is insufficient. Elena owns the additional evidence; no broader rollout occurs.
- `revise`: If interception evidence supports the mechanism but exactly one boundary, trigger, false-positive rate, checker service target, or workload assumption misses without a harm event, change that one variable by August 18 and run the four-site scope to one final review on August 28. Elena owns interface changes; Ravi owns a validator-rule change. A second material miss stops the pilot.
- `expand`: If every expansion threshold passes, extend only this validator-plus-triggered-check mechanism to the next four sites on August 17, after their operator-confirmed schemas and named owners are recorded. Elena owns the next scope and a September 11 review. Do not add a QA title, universal sign-off, or headcount.
- `rollback-or-stop`: Immediately disable validator enforcement and restore the four sites' prior release path if a pilot configuration causes an unsafe excursion, material incident, operator override, or food loss; if a required operator/interlock/24/7 control is absent; if an author bypasses a hard block or required independent check; or if evidence cannot be preserved. The licensed operator owns physical containment, Elena owns customer continuity and incident logging, Ravi owns technical rollback, and the CEO hands safety, contract, or legal consequences to the qualified independent owner assigned by July 18. Preserve all artifacts and do not restart without that owner's clearance and a new dated decision.

Open a role analysis only if, after trigger and interface revision, four consecutive pilot weeks show a sustained unstaffed checker queue, repeated missed response thresholds, or measured author/checker load that Elena and Ravi cannot cover without losing their current outcomes, and the expected relief exceeds recruiting, ramp, management, compensation, handoff, continuity, and runway costs. A customer request for a title alone is not enough; an observed procurement control requirement changes the control design, not automatically the headcount decision.

# Decision closure and lineage

Decision now: run the bounded process control; do not hire or add universal approval. The preserved option is the unchanged release path at 18 sites and immediate rollback of the four pilot sites, plus a later prewritten role analysis if a residual capacity/capability gap is measured. The switch condition is a failed safety/control gate, a falsified validator mechanism, or a sustained post-process capacity gap. Elena is next owner for every live outcome and the August 14 branch; Ravi is next owner for replay, validator, documentation, and technical rollback; the licensed operator remains physical-safety owner at each site.

The factual lineage is the user-supplied deployment log, June 27 incident ticket, Slack-check record, current operating controls, contract statement, and pilot schedule. The branch names, evidence classification, bounded-test schema, and decision-record shape are taxonomy synthesis. No essay-derived mechanism, historical company practice, grant formula, salary, legal conclusion, or current market claim is asserted. Contract interpretation, customer consent, safety obligations, incident handling, and any future employment or compensation action require current qualified review; the named qualified reviewer is unavailable in the supplied facts and must be assigned by the CEO by July 18.
