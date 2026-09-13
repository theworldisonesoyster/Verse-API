---
name: SpatialMath module
slug: versedotorg/spatialmath
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath
kind: module
module: /versedotorg
grade: A
depth: brief
status: done
---

# SpatialMath module <A>

三维数学：vector3/rotation/transform 三大类型与构造、距离、点积/叉积、插值等函数。

## Classes and Structs

| Name | Description |
|---|---|
| [rotation](rotation.md) | 三维空间中朝向变化的抽象表示。 |
| [transform](transform.md) | 缩放、旋转、平移的组合，按此顺序应用。 |
| [vector3](vector3.md) | 带浮点分量的三维向量。 |

## Functions

| Name | Description |
|---|---|
| [MakeRotationRadians](makerotationradians.md) | 用 Axis 与 Angle（弧度，右手系）构造旋转：例如绕 Up 的正旋转会把 Forward 转向 Left。 |
| [MakeRotationDegrees](makerotationdegrees.md) | MakeRotationRadians 的角度（Degrees）版本。 |
| [MakeRotationFromYawPitchRollRadians](makerotationfromyawpitchrollradians.md) | 以 Yaw、Pitch、Roll 的顺序做预旋转，构造旋转（右手系）。 |
| [MakeRotationFromYawPitchRollDegrees](makerotationfromyawpitchrolldegrees.md) | 上者的角度版本。 |
| [MakeRotationFromEulerRadians](makerotationfromeulerradians.md) | 以 Left、Up、Forward 轴的顺序做后旋转，构造旋转（右手系）。 |
| [MakeRotationFromEulerDegrees](makerotationfromeulerdegrees.md) | 上者的角度版本。 |
| [IdentityRotation](identityrotation.md) | 构造单位旋转。 |
| [Distance](distance.md) | 返回 Rotation1 与 Rotation2 之间的距离：0.0 表示等价旋转，1.0 表示相对（相反）旋转。 |
| [AngularDistanceRadians](angulardistanceradians.md) | 返回两旋转间的最小角距离（弧度）。 |
| [AngularDistanceDegrees](angulardistancedegrees.md) | 上者的角度版本。 |
| [operator'*'](operatorstar.md) | 把 PreRotation 前置应用到 PostRotation（v * PreRotation * PostRotation）。 |
| [MakeShortestRotationBetween](makeshortestrotationbetween.md) | 构造从 InitialVector 转到 FinalVector 的最小角度旋转（向量长度任意）。 |
| [Slerp](slerp.md) | 在 From（Ratio=0.0）与 To（Ratio=1.0）之间做球面线性插值；要求 0.0 ≤ Ratio ≤ 1.0。 |
| [operator'*'](operatorstar-1.md) | 用 Rotation 旋转 Vector，得到新的 vector3。 |
| [ToString](tostring.md) | 以轴/角度格式（右手系）返回旋转的字符串表示。 |
| [DegreesToRadians](degreestoradians.md) | 把角度转为弧度。 |
| [RadiansToDegrees](radianstodegrees.md) | 把弧度转为角度。 |
| [operator'*'](operatorstar-2.md) | 用 InTransform（缩放＋旋转＋平移）变换 InVector。 |
| [ToString](tostring-1.md) | 返回 InTransform 的字符串表示（Translation/Rotation/Scale 形式）。 |
| [ReflectVector](reflectvector.md) | 反转 Direction 中 SurfaceNormal 方向的分量，得到反射向量。 |
| [DotProduct](dotproduct.md) | 返回 V1 与 V2 的点积。 |
| [CrossProductLeftHanded](crossproductlefthanded.md) | 返回 V1 与 V2 的左手叉积。 |
| [CrossProduct](crossproduct.md) | 返回 V1 与 V2 的右手叉积。 |
| [Distance](distance-1.md) | 返回 V1 与 V2 的欧氏距离。 |
| [DistanceSquared](distancesquared.md) | 返回 V1 与 V2 欧氏距离的平方（比较远近时代价比 Distance 低）。 |
| [DistanceForwardLeft](distanceforwardleft.md) | 忽略 Up 分量差异后的二维欧氏距离。 |
| [DistanceSquaredForwardLeft](distancesquaredforwardleft.md) | 上者的平方版本。 |
| [ToString](tostring-2.md) | 返回 V 的字符串表示。 |
| [Lerp](lerp.md) | 在 From（Parameter=0.0）与 To（Parameter=1.0）之间线性插值/外推；要求所有参数有限。 |
| [prefix'-'](prefixminus.md) | 取负：各分量变号。 |
| [operator'+'](operatorplus.md) | Left 与 Right 逐分量相加。 |
| [operator'-'](operatorminus.md) | Left 逐分量减去 Right。 |
| [operator'*'](operatorstar-3.md) | Left 与 Right 逐分量相乘。 |
| [operator'*'](operatorstar-4.md) | Left 的各分量乘以 Right。 |
