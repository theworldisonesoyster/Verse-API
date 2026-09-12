---
name: editable_vector_slider
slug: versedotorg/simulation/editable_vector_slider
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/editable_vector_slider
kind: class
module: /Verse.org/Simulation
grade: A
depth: full
status: done
---

# editable_vector_slider 🟩【A级·常用】

> Parametric type that exposes three sliders (X/Y/Z) in the Details panel.
> 参数化类型：详情面板上暴露 X/Y/Z 三条滑条。

## 签名

```verse
editable_vector_slider<public>(t:any) := class<concrete>(editable_object):
    # 参数 t 常用 int 或 float
```

## 这是什么

[editable_vector_number](editable_vector_number.md) 的滑条版：三个分量各一条滑条，适合在范围内"拖出感觉"的向量参数（如风向强度、颜色分量配合使用时）。用法与读取函数与 editable_vector_number 完全一致。

## 最小示例

```verse
using { /Verse.org/Simulation }
using { /Verse.org/SpatialMath }

wind := class(creative_device):

    @editable
    Strength : editable_vector_slider = editable_vector_slider{Default := vector3{Up := 1.0}}

    OnBegin<override>()<suspends>:void =
        Print("风力向量 = {Strength.GetCurrentValue()}")
```

## 常用成员

| 成员 | 签名 | 说明 | 级别 |
|---|---|---|---|
| `GetCurrentValue` | `():vector3` | 取当前向量 | 🟩 A |
| `Default` / `Min` / `Max` | 属性 | 默认值与滑条范围 | 🟩 A |

## 何时用 / 何时不用

- 用：连续可调的三维量。
- 不用：需要精确键入的坐标——用 editable_vector_number。

## 相关页面

- [editable_vector_number](editable_vector_number.md)
- [editable_slider](editable_slider.md)
