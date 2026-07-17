# Forward review

Reviewer ID: calibration-forward-generator-001

The forward run scores 14/25 (`0.56`), improving on the `0.28` baseline by `0.28`. The improvement is material. Primary routing is correct in all five cases, and the high-harm cases preserve conservative gates, so no routing or safety regression is present; `forward_valid` is therefore `true`.

## Gaps

- `scenario-01`: explicitly gate a partner announcement, attach delay costs to the dated branches, and use exact specialist workflow handoffs in every branch.
- `scenario-02`: commit to an observation window and rollback threshold, then express observable expand, hold, adapt, and rollback branches.
- `scenario-03`: add the missing `designing-business-models` handoff; assign owners and dates to verifications; compare move/remain/temporary-presence/no-raise options; and return dated action/no-action branches with falsifiers, delay costs, preserved options, and a claim-retirement rule.
- `scenario-04`: wire the three named partners' adoption outcomes into the branches and state the resulting source-credibility update; include a true pivot branch if its gate passes.
- `scenario-05`: add explicit later financing routing and qualified legal evidence to the specialist gate.

The repeated failure pattern is incomplete output contracts: the reasoning is often calibrated, but required owners, dates, named branches, or switch effects remain implicit or absent. Tightening the response shape would recover most missed bits without adding much prose.
