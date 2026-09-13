---
name: Simulation
slug: versedotorg/simulation
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation
kind: module
module: /Verse.org
grade: S
depth: brief
status: done
---

# Simulation module <S>

> Verse path: `/Verse.org` · Module import path: `/Verse.org/Simulation`
> 对局世界的基本概念模块：谁在对局里（agent/player）、怎么分组（team）、这是哪一局（session），以及 Sleep、editable_\* 等基础函数。

`using { /Verse.org/Simulation }`

- Verse.org
- Simulation [Tags](010_Tags/_overview.md)

## Classes and Structs

| Name | Description |
|---|---|
| [agent](agent.md) | 对局参与者的抽象（真人玩家或 AI 单位）。 |
| [player](player.md) | 对局中的真人玩家，agent 的子类。 |
| [session](session.md) | 每回合一个实例的类型；用 GetSession 获取当前实例，可配合 weak_map 实现全局变量。注意：未来可能改为每局一个实例，勿依赖回合级行为。 |
| [team](team.md) | 表示对局中的一支队伍。 |

## Functions

| Name | Description |
|---|---|
| [editable_slider](editable_slider.md) | 参数化类型构造器：生成详情面板滑条类。 |
| [editable_number](editable_number.md) | 参数化类型构造器：生成详情面板数字输入类。 |
| [editable_vector_slider](editable_vector_slider.md) | 参数化类型构造器：生成详情面板三维向量滑条类。 |
| [editable_vector_number](editable_vector_number.md) | 参数化类型构造器：生成详情面板三维向量数字输入类。 |
| [GetSession](getsession.md) | 返回当前回合对应的 session 实例；可配合 weak_map 实现全局变量。 |
| [Sleep](sleep.md) | 暂停指定秒数后恢复；0 等下一帧、Inf 永久等待（仅取消时返回）、负值立即完成不让出。 |
| [GetSimulationElapsedTime](getsimulationelapsedtime.md) | 获取世界开始模拟以来经过的秒数。 |

## Enumerations

| Name | Description |
|---|---|
| [session_environment](session_environment.md) | 指明当前对局环境类型（Edit / Private / Live）。 |

## 补充说明

- 写任何 Verse 玩法逻辑几乎都要 `using { /Verse.org/Simulation }`——它提供参与者、队伍、时间与编辑器控件的基本类型。
- agent/player 继承自 SceneGraph 的 entity，因此也拥有实体与标签两族函数（详见各自页面）。
- 相关页面：[Verse.org module](../_overview.md)、[entity class](../040_SceneGraph/entity.md)。
