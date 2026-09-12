---
name: component
slug: versedotorg/scenegraph/component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component
kind: class
module: /Verse.org/SceneGraph
grade: S
depth: full
status: done
---

# component 🟦【S级·核心】

> Base class for authoring logic and data in the SceneGraph.
> SceneGraph 中编写逻辑与数据的基类——实体的一切"行为"都挂在组件上。

## 这是什么

组件是 SceneGraph 的"能力插件"：[entity](entity.md) 只是节点，功能（变换、网格、灯、音效、你写的玩法逻辑）全是组件。写自定义组件 = 继承 `component`，重写生命周期函数：

| 生命周期 | 时机（官方保证顺序） |
|---|---|
| `OnAddedToScene` | 挂进场景后；此后可查询场景中的组件 |
| `OnBeginSimulation` | 开始模拟；适合注册 Tick 回调 |
| `OnSimulate` | 可挂起（`<suspends>`）的常驻逻辑写这里 |
| `OnEndSimulation` / `OnRemovingFromScene` | 收尾 |

## 签名

```verse
component<public><native> := class<native>:
    # Data
    Entity<public>:entity              # 父实体（构造时指定，不可更换）
    TickEvents<public>:?tick_events    # 帧回调注册器
    # 生命周期（节选）
    OnAddedToScene<public>()<suspends>:void
    OnBeginSimulation<public>():void
    OnSimulate<public>()<suspends>:void
```

## 最小示例

```verse
using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }

# 自定义组件：每秒数一拍（节拍器示例）
beat_component := class(component):
    var Beat:int = 0

    OnSimulate<override>()<suspends>:void =
        loop:
            Sleep(1.0)
            set Beat += 1
            Print("♪ {Beat}")
```

## 常用成员

| 成员 | 说明 | 级别 |
|---|---|---|
| `Entity` | 所属实体（组件不能换父） | 🟦 S |
| `TickEvents` | 注册每帧/定时回调 | 🟩 A |
| 生命周期四件套 | 见上表 | 🟦 S |

## 何时用 / 何时不用

- 用：一切新写法的玩法逻辑——把逻辑做成组件挂到实体上。
- 不用：老式 creative_device 脚本（仍完全可用）；同一份逻辑别两套混写。

## 常见坑

- 生命周期是**固定顺序**：OnAddedToScene → OnBeginSimulation → OnSimulate；别在 OnAddedToScene 里做需要"场景已模拟"的查询。
- 组件的 `Entity` 是构造时定死的，"移动组件"要拆下重挂。

## 相关页面

- [entity](entity.md)
- [transform_component](transform_component.md)
- [tick_events](tick_events.md)
