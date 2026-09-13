---
name: Slerp
slug: versedotorg/spatialmath/slerp
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/slerp
kind: function
module: /Verse.org/spatialmath
grade: B
depth: brief
status: done
---

# Slerp function <B>

> Used to perform spherical linear interpolation between From (when Ratio = 0.0) and To (when Ratio = 1.0). Expects 0.0 <= Ratio <= 1.0.
> 在 From（Ratio=0.0）与 To（Ratio=1.0）之间做球面线性插值；要求 0.0 ≤ Ratio ≤ 1.0。

`using { /Verse.org/SpatialMath }`

```verse
Slerp<public><native>(InitialRotation:rotation, FinalRotation:rotation, Ratio:float):rotation
```

## Parameters

Slerp 接受以下参数：
| Name | Type | Description |
| InitialRotation | rotation |  |
| FinalRotation | rotation |  |
| Ratio | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
