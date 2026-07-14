Case ID: scenario-01
Reviewer ID: engineering-baseline-001

Use the familiar TypeScript and Postgres foundation, but isolate connection management and fanout behind a narrow interface so that the hot path can be replaced without rewriting product logic. The niche runtime's theoretical fit is not enough to accept its operational, hiring, and ecosystem costs before either option has been tested at the required load.

Before committing the production design, run a time-boxed, production-shaped benchmark against both approaches. It should sustain at least 50,000 persistent connections, realistic message sizes and fanout distributions, reconnect storms, deploys, node failures, and database pressure while meeting the sub-100 ms latency objective at an agreed percentile. Also exercise observability, recovery, local development, and one realistic operational incident.

Keep the familiar stack if it meets the target with reasonable headroom, understandable failure modes, and an affordable operating profile. Switch the isolated real-time tier to the actor runtime if repeated measurements show that the familiar design cannot meet the target without materially greater complexity or cost, and if the founders can demonstrate reliable deployment and recovery. Reconsider either choice when actual traffic shape, tail latency, incident burden, infrastructure cost, or hiring constraints contradict the benchmark assumptions.
