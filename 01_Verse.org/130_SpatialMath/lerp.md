---
name: Lerp
slug: versedotorg/spatialmath/lerp
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/lerp
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

# Lerp function <A>

> Used to linearly interpolate/extrapolate between From (when Parameter = 0.0) and To (when Parameter = 1.0). Expects that all arguments are finite. Returns From*(1 - Parameter) + To*Parameter.
> 在 From（Parameter=0.0）与 To（Parameter=1.0）之间线性插值/外推；要求所有参数有限。

`using { /Verse.org/SpatialMath }`

```verse
Lerp<public>(From:vector3, To:vector3, Parameter:float):vector3
```

## Parameters

Lerp 接受以下参数：
| Name | Type | Description |
| From | vector3 |  |
| To | vector3 |  |
| Parameter | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
M := Lerp(0.0, 10.0, 0.25)   # 2.5
```
