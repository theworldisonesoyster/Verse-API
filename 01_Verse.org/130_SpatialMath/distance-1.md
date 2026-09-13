---
name: Distance
slug: versedotorg/spatialmath/distance-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/distance-1
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

# Distance function <A>

> Returns the Euclidean distance between V1 and V2.
> 返回 V1 与 V2 的欧氏距离。

`using { /Verse.org/SpatialMath }`

```verse
Distance<public>(V1:vector3, V2:vector3):float
```

## Parameters

Distance 接受以下参数：
| Name | Type | Description |
| V1 | vector3 |  |
| V2 | vector3 |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
D := Distance(A, B)
```
