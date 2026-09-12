---
name: editable_vector_number
slug: versedotorg/simulation/editable_vector_number
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/editable_vector_number
kind: function
module: /Verse.org/Simulation
grade: A
depth: full
status: done
---

# editable_vector_number function 🟩【A级·常用】

> （本页官网无导语描述。）
> editable_vector_number 是参数化类型构造器：按给定数字类型 t 生成一个"编辑器详情面板三维向量数字输入"类（X/Y/Z 三个输入框）。

`using { /Verse.org/Simulation }`

```verse
editable_vector_number<public>(t:any):
```

This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
（此函数是参数化类型：它返回的是类或接口，而不是值或对象实例。）

## Parameters

editable_vector_number takes the following parameters:（editable_vector_number 接受以下参数：）

| Name | Type | Description |
|---|---|---|
| t | any | 各分量的数字类型，常用 `int` 或 `float`。 |

## Attributes, Specifiers, and Effects

`editable_vector_number<public>(t:any)` —— 标签：public，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Simulation }
using { /Verse.org/SpatialMath }

mover := class(creative_device):

    @editable
    Offset : editable_vector_number = editable_vector_number{Default := vector3{Up := 100.0}}

    OnBegin<override>()<suspends>:void =
        V := Offset.GetCurrentValue()   # t=float 时返回 vector3
        Print("向上偏移 {V.Up}")
```

## 补充说明

- 取值返回 [vector3 struct](../130_SpatialMath/vector3.md)（注意其分量名为 Left/Up/Forward）。
- 三个数含义独立时（如"血量/护盾/能量"）拆成多个 [editable_number function](editable_number.md) 更清晰。
