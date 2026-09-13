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

# fort_character interface <S>

> Main API implemented by Fortnite characters.
> 由堡垒之夜角色实现的主 API——玩家/AI 在世界中的"角色身体"。

`using { /Fortnite.com/Characters }`

## Exposed Interfaces

This interface exposes the following interfaces:（此接口暴露以下接口：）

| Name | Description |
|---|---|
| positional | 由对象实现，允许读取位置信息。 |
| healable | 由可被治疗的堡垒之夜对象实现。 |
| healthful | 由拥有生命状态、可被淘汰的堡垒之夜对象实现。 |
| damageable | 由可被伤害的堡垒之夜对象实现。 |
| shieldable | 由拥有护盾的堡垒之夜对象实现。护盾是一种保护机制：先承受伤害，生命值保持不变。 |
| game_action_instigator | 由发起游戏动作（如伤害、治疗）的堡垒之夜对象实现，例如玩家或 agent。事件监听器常用它计算玩家伤害积分。 |
| game_action_causer | 由可作为游戏动作事件（如伤害、治疗）载体传递的堡垒之夜对象实现，例如玩家、载具或武器。监听器常用它传递"什么武器造成了伤害"等附加信息，供任务系统或玩法逻辑使用。 |

## Members

This interface has functions, but no data members.（此接口只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| GetAgent | 返回与此 fort_character 关联的 agent。与需要 agent 引用的 API 交互时使用。 |
| EliminatedEvent | 此 fort_character 被淘汰出对局时触发。 |
| GetViewRotation | 返回此 fort_character 视线/瞄准指向的旋转。 |
| GetViewLocation | 返回此 fort_character 视线/瞄准发出的位置。 |
| JumpedEvent | 此 fort_character 跳跃时触发。返回以该 fort_character 为载荷的 listenable。 |
| CrouchedEvent | 此 fort_character 改变蹲伏状态时触发。发送元组载荷：0——改变蹲伏状态的 fort_character；1——正在蹲伏为 true，否则 false。 |
| SprintedEvent | 此 fort_character 改变冲刺状态时触发。发送元组载荷：0——改变冲刺状态的 fort_character；1——正在冲刺为 true，已停止冲刺为 false。 |
| IsActive | 若此 fort_character 在世界中且未被淘汰则成功。若此判断失败，大多数 fort_character 操作都会静默失败。想处理这些失败情况就先测 IsActive，而不是放任静默失败。 |
| IsDownButNotOut | 若此 fort_character 处于"倒地未淘汰"（Down But Not Out）状态则成功。该状态下角色倒地，但在一段时间内仍可被队友扶起。 |
| IsCrouching | 若此 fort_character 正在蹲伏则成功。 |
| IsOnGround | 若此 fort_character 站在地面上则成功。 |
| IsInAir | 若此 fort_character 处于空中则成功。 |
| IsInWater | 若此 fort_character 位于水体体积内则成功。 |
| IsFalling | 若此 fort_character 处于下落移动状态则成功。 |
| IsGliding | 若此 fort_character 处于滑翔移动状态则成功。 |
| IsFlying | 若此 fort_character 处于飞行移动状态则成功。 |
| PutInStasis | 将此 fort_character 置入凝固（stasis）状态，按 Args 阻止特定类型的移动。 |
| ReleaseFromStasis | 将此 fort_character 从凝固状态释放。 |
| Show | 将此 fort_character 的可见性设为可见。 |
| Hide | 将此 fort_character 的可见性设为不可见。 |
| SetVulnerability | 控制此 fort_character 是否可被伤害。 |
| IsVulnerable | 若此 fort_character 可被伤害则成功；不可被伤害则失败。 |
| TeleportTo | 将此 fort_character 传送到给定 Position，并应用 Rotation 的 yaw 与 pitch。若指定位置在有效对局空间之外或角色无法容纳等情形，则失败。 |
| GetEntity | 返回与此 fort_character 关联的 entity。与需要 entity 引用的 API 交互时使用。 |
| GetLinearVelocity | 返回 fort_character 的线速度（米/秒）。 |
| SetLinearVelocity | 设置 fort_character 的线速度（米/秒）。物理被禁用时无效果。 |
| ApplyLinearImpulse | 对 fort_character 施加线冲量（单位：牛顿·秒）。物理被禁用时无效果。 |
| GetMass | 返回 fort_character 的质量（千克）。 |
| ApplyForce | 对 fort_character 施加力（单位：牛顿）。物理被禁用时无效果。 |

## 示例

```verse
using { /Fortnite.com/Characters }
using { /Verse.org/Simulation }

# 等待某个角色被淘汰；动作前先做 IsActive 检查
Watch(Agent:agent)<suspends>:void =
    if (FC := Agent.GetFortCharacter[]):
        if (FC.IsActive[]):
            Print("在场上")
        FC.EliminatedEvent().Await()
        Print("被淘汰了")
```

## 补充说明

- 本页**没有** Damage/Heal 函数——伤害/治疗/生命/护盾能力在 Exposed Interfaces 列出的 damageable / healable / healthful / shieldable 接口上（见官网对应接口页）。
- 获取方式：`Agent.GetFortCharacter[]`（可失败）；动作前先 `IsActive[]`，否则失败是静默的（官方原话提醒）。
- 跳/蹲/冲刺事件带元组载荷，配合 [listenable function](../../01_Verse.org/010_Verse/listenable.md) 的 Subscribe 使用。
