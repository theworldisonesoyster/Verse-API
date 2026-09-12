---
name: editable_number
slug: versedotorg/simulation/editable_number
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/editable_number
kind: class
module: /Verse.org/Simulation
grade: S
depth: full
status: done
---

# editable_number 🟦【S级·核心】

> Parametric type that exposes a numeric field in the editor's Details panel.
> 参数化类型：在 UEFN 详情面板上暴露一个可编辑的数字输入框。

## 签名

```verse
editable_number<public>(t:any) := class<concrete>(editable_object):
    # 参数 t 决定数字类型，常用 int 或 float
```

## 这是什么

写"自定义设备"的核心模式：把类成员声明成 `@editable` 的 `editable_number`，编辑器右侧详情面板就会出现一个数字框，关卡作者不写代码就能调这个值。`t` 填 `int` 就是整数框，填 `float` 就是小数框。

配套读取函数 `GetCurrentValue()`（返回 t 类型）取用户填的值。同一族的还有 [editable_slider](editable_slider.md)（滑条）、[editable_vector_number](editable_vector_number.md)/[editable_vector_slider](editable_vector_slider.md)（三维向量）。

## 最小示例

```verse
using { /Verse.org/Simulation }
using { /Fortnite.com/Devices }

# 一个可调"节拍间隔"的自定义设备
beat_device := class(creative_device):

    @editable
    Interval : editable_number = editable_number{Default := 0.5, Min := 0.1, Max := 5.0}

    var BeatClock : beat_clock = beat_clock{}

    OnBegin<override>()<suspends>:void =
        IntervalNumber := Interval.GetCurrentValue()   # float
        Print("节拍间隔 = {IntervalNumber}")
```

## 常用成员

| 成员 | 签名 | 说明 | 级别 |
|---|---|---|---|
| `GetCurrentValue` | `():t` | 取详情面板当前值 | 🟦 S |
| `Default` / `Min` / `Max` | 属性 | 声明处设置默认值与范围 | 🟦 S |

## 何时用 / 何时不用

- 用：任何想让别人"不写代码就能调"的参数：数量、间隔、概率、阈值。
- 不用：运行中要变的值——editable 是"关卡作者在编辑器里调"的入口，运行时请用 `var`。

## 常见坑

- 忘写 `@editable` 特性，面板上就不会出现这个字段。
- `Min/Max` 只约束面板输入，代码里仍要防范越界值。

## 相关页面

- [editable_slider](editable_slider.md) —— 同族滑条版
- [creative_device](../../../03_Fortnite.com/070_Devices/creative_device.md) —— editable 的宿主基类
