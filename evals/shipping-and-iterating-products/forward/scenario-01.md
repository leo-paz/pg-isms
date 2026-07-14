# Raw forward output
Case ID: scenario-01
Reviewer ID: shipping-forward-001

## Release decision

Release the core workflow next week to the eight crews that have agreed to try it, with room to add the other two crews only after the first cohort is stable. Do not hold the release for avatars, themes, advanced permissions, or polished analytics: none enables the complete job of creating a shoot, assigning and acknowledging a handoff, and seeing what is blocked, and none materially lowers the stated release risk.

This is a bounded first release of a working task-handoff tool for independent film crews. The target outcome is that a crew can move one real handoff from assignment to acknowledgement and detect blockers without losing work. The existing spreadsheet is the principal rival and also the fallback. Evidence so far is that the core path works and eight crews are willing to try it; actual repeated use in production is still unknown.

## Pre-release gate and scope

Before opening access, run end-to-end tests of create shoot → assign handoff → acknowledge → blocked view, including duplicate actions, a disconnected client, and recovery from a failed save. Verify minimum authorization, security, privacy, and data-integrity safeguards; these are not optional even though the operational mistakes are reversible. Confirm that each crew sees only its own shoots and that exports or copies needed for spreadsheet fallback work. Name one release owner and one support owner from the four-person team.

Ship only:

- shoot creation and the four-step handoff path;
- a simple roster/role model sufficient for the pilot;
- basic activity logging and error instrumentation;
- a visible way to report a problem and export or copy current handoffs.

Defer avatars, themes, advanced permissions, and the polished analytics page. If a crew genuinely requires a permission boundary to use the product safely, add the narrow boundary needed for that crew rather than the proposed general permissions system.

## Rollout and evidence loop

On Monday, onboard two crews with a 30-minute walkthrough and written fallback instructions. If no core-path data loss, cross-crew exposure, or unrecoverable blockage occurs in their first two operating days, add the other six crews in two groups of three. Consider crews nine and ten only at the first weekly review. Keep the spreadsheet available throughout the pilot; crews should know when and how to return to it, and the team should not force a one-way migration.

The release owner reviews telemetry and support reports daily during week one and on a fixed weekly calendar thereafter. Track real handoffs created, assignment-to-acknowledgement completion, time to acknowledgement, blockers found and cleared, abandoned handoffs, repeated use by crew, core-path errors, data corrections, spreadsheet fallback, and support load. Do not use sign-ups, compliments, or launch completion as the success measure.

Proposed thresholds, explicitly assumptions to confirm with the crews before launch:

- **Pass/expand:** at least six of eight crews complete the core path on two separate shoot days within two weeks; at least 80% of assigned handoffs are acknowledged or deliberately closed; no cross-crew exposure or data loss; and support remains manageable by the named owner.
- **Change and retest:** crews attempt the job but abandon a repeatable step, acknowledgement is below 80%, or spreadsheet fallback is frequent for one identifiable cause. Make the smallest change that discriminates among usability, missing workflow, training, and reliability, then rerun the same cohort.
- **Pause/rollback:** any cross-crew access, lost handoff state, unrecoverable core-path failure, or more than two crews unable to complete the path in a working day. Stop new exposure and direct affected crews to the spreadsheet until repaired and verified.
- **Stop or return to learning:** after two shoot cycles, crews do not perform the handoff job in the tool even when the path is reliable. Return the named uncertainty—whether this workflow is valuable enough to replace the spreadsheet—to learning rather than adding cosmetic features.

At the two-week review, expand toward ten crews only on a pass. Otherwise make one discriminating change, hold the cohort, or roll back. The next iteration should be driven by observed workflow failure or repeated use, not by the six-week polish list.
