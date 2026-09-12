---
name: editable_slider
slug: versedotorg/simulation/editable_slider
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/editable_slider
kind: function
module: /Verse.org/Simulation
grade: S
depth: full
status: done
---

# editable_slider function 🟦【S级·核心】

> （本页官网无导语描述。）
> editable_slider 是参数化类型构造器：按给定的数字类型 t 生成一个"编辑器详情面板滑条"类。

`using { /Verse.org/Simulation }`

```verse
editable_slider<public>(t:any):
```

This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
（此函数是参数化类型：它返回的是类或接口，而不是值或对象实例。）

## Parameters

editable_slider takes the following parameters:（editable_slider 接受以下参数：）

| Name | Type | Description |
|---|---|---|
| t | any | 滑条的数值类型，常用 `int` 或 `float`。 |

## Attributes, Specifiers, and Effects

`editable_slider<public>(t:any)` —— 标签：public，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Simulation }
using { /Fortnite.com/Devices }

music_device := class(creative_device):

    @editable
    Volume : editable_slider = editable_slider{Default := 0.8, Min := 0.0, Max := 1.0}

    OnBegin<override>()<suspends>:void =
        Print("音量 = {Volume.GetCurrentValue()}")
```

## 补充说明

- 与 [editable_number function](editable_number.md) 同构，仅面板外观为滑条，适合连续量；离散档位建议用枚举型 editable。
- 返回类的成员（`GetCurrentValue()` 等）以 UEFN 编辑器内提示与官方创作文档为准。
