---
name: basic_interactable_component
slug: versedotorg/scenegraph/basic_interactable_component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/basic_interactable_component
kind: class
module: /Verse.org/scenegraph
grade: A
depth: full
status: done
---

# basic_interactable_component class <A>

> An interactable component with a composable feature set.
> 具有可组合特性集的交互组件。

`using { /Verse.org/SceneGraph }`

## Inheritance Hierarchy

此类派生自以下层级，起点为 ：
| Name | Description |
| component | 在 SceneGraph 中编写逻辑与数据的基类。通过组件可创作可复用的逻辑与数据构件并添加到场景中的实体上。组件是非常底层的构件：可暴露网格/声音等引擎概念、添加伤害/交互等玩法能力、存储物品栏；用一个大组件还是拆成多个小组件由体验需求决定。派生自 component 的类必须指定 <final_super> 才能添加到实体；同一子类组在同一实体上只能有一个实例。生命周期：OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene。 |
| interactable_component | 用于处理通用交互。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [CanceledEvent](basic_interactable_component_canceledevent.md) | unknown | 交互在成功完成前被中断时触发；载荷为此前交互的代理。interactable_component 本身不可取消，此事件供子类在合适时机触发。 |
| [CanInteractMessage](basic_interactable_component_caninteractmessage.md) | ?message | CanInteract 成功时显示的消息。 |
| [CannotInteractMessage](basic_interactable_component_cannotinteractmessage.md) | ?message | CanInteract 失败时显示的消息。 |
| [Cooldown](basic_interactable_component_cooldown.md) | ?interactable_cooldown | 冷却在成功交互后开始计时；作用于该组件上的所有交互尝试（全局冷却）。 |
| [CooldownPerAgent](basic_interactable_component_cooldownperagent.md) | ?interactable_cooldown_per_agent | 冷却在成功交互后开始计时；仅作用于成功者的后续交互尝试（按代理冷却）。 |
| [Entity](basic_interactable_component_entity.md) | entity | 此组件的父实体。组件构造时必须提供父实体指针；组件不能在父实体之间移动。 |
| [InteractableDuration](basic_interactable_component_interactableduration.md) | ?interactable_duration | 带时长的交互要等时长走完才算成功；期间可被取消，不保证成功。 |
| [InteractingAgents](basic_interactable_component_interactingagents.md) | ?[]agent | 当前正在与此可交互物交互的代理。 |
| [StartedEvent](basic_interactable_component_startedevent.md) | unknown | 成功交互开始时触发；载荷为交互代理。InteractDuration ≤ 0 时本事件与 InteractSucceededEvent 相同。 |
| [SucceededEvent](basic_interactable_component_succeededevent.md) | unknown | 交互成功完成时触发；载荷为此前交互的代理。InteractDuration ≤ 0 时本事件与 InteractStartedEvent 相同。 |
| [SuccessLimit](basic_interactable_component_successlimit.md) | ?interactable_success_limit | 成功次数上限：达到指定成功次数后阻止新的交互。 |
| [TickEvents](basic_interactable_component_tickevents.md) | ?tick_events | 设置 TickEvents.PrePhysics 与 TickEvents.PostPhysics 回调，在对象物理更新前/后接收逐帧更新。 |

### Functions
| Function Name | Description |
| [Cancel](basic_interactable_component_cancel.md) | 尝试取消一次交互；给定代理当前未在交互则失败。 |
| [CanInteract](basic_interactable_component_caninteract.md) | 返回指定代理当前能否交互。 |
| [Disable](basic_interactable_component_disable.md) | 禁用与该组件的交互。禁用后不显示交互提示。 |
| [Enable](basic_interactable_component_enable.md) | 启用与该组件的交互。 |
| [GetRemainingCooldownDurationAffectingAgent](basic_interactable_component_getremainingcooldowndurationaffectingagent.md) | 获取给定代理的剩余冷却：返回共享冷却与按代理冷却中较大者的剩余秒数；同一事务内多次调用返回相同值。 |
| [InteractMessage](basic_interactable_component_interactmessage.md) |  |
| [InteractMessage](basic_interactable_component_interactmessage.md) | 返回适合展示给玩家、说明当前交互状态的消息。 |
| [IsEnabled](basic_interactable_component_isenabled.md) | 组件处于启用状态则成功，禁用则失败。 |
| [IsInScene](basic_interactable_component_isinscene.md) | 若组件当前在场景中则成功。OnAddedToScene 调用后成功；OnRemovingFromScene 调用后失败。 |
| [IsSimulating](basic_interactable_component_issimulating.md) | 若组件当前正在模拟则成功。OnBeginSimulation 调用后成功；OnEndSimulation 调用后失败。 |
| [OnAddedToScene](basic_interactable_component_onaddedtoscene.md) | 当组件通过挂到 simulation 实体（或已在场景中的其他实体）之下而被加入场景时调用。该阶段完成后，查询场景中的组件才是有效的。 |
| [OnBeginSimulation](basic_interactable_component_onbeginsimulation.md) | 当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。 |
| [OnEndSimulation](basic_interactable_component_onendsimulation.md) | 当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。 |
| [OnReceive](basic_interactable_component_onreceive.md) | 响应场景事件。返回 true 表示消费该事件并阻止向下一个实体继续传播。 |
| [OnRemovingFromScene](basic_interactable_component_onremovingfromscene.md) | 当组件即将被移出场景时调用。父实体被移出场景时其上的组件随之移除。只有已调用过 OnAddedToScene 的组件才会收到 OnRemovingFromScene。 |
| [OnSimulate](basic_interactable_component_onsimulate.md) | 当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。 |
| [OnStarted](basic_interactable_component_onstarted.md) | 当 CanInteract 通过后由 Start 调用以开始交互；重写它可实现自定义交互行为。 |
| [RemoveFromEntity](basic_interactable_component_removefromentity.md) | 把组件从实体上移除。被移除的组件会离开场景，且之后只能加回同一个实体。流程经过 OnEndSimulation → OnRemovingFromScene。 |
| [SendDown](basic_interactable_component_senddown.md) | 向此组件发送场景事件，触发 OnReceive。有参与者消费该事件则返回 true。 |
| [SignalCancelEvent](basic_interactable_component_signalcancelevent.md) | 触发 CanceledEvent 事件。 |
| [SignalStartEvent](basic_interactable_component_signalstartevent.md) | 触发 StartedEvent 事件。 |
| [SignalSucceedEvent](basic_interactable_component_signalsucceedevent.md) | 触发 SucceededEvent 事件。 |
| [Start](basic_interactable_component_start.md) | 尝试开始交互；代理未通过 CanInteract 则失败。 |
| [Succeed](basic_interactable_component_succeed.md) | 尝试使交互成功。开始交互后经过 InteractDuration 也会自动成功；给定代理当前未在交互则失败。 |
