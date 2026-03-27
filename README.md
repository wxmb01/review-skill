![Review Skill Banner](./assets/review-banner.svg)

# Review Skill

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](./LICENSE)
[![Release](https://img.shields.io/github/v/release/wxmb01/review-skill?style=flat-square)](https://github.com/wxmb01/review-skill/releases)
[![Stars](https://img.shields.io/github/stars/wxmb01/review-skill?style=flat-square)](https://github.com/wxmb01/review-skill/stargazers)

Open review skill for project, code, readiness, architecture, requirements, risk, and documentation review.

[English](./README.md) | [简体中文](./README.zh-CN.md)

## At a Glance

`Review` is built for the moments when a normal code review is too narrow.

It helps answer questions like:

- Is this project actually complete?
- Is this change safe to merge?
- Is this release ready?
- What are the biggest risks?
- What should be fixed first?

Unlike a narrow code-style reviewer, `Review` is designed to judge evidence, completion, readiness, and risk.
It is read-only by default for review requests.

## What It Covers

### Review Scopes

| Scope | Best for | Typical output |
| --- | --- | --- |
| `change` | PRs, commits, diffs, patch sets, uncommitted changes | merge recommendation, regression findings, impacted areas |
| `project` | Whole repositories, products, systems, delivery-state audits | completion verdict, readiness summary, remediation roadmap |
| `artifact` | Specs, plans, reports, architecture notes, design documents | ambiguity list, requirements gaps, tradeoff notes |

### Review Modes

- `project`
- `readiness`
- `architecture`
- `code`
- `requirements`
- `risk`
- `documentation`

## What Makes It Different

- Routes by scope before mode, so PR review and full-project audit are treated differently
- Uses evidence floors and readiness gates instead of vague impressions
- Supports blocker/high/medium/low severity judgment
- Splits risk into security, privacy, compliance, performance, and reliability
- Includes reusable templates for go/no-go reviews, risk registers, requirements gaps, and remediation plans

## Use It When

- You need more than style feedback
- You need a completion or readiness verdict
- You need a diff review with impact and regression thinking
- You need to review a design document or project plan
- You need a structured risk or requirements review

## Do Not Use It As

- a replacement for linting
- a purely cosmetic refactoring assistant
- proof that a system is safe without real evidence
- a reason to skip tests, QA, or release checks

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

## Outputs You Can Expect

Depending on the request, the skill can produce:

- severity-ordered findings
- completion verdicts
- readiness gate summaries
- risk registers
- requirements gap reports
- architecture tradeoff notes
- remediation roadmaps
- validation plans

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
assets/
  review-banner.svg
```

## License

Released under the MIT License.
