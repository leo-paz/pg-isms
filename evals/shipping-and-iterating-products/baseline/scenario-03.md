# Raw baseline output

Case ID: scenario-03
Reviewer ID: shipping-baseline-001

The primary workflow is engineering maintenance and architecture, owned by the engineering team rather than product shipping. The work should be justified and reviewed through technical outcomes: behavioral parity, tests, simpler module boundaries, reduced duplication, migration risk, and whether it actually makes subsequent changes safer or cheaper.

Ownership transfers to product shipping when the shared syntax tree becomes part of a user-visible capability or changes a release artifact, compatibility contract, performance characteristic, migration requirement, or rollout decision that affects customers. At that point the work needs a product-defined outcome, release scope, customer-impact assessment, and shipping plan; until then, product can supply context but should not manage the refactor as a product launch.
