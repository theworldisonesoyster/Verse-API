---
name: rotation
slug: versedotorg/spatialmath/rotation
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/rotation
kind: class
module: /Verse.org/SpatialMath
grade: S
depth: full
status: done
---

# rotation 🟦【S级·核心】

> 三维旋转（四元数表示的 struct）；实体"朝向"的统一类型。

## 这是什么

`rotation` 表示空间中的旋转。它是无公开分量的 struct——**全部通过模块级工厂函数构造**，不直接操纵内部数据：

- 按欧拉角：`MakeRotationFromEulerDegrees(Pitch, Yaw, Roll)`（以及 Radians/FromYawPitchRoll 变体）
- 朝向某方向：配合 vector3 使用 `MakeShortestRotationBetween`
- 单位旋转：`IdentityRotation()`

组合与插值：`A * B` 依次施加旋转，`Slerp` 球面插值（平滑转身）。与 [vector3](vector3.md) 相乘可旋转一个向量。

## 签名

```verse
rotation<public><native> := struct:
    # 无公开数据成员；经工厂函数构造
```

## 最小示例

```verse
using { /Verse.org/SpatialMath }

FaceEast():rotation =
    MakeRotationFromEulerDegrees(0.0, 90.0, 0.0)   # Pitch=0, Yaw=90°, Roll=0

HalfTurn():rotation =
    Slerp(IdentityRotation(), FaceEast(), 0.5)     # 中间朝向
```

## 常用配套函数

| 函数 | 说明 | 级别 |
|---|---|---|
| `MakeRotationFromEulerDegrees(P,Y,R)` | 最常用构造 | 🟦 S |
| `IdentityRotation()` | 单位旋转 | 🟦 S |
| `MakeRotationFromYawPitchRollDegrees` | 仅 yaw/pitch/roll 的变体 | 🟩 A |
| `Slerp(A, B, t)` | 球面插值 | 🟨 B |
| `MakeShortestRotationBetween` | 最短转向 | 🟨 B |
| `AngularDistanceDegrees` | 夹角 | 🟨 B |

## 何时用 / 何时不用

- 用：设置实体朝向、相机转向、转向插值动画。
- 不用：只有位置没有朝向的改动用 vector3 就够。

## 常见坑

- 欧拉角单位分 Degrees/Radians 两套函数，混用是常见错误源——工程内统一用 Degrees。
- 旋转组合 `A * B` 的先后顺序有语义（先 B 后 A），直觉不确定时小步验证。

## 相关页面

- [vector3](vector3.md)
- [transform](rotation.md) 同族：transform = 位置＋旋转＋缩放（见 SpatialMath 总览）
