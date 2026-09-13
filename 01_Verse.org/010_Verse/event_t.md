---
name: event(t)
slug: versedotorg/verse/event/event(t)
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/event/event(t)
kind: class
module: /Verse.org/Verse
grade: S
depth: full
status: done
---

# event(t) class <S>

> A recurring, successively signaled parametric event with a payload allowing a simple mechanism to coordinate between concurrent tasks.
> 可重复、按次序触发的参数化事件，带有载荷，为并发任务之间的协调提供简单机制。

`using { /Verse.org/Verse }`

## Exposed Interfaces

This class exposes the following interfaces:（此类暴露以下接口：）

| Name | Description |
|---|---|
| signalable(payload) | 带载荷、可被触发（signal）的事件所实现的参数化接口。可与 awaitable、subscribable 配合使用（参见 listenable）。 |
| awaitable(payload) | 带载荷、可被等待（await）的事件所实现的参数化接口。与 signalable 配对。 |

## Members

This class has functions, but no data members.（此类只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| [Await](event_t_await.md) | 挂起当前任务，直到另一个任务调用 Signal。若在 Signal 的调用过程中调用 Await，任务仍会挂起，并等到**下一次** Signal 调用时恢复。 |
| [Signal](event_t_signal.md) | 并发恢复在此次 Signal 之前被 Await 挂起的任务。任务按挂起的先后顺序恢复；每个任务会尽可能执行直到遇到阻塞调用，随即把控制权交给下一个被挂起的任务。 |

## Attributes, Specifiers, and Effects

`event(t:any)<public> := class<concrete>(subscribable(t), signalable(t))` —— 标签：public / concrete，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Verse }
using { /Verse.org/Simulation }

Counter := class:
    Tick:event(int) = event(int){}   # int 载荷事件

    Run()<suspends>:void =
        N := Tick.Await()            # 挂起等待，Signal 一到即恢复
        Print("收到 {N}")

    Bump():void =
        Tick.Signal(1)
```

## 补充说明

- `Await` 只等**下一次** Signal：信号发出时若无等待者，载荷不会被记住（先有等待者，后有 Signal）。
- 类内声明事件字段要带构造：`Tick:event(int) = event(int){}`；构造函数见 [event function](event.md)。
- 与设备/系统交互用 [listenable function](listenable.md)（订阅模型），自建 event 用于脚本内部的即时协调。
