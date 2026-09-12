---
name: session
slug: versedotorg/simulation/session
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/session
kind: class
module: /Verse.org/Simulation
grade: A
depth: full
status: done
---

# session 🟩【A级·常用】

> Type for which there is a single instance per round. Use GetSession to get the current round's session instance.
> 每一回合只存在一个实例的类型。用 GetSession 取当前回合的实例。

## 这是什么

Verse 没有"全局变量"这个概念，但 `session` ＋ `weak_map` 是官方给出的替代方案：`session` 保证每回合只有一个实例，把它当 weak_map 的 key，就能存"整局共享"的数据——比分、配置、世界状态。官方注明：未来可能改为"每局游戏一个实例"，不要依赖"每回合重置"的行为。

## 签名

```verse
session<public><epic_internal> := class<epic_internal>:
    # 无自有成员；作为唯一 key 使用
```

## 最小示例

```verse
using { /Verse.org/Simulation }

# "全局变量"标准写法
var GlobalScoreMap:weak_map[session, int] = map{}

AddGlobalScore(Points:int):void =
    S := GetSession()
    Current := GlobalScoreMap[S] or 0     # 取不到就用 0
    if (set GlobalScoreMap[S] = Current + Points) {}
```

## 常用成员

| 名称 | 形式 | 说明 | 级别 |
|---|---|---|---|
| `GetSession()` | 模块函数 | 取当前 session 实例 | 🟩 A |
| `weak_map[session, T]` | 组合用法 | session 作 key 存全局数据 | 🟩 A |
| [session_environment](session_environment.md) | 枚举 | 判断当前是编辑/私人/线上环境 | 🟨 B |

## 何时用 / 何时不用

- 用：跨设备/跨脚本共享状态、模块级计分板、配置单例。
- 不用：只和单个玩家有关的数据——用 `weak_map[player, T]` 更贴切；每帧变化的大量数据别往全局塞。

## 常见坑

- 官方明示**回合级行为可能变化**，别把"回合结束自动清空"当保证，需要重置就显式重置。
- `weak_map` 的键是弱引用，取值是可失败操作，统一用 `Map[Key] or 默认值` 的写法最稳。

## 相关页面

- [GetSession](getsession.md) —— 拿实例
- [session_environment](session_environment.md)
- [Verse 核心的 weak_map](../010_Verse/weak_map.md)
