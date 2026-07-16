# Operating-with-focus-and-morale paired microtest design

## Predeclared protocol

Freeze `.superpowers/sdd/focus-micro-design.json`, its decoded prompt and five criteria, the current skill and runtime contract, all ten sample identities, arm inputs, capture contract, scoring rule, and acceptance threshold before generation.

Run five prompt-only controls and five prompt-plus-frozen-guidance replications. Pair replications by index for reporting, but run all ten in unique fresh-context tasks. Generators receive no criteria, rationale, earlier response, opposite-arm input, or score. Each response is capped by the shared prompt at 1,200 words.

Capture each task's final response once, directly to its declared unique path. Freeze its hash after the first complete write. Do not reconstruct responses from event logs, edit them, or regenerate for quality. A missing or incomplete first write invalidates the attempt rather than authorizing a replacement under the same design.

After all outputs are frozen, give the five hidden criteria and de-identified responses in randomized order to one scorer who is distinct from the designer and all generators. Hide arm and generation provenance until the scorer freezes all 50 binary judgments. A criterion passes only when every conjunct is satisfied; accept semantic equivalents, infer no omissions, and award no partial credit. Read every response manually.

Compute each response as passed criteria divided by five and each arm as its 25 passed bits divided by 25. Accept only if all ten samples and integrity checks are valid and `guided mean - control mean >= 0.20`.

## Hidden rubric structure

The JSON contains exactly five strict criteria, one for each intended behavior:

1. Select attention fragmentation, sustainable execution, and the persistence decision as the primary route while ruling out survival, live capital or sale, authority redesign, and continuity incidents as leading diagnoses from the supplied facts.
2. Separate observations, stakeholder interpretations, and unresolved questions; classify the supplied evidence correctly and attach an owner, method, date, threshold, and decision effect to consequential unknowns.
3. Choose exactly one state-changing five-week customer or product outcome and explicitly dispose of all four named competing initiatives while preserving essential obligations.
4. Establish recurring maker and customer contact, a bounded sustainable workload and recovery cadence, removed or transferred work, backup coverage, and escalation without using hours or nights as proof of commitment.
5. Separate the customer-outcome premise from the current tactic and close on owned, dated, measurable conditions for continuing, adapting, reopening the outcome, or stopping.

The exact conjunctive wording is authoritative in the JSON. This summary is for design review only and must never be supplied to a generator.

## Design rationale

The prompt is held out from all six canonical cases. CanopyTrace's state is technical portfolio fragmentation across noncomparable greenhouse hardware trials with a real 90-day evidence latency: there is no conference, competitor shock, software adoption dispute, live fundraise, payroll threat, founder approval queue, or optional-publicity calendar. Healthy runway, no transaction process, clear rights, separate certified control systems, and no open incident make the focus workflow primary while leaving hardware analysis as a supporting workflow.

The data deliberately support none of the three technical tactics as proven. Bench projection, a long lab run, partial sunny-site results, shaded-row failures, different hardware revisions, and inconsistent reporting leave representative performance, comparability, grower value, certification work, and causality unresolved. The four side initiatives and recorded reassignments create observable stop choices. Weekend trial checks, single-person field coverage, hours, and the pulse decline make sustainable execution material without introducing an acute safety scenario.

The user-facing request remains a plausible board memo: decide now, identify work not to do, operate for five weeks without extending hours, and prepare for a dated review. It does not expose the internal route names, evidence ledger, one-priority fields, maker/user cadence fields, four branch labels, scoring threshold, or intended answer. Generic productivity advice cannot pass because the hidden rubric requires company-specific classifications, dispositions, safeguards, thresholds, owners, and dates.

## Prompt leakage audit

- No skill identifier or taxonomy route appears in the prompt.
- No `observed` / `claimed` / `unknown` classification or ledger is requested.
- No one-priority, stop/defer, maker-time, user-contact, or operating-record template is supplied.
- No `continue` / `adapt` / `reopen-goal` / `stop` branch vocabulary is supplied.
- No criteria, binary scoring rule, paired-arm design, or effect threshold is disclosed.
- The prompt's memo format, June 15 deadline, 1,200-word cap, service-preservation request, caveat request, and no-invention rule are natural constraints.

## Artifact fingerprints

Canonicalization and final fingerprints are recorded after byte-level validation. The decoded prompt hash uses `jq -j .prompt`; the criteria hash uses compact ordered JSON from `jq -c .criteria`; neither includes a trailing newline.

- Decoded prompt UTF-8 SHA-256: `3dfbc9ff01c708e1f8fe4859f19630b20e8ce7bf8ca2d731da92572d13f3bfc8`
- Ordered criteria JSON SHA-256: `caccab3035924484f94e270faff0082b4aad39b4f4069abe544f8ca37b0f7285`
