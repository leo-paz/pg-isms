# 30-day focus and morale operating record

## Decision header

- **Record date:** July 15, 2026
- **Decision:** Persist with the outcome of reducing missed appointments for clinics, but stop persisting with the present double-entry workflow and reject nights as an operating tactic. For the next 30 days, make the workflow repeatably usable at the third clinic.
- **Horizon:** July 15-August 14, 2026
- **Primary route:** `operating-with-focus-and-morale`, provisionally. There is no stated live financing or buyer process, fatal cash pinch, repeated authority queue, or acute incident. Because runway is not provided, the CEO must verify cash and the next two payrolls by July 16. If the cash math is default-dead or threatens payroll, `managing-runway-and-survival` immediately becomes primary and this plan becomes only its workload and customer-continuity envelope.
- **Supporting routes:** A privacy/security owner reviews the clinic workflow before release. If a live dated fundraise, sale process, or repeated authority bottleneck is discovered, route it respectively to `raising-and-governing-capital`, `navigating-acquisitions-and-exits`, or `building-and-evolving-organizations` and explicitly reallocate capacity rather than stacking this plan on top.
- **Current constraint:** The company has one promising outcome but has not shown that the workflow is usable and repeatable across clinics. Attention is being pulled toward a competitor narrative and an unsustainable hours proposal instead of resolving that uncertainty.
- **Evidence latency:** Workflow behavior can be seen daily; a trustworthy adoption read needs 10 scheduled clinic days. No-show outcomes may take longer and remain a secondary measure in this cycle.
- **Reversibility/error cost:** A small workflow change is reversible, but incorrect reminders, lost clinic continuity, or mishandled health data have high error cost and require release review and rollback.
- **Accountable owner:** CEO/founder. The CEO names one product lead, one implementation engineer, one clinic-success owner, and one backup engineer on July 15; a named person may hold more than one role, but each obligation below has exactly one owner.
- **Checks:** July 16 (survival and acute workload gates), July 17 (evidence audit and observed workflow), July 24 (release readiness), July 31 (first five clinic days), August 7 (10-day result), August 14 (final decision).

## What is true, claimed, and unknown

### Observed from the scenario, pending source-record verification

- The company has ten people and has operated for eight months.
- Three clinics have piloted the reminder workflow. Clinic 1 used it daily and recorded an 18% no-show reduction. Clinic 2 signed but has not launched because procurement stalled. At Clinic 3, staff opened 22% of alerts.
- Fourteen recent sales demos led to two paid pilots, a 14.3% demo-to-paid-pilot rate. This proves some willingness to try or pay; it does not yet prove repeatable demand.
- A funded competitor announced a similar product last week.
- Two engineers said the market does not care, and the product lead proposed continuing the current plan by working nights.

### Claimed, not established

- Clinic 3 staff attribute poor use to double entry. That is a valuable causal hypothesis, not yet a verified cause.
- The competitor's funding or announcement changes customer demand.
- The market “clearly does not care.” One daily-use clinic, one recorded outcome, and two paid pilots contradict certainty in that claim, while still falling short of product-market proof.
- More hours would make the current plan succeed. No outcome evidence supports this, and fatigue could degrade decisions and release quality.
- “Morale is low.” Treat this as a signal to investigate privately; do not infer lack of commitment or goal invalidity without behavior, workload, and user evidence.

### Consequential unknowns and owned tests

