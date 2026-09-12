---
name: GetSession
slug: versedotorg/simulation/getsession
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/getsession
kind: function
module: /Verse.org/Simulation
grade: A
depth: full
status: done
---

# GetSession function 🟩【A级·常用】

> Returns the session corresponding to the current round. The result can be used with `weak_map` to implement global variables. Note: may be changed in a future release to return a single instance per game. Round-local behavior should not be relied upon.
> 返回当前回合对应的 session 实例。结果可配合 `weak_map` 实现全局变量。注意：未来版本可能改为"每局游戏返回一个实例"，请勿依赖其回合级行为。

`using { /Verse.org/Simulation }`

```verse
GetSession<public><native>():session
```

## Parameters

GetSession does not take any parameters.（GetSession 不接受任何参数。）

## Attributes, Specifiers, and Effects

`GetSession<public><native>():session` —— 标签：public / native，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Simulation }

var Visited:weak_map[session, logic] = map{}

MarkVisited():void =
    if (set Visited[GetSession()] = true) {}

WasVisited():logic =
    Visited[GetSession()] or false
```

## 补充说明

- `session` 类没有公开构造方式，全局唯一实例只能从这里拿；它最重要的用法是当 `weak_map` 的 key 存"整局共享"的状态。
- 相关页面：[session class](session.md)。
