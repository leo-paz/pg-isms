mode: cross-domain-decision  
primary_skill: making-calibrated-decisions  
reason: The July 31 commitment couples product exposure, customer concentration, contractual control, runway, and financing timing; no single specialist owns the whole choice.

## Decision header — July 20, 2026

decision: Whether to make three commitments now—general onboarding release, partner exclusivity, and a seed-extension launch—or sequence them behind separate evidence gates.  
owner and deadline: CEO; decision on July 31, 2026.  
state: Ten-person enterprise startup; collected revenue of $95,000/month against $185,000/month cash expense; current net burn about $90,000/month and static runway about 11.7 months before transaction costs or changes in collections. The binding constraint is preserving cash and commercial control while three customers represent 61% of ARR.  
product type: Enterprise/integration software.  
error profile: The prototype and a limited rollout are reversible; a general release can impose onboarding and accessibility failures; exclusivity can irreversibly constrain customer and product options; fundraising consumes management time and may create financing exposure. Protected obligations are accessibility, customer trust, contractual control, and a viable cash floor.  
evidence clock: Administrator/accessibility testing and counsel review can inform July 31; reliable fundraising results cannot. Waiting one week delays rollout and the partner announcement but preserves control.

## Evidence ledger

**Observed**

- Cash is $1.05 million; monthly collected revenue is $95,000; monthly cash expense is $185,000.
- Three of twelve paying customers represent 61% of ARR.
- In a moderated 14-user prototype, 11 completed onboarding versus 6 of 14 on the current flow.
- The prototype has no administrator or accessibility-tool test, and no exclusivity agreement is signed.

**Claimed**

- The design partner says exclusivity is required for a $240,000 annual contract.
- An investor says fundraising will be easier after a partner announcement.
- Product and sales leaders assert that immediate broad release and signature are preferable.

**Inferred**

- Static runway is approximately 11.7 months at the current net burn; this is a planning estimate, not a forecast.
- User-level completion evidence favors the prototype, but does not establish administrator operability, accessibility, retention, or broad enterprise readiness.
- The partner contract could materially improve revenue and concentration, but exclusivity could also deepen dependence or block alternatives; scope and enforceability are not yet known.

**Unknowns that can change the decision**

| Unknown | Owner | Artifact/source | Due | Threshold | Decision effect |
|---|---|---|---|---|---|
| Admin and accessibility performance | Product lead | Moderated admin test plus normal accessibility report | Jul 27 | No critical blocker; completion improves materially without guardrail regression | Pass permits staged release; fail requires adaptation |
| Exclusivity scope, term, remedies, and exit | CEO | Counsel-reviewed draft and redline | Jul 28 | Qualified review complete; bounded scope/term; credible exit; economics survive downside | Pass allows commercial negotiation; fail stops signature |
| Partner commitment | Sales lead | Executable contract, not forecast | Jul 29 | Signed or signature-ready agreement with approved terms | Determines whether partner economics enter the decision |
| Cash downside and concentration after each choice | Finance owner | 18-month cash model with collection and loss cases | Jul 27 | Board-approved minimum cash floor remains funded | Failure routes survival before financing |
| Financing readiness independent of announcement | CEO | Current investor conversations and financing plan | Jul 29 | Enough qualified interest and runway for a bounded process | Determines launch, preparation only, or deferral |

Rival explanations: the completion lift may come from moderation or sample mix rather than the design; exclusivity may be a negotiating position rather than a true requirement; the investor may be describing signaling value rather than actual commitments. Disconfirming observations are the absent admin/accessibility evidence, unsigned paper, and concentrated ARR.

## Options

| Option | Hard gates and survival | Users and payoff | Reversibility, optionality, evidence, delay |
|---|---|---|---|
| Commit to all three now | Fails current product, contract, and financing evidence gates; cash floor unmodeled | Maximum speed and possible $240,000 ARR; broad users bear errors | Release partly reversible; exclusivity and financing consequences less so; destroys information value |
| Decouple and stage each commitment | Requires tests, counsel review, and cash model | Captures onboarding evidence and possible partner upside while bounding harm | Preserves general-release, nonexclusive sales, and later financing options; one-week delay |
| Defer all | Safest near term but does not address concentration or product opportunity | Avoids immediate errors; loses learning and may lose partner timing | Preserves cash/control, but sacrifices evidence and may incur commercial delay |

**Commitment:** choose decoupled staging. Run a limited onboarding exposure only after admin/accessibility gates; negotiate but do not sign exclusivity before qualified review and cash modeling; prepare financing materials, but launch a process only on its own readiness and survival evidence—not on an announcement alone.

## Dated branches

- **proceed** — Predicate: by Jul 29 all three independent gates pass. Owner/date/action: CEO, Jul 31; authorize staged onboarding, execute only counsel-reviewed bounded partner terms, and start the approved financing process. Safeguard/preserved option: rollout rollback, contractual exit, and minimum cash floor. Switch: any gate regresses before execution → `adapt` or `stop-or-route`. Handoffs: `shipping-and-iterating-products`, qualified counsel, and `raising-and-governing-capital`.
- **adapt** — Predicate: onboarding passes but contract or financing evidence is mixed, or vice versa. Owner/date/action: CEO, Jul 31; execute only the passing reversible component and bound the mixed component with a new test or narrower term. Preserved option: other commitments remain unmade. Switch: defined threshold passes → `proceed`; fails → `stop-or-route`. Handoffs: the corresponding product, counsel, runway, or capital specialist.
- **defer** — Predicate: material artifacts remain unavailable by Jul 29 without a failed hard gate. Owner/date/action: CEO, Jul 31; preserve the current product and nonexclusive position, continue financing preparation only, and set the next review for Aug 7. Preserved option: limited pilot and revised partner proposal. Switch: missing artifact resolves → re-enter the applicable branch. Handoffs: `learning-from-users`, counsel, and `managing-runway-and-survival`.
- **stop-or-route** — Predicate: accessibility/customer-trust blocker, unacceptable contract control, or cash floor failure. Owner/date/action: CEO, immediately upon evidence and no later than Jul 31; stop the affected commitment. Preserved option: current flow, nonexclusive selling, and survival-first plan. Switch: specialist supplies a passing, documented gate. Handoffs: `shipping-and-iterating-products`, qualified counsel, then `managing-runway-and-survival` before `raising-and-governing-capital`.

This is a decision-process record, not legal or investment advice.

Case ID: scenario-01
Reviewer ID: calibration-forward-generator-001
