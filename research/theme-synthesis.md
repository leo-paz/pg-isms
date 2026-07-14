# Theme synthesis and final skill taxonomy

## Decision

The final research set contains 209 startup-relevant essays and 122 canonical themes. They resolve into 21 user-facing workflows plus seven inherited invariants, six product-type branches, and nine deterministic routing rules. This remains a compact ten-to-one compression from relevant essays to skills, while separating jobs whose actors, evidence loops, or stopping conditions differ.

`research/taxonomy-source.json` is the human-authored decision artifact. `scripts/sync_taxonomy.py` validates its runtime contract, requires each canonical theme to have one primary evidence owner, derives essay IDs from `research/essay-theme-map.jsonl`, and writes `research/taxonomy.json` plus reciprocal `final_skills` in the 12 primary audit batches.

## How the taxonomy was derived

Taxonomy work began only after all 223 essays had been audited and the raw themes normalized. Three fresh-context agents independently clustered the 204 essays then considered relevant:

| Lens | Proposed size | Main contribution |
|---|---:|---|
| Distinct user jobs and triggers | 17 | Kept preparation, opportunity, validation, product, growth, model, competition, engineering, founder operations, survival, capital, organization, communication, exits, evaluation, support, and communities visible. |
| Minimum complete library | 14 | Challenged splits whose triggers and deliverables were not independently recognizable. |
| Conditions and tensions | 18 | Preserved stage, survival, product-type, error-cost, writing-mode, focus, and community exceptions. |

The primary agent reconciled these proposals against theme co-occurrence, audit workflows, BM25 retrieval, semantic retrieval, and complete source passages. The first 18-skill draft passed mechanical checks but then failed three independent fresh-context red teams. Those reviews found five wrongly excluded essays, broad themes that created false skill links, duplicate marketplace and launch cases, compound writing and evaluator/support jobs, a missing ecosystem-builder actor, and cross-cutting conditions quarantined in a catch-all skill.

The draft was reopened. Articles 060, 144, 189, 199, and 210 were re-read, reclassified as supporting, and mapped through reviewed correction artifacts. Broad equity, adversarial, network-effect, and policy themes were split by actor or mechanism. The taxonomy grew to 21 only where the user job changed; no count target was preserved.

## Final workflow map

| Skill | Primary actor and deliverable | Boundary |
|---|---|---|
| `preparing-to-found` | A prospective founder or active team decides readiness and location. | Personal readiness and mobility, not ecosystem policy. |
| `building-startup-ecosystems` | A city, university, policymaker, accelerator, or community builder selects ecosystem interventions. | Regional density and institutions, not one founder's relocation. |
| `choosing-startup-opportunities` | A founder chooses, reframes, kills, or pivots a problem direction. | Direction decision, not the validation study. |
| `learning-from-users` | A team designs and interprets evidence about whether and why demand exists. | Evidence plan before a repeatable growth loop. |
| `shipping-and-iterating-products` | A team scopes, releases, observes, and improves a user-visible artifact. | Artifact and rollout, not internal technical structure. |
| `engineering-for-leverage` | A technical team chooses architecture, technology, abstraction, ownership, or adversarial system design. | Internal structure and robust machinery, not release strategy. |
| `acquiring-and-growing-users` | A team changes acquisition, activation, liquidity, retention, or expansion after evidence of need. | Owns marketplace cold start; governance joins only for interaction-quality constraints. |
| `designing-business-models` | A team chooses pricing, sales, channel, company boundary, and venture model. | Value capture and venture shape, not a financing transaction. |
| `competing-and-positioning` | A team differentiates against alternatives, incumbents, platforms, and technology ecosystems. | External position, not governance of its own participants. |
| `forming-founder-partnerships` | Founders select and test cofounder trust, commitment, roles, and durability. | Existential founder relationship, not ordinary hiring or broad equity mechanics. |
| `building-and-evolving-organizations` | A company hires, allocates employee equity, preserves ownership, and adds coordination as scale requires. | Employee and organizational evolution, not cofounder selection. |
| `operating-with-focus-and-morale` | Founders protect attention, deep work, agency, morale, and adaptive persistence. | Normal operating system; survival state can override it. |
| `managing-runway-and-survival` | A company diagnoses default-alive state and chooses burn, revenue, profitability, spending, and hiring actions. | Survival branch precedes even plausible rescue financing. |
| `raising-and-governing-capital` | A company executes a financing process and chooses investors, terms, valuation, dilution, control, and truth. | Assumes financing is the chosen instrument. |
| `making-calibrated-decisions` | A user explicitly wants a cross-domain framework, conflicting advice reconciled, or a source/historical claim calibrated. | Residual primary trigger; its invariants are inherited inside specialists. |
| `thinking-through-writing` | A writer uses private drafting and a neutral-reader test to discover and repair an unsettled idea. | Discovery ends before audience optimization begins. |
| `communicating-clearly` | A writer adapts settled, calibrated claims for a specific audience. | Domain skill establishes facts; communication cannot change their calibration. |
| `navigating-acquisitions-and-exits` | Founders decide whether and when to engage an acquirer and protect leverage and focus. | Specialized transaction and distraction state. |
| `evaluating-startups-and-founders` | An investor or program selects applications, bets, and a portfolio. | Selection and power-law portfolio logic, not ongoing coaching. |
| `advising-and-supporting-founders` | An advisor or program diagnoses an accepted founder's bottleneck and support intervention. | Contextual intervention, office hours, cohorts, and peer support, not selection. |
| `governing-platforms-and-communities` | A networked product governs norms, ranking, reputation, transparency, user welfare, moderation, and abuse. | Interaction quality after participants can interact, not raw cold-start acquisition. |

