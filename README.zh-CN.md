![Review Skill Banner](./assets/review-banner.svg)

# Review Skill

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](./LICENSE)
[![Release](https://img.shields.io/github/v/release/wxmb01/review-skill?style=flat-square)](https://github.com/wxmb01/review-skill/releases)
[![Stars](https://img.shields.io/github/stars/wxmb01/review-skill?style=flat-square)](https://github.com/wxmb01/review-skill/stargazers)

一个面向项目评审的开源 skill，支持项目审查、代码审查、就绪度审查、架构审查、需求审查、风险审查和文档审查。

[English](./README.md) | [简体中文](./README.zh-CN.md)

## 一眼看懂它做什么

`Review` 是为“普通代码审查已经不够用”的场景设计的。

它重点回答这类问题：

- 这个项目到底做完了吗？
- 这次改动可以安全合并吗？
- 现在能提交、上线或交付了吗？
- 最大的风险在哪里？
- 应该优先修什么？

和只关注代码风格的 review 不同，`Review` 更强调证据、完成度、就绪门槛和风险判断。  
在 review 请求下，它默认只读分析，不会擅自改文件。

## 它覆盖哪些场景

### Review 范围

| 范围 | 最适合的场景 | 常见输出 |
| --- | --- | --- |
| `change` | PR、commit、diff、patch、未提交改动 | 合并建议、回归风险、影响范围 |
| `project` | 整个仓库、完整项目、服务系统、交付状态 | 完成度结论、就绪摘要、整改路线图 |
| `artifact` | 需求文档、设计文档、计划、报告、检查表 | 歧义清单、需求缺口、取舍说明 |

### Review 模式

- `project`
- `readiness`
- `architecture`
- `code`
- `requirements`
- `risk`
- `documentation`

## 它和普通 Review 的区别

- 先判断 review 范围，再判断 review 模式
- 用证据底线和 readiness gates 做判断，而不是只凭感觉
- 支持 blocker/high/medium/low 严重级别
- 风险会继续拆成安全、隐私、合规、性能、可靠性
- 自带 go/no-go、risk register、requirements gaps、整改路线图等模板

## 适合什么时候用

- 你需要的不只是代码风格反馈
- 你想判断项目是否真正完成
- 你想审查一次改动是否安全
- 你想判断能不能提交、上线、交付
- 你想审查设计文档、计划或需求是否靠谱

## 不适合把它当成

- lint 的替代品
- 单纯的代码美化工具
- 没有证据时替代 QA 的“安全证明”
- 跳过测试、发布检查或人工判断的理由

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

## 你通常会得到什么输出

按任务不同，它可以输出：

- 按严重级别排序的问题列表
- 完成度结论
- 就绪门槛摘要
- 风险登记表
- 需求缺口报告
- 架构取舍说明
- 整改路线图
- 验证计划

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
assets/
  review-banner.svg
```

## 许可证

本仓库使用 MIT License 开源。
