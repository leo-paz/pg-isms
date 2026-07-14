# 30-day plan

## Decision and scope

Treat the three paid pilots as the launch, not as permission for a universal rollout. Ship the already-working notification flow for the one validated problem—urgent cycle-count exceptions—behind warehouse and user feature flags. Keep email running as a fallback during the 30 days. Defer the six-week rules-engine rewrite until usage shows that rule complexity is actually blocking the product, and defer the broad campaign until the pilots produce credible operational evidence.

The card-layout change is the main adoption risk. Before expanding, preserve the existing queue's shortcut mappings, focus order, information density, and common action sequence. New notification cues can be added without forcing 600 experienced clerks to relearn their core workflow at once.

## Days 1–5: establish the release contract

- The product lead owns one written release brief covering the target exception type, excluded use cases, cohort sequence, success thresholds, and stop conditions. The engineering lead signs off on reliability and rollback.
- Use the prior two manual-SMS cycles and old email data to establish per-warehouse and per-shift baselines: alert-to-acknowledgment time, acknowledgment-to-resolution time, exceptions still unacknowledged at the operational deadline, duplicate work, corrections, and queue throughput.
- Instrument the web flow end to end: alert created, delivered, viewed, acknowledged, assigned, resolved, reopened, and reverted. Record delivery channel and cohort so web, SMS, and email outcomes can be compared.
- Observe 10–15 clerks across shifts performing the highest-frequency queue tasks. Document the shortcut and focus-order contract, then add automated coverage for it. A layout is not release-ready merely because its clicks work.
- Name one warehouse champion and one backup at each paid pilot. Give them a one-page change guide, escalation path, and authority to pause their warehouse's rollout.

## Days 6–10: harden the smallest useful product

- Fix shortcut, focus, and screen-density regressions in the current flow; do not broaden the feature set.
- Add warehouse/user feature flags, audit logs, deduplication, delivery-health monitoring, and a tested one-step rollback to the old queue/email process.
- Run the web flow in shadow mode at the three paid pilots: generate and log the same alerts without making the new flow the clerk's source of truth. Compare routing and timing with email and the manual service, and fix mismatches.
- Use simple, explicit configuration for the already-validated alert rules. Keep a log of requested rule changes; that log, rather than architectural preference, will determine whether a rules engine is justified later.
- Conduct a release rehearsal with each warehouse champion and the support/on-call owner. No cohort starts until fallback, auditability, and notification delivery have been demonstrated.

## Days 11–16: controlled live release

- Start with 5–10 volunteer clerks per shift at one paid pilot, while email continues in parallel. Avoid managers selecting only unusually enthusiastic or expert users.
- After two stable operating days, add similarly sized cohorts at the other two paid pilots. Hold brief daily reviews with the champion, product lead, engineering lead, and analyst.
- Fix blocking workflow issues within the flag-protected cohort. Revert affected users immediately if the new layout impairs shortcut use or creates missed or duplicate work.
- Do direct, factual pilot communication only. Growth may prepare onboarding and interview material, but does not run a broad acquisition campaign.

## Days 17–23: expand only on evidence

Expand to roughly half, then all willing clerks at each paid pilot only after that warehouse has completed at least one representative operating week and passed the agreed gate:

- no critical delivery, data-integrity, or missed-alert incident attributable to the new flow;
- at least a 20% improvement in p90 alert-to-acknowledgment time versus its baseline;
- no increase in urgent exceptions left unresolved at the operational deadline;
- queue throughput no worse than 5% below baseline after accounting for volume and shift mix; and
- no material deterioration in keyboard task completion, duplicate handling, corrections, or support burden.

Sample size and raw counts accompany percentages. If event volume is too low, keep the cohort running rather than declaring a win. Pause a cohort for any system-caused missed urgent alert, data-integrity issue, repeated duplicate work, or throughput drop above 10%. Because rollback is cheap, use it promptly and investigate before resuming.

If the three paid pilots pass, invite—not mandate—the other three validation warehouses into the flagged rollout. Their inclusion tests transferability without exposing all 600 clerks.

## Days 24–30: decide the next increment

- Analyze outcomes by warehouse, shift, tenure, and cohort, not just in aggregate. Pair event data with short interviews of active users, reluctant users, and warehouse supervisors.
- Document which rule changes were requested, how often they occurred, and whether the simple configuration delayed delivery or caused errors. Approve a rules-engine investment only if repeated, valuable changes cannot be handled safely by the thin configuration.
- Produce a decision memo with one of three outcomes: expand to the next named cohort, hold and fix a specific problem, or stop and return to email. A successful pilot authorizes the next bounded cohort, not an automatic launch to everyone.
- Keep email available until at least two successive release cohorts meet the gates and warehouse leaders confirm that rollback is no longer operationally necessary.
- Growth may turn verified pilot results into a narrow case study and recruitment message for the next cohort. A broad campaign and mandatory rollout remain out of scope until the product performs reliably across different warehouses and experienced clerks can retain their established workflow.

## Evidence and ownership

The primary outcome is faster, more reliable handling of urgent exceptions: p50/p90 time to acknowledge, time to resolve, and the share missed by the operational deadline. Guardrails are incorrect routing, duplicates, reversals, queue throughput, shortcut-task completion, support contacts, and severe incidents. Adoption—activation, repeated use, and opt-out—is diagnostic, not a substitute for operational improvement. Commercial evidence is pilot continuation, expansion requests, and willingness to renew after observed use.

The product lead is the single DRI for scope, sequencing, the daily decision log, and go/no-go recommendations. The engineering lead owns delivery correctness, observability, on-call response, and rollback. The analyst owns baseline integrity and cohort reporting. Design/research owns shortcut compatibility and clerk observation. Each warehouse champion owns local training and can stop the rollout. Customer success owns pilot communication and issue intake. Growth owns only evidence-backed pilot materials during this period. The CEO approves the 30-day release envelope and receives twice-weekly updates; product and engineering jointly advance gates, and either engineering or the warehouse champion can halt a cohort on a stop condition.
