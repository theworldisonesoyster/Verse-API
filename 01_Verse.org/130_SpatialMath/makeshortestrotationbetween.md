---
name: MakeShortestRotationBetween
slug: versedotorg/spatialmath/makeshortestrotationbetween
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/makeshortestrotationbetween
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

# MakeShortestRotationBetween function <A>

> Makes the smallest angular rotation from InitialVector to FinalVector two vectors of arbitrary length such that: InitialVector * MakeShortestRotationBetween(InitialVector, FinalVector) = FinalVector and MakeShortestRotationBetween(InitialVector, FinalVector)?.GetAngleRadians() is as small as possible.
> 构造从 InitialVector 转到 FinalVector 的最小角度旋转（向量长度任意）。

`using { /Verse.org/SpatialMath }`

```verse
MakeShortestRotationBetween<public><native>(InitialVector:vector3, FinalVector:vector3):rotation
```

## Parameters

MakeShortestRotationBetween 接受以下参数：
| Name | Type | Description |
| InitialVector | vector3 |  |
| FinalVector | vector3 |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
R := MakeShortestRotationBetween(vector3{Forward:=1.0}, vector3{Left:=1.0})
```
