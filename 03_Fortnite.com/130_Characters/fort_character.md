---
name: fort_character
slug: fortnitedotcom/characters/fort_character
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/characters/fort_character
kind: interface
module: /Fortnite.com/Characters
grade: S
depth: full
status: done
---

# fort_character 🟦【S级·核心】

> Represents the physical character body of a player (or NPC) in the world.
> 玩家（或 NPC）在世界中的"角色身体"——移动、跳跃、淘汰、生命值都发生在它身上。

## 这是什么

[agent](../../01_Verse.org/100_Simulation/agent.md)/[player](../../01_Verse.org/100_Simulation/player.md) 是"参与者身份"，`fort_character` 才是**世界里的那具身体**。它是**接口**（不是类），由角色对象实现。获取方式是从 agent/player 可失败转换：`Agent.GetFortCharacter[]`。

它通过一组能力接口暴露功能，这决定了"哪些操作要去哪个接口找"：

| 暴露接口 | 提供什么 |
|---|---|
| `positional` | 读位置信息 |
| `healthful` | 生命状态与淘汰 |
| `healable` / `damageable` | 治疗 / 受击 |
| `shieldable` | 护盾状态 |
| `game_action_instigator` | 伤害/治疗等游戏动作的发起者信息 |

**注意**：本版本中"扣血/加血"等操作分散在上述接口（官方页各接口章节），fort_character 页面本身不提供 Damage/Heal 函数——使用前按接口查找，勿凭旧教程硬写。

## 签名

```verse
fort_character<public><native> := interface<native>(positional, healable, healthful,
                                                  damageable, shieldable,
                                                  game_action_instigator):
```

## 最小示例

```verse
using { /Fortnite.com/Characters }
using { /Verse.org/Simulation }

WatchPlayer(Agent:agent)<suspends>:void =
    if (FC := Agent.GetFortCharacter[]):
        if (FC.IsActive[]):
            Print("角色在场上")
        FC.EliminatedEvent().Await()      # 挂起等待该角色被淘汰
        Print("被淘汰了")
```

## 常用成员（官方页验证）

| 成员 | 说明 | 级别 |
|---|---|---|
| `Agent.GetFortCharacter[]` | agent → 角色（可失败） | 🟦 S |
| `IsActive[]` | 在场且未被淘汰（可失败/断言） | 🟦 S |
| `EliminatedEvent()` | 淘汰事件（listenable） | 🟦 S |
| `GetViewLocation` / `GetViewRotation` | 视线位置/朝向 | 🟩 A |
| `JumpedEvent` / `CrouchedEvent` / `SprintedEvent` | 跳/蹲/冲刺事件（带载荷） | 🟩 A |
| `IsCrouching` / `IsOnGround` / `IsInAir` / `IsDownButNotOut` | 状态断言 | 🟩 A |
| `GetAgent` | 反查 agent | 🟩 A |

## 何时用 / 何时不用

- 用：动作玩法——跟随跳跃/蹲/冲刺做节奏判定、淘汰计数、位置玩法。
- 不用：只是发道具/传送这类"对参与者"的操作，用 player/设备即可，不必绕到身体层。

## 常见坑

- 角色可能不存在（玩家未生成/已退出）：`GetFortCharacter[]` 与 `IsActive[]` 两道失败检查别省。
- 事件回调里拿到的角色引用在淘汰后失效，长流程要做存在性检查。

## 相关页面

- [player](../../01_Verse.org/100_Simulation/player.md)
- [listenable](../../01_Verse.org/010_Verse/listenable.md) —— 事件订阅模式
