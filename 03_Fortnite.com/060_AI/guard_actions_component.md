---
name: guard_actions_component
slug: fortnitedotcom/ai/guard_actions_component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/guard_actions_component
kind: class
module: /Fortnite.com/ai
grade: B
depth: brief
status: done
---

# guard_actions_component class <B>

> Fortnite Guards AI actions management
> 堡垒之夜 Guard（守卫）的 AI 行为管理。

`using { /Fortnite.com/AI }`

## Inheritance Hierarchy

此类派生自以下层级，起点为 ：
| Name | Description |
| component | 在 SceneGraph 中编写逻辑与数据的基类。通过组件可创作可复用的逻辑与数据构件并添加到场景中的实体上。组件是非常底层的构件：可暴露网格/声音等引擎概念、添加伤害/交互等玩法能力、存储物品栏；用一个大组件还是拆成多个小组件由体验需求决定。派生自 component 的类必须指定 <final_super> 才能添加到实体；同一子类组在同一实体上只能有一个实例。生命周期：OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene。 |
| npc_actions_component | 堡垒之夜 NPC 的 AI 行为管理。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [Entity](guard_actions_component_entity.md) | entity | 此组件的父实体。组件构造时必须提供父实体指针；组件不能在父实体之间移动。 |
| [MovementSpeedMultiplier](guard_actions_component_movementspeedmultiplier.md) | ?float | 移动速度倍率（钳制在 0.5~2 之间）。 |
| [TickEvents](guard_actions_component_tickevents.md) | ?tick_events | 设置 TickEvents.PrePhysics 与 TickEvents.PostPhysics 回调，在对象物理更新前/后接收逐帧更新。 |

### Functions
| Function Name | Description |
| [Attack](guard_actions_component_attack.md) | 攻击目标；目标必须已被侦测。 |
| [Crouch](guard_actions_component_crouch.md) | 切换为蹲伏姿态；不中断则永不完成。 |
| [Focus](guard_actions_component_focus.md) | 看向指定位置。LockFocus 为 false 时，NPC 面向该位置后动作即停止。 |
| [Focus](guard_actions_component_focus.md) | 看向指定实体。LockFocus 为 false 时，NPC 面向该实体后动作即停止。 |
| [GetCurrentDestination](guard_actions_component_getcurrentdestination.md) | 返回角色当前的导航目的地。 |
| [Idle](guard_actions_component_idle.md) | 保持空闲指定时长。 |
| [IsInScene](guard_actions_component_isinscene.md) | 若组件当前在场景中则成功。OnAddedToScene 调用后成功；OnRemovingFromScene 调用后失败。 |
| [IsSimulating](guard_actions_component_issimulating.md) | 若组件当前正在模拟则成功。OnBeginSimulation 调用后成功；OnEndSimulation 调用后失败。 |
| [Jump](guard_actions_component_jump.md) | 触发一次跳跃。 |
| [MoveInRangeToAttack](guard_actions_component_moveinrangetoattack.md) | 移动到可攻击当前目标的范围内。 |
| [NavigateTo](guard_actions_component_navigateto.md) | 向指定的导航目标移动。 |
| [OnAddedToScene](guard_actions_component_onaddedtoscene.md) | 当组件通过挂到 simulation 实体（或已在场景中的其他实体）之下而被加入场景时调用。该阶段完成后，查询场景中的组件才是有效的。 |
| [OnBeginSimulation](guard_actions_component_onbeginsimulation.md) | 当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。 |
| [OnEndSimulation](guard_actions_component_onendsimulation.md) | 当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。 |
| [OnReceive](guard_actions_component_onreceive.md) | 响应场景事件。返回 true 表示消费该事件并阻止向下一个实体继续传播。 |
| [OnRemovingFromScene](guard_actions_component_onremovingfromscene.md) | 当组件即将被移出场景时调用。父实体被移出场景时其上的组件随之移除。只有已调用过 OnAddedToScene 的组件才会收到 OnRemovingFromScene。 |
| [OnSimulate](guard_actions_component_onsimulate.md) | 当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。 |
| [PlayRandomEmote](guard_actions_component_playrandomemote.md) | 从角色表情库中随机播放一个表情。 |
| [RemoveFromEntity](guard_actions_component_removefromentity.md) | 把组件从实体上移除。被移除的组件会离开场景，且之后只能加回同一个实体。流程经过 OnEndSimulation → OnRemovingFromScene。 |
| [Revive](guard_actions_component_revive.md) | 复活指定目标。 |
| [RoamAround](guard_actions_component_roamaround.md) | 在当前位置附近游荡。可用 Tether 指定半径；否则 Guard 会随处游荡。 |
| [SendDown](guard_actions_component_senddown.md) | 向此组件发送场景事件，触发 OnReceive。有参与者消费该事件则返回 true。 |
| [Slide](guard_actions_component_slide.md) | 触发一次滑铲。 |
| [StandUp](guard_actions_component_standup.md) | 回到站立状态。 |
| [StopNavigation](guard_actions_component_stopnavigation.md) | 停止导航。 |
| [Tether](guard_actions_component_tether.md) | 把 NPC 拴定到某个位置。Radius 单位为厘米。 |
| [Tether](guard_actions_component_tether.md) | 把 NPC 拴定到某个实体。Radius 单位为厘米。 |
| [Untether](guard_actions_component_untether.md) | 解除 NPC 的拴定。 |
