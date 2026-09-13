---
name: guard_awareness_component
slug: fortnitedotcom/ai/guard_awareness_component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/guard_awareness_component
kind: class
module: /Fortnite.com/ai
grade: B
depth: brief
status: done
---

# guard_awareness_component class <B>

> Fortnite Guard perception management
> 堡垒之夜 Guard 的感知管理。

`using { /Fortnite.com/AI }`

## Inheritance Hierarchy

此类派生自以下层级，起点为 ：
| Name | Description |
| component | 在 SceneGraph 中编写逻辑与数据的基类。通过组件可创作可复用的逻辑与数据构件并添加到场景中的实体上。组件是非常底层的构件：可暴露网格/声音等引擎概念、添加伤害/交互等玩法能力、存储物品栏；用一个大组件还是拆成多个小组件由体验需求决定。派生自 component 的类必须指定 <final_super> 才能添加到实体；同一子类组在同一实体上只能有一个实例。生命周期：OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene。 |
| npc_awareness_component | 堡垒之夜 NPC 的感知管理。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [AlertLevel](guard_awareness_component_alertlevel.md) | ?guard_alert_level | 当前警戒级别。 |
| [AlertLevelChangeEvent](guard_awareness_component_alertlevelchangeevent.md) | listenable(payload) | 警戒级别变化时的事件。 |
| [DetectedObstacle](guard_awareness_component_detectedobstacle.md) | ??entity | 可能被侦测到的障碍物。 |
| [DetectedTargets](guard_awareness_component_detectedtargets.md) | ?[]npc_target_info | 所有已侦测目标的信息。 |
| [DetectObstacleEvent](guard_awareness_component_detectobstacleevent.md) | listenable(payload) | 侦测到新障碍物时的事件。 |
| [DetectTargetEvent](guard_awareness_component_detecttargetevent.md) | listenable(payload) | 侦测到目标时的事件。 |
| [Entity](guard_awareness_component_entity.md) | entity | 此组件的父实体。组件构造时必须提供父实体指针；组件不能在父实体之间移动。 |
| [ForgetObstacleEvent](guard_awareness_component_forgetobstacleevent.md) | listenable(payload) | 当前障碍物被遗忘时的事件。 |
| [ForgetTargetEvent](guard_awareness_component_forgettargetevent.md) | listenable(payload) | 目标被遗忘时的事件。 |
| [HearTargetEvent](guard_awareness_component_heartargetevent.md) | listenable(payload) | 听到目标时的事件（听觉感知须处于激活状态）。 |
| [PrimaryThreat](guard_awareness_component_primarythreat.md) | ??npc_target_info | 主要威胁的信息。 |
| [PrimaryThreatChangeEvent](guard_awareness_component_primarythreatchangeevent.md) | listenable(payload) | 主要威胁变化时的事件。 |
| [SeeTargetEvent](guard_awareness_component_seetargetevent.md) | listenable(payload) | 看到目标时的事件（视觉感知须处于激活状态）。 |
| [TickEvents](guard_awareness_component_tickevents.md) | ?tick_events | 设置 TickEvents.PrePhysics 与 TickEvents.PostPhysics 回调，在对象物理更新前/后接收逐帧更新。 |
| [TouchTargetEvent](guard_awareness_component_touchtargetevent.md) | listenable(payload) | 触到目标时的事件（触觉感知须处于激活状态）。 |

### Functions
| Function Name | Description |
| [GetAlertLevel](guard_awareness_component_getalertlevel.md) | 获取对特定目标的当前警戒级别。 |
| [IsInScene](guard_awareness_component_isinscene.md) | 若组件当前在场景中则成功。OnAddedToScene 调用后成功；OnRemovingFromScene 调用后失败。 |
| [IsSimulating](guard_awareness_component_issimulating.md) | 若组件当前正在模拟则成功。OnBeginSimulation 调用后成功；OnEndSimulation 调用后失败。 |
| [OnAddedToScene](guard_awareness_component_onaddedtoscene.md) | 当组件通过挂到 simulation 实体（或已在场景中的其他实体）之下而被加入场景时调用。该阶段完成后，查询场景中的组件才是有效的。 |
| [OnBeginSimulation](guard_awareness_component_onbeginsimulation.md) | 当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。 |
| [OnEndSimulation](guard_awareness_component_onendsimulation.md) | 当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。 |
| [OnReceive](guard_awareness_component_onreceive.md) | 响应场景事件。返回 true 表示消费该事件并阻止向下一个实体继续传播。 |
| [OnRemovingFromScene](guard_awareness_component_onremovingfromscene.md) | 当组件即将被移出场景时调用。父实体被移出场景时其上的组件随之移除。只有已调用过 OnAddedToScene 的组件才会收到 OnRemovingFromScene。 |
| [OnSimulate](guard_awareness_component_onsimulate.md) | 当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。 |
| [RemoveFromEntity](guard_awareness_component_removefromentity.md) | 把组件从实体上移除。被移除的组件会离开场景，且之后只能加回同一个实体。流程经过 OnEndSimulation → OnRemovingFromScene。 |
| [SendDown](guard_awareness_component_senddown.md) | 向此组件发送场景事件，触发 OnReceive。有参与者消费该事件则返回 true。 |
