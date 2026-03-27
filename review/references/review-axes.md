# Review Axes

Use this reference when the request is broad or asks whether a project is complete, good, ready, or in need of improvement.

## Scope And Requirements

Check for:

- clear objective
- explicit deliverables
- acceptance criteria
- constraints and assumptions
- non-goals where relevant
- unresolved ambiguity

Warning signs:

- "done" is undefined
- key flows are not named
- success cannot be verified

## Product And Outcome Fit

Check for:

- target users or stakeholders
- clear problem statement
- success metrics or completion criteria
- evidence that the implementation matches the intended outcome

Warning signs:

- implementation exists without a clear purpose
- functionality is hard to trace back to user value
- there is no way to tell whether the project succeeded

## Prioritization And Tradeoffs

Check for:

- core scope versus nice-to-have scope
- explicit tradeoffs
- rationale for deferrals
- alignment between priorities and actual implementation effort

Warning signs:

- low-value work dominates while critical gaps remain
- tradeoffs appear accidental rather than intentional
- success criteria and priorities conflict

## Completion And Readiness

Check for:

- core flows implemented
- critical edge cases considered
- blockers or TODOs resolved
- release or submission checklist covered
- evidence that major dependencies are in place

Warning signs:

- unfinished placeholder logic
- known blockers with no mitigation
- manual steps that are undocumented

## Execution And Delivery

Check for:

- ownership of major workstreams
- dependency awareness
- milestone or checkpoint clarity
- visible blocker management
- realistic next steps

Warning signs:

- critical work has no owner
- dependency risk is implicit
- progress is hard to evaluate

## Change Impact And Regression Risk

Check for:

- affected modules are understood
- nearby tests were considered
- config or docs updates match the change
- migrations, compatibility, or rollout concerns were addressed

Warning signs:

- code changed without corresponding validation
- behavior changed at an interface boundary without impact analysis
- supporting docs or configs are out of sync

## Architecture And Design

Check for:

- clear module boundaries
- sensible ownership of responsibilities
- acceptable coupling
- clear data flow
- explicit tradeoffs
- failure modes considered

Warning signs:

- hidden cross-module dependencies
- unclear boundaries
- architecture that cannot support expected change or load

## Implementation Quality

Check for:

- correctness
- maintainability
- duplication
- complexity hot spots
- unsafe patterns
- standards compliance

Warning signs:

- fragile branching logic
- copy-paste drift
- weak error handling
- inconsistent patterns in core paths

## Testing And Validation

Check for:

- unit or integration coverage where it matters
- validation for critical flows
- regression protection
- reproducible verification steps
- realistic test data or fixtures when needed

Warning signs:

- critical code with no tests
- tests that do not assert real behavior
- no evidence of end-to-end validation

## Risks And Security

Check for:

- authentication and authorization
- input validation
- secret handling
- dependency or configuration risk
- failure recovery
- data sensitivity

Warning signs:

- trust of unchecked input
- secrets in code or config
- no mitigation for obvious abuse or failure cases

## Performance And Reliability

Check for:

- latency or throughput constraints where relevant
- acceptable resource behavior
- resilience under failure
- observability and recovery paths

Warning signs:

- no rollback or recovery thinking
- unbounded work in core paths
- poor visibility into failure or degradation

## Documentation And Handoff

Check for:

- setup instructions
- architecture notes
- operational guidance
- changelog or release notes when relevant
- enough context for the next maintainer

Warning signs:

- project depends on tribal knowledge
- no run or debug instructions
- no explanation of key decisions

## Optimization Opportunities

Prioritize improvements that:

- reduce major risk
- simplify core flows
- improve testability
- reduce maintenance cost
- improve performance where performance matters
- close a repeated source of confusion

Ignore cosmetic cleanup unless it materially helps one of the outcomes above.
