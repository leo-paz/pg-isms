# Forward scorecard

Case ID: scenario-02  
Reviewer ID: calibration-forward-generator-001  
Score: 3/5

- Bit 1 — PASS (1): Routes the routine reversible experiment to `shipping-and-iterating-products`, not the cross-domain workflow.
- Bit 2 — PASS (1): Keeps calibration to inherited guards and explicitly covers bounded error exposure, immediate rollback, short evidence latency, passed QA/accessibility checks, and lack of cross-domain risk.
- Bit 3 — FAIL (0): Defines allocation, metric, guardrails, and ownership, but leaves both the observation window and material-regression threshold to be specified later instead of precommitting them in the plan.
- Bit 4 — PASS (1): Retains a 90% control and warns against early stopping on noise before the fixed horizon.
- Bit 5 — FAIL (0): The response is concise but does not return explicit observable expand, hold, adapt, and rollback branches; it only says to ship, revise, or end after the horizon.

Verdict: Correct routing and experiment skeleton, but incomplete as the compact branch plan requested.
