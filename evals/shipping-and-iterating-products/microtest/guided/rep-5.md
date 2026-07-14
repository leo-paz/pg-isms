# 30-day release plan

## Release record and gate

This is a user-visible redesign layered onto an existing B2B workflow, not a greenfield launch. The job is: get an urgent cycle-count exception to the responsible supervisor, have it acknowledged and assigned, and let clerks continue processing the queue without losing speed or control.

The manual SMS trial is strong evidence that the alert problem is real: six warehouses used it for two cycles, and three made a payment commitment. It does **not** yet prove that the web notification flow works in released use or that changing the queue cards is safe for 600 experienced clerks. The smallest complete release is therefore the working notification path—exception created, notification delivered, supervisor opens and acknowledges it, work is assigned and resolved—with the existing email process, legacy card layout, and keyboard shortcuts available as fallback.

Defer the six-week rules-engine rewrite; use the current rules or a small, auditable manual configuration for this release. Also defer the broad campaign and the mandatory all-user launch. At day 14, the credible commitment is a bounded paid-pilot release if the readiness gate passes, not exposure of all 600 clerks.

Assumptions to record and confirm by day 2: alerts contain operational inventory data but no regulated or highly sensitive data; warehouse administrators may authorize pilot participation; and prior SMS/email logs can establish baseline acknowledgment and resolution times. Minimum authorization, privacy, security, and data-integrity checks remain release blockers even though workflow errors are reversible.

## Evidence and precommitted thresholds

Use the old email workflow as the concurrent fallback and comparison. Within each participating warehouse, phase the new flow by matched shift or supervisor group while the other group remains email-only, then cross over only after review. Stratify results by warehouse, shift, supervisor, and clerk experience so a favorable site mix or training effect does not masquerade as product impact.

By day 2, replace the proposed numeric thresholds below with stricter values if contracts, existing SLAs, or the two-cycle baseline require them; do not relax them after seeing pilot results.

- Core-path readiness: 100% of synthetic and replayed urgent events produce the correct notification and audit record; no event is lost, duplicated, or routed to an unauthorized user.
- Supervisor outcome: at least 90% of urgent exceptions are acknowledged within 10 minutes, and median time to acknowledgment improves by at least 25% versus the concurrent email comparison.
- Operational outcome: the share resolved within the existing warehouse SLA improves by at least 10 percentage points, with no increase in incorrect assignment, duplicate work, or reopened counts.
- Clerk compatibility: every existing documented shortcut works on the legacy layout; in representative queue tasks, experienced clerks' median completion time and error rate are no more than 5% worse in the new layout than in the old one.
- Reliability and adoption: at least 99% notification delivery, fewer than 5 workflow-related support contacts per 100 exposed users per week, and no warehouse abandoning the flow after first use.

Pause new exposure immediately for a lost or misrouted urgent event, unauthorized disclosure, a blocking shortcut regression, or notification delivery below 99%. Roll the affected cohort back to the old layout and email path if acknowledgment is more than 10% worse than its comparison for one full shift, if queue errors exceed the 5% guardrail, or if support cannot restore normal work within 30 minutes. Preserve event logs and record the reason for every pause.

## Calendar plan

**Days 1–3 — Freeze the release record.** The shipping lead names cohorts, comparison groups, review dates, thresholds, and rollback authority. Engineering maps the complete path and instruments notification created/delivered/opened/acknowledged/assigned/resolved, queue task time, shortcut use, errors, fallback use, and support incidents. Confirm site authorization and identify one supervisor and one operations contact per pilot warehouse. Publish a simple daily dashboard; launch completion and user sentiment are not success metrics.

**Days 4–7 — Make the narrow path release-ready.** Put notifications, the card redesign, and cohort assignment behind separate server-side flags so the alert can be tested without forcing the new cards. Keep the legacy route addressable and preserve interruption recovery. Run automated core-path, permissions, delivery, audit, and rollback tests. Test all documented shortcuts and the most frequent queue tasks with 8–12 representative experienced clerks across at least two warehouses. Fix blocking compatibility issues; do not add rules-engine scope.

**Days 8–10 — Rehearse operations.** Replay anonymized prior exceptions in a non-production or shadow mode, verify routing with supervisors, and perform a timed rollback drill. Train site contacts and support on a one-page runbook covering acknowledgment, fallback, escalation, and how to report a broken shortcut. Give exposed clerks a brief in-product explanation and an immediate “use old queue” control. The day-10 go/no-go review requires every core-path and compatibility readiness threshold to pass.

**Days 11–14 — First paid-pilot exposure.** Enable notifications for one matched supervisor group on one shift in two of the three paid-pilot warehouses. Initially leave all clerks on the legacy cards; introduce the redesigned cards to a small group of experienced clerks only after two clean shifts. Engineering and support monitor the first hour of each shift and review the dashboard daily. If the pause rule fires, stop exposure and fall back without waiting for day 14.

**Days 15–17 — First calendar review.** Compare real acknowledgment, resolution, routing, clerk performance, repeated use, support, and fallback data with the holdback. Interview only to explain observed behavior—for example, novelty, training, migration, or interruption—not to substitute approval for outcomes. Expand only if outcome thresholds and every guardrail pass.

**Days 18–24 — Controlled expansion.** If the gate passes, add the remaining paid-pilot warehouse and additional shifts, no more than doubling exposed users at a review. Cross over the original matched groups so site and shift effects can be checked. Growth may own pilot activation, retention follow-up, and recruiting from the already validated warehouse segment, but may not run a broad campaign or set exposure. Keep email and the legacy queue live throughout.

**Days 25–29 — Confirm repeatability.** If two reviews pass, invite the other three previously validated warehouses into the same staged process. Do not automatically include all 600 clerks. Re-run compatibility checks with less frequent but business-critical shortcuts, review differences between new and experienced users, and document support load and migration needs. Prepare the day-30 decision from the predefined evidence window rather than from launch pressure.

**Day 30 — Decide and hand off.** Make one explicit decision:

- If all outcome and guardrail thresholds pass across at least three warehouses and two cycles or the shortest trustworthy operational interval available, continue staged rollout. Shipping retains exposure control; growth owns segment activation and retention; engineering may then propose rules-engine work against demonstrated bottlenecks.
- If the alert outcome passes but clerk compatibility fails, keep notifications on the legacy cards, roll back the redesign, and give engineering the smallest discriminating compatibility fix. Re-test with experienced clerks before more exposure.
- If results differ by warehouse, shift, training, or experience, hold exposure and run the smallest matched test that isolates that factor.
- If acknowledgment or resolution does not improve despite reliable delivery, stop scaling and return the named uncertainty—channel, timing, or supervisor workflow—to learning for a focused test.
- If a pause trigger or minimum safeguard fails, roll back to email and the legacy queue, assign remediation to engineering, and require a fresh readiness review.

## Ownership

The shipping lead is the single owner of the release record, visible artifact, cohort flags, calendar reviews, exposure changes, and rollback decision. The engineering lead owns implementation, instrumentation, test coverage, migration machinery, and technical rollback. A warehouse operations lead owns site authorization, training, shift coordination, and validation that work recovered after fallback. The support lead owns the runbook, live coverage, ticket classification, and the 30-minute recovery escalation. The data/learning owner locks the comparison and thresholds before exposure and interprets confounders. Growth owns activation and retention only after a cohort passes the released-workflow gate. The CEO receives the day-14 and day-30 evidence reviews but does not override a recorded safety, compatibility, or rollback gate.
