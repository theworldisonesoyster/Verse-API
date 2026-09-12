# Verse API Reference

> **本资料库（Verse API Reference）基于 [Epic 官方 Verse API Reference](https://dev.epicgames.com/documentation/fortnite/verse-api) 生成**（快照版本：API 42.10，抓取日期 2026-09-13），在官网结构之上增加了中文注解、示例代码与 S/A/B/C 重要程度分级。

## 这是什么

学习 Epic Games 的 Verse 语言时，官方 API 文档是英文的、按字母序排列、缺少"该不该学"的指引。本资料库按官网原本的 **模块层级与页面顺序** 重新组织，并为每个 API 提供：

- 🇨🇳 **中文注解**——翻译官方描述，补充"这是什么/何时用/常见坑"
- 💻 **可运行示例**——每个重要 API 配最小可用代码
- 🎚️ **重要程度分级**——S 核心 / A 常用 / B 进阶 / C 参考，多选过滤见下方"分级索引"

## 收录范围

| 顶层模块 | 收录情况 |
|---|---|
| Verse.org | **全部 16 个子模块**（语言核心＋SceneGraph＋Simulation 等） |
| UnrealEngine.com | **全部 11 个子模块**（含 Temporary 下的 UI/Curves/Diagnostics/SpatialMath） |
| Fortnite.com | 精选 **5 个**：AI、Animation、Characters、Vehicles、UI（依据"可能迁移至 UE6"判断）；Devices 提供**纯索引页** |

收录判断依据与逐模块说明见 [使用说明](使用说明.md)。

## 分级与索引

| 徽标 | 级别 | 说明 | 快速入口 |
|---|---|---|---|
| 🟦 | S 核心 | 几乎每个项目必用 | [S 级索引](90_分级索引/S索引.md) |
| 🟩 | A 常用 | 多数项目会用 | [A 级索引](90_分级索引/A索引.md) |
| 🟨 | B 进阶 | 特定场景使用 | [B 级索引](90_分级索引/B索引.md) |
| ⬜ | C 参考 | 极少用、按需查询 | [C 级索引](90_分级索引/C索引.md) |

## 在线浏览

- **GitBook（推荐阅读）**：本仓库导入 GitBook 后在线查看，左侧边栏即完整层级。
- **交互式页面**：仓库内的 `index.html` 是单文件交互版（双击本地即可打开，或部署到 GitHub Pages），支持**左侧层级树＋分级多选过滤＋搜索**。
- **官方原文对照**：每个页面的 frontmatter 都有 `url` 字段指向官网原始页面。

## 生成与维护

结构清单见 [MANIFEST](MANIFEST.md)，写作规范见 [STYLE_GUIDE](STYLE_GUIDE.md)，各模块生成进度见 [PROGRESS](PROGRESS.md)。所有页面基于 `sources/` 目录中保存的官方页面快照生成，避免臆造 API。
