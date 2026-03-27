# Code Review Reference

Use this reference when the request is mainly about changed code, implementation quality, pull requests, commits, or regression risk.

## Reviewer Posture

- Review the work, not the author.
- Stay read-only unless the user explicitly asks for fixes.
- Default to diff-first review for `change` scope.
- Prioritize correctness, safety, and maintainability over style preference.
- Do not spend manual review energy on formatting, import ordering, or lint trivia when automation should handle it.
- Record strengths when they help preserve a good pattern or make the final review more balanced.

## Code Review Workflow

### 1. Gather Context First

Before line-by-line review, establish:

- what changed and why
- the expected behavior or linked requirement
- the base and head range when available
- CI or validation status
- diff size and whether the change mixes too many concerns

If the change is very large or bundles unrelated concerns, say so and recommend splitting when that would materially improve review quality.

Use these rough review-size heuristics:

- under ~200 changed lines: normal review flow
- 200 to 400 changed lines: extra caution on hidden impact
- above ~400 changed lines: explicitly consider whether the change should be split

### 2. Do a High-Level Pass

Check:

- whether the approach fits the requirement
- whether the design matches existing patterns
- whether new files, boundaries, or abstractions make sense
- whether docs, config, migrations, or tests changed alongside the code

### 3. Do a Deep Implementation Pass

Review the code across these lenses:

#### Correctness And Data Integrity

- logic errors
- missing edge-case handling
- null or undefined handling
- state transition mistakes
- unsafe defaults
- data corruption or partial-write risk

#### Security And Trust Boundaries

- input validation
- auth or authorization checks
- secrets handling
- injection risk
- unsafe file or path behavior
- dangerous dynamic execution

#### Concurrency, Time, And State

- race conditions
- stale data use
- retry or idempotency gaps
- timeout handling
- timezone or clock assumptions
- async ordering hazards

#### Performance And Cost

- N+1 queries
- unbounded loops or scans
- repeated work in hot paths
- unnecessary network or storage round-trips
- large allocations or leaks
- avoidable re-renders or heavy rendering work

#### Reliability And Operations

- error handling
- rollback or recovery gaps
- missing feature-flag, migration, or rollout safeguards
- missing observability where failures would be hard to debug

#### Maintainability And Design

- duplication
- complexity hot spots
- tight coupling
- weak naming
- hidden dependencies
- code that is hard to test or reason about
- places where the change fights the language or framework conventions

## High-Risk Change Types

Increase scrutiny when the diff touches one of these areas:

### API Or Contract Changes

Check:

- backward compatibility
- versioning expectations
- client impact
- serialization and validation behavior
- docs or changelog updates

### Data Model Or Migration Changes

Check:

- forward and backward migration safety
- partial-failure behavior
- data backfill assumptions
- rollback plan
- production-scale performance

### Auth, Permissions, Or Sensitive Data

Check:

- access control before every sensitive action
- default-deny behavior
- secret or token handling
- logging of sensitive material
- abuse or privilege-escalation paths

### Dependency, Build, Or Runtime Config Changes

Check:

- version compatibility
- lockfile and config drift
- deployment impact
- environment variable requirements
- whether rollback becomes harder

### Concurrency Or Background Processing Changes

Check:

- idempotency
- retries and duplicate work
- ordering assumptions
- stale reads and races
- cleanup on failure

## Automated Finding Verification

When the review input includes bot comments, scanner output, or static analysis findings:

1. Verify the finding still applies to the current code.
2. Read the surrounding code instead of trusting the reported line in isolation.
3. Distinguish true positive, stale finding, and false positive.
4. Prefer explaining the real failure mode over repeating the tool wording.
5. If the tool is directionally right but technically imprecise, rewrite the finding in accurate terms.

Do not treat automated findings as self-proving evidence.

## Common Language Hotspots

Use these as prompts, not as a replacement for reasoning.

### Python

- mutable default arguments
- broad `except:` blocks
- shared mutable class attributes
- context-manager or cleanup gaps
- async code that forgets cancellation or exception paths

### TypeScript Or JavaScript

- unsafe `any` or unchecked casts
- stale closures in async or UI code
- unhandled promises
- mutation of props, shared objects, or external state
- missing runtime validation at trust boundaries

### SQL And Data Access

- string-built queries
- missing transaction boundaries
- N+1 query patterns
- missing indexes for new access paths
- mismatch between application assumptions and schema constraints

### 4. Review Tests As First-Class Evidence

Do not stop at "tests exist".
Check whether tests:

- cover the changed behavior
- cover negative and edge cases
- validate behavior rather than private implementation details
- are deterministic and order-independent
- would actually catch the failure mode you are worried about

If critical paths changed without meaningful validation, call that out directly.

### 5. Check Cross-File Impact

Look beyond the edited lines for:

- impacted entrypoints and callers
- nearby tests
- configs and environment variables
- docs and release notes
- schema or migration files
- API contracts and client impact

### 6. Produce The Review Decision

Use one of these outcomes:

- `approve`: no blocker or high findings, and evidence is adequate
- `approve with caveats`: only medium or low findings remain
- `changes needed`: blocker or high findings remain, or critical validation evidence is missing

## What To Surface In Code Review Findings

For each important finding, include:

- severity
- file and line when possible
- what is wrong
- why it matters
- what evidence supports it
- the most direct fix or mitigation

Use these optional tags sparingly:

- `question`: when clarification is needed before a confident judgment
- `praise`: when a notable good pattern should be preserved
- `nit`: for tiny non-blocking suggestions only

## Feedback Style

Prefer comments shaped like:

- context
- specific issue
- concrete impact
- direct fix or question

Keep the language collaborative and technical.
Avoid vague comments like "this is bad" or "rewrite this".

## Strengths Worth Mentioning

Call out strengths only when they are concrete and useful, such as:

- good test coverage on a risky path
- a clean abstraction that reduces coupling
- thoughtful handling of rollback or migration risk
- a design choice that keeps behavior easy to reason about

Avoid generic praise like "looks good" or "nice work".

## Code Review Anti-Patterns

Do not:

- block on personal style preference
- ask for speculative refactors unrelated to the change
- equate green CI with full correctness
- assume tool output is automatically true
- bury blocker findings under nits
- demand perfect architecture in a localized fix
- widen scope without saying why

## What Not To Review Manually

Prefer automation for:

- formatting
- import ordering
- trivial lint fixes
- mechanically enforceable style rules

Manual review time should go to reasoning, risk, design, and validation quality.

## Escalation Triggers

Widen the review when the change touches:

- authentication or authorization
- secret or credential flows
- database schema or data migration
- deployment, CI, or infrastructure config
- public APIs or shared libraries
- feature flags, rollout controls, or incident-prone paths
