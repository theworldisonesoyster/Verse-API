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

# team 🟩【A级·常用】

> team represents a team in the experience.
> team 表示对局中的一支队伍。

## 这是什么

`team` 是"队伍"的抽象标识。它自身没有成员，作用是作为身份被其他 API 接收/返回：拿某玩家所在队伍、比较两个玩家是否同队、按队伍分组处理。队伍的实际划分与设置通常由对局设置/设备完成，Verse 里只做查询与判断。

## 签名

```verse
team<public><epic_internal> := class<epic_internal>:
    # 无自有成员
```

## 最小示例

```verse
using { /Verse.org/Simulation }
using { /Fortnite.com/Game }   # GetPlayspace / GetTeams 所在

# 两名玩家是否同队
SameTeam(A:agent, B:agent):logic =
    TA := A.GetTeam[]   # 可失败：取不到则失败
    TB := B.GetTeam[]
    TA = TB             # 队伍实例相等比较
```

## 常用成员

| 名称 | 形式 | 说明 | 级别 |
|---|---|---|---|
| `Agent.GetTeam[]` | 可失败扩展 | 取参与者所在队伍 | 🟩 A |
| `GetPlayspace().GetTeams()` | 常配 | 对局全部队伍 | 🟩 A |

## 何时用 / 何时不用

- 用：分队玩法、队伍计分、判断敌我。
- 不用：想"创建/解散队伍"——队伍结构由对局设置决定，Verse 只读。

## 常见坑

- 取队伍一律是可失败操作（`GetTeam[]`），要写在失败上下文里。
- 队伍数量因对局设置而异，别假设只有两队。

## 相关页面

- [agent](agent.md) / [player](player.md) —— 队伍的成员
- [session](session.md) —— 按队伍存全局数据
