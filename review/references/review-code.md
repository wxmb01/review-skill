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

## Escalation Triggers

Widen the review when the change touches:

- authentication or authorization
- secret or credential flows
- database schema or data migration
- deployment, CI, or infrastructure config
- public APIs or shared libraries
- feature flags, rollout controls, or incident-prone paths
