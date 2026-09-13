---
name: MakeRotationFromEulerRadians
slug: versedotorg/spatialmath/makerotationfromeulerradians
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/makerotationfromeulerradians
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

# MakeRotationFromEulerRadians function <A>

> Makes a rotation by applying a post-rotation of LeftAxisAngle followed by UpAxisAngle and then ForwardAxisAngle in that order. Right-handed convention (e.g. a positive rotation around Up takes +Forward to Left).
> 以 Left、Up、Forward 轴的顺序做后旋转，构造旋转（右手系）。

`using { /Verse.org/SpatialMath }`

```verse
MakeRotationFromEulerRadians<public><native>(LeftAxisAngle:float, UpAxisAngle:float, ForwardAxisAngle:float):rotation
```

## Parameters

MakeRotationFromEulerRadians 接受以下参数：
| Name | Type | Description |
| LeftAxisAngle | float |  |
| UpAxisAngle | float |  |
| ForwardAxisAngle | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
