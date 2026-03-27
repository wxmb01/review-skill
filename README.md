# Review Skill

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](./LICENSE)
[![Release](https://img.shields.io/github/v/release/wxmb01/review-skill?style=flat-square)](https://github.com/wxmb01/review-skill/releases)
[![Stars](https://img.shields.io/github/stars/wxmb01/review-skill?style=flat-square)](https://github.com/wxmb01/review-skill/stargazers)

Open review skill for project review, code review, readiness review, architecture review, requirements review, risk review, and documentation review.

[English](./README.md) | [简体中文](./README.zh-CN.md)

## Why This Skill Exists

Normal code review is often too narrow for real project decisions.

`Review` is built for questions like:

- Is this project actually complete?
- Is this change safe to merge?
- Is this release ready?
- What are the biggest risks?
- What should be fixed first?

It is read-only by default for review requests, and it is designed to judge evidence, completion, readiness, and risk instead of only commenting on code style.

## What It Covers

### Review Scopes

| Scope | Use it for |
| --- | --- |
| `change` | PRs, commits, diffs, patch sets, and uncommitted changes |
| `project` | Full repositories, products, systems, and delivery-state audits |
| `artifact` | Specs, plans, reports, architecture notes, and design documents |

### Review Modes

- `project`
- `readiness`
- `architecture`
- `code`
- `requirements`
- `risk`
- `documentation`

## Key Features

- Read-only by default for review requests
- Scope routing before review mode selection
- Evidence-based completion and readiness judgment
- Severity ladder with blocker and high-risk handling
- Readiness gates and optional scorecard
- Risk subdomains for security, privacy, compliance, performance, and reliability
- Reusable review templates for diff reviews, go/no-go summaries, risk registers, and remediation roadmaps

## What You Get

Depending on the request, the skill can produce:

- severity-ordered findings
- completion verdicts
- readiness gate summaries
- risk registers
- requirements gap reports
- architecture tradeoff notes
- remediation roadmaps
- validation plans

## Installation

Install directly from GitHub:

```bash
npx skills add https://github.com/wxmb01/review-skill --skill review -g -y
```

## Example Prompts

```text
Use $review to assess this project for completion, risks, and next improvements.
```

```text
Use $review to review this PR in change scope and tell me whether it is safe to merge.
```

```text
Use $review to perform a readiness review and tell me whether this project is ready to submit or release.
```

```text
Use $review to review this design document in artifact scope and identify ambiguity, missing acceptance criteria, and major risks.
```

## Repository Layout

```text
review/
  SKILL.md
  agents/
    openai.yaml
  references/
    review-axes.md
    review-playbook.md
    review-templates.md
```

## License

Released under the MIT License.
