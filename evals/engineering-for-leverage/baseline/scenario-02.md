Case ID: scenario-02
Reviewer ID: engineering-baseline-001

Extract the nine-month stable retry, idempotency, and audit behavior into a small shared connector protocol with a conformance test suite. The common layer should define request identity, retry classification and backoff, duplicate handling, audit events, error reporting, and the lifecycle hooks a connector must implement. Refactor the two existing connectors through it, then use the third connector to verify that the contract is genuinely reusable.

Keep authentication, request and response mapping, provider-specific state, settlement rules, reconciliation, and unusual failure handling concrete inside each connector. Do not pause delivery for a universal plugin framework, and do not design for the speculative fourth provider. A narrow internal interface and test harness preserve leverage without committing to dynamic loading, extension registries, configuration languages, or abstractions for differences that have not appeared.

Revisit the boundary after the third provider is complete and operating, or when another provider is contractually committed. Expand the abstraction only when repeated concrete implementations reveal another stable common behavior, when connector changes cause recurring coordination costs, or when third-party extensibility becomes an actual product requirement.
