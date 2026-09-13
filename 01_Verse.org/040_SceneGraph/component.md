---
name: component
slug: versedotorg/scenegraph/component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component
kind: class
module: /Verse.org/SceneGraph
grade: S
depth: full
status: done
---

# component class <S>

> Base class for authoring logic and data in the SceneGraph. Using components you can author re-usable building blocks of logic and data which can then be added to entities in the scene.
> 在 SceneGraph 中编写逻辑与数据的基类。通过组件，你可以创作可复用的逻辑与数据构件，然后把它们添加到场景中的实体上。
>
> Components are a very low level building block which can be used in many ways. For example:
> 组件是非常底层的构件，用法很多，例如：
>
> - Exposing engine level concepts like mesh or sound
>   暴露网格、声音等引擎级概念
> - Adding gameplay capabilities like damage or interaction
>   添加伤害、交互等玩法能力
> - Storing an inventory for a character in the game
>   为游戏中的角色存储物品栏
>
> As components are generic there is no specific way that they must be used. It is up to the needs of your experience if you use one big game component or if you break up logic into many small components.
> 组件是通用的，没有强制的使用方式。用一个大的"游戏组件"还是把逻辑拆成许多小组件，由你的体验需求决定。

Classes deriving from component must also specify `<final_super>` to be added to entities. This ensures the class will always derive directly from component. Further subclassing of the initial derived component is allowed and does not require specifying `<final_super>` on the derived classes.
派生自 component 的类还必须指定 `<final_super>` 才能被添加到实体。这保证该类永远直接派生自 component。在最初派生的组件之上继续派生子类是允许的，且不需要再标 `<final_super>`。

Only one instance of a component from each subclass group can be added to an entity at a time. For example, given this group of components, only one light_component can exist on a single entity. To create multiple lights you should use multiple entities.
`light_component := class(component){} capsule_light_component := class(light_component){} directional_light_component := class(light_component){} spot_light_component := class(light_component){} sphere_light_component := class(light_component){} rect_light_component := class(light_component){}`
同一子类组中的组件，同一时刻在一个实体上只能有一个实例。例如上面这组组件里，一个实体上只能存在一个 light_component；要创建多盏灯应该使用多个实体。

**Component Lifetime** — Components move through a series of lifetime functions as they are added to entities, added to the scene, and begin running in the simulation. Components should override these methods to perform setup and run their simulation. As a component shuts down it will then move through shutdown version of these functions, giving users the opportunity to clean up any retained state on the component before it is disposed. Lifetime Methods: OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene
**组件生命周期** —— 组件被添加到实体、加入场景、开始在模拟中运行时，会经过一系列生命周期函数。组件应重写这些方法来完成初始化并运行自己的模拟。组件关闭时会按相反的关停版本走一遍，让你有机会在组件被销毁前清理保留状态。生命周期方法：OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene。

`using { /Verse.org/SceneGraph }`

## Members

This class has both data members and functions.（此类兼有数据成员和函数。）

### Data

| Data Member Name | Type | Description |
|---|---|---|
| [Entity](component_entity.md) | entity | 此组件的父实体。组件构造时必须提供父实体指针；组件不能在父实体之间移动。 |
| [TickEvents](component_tickevents.md) | ?tick_events | 设置 TickEvents.PrePhysics 与 TickEvents.PostPhysics 回调，可在对象物理更新前/后接收逐帧更新。 |

### Functions

| Function Name | Description |
|---|---|
| [OnAddedToScene](component_onaddedtoscene.md) | 当组件通过挂到 simulation 实体（或已在场景中的其他实体）之下而被加入场景时调用。该阶段完成后，查询场景中的组件才是有效的。 |
| [OnBeginSimulation](component_onbeginsimulation.md) | 当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。 |
| [OnSimulate](component_onsimulate.md) | 当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。 |
| [OnEndSimulation](component_onendsimulation.md) | 当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。 |
| [OnRemovingFromScene](component_onremovingfromscene.md) | 当组件即将被移出场景时调用。父实体被移出场景时其上的组件随之移除。只有已调用过 OnAddedToScene 的组件才会收到 OnRemovingFromScene。 |
| [RemoveFromEntity](component_removefromentity.md) | 把组件从实体上移除。被移除的组件会离开场景，且之后只能加回**同一个**实体。流程经过 OnEndSimulation → OnRemovingFromScene。 |
| [IsInScene](component_isinscene.md) | 若组件当前在场景中则成功。OnAddedToScene 调用后成功；OnRemovingFromScene 调用后失败。 |
| [IsSimulating](component_issimulating.md) | 若组件当前正在模拟则成功。OnBeginSimulation 调用后成功；OnEndSimulation 调用后失败。 |
| [SendDown](component_senddown.md) | 向此组件发送场景事件，触发 OnReceive。有参与者消费该事件则返回 true。 |
| [OnReceive](component_onreceive.md) | 响应场景事件。返回 true 表示消费该事件并阻止向下一个实体继续传播。 |

## 示例

```verse
using { /Verse.org/SceneGraph }
using { /Verse.org/Simulation }

# 自定义组件：每秒数一拍（节拍器示例）
beat_component<final_super> := class(component):
    var Beat:int = 0

    OnSimulate<override>()<suspends>:void =
        loop:
            Sleep(1.0)
            set Beat += 1
            Print("♪ {Beat}")
```

## 补充说明

- 派生组件必须加 `<final_super>` 才能挂到实体上（官方导语明示）——这是新组件类最常见的编译错误来源。
- 生命周期固定顺序：OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene；帧回调走 TickEvents。
- 相关页面：[entity class](entity.md)、[transform_component class](transform_component.md)、[tick_events class](tick_events.md)。
