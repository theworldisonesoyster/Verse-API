---
name: CrossProduct
slug: versedotorg/spatialmath/crossproduct
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/crossproduct
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

# CrossProduct function <A>

> Returns the right-handed cross product of V1 and V2.
> 返回 V1 与 V2 的右手叉积。

`using { /Verse.org/SpatialMath }`

```verse
CrossProduct<public>(V1:vector3, V2:vector3):vector3
```

## Parameters

CrossProduct 接受以下参数：
| Name | Type | Description |
| V1 | vector3 |  |
| V2 | vector3 |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
N := CrossProduct(Up, Forward)
```
