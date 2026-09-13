---
name: orthographic_camera_component
slug: versedotorg/scenegraph/orthographic_camera_component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/orthographic_camera_component
kind: class
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# orthographic_camera_component class <B>

> Simple orthographic camera.
> 简单的正交相机。

`using { /Verse.org/SceneGraph }`

## Inheritance Hierarchy

此类派生自以下层级，起点为 ：
| Name | Description |
| component | 在 SceneGraph 中编写逻辑与数据的基类。通过组件可创作可复用的逻辑与数据构件并添加到场景中的实体上。组件是非常底层的构件：可暴露网格/声音等引擎概念、添加伤害/交互等玩法能力、存储物品栏；用一个大组件还是拆成多个小组件由体验需求决定。派生自 component 的类必须指定 <final_super> 才能添加到实体；同一子类组在同一实体上只能有一个实例。生命周期：OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene。 |
| camera_component | 表示相机的物理机身、镜头及其他电影摄影属性（传感器尺寸、宽高比锁定、焦距、对焦距离、位置等）。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [Entity](orthographic_camera_component_entity.md) | entity | 此组件的父实体。组件构造时必须提供父实体指针；组件不能在父实体之间移动。 |
| [FarClippingPlaneDistance](orthographic_camera_component_farclippingplanedistance.md) | ?float | 可选覆盖远裁剪面距离；值为 Inf 时使用默认设置。 |
| [NearClippingPlaneDistance](orthographic_camera_component_nearclippingplanedistance.md) | ?float | 可选覆盖近裁剪面距离；值 ≤ 0.0 时使用默认设置。 |
| [OrthographicProjectionWidth](orthographic_camera_component_orthographicprojectionwidth.md) | ?float | 正交模式下相机投影的宽度（厘米）。 |
| [TickEvents](orthographic_camera_component_tickevents.md) | ?tick_events | 设置 TickEvents.PrePhysics 与 TickEvents.PostPhysics 回调，在对象物理更新前/后接收逐帧更新。 |

### Functions
| Function Name | Description |
| [GetEnterTransition](orthographic_camera_component_getentertransition.md) | 获取进入此相机模式、过渡到指定相机模式时所用的过渡。 |
| [GetExitTransition](orthographic_camera_component_getexittransition.md) | 获取退出此相机模式、过渡到目标相机模式时所用的过渡。 |
| [IsInScene](orthographic_camera_component_isinscene.md) | 若组件当前在场景中则成功。OnAddedToScene 调用后成功；OnRemovingFromScene 调用后失败。 |
| [IsSimulating](orthographic_camera_component_issimulating.md) | 若组件当前正在模拟则成功。OnBeginSimulation 调用后成功；OnEndSimulation 调用后失败。 |
| [OnAddedToScene](orthographic_camera_component_onaddedtoscene.md) | 当组件通过挂到 simulation 实体（或已在场景中的其他实体）之下而被加入场景时调用。该阶段完成后，查询场景中的组件才是有效的。 |
| [OnBeginSimulation](orthographic_camera_component_onbeginsimulation.md) | 当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。 |
| [OnEndSimulation](orthographic_camera_component_onendsimulation.md) | 当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。 |
| [OnReceive](orthographic_camera_component_onreceive.md) | 响应场景事件。返回 true 表示消费该事件并阻止向下一个实体继续传播。 |
| [OnRemovingFromScene](orthographic_camera_component_onremovingfromscene.md) | 当组件即将被移出场景时调用。父实体被移出场景时其上的组件随之移除。只有已调用过 OnAddedToScene 的组件才会收到 OnRemovingFromScene。 |
| [OnSimulate](orthographic_camera_component_onsimulate.md) | 当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。 |
| [RemoveFromEntity](orthographic_camera_component_removefromentity.md) | 把组件从实体上移除。被移除的组件会离开场景，且之后只能加回同一个实体。流程经过 OnEndSimulation → OnRemovingFromScene。 |
| [SendDown](orthographic_camera_component_senddown.md) | 向此组件发送场景事件，触发 OnReceive。有参与者消费该事件则返回 true。 |
