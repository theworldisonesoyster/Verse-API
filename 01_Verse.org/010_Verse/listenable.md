---
name: listenable
slug: versedotorg/verse/listenable
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/listenable
kind: function
module: /Verse.org/Verse
grade: S
depth: full
status: done
---

# listenable function 🟦【S级·核心】

> A parametric interface combining awaitable and subscribable.
> 参数化**接口**：组合了 awaitable（可等待）与 subscribable（可订阅）。

`using { /Verse.org/Verse }`

```verse
listenable<public>(payload:any):listenable(payload)
```

This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
（此函数是参数化类型：它返回的是类或接口，而不是值或对象实例。）

## Parameters

listenable takes the following parameters:（listenable 接受以下参数：）

| Name | Type | Description |
|---|---|---|
| payload | any | 订阅回调接收的载荷类型。 |

### Generated Interface

listenable returns the parametric interface `listenable(payload)`.（listenable 返回参数化接口 listenable(payload)。）

## Attributes, Specifiers, and Effects

`listenable<public>(payload:any):listenable(payload)` —— 标签：public，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Verse }
using { /Fortnite.com/Devices }

# 订阅按钮设备的交互事件（设备事件都是现成的 listenable）
MyDevice := class(creative_device):

    @editable
    MyButton : button_device = button_device{}

    OnBegin<override>()<suspends>:void =
        MyButton.InteractedWithEvent.Subscribe(OnButtonPressed)

    OnButtonPressed(Agent:agent):void =
        Print("按钮被按下")
```

## 补充说明

- listenable 与 [event(t) class](event_t.md) 的分工：listenable 面向"持续广播、多方订阅"（设备事件、玩家进出），event 面向"脚本内部一次性等待"。
- 订阅回调是类成员函数；订阅时机通常在 OnBegin 中完成，避免漏事件。
