# Raw forward output
Case ID: scenario-04
Reviewer ID: shipping-forward-001

## Release decision

Do not perform a mandatory overnight replacement. This is a redesign of a high-frequency installed workflow used by 900 hospital dispatchers, so learned shortcuts, interruption recovery, compatibility, training cost, and safe migration are product requirements. The cleaner appearance is informed taste, not release evidence; complaints alone are also not a veto. The conflict should be resolved with representative behavior and operational outcomes.

The current evidence suggests a segment effect: new hires complete mock tasks faster, while experienced dispatchers lose fluency and recover from interruptions more slowly. The next uncertainty is whether the experienced-user deficit is temporary novelty/training cost, a missing keyboard-compatibility requirement, or a durable regression in real work.

## Prepare a reversible redesign

Keep the old queue available and put the card layout behind per-user or per-site staged access. Preserve existing keyboard shortcuts wherever their meaning remains valid; where a shortcut must change, provide an explicit compatibility map and in-product reminder. Instrument both versions consistently. Provide a short practice environment, a one-page shortcut guide, floor support for launch shifts, and a visible way to switch back without losing queue state.

Before live exposure, verify that the redesign preserves assignment state, priority, patient and destination accuracy, permissions, audit history, accessibility, and performance at peak load. Hospital operations/safety and privacy/security owners must approve the staged protocol and incident response. Name a product release owner, a clinical/operations safety owner, a support lead, and a rollback operator.

## Cohorts and comparison

Establish a one-week baseline on the current queue. Then run a two-week opt-in or scheduled crossover at a small number of representative sites and shifts: include new hires, experienced dispatchers, high-volume periods, overnight shifts, and interruption-heavy roles. Compare each segment against its own baseline and, where operations permit, rotate trained users between old and new versions to separate layout effects from site and shift effects.

Measure real work rather than preference alone:

- time from request arrival to correct assignment and completion;
- wrong assignment, missed priority, duplicate action, and correction rates;
- keyboard versus pointer paths and failed shortcut attempts;
- interruption-recovery time and abandoned or reopened work;
- queue throughput and backlog by shift and experience level;
- fallback use, support requests, training completion, and repeated voluntary use;
- any delayed transport, clinical escalation, privacy issue, or other harm.

Collect brief structured reports after shifts to explain observed behavior, but do not substitute satisfaction scores for operational evidence. Check confounders such as training exposure, novelty, shift mix, case complexity, local configuration, and workstation performance.

## Precommitted decision rules

The exact clinical limits must be set with hospital operations before exposure. Proposed product thresholds, labeled assumptions, are:

- **Expand:** after training, neither experience segment is worse than its baseline on errors, priority handling, or interruption recovery; task time improves or is equivalent for experienced dispatchers and improves for new hires; there is no transport harm; and support demand is declining by the end of the two-week window.
- **Make the smallest discriminating change:** experienced users remain slower but failed shortcut attempts account for the gap. Restore compatibility or change the narrow interaction, retrain, and repeat the same comparison before expanding.
- **Hold/redesign:** the deficit persists after shortcut compatibility and adequate training, or the card layout increases interruption loss, backlog, or correction rates. Keep the old queue as default while redesigning the affected path.
- **Pause/rollback immediately:** any credible delayed patient transport, missed urgent priority, wrong patient/destination caused by the redesign, lost queue state, privacy breach, or inability to restore the old view safely. Stop new exposure, revert affected sites, and run the hospital incident process.

Review at the end of each pilot week. Expand by site or shift, not all 900 users at once, and keep fallback through at least one stable full operating cycle after the last cohort migrates. Retire the old queue only when both new and experienced segments meet the agreed operational and safety thresholds and rollback is no longer being exercised. If the evidence remains segmented, support segment-specific rollout or interaction modes rather than declaring either aesthetic taste or vocal resistance the winner.
