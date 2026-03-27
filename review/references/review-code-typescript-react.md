# TypeScript And React Code Review

Use this reference when the change is mainly in TypeScript, TSX, React, or frontend-heavy application code.

## Type Safety And Trust Boundaries

Check for:

- `any`, unchecked casts, or type assertions that silence real uncertainty
- missing runtime validation at boundaries such as API input, query params, local storage, environment variables, and feature flags
- widened types that erase invariants the rest of the code depends on
- enum, union, or discriminated-union handling that misses a case but still compiles
- optional fields treated as always present after refactors

Do not let "the compiler is green" substitute for runtime safety.

## React State, Effects, And Rendering

Check for:

- stale closures in event handlers, async callbacks, intervals, and subscriptions
- effects that should be pure derivation instead of synchronization
- dependency-array suppression that hides a real bug
- duplicated source of truth between props, local state, cache state, or form state
- async effects that race, update after unmount, or never cancel
- unstable keys, accidental remounts, and state loss across list or conditional rendering

Do not request memoization by default.
Only call out memoization or render optimization when the code clearly causes avoidable churn in a hot path.

## Server And Client Boundaries

Increase scrutiny when the code crosses framework boundaries such as server and client components, loaders, actions, or API routes.

Check for:

- browser-only APIs used in server code
- server-only secrets or privileged logic leaking into client bundles
- hydration mismatch risk from nondeterministic rendering
- serialization issues across network or server/client boundaries
- cache invalidation or revalidation gaps after mutations

## Forms, UX, And Accessibility

Check for:

- controlled and uncontrolled input mismatches
- missing labels, accessible names, keyboard support, or focus management
- optimistic UI without rollback or failure states
- loading, empty, and error states that are missing or inconsistent
- validation rules that differ between client and server

## Frontend Performance Hotspots

Check for:

- heavy computation during render
- unnecessary rerenders from unstable props or recreated objects on hot paths
- large lists without virtualization or batching where scale matters
- over-fetching, duplicate fetching, or fetches tied to noisy state changes
- layout thrash or animation work that blocks interaction

## TypeScript And React Testing Expectations

Prefer evidence that:

- tests verify behavior, not hook internals or implementation details
- async UI behavior uses the right waiting semantics and would catch race conditions
- loading, error, empty, and success states are covered
- tests exercise trust boundaries such as malformed payloads or invalid user input
- accessibility-sensitive flows are queried in user-facing ways when practical

## Common High-Leverage Findings

These are often worth surfacing when true:

- a cast or assertion is hiding a missing runtime check
- an effect is compensating for state modeling that should be simplified
- a server/client boundary is leaking assumptions that will fail in production
- a component tree is fragile because identity or key stability is not preserved