| Unknown | Evidence owner and method | Due date and threshold | Decision effect |
|---|---|---|---|
| Is the company inside a survival or payroll pinch? | CEO reviews bank balance, committed receipts, burn, liabilities, and exact payroll dates in a one-page cash schedule. | July 16. Threshold: the next two payrolls are funded and cash math is not default-dead under the company's current assumptions. | If missed, survival becomes primary immediately; CEO issues a bounded continuity plan and a dated handoff back here. |
| Is Clinic 1's 18% reduction real and attributable enough to use as premise evidence? | Product lead audits the numerator, denominator, comparison period, clinic closures, patient mix, and concurrent changes with Clinic 1. | July 17. Threshold: source records reproduce the result, with no obvious rival explaining most of it. | If reproduced, retain it as goal evidence. If not, label it unverified and do not use it to defend the premise. |
| Does double entry cause most of Clinic 3's abandonment? | Product lead observes at least three live or screen-shared reminder sessions with at least two staff roles, maps every handoff, and codes skipped alerts by reason. | July 17. Threshold: duplicate entry occurs in at least 70% of observed failed or abandoned alert attempts, and staff confirm a specific removal would change their behavior. | If met, build the smallest removal. If missed, do not build an assumed integration; select the largest observed friction as the one variable to test. |
| Is the 22% Clinic 3 baseline comparable and instrumented? | Implementation engineer reconciles eligible alerts, opens, users, days, and missing events with clinic staff. | July 17. Threshold: at least 95% of eligible alerts have a traceable disposition; otherwise collect three clean baseline clinic days. | Use the verified baseline for the August decision; if instrumentation is incomplete, fix measurement before feature work proceeds. |
| Can the top friction be removed safely within this cycle? | Product lead and implementation engineer compare no more than three reversible options—such as import, prefill, or one-system handoff—against the observed map; privacy/security owner reviews data flow. | Option chosen July 18; release-ready July 24. Threshold: the option removes duplicate manual entry from at least 80% of sampled target tasks, passes clinic acceptance, and introduces no unresolved privacy or reminder-correctness issue. | Release if met. Narrow or change the tactic if missed; do not start a broad redesign. |
| Is Clinic 3 adoption recoverable after the change? | Clinic-success owner reads the event log daily and holds two brief staff check-ins per week. | July 31 early check: at least 45% of eligible alerts opened across the first five scheduled clinic days. August 7: at least 60% across 10 scheduled clinic days and use on at least 8 of those days. | At target, continue. At 40-59%, adapt one observed friction. Below 40% without a data-quality confound, the current tactic is falsified. |
| Is Clinic 2 procurement actually unblockable in 30 days? | Clinic-success owner asks the clinic for the named approver, missing artifact, and earliest launch date, then records the answer. | July 22. Threshold: a named approver and dated path to launch exist. | If yes, preserve the option with paperwork only; it does not displace Clinic 3. If no, pause work until the clinic supplies a next action. |
| What do the 14 demos indicate about urgency and fit? | Sales owner codes each demo's segment, decision maker, stated pain, loss reason, next step, and whether the pilot was paid. | July 20. Threshold: records are available for at least 12 of 14 demos and loss reasons are customer-sourced rather than guesses. | Use this at the final goal review. Do not broaden sales activity merely to manufacture a larger funnel during this test. |
| Is the competitor changing buyer behavior now? | Sales owner asks active prospects a neutral question and records any deal loss or requirement directly tied to the competitor; CEO bounds research to two hours. | Initial read July 20; final August 14. Threshold: direct evidence from at least three relevant buyers or an actual lost deal. | Without that evidence, ignore the announcement operationally. With it, adapt positioning or requirements at the August review, not the core calendar mid-cycle. |
| Is workload already degrading judgment or health? | Each manager conducts a private check on hours, sleep loss, reversals, errors, conflict, and health symptoms; individuals may escalate confidentially to the CEO or a qualified professional. | First check July 16, then Mondays and Thursdays. Threshold: any acute health/safety concern, repeated sleep loss, or two fatigue-linked errors/reversals triggers immediate recovery and backup coverage. | Remove the person from the critical decision or release path until covered; route medical or acute mental-health concerns to qualified help. Do not treat the result as a morale score. |

## One state-changing priority

**Outcome:** By August 7, Clinic 3 will use the revised reminder workflow on at least 8 of 10 scheduled clinic days and open at least 60% of eligible alerts over those days, up from the stated 22% baseline, without wrong-reminder or privacy incidents. Sustain or improve that result through the August 14 review.

