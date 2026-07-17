# Tooltip rollout plan

**Primary workflow:** run a lightweight, reversible product experiment. This does not require a cross-domain strategic decision process because the decision to experiment is already made, the change has passed normal checks, and rollback is immediate.

## Sequence

1. Confirm event instrumentation and exclude employees, bots, and users who cannot see the relevant feature.
2. Randomly assign eligible free-trial users to 10% treatment and 90% control, keeping assignment stable per user.
3. Run a brief smoke check after the first 50–100 eligible treatment exposures to confirm rendering, event delivery, and no obvious support or accessibility regressions.
4. Continue the 10% rollout for seven days, or until the preselected sample requirement is reached, so weekday mix is represented.
5. At the end of the window, compare the prespecified outcome and guardrails. Either roll back, continue collecting data, or expand in one or two stages.

## Metric

**Primary success metric:** the proportion of eligible trial users who complete the action explained by the tooltip within 24 hours of first exposure, measured treatment versus control.

Set a minimum worthwhile lift before looking at results—for example, a 10% relative improvement—then use the team’s normal statistical method or confidence interval. Do not substitute tooltip clicks for the intended user outcome.

**Guardrails:** trial activation rate, tooltip dismissal/complaint rate, client errors, page performance, and accessibility or support reports.

## Monitoring and rollback

- Monitor technical health immediately after launch, again after the smoke-check cohort, and daily during the seven-day window.
- Roll back immediately for a reproducible blocking UI/accessibility issue, a material increase in client errors, or evidence the tooltip prevents the underlying action.
- For a quantitative threshold, roll back if any core guardrail is worse by more than 5% relative and the effect persists after basic instrumentation checks. If the primary metric is flat or negative without a safety issue, finish the planned window, then remove the tooltip rather than reacting to early noise.
- If results are positive but imprecise, keep exposure at 10% until the sample is sufficient; do not call an inconclusive result a win.

Case ID: scenario-02
Reviewer ID: calibration-baseline-generator-001
