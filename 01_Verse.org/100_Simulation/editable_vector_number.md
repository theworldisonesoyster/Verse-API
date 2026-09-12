---
name: editable_vector_number
slug: versedotorg/simulation/editable_vector_number
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/editable_vector_number
kind: class
module: /Verse.org/Simulation
grade: A
depth: full
status: done
---

# editable_vector_number 🟩【A级·常用】

> Parametric type that exposes a 3-component vector field in the Details panel.
> 参数化类型：在详情面板暴露一个三维向量输入（X/Y/Z 三个数字框）。

## 签名

```verse
editable_vector_number<public>(t:any) := class<concrete>(editable_object):
    # 参数 t 常用 int 或 float
```

## 这是什么

[editable_number](editable_number.md) 的三维版：一次编辑三个分量，常用于"偏移量""缩放""速度方向"这类向量参数。读取 `GetCurrentValue()` 返回 [vector3](../130_SpatialMath/vector3.md)（t 为 float 时）。

## 最小示例

```verse
using { /Verse.org/Simulation }
using { /Verse.org/SpatialMath }

mover := class(creative_device):

    @editable
    Offset : editable_vector_number = editable_vector_number{Default := vector3{Up := 100.0}}

    OnBegin<override>()<suspends>:void =
        V := Offset.GetCurrentValue()
        Print("向上偏移 {V.Up}")
```

## 常用成员

| 成员 | 签名 | 说明 | 级别 |
|---|---|---|---|
| `GetCurrentValue` | `():vector3` | 取当前向量（t=float 时） | 🟩 A |
| `Default` / `Min` / `Max` | 属性 | 默认值与范围（按分量生效） | 🟩 A |

## 何时用 / 何时不用

- 用：位置偏移、方向、比例等成组出现的三个数。
- 不用：三个数含义独立（比如"血量/护盾/能量"）——拆成三个 editable_number 语义更清楚。

## 常见坑

- `t=int` 时各分量取整，做精确位移请用 float。

## 相关页面

- [editable_vector_slider](editable_vector_slider.md)
- [vector3](../130_SpatialMath/vector3.md)
