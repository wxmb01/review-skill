---
name: review
description: End-to-end project, artifact, and code review for assessing completion, requirements coverage, architecture, implementation quality, testing, risks, documentation, readiness, and improvement opportunities. Use when Codex needs to audit a software or technical project, review a diff or PR, judge whether work is complete or ready, review an architecture or delivery plan, or produce a prioritized remediation plan.
---

# Review

## Overview

Use this skill to review a project beyond surface-level code style comments.
Cover the axes that matter for the request and skip irrelevant ones.

Default to read-only analysis when the user asks to review, audit, assess, evaluate, or check work.
Do not modify files unless the user explicitly asks for fixes, improvements, or implementation work in addition to the review.

Read `references/review-axes.md` when the request is broad, asks whether the project is "done" or "ready", or needs a full audit rather than a narrow code review.
Read `references/review-playbook.md` when you need scope routing, severity rules, evidence discovery strategy, readiness scoring, anti-shortcut guardrails, or risk subdomains.
Read `references/review-code.md` when the request is mainly about a PR, diff, commit, implementation quality, regression risk, or actionable code-review feedback.
When the stack is clear, also read one or more specialized code-review references:
- `references/review-code-typescript-react.md` for TypeScript, React, and modern frontend review
- `references/review-code-python.md` for Python services, scripts, and async code
- `references/review-code-java.md` for Java, Spring-style backends, and JVM review
Read `references/review-templates.md` when you want a reusable output template such as a diff review, risk register, go or no-go summary, or remediation roadmap.

## Scope Router

Choose one scope first.
Scope answers "what is being reviewed", before mode answers "how to review it".

- `change`: review a diff, PR, commit, patch set, or uncommitted changes
- `project`: review a whole repository, product, service, system, or delivery state
- `artifact`: review a spec, design doc, report, checklist, architecture note, or project plan

If the user asks to review a PR, commit, diff, or recent changes, stay in `change` scope unless the evidence forces a broader audit.
If the user asks whether the project is complete, ready, or good overall, use `project` scope.
If the review target is mainly a document or plan, use `artifact` scope even when code also exists.

## Mode Router

Choose one primary mode and optional secondary modes.
Use the smallest set of modes that answers the user well.

- `project`: review scope coverage, blockers, dependencies, ownership, completion, and handoff
- `readiness`: review whether the work is ready to ship, submit, merge, release, or hand over
- `architecture`: review boundaries, tradeoffs, non-functional requirements, and failure modes
- `code`: review correctness, regressions, maintainability, and test gaps
- `requirements`: review problem framing, acceptance criteria, success metrics, prioritization, and ambiguity
- `risk`: review security, privacy, compliance, dependency, performance, and reliability risk
- `documentation`: review setup, runbooks, design notes, release notes, and maintainability of docs

For broad requests, do a quick scoping pass first, then choose the two to four modes with the highest uncertainty or risk.
Do not force every mode into every review.

## Workflow

### 1. Establish the target, scope, and delivery stage

Identify the review goal, the scope, and the delivery stage: planning, implementation, stabilization, release, submission, or handoff.
State assumptions when scope, acceptance criteria, or requirements are missing.

### 2. Pick review depth

Use one depth level deliberately:

- `quick`: triage the highest-risk areas only
- `standard`: gather enough evidence to support a reliable verdict
- `deep`: perform a broad audit with cross-checks and follow-up evidence collection

Use `standard` by default.

### 3. Set the evidence floor

Before calling anything complete or ready, look for evidence across these categories:

- scope or acceptance criteria
- implementation of core flows
- validation or testing
- operational or handoff coverage when relevant
- major risks or dependencies

If a category is missing, record an evidence-gap finding instead of guessing.

### 4. Discover evidence strategically

Follow the discovery strategy in `references/review-playbook.md`.

For `change` scope, start with the changed files, nearby tests, configs, docs, and impacted entrypoints.
For `project` scope, start with manifests, READMEs, tests, CI, deployment config, entrypoints, and the most central modules before widening.
For `artifact` scope, inspect the stated goals, constraints, assumptions, acceptance criteria, and traceability to implementation or planned work.

