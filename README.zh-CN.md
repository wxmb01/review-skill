# Review Skill

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](./LICENSE)
[![Release](https://img.shields.io/github/v/release/wxmb01/review-skill?style=flat-square)](https://github.com/wxmb01/review-skill/releases)
[![Stars](https://img.shields.io/github/stars/wxmb01/review-skill?style=flat-square)](https://github.com/wxmb01/review-skill/stargazers)

一个面向项目评审的开源 skill，支持项目审查、代码审查、就绪度审查、架构审查、需求审查、风险审查和文档审查。

[English](./README.md) | [简体中文](./README.zh-CN.md)

## 这个 Skill 解决什么问题

普通代码审查通常只盯着代码实现本身，但很多真实问题其实是：

- 这个项目到底做完了吗？
- 这次改动可以安全合并吗？
- 现在能提交、上线或交付了吗？
- 最大的风险在哪里？
- 应该优先修什么？

`Review` 就是为这些问题设计的。  
它在 review 场景下默认只读，不会擅自修改文件；它更强调证据、完成度、就绪门槛和风险判断，而不只是代码风格评论。

## 它覆盖哪些场景

### Review 范围

| 范围 | 适用场景 |
| --- | --- |
| `change` | PR、commit、diff、patch、未提交改动 |
| `project` | 整个仓库、完整项目、服务系统、交付状态 |
| `artifact` | 需求文档、设计文档、计划、报告、检查表 |

### Review 模式

- `project`
- `readiness`
- `architecture`
- `code`
- `requirements`
- `risk`
- `documentation`

## 核心能力

- review 请求默认只读分析
- 先判断 review 范围，再判断 review 模式
- 基于证据判断完成度和就绪度
- 支持严重级别和 blocker/high 风险判断
- 支持 readiness gates 和可选 scorecard
- 支持安全、隐私、合规、性能、可靠性等风险子域
- 提供 diff review、go/no-go、risk register、整改路线图等模板

## 能输出什么

按不同任务，它可以输出：

- 按严重级别排序的问题列表
- 完成度结论
- 就绪门槛摘要
- 风险登记表
- 需求缺口报告
- 架构取舍说明
- 整改路线图
- 验证计划

## 安装方式

直接从 GitHub 安装：

```bash
npx skills add https://github.com/wxmb01/review-skill --skill review -g -y
```

## 示例提示词

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

## 仓库结构

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

## 许可证

本仓库使用 MIT License 开源。
