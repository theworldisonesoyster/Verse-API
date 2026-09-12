---
name: editable_slider
slug: versedotorg/simulation/editable_slider
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/editable_slider
kind: class
module: /Verse.org/Simulation
grade: S
depth: full
status: done
---

# editable_slider 🟦【S级·核心】

> Parametric type that exposes a slider in the editor's Details panel.
> 参数化类型：在详情面板上暴露一个滑条（拖动取值的数字控件）。

## 签名

```verse
editable_slider<public>(t:any) := class<concrete>(editable_object):
    # 参数 t 常用 int 或 float
```

## 这是什么

[editable_number](editable_number.md) 的滑条版：面板上显示为可拖动滑条，适合"在连续范围内调感觉"的参数——音量、角度、速度、透明度。声明方式与读取函数完全同 editable_number，只是外观与交互不同。

## 最小示例

```verse
using { /Verse.org/Simulation }
using { /Fortnite.com/Devices }

music_device := class(creative_device):

    @editable
    Volume : editable_slider = editable_slider{Default := 0.8, Min := 0.0, Max := 1.0}

    OnBegin<override>()<suspends>:void =
        Print("音量 = {Volume.GetCurrentValue()}")
```

## 常用成员

| 成员 | 签名 | 说明 | 级别 |
|---|---|---|---|
| `GetCurrentValue` | `():t` | 取滑条当前值 | 🟦 S |
| `Default` / `Min` / `Max` | 属性 | 默认值与滑条范围 | 🟦 S |

## 何时用 / 何时不用

- 用：连续量、需要"试着拖"的参数。
- 不用：离散选项（3 种模式、5 档难度）——那应该用枚举型 editable 或下拉。

## 常见坑

- 滑条精度受面板显示位数影响，要求精确整数时用 editable_number(int)。

## 相关页面

- [editable_number](editable_number.md) —— 数字输入版
- [editable_vector_slider](editable_vector_slider.md)
