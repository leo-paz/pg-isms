# 30-day release record

## Release decision

This is a first web release with redesign risk. The manual SMS trial across six warehouses and three paid pilots validates the buried-alert problem and willingness to commit, but it does not validate the web workflow or the changed queue for 600 shortcut-dependent clerks. Day 14 should therefore be the first bounded production release, not a mandatory all-user cutover.

The smallest complete outcome is: an authorized supervisor sees an urgent cycle-count exception, acknowledges it, and reaches the existing resolution path; an experienced clerk can then process the queue without losing keyboard efficiency or interruption recovery. Keep the old email process and legacy queue available throughout the 30 days.

Scope only urgent cycle-count exceptions, notification delivery, acknowledgement, deep-linking, and the minimum queue integration needed to complete that path. Defer the six-week rules engine, other alert types, cosmetic queue redesign, and the broad campaign. The main uncertainty is whether the web flow improves timely acknowledgement without degrading the installed clerk workflow.

## Build and release calendar

| Days | Build and exposure | Gate |
|---|---|---|
| 1-3 | The shipping DRI freezes the release record and maps the supervisor-to-clerk path. Engineering records every existing shortcut and interruption/re-entry behavior with representative experienced clerks. Establish the email baseline by warehouse, role, alert volume, acknowledgement time, queue completion time, abandonment, and support incidents. | No build expansion until cohort, metrics, fallback, and stop rules are signed off. |
| 4-7 | Instrument alert created/delivered/viewed/acknowledged/resolved events. Add a warehouse/user feature flag, one-action rollback, delivery monitoring, audit trail, and legacy-layout switch. Preserve existing shortcuts or add a compatibility mode; run core-path, authorization, wrong-warehouse routing, data-integrity, keyboard, and interruption-recovery tests. | Zero critical failures; every urgent alert still sends email; support can revert a user or warehouse without a deploy. |
| 8-10 | Run the web flow in shadow alongside email in the three paid-pilot warehouses. Supervisors and 10-15 experienced clerks perform scripted and real-path rehearsals while email remains authoritative. Fix only release-blocking path, instrumentation, accessibility, or compatibility defects. | Event counts reconcile to source exceptions; no alert is lost or misrouted; all critical shortcuts work. |
| 11-13 | Train local champions and support using a one-page workflow, make fallback visible, publish the on-call route, and confirm the next cycle window. Segment the pilot so new and experienced clerks are both represented. | Each site has a named champion; support and rollback rehearsal succeeds. |
| 14 | Enable the web flow for one paid-pilot warehouse at the start of its cycle, initially for its supervisors and a representative group of experienced clerks. Email and the legacy queue stay on. | This satisfies the two-week launch request as a real production release, but not as forced exposure to all 600 users. |
| 15-20 | Review delivery and safety daily; observe real acknowledgement, queue, shortcut, abandonment, and support paths. If the operational gate holds for 48 hours and there is enough alert volume, enable the other two paid-pilot warehouses. Do not treat low-volume elapsed time as evidence. | Expand only after operational thresholds pass; otherwise make the smallest discriminating fix and restart the observation window. |
| 21-27 | Hold exposure through a complete cycle and compare with each warehouse's email baseline. Growth may prepare targeted activation for the already validated segment, but no broad campaign runs. | Do not expand beyond the paid pilots on interim enthusiasm or launch completion. |
| 28-30 | Evidence owner locks the dataset and reports by warehouse, role, tenure, and alert volume. On day 30, the shipping DRI runs the precommitted expand/change/rollback decision. If a complete cycle has not occurred, keep the cohort stable and move the outcome review rather than claiming success. | Full-cycle evidence and all pass thresholds are required for broader exposure. |

## Evidence contract

Use the prior email period as the within-warehouse comparison and report new and experienced users separately. The primary outcome is timely acknowledgement of urgent exceptions; the redesign guardrail is experienced-clerk queue performance. Supporting evidence is repeated web use, resolution completion, abandonment, fallback use, support load, and errors—not survey approval.

The following are explicit starting assumptions to confirm on days 1-3 because the scenario supplies no baselines:

- Pass: at least 90% of urgent exceptions are acknowledged within 15 minutes and median time-to-acknowledge improves by at least 30% versus the matched email baseline.
- Workflow guardrail: experienced-clerk median and p95 queue completion time degrade by no more than 5% and 10%, respectively; at least 98% of observed keyboard-driven tasks complete without mouse substitution or shortcut failure.
- Reliability/harm limits: 100% of source urgent exceptions are delivered by at least one channel, 0 wrong-warehouse or unauthorized disclosures, and at least 99.5% successful web delivery.
- Adoption/support: at least 80% of enabled supervisors use the web acknowledgement path repeatedly during the cycle, abandonment is below 5%, and support stays below 10 workflow tickets per 100 enabled users with no critical ticket unresolved beyond one business hour.
- Evidence minimum: one complete cycle, all three paid-pilot warehouses, at least 30 urgent exceptions, and at least 10 experienced clerks observed. If volume is lower, hold rather than relax the sample after seeing results.

Stratify or annotate warehouse size, exception volume, supervisor tenure, clerk experience, training attendance, cycle timing, outages, and simultaneous email/SMS exposure. Those can otherwise make novelty, training, or a busy site look like product effect.

Pause new enrollment immediately for a lost or misrouted alert, unauthorized access, irreconcilable event counts, a critical shortcut failure, or core-path unavailability longer than 15 minutes. Roll the affected cohort back to email and the legacy queue if the issue is not contained within one hour, if either workflow guardrail breaches for two consecutive operating days, or if support exceeds its limit. Preserve logs and notify site champions before re-exposure.

## Ownership and day-30 branches

- **Shipping DRI (product):** owns scope, artifact, release record, feature-flag exposure, calendar, support readiness, and the day-30 decision.
- **Evidence owner (research/analytics):** owns the sample, baselines, threshold integrity, confounder analysis, and interpretation; the shipping DRI cannot redefine a miss after results arrive.
- **Engineering DRI:** owns tests, authorization and data integrity, instrumentation, shortcut compatibility, flags, migration machinery, monitoring, and rollback execution. The rules-engine rewrite remains a separate architecture proposal.
- **Warehouse operations lead:** selects representative users, schedules training, names each site champion, and coordinates fallback. Support owns the response queue; the engineering on-call owns technical incidents.
- **Growth DRI:** may own targeted activation and retention for the paid segment, but holds the broad campaign until the released web workflow passes the evidence gate. Business-model ownership retains payer, price, and pilot packaging decisions.
- **CEO:** sponsors the outcome and resolves resourcing conflicts, but does not substitute a deadline for the recorded user-safety and migration gates.

At day 30: if all thresholds pass, enable the next 10-20% of the 600 clerks with the same fallback and repeat the gate before each expansion; growth can start a segment-specific campaign. If acknowledgement improves but clerk performance misses, keep the pilots, restore the legacy card layout/compatibility mode, and test that single change. If clerk performance passes but acknowledgement does not improve, keep email authoritative and test notification salience or delivery, not the rules engine. If reliability or harm limits fail, roll back and return to shadow mode. If both primary outcome and workflow guardrails fail after a valid cycle, stop this release; return only the specific unresolved notification need to learning rather than silently pivoting.
