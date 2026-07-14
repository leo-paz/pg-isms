# 30-day release plan

This is a redesign of an installed workflow, not just a low-risk notification feature. The need and willingness-to-pay signal are strong enough to ship a bounded release: six warehouses used the manual workaround for two monthly cycles, and three committed money. They do not yet justify a broad campaign or a mandatory launch to 600 clerks. The keyboard-dependent queue makes compatibility, migration, and interruption recovery release requirements.

## Release record and scope

- **Target job:** get an urgent cycle-count exception to the responsible supervisor quickly enough for a clerk to resolve it without the alert disappearing in email.
- **First complete outcome:** deliver the existing urgent-exception decision through the web flow, deep-link to the correct queue item, let the supervisor acknowledge or assign it, and record acknowledgment and resolution. Keep email active as fallback.
- **Build now:** feature-flagged warehouse/cohort access; notification delivery and retry; deep link; acknowledgment/assignment; audit events; monitoring; rollback; and either preservation of existing queue cards and shortcuts or a clearly labeled compatibility view. The core experienced-clerk shortcuts must work end to end before live exposure.
- **Defer:** the six-week rules-engine rewrite, new rule authoring, unrelated queue redesign, broad acquisition campaign, and forced migration. The rewrite enters a later engineering plan only if release evidence identifies a rule limitation that blocks the outcome or materially increases risk.
- **Assumptions to confirm by day 3:** the current exception rules are usable without the rewrite; the web flow has appropriate authentication and warehouse-level authorization; and no new regulated messaging or employee-monitoring issue is introduced. A failed security, privacy, authorization, or data-integrity check blocks release.

## Calendar, exposure, and work

### Days 1–3: lock the gate and baseline

The shipping DRI creates the release record and names one engineering DRI, one evidence DRI, one support DRI, and a local supervisor at each pilot warehouse. Use the three paid pilots as the initial release population. For each, capture the prior two cycles' email/manual-SMS baseline: time from exception creation to acknowledgment and resolution, missed urgent exceptions, duplicate or stale alerts, queue errors, abandonment, and support load. Segment results by warehouse, shift, supervisor, and experienced versus newer clerks.

Recruit a representative acceptance group from the paid pilots, including heavy shortcut users. Publish the cohort list, support channel, escalation schedule, rollout calendar, and rollback authority. Tell participants that this is a staged pilot, email remains available, and the new flow can be withdrawn.

### Days 4–8: make the smallest complete release safe

Engineering closes only gaps required for the outcome: reliable delivery, retry/deduplication, correct deep links, acknowledgment/assignment, event instrumentation, warehouse authorization, feature flags, and an immediate switch back to email-only operation. Preserve shortcut bindings, focus order, card meaning, and interruption recovery. If the new card layout cannot meet the experienced-user acceptance gate in this window, ship notifications into the existing card layout or a compatibility view; do not force the new layout.

Replay representative events and failure cases: duplicate and stale alerts, wrong-warehouse access, lost connectivity, notification retry, a clerk resuming interrupted work, and rollback while work is in flight. The support DRI prepares a one-page migration aid and office hours; engineering writes the operational runbook.

### Days 9–10: acceptance and go/no-go

Run observed core-path tests with both experienced shortcut users and newer clerks. Compare against the existing queue rather than collecting preference votes. The release proceeds only if all core actions are reachable by keyboard, no critical shortcut or focus regression remains, authorization and data-integrity tests pass, instrumentation is complete, support is staffed, and rollback is rehearsed.

### Days 11–15: one-warehouse canary

At one paid-pilot warehouse, run one day in shadow mode to compare intended notifications with actual urgent exceptions, then enable live notifications for a small consenting cohort across at least two shifts. Email remains on. Shipping and engineering monitor delivery, acknowledgment, missed/duplicate/stale alerts, queue completion, shortcut errors, and support requests daily. The local supervisor checks anomalies against the source record.

At the day-15 review, expand only if the operational and experienced-user gates below pass. Otherwise make the smallest discriminating change, extend the canary, or roll back; elapsed calendar time is not a reason to expand.

