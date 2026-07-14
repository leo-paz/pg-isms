# Raw evaluation output

Case ID: scenario-02

Reviewer ID: engineering-forward-001

## Decision

Extract the proven retry/idempotency/audit protocol as a narrow internal primitive while delivering the third connector. Keep authentication, wire formats, response interpretation, settlement, and reconciliation concrete in each provider adapter. Do not pause delivery for a universal plugin framework, and write no code for the fourth provider until it is a committed integration with known requirements.

The evidence supports one abstraction, not a platform: two live connectors have shared stable semantics for nine months, and a third confirmed connector needs them. It does not support hooks for every imaginable provider. The third provider's differing authentication and settlement behavior is evidence that those details are outside the shared core.

## Boundary and migration

Define the common protocol in product vocabulary:

- a billing operation with a durable idempotency key;
- explicit attempt and terminal-result states;
- retry eligibility and scheduling based on a small normalized failure classification;
- an append-only audit record for every decision and provider response; and
- a provider-independent result passed back to the billing workflow.

Each adapter should own credential use, request construction, provider calls, mapping provider-specific responses into the small failure/result vocabulary, settlement behavior, and reconciliation. If the third provider cannot express a behavior without provider-name conditionals in the core, leave that behavior in the adapter; do not enlarge the “universal” model to make the diagram look uniform.

Before extraction, capture the two current connectors' invariants in conformance tests: the same idempotency key cannot create a second billing effect, retryable and terminal failures transition correctly, every attempt is auditable, and interruption can resume without losing the result. Add provider-specific contract tests for authentication and settlement. Introduce the shared primitive behind one existing connector, compare audit/state transitions, then migrate the second and implement the third. Keep the old path available per connector until production comparison shows equivalent behavior. The billing connector owner must be able to test, deploy, observe, recover, and change the end-to-end operation; incident responsibility cannot stop at the shared library boundary.

Explicitly reject, for now, a plugin registry, a configuration language, generic lifecycle hooks, dynamic loading, and extension points for hypothetical settlement models. Those add concepts and call sites without removing demonstrated duplication or coordination cost.

## Evidence and review

Record the current connector lead time, duplicated protocol code, provider-specific branches, defects, handoffs, and incident recovery time before the change. Review on 2026-11-30 or after the third connector has completed 60 days of production traffic, whichever is later.

Keep the shared primitive if it reduces duplicated protocol logic and connector delivery or defect cost without increasing cross-provider coordination, adapter workarounds, call-site complexity, or incident ambiguity. Revisit a broader framework only when at least three live connectors reveal additional repeated, stable vocabulary and another confirmed connector would materially benefit from it. A sales possibility is not that evidence.

Retreat by moving behavior back into concrete adapters if exceptions, provider-name branches, coordinated releases, or debugging time rise. The preserved option is cheap duplication at the edges; the switch condition is observed stable repetition, not the number of possible providers in a sales deck.
