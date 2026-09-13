---
name: event
slug: versedotorg/verse/event-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/event-1
kind: function
module: /Verse.org/Verse
grade: S
depth: full
status: done
---

# event function（无载荷）<S>

> A recurring, successively signaled event allowing a simple mechanism to coordinate between concurrent tasks.
> 可重复、按次序触发的事件，为并发任务之间的协调提供简单机制（本重载不带构造参数，载荷类型由上下文推断）。

`using { /Verse.org/Verse }`

```verse
event<public>():event(t)
```

## Parameters

event does not take any parameters.（event 不接受任何参数。）

## Attributes, Specifiers, and Effects

`event<public>():event(t)` —— 标签：public，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Verse }
using { /Verse.org/Simulation }

Kickoff:event() = event(){}

WaitAndGo()<suspends>:void =
    Kickoff.Await()      # 不关心载荷，只等信号
    Print("GO!")
```

## 补充说明

- Signal/Await 的行为见 [event(t) class](event_t.md)；带载荷的构造见 [event function](event.md)。