## Boundary evidence

### Five audit reopenings

- Article 060 supplies a concrete attribution test: compare observer-centered intent with situational or random explanations before treating noise as signal (`060:20-42`).
- Article 144 connects technical change to obsolete value capture, incumbent short-term incentives, and legal distortion (`144:18-38`, `144:44-48`).
- Article 189 makes forecast accountability depend on rapid, unambiguous falsification and remembered outcomes (`189:12-22`).
- Article 199 gives a resource-allocation rule with domain-expertise and umbrella exceptions, and warns that power asymmetry suppresses candor (`199:12-24`).
- Article 210 provides a product-taste evaluation model based on intended audience effects, controlled comparison, practice, and discounting prestige (`210:18-38`). Its exclusion was inconsistent with included article 070.

The correction record is `research/audit-reclassifications.json`; the raw-to-canonical updates and actor/mechanism splits are in `research/normalization-revisions.json`.

### Opportunity, learning, and growth

Article 151 distinguishes problem choice, founder/problem fit, narrow urgent demand, deliberate validation, and selling before building (`151:14-56`, `151:84-114`, `151:158-204`). Article 153 deliberately composes manual recruitment, direct user learning, delight, and contained-market critical mass (`153:14-80`). The taxonomy therefore routes by deliverable: direction decision, evidence plan and conclusion, then funnel or channel intervention once a segment shows real use or payment.

### Marketplace cold start and community governance

Article 153 puts manual recruitment and contained-market liquidity in acquisition (`153:14-44`, `153:76-80`). Article 106 begins the governance problem with dilution, norms, selection, ranking, comments, moderation, transparency, reputation experiments, and participant welfare (`106:14-44`, `106:48-118`). Growth owns an empty marketplace; governance composes when trust, interaction quality, reputation, moderation, or abuse becomes binding.

### Cofounders, employees, and equity

Article 123 treats cofounder character, commitment, and tested work as existential (`123:30-50`) and later describes founder role evolution toward hiring, planning, and management (`123:338-366`). Article 078 applies outcome-adjusted equity to employees, investors, and company deals (`078:18-50`), so the broad `equity-and-ownership` label was removed. Employee equity now belongs to organization building; financing dilution and liquidity belong to capital; cofounder formation no longer receives false employee/deal provenance.

### Adversarial systems and community abuse

Articles 018 and 020 concern adaptive classifiers, personalized learning, asymmetric errors, and robust evaluation, not community norms (`018:20-34`, `018:38-100`, `018:124-148`; `020:18-34`, `020:122-166`). Their evidence now belongs to engineering through `adversarial-system-robustness`. Troll prevention, human moderation, and user abuse controls belong to community governance through `abuse-and-moderation-controls`.

