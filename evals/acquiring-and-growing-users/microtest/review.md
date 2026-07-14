# Acquiring and Growing Users Microtest Review

Scorer ID: growth-micro-scorer-001

Final rescorer ID: null

Skill SHA-256: `8d0a3145d9957bd16cfcd1130f9bb64af84f7ee7535ce1516b39d8530a981da4`

Rubric SHA-256: `da3398b90c659a8c729e345351b77b6250764aa9d66261d82d55ae5b8f226a56`

Rubric frozen before scoring: **true**.

I independently scored all ten frozen responses against the five criteria as strict conjunctions. A criterion passes only when every named ownership, state, cohort, measurement, branch, and scale-gate clause is explicit. Strong general growth practice, a metric mentioned without its eligible denominator, a founder observing work owned by someone else, or a product owner informally “shipping” something does not substitute for a missing founder-support or shipping-exposure responsibility.

The artifact contains exactly five control and five guided response/manifest pairs, with filename and manifest repetitions 1–5. Every manifest has the same exact nine keys, numeric schema version 1, the correct variant and repetition, a unique nonempty canonical task, model identity `GPT-5`, a valid UTC timestamp, and the exact frozen rubric prompt. Control skill hashes are null; guided skill hashes equal the current skill hash. All ten declared response hashes match the response bytes; tasks and response hashes are unique, so there are no duplicate responses. Control response byte counts are `[9936, 10801, 11863, 9874, 8683]`; guided byte counts are `[10213, 10283, 13373, 10708, 10473]`. All artifact JSON parses. Every response begins with content, ends in exactly one line feed, and has no trailing horizontal whitespace.

Integrity gate: **Pass**. The current skill and rubric hashes exactly match the required frozen values. No skill, rubric, response, or manifest was edited.

Strict control scores are `[2, 1, 0, 1, 0]`. Control repetitions 1, 2, and 4 fully map the narrow source-to-retention loop, while repetitions 3 and 5 never explicitly carry acquisition source through implementation-state cohorts. Only repetition 1 jointly conditions trade-show, reseller, and hiring scale on an operational user outcome as well as activation, retention, support burden, and economics. All controls omit a survival-state assumption, all omit at least one founder/manual or cross-skill routing clause, and all omit the complete numerator/denominator plus four-branch measurement contract.

Strict guided scores are `[3, 3, 4, 4, 3]`. All five map the beachhead and causal loop and all five cap scale behind activation, retention, burden, economics, and accountable user effects. Repetitions 1–4 record survival state and pass criterion 1; repetition 5 never records runway, time-to-zero, or another survival assumption. Repetitions 3–5 operationalize the complete measurement contract; repetitions 1 and 2 mention referrals and costs but do not state the referral numerator over an eligible retained-customer denominator and do not normalize the full cost/support set explicitly enough to pass. Every guided repetition misses criterion 3: repetitions 1, 3, and 5 move binding-point onboarding/support to non-founder owners; repetition 4 also combines setup and integration ownership; repetition 2 comes closest but still assigns actual support to customer success and leaves bounded exposure without a distinct shipping owner.

Result: the control normalized mean is `0.16`; the guided normalized mean is `0.68`; the guided-minus-control normalized delta is **`+0.52`**. Control population variance is `0.56`; guided population variance is `0.24`. Neither variant has an all-criteria pass, so the guidance materially improves average strict compliance while the founder/manual and shipping-exposure ownership contract remains a consistent residual miss.
