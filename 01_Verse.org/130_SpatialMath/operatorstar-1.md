---
name: operator'*'
slug: versedotorg/spatialmath/operatorstar-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/operatorstar-1
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

# operator'*' function <A>

> Makes a vector3 by applying Rotation to Vector.
> 用 Rotation 旋转 Vector，得到新的 vector3。

`using { /Verse.org/SpatialMath }`

```verse
operator'*'<public><native>(Vector:vector3, Rotation:rotation):vector3
```

## Parameters

operator'*' 接受以下参数：
| Name | Type | Description |
| Vector | vector3 |  |
| Rotation | rotation |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
V := vector3{Forward:=1.0} * MakeRotationDegrees(0.0, 90.0, 0.0)
```
