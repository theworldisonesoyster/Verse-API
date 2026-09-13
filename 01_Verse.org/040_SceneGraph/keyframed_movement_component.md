---
name: keyframed_movement_component
slug: versedotorg/scenegraph/keyframedmovement/keyframed_movement_component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/keyframedmovement/keyframed_movement_component
kind: class
module: /Verse.org/scenegraph/keyframedmovement
grade: A
depth: full
status: done
---

# keyframed_movement_component class <A>

> Provides teleportation and simple keyframe-based animation for an entity. Animations play back in the Pre-Physics tick phase. When animating an entity with a parent_constraint, animation will be relative to the parent entity.
> 为实体提供传送与基于关键帧的简单动画；动画在物理前置（Pre-Physics）tick 阶段播放。

`using { /Verse.org/SceneGraph/KeyframedMovement }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| component | 在 SceneGraph 中编写逻辑与数据的基类。通过组件可创作可复用的逻辑与数据构件并添加到场景中的实体上。组件是非常底层的构件：可暴露网格/声音等引擎概念、添加伤害/交互等玩法能力、存储物品栏；用一个大组件还是拆成多个小组件由体验需求决定。派生自 component 的类必须指定 <final_super> 才能添加到实体；同一子类组在同一实体上只能有一个实例。生命周期：OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [Duration](keyframed_movement_component_duration.md) | ??float | 获取此关键帧动画将花费的秒数；无固定时长时（如循环动画）失败。 |
| [Entity](keyframed_movement_component_entity.md) | entity | 此组件的父实体。组件构造时必须提供父实体指针；组件不能在父实体之间移动。 |
| [FinishedEvent](keyframed_movement_component_finishedevent.md) | unknown | 获取动画结束时触发的事件；动画时长无限则失败。 |
| [KeyframeReachedEvent](keyframed_movement_component_keyframereachedevent.md) | unknown | 到达任一关键帧时触发。载荷：（关键帧序号:int, 是否反向:logic）。 |
| [PausedEvent](keyframed_movement_component_pausedevent.md) | unknown | 获取动画暂停时触发的事件。 |
| [PlayedEvent](keyframed_movement_component_playedevent.md) | unknown | 获取动画开始或恢复播放时触发的事件。 |
| [StoppedEvent](keyframed_movement_component_stoppedevent.md) | unknown | 获取动画停止时触发的事件。 |
| [TickEvents](keyframed_movement_component_tickevents.md) | ?tick_events | 设置 TickEvents.PrePhysics 与 TickEvents.PostPhysics 回调，在对象物理更新前/后接收逐帧更新。 |

### Functions
| Function Name | Description |
| [HasValidAnimation](keyframed_movement_component_hasvalidanimation.md) | 是否存在可播放的有效关键帧集？ |
| [IsInScene](keyframed_movement_component_isinscene.md) | 若组件当前在场景中则成功。OnAddedToScene 调用后成功；OnRemovingFromScene 调用后失败。 |
| [IsPaused](keyframed_movement_component_ispaused.md) | 动画是否已暂停？ |
| [IsPlaying](keyframed_movement_component_isplaying.md) | 动画是否正在播放？ |
| [IsSimulating](keyframed_movement_component_issimulating.md) | 若组件当前正在模拟则成功。OnBeginSimulation 调用后成功；OnEndSimulation 调用后失败。 |
| [OnAddedToScene](keyframed_movement_component_onaddedtoscene.md) | 当组件通过挂到 simulation 实体（或已在场景中的其他实体）之下而被加入场景时调用。该阶段完成后，查询场景中的组件才是有效的。 |
| [OnBeginSimulation](keyframed_movement_component_onbeginsimulation.md) | 当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。 |
| [OnEndSimulation](keyframed_movement_component_onendsimulation.md) | 当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。 |
| [OnReceive](keyframed_movement_component_onreceive.md) | 响应场景事件。返回 true 表示消费该事件并阻止向下一个实体继续传播。 |
| [OnRemovingFromScene](keyframed_movement_component_onremovingfromscene.md) | 当组件即将被移出场景时调用。父实体被移出场景时其上的组件随之移除。只有已调用过 OnAddedToScene 的组件才会收到 OnRemovingFromScene。 |
| [OnSimulate](keyframed_movement_component_onsimulate.md) | 当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。 |
| [Pause](keyframed_movement_component_pause.md) | 暂停运动；之后调用 Play() 会从暂停处继续。 |
| [Play](keyframed_movement_component_play.md) | 开始或恢复播放。 |
| [RemoveFromEntity](keyframed_movement_component_removefromentity.md) | 把组件从实体上移除。被移除的组件会离开场景，且之后只能加回同一个实体。流程经过 OnEndSimulation → OnRemovingFromScene。 |
| [SendDown](keyframed_movement_component_senddown.md) | 向此组件发送场景事件，触发 OnReceive。有参与者消费该事件则返回 true。 |
| [SetKeyframes](keyframed_movement_component_setkeyframes.md) | 停止进行中的动画，设置动画路径并以其当前变换为基准重定基；调用 Play() 前不会开始播放。 |
| [Stop](keyframed_movement_component_stop.md) | 停止并把变换重置到初始状态；之后调用 Play() 将从头开始动画。 |
| [Stop](keyframed_movement_component_stop.md) | 停止并把变换重置到初始状态；之后调用 Play() 将从头开始动画。 |
