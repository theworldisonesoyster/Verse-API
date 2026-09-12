---
name: Simulation
slug: versedotorg/simulation
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation
kind: module
module: /Verse.org/Simulation
grade: S
depth: brief
status: done
---

# Simulation 🟦【S级·核心】

> 官网对本模块无单独描述；本页为模块总览。
> Simulation 模块提供"对局世界"的基本概念：谁在对局里（agent/player）、怎么分组（team）、这是哪一局（session），以及控制执行节奏的 Sleep 等函数。

## 这是什么

写任何 Verse 玩法逻辑都绕不开这个模块：

- **[agent](agent.md)**（S）——"参与者"的抽象：可能是真人玩家，也可能是 AI 单位。大多数设备事件回传的是 agent，先判别再转成 player。
- **[player](player.md)**（S）——真人玩家，继承自 agent；查状态、给道具最终都要落到具体 player 上。
- **[team](team.md)**（A）——队伍，对局中的分组单位。
- **[session](session.md)**（A）——每回合一个实例的全局对象，常配合 `weak_map` 实现"全局变量"。
- **[Sleep](sleep.md)**（S）——暂停当前协程若干秒，几乎每个异步玩法都要用。
- **[editable_\*](editable_number.md)**（S/A）——把脚本参数暴露到 UEFN 详情面板的数字/滑条控件，写自定义设备必备。

子模块 [Tags](010_Tags/_overview.md) 提供通用标签系统（打标、查询、过滤）。

## 使用前提

```verse
using { /Verse.org/Simulation }
```

## 成员一览

| 成员 | 类型 | 一句话 | 级别 |
|---|---|---|---|
| [agent](agent.md) | 类 | 参与者的抽象基类（玩家或 AI） | 🟦 S |
| [player](player.md) | 类 | 真人玩家，继承 agent | 🟦 S |
| [team](team.md) | 类 | 队伍 | 🟩 A |
| [session](session.md) | 类 | 每回合一个实例的全局对象 | 🟩 A |
| [Sleep](sleep.md) | 函数 | 暂停当前协程若干秒 | 🟦 S |
| [GetSession](getsession.md) | 函数 | 取当前回合的 session | 🟩 A |
| [GetSimulationElapsedTime](getsimulationelapsedtime.md) | 函数 | 世界开始模拟以来经过的秒数 | 🟩 A |
| [editable_slider](editable_slider.md) | 参数化类 | 详情面板滑条 | 🟦 S |
| [editable_number](editable_number.md) | 参数化类 | 详情面板数字输入 | 🟦 S |
| [editable_vector_slider](editable_vector_slider.md) | 参数化类 | 三维向量滑条 | 🟩 A |
| [editable_vector_number](editable_vector_number.md) | 参数化类 | 三维向量数字输入 | 🟩 A |
| [session_environment](session_environment.md) | 枚举 | 对局环境：编辑/私人/线上 | 🟨 B |

## 相关页面

- [Verse.org 总览](../_overview.md) —— 语言核心与模块地图
- [entity](../040_SceneGraph/entity.md) —— agent/player 的 SceneGraph 基类
- [Tags 子模块](010_Tags/_overview.md)
