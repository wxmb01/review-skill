# Review Templates

Use these templates when the user would benefit from a stable deliverable shape instead of a free-form review.

## Default Review

```md
## Findings
- [severity] issue, impact, evidence, direct fix

## Evidence Gaps And Open Questions
- missing evidence or unanswered question

## Completion Verdict
- verdict: not started | partial | functionally complete but risky | ready with caveats | ready
- rationale: short explanation

## Recommended Next Actions
- blockers first
- next wave
- optional improvements
```

## Change Review

```md
## Change Summary
- what changed
- why it changed

## Findings
- [severity] regression or risk in the change

## Strengths
- good patterns or safeguards worth preserving

## Impacted Areas
- modules, tests, docs, config, rollout

## Evidence Gaps
- what should have been checked but was not proven

## Recommendation
- approve | approve with caveats | changes needed
```

## Code Review Report

```md
## Findings
- [severity] [optional tag] file:line issue, impact, evidence, direct fix

## Strengths
- concrete good choices worth preserving

## Test And Regression Notes
- what validation exists
- what important gaps remain

## Recommendation
- approve | approve with caveats | changes needed
```

## Readiness Summary

```md
## Readiness Gate Summary
- scope clarity: pass | partial | fail | unknown
- core flows: pass | partial | fail | unknown
- validation: pass | partial | fail | unknown
- operations or handoff: pass | partial | fail | unknown
- risk closure: pass | partial | fail | unknown

## Go Or No-Go
- recommendation
- rationale

## Caveats
- unresolved issues that remain acceptable
```

## Risk Register

```md
| Risk | Domain | Impact | Likelihood | Evidence | Mitigation |
| --- | --- | --- | --- | --- | --- |
| Example risk | reliability | high | medium | short note | direct mitigation |
```

## Requirements Gaps

```md
## Missing Or Weak Requirements
- gap

## Ambiguities
- unclear statement and why it matters

## Missing Acceptance Criteria
- missing criterion

## Success Metrics
- missing or weak metric
```

## Architecture Tradeoff Note

```md
## Current Decision
- short description

## Strengths
- what works well

## Risks
- what may fail or scale poorly

## Tradeoffs
- what was gained and what was sacrificed

## Suggested Change
- smallest useful architecture adjustment
```

## Remediation Roadmap

```md
## Phase 1: Blockers
- fix

## Phase 2: Readiness Gaps
- fix

## Phase 3: Maintainability And Optimization
- fix
```