### Days 16–23: paid-pilot rollout

Expand sequentially to the other two paid pilots, one warehouse at a time with a 48-hour observation interval. Include representative experienced and newer users; do not make the flow mandatory. Provide shift-based training and keep email and the compatibility path available. The evidence DRI publishes a warehouse- and user-segment comparison, not a blended success number.

At day 23, allow at most one targeted iteration supported by observed behavior—for example, alert routing, shortcut focus, or acknowledgment copy. Do not turn the pilot into the rules-engine rewrite or a feature-vote exercise.

### Days 24–30: complete one trustworthy cycle and decide

Hold exposure steady long enough to observe the remainder of the monthly cycle. Growth may prepare same-segment recruitment materials, but may not start the broad campaign. On day 30, review results against the precommitted gates and document one of the branches below. Because the underlying job is monthly, one web cycle is the minimum useful release window; a general launch should require a second released-workflow cycle unless the team had pre-registered a shorter, demonstrably representative interval.

## Evidence and precommitted gates

Confirm numeric thresholds on day 3 from baseline rather than adjusting them after seeing pilot results. A reasonable initial proposal is:

- **Outcome pass:** at least 25% lower median time to acknowledge urgent exceptions than the email baseline, no increase in the share missed by the existing SLA, and improvement or non-inferiority in time to resolution in each paid pilot.
- **Repeated-use pass:** at least 70% of included supervisors use acknowledgment/assignment on two or more eligible occasions, where volume permits. Report low-volume sites separately.
- **Experienced-user pass:** core queue completion time is no worse than 10% above baseline after brief training, with no more than a 2 percentage-point increase in error or abandonment; all critical shortcuts remain operable.
- **Operational pass:** at least 99% correct delivery, under 1% duplicate or stale alerts, no wrong-warehouse delivery, no lost audit state, and support volume manageable by the named owner.
- **Immediate pause/rollback:** any unauthorized disclosure, wrong-warehouse alert, lost or corrupted queue state, critical shortcut failure, or evidence that the web flow causes more urgent exceptions to be missed than email. Also pause if delivery falls below 95% for 30 minutes or the experienced-user completion penalty exceeds 15% in two consecutive observed sessions.

Track alert volume, shift staffing, warehouse mix, cycle timing, training, novelty, outages, and concurrent process changes as confounders. Do not use launch completion, satisfaction, clicks, or raw notification opens as the primary evidence.

## Ownership and day-30 branches

- **Shipping/product DRI:** artifact scope, cohort and inclusion, exposure sequence, calendar reviews, migration, and the expand/pause/rollback decision.
- **Engineering DRI:** implementation, security/authorization and data integrity, shortcut compatibility, flags, telemetry, monitoring, and technical rollback. Engineering may propose the rules rewrite later but does not make it a prerequisite without evidence.
- **Evidence/learning DRI:** baseline integrity, comparison design, segmentation, confounders, and interpretation. Only a newly exposed uncertainty about the user need returns to learning.
- **Support/warehouse-operations DRI:** training, office hours, incident intake, local escalation, and confirming that anomalies match warehouse reality.
- **Growth DRI:** no broad campaign during the first release. After the released workflow passes the outcome, repeat-use, compatibility, and operational gates, growth may recruit the same warehouse segment into the next bounded cohort and own activation and retention evidence.
- **CEO:** executive sponsor who resolves resources and accepts the recorded gate; the CEO's two-week target does not override safety, compatibility, or evidence thresholds.

Day 30 has four explicit branches: **expand** to the other three validated warehouses as a bounded cohort if every gate passes; **iterate** on the smallest diagnosed friction if outcomes are promising but a non-safety gate misses; **redesign** the queue integration if experienced-user performance fails; or **pause/rollback** if reliability, authorization, data integrity, or missed-exception limits fail. Only after another trustworthy released-workflow cycle should the team decide on mandatory migration, a broad campaign, or an engineering investment in a new rules engine.
