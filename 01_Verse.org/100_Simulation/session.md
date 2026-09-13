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

# session class <A>

> Type for which there is a single instance per round. Use `GetSession` to get the current round's session instance. May be used with `weak_map` to implement global variables. Note: may be changed in a future release to a single instance per game. Round-local behavior should not be relied upon.
> 每一回合只存在一个实例的类型。用 `GetSession` 获取当前回合的 session 实例。可配合 `weak_map` 实现全局变量。注意：未来版本可能改为"每局游戏一个实例"，请勿依赖其回合级行为。

`using { /Verse.org/Simulation }`

## Members

This class has no members.（此类没有成员。）

## Attributes, Specifiers, and Effects

`session<public><epic_internal> := class<epic_internal>` —— 标签：public / epic_internal，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Simulation }

# "全局变量"标准写法：session 作 weak_map 的 key
var GlobalScore:weak_map[session, int] = map{}

AddScore(Points:int):void =
    S := GetSession()
    Current := GlobalScore[S] or 0
    if (set GlobalScore[S] = Current + Points) {}
```

## 补充说明

- Verse 没有传统"全局变量"，session ＋ `weak_map` 是官方给出的替代方案。
- 官方明示回合级行为可能变化——需要"每回合重置"就显式重置，别靠换实例。
- 相关页面：[GetSession function](getsession.md)、[session_environment enumeration](session_environment.md)、[weak_map function](../010_Verse/weak_map.md)。
