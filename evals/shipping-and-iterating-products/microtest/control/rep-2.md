# 30-day plan

## Decision and operating constraints

Ship the smallest reliable notification flow now, but do not make the changed queue mandatory for all 600 clerks in two weeks. The manual SMS use and three paid pilots validate the problem and willingness to pay; they do not yet prove that the new card layout is safe for a keyboard-dependent workforce.

For this month:

- Keep the existing rules and defer the six-week rules-engine rewrite. Add only the rules needed for the validated urgent exceptions.
- Put the new flow behind warehouse- and user-level flags, with the email process and old queue available as fallbacks.
- Preserve existing shortcuts and card order where possible. Where parity is not possible, make the difference explicit and test it before expansion.
- Limit growth to pilot enablement and proof collection. Do not run a broad campaign until the product reliably produces the promised outcome.
- Pre-agree rollout gates and stop conditions with the CEO. If the gates fail, pausing is execution of the launch plan, not a new debate.

## Days 1–5: Baseline, scope, and ownership

The product lead is the single launch DRI and publishes a one-page brief covering the target user, urgent-exception definition, release cohorts, measures, and gates. The engineering lead owns delivery and reliability; design/research owns keyboard workflow testing; one operations champion at each warehouse owns training and incident escalation; data owns the scorecard; support owns intake and daily issue summaries. Growth prepares pilot communications but has no authority to expand the audience. The CEO is the accountable executive for accepting or changing the agreed gates.

Capture a baseline from the current email/manual process at all six warehouses:

- urgent exceptions created, acknowledged, and resolved;
- median and 90th-percentile time to acknowledgement and resolution;
- exceptions missed or first seen after the operational deadline;
- clerk task time, correction rate, and shortcut usage in the existing queue;
- support incidents and supervisor escalations.

Interview or observe 8–12 clerks across the six warehouses, including highly experienced users. Run keyboard-only tests on the new queue. Define launch gates before modifying more product surface:

- no critical keyboard trap or inaccessible action;
- at least 99% of eligible urgent alerts delivered, with auditability;
- no increase in missed urgent exceptions;
- no material regression in clerk task time or error rate;
- fallback works in a drill and can be activated by the engineering lead without a deploy.

## Days 6–10: Finish the narrow product

Engineering completes only the end-to-end path: detect the already-validated exception types, notify the correct supervisor, deep-link to the relevant work, record delivery and acknowledgement, and expose a small audit trail. Add monitoring, deduplication, retry behavior, feature flags, and the email fallback. Do not build a general rules engine.

Design and engineering restore shortcut and layout parity for the highest-frequency queue actions. If full parity cannot fit, retain the old queue as the default working surface and let the notification deep-link there. Data instruments exposure, delivery, acknowledgement, resolution, fallback use, task duration, errors, and user/warehouse cohort. Support documents severity levels, the rollback path, and a response owner for every launch day.

## Days 11–14: Shadow and paid-pilot release

Run the alerts in shadow mode for two working days at the three paid-pilot warehouses: generate and log notifications without making them the sole operational signal. Compare them with the manual SMS/email record to find false negatives, false positives, duplicates, and routing errors.

If the delivery, accuracy, fallback, and keyboard gates pass, enable the working flow for supervisors and a small representative clerk cohort at those warehouses. Keep email on. Train users in a 15-minute session and give them an immediate feedback route. The launch DRI and engineering lead review telemetry and incidents daily. Any missed critical alert, incorrect destructive action, repeated duplicate alert, or severe workflow regression triggers immediate fallback and diagnosis.

This is the credible two-week launch: real paying customers use the product in production, but the entire workforce is not forced through an unproven layout.

## Days 15–21: Iterate and expand deliberately

Fix the highest-impact observed failures in short increments. Avoid adjacent features unless evidence shows they block acknowledgement or resolution. Run five brief clerk observations and supervisor interviews, then compare behavioral data with what users say.

After three consecutive working days above the gates, expand within the paid-pilot warehouses in steps such as 25%, 50%, then 100% of eligible users. Hold each step long enough to cover a normal shift pattern. If results remain healthy, invite the other three warehouses that used the manual service into a flagged rollout; start them in shadow mode, then enable a small cohort. Do not add unvalidated warehouses merely to increase the launch count.

Growth may publish targeted onboarding and a pilot case-study draft, but external claims must match measured outcomes. Sales can offer the same bounded paid pilot with explicit scope and fallback; it should not promise the future rules engine.

## Days 22–30: Decide from evidence

Data publishes a cohort scorecard against the baseline, split by warehouse, role, shift, and experience level. The primary outcome is the rate of urgent exceptions acknowledged within the operational target. Guardrails are missed exceptions, time to resolution, alert accuracy and delivery, clerk task time and error rate, support burden, and fallback usage. Commercial evidence includes paid-pilot activation, continued weekly use, willingness to renew or convert, and objections from the other three warehouses.

On day 27, the product lead runs a decision review with engineering, design, operations, support, data, growth, and the CEO. The decision is one of:

1. Expand if the outcome improves and all guardrails hold across shifts and experience levels.
2. Hold the cohort and iterate if value is visible but a fixable workflow or reliability issue remains.
3. Roll back to email/old queue if missed exceptions or clerk errors worsen.

By day 30, publish the decision, evidence, unresolved risks, and next owner. Only after safe usage is demonstrated should the team schedule broader mandatory migration, accompanied by shortcut parity, training, staged warehouse waves, and an end date for the fallback. Fund a rules-engine rewrite only when multiple real customers require rule variation that the narrow implementation cannot support; scope it from those observed cases rather than making it a prerequisite for learning.
