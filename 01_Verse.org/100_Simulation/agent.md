---
name: agent
slug: versedotorg/simulation/agent
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/agent
kind: class
module: /Verse.org/Simulation
grade: S
depth: full
status: done
---

# agent 🟦【S级·核心】

> Agent is the abstract representation of a participant in an experience: a player or an AI agent.
> agent 是"对局参与者"的抽象表示——可以是真人玩家，也可以是 AI 单位。

## 这是什么

设备事件回传的"是谁触发了按钮"、排行榜里的"是谁"、物品栏的"是谁的"——这些"谁"的类型都是 `agent`。它是**抽象基类**：真人玩家是它的子类 [player](player.md)，AI 单位同样继承它。你的函数通常**接收 agent**（宽进），内部再判断/转换成 player 或做 agent 级操作（严用）。

在当前版本的 SceneGraph 体系里，agent 继承自 [entity](../040_SceneGraph/entity.md)，因此也拥有实体层的组件管理函数（AddComponents 等），但多数玩法代码只用"它代表一个参与者"这一身份。

## 签名

```verse
agent<public><epic_internal> := class<epic_internal>(entity):
    # 官方未公开任何自有成员；作为类型标识使用
```

## 最小示例

```verse
using { /Verse.org/Simulation }

# 设备事件拿到 agent 后，识别出真人玩家
OnAgentJoined(Agent:agent):void =
    if (P := player[Agent]):
        Print("玩家 {P.GetPlayerUI? } 加入")   # player 才有玩家级操作
    else:
        Print("AI 参与者加入")
```

## 常用成员

agent 自身几乎无成员，价值在"作为参与者的通行证"被各类 API 接收。常用配套函数（模块级）：

| 函数 | 形式 | 说明 | 级别 |
|---|---|---|---|
| `player[Agent]` | 可失败转换 | 把 agent 尝试转为 player，失败则走失败分支 | 🟦 S |
| `GetPlayspace().GetPlayers()` | 常配 | 取全部玩家（Fortnite.com/Game） | 🟩 A |
| 继承自 entity | `AddEntities` / `AddComponents` / `GetParent` | SceneGraph 实体操作 | 🟨 B |

## 何时用 / 何时不用

- 用：任何"对每个参与者做事"的场合——发奖励、记分、事件回调参数类型。
- 不用：需要真人专属信息（角色血量、UI）时直接转成 player；不要把 agent 当成具体角色对象用。

## 常见坑

- `agent` ≠ 角色（character）：agent 是"参与者"，角色是 player 在世界里的身体（如 fort_character）。两者要分清。
- 从设备事件拿到的 agent 未必是真人，转 player 必须走失败分支（`if (P := player[Agent])`）。

## 相关页面

- [player](player.md) —— 唯一的常用子类
- [entity](../040_SceneGraph/entity.md) —— SceneGraph 基类
- [team](team.md) —— 参与者的分组
