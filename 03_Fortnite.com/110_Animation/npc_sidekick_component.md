---
name: npc_sidekick_component
slug: fortnitedotcom/ai/npc_sidekick_component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/npc_sidekick_component
kind: class
module: /Fortnite.com/ai
grade: B
depth: brief
status: done
---

# npc_sidekick_component class <B>

> Component to manage functionality specifically for an NPC Sidekick.
> 管理 NPC Sidekick 专属功能的组件。

`using { /Fortnite.com/AI }`

## Inheritance Hierarchy

此类派生自以下层级，起点为 ：
| Name | Description |
| component | 在 SceneGraph 中编写逻辑与数据的基类。通过组件可创作可复用的逻辑与数据构件并添加到场景中的实体上。组件是非常底层的构件：可暴露网格/声音等引擎概念、添加伤害/交互等玩法能力、存储物品栏；用一个大组件还是拆成多个小组件由体验需求决定。派生自 component 的类必须指定 <final_super> 才能添加到实体；同一子类组在同一实体上只能有一个实例。生命周期：OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene。 |
| sidekick_component | 管理所有 Sidekick 类型共享功能的组件。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [ChangeMoodEvent](npc_sidekick_component_changemoodevent.md) | listenable(payload) | Sidekick 情绪变化时触发；返回旧情绪与新情绪。 |
| [ChangeMoodEvent](npc_sidekick_component_changemoodevent.md) | listenable(payload) | Sidekick 情绪变化时触发；返回旧情绪与新情绪。 |
| [Entity](npc_sidekick_component_entity.md) | entity | 此组件的父实体。组件构造时必须提供父实体指针；组件不能在父实体之间移动。 |
| [IdleAnticsEnabled](npc_sidekick_component_idleanticsenabled.md) | ?logic | 启用/禁用 Sidekick 的滑稽动作（待机个性动画）；默认启用。 |
| [MoodOverride](npc_sidekick_component_moodoverride.md) | ??sidekick_mood | 默认情况下 Sidekick 会根据游戏中的行为改变情绪；设置此值可把 Sidekick 锁定到指定情绪，覆盖自动情绪系统。 |
| [MoodOverride](npc_sidekick_component_moodoverride.md) | ??sidekick_mood | 默认情况下 Sidekick 会根据游戏中的行为改变情绪；设置此值可把 Sidekick 锁定到指定情绪，覆盖自动情绪系统。 |
| [StartPlayReactionEvent](npc_sidekick_component_startplayreactionevent.md) | listenable(payload) | Sidekick 开始播放反应动作时触发；返回开始播放的反应。 |
| [StartPlayReactionEvent](npc_sidekick_component_startplayreactionevent.md) | listenable(payload) | Sidekick 开始播放反应动作时触发；返回开始播放的反应。 |
| [StopPlayReactionEvent](npc_sidekick_component_stopplayreactionevent.md) | listenable(payload) | Sidekick 结束播放反应动作时触发；返回播放过的反应。 |
| [StopPlayReactionEvent](npc_sidekick_component_stopplayreactionevent.md) | listenable(payload) | Sidekick 结束播放反应动作时触发；返回播放过的反应。 |
| [TickEvents](npc_sidekick_component_tickevents.md) | ?tick_events | 设置 TickEvents.PrePhysics 与 TickEvents.PostPhysics 回调，在对象物理更新前/后接收逐帧更新。 |

### Functions
| Function Name | Description |
| [ApplyEquippedSidekickCosmetic](npc_sidekick_component_applyequippedsidekickcosmetic.md) | 把该代理当前装备的 Sidekick 的外观与自定义应用到这个 Sidekick NPC。若 NPC 未使用 FortniteSidekick 外观，或该代理的柜子中没有装备 Sidekick，则失败。 |
| [GetMood](npc_sidekick_component_getmood.md) | 获取 Sidekick 当前情绪。 |
| [GetMood](npc_sidekick_component_getmood.md) | 获取 Sidekick 当前情绪。 |
| [IsInScene](npc_sidekick_component_isinscene.md) | 若组件当前在场景中则成功。OnAddedToScene 调用后成功；OnRemovingFromScene 调用后失败。 |
| [IsSimulating](npc_sidekick_component_issimulating.md) | 若组件当前正在模拟则成功。OnBeginSimulation 调用后成功；OnEndSimulation 调用后失败。 |
| [OnAddedToScene](npc_sidekick_component_onaddedtoscene.md) | 当组件通过挂到 simulation 实体（或已在场景中的其他实体）之下而被加入场景时调用。该阶段完成后，查询场景中的组件才是有效的。 |
| [OnBeginSimulation](npc_sidekick_component_onbeginsimulation.md) | 当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。 |
| [OnEndSimulation](npc_sidekick_component_onendsimulation.md) | 当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。 |
| [OnReceive](npc_sidekick_component_onreceive.md) | 响应场景事件。返回 true 表示消费该事件并阻止向下一个实体继续传播。 |
| [OnRemovingFromScene](npc_sidekick_component_onremovingfromscene.md) | 当组件即将被移出场景时调用。父实体被移出场景时其上的组件随之移除。只有已调用过 OnAddedToScene 的组件才会收到 OnRemovingFromScene。 |
| [OnSimulate](npc_sidekick_component_onsimulate.md) | 当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。 |
| [PlayReaction](npc_sidekick_component_playreaction.md) | 请求在 Sidekick 上播放给定反应。不保证立即播放；应通过 StartPlayReactionEvent 监视。无法播放该反应则失败。 |
| [PlayReaction](npc_sidekick_component_playreaction.md) | 请求在 Sidekick 上播放给定反应。不保证立即播放；应通过 StartPlayReactionEvent 监视。无法播放该反应则失败。 |
| [RemoveFromEntity](npc_sidekick_component_removefromentity.md) | 把组件从实体上移除。被移除的组件会离开场景，且之后只能加回同一个实体。流程经过 OnEndSimulation → OnRemovingFromScene。 |
| [SendDown](npc_sidekick_component_senddown.md) | 向此组件发送场景事件，触发 OnReceive。有参与者消费该事件则返回 true。 |
