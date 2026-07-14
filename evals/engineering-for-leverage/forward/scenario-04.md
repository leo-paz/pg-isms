# Raw evaluation output

Case ID: scenario-04

Reviewer ID: engineering-forward-001

## Decision

Do not split the monolith into microservices immediately. First replace layer ownership with end-to-end technical ownership inside a modular monolith, using observed co-change, data, and incident patterns to draw boundaries. The current failure is ambiguous ownership and high coordination in shared files; network services would add deployment, observability, failure, and data-consistency costs before proving that process boundaries solve it.

`engineering-for-leverage` owns the technical seam and code-ownership recommendation. `building-and-evolving-organizations` must own the staffing, reporting lines, incentives, and final team topology. Engineering should give that workflow capability costs and boundary evidence rather than silently treating a service diagram as an org chart.

## Map before splitting

For the two weeks ending 2026-07-28, map:

- customer journeys and data flow from checkout through entitlement, invoice, and notification;
- which files and tables co-change, how often, and for which product reasons;
- the invariants shared across those changes;
- handoffs, merge conflicts, deploy coupling, incidents, and recovery ownership; and
- independent scaling, security, availability, and release requirements, if any.

Likely provisional surfaces are purchase-to-entitlement, invoice lifecycle, and lifecycle communication, but the map must be allowed to disprove them. Preserve explicit invariants: one accepted purchase has one economic identity; entitlement changes agree with the authoritative payment state; invoices reconcile to that economic event; and email is a notification side effect, never the source of entitlement or billing truth.

## Change ownership and code boundaries first

Assign one accountable end-to-end technical owner to each validated surface. That owner controls its domain code and writes, tests, dashboards, runbook, deployment readiness, and first incident response, and can change the full path needed to restore the customer outcome. Other engineers may contribute, but responsibility does not stop at a controller, database, or UI layer.

Within the monolith:

1. Put each surface behind an in-process interface with explicit table/write ownership. Stop unreviewed cross-module writes.
2. Add invariant and conformance tests at each boundary, plus end-to-end tests for checkout-to-entitlement and billing reconciliation.
3. Use an outbox or another behavior-preserving seam for notifications that must follow committed billing events; compare results before removing the old call path.
4. Move shared code only when it represents genuinely shared stable vocabulary. Duplicating a small adapter is preferable to a “common” module that requires all owners to coordinate.
5. Name the incident owner and fallback for every boundary. During migration, retain the old path or a reversible flag until the new path produces equivalent outcomes.

This yields most of the ownership benefit without a distributed transaction, extra on-call surfaces, or forced synchronized service contracts.

## Service extraction gate

Review the modular trial on 2026-09-08 against a baseline fixed before changes. Precommit concrete thresholds—for example, at least 30% fewer cross-owner handoffs and hot-file conflicts, at least 25% lower median restore time for affected incidents, and no material regression in change lead time or correctness. Use the actual baseline to confirm that those thresholds are meaningful before beginning the trial.

Extract one module only if production evidence shows a binding need for independent deployment, scaling, isolation, security, or release cadence; its vocabulary and invariants are stable; and one owner can operate it end to end. Lifecycle communication may be a candidate because it can consume committed events, but it does not get a service merely because it looks separable on a diagram. Preserve a versioned interface, contract tests, replay/reconciliation for events, deployment observability, and a route back to the in-process implementation.

Keep or redraw boundaries based on lead time, conflicts, handoffs, incidents, and recovery. Retreat if the new boundary increases adapters, coordinated releases, call sites, conceptual load, or incident bouncing. The rejected alternative is an all-at-once microservice split; the preserved option is incremental extraction after a modular boundary proves useful.
