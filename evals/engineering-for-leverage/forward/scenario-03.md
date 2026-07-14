# Raw evaluation output

Case ID: scenario-03

Reviewer ID: engineering-forward-001

The primary workflow is `shipping-and-iterating-products`. The remaining decision is user-visible exposure: release a settled, routine change behind a flag to a bounded cohort, observe whether customers repeatedly use it, monitor the release, and keep rollback/support gates. The existing product/code owner should finish the implementation, tests, flag, telemetry, and technical rollback as part of that workflow.

`engineering-for-leverage` has no separate architecture project here. The stack, data model, module boundaries, and owner are already settled, and no binding structural constraint has been named. It should not reopen those choices, invent an abstraction, or delay exposure for a technical redesign.

Engineering-for-leverage re-enters only if implementation uncovers a specific structural blocker before release—for example, the settled model cannot represent the filter without violating a shared invariant, or the query cannot meet a predeclared reliability/latency threshold. In that event, make the smallest reversible technical change, record the constraint and fallback, and return ownership to shipping. Cohort selection, exposure, measurement of repeated use, monitoring, support, and the release/rollback gate remain with shipping.
