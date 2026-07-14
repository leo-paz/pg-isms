The 30-day objective is to prove that the web flow reduces missed urgent exceptions without slowing the 600 clerks who depend on the existing queue. Do not make the new flow mandatory for everyone in two weeks, fund a six-week rewrite, or begin a broad campaign yet. The paid pilots are strong evidence of demand, but not yet evidence that this particular interface is safe at full scale.

## Product and release decisions

- Ship the smallest useful slice: urgent cycle-count notifications, a clear path back to the affected queue item, acknowledgment status, and escalation when an alert remains unacknowledged. Defer the general rules engine; encode only the few validated rules behind the manual SMS service.
- Preserve the current email path and queue behind feature flags. Rollback must be possible by warehouse and user without a deployment.
- Treat keyboard parity as a launch requirement. Keep existing shortcuts and focus order, and avoid changing unrelated queue-card information. Publish a shortcut map and test with experienced clerks before exposing a live pilot.
- Use growth for pilot recruitment, onboarding, and interviews during these 30 days—not acquisition. Broader messaging waits until retention and workflow safety are demonstrated.

## Days 1–7: baseline, design, and build

The product lead is the single accountable owner and writes a one-page release brief with scope, exclusions, success thresholds, rollback criteria, and a daily decision log. The warehouse-operations lead supplies one supervisor and two experienced clerks from each of the six original warehouses as a working group.

Engineering adds notification delivery, acknowledgment, escalation, feature flags, audit logs, and analytics. It also instruments the old process so the team can compare flows. Design and research map every current shortcut and run task-based sessions with at least 10 experienced clerks using realistic exception queues. Any regression in completing common tasks is fixed before release.

The data owner reconstructs a baseline from the two manual-SMS cycles and recent email-only cycles: number of urgent exceptions, percentage acknowledged within 15 minutes, percentage never acknowledged during the shift, median time to acknowledgment, and time from alert to completed count. Baseline queue completion time, error rate, and support volume as guardrails.

Exit gate for day 7: the critical notification path works end to end; events can be reconciled against source exceptions; all existing shortcuts used in the tested tasks still work; and rollback has been rehearsed in staging.

## Days 8–14: shadow mode, then limited live release

On days 8–10, run the web notifications in shadow mode at two of the paid-pilot warehouses. Supervisors continue receiving the established channel, while the team compares what the web flow would have sent. The engineering lead reviews missed, duplicate, late, and incorrectly routed alerts daily.

If shadow delivery covers at least 99% of eligible alerts, produces no high-severity routing errors, and the rollback drill succeeds, enable the live flow on days 11–14 for those two warehouses. Start with the working-group clerks, then expand within those sites. Keep email active in parallel. An operations owner is on call during every participating shift and can disable the feature immediately.

The CEO receives a day-14 launch, but it is a real paid-pilot launch rather than a mandatory company-wide cutover. The product lead owns this recommendation; the CEO owns any decision to accept risk outside the stated gates and must explicitly record that decision.

## Days 15–21: learn and expand deliberately

Review pilot data and interview supervisors and clerks within 24 hours of each cycle. Segment results by warehouse, shift, tenure, and keyboard-heavy versus pointer-heavy users so an aggregate improvement does not hide harm to experienced clerks.

Expand to the other four original warehouses only if the live cohort meets all of these gates for one full cycle:

- urgent exceptions acknowledged within 15 minutes improve by at least 25% relative to each warehouse's baseline;
- the unacknowledged-by-end-of-shift rate does not worsen and trends downward;
- no alert is silently lost and no incorrect alert causes an irreversible action;
- median time for common queue tasks worsens by no more than 5%, with no material shortcut regression;
- there are no unresolved severity-one incidents and fewer than 5% of users require assisted recovery.

If a guardrail fails, stop expansion, revert the affected cohort to the old path, and spend the remaining week fixing the observed problem. Do not average a failing warehouse into a passing result.

## Days 22–30: confirm repeatability and decide

Run the improved flow for a second cycle across every cohort that passed its gate. Growth prepares case-study material and a narrow waitlist but does not publish claims until the evidence review. Engineering documents the manual rules that caused operational burden; only then should it propose whether a generalized rules engine is justified.

On day 30, the product lead chairs a decision review with the engineering, operations, data, support, growth, and warehouse representatives. There are three possible outcomes:

1. Expand in staged warehouse cohorts if the primary metric improves, all guardrails hold for two cycles, and paid pilots want to continue.
2. Iterate for another cycle if value is visible but usability or reliability is below a gate.
3. Roll back and reassess if acknowledgment does not improve or clerk productivity materially declines.

## Ownership and operating cadence

The product lead owns scope, gates, and the day-30 recommendation. The engineering lead owns delivery correctness, observability, feature flags, and rollback. Design/research owns keyboard workflow validation. The data owner owns baseline integrity and the daily dashboard. Warehouse operations owns shift readiness, training, and incident escalation. Support logs every issue and recovery. Growth owns pilot communications only. Each warehouse supervisor can pause the flow locally.

Run a 15-minute daily pilot review with a shared dashboard and incident log, plus a twice-weekly written update to the CEO. Decisions to expand require product, engineering, and operations sign-off; any one of those owners can halt a cohort for safety or workflow degradation. This gives the team shipping momentum in 30 days while making the next investment depend on observed behavior rather than executive urgency or architectural preference.
