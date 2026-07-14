# Raw forward output
Case ID: scenario-03
Reviewer ID: shipping-forward-001

The primary workflow is **engineering for leverage**. The shared internal syntax tree, module boundaries, tests, and migration machinery are internal technology intended to reduce defects and lower the cost of future work; they do not yet constitute product shipping because no user-visible artifact or exposure changes.

Ownership transfers to product shipping at the event where the work becomes a user-affecting release decision—for example, a parser migration changes shipped behavior or compatibility, enters a release artifact, requires user migration, or is exposed to a cohort. Engineering for leverage continues to own the internal architecture and migration machinery, while shipping owns the scope, staged exposure, monitoring, fallback, and user-visible rollout. A future feature merely becoming easier to build is not itself that transfer event.