### Product, technology, and regional network effects

The old network-effect theme mixed marketplace liquidity, referrals, programming-language adoption, developer ecosystems, and startup-hub density. It is now split into `product-network-effects-and-critical-mass` for growth, `technology-ecosystem-adoption` for competition, and `regional-ecosystem-density` for ecosystem building. This removes false mappings such as article 023's tool-popularity evidence triggering community governance.

### Founder relocation and ecosystem construction

Article 085 addresses a founder or active startup choosing where to operate, conditioned on family, immigration, industry, funding, and distraction (`085:24-40`, `085:52-58`). Articles 062 and 176 address cities, universities, policy, talent, investor density, and multi-year hub formation (`062:18-60`, `062:74-78`, `062:114-124`; `176:12-70`). Different actors, levers, latency, and success measures require separate skills.

### Survival and financing

Article 169 says default-alive analysis requires operating history; before that, scenario ranges are more honest. It also makes the default-dead branch and plan-B switch date precede a funding assumption (`169:12-30`). Articles 098 and 156 keep product execution and alternatives alive during a raise (`098:40-78`, `098:82-150`; `156:32-76`, `156:244-296`). Survival therefore runs first whenever default-dead or time-to-zero is binding, even if a rescue round seems plausible.

### Writing discovery and audience communication

Article 211 uses writing and a neutral reader to expose incomplete or broken ideas (`211:12-32`). Article 122 says discovery and persuasion can pull in opposite directions because audience spin can alter the thought (`122:38-48`). Article 045 adds a reader- and incentive-specific PR environment (`045:20-46`). Private discovery and audience communication are sequentially composable, but independently triggered jobs.

### Evaluation and founder support

Articles 109 and 148 make selection about founder evidence, outlier potential, and power-law portfolios (`109:54-78`, `148:14-28`, `148:44-62`). Article 213 makes support an individualized bottleneck diagnosis with evidence-latency-aware intervention and peer help (`213:20-66`). Article 199 adds flexible allocation and candor conditions. These are separate actors and completion tests.

### Acquisition and exit

Article 163 retains a narrow specialist: acquirer contact is usually rational only when the company wants to sell and has leverage, while young promising companies face exceptional distraction and manipulation risk (`163:12-34`, `163:42-58`).

## Inherited runtime contract

The source taxonomy makes seven invariants mechanically required for all skills:

1. stage and survival state;
2. reversibility and error cost;
3. evidence latency;
4. product and venture type;
5. truth, character, and accountable user effects;
6. historical and current-context revalidation;
7. preserved optionality with explicit switch conditions.

This resolves the failed draft's structural contradiction: `making-calibrated-decisions` remains an evidence owner and residual user job, but specialists inherit the gates rather than routing away from them.

The six-row product matrix covers capital-light software, enterprise/integration, hardware, biotech/energy, marketplaces/communities, and high-harm regulated products. Each row states evidence latency, launch gate, manual-test form, capital/runway implication, acquisition mechanism, and invalid default advice.

Nine routing predicates disambiguate opportunity/learning/growth, marketplace cold start, survival/capital, domain/communication, writing/persuasion, location/ecosystem, selection/support, technical structure/release, and residual calibration. The evaluation contract requires both sides of each named tension to become observable branches in per-skill baseline and forward tests.

## Coverage contract

The following checks must pass together:

```sh
python3 scripts/apply_audit_reclassifications.py --repo . --check
python3 scripts/apply_normalization_revisions.py --repo . --check
python3 scripts/build_theme_projection.py --repo . --check
python3 scripts/sync_taxonomy.py --repo . --check
python3 scripts/validate_repository.py --phase taxonomy --repo . --corpus /Users/leopaz/dev/opensource/graham-essays/corpus
```

They prove 223 explicit classifications, 209 relevant essays, 122 canonical themes with one primary evidence owner, 21 non-orphan skills, reciprocal essay/skill mappings, complete inherited runtime guards, six product types, nine routing rules, and zero uncovered relevant essays. Skill prose may compose neighboring workflows, but it may not erase these actor, stage, state, product-type, truth, historical, or safety boundaries.
