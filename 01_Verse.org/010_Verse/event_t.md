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

# event(t) 🟦【S级·核心】

> Signaling events with payloads of type t.
> 带类型 t 载荷的"信号事件"：一端触发（Signal），一端等待（Await）或订阅（Subscribe）。

## 这是什么

`event(t)` 是 Verse 异步协作的核心原语，理解成"类型化信箱"：

- **Signal(值)**：投递一个载荷，唤醒所有等待者，**不阻塞**调用方。
- **Await()**：阻塞当前协程直到下一次 Signal，返回载荷；只能在 `<suspends>` 上下文用。
- **Subscribe(对象)**：注册一个成员函数持续接收信号（实现 subscribable 接口）。
- **Reset()**：清空状态。

事件是"一次性信使"：`Await` 只拿**下一次** Signal 的值，没有"积压回放"。持续监听变化请配 listenable（设备事件都是 listenable）。

## 签名

```verse
event(t:any)<public> := class<concrete>(subscribable(t), signalable(t)):
    Await<public>()<suspends>:t          # 等待下一次信号并返回载荷
    Signal<public>(x:t):void             # 触发事件（广播载荷）
    Reset<public>():void                 # 重置内部状态
```

构造用参数化函数：`MyEvent := event(int){}`（见 [event](event.md) 构造页）。

## 最小示例

```verse
using { /Verse.org/Verse }
using { /Verse.org/Simulation }

Counter := class:
    Tick:event(int) = event(int){}       # 建一个 int 载荷事件
    var Count:int = 0

    Bump():void =
        set Count += 1
        Tick.Signal(Count)               # 广播

    Run()<suspends>:void =
        N := Tick.Await()                # 挂起等待，Signal 一到就醒
        Print("第 {N} 次计数")
```

## 常用成员

| 成员 | 签名 | 说明 | 级别 |
|---|---|---|---|
| `Signal` | `(x:t):void` | 触发，广播载荷 | 🟦 S |
| `Await` | `()<suspends>:t` | 等下一次信号，返回载荷 | 🟦 S |
| `Subscribe` | 来自 subscribable | 持续订阅（成员函数回调） | 🟩 A |
| `Reset` | `():void` | 清空 | 🟨 B |

## 何时用 / 何时不用

- 用：脚本内部"这里发生了，请那边继续"的协作；一次性的状态通知；配 `race` 做超时（`Await` 与 `Sleep(5.0)` 竞速）。
- 不用：与设备/玩家系统交互——那些是 listenable（Subscribe 模式），不是自建 event。

## 常见坑

- `Await` 丢历史：Signal 发生时若无人等待，载荷不会被记住。要先有等待者。
- `Signal` 不会等待处理者完成——广播后立刻返回。
- 类里声明事件字段要带构造：`Tick:event(int) = event(int){}`，缺了 `{}` 是空引用错误。

## 相关页面

- [event 构造函数](event.md)
- [listenable](listenable.md) —— 设备事件的订阅模型
- [Sleep](../100_Simulation/sleep.md) —— 配 race 做超时
