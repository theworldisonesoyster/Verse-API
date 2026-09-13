---
name: basic_stackable_component
slug: versedotorg/scenegraph/basic_stackable_component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/basic_stackable_component
kind: class
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# basic_stackable_component class <B>

基础堆叠组件。

`using { /Verse.org/SceneGraph }`

## Inheritance Hierarchy

此类派生自以下层级，起点为 ：
| Name | Description |
| component | 在 SceneGraph 中编写逻辑与数据的基类。通过组件可创作可复用的逻辑与数据构件并添加到场景中的实体上。组件是非常底层的构件：可暴露网格/声音等引擎概念、添加伤害/交互等玩法能力、存储物品栏；用一个大组件还是拆成多个小组件由体验需求决定。派生自 component 的类必须指定 <final_super> 才能添加到实体；同一子类组在同一实体上只能有一个实例。生命周期：OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene。 |
| stackable_component | 挂到实体后，允许其与具有兼容组件的其他实体合并（堆叠）的组件。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| ChangeMaxStackSizeEvent | unknown |  |
| ChangeStackSizeEvent | unknown |  |
| Entity | entity | 此组件的父实体。组件构造时必须提供父实体指针；组件不能在父实体之间移动。 |
| MaxStackSize | ??int | 此组件可容纳的最大数量；未设置则不限。 |
| split_prefab_type | concrete_subtype(castable_subtype(entity)) | 此实体与其他实体合并、或被拆分为新实例时使用的预制体。 |
| StackSize | ?int | 此实体当前堆叠的数量。 |
| TickEvents | ?tick_events | 设置 TickEvents.PrePhysics 与 TickEvents.PostPhysics 回调，在对象物理更新前/后接收逐帧更新。 |

### Functions
| Function Name | Description |
| CanMergeInto | 若此实体可合并进目标实体则成功；与自己合并恒失败。 |
| CanMergeInto | 若此实体可合并进目标实体则成功；与自己合并恒失败。注意合并检查应当双向进行！ |
| IsInScene | 若组件当前在场景中则成功。OnAddedToScene 调用后成功；OnRemovingFromScene 调用后失败。 |
| IsSimulating | 若组件当前正在模拟则成功。OnBeginSimulation 调用后成功；OnEndSimulation 调用后失败。 |
| MergeInto | 尝试把此实体合并进指定实体；无法合并则失败。指定 TargetAmount 时只合并该数量（默认合并整叠）；数量无效则失败。 |
| OnAddedToScene | 当组件通过挂到 simulation 实体（或已在场景中的其他实体）之下而被加入场景时调用。该阶段完成后，查询场景中的组件才是有效的。 |
| OnBeginSimulation |  |
| OnBeginSimulation | 当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。 |
| OnEndSimulation |  |
| OnEndSimulation | 当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。 |
| OnReceive | 响应场景事件。返回 true 表示消费该事件并阻止向下一个实体继续传播。 |
| OnRemovingFromScene | 当组件即将被移出场景时调用。父实体被移出场景时其上的组件随之移除。只有已调用过 OnAddedToScene 的组件才会收到 OnRemovingFromScene。 |
| OnSimulate | 当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。 |
| RemoveFromEntity | 把组件从实体上移除。被移除的组件会离开场景，且之后只能加回同一个实体。流程经过 OnEndSimulation → OnRemovingFromScene。 |
| SendDown | 向此组件发送场景事件，触发 OnReceive。有参与者消费该事件则返回 true。 |
| SetMaxStackSize | 设置此组件的最大堆叠数。NewMaxStackSize 为 false 表示不限；ClampStackSize 为 true 时会把当前堆叠数钳制到新上限。 |
| SetStackSize | 设置此组件的堆叠数。给定值无效（负数或超过 MaxStackSize）时堆叠数不变。 |
| Split |  |
| Split |  |
