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

# player 🟦【S级·核心】

> A human participant in an experience. This class is derived from agent.
> 对局里的真人玩家，是 agent 的子类。

## 这是什么

`player` 代表一个坐在屏幕前的真人。凡是"针对这个人"的操作——查分数、发道具、开 UI、传送、绑定角色——最终都要落到 player 上。从设备事件拿到的 [agent](agent.md) 用可失败转换 `player[Agent]` 变成 player；反过来 player 可以隐式当 agent 用。

它继承自 [entity](../040_SceneGraph/entity.md)（SceneGraph），所以也带实体层函数，但玩法代码里最常用的还是"作为玩家身份"参与各类 API。与 player 强相关的进阶能力（角色、背包、进度）分布在其他模块：fort_character（角色身体）、inventory_component（物品栏）、quest（任务）。

## 签名

```verse
player<public><epic_internal> := class<epic_internal>(agent):
    # 官方未公开自有数据成员；作为"真人玩家"标识与各类 API 的入口类型
```

## 最小示例

```verse
using { /Verse.org/Simulation }

# 对局开始：给每个玩家发一次欢迎（遍历所有玩家）
OnBegin<override>()<suspends>:void =
    for (P : GetPlayspace().GetPlayers()):
        Print("欢迎，玩家！")
        Sleep(0.2)

# 从 agent 安全转 player
HandleAgent(A:agent):void =
    if (P := player[A]):
        Print("是真人玩家")
```

## 常用成员

| 名称 | 形式 | 说明 | 级别 |
|---|---|---|---|
| `player[Agent]` | 可失败转换 | agent → player | 🟦 S |
| `GetPlayspace().GetPlayers()` | 常配 | 当前全部玩家列表 | 🟩 A |
| `P.GetPlayerUI()` | 常配 | 拿玩家 UI 入口（Temporary/UI） | 🟦 S |
| 继承自 entity | `AddEntities` 等 | SceneGraph 实体操作 | 🟨 B |

## 何时用 / 何时不用

- 用：需要"这个人"的场合——计分、奖励、UI、按玩家存状态（weak_map[player]）。
- 不用：AI 单位也要参与的同一段逻辑，请把参数写成 agent，内部再分流。

## 常见坑

- 玩家中途退出后，player 引用失效；跨回合长期持有的逻辑要做有效性判断。
- `player[X]` 是可失败转换，必须写在失败上下文（`if`/`for`）里，不能裸调用。

## 相关页面

- [agent](agent.md) —— 父类，参数尽量用宽类型
- [session](session.md) —— 配合 weak_map 按玩家存"全局变量"
- [fort_character](../../../03_Fortnite.com/050_Characters/fort_character.md) —— 玩家在世界中的角色身体
