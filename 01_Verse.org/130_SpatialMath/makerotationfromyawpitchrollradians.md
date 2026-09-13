---
name: MakeRotationFromYawPitchRollRadians
slug: versedotorg/spatialmath/makerotationfromyawpitchrollradians
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/makerotationfromyawpitchrollradians
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

# MakeRotationFromYawPitchRollRadians function <A>

> Makes a rotation by applying a pre-rotation of YawAngle followed by PitchAngle and then RollAngle, in that order:
> - yaw is right-handed rotation about the Down axis,
> - pitch is right-handed rotation about the Right axis,
> - roll is right-handed rotation about the Forward axis.
> 以 Yaw、Pitch、Roll 的顺序做预旋转，构造旋转（右手系）。

`using { /Verse.org/SpatialMath }`

```verse
MakeRotationFromYawPitchRollRadians<public>(YawAngle:float, PitchAngle:float, RollAngle:float):rotation
```

## Parameters

MakeRotationFromYawPitchRollRadians 接受以下参数：
| Name | Type | Description |
| YawAngle | float |  |
| PitchAngle | float |  |
| RollAngle | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
