---
name: operator'*'
slug: versedotorg/spatialmath/operatorstar
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/operatorstar
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

# operator'*' function <A>

> Apply a PreRotation to PostRotation as v * PreRotation * PostRotation.
> 把 PreRotation 前置应用到 PostRotation（v * PreRotation * PostRotation）。

`using { /Verse.org/SpatialMath }`

```verse
operator'*'<public><native>(PreRotation:rotation, PostRotation:rotation):rotation
```

## Parameters

operator'*' 接受以下参数：
| Name | Type | Description |
| PreRotation | rotation |  |
| PostRotation | rotation |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
Combined := IdentityRotation() * MakeRotationDegrees(0.0, 90.0, 0.0)
```
