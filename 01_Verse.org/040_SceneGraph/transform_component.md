---
name: transform_component
slug: versedotorg/scenegraph/transform_component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/transform_component
kind: class
module: /Verse.org/SceneGraph
grade: S
depth: full
status: done
---

# transform_component class 🟦【S级·核心】

> Stores the transforms for an entity, which are used to position the entity.
> 存储实体的变换（transform），用于确定实体的位置。

`using { /Verse.org/SceneGraph }`

## Inheritance Hierarchy

This class is derived from `component`.（本类派生自 component；component 的完整官方描述与生命周期说明见 [component class](component.md)。）

## Members

This class has both data members and functions.（此类兼有数据成员和函数。）

### Data

| Data Member Name | Type | Description |
|---|---|---|
| Entity | entity | 此组件的父实体。组件构造时必须提供父实体指针；组件不能在父实体之间移动。 |
| GlobalTransform | ?transform | 实体当前的世界（全局参照）变换。构造时设置的任何值都会被基于 LocalTransform 的计算结果覆盖。 |
| LocalTransform | ?transform | 相对父实体/原点的局部变换。 |
| Origin | ??origin | 相对默认父实体的替代原点。 |
| TickEvents | ?tick_events | 设置 TickEvents.PrePhysics 与 TickEvents.PostPhysics 回调，可在对象物理更新前/后接收逐帧更新。 |

### Functions

| Function Name | Description |
|---|---|
| IsInScene | 若组件当前在场景中则成功。OnAddedToScene 调用后成功；OnRemovingFromScene 调用后失败。 |
| IsSimulating | 若组件当前正在模拟则成功。OnBeginSimulation 调用后成功；OnEndSimulation 调用后失败。 |
| OnAddedToScene | 当组件通过挂到 simulation 实体（或已在场景中的其他实体）之下而被加入场景时调用。该阶段完成后，查询场景中的组件才是有效的。 |
| OnBeginSimulation | 当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。 |
| OnEndSimulation | 当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。 |
| OnReceive | 响应场景事件。返回 true 表示消费该事件并阻止向下一个实体继续传播。 |
| OnRemovingFromScene | 当组件即将被移出场景时调用。父实体被移出场景时其上的组件随之移除。只有已调用过 OnAddedToScene 的组件才会收到 OnRemovingFromScene。 |
| OnSimulate | 当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。 |
| RemoveFromEntity | 把组件从实体上移除。被移除的组件会离开场景，且之后只能加回**同一个**实体。流程经过 OnEndSimulation → OnRemovingFromScene。 |
| SendDown | 向此组件发送场景事件，触发 OnReceive。有参与者消费该事件则返回 true。 |

## 示例

```verse
using { /Verse.org/SceneGraph }
using { /Verse.org/SpatialMath }

# 读取局部变换：两个 ?transform 字段都是可失败读取
GetPos(TC:transform_component):void =
    if (T := TC.LocalTransform?):
        Print("位置 Forward 分量 = {T.Position.Forward}")
```

## 补充说明

- 本页函数表**没有** Set 位置/旋转类函数——变换通过 `LocalTransform` 等数据成员读写；`GlobalTransform` 是计算结果，构造时赋值会被覆盖（官方 Data 表明示）。
- `LocalTransform`/`GlobalTransform`/`Origin` 均为可失败读取（`?`/`??` 类型），必须写在失败上下文里。
- 相关页面：[component class](component.md)、[vector3 struct](../130_SpatialMath/vector3.md)、[rotation struct](../130_SpatialMath/rotation.md)。
