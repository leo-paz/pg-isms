# 30-day release record

## Decision and scope

Ship a staged release of the web notification flow, not a mandatory all-user launch. The six-warehouse SMS test over two monthly cycles validates the urgent-exception problem, and three paid pilots validate willingness to pay in this segment. It does **not** yet show that the web flow improves exception handling or that its changed queue layout is safe for experienced clerks.

The smallest complete outcome is: an urgent cycle-count exception is visibly delivered, a supervisor can acknowledge it, and a clerk can open and act on it without losing the existing queue's keyboard-driven workflow. Keep email available as fallback. Treat the current email process and the manual SMS results as comparisons.

Defer the six-week rules-engine rewrite; the working notification path does not need it to answer the release question. Also defer a broad campaign and a compulsory launch until released-workflow evidence clears the gate. Minimum access control, data integrity, privacy, and audit logging are not deferrable.

## Days 1-7: make the working flow releasable

The shipping owner writes and signs the release record on day 1, including the cohorts, metrics, thresholds, pause rule, support rota, and fallback owner. Product/learning owns the unresolved hypothesis and interpretation: *the web flow reduces missed or late urgent exceptions without materially degrading experienced clerks' queue work*.

Engineering should spend the week on the release path rather than the rules rewrite:

- instrument alert creation, delivery, view, acknowledgement, queue open, resolution, abandonment, errors, fallback use, and user/cohort identity;
- put exposure behind warehouse- and user-level flags, with one-command rollback to email-only;
- preserve every existing keyboard shortcut on the changed cards, or add an equivalent compatibility mode before pilot exposure;
- test alert deduplication, ordering, permissions, interruption recovery, and the core acknowledge-to-resolution path; and
- publish an operator dashboard and alerting for delivery failures and client errors.

On days 3-5, observe a representative set of experienced clerks doing real queue tasks in the old and new layouts. Include high-volume and accessibility-dependent shortcut users, not just supervisors or enthusiastic pilot contacts. Record baseline task time, shortcut completion, wrong-card actions, abandonment, and urgent-exception acknowledgement time. Fix core-path and compatibility failures; do not use preference voting to design the cards.

Assumption to confirm on day 1: the web alerts do not introduce a new legal, security, or privacy classification. If they do, the appropriate owner must clear that gate before exposure.

## Days 8-14: bounded paid-pilot release

Release first to the three paid-pilot warehouses, with explicit supervisor participation and a deliberately mixed clerk cohort: roughly 10% of clerks at each site, at least half experienced keyboard users. Keep the remaining users on email as a contemporaneous comparison, stratified by warehouse, role, workload, and exception volume. Email remains active for exposed users during this phase so no urgent item depends on an unproven channel.

Warehouse operations names one local champion per site. Support provides a short shortcut/migration guide, office hours at shift changes, and a staffed escalation route. Engineering owns telemetry, defects, and rollback execution. Shipping owns exposure changes and the day-14 review; no executive, growth, or sales announcement changes the cohort outside that record.

Review daily for harm and operability, but make the evidence decision at the scheduled review. Proposed thresholds are assumptions to precommit with the baseline data by day 7:

- **Pass workflow:** at least 90% of exposed urgent exceptions are acknowledged within the baseline service window, with at least a 25% relative reduction in median time to acknowledgement versus matched email users.
- **Pass migration:** experienced users complete at least 95% of sampled queue tasks with shortcuts, and their median task time is no more than 10% worse than baseline by their third session.
- **Error limit:** wrong-card actions, duplicate acknowledgements, or unrecoverable client errors affect less than 1% of acted-on exceptions; no urgent exception is lost.
- **Operational limit:** web delivery succeeds for at least 99.5% of generated urgent notifications, and fewer than 5% of exposed users require support after their first three sessions.
- **Use signal:** at least 70% of exposed supervisors use the web flow on two or more distinct workdays; measure actual use and resolution, not stated approval.

Pause new exposure immediately for any lost urgent exception, permissions/data leak, sustained delivery below 99%, or a greater than 5% wrong-action rate. Roll back affected users to email-only if the issue is not diagnosed and contained within one shift. The engineering on-call executes rollback; the shipping owner declares the pause; the support lead contacts affected warehouses and confirms recovery.

## Days 15-21: discriminate, then expand one step

At the day-14 gate:

- If all workflow, migration, error, and operational thresholds pass, expand to all consenting supervisors and 25% of clerks in the three paid pilots, then to a small cohort in the other three previously tested warehouses. Keep an email-only comparison and include experienced clerks in every cohort.
- If notification outcomes pass but experienced-clerk migration fails, do not expand. Make the smallest discriminating change—restore the familiar card layout or ship compatibility mode—and rerun the same cohort for one week.
- If delivery or integrity fails, pause and return the machinery problem to engineering. A rules-engine rewrite is justified only if evidence identifies the existing rules implementation as the limiting cause.
- If supervisors do not repeatedly use the web flow despite reliable delivery and workable migration, return the specifically named uncertainty (alert placement, acknowledgement job, or target role) to learning; do not silently pivot or market around it.

Growth may prepare positioning for the already validated regional-warehouse segment and recruit within the controlled release only. It does not start a broad campaign: payment for the manual pilot is not evidence that the released web workflow activates or retains users.

## Days 22-30: one-cycle evidence and decision

Continue only the exposure authorized at day 21. Measure acknowledgement and resolution latency, miss rate, repeated use, queue throughput, error and abandonment rates, fallback use, support load, and any differences by experience level, shift, and warehouse. Check for confounders such as exception volume, staffing, training attendance, duplicate email alerts, and local champion involvement.

Day 30 is a calendar decision, not a launch ceremony:

- **Expand carefully** if the thresholds continue to pass across the paid and unpaid-pilot warehouses, no subgroup is materially harmed, and support load is stable. The next release can increase exposure in steps such as 25%, 50%, then 100%, with the same rollback gate.
- **Revise and repeat** if the core outcome improves but one layout, training, or segment issue remains. Change only what discriminates that cause.
- **Pause or roll back** if error, harm, or migration limits fail.
- **Stop or return a named need uncertainty to learning** if repeated, reliable exposure does not improve urgent-exception handling.

Because the trusted behavior interval is monthly, 30 days yields roughly one released cycle. It can support a next-stage decision, but not a claim of multi-cycle retention or justify forcing all 600 clerks onto the flow. A mandatory all-user launch requires another calendar gate after at least a second successful released cycle.

## Named owners

- **Shipping DRI:** scope, release record, visible artifact, flags/cohorts, exposure decisions, day-14/day-21/day-30 reviews, and coordination of fallback.
- **Product/learning:** hypothesis, sample quality, thresholds, confounders, and interpretation of unresolved user/job questions.
- **Engineering lead/on-call:** core-path quality, shortcut compatibility implementation, instrumentation, delivery machinery, monitoring, rollback, and any later architecture work supported by evidence.
- **Warehouse operations lead plus local champions:** cohort inclusion, shift-aware onboarding, observation access, and local escalation.
- **Support lead:** migration guide, staffed response, issue taxonomy, user contact after incidents, and confirmation that fallback worked.
- **Analytics owner:** baseline, matched comparison, segment cuts, and decision packet before each review.
- **Growth owner:** controlled recruitment and activation only after the released workflow passes; broader channel spend waits for repeat-use evidence.
- **CEO/executive sponsor:** resources and resolution of cross-functional blockers, while the precommitted release and rollback gates—not the two-week date—govern exposure.
