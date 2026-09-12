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

# GetSession 🟩【A级·常用】

> Returns the session corresponding to the current round.
> 返回当前回合对应的 session 实例。

## 签名

```verse
GetSession<public><native>():session<transacts>
```

## 这是什么

`session` 类没有公开构造方式，全局唯一的实例就靠这个函数拿。它最重要的用法不是"用 session 做什么"，而是"**用 session 当 key**"：配合 `weak_map[session, T]` 实现跨脚本的全局状态。

## 最小示例

```verse
using { /Verse.org/Simulation }

var Visited:weak_map[session, logic] = map{}

MarkVisited():void =
    if (set Visited[GetSession()] = true) {}

WasVisited():logic =
    Visited[GetSession()] or false
```

## 何时用 / 何时不用

- 用：需要全局单例 key 的每一处；判断"这局"级别的状态。
- 不用：它不提供回合信息本身（如剩余时间），那是 round 设置/设备的事。

## 常见坑

- 官方注明未来可能变为"每局一个实例"，不要依赖"每回合换实例"来自动清状态。

## 相关页面

- [session](session.md) —— 类型本体与标准用法
- [GetSimulationElapsedTime](getsimulationelapsedtime.md)
