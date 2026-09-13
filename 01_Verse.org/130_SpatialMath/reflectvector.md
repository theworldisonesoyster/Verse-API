---
name: ReflectVector
slug: versedotorg/spatialmath/reflectvector
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/reflectvector
kind: function
module: /Verse.org/spatialmath
grade: B
depth: brief
status: done
---

# ReflectVector function <B>

> Makes a vector3 by inverting the SurfaceNormal component of Direction.
> 反转 Direction 中 SurfaceNormal 方向的分量，得到反射向量。

`using { /Verse.org/SpatialMath }`

```verse
ReflectVector<public>(Direction:vector3, SurfaceNormal:vector3):vector3
```

## Parameters

ReflectVector 接受以下参数：
| Name | Type | Description |
| Direction | vector3 |  |
| SurfaceNormal | vector3 |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
