---
name: MakeRotationRadians
slug: versedotorg/spatialmath/makerotationradians
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/makerotationradians
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

# MakeRotationRadians function <A>

> Makes a rotation from Axis and Angle in radians using a right-handed sign convention (e.g. a positive rotation around Up takes Forward to Left).
> 用 Axis 与 Angle（弧度，右手系）构造旋转：例如绕 Up 的正旋转会把 Forward 转向 Left。

`using { /Verse.org/SpatialMath }`

```verse
MakeRotationRadians<public><native>(Axis:vector3, Angle:float):rotation
```

## Parameters

MakeRotationRadians 接受以下参数：
| Name | Type | Description |
| Axis | vector3 |  |
| Angle | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
