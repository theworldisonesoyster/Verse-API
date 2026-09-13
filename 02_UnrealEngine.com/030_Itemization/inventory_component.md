---
name: inventory_component
slug: unrealenginedotcom/itemization/inventory_component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/itemization/inventory_component
kind: class
module: /UnrealEngine.com/itemization
grade: A
depth: full
status: done
---

# inventory_component class <A>

> Inventory components hold items. An entity with an inventory component can be considered to have an inventory. The inventory component controls which items can enter or exit. They also determine whether an item can be equipped.
> 物品栏组件持有物品。带有物品栏组件的实体即视为拥有物品栏；它控制哪些物品可以进出，并决定物品能否被装备。

`using { /UnrealEngine.com/Itemization }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| component | 在 SceneGraph 中编写逻辑与数据的基类。通过组件可创作可复用的逻辑与数据构件并添加到场景中的实体上。组件是非常底层的构件：可暴露网格/声音等引擎概念、添加伤害/交互等玩法能力、存储物品栏；用一个大组件还是拆成多个小组件由体验需求决定。派生自 component 的类必须指定 <final_super> 才能添加到实体；同一子类组在同一实体上只能有一个实例。生命周期：OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [AddItemEvent](inventory_component_additemevent.md) | listenable(payload) | 物品被添加时触发。先在本物品栏触发，再向上传播到所有祖先物品栏。 |
| [Entity](inventory_component_entity.md) | entity | 此组件的父实体。组件构造时必须提供父实体指针；组件不能在父实体之间移动。 |
| [EquipItemEvent](inventory_component_equipitemevent.md) | listenable(payload) | 物品被装备时触发。先在本物品栏触发，再向上传播到所有祖先物品栏。 |
| [RemoveItemEvent](inventory_component_removeitemevent.md) | listenable(payload) | 物品被移除时触发。先在本物品栏触发，再向上传播到所有祖先物品栏。 |
| [TickEvents](inventory_component_tickevents.md) | ?tick_events | 设置 TickEvents.PrePhysics 与 TickEvents.PostPhysics 回调，在对象物理更新前/后接收逐帧更新。 |
| [UnequipItemEvent](inventory_component_unequipitemevent.md) | listenable(payload) | 物品被卸下时触发。先在本物品栏触发，再向上传播到所有祖先物品栏。 |

### Functions
| Function Name | Description |
| [AddItem](inventory_component_additem.md) | 只把物品加入此物品栏本身（忽略子物品栏）；一件都加不进去则失败。 |
| [AddItemDistribute](inventory_component_additemdistribute.md) | 把物品加入此物品栏（含子物品栏）；一件都加不进去则失败。 |
| [FindInventories](inventory_component_findinventories.md) | 返回此物品栏及其后代物品栏中的全部子物品栏。 |
| [FindItems](inventory_component_finditems.md) | 返回此物品栏及其后代物品栏中的全部物品。 |
| [FindItems](inventory_component_finditems.md) | 返回此物品栏及其后代物品栏中指定类型的全部物品。 |
| GetEquippedItems |  | 返回当前已装备的物品。 | [GetInventories](inventory_component_getinventories.md) | 仅返回此物品栏自身的子物品栏。 |
| [GetItems](inventory_component_getitems.md) | 仅返回此物品栏自身的物品。 |
| [GetItems](inventory_component_getitems.md) | 仅返回此物品栏自身中指定类型的物品。 |
| [IsInScene](inventory_component_isinscene.md) | 若组件当前在场景中则成功。OnAddedToScene 调用后成功；OnRemovingFromScene 调用后失败。 |
| [IsSimulating](inventory_component_issimulating.md) | 若组件当前正在模拟则成功。OnBeginSimulation 调用后成功；OnEndSimulation 调用后失败。 |
| [OnAddedToScene](inventory_component_onaddedtoscene.md) | 当组件通过挂到 simulation 实体（或已在场景中的其他实体）之下而被加入场景时调用。该阶段完成后，查询场景中的组件才是有效的。 |
| [OnBeginSimulation](inventory_component_onbeginsimulation.md) | 当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。 |
| [OnEndSimulation](inventory_component_onendsimulation.md) | 当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。 |
| [OnReceive](inventory_component_onreceive.md) |  |
| [OnReceive](inventory_component_onreceive.md) | 响应场景事件。返回 true 表示消费该事件并阻止向下一个实体继续传播。 |
| [OnRemovingFromScene](inventory_component_onremovingfromscene.md) | 当组件即将被移出场景时调用。父实体被移出场景时其上的组件随之移除。只有已调用过 OnAddedToScene 的组件才会收到 OnRemovingFromScene。 |
| [OnSimulate](inventory_component_onsimulate.md) | 当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。 |
| [RemoveFromEntity](inventory_component_removefromentity.md) | 把组件从实体上移除。被移除的组件会离开场景，且之后只能加回同一个实体。流程经过 OnEndSimulation → OnRemovingFromScene。 |
| [RemoveItem](inventory_component_removeitem.md) | 从此物品栏或其后代物品栏移除物品；移除失败则失败。 |
| [SendDown](inventory_component_senddown.md) | 向此组件发送场景事件，触发 OnReceive。有参与者消费该事件则返回 true。 |
