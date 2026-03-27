# Review Playbook

Use this reference when the review needs sharper structure, severity rules, search strategy, readiness gates, or more concrete deliverables.

## Read-Only Default

If the user asks to review, audit, assess, evaluate, or check work, default to analysis only.
Do not edit files unless the user also asks for fixes, improvements, implementation, or remediation.

## Scope Strategy

### Change Scope

Use when the target is a PR, commit, diff, patch set, or recent changes.

Prioritize:

- regressions
- unintended side effects
- compatibility impact
- test impact
- rollout or migration risk
- missing docs or config changes near the diff

Broaden from `change` to `project` when the change touches high-impact areas such as:

- auth or secrets
- data migrations
- CI or deployment
- dependency upgrades
- architecture boundaries
- shared infrastructure

### Project Scope

Use when the target is a whole repository, service, product, or delivery state.

Prioritize:

- scope coverage
- readiness
- architectural soundness
- validation quality
- operational maturity
- handoff quality

### Artifact Scope

Use when the primary target is a spec, design doc, report, checklist, or plan.

Prioritize:

- clarity
- traceability
- testability
- ambiguity
- assumptions
- decision quality

## Depth Modes

- `quick`: inspect the highest-risk paths and deliver a triage verdict fast
- `standard`: inspect enough evidence to support a reliable verdict
- `deep`: cross-check multiple artifacts, follow dependency chains, and hunt for hidden gaps

Use `standard` unless the user asks for a light pass or a deep audit.

## Discovery Strategy

Start with the smallest set of artifacts that explains the system, then widen only when needed.

### For Change Scope

1. Inspect the changed files and summarize what changed.
2. Inspect nearby tests, configs, docs, and dependent modules.
3. Trace impact to entrypoints, public interfaces, storage, network boundaries, or user-visible behavior.
4. Look for missing validation, migration, rollback, or documentation updates.

### For Project Scope

1. Inspect repository structure, manifests, and entrypoints.
2. Inspect README, docs, CI, deployment config, and test layout.
3. Identify core flows, critical modules, and risky boundaries.
4. Sample implementation, validation, and operational evidence before widening.

### For Artifact Scope

1. Identify the objective and target audience.
2. Extract constraints, assumptions, and acceptance criteria.
3. Check internal consistency and traceability to implementation or next steps.

### Useful Discovery Signals

Look for:

- TODO, FIXME, HACK, XXX, placeholder, unimplemented
- skipped or flaky tests
- missing runbooks or setup steps
- dependency or configuration drift
- docs that no longer match implementation

## Severity Ladder

- `blocker`: release, submission, merge, or handoff should stop until fixed
- `high`: major correctness, readiness, security, or scope risk; cannot support a confident `ready` verdict
- `medium`: meaningful weakness or gap that can proceed with caveats
- `low`: localized improvement, polish, or maintainability issue

If no blocker or high findings exist, say that explicitly.

## Evidence Floor

Look for evidence across these categories before giving a strong verdict:

- target scope or acceptance criteria
- implemented core flows
- validation or test evidence
- operational or handoff coverage when relevant
- major risks and dependencies

If one of these is missing, report an evidence gap instead of inventing certainty.

## Readiness Gates

To call something `ready` or `ready with caveats`, verify:

- the target scope is understandable
- core flows are implemented
- critical flows have validation evidence
- operational, setup, or handoff requirements are covered when relevant
- blocker findings are absent
- unresolved high-severity risks are either closed or explicitly accepted

If these gates are not met, use a lower completion verdict.

## Optional Readiness Scorecard

Use this scorecard when the user wants a more measurable readiness judgment.
Score each category as `pass`, `partial`, `fail`, or `unknown`.

- requirements clarity
- core flow implementation
- validation quality
- operational or handoff readiness
- risk closure

Use these heuristics:

- any `fail` in a critical category prevents `ready`
- more than one `unknown` means the verdict should stay cautious
- `ready` normally requires mostly `pass` with no blocker findings
- `ready with caveats` can include `partial`, but not blocker findings

## Anti-Shortcut Rules

Do not accept any of these shortcuts:

- tests exist, therefore quality is sufficient
- docs exist, therefore handoff is sufficient
- the build passes, therefore the project is complete
- there are no TODO comments, therefore scope is complete
- it worked once, therefore it is operationally ready
- no obvious security issue was seen, therefore risk is acceptable
- a requirements document exists, therefore the requirements are testable

When in doubt, name the missing evidence directly.

## Prioritization And Tradeoffs

When scope, quality, and time are in tension, prioritize:

1. correctness and safety
2. completion of core flows
3. validation of user-critical paths
4. operational readiness
5. maintainability and optimization

For requirements or project review, explicitly call out:

- what is core scope versus nice-to-have
- what was deferred
- whether the tradeoff appears intentional and acceptable

## Risk Subdomains

Widen `risk` review into one or more of these domains when relevant:

- `security`: auth, secrets, input validation, privilege boundaries, abuse cases
- `privacy`: personal data handling, retention, exposure, consent, logging of sensitive data
- `compliance`: policy, regulatory, or audit obligations
- `performance`: latency, throughput, resource cost, scaling bottlenecks
- `reliability`: failure recovery, resilience, observability, rollback, operational fragility

## Deliverables By Mode

### Project Review

Deliver:

- prioritized findings
- completion verdict
- key blockers and dependencies
- next milestones or phases

### Readiness Review

Deliver:

- readiness gate summary
- go or no-go recommendation
- validation gaps
- release, submission, or handoff caveats

### Architecture Review

Deliver:

- major design strengths and weaknesses
- tradeoff notes
- non-functional risk summary
- suggested architecture changes

### Code Review

Deliver:

- severity-ordered findings
- file references and line numbers when possible
- regression and test-gap notes
- direct remediation suggestions

### Requirements Review

Deliver:

- ambiguity list
- missing acceptance criteria
- missing success metrics
- prioritization or tradeoff concerns
- open questions that block a strong verdict

### Risk Review

Deliver:

- top risks
- affected risk domains
- impact and likelihood notes
- proposed mitigations

### Documentation Review

Deliver:

- missing or stale docs
- handoff gaps
- setup or runbook gaps
- highest-leverage documentation updates