This is the shortest outcome that can change the company's state: it tests whether the successful Clinic 1 result can become a usable workflow at a second clinic. It is not a generic redesign, morale program, sales campaign, or race against the competitor.

- **Baseline:** 22% of alerts opened at Clinic 3; denominator and period verified by July 17. Clinic 1's daily usage and 18% no-show reduction are continuity and premise evidence, not permission to assume repeatability.
- **Target and affected users:** At least 60% of eligible Clinic 3 alerts opened across 10 scheduled clinic days, use on at least 8 days, and no critical correctness/privacy incident. Clinic staff and the patients receiving reminders are the affected users.
- **Mechanism:** Removing the largest observed workflow friction—currently hypothesized to be duplicate entry—will reduce the marginal effort of acting on an alert enough for staff to incorporate it into daily work.
- **Causal rivals:** Alerts may be poorly timed or irrelevant; ownership may be unclear; training may be weak; the clinic may not value the problem; or event instrumentation may undercount use.
- **Tactic:** Observe the workflow, choose one smallest reversible intervention on July 18, build and test it July 20-24, deploy July 27, and measure through August 14. The exact intervention follows the observation; “integration” is not preselected.
- **Falsifier:** After the intervention demonstrably removes the top verified friction and data capture is sound, Clinic 3 remains below 40% opens over 10 scheduled clinic days and staff behavior shows no move toward daily use. That falsifies this tactic, not automatically the missed-appointments goal.
- **Cycle end:** August 14. No threshold may be lowered after the results are seen.
- **Essential obligations:** Clinic 1 service continuity; Clinic 3 support and safe rollback; patient privacy and reminder correctness; incident response; payroll, legal, fiduciary, and existing teammate commitments; and the minimum Clinic 2 procurement response.

## Explicit stop, defer, delegate, and bound list

| Competing work | Disposition, owner, and effective date |
|---|---|
| Planned nights or weekend work | **Cancel** immediately, July 15. CEO owns enforcement. Incidents use the on-call path and compensating recovery, not a standing crunch plan. |
| Continuing the current workflow unchanged | **Cancel** as the Clinic 3 tactic on July 15. Product lead owns the observed-friction test. |
| Net-new features, broad redesign, new segments, and custom prospect features | **Defer** through August 14. CEO owns exceptions; only a safety, legal, or continuity need can interrupt. |
| Competitor response, launch campaign, conference, media, or prestige work | **Defer** through August 14. CEO permits one two-hour evidence review by the sales owner by July 20. |
| New sales demos | **Bound** to existing qualified commitments and at most two half-days per week for the sales owner. Product and engineering do not join unless the demo supplies evidence for this exact workflow question. Effective July 15. |
| Clinic 2 procurement | **Delegate** to the clinic-success owner, capped at two hours per week, with one dated request for the missing artifact and approver by July 22. |
| Clinic 1 continuity | **Delegate** to the clinic-success owner with a weekly usage review and a two-business-hour response for clinic-blocking issues. Escalate material deterioration to the CEO and backup engineer. |
| Internal status, all-hands preparation, and recurring meetings | **Cancel or replace asynchronously** on July 15 except the cadence below, required one-to-ones, incident coordination, and legal/privacy review. |
| Notifications and unscheduled availability | **Bound** during protected blocks. Clinic-blocking, security, privacy, and safety escalations use the named on-call channel; other messages are checked at noon and 4:30 p.m. |

## Protected execution and coverage

