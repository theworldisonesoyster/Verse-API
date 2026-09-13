---
name: editable_number
slug: versedotorg/simulation/editable_number
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/editable_number
kind: function
module: /Verse.org/Simulation
grade: S
depth: full
status: done
---

# editable_number function <S>

> （本页官网无导语描述。）
> editable_number 是参数化类型构造器：按给定的数字类型 t 生成一个"编辑器详情面板数字输入"类。

`using { /Verse.org/Simulation }`

```verse
editable_number<public>(t:any):
```

This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
（此函数是参数化类型：它返回的是类或接口，而不是值或对象实例。）

## Parameters

editable_number takes the following parameters:（editable_number 接受以下参数：）

| Name | Type | Description |
|---|---|---|
| t | any | 输入框的数字类型，常用 `int` 或 `float`。 |

## Attributes, Specifiers, and Effects

`editable_number<public>(t:any)` —— 标签：public，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Simulation }
using { /Fortnite.com/Devices }

# 可调"节拍间隔"的自定义设备：详情面板出现数字输入框
beat_device := class(creative_device):

    @editable
    Interval : editable_number = editable_number{Default := 0.5, Min := 0.1, Max := 5.0}

    OnBegin<override>()<suspends>:void =
        N := Interval.GetCurrentValue()   # 取面板当前值（float）
        Print("节拍间隔 = {N}")
```

## 补充说明

- API Reference 本页只定义构造器本身；返回的类暴露的成员（如 `GetCurrentValue()`、`Default/Min/Max` 属性）以 UEFN 编辑器内提示与官方创作文档为准，本页不罗列。
- 必须在类成员上添加 `@editable` 特性，详情面板才会显示该控件。
- 同族：[editable_slider function](editable_slider.md)（滑条）、[editable_vector_number function](editable_vector_number.md)、[editable_vector_slider function](editable_vector_slider.md)。
