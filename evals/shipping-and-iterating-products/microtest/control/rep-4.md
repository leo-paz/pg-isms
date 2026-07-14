# 30-day plan

The goal for the month is not “launch the new flow.” It is to prove that the flow gets urgent exceptions handled faster without damaging the high-volume clerk workflow. The manual-service usage and three paid pilots are enough evidence to ship a narrow productized version, but not enough to force it on all 600 clerks.

## Days 1–5: Freeze scope and establish the baseline

- Make the current web notification flow the release candidate. Do not begin the six-week rules-engine rewrite. Put any missing rule logic behind a small adapter or manually managed configuration so it can be replaced later.
- Keep the existing queue and email process intact. Add a per-warehouse feature flag, an immediate rollback switch, and an audit trail showing which exception produced which notification.
- Define the primary outcome as time from an urgent exception being created to supervisor acknowledgement and resolution. Capture the prior two cycles' median and 90th-percentile times, plus the share that missed the operating SLA.
- Define guardrails: missed or duplicate alerts, incorrect urgency classifications, delivery failures, clerk task-completion time, queue errors, support requests, and successful use of existing keyboard shortcuts.
- Observe 8–12 experienced clerks completing representative queue tasks. Document the shortcut and focus-order contract before changing the card layout. Either preserve it exactly or provide a compatibility layout for this release.
- Agree in writing on rollout gates and stop conditions. Examples: no known shortcut regression; no severe queue defects; at least 95% notification delivery; no increase greater than 5% in clerk task time; and a meaningful improvement in acknowledgement time.

## Days 6–10: Harden the narrow release

Engineering should focus only on release safety and measurement: feature flags, email fallback, notification status, acknowledgement, retry behavior, logging, and dashboards. Add automated checks for every documented shortcut and for keyboard focus across the new cards. Run failure drills for duplicate, delayed, and misclassified notifications, and verify that disabling the flag restores the old workflow immediately.

Design and research should test the candidate with the experienced clerks, including the fastest shortcut users, not only supervisors who requested alerts. Fix workflow regressions before adding polish. Customer success should prepare a one-page pilot guide, a named escalation path, and a 15-minute supervisor onboarding session.

## Days 11–14: Meet the launch date with a controlled pilot

Release to the three paid-pilot warehouses, initially to their supervisors and a small clerk cohort. Run the new notifications alongside email rather than replacing it. For the first 48 hours, review every urgent exception and compare the product's routing with the expected routing. Hold daily 20-minute reviews with each warehouse's supervisor.

This is the two-week launch commitment: a real production release to paying design partners, not a mandatory release to all 600 users. Announce only to the participating accounts. Growth can prepare broader material, but should not run the campaign yet.

Pause or roll back a warehouse if there is a missed urgent alert, a material shortcut regression, an unexplained duplicate rate above 2%, or a sustained clerk task-time regression above the agreed guardrail. Because the old process remains live, rollback is low-cost and should be used quickly.

## Days 15–21: Learn and expand one cohort at a time

Compare each pilot's results with its own baseline and, where practical, keep a staggered holdout group on the old flow for several days. Review quantitative results alongside ten short interviews: supervisors should explain whether alerts changed action, and clerks should demonstrate their normal work rather than merely report satisfaction.

If the day-14 gates pass, add the other three warehouses that used the manual SMS service, one at a time with at least 48 hours between additions. Fix only issues that affect the central outcome or guardrails. Put requests for flexible rule authoring, new channels, and broad layout redesign into a learning backlog. Use observed rule-change frequency and failure modes to decide later whether a rules engine is warranted.

At day 21, publish a short evidence review containing baseline versus current acknowledgement and resolution times, SLA misses, alert quality, workflow guardrails, qualitative findings, and pilot commercial status. Record contrary evidence and missing data, not just favorable anecdotes.

## Days 22–30: Decide, then scale deliberately

If all six warehouses pass the gates, expand by account cohorts at roughly 10%, 25%, and 50%, with a checkpoint after each cohort. Keep the feature optional and keep email fallback through the month. Do not expose the changed cards to the remaining clerks until shortcut parity and task-time guardrails have held under production load.

On day 28, make one explicit decision:

1. **Scale** if acknowledgement/SLA performance improves materially, alert quality is reliable, clerk guardrails hold, and pilots are using the product. Schedule the remaining rollout after day 30 and let growth launch a targeted campaign using verified results.
2. **Iterate** if the outcome improves but a contained workflow or reliability issue remains. Keep the successful cohorts live and run another narrow cycle.
3. **Stop or revert** if alerts do not change response behavior, urgent events are missed, or clerk productivity materially declines. Preserve the evidence and do not justify the rules-engine rewrite on sunk effort.

## Ownership

- **Product lead:** single DRI for scope, rollout gates, daily decisions, and the day-28 scale/iterate/stop recommendation.
- **Engineering lead:** release safety, feature flags, fallback, alert correctness, instrumentation, and rollback execution.
- **Product designer/researcher:** clerk workflow contract, usability sessions, and keyboard/focus acceptance criteria.
- **Data owner:** baseline integrity, dashboards, cohort comparisons, and the day-21 evidence review.
- **Customer success lead:** warehouse onboarding, daily pilot contact, issue intake, and pilot conversion signals.
- **Growth lead:** targeted pilot communications now; broader campaign only after the scale decision and only with substantiated claims.
- **CEO/executive sponsor:** approve the pre-agreed gates and resolve resource conflicts, but not override stop conditions account by account.

The month ends with a safer product in real use, credible evidence about its effect, and a bounded next investment. A rules-engine rewrite, broad campaign, or mandatory launch becomes a consequence of that evidence rather than a prerequisite for collecting it.
