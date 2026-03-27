# Java Code Review

Use this reference when the change is mainly in Java, Spring-style backends, JVM services, or library code.

## Object Model And Null Safety

Check for:

- `equals`, `hashCode`, `compareTo`, and identity assumptions that can drift out of contract
- `Optional` used as decoration instead of real null-safety
- mutable objects shared where immutability would protect invariants
- builders or constructors that allow invalid partially-initialized state
- serialization or DTO mapping that drops required fields silently

## Exceptions, Transactions, And Framework Boundaries

Check for:

- checked or unchecked exceptions being swallowed, wrapped too broadly, or converted into misleading success
- transaction boundaries that are too broad, too narrow, or bypassed by internal self-invocation
- validation missing at controller, message-consumer, or API boundaries
- framework annotations whose lifecycle implications are easy to misunderstand
- rollback behavior that differs from what the business flow expects

When Spring is involved, pay extra attention to proxy-based behavior such as `@Transactional`, `@Async`, and caching annotations.

## Concurrency And Threading

Increase scrutiny when the change touches executors, schedulers, caches, or shared services.

Check for:

- shared mutable state without a clear thread-safety model
- `CompletableFuture` chains that drop exceptions or never join critical work
- thread pools that are unbounded, undersized, or never shut down
- blocking work on request threads, reactive threads, or scheduler threads where latency matters
- caching or memoization that is not safe under concurrent access

## Collections, Streams, And Performance

Check for:

- stream chains with side effects that hide order or exception behavior
- accidental `parallelStream()` use or parallelism assumptions that do not hold
- repeated allocations or conversions in hot paths
- returning mutable internal collections that break encapsulation
- ORM or repository access that creates N+1 patterns or hidden lazy-loading costs

## API And Compatibility Concerns

Check for:

- backward compatibility for public methods, DTOs, events, and serialized models
- annotation or reflection changes that break frameworks or code generation
- dependency upgrades that change bytecode, language-level, or runtime assumptions
- migration paths when configuration keys, endpoints, or contracts change

## Java Testing Expectations

Prefer evidence that:

- tests cover exception behavior and not just happy paths
- slice or integration tests prove controller, persistence, or serialization boundaries
- concurrency-sensitive code has at least one test or benchmark that would catch race-prone behavior
- transaction, rollback, and retry expectations are proven where the diff changes them
- framework-driven behavior is tested where annotations or proxies are part of the design

## Common High-Leverage Findings

These are often worth surfacing when true:

- a transaction annotation suggests safety that self-invocation or async execution will bypass
- a stream-heavy refactor looks cleaner but obscures side effects or exception handling
- an apparently simple DTO or entity change quietly breaks persistence, serialization, or equality semantics
- a service appears stateless but actually shares mutable objects across requests
