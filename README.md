# Review Skill

`Review` is an open skill for project review, code review, readiness review, architecture review, requirements review, risk review, and documentation review.

It is designed for cases where a normal code review is not enough and you need a clearer answer to questions like:

- Is this project actually complete?
- Is this change safe to merge?
- Is this release ready?
- What are the biggest risks?
- What should be fixed first?

## What It Does

The skill supports:

- `change` scope for PR, commit, diff, and patch review
- `project` scope for full repository or delivery-state review
- `artifact` scope for reviewing specs, plans, reports, and design documents

It also supports these review modes:

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
- Reusable review templates for common deliverables

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

## Installation

After publishing this repository to GitHub, install the skill with:

```bash
npx skills add https://github.com/wxmb01/review-skill --skill review -g -y
```

## Example Prompts

Use the skill like this:

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

## Output Shapes

The skill can produce:

- severity-ordered findings
- completion verdicts
- readiness gate summaries
- risk registers
- requirements gap reports
- architecture tradeoff notes
- remediation roadmaps

## License

This repository is released under the MIT License.
