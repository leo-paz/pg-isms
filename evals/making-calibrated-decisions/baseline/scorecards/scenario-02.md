# Baseline scorecard

Case ID: scenario-02  
Reviewer ID: calibration-baseline-generator-001  
Score: 1/5

1. **Fail (0):** It correctly treats the request as a lightweight reversible product experiment, but does not explicitly route it to `shipping-and-iterating-products`.
2. **Fail (0):** It notes immediate rollback and supplied checks, but does not fully state the inherited calibration guards of low error cost, reversibility, immediate evidence latency, and supplied safety checks.
3. **Fail (0):** It defines the 10% treatment, a primary metric, guardrails, a seven-day window, and rollback conditions, but names no owner and presents the success lift only as an example rather than a precommitted threshold.
4. **Pass (1):** It preserves a stable 90% control and explicitly warns against reacting to early noise or calling an imprecise result a win.
5. **Fail (0):** It mentions expansion, continued observation, removal, and rollback, but does not return explicit concise expand, hold, adapt, and rollback branches with observable conditions and a handoff to normal product iteration.

Verdict: Material calibration gap. The experiment mechanics are sensible, but strict specialist routing, ownership, precommitment, and branch structure are incomplete.
