---
name: ability_effect
slug: unrealenginedotcom/abilities/ability_effect
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/abilities/ability_effect
kind: class
module: /UnrealEngine.com/abilities
grade: B
depth: brief
status: done
---

# ability_effect class <B>

> Prefab to provide a central location for handling desired ability and gameplay logic.
> 预制体：为技能与玩法逻辑提供集中处理位置。

`using { /UnrealEngine.com/Abilities }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| entity | 实体是 SceneGraph 的基础对象：体验中的对象由一个或多个实体构成；实体有层级，可用 GetParent 查询父实体、AddEntities 添加子实体；行为通过组件添加（AddComponents）；结构与内容动态可变。派生自 entity 的类即预制体（prefab），主要由编辑器生成；官方强烈建议逻辑写在组件而非 entity 类里，便于重构。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| AbilityComponent | ability_effect_component |  |

### Functions
| Function Name | Description |
| AddComponents | 把给定的组件添加到实体。若某组件不允许加到该实体则跳过。注意：在 AddedToScene 或 BeginSimulation 阶段调用时，会确保被加组件已达到对应阶段。添加规则：所有组件加入实体子列表；实体在场景中时各组件的 OnAddedToScene 被调用；实体正在模拟时各组件的 OnBeginSimulation 被调用。 |
| AddEntities | 把给定的实体添加为子实体。若子实体已有父实体，会先从原父实体移除再加入新父。加入的子实体会沿各自的生命周期方法推进，直到与新父实体的状态一致。 |
| AddTag | 向此实体添加一个标签实例，返回与该实例唯一关联的 tag_key。 |
| ContainsAllTags | 若 tag_types 中有任一类型在容器中找不到则失败，否则成功。注意 tag_types 为空时此调用成功。 |
| ContainsAnyTag | 若 tag_types 中至少一个类型在容器中找到则成功，否则失败。注意 tag_types 为空时此调用失败。 |
| ContainsTag | 若容器中找到至少一个 tag_type 类型的标签则成功，否则失败。 |
| GetComponent | 若 component_type 类型的子组件存在且可访问，则成功并返回它。注意：在 AddedToScene 或 BeginSimulation 阶段调用时，会确保返回的组件已达到对应阶段。不存在或不可访问则失败。 |
| GetComponents | 返回此实体下属、可从调用方上下文访问的子组件。 |
| GetEntities | 返回此实体下属、可从调用方上下文访问的子实体。只取直接子实体；跨多层查询请用 Find* 系列。 |
| GetParent | 返回此实体的父实体。父实体掌控其子实体与组件的生命周期——实体从场景移除时其所有子实体和组件也会一并移除。当前没有父实体时此方法失败。 |
| RemoveAllTags | 移除 tag_type 类型的全部标签实例；至少移除一个则成功，否则失败。 |
| RemoveAllTagsExcept | 移除不属于 tag_type 类型的全部标签实例；至少移除一个则成功，否则失败。 |
| RemoveAllTagsExcept | 移除不属于 tag_types 中任何类型的全部标签实例；至少移除一个则成功，否则失败。 |
| RemoveFromParent | 把此实体从父实体移除，用于将实体移出场景。该实体及其子级上的组件会依次走 OnEndSimulation → OnRemovingFromScene。之后可用 NewParent.AddEntities 再加回。 |
| RemoveTag | 移除与 tag_key 关联的标签实例；移除成功则成功，否则失败。 |
| SendDown | 向此实体发送场景事件并沿层级向下传播：先在本实体的每个组件上调用 SendDown/OnReceive，再对每个子实体调用 SendDown。任一环节消费该事件即停止传播。有参与者消费则返回 true。 |
| SendUp | 向此实体发送场景事件并沿层级向上传播：先在本实体的每个组件上调用 SendDown/OnReceive，再对父实体调用 SendUp。任一环节消费该事件即停止传播。有参与者消费则返回 true。 |