### 5. Choose review axes and gather evidence

Prefer primary artifacts:

- source files
- tests
- configs
- build or CI files
- docs and READMEs
- deployment or environment config
- tickets, specs, checklists, or diagrams when available

Distinguish facts from inference.
Treat missing evidence as a risk, not as proof that the area is healthy.

For broad audits, read both reference files before finalizing the verdict.

### 6. Produce findings

Lead with findings, not summary.
Order findings by severity and user impact using the severity ladder in `references/review-playbook.md`.

For each finding, include:

- severity
- what is wrong
- why it matters
- what evidence supports it
- the most direct fix

Distinguish between:

- confirmed issues
- likely risks
- evidence gaps

For code findings, include file references and line numbers when available.
For project findings, name the affected area, artifact, workflow, or delivery gate.

### 7. Judge completion and readiness

Use the completion verdicts below together with the readiness gates and optional scorecard in `references/review-playbook.md`.
Never mark work as `ready` if blocker or high-severity findings remain unresolved, or if critical validation evidence is missing.

### 8. Recommend next actions

Separate blocking fixes from the next wave of work and optional optimizations.
Prefer the smallest set of changes that materially improves correctness, readiness, or maintainability.
When asked to improve the project, turn the review into a phased remediation plan or a patch set.

## Review Modes

### Project Review

Focus on objective, scope coverage, open work, blockers, dependencies, ownership, delivery risk, and handoff readiness.

### Readiness Review

Focus on definition of done, acceptance criteria, validation, release or submission gates, rollback or recovery, observability, and unresolved risks.

### Architecture Review

Focus on boundaries, coupling, data flow, tradeoffs, non-functional requirements, failure modes, scaling assumptions, and operational complexity.

### Code Review

Focus on correctness, regressions, maintainability, duplication, complexity, unsafe patterns, test gaps, and standards compliance.
Use the dedicated code review workflow in `references/review-code.md` for `change` scope and for implementation-heavy reviews.
If the user simply asks for a "review", start here for `change` scope, then widen if architecture, requirements, QA, or readiness gaps dominate.

### Requirements Review

Focus on problem framing, users or stakeholders, acceptance criteria, success metrics, prioritization, missing constraints, and unverifiable requirements.

### Risk Review

Focus on security, privacy, compliance, dependency, performance, and reliability exposure.
Split the review further when one of those domains is clearly dominant.

### Documentation Review

Focus on setup instructions, debug paths, runbooks, architecture notes, release notes, and handoff quality.

## Output Contract

Use this default structure:

1. Findings
2. Evidence gaps and open questions
3. Completion verdict
4. Recommended next actions

When useful, append one or more of these deliverables:

- readiness gate summary
- risk register
- requirements gaps
- architecture tradeoff notes
- remediation roadmap
- validation plan

Use `references/review-templates.md` when a stable deliverable shape would help.

Keep summaries brief.
Make findings the primary output.

## Completion Verdicts

Use these verdicts consistently:

- `not started`: little or no evidence of implementation
- `partial`: meaningful work exists, but major scope is still open
- `functionally complete but risky`: main flows exist, but validation, risk, or maintainability gaps are significant
- `ready with caveats`: shippable or submittable, but non-blocking issues remain
- `ready`: evidence supports scope completion, acceptable risk, and readiness gates are met

## Optimization Guidance

Do not suggest generic cleanup for its own sake.
Prefer optimizations with clear leverage:

- removes correctness risk
- shortens future delivery time
- reduces operational burden
- improves testability
- improves maintainability in high-change areas
- closes a clear documentation or handoff gap

## Limits

Do not claim certainty when the evidence is incomplete.
Do not reduce a broad project review to lint-style code comments.
Do not treat "works on my machine" as proof of completion.
Do not bury high-severity findings under style suggestions.
Do not confuse the presence of artifacts with proof of quality; use the anti-shortcut rules in `references/review-playbook.md`.
