---
name: player
slug: versedotorg/simulation/player
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/player
kind: class
module: /Verse.org/Simulation
grade: S
depth: full
status: done
---

# player class 🟦【S级·核心】

（本页官网无导语描述；player 表示对局中的真人玩家，是 agent 的子类。）

`using { /Verse.org/Simulation }`

## Inheritance Hierarchy

This class is derived from the following hierarchy, starting with `entity`:（本类派生自以下层级，起点为 entity：）

| Name | Description |
|---|---|
| entity | 实体是 SceneGraph 的基础对象。体验中的对象由一个或多个实体构成。实体是有层级的：可用 `GetParent` 查询父实体、用 `AddEntities` 添加子实体。行为通过组件（component）添加：用 `AddComponents` 添加新组件。实体的结构和内容是动态的，可在体验运行中的任意时刻改变。 **派生自 entity** 在 SceneGraph 体系中，派生自 entity 的类也被称为预制体（prefab）。当你想在游戏中多次生成/复用一组实体和组件时，预制体非常有用。预制体主要在编辑器中创作，其 Verse 类会在构建时生成到项目的 Assets.digest.verse 文件里。虽然你可以为载具、角色等常见对象类型创建基础预制体，但官方强烈建议**不要直接在 entity 类里写代码**，而是把逻辑放在组件里。把逻辑和数据放进组件，你在体验制作全程中重构预制体时，就不必大改类结构。 |
| agent | （agent 的官方页面无描述。） |

## Members

This class has functions, but no data members.（此类只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| AddComponents | 把给定的组件添加到实体。若某组件不允许加到该实体，则跳过。注意：在 AddedToScene 或 BeginSimulation 阶段调用时，会确保被加组件已达到对应阶段。组件按以下规则添加：所有组件加入实体的子列表；若该实体在场景中，所有组件的 OnAddedToScene 被调用；若该实体正在模拟，所有组件的 OnBeginSimulation 被调用。 |
| AddEntities | 把给定的实体添加为子实体。若子实体已有父实体，会先从原父实体移除再加入新父。加入的子实体会沿各自的生命周期方法推进，直到与新父实体的状态一致。 |
| AddTag | 向此实体添加一个标签实例，返回与该实例唯一关联的 tag_key。 |
| ContainsAllTags | 若 tag_types 中有任一类型在容器中找不到则失败，否则成功。注意 tag_types 为空时此调用成功。 |
| ContainsAnyTag | 若 tag_types 中至少一个类型在容器中找到则成功，否则失败。注意 tag_types 为空时此调用失败。 |
| ContainsTag | 若容器中找到至少一个 tag_type 类型的标签则成功，否则失败。 |
| GetComponent | 若 component_type 类型的子组件存在且可从调用方上下文访问，则成功并返回该组件。注意：在 AddedToScene 或 BeginSimulation 阶段调用时，会确保返回的组件已达到对应阶段。若不存在或不可访问则失败。 |
| GetComponents | 返回此实体下属、可从调用方上下文访问的子组件。 |
| GetEntities | 返回此实体下属、可从调用方上下文访问的子实体。只取直接子实体；要跨多层查询请改用 Find* 系列查询方法。 |
| GetParent | 返回此实体的父实体。父实体掌控其子实体与组件的生命周期——实体从场景移除时，其所有子实体和组件也会一并移除。当前没有父实体时此方法失败。 |
| IsActive | 当此 player 可以用作模块级 `var` `weak_map` 的键时成功。这对应相应玩家已加入游戏且尚未离开。当此方法失败时，把该 player 用作模块级 var weak_map 的键会导致运行时错误。 |
| RemoveAllTags | 移除 tag_type 类型的全部标签实例；至少移除一个则成功，否则失败。 |
| RemoveAllTagsExcept | 移除不属于 tag_type 类型的全部标签实例；至少移除一个则成功，否则失败。 |
| RemoveAllTagsExcept | 移除不属于 tag_types 中任何类型的全部标签实例；至少移除一个则成功，否则失败。 |
| RemoveFromParent | 把此实体从父实体移除，用于将实体移出场景。该实体及其子级上的组件会依次走 OnEndSimulation → OnRemovingFromScene。之后可用 NewParent.AddEntities 再加回。 |
| RemoveTag | 移除与 tag_key 关联的标签实例；移除成功则成功，否则失败。 |
| SendDown | 向此实体发送场景事件并沿层级向下传播：先在本实体的每个组件上调用 SendDown/OnReceive，再对每个子实体调用 SendDown。任一环节消费该事件即停止传播。有参与者消费则返回 true。 |
| SendUp | 向此实体发送场景事件并沿层级向上传播：先在本实体的每个组件上调用 SendDown/OnReceive，再对父实体调用 SendUp。任一环节消费该事件即停止传播。有参与者消费则返回 true。 |

## 示例

```verse
using { /Verse.org/Simulation }

# 对局开始：遍历全部玩家打招呼；从 agent 安全转 player
OnBegin<override>()<suspends>:void =
    for (P : GetPlayspace().GetPlayers()):
        Print("欢迎！")
        Sleep(0.2)

HandleAgent(A:agent):void =
    if (P := player[A]):
        Print("真人玩家")
```

## 补充说明

- `player[Agent]` 是可失败转换，必须写在失败上下文里；AI 参与者转换会失败。
- **IsActive[] 是 player 相对 agent 唯一新增的函数**：把 player 存进模块级 weak_map 前先判断它，可避免"玩家已退出仍作键"的运行时错误。
- 玩家专属能力分布在其他模块：角色身体 fort_character（Characters）、玩家 UI player_ui（Temporary/UI）等。
- 相关页面：[agent class](agent.md)、[session class](session.md)、[fort_character interface](../../../03_Fortnite.com/130_Characters/fort_character.md)。
