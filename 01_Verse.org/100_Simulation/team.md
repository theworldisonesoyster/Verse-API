---
name: team
slug: versedotorg/simulation/team
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/team
kind: class
module: /Verse.org/Simulation
grade: A
depth: full
status: done
---

# team class 🟩【A级·常用】

> team represents a team in the experience.
> team 表示对局中的一支队伍。

`using { /Verse.org/Simulation }`

## Members

This class has no members.（此类没有成员。）

## Attributes, Specifiers, and Effects

`team<public><epic_internal> := class<epic_internal>` —— 标签：public / epic_internal，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Simulation }
using { /Fortnite.com/Game }   # GetPlayspace / GetTeams 所在

# 两名参与者是否同队（取队伍是可失败操作）
SameTeam(A:agent, B:agent):logic =
    TA := A.GetTeam[]
    TB := B.GetTeam[]
    TA = TB
```

## 补充说明

- `team` 自身零成员，价值在于作为"队伍身份"被其他 API 接收/返回（如 `GetTeam[]`、`GetPlayspace().GetTeams()`）。
- 队伍的划分由对局设置决定，Verse 侧只读：没有"创建/解散队伍"的 API。
- 相关页面：[agent class](agent.md)、[player class](player.md)。
