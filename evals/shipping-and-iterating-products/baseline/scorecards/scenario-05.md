# Baseline scorecard

Case ID: scenario-05

Reviewer ID: shipping-baseline-001

Cases SHA-256: a57c2b42f0a14fb52a6ebca3c6c80ec21dba8adfc4f739fcb80463bca4619efb

## Score

Score: 1/5

1. **1/1 — Makes shipping primary now:** It uses repeated manual service and paid pilots to move the validated narrow segment into a user-visible build and release workflow.
2. **0/1 — The release contract is incomplete:** The response defines a smallest complete notification loop and defers extra integrations, channels, rules, and administration, but sets no release date, no quantitative behavior thresholds, and no explicit rollback rule.
3. **0/1 — The engineering route is not named:** It leaves event-bus replacement with engineering unless release correctness, timeliness, or observability require it, but does not route the abstraction and migration work to `engineering-for-leverage`.
4. **0/1 — The learning return condition is unstated:** It correctly says the discovery-to-shipping gate has passed and does not reopen validated demand now, but never limits a future learning handback to a newly stated uncertainty or behavior that contradicts the validated need.
5. **0/1 — Growth ownership is handed off too late:** The paid pilots already pass the canonical growth-ownership gate. The response correctly delays a broad campaign until product use, activation, and retention are repeatable, but incorrectly says the shipping-to-growth handoff itself waits for predictable onboarding and credible product data.
