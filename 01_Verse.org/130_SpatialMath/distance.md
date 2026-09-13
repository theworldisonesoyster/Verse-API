---
name: Distance
slug: versedotorg/spatialmath/distance
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/distance
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

# Distance function <A>

> Returns the distance between Rotation1 and Rotation2. The result will be between:
> - 0.0, representing equivalent rotations and
> - 1.0 representing rotations which are 180 degrees apart (i.e., the shortest rotation between them is 180 degrees around some axis).
> 返回 Rotation1 与 Rotation2 之间的距离：0.0 表示等价旋转，1.0 表示相对（相反）旋转。

`using { /Verse.org/SpatialMath }`

```verse
Distance<public><native>(Rotation1:rotation, Rotation2:rotation):float
```

## Parameters

Distance 接受以下参数：
| Name | Type | Description |
| Rotation1 | rotation |  |
| Rotation2 | rotation |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
