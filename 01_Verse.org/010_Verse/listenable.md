---
name: listenable(payload) 构造
slug: versedotorg/verse/listenable
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/listenable
kind: function
module: /Verse.org/Verse
grade: S
depth: full
status: done
---

# listenable(payload) 构造 🟦【S级·核心】

> listenable<public>(payload:any):listenable(payload) —— 参数化构造：创建可被多方持续订阅的广播事件。
> 官方说明：This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.

## 这是什么

`listenable` 是"持续广播"的事件源，与 [event](event_t.md) 的"一次性等待"相对：

- **Subscribe(处理器)**：注册回调，之后**每次**触发都会收到，直到 Unsubscribe。
- **Signal**：一般由系统/内部触发——设备事件（如 `TriggerDevice.InteractedWithEvent`）就是现成的 listenable，你的代码通常只做 Subscribe。
- 处理器是**类的成员函数**，第一个参数自动传入订阅者实例，后续参数接载荷。

## 签名

```verse
listenable<public>(payload:any):listenable(payload)
```

## 最小示例

```verse
using { /Verse.org/Verse }
using { /Fortnite.com/Devices }

# 订阅按钮设备的交互事件（listenable 的典型用法）
MyDevice := class(creative_device):

    @editable
    MyButton : button_device = button_device{}

    OnBegin<override>()<suspends>:void =
        MyButton.InteractedWithEvent.Subscribe(OnButtonPressed)

    OnButtonPressed(Agent:agent):void =
        Print("{Agent} 按下了按钮")
```

## 常用成员

| 成员 | 说明 | 级别 |
|---|---|---|
| `Subscribe(Obj.函数)` | 持续订阅；返回 cancelable 句柄可退订 | 🟦 S |
| `Unsubscribe(句柄)` | 取消订阅 | 🟩 A |
| `Signal(载荷)` | 手动触发（自建 listenable 时） | 🟩 A |

## 何时用 / 何时不用

- 用：响应设备事件、玩家进出对局、回合开始结束——一切"系统推给你"的消息。
- 不用：脚本内部一次性握手用 event 更轻。

## 常见坑

- 订阅回调是**类成员函数**，写在类里；函数体不能 `<suspends>`（想异步处理就在回调里 `spawn`）。
- 订阅时机要在 `OnBegin` 里完成，晚了会漏事件。

## 相关页面

- [listenable-1](listenable-1.md) —— 无载荷构造
- [event(t) 类](event_t.md)
- [creative_device](../../../03_Fortnite.com/070_Devices/creative_device.md) —— 订阅设备事件的主战场
