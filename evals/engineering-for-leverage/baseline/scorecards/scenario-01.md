# Baseline scorecard

Case ID: scenario-01

Reviewer ID: engineering-baseline-001

Independent scorer: engineering-baseline-scorer-001

Cases SHA-256: 8b57b50bc78649fac772fb3231373cc04b73926db43bd5f26bfae7701078979a

## Score

Score: 0/5

1. **0/1 — Primary workflow is unnamed:** The response makes a measurable architecture choice around 50,000 connections and sub-100 ms latency, but it never makes `engineering-for-leverage` the primary workflow or records the choice as a written technical decision.
2. **0/1 — Representative throughput is omitted:** It compares both approaches under production-shaped connection, fanout, recovery, and operability conditions, but supplies no message-rate or throughput workload or threshold.
3. **0/1 — The bounded decision contract is incomplete:** It calls the benchmark time-boxed and provides a portability seam and result branches, but sets neither a bounded duration nor a decision date, and it does not precommit a branch if neither approach passes.
4. **0/1 — The full durable-cost test is absent:** It mentions operational, hiring, ecosystem, deployment, observability, incident, and replacement concerns, but does not explicitly count team proficiency, debugging, libraries, maintenance, and switching cost or require durable product leverage to exceed the complete cost set.
5. **0/1 — No ordered workflow handoff:** It does not keep the internal choice explicitly with engineering or transfer a later user-visible artifact, exposure, or rollout experiment to `shipping-and-iterating-products`.
