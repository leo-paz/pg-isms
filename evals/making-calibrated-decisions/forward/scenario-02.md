mode: route-away  
primary_skill: shipping-and-iterating-products  
reason: This is a bounded, reversible product-release execution request with no cross-domain or source-calibration decision.

## Inherited guards

- Stage/survival: six-person SaaS team; no funding or runway decision is implicated.
- Reversibility/error cost: immediate rollback; no payment, permission, or data-storage change; exposure is limited to 10% of free-trial users.
- Evidence latency: tooltip behavior can be measured within a short, predefined monitoring window.
- Product/user effects: watch task completion and negative interaction signals; normal accessibility and QA gates have passed.
- Optionality: retain the current experience as the 90% control and rollback target.

## Known facts and unknowns

Known: the team has decided to run the experiment; exposure is capped at 10%; rollback is immediate; normal QA and accessibility checks passed; the change creates no payment, permission, or new-data risk.

Unknown: baseline conversion volume and variance, so a statistically meaningful sample duration cannot be inferred. The product manager should set the fixed horizon from historical traffic before exposure begins and avoid stopping early on noise.

## Compact rollout plan

1. Product manager records the hypothesis, assignment rule, fixed 10% treatment/90% control, primary metric, guardrails, fixed monitoring horizon, and rollback rule before launch.
2. Release to 10% of eligible free-trial users; verify assignment, event delivery, and tooltip rendering immediately.
3. Primary success metric: incremental completion rate of the specific trial action the tooltip is intended to cause, treatment versus control, over the fixed horizon.
4. Monitor for the precommitted window sized from baseline traffic, with an immediate technical check after release and daily checks for guardrails. Guardrails: client errors, support complaints, tooltip dismissal/obstruction, and accessibility regressions.
5. Roll back immediately if a critical accessibility or functional defect appears, or if the treatment causes a predeclared material guardrail regression. Otherwise keep allocation unchanged through the fixed horizon, then ship, revise, or end based on the primary metric and guardrails.

handoff_gate: `shipping-and-iterating-products` owns execution once the product manager has written the metric denominator, minimum meaningful lift, fixed sample/window, and numeric material-regression threshold. If any new payment, permission, data, safety, legal, or survival exposure appears, stop and reroute before expanding.

Case ID: scenario-02
Reviewer ID: calibration-forward-generator-001