- **Maker time:** Product lead and assigned engineer reserve Monday-Thursday, 9:00 a.m.-noon, July 20-August 13. No routine meetings or notifications. Friday morning is for instrumentation, review, and rollback readiness. The CEO removes conflicting approval work before the blocks begin.
- **Direct user contact:** The product lead conducts three Clinic 3 workflow observations by July 17. From July 27, the clinic-success owner holds 20-minute Clinic 3 check-ins Monday and Thursday; the product lead attends the first two and any session tied to an observed failure. Clinic 1 gets one weekly continuity check.
- **Meetings:** A 30-minute Monday commitment review and a 45-minute Friday evidence review are the only team-wide recurring meetings for this cycle. Release/privacy review is a one-time bounded meeting. Status is written against the measures below.
- **Decision coverage:** The product lead owns scope and workflow decisions; the assigned engineer owns release readiness; the backup engineer has the current decision log, test plan, rollback steps, and clinic contacts. The CEO resolves priority conflicts within four business hours. If the CEO is unavailable, the product lead may preserve scope but may not expand it.
- **Escalation:** Wrong reminders, suspected privacy/security events, or patient-safety concerns go immediately to the privacy/security owner and CEO; pause the affected workflow and preserve evidence. A clinic-blocking defect receives acknowledgement within two business hours. Nonurgent requests wait until the next working day.
- **Release safeguards:** Staging or test data first, clinic acceptance on representative cases, privacy/security review, a named rollback owner, and daily correctness checks for the first five clinic days. Deep work never overrides an incident, patient safety, legal duty, or clinic-continuity handoff.
- **Workload boundary:** Plan for no more than 45 hours per person per week, no scheduled work after 6:00 p.m., and no weekend work. Everyone retains two consecutive recovery days. The company does not score commitment by hours or availability.
- **Exceptional push:** None is authorized. A genuine incident may require temporary coverage, but it ends when service is safe; the incident owner assigns equivalent recovery within 48 hours and reviews whether staffing or scope must change.

## Morale and persistence diagnosis

The observable morale signals supplied are two engineers' pessimistic statement and the product lead's nights proposal. By July 17, managers should privately establish whether there are also errors, withdrawal from decisions, conflict, sleep loss, blocked ownership, or lack of a finish line. Do not stage a public morale performance or pressure anyone to express optimism.

Plausible mechanisms are weak and delayed user evidence, Clinic 3 friction, an alarming competitor story, invisible progress, and an implausible workload proposal. The operating response is a short finish line, direct clinic contact, clear ownership, visible daily evidence, protected recovery, and a trusted private escalation channel. Morale is a safeguard and diagnostic signal, not a vote on market demand.

- **Goal premise:** Clinics with meaningful no-show costs will pay for and repeatedly use a reminder workflow that measurably reduces missed appointments without adding burdensome staff work.
- **Evidence for persistence:** One clinic reportedly uses the product daily and reduced no-shows by 18%; two of 14 demos produced paid pilots. These are promising but require audit and replication.
- **Current tactic:** A reminder-alert workflow that, at least at Clinic 3, appears to require double entry.
- **Decision now:** Persist with the goal premise and the clinic problem. Change the tactic. Do not persist with the unchanged workflow, broad activity, or nights.
- **Hard phase vs. tactic failure vs. premise failure:** A competitor announcement, one difficult month, or low confidence is only a hard-phase signal. Clinic 3 remaining below 40% after verified friction removal is tactic failure. Premise failure requires the stronger, precommitted combination in the decision rules below.

## Owned cadence and decision rules

