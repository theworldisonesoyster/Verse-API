---
name: DotProduct
slug: versedotorg/spatialmath/dotproduct
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/dotproduct
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

# DotProduct function <A>

> Returns the dot product of V1 and V2.
> 返回 V1 与 V2 的点积。

`using { /Verse.org/SpatialMath }`

```verse
DotProduct<public>(V1:vector3, V2:vector3):float
```

## Parameters

DotProduct 接受以下参数：
| Name | Type | Description |
| V1 | vector3 |  |
| V2 | vector3 |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
D := DotProduct(vector3{Forward:=1.0}, vector3{Forward:=2.0})   # 2.0
```
