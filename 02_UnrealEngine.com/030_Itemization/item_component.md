---
name: item_component
slug: unrealenginedotcom/itemization/item_component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/item_component
kind: class
module: /UnrealEngine.com/itemization
grade: A
depth: full
status: done
---

# item_component class <A>

> Anything using this component should be considered an item. Required to interact with inventories.
> 使用此组件的实体应视为物品；与物品栏交互必需。

`using { /UnrealEngine.com/Itemization }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| component | 在 SceneGraph 中编写逻辑与数据的基类。通过组件可创作可复用的逻辑与数据构件并添加到场景中的实体上。组件是非常底层的构件：可暴露网格/声音等引擎概念、添加伤害/交互等玩法能力、存储物品栏；用一个大组件还是拆成多个小组件由体验需求决定。派生自 component 的类必须指定 <final_super> 才能添加到实体；同一子类组在同一实体上只能有一个实例。生命周期：OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| Categories | []item_category | 添加一个或多个类别实例，帮助定义和组织此物品。 |
| ChangeEquippedEvent | listenable(payload) | 此物品被装备/卸下时广播。 |
| ChangeInventoryEvent | listenable(payload) | 此物品更换物品栏时广播。 |
| Entity | entity | 此组件的父实体。组件构造时必须提供父实体指针；组件不能在父实体之间移动。 |
| TickEvents | ?tick_events | 设置 TickEvents.PrePhysics 与 TickEvents.PostPhysics 回调，在对象物理更新前/后接收逐帧更新。 |

### Functions
| Function Name | Description |
| Drop | 把物品从物品栏移出并放入模拟世界。也适用于「孤儿」物品（不在世界或任何物品栏中）。物品已是拾取物则失败。除与物品栏解除父子关系外，不改变物品的变换。 |
| Drop | 把物品从物品栏移出并放入模拟世界。也适用于孤儿物品。物品已在世界中则失败。被丢弃物品的变换会设为 WorldTransform。 |
| Equip | 尝试在物品当前所在物品栏中装备它；不在物品栏中，或 equip_item_query_event 查询后仍含错误，则失败。 |
| GetParentInventory | 返回此物品当前所在的 inventory_component；找不到有效父物品栏则失败。 |
| IsEquipped | 若此物品当前在物品栏中且已装备则成功。 |
| IsInScene | 若组件当前在场景中则成功。OnAddedToScene 调用后成功；OnRemovingFromScene 调用后失败。 |
| IsSimulating | 若组件当前正在模拟则成功。OnBeginSimulation 调用后成功；OnEndSimulation 调用后失败。 |
| OnAddedToScene | 当组件通过挂到 simulation 实体（或已在场景中的其他实体）之下而被加入场景时调用。该阶段完成后，查询场景中的组件才是有效的。 |
| OnBeginSimulation |  |
| OnBeginSimulation | 当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。 |
| OnEndSimulation |  |
| OnEndSimulation | 当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。 |
| OnReceive | 响应场景事件。返回 true 表示消费该事件并阻止向下一个实体继续传播。 |
| OnRemovingFromScene | 当组件即将被移出场景时调用。父实体被移出场景时其上的组件随之移除。只有已调用过 OnAddedToScene 的组件才会收到 OnRemovingFromScene。 |
| OnSimulate | 当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。 |
| PickUp | 物品已在某物品栏中，或该物品栏无法接收此物品，则失败。 |
| RemoveFromEntity | 把组件从实体上移除。被移除的组件会离开场景，且之后只能加回同一个实体。流程经过 OnEndSimulation → OnRemovingFromScene。 |
| SendDown | 向此组件发送场景事件，触发 OnReceive。有参与者消费该事件则返回 true。 |
| Unequip | 尝试卸下此物品；不在物品栏、未装备，或 unequip_item_query_event 查询后仍含错误，则失败。 |
