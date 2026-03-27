# Python Code Review

Use this reference when the change is mainly in Python services, scripts, data-processing code, or async backends.

## Data Model And Control Flow Risks

Check for:

- mutable default arguments or dataclass defaults that should use `default_factory`
- broad `except` blocks that hide operational or correctness failures
- truthiness checks that collapse valid states such as `0`, `False`, or empty containers
- naive datetime handling, timezone drift, or inconsistent UTC assumptions
- implicit behavior in magic methods, decorators, or dynamic attribute access that makes control flow hard to reason about

## Resource, IO, And Process Safety

Check for:

- files, sockets, sessions, and locks that are not cleaned up reliably
- subprocess or shell usage that risks injection or quoting bugs
- unsafe temporary-file, path-join, or archive-extraction behavior
- retry loops without timeout, backoff, or duplicate-work protection
- logging that leaks secrets or sensitive data

Prefer context managers and explicit cleanup on failure paths.

## Async And Concurrency

Increase scrutiny when the code uses `asyncio`, worker pools, threads, or background jobs.

Check for:

- blocking IO inside async code
- cancellation that is swallowed instead of propagated safely
- tasks spawned without lifecycle ownership, waiting, or error handling
- shared mutable state across threads, workers, or requests
- ordering assumptions that break under retries or concurrent execution

## Typing And Interface Discipline

Check for:

- `Optional` values used without a real guard
- type hints that are so broad they stop protecting call sites
- runtime behavior that disagrees with annotated types
- dictionary-shaped data used where a validated model would reduce ambiguity
- monkeypatching or dynamic attributes that hide real contracts

Type hints help, but runtime validation still matters at trust boundaries.

## Persistence And Framework Boundaries

Check for:

- transaction boundaries that are too wide, too narrow, or missing
- ORM access patterns that hide N+1 queries or lazy-loading surprises
- background jobs that are not idempotent
- schema or migration assumptions that will fail on partial rollout
- request-scoped state leaking into global or cached objects

## Python Testing Expectations

Prefer evidence that:

- tests cover exception paths, boundary values, and malformed inputs
- time-sensitive behavior uses deterministic clocks or fixtures
- filesystem and network tests isolate external effects cleanly
- async tests would catch cancellation, timeout, or ordering bugs
- data-layer tests exercise transaction and rollback behavior when it matters

## Common High-Leverage Findings

These are often worth surfacing when true:

- a broad exception handler is converting data corruption into silent success
- an async path looks correct but blocks the event loop under load
- a global mutable object makes request or job isolation unsafe
- a type hint gives confidence that runtime behavior does not actually honor
