---
name: event() 构造函数（无载荷）
slug: versedotorg/verse/event-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/event-1
kind: function
module: /Verse.org/Verse
grade: S
depth: brief
status: done
---

# event() 构造函数（无载荷）🟦【S级·核心】

> event<public>():event(t) —— 不指定载荷类型的构造重载，由上下文推断 t。
> 无载荷事件只关心"发生了"这个事实，`Await()` 返回值忽略即可。

## 签名

```verse
event<public>():event(t)
```

## 最小示例

```verse
using { /Verse.org/Verse }

Kickoff:event() = event(){}

WaitAndGo()<suspends>:void =
    Kickoff.Await()      # 不关心载荷，只等信号
    Print("GO!")
```

## 相关页面

- [event(t) 类](event_t.md)
- [event 构造函数](event.md)