| Measure | Owner | Baseline | Target or limit | Source and review |
|---|---|---|---|---|
| Clinic 3 alert opens / eligible alerts | Implementation engineer | Stated 22%; verified July 17 | At least 45% after five clinic days; at least 60% after 10 | Event log reconciled with clinic; daily, July 31, August 7 and 14 |
| Clinic 3 active clinic days | Clinic-success owner | Unknown | Use on at least 8 of 10 scheduled days | Event log plus staff confirmation; daily and August 7 |
| Top-friction removal | Product lead | Unknown | At least 80% of sampled target tasks no longer require the duplicate manual step, or equivalent threshold for the observed top friction | Workflow sample; July 24 and first two clinic days |
| Clinic 1 continuity | Clinic-success owner | Daily use; reported 18% no-show reduction | No material deterioration from its verified July 17 baseline; clinic-blocking issues acknowledged within two business hours | Usage/outcome records and clinic contact; weekly |
| Reminder correctness and privacy | Assigned engineer and privacy/security owner | No incident stated; verify | Zero known wrong-reminder, privacy, or security incidents | Release checklist and incident log; daily during rollout |
| Qualified sales evidence | Sales owner | 14 demos, two paid pilots | At least 12 demos coded with customer-sourced pain and loss reasons | CRM/notes; July 20 and August 14 |
| Workload health | Each manager; CEO accountable | Unknown | At most 45 planned hours, no scheduled nights/weekends, two recovery days; zero ignored acute escalations | Private check and schedule; Monday/Thursday |

At every check, the product lead records the observed result, any instrumentation or clinic-schedule confounder, safeguard status, and the matching branch in a one-page decision log.

- **Continue:** On August 7, Clinic 3 is at or above 60% opens across 10 scheduled days, used on at least 8 days, staff confirm the revised step fits the workflow, Clinic 1 remains stable, and safeguards hold. Continue the tactic through August 14, then prepare one bounded replication at Clinic 2 or the next matched clinic.
- **Adapt:** The goal evidence remains credible, but Clinic 3 is at 40-59%, or it reaches the usage target while a new single dominant friction is directly observed. Change one material variable—timing, ownership, relevance, training, or the next workflow step—and run a new 14-day test with a fresh threshold. The product lead proposes it; the CEO decides by August 14.
- **Reopen goal:** At the August 14 review, reopen the goal premise only if all three discriminating signals hold: (1) Clinic 1's 18% result cannot be reproduced or is largely explained by a rival; (2) Clinic 3 stays below 40% after the verified top friction is removed with sound data; and (3) both paid-pilot decision makers say, with recorded reasons, that the solved workflow is not worth continued use or payment. If any element is missing, name it and adapt rather than declaring the market dead. The CEO owns the review with the product lead and sales owner.
- **Stop:** Stop the deployed tactic immediately for wrong-reminder, privacy/security, safety, or legal harm that cannot be promptly contained, or if the clinic withdraws authorization. Stop or supersede the 30-day plan if survival math threatens payroll. Stop pursuing the goal only when the premise is invalidated under the reopen review or a qualified legal/safety owner says it cannot proceed.
- **Preserved option:** Maintain Clinic 1 safely, keep Clinic 2's procurement relationship warm with bounded effort, preserve the audited workflow and instrumentation, and avoid a broad integration or marketing spend until repeatability is demonstrated.
- **Next decision date and branch owner:** August 14, 2026; CEO/founder decides `continue`, `adapt`, `reopen-goal`, or `stop` from the written evidence. Product lead owns the next tactic, clinic-success owns continuity, and the CEO owns any route change.
- **Handoff back to ordinary focus:** Survival, financing, buyer, organizational, or acute-risk routing hands back only when its owner records that the binding condition is closed or bounded, names released capacity, and gives a dated checkpoint. This 30-day plan must then be re-baselined rather than silently resumed.

## Lineage and revalidation boundary

This record applies the mechanisms and runtime structure in the supplied frozen `operating-with-focus-and-morale` skill package. The route precedence, evidence classes, branch names, safety gates, record structure, and combined thresholds are cross-source/taxonomy synthesis, not a claim about a single author's recipe. No essay URL or exact source-line material was included in the authorized inputs for this response, so no essay-derived claim is attributed here.

Before acting, the CEO must revalidate the scenario's clinic metrics, cash/payroll facts, contractual commitments, product telemetry, staff availability, and current competitor effects. A qualified privacy/security owner and, where necessary, healthcare/privacy counsel must validate data handling, patient communications, incident duties, and the release/rollback plan. Qualified medical or mental-health support—not this operating record—owns any acute health concern.
