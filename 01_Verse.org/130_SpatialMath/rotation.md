---
name: rotation
slug: versedotorg/spatialmath/rotation
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/rotation
kind: struct
module: /Verse.org/SpatialMath
grade: S
depth: full
status: done
---

# rotation struct <S>

> An abstract representation of an orientation change in 3d-space.
> 三维空间中朝向变化的抽象表示。

`using { /Verse.org/SpatialMath }`

## Members

This struct has no members.（此结构体没有成员——构造与运算全部通过 [SpatialMath module](../_overview.md) 的工厂函数完成。）

## 示例

```verse
using { /Verse.org/SpatialMath }

FaceEast():rotation =
    MakeRotationFromEulerDegrees(0.0, 90.0, 0.0)   # Pitch=0, Yaw=90°, Roll=0

HalfTurn():rotation =
    Slerp(IdentityRotation(), FaceEast(), 0.5)     # 中间朝向（球面插值）
```

## 补充说明

- 常用工厂函数（均在 SpatialMath 模块）：MakeRotationFromEulerDegrees / MakeRotationFromEulerRadians / MakeRotationFromYawPitchRollDegrees、IdentityRotation、Slerp、MakeShortestRotationBetween、AngularDistanceDegrees 等。
- 度/弧度是两套函数（…Degrees / …Radians），工程内统一用 Degrees 可避免混用错误。
- 相关页面：[vector3 struct](vector3.md)、[transform_component class](../040_SceneGraph/transform_component.md)。
