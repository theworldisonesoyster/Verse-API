---
name: editable_vector_slider
slug: versedotorg/simulation/editable_vector_slider
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/editable_vector_slider
kind: function
module: /Verse.org/Simulation
grade: A
depth: full
status: done
---

# editable_vector_slider function <A>

> （本页官网无导语描述。）
> editable_vector_slider 是参数化类型构造器：按给定数字类型 t 生成一个"编辑器详情面板三维向量滑条"类（X/Y/Z 三条滑条）。

`using { /Verse.org/Simulation }`

```verse
editable_vector_slider<public>(t:any):
```

This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
（此函数是参数化类型：它返回的是类或接口，而不是值或对象实例。）

## Parameters

editable_vector_slider takes the following parameters:（editable_vector_slider 接受以下参数：）

| Name | Type | Description |
|---|---|---|
| t | any | 各分量的数字类型，常用 `int` 或 `float`。 |

## Attributes, Specifiers, and Effects

`editable_vector_slider<public>(t:any)` —— 标签：public，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Simulation }
using { /Verse.org/SpatialMath }

wind := class(creative_device):

    @editable
    Strength : editable_vector_slider = editable_vector_slider{Default := vector3{Up := 1.0}}

    OnBegin<override>()<suspends>:void =
        Print("风力向量 = {Strength.GetCurrentValue()}")
```

## 补充说明

- 与 [editable_vector_number function](editable_vector_number.md) 同构，滑条外观适合"拖出感觉"的连续向量参数。
