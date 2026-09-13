---
name: entity
slug: versedotorg/scenegraph/entity
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/entity
kind: class
module: /Verse.org/SceneGraph
grade: S
depth: full
status: done
---

# entity class <S>

> Entities are the base object in the SceneGraph.
> 实体是 SceneGraph 的基础对象。
>
> - Objects in experiences are constructed of one or more entities.
>   体验中的对象由一个或多个实体构成。
> - Entities are hierarchical. You can query your parent using GetParent and add child entities using AddEntities.
>   实体是有层级的：可用 GetParent 查询父实体、用 AddEntities 添加子实体。
> - Behavior is added to entities through components. You can add new components using AddComponents.
>   行为通过组件（component）添加：用 AddComponents 添加新组件。
> - The structure and content of entities is dynamic and can be changed at any time through your experience.
>   实体的结构和内容是动态的，可在体验运行中的任意时刻改变。

**Deriving from entity** — In the SceneGraph system a class that derives from entity is also known as a prefab. Prefabs are useful when you want to spawn/re-use a collection of entities and components many times within your game. Primarily prefabs are authored through the editor, with their Verse classes generated as part of the build into the projects Assets.digest.verse file.
**派生自 entity** —— 在 SceneGraph 体系中，派生自 entity 的类也被称为预制体（prefab）。当你想在游戏中多次生成/复用一组实体和组件时，预制体非常有用。预制体主要在编辑器中创作，其 Verse 类会在构建时生成到项目的 Assets.digest.verse 文件里。

While you can create base prefabs for common game object types like a vehicle or character, we highly recommended that you do not add code directly to the entity class, and instead keep logic in components. Keeping logic and data in components allows you to restructure your prefabs throughout production of your experience, without needing to massively refactor your class structure.
虽然你可以为载具、角色等常见对象类型创建基础预制体，但官方强烈建议**不要直接在 entity 类里写代码**，而是把逻辑放在组件里。把逻辑和数据放进组件，你在体验制作全程中重构预制体时，就不必大改类结构。

`using { /Verse.org/SceneGraph }`

## Exposed Interfaces

This class exposes the following interfaces:（此类暴露以下接口：）

| Name | Description |
|---|---|
| has_tags | 表示"可变标签集合"的接口。 |

## Members

This class has functions, but no data members.（此类只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| GetParent | 返回此实体的父实体。父实体掌控其子实体与组件的生命周期——实体从场景移除时，其所有子实体和组件也会一并移除。当前没有父实体时此方法失败。 |
| RemoveFromParent | 把此实体从父实体移除，用于将实体移出场景。该实体及其子级上的组件会依次走 OnEndSimulation → OnRemovingFromScene。之后可用 NewParent.AddEntities 再加回。 |
| AddEntities | 把给定的实体添加为子实体。若子实体已有父实体，会先从原父实体移除再加入新父。加入的子实体会沿各自的生命周期方法推进，直到与新父实体的状态一致。 |
| GetEntities | 返回此实体下属、可从调用方上下文访问的子实体。只取直接子实体；要跨多层查询请改用 Find* 系列查询方法。 |
| GetComponent | 若 component_type 类型的子组件存在且可从调用方上下文访问，则成功并返回该组件。注意：在 AddedToScene 或 BeginSimulation 阶段调用时，会确保返回的组件已达到对应阶段。若不存在或不可访问则失败。 |
| GetComponents | 返回此实体下属、可从调用方上下文访问的子组件。 |
| AddComponents | 把给定的组件添加到实体。若某组件不允许加到该实体，则跳过。注意：在 AddedToScene 或 BeginSimulation 阶段调用时，会确保被加组件已达到对应阶段。组件按以下规则添加：所有组件加入实体的子列表；若该实体在场景中，所有组件的 OnAddedToScene 被调用；若该实体正在模拟，所有组件的 OnBeginSimulation 被调用。 |
| SendUp | 向此实体发送场景事件并沿层级向上传播：先在本实体的每个组件上调用 SendDown/OnReceive，再对父实体调用 SendUp。任一环节消费该事件即停止传播。有参与者消费则返回 true。 |
| SendDown | 向此实体发送场景事件并沿层级向下传播：先在本实体的每个组件上调用 SendDown/OnReceive，再对每个子实体调用 SendDown。任一环节消费该事件即停止传播。有参与者消费则返回 true。 |
| AddTag | 向此实体添加一个标签实例，返回与该实例唯一关联的 tag_key。 |
| RemoveTag | 移除与 tag_key 关联的标签实例；移除成功则成功，否则失败。 |
| RemoveAllTags | 移除 tag_type 类型的全部标签实例；至少移除一个则成功，否则失败。 |
| RemoveAllTagsExcept | 移除不属于 tag_type 类型的全部标签实例；至少移除一个则成功，否则失败。 |
| RemoveAllTagsExcept | 移除不属于 tag_types 中任何类型的全部标签实例；至少移除一个则成功，否则失败。 |
| ContainsTag | 若容器中找到至少一个 tag_type 类型的标签则成功，否则失败。 |
| ContainsAllTags | 若 tag_types 中有任一类型在容器中找不到则失败，否则成功。注意 tag_types 为空时此调用成功。 |
| ContainsAnyTag | 若 tag_types 中至少一个类型在容器中找到则成功，否则失败。注意 tag_types 为空时此调用失败。 |

## 示例

```verse
using { /Verse.org/SceneGraph }

# 运行时搭一个"灯杆"：实体 + 变换组件 + 聚光灯组件
BuildLamp(Parent:entity):void =
    Pole := entity{}
    Pole.AddComponents(array{transform_component{}, spot_light_component{}})
    Parent.AddEntities(array{Pole})
```

## 补充说明

- 官方明确：逻辑写进组件、entity 只当容器/预制体壳；组件一旦挂上不能换父，要移动就 RemoveFromParent 后重挂。
- 场景事件的向上/向下传播靠 SendUp/SendDown，组件侧在 OnReceive 里响应。
- 相关页面：[component class](component.md)、[transform_component class](transform_component.md)、[agent class](../100_Simulation/agent.md)。
