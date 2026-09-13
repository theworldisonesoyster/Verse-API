---
name: operator'*'
slug: versedotorg/spatialmath/operatorstar-2
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/operatorstar-2
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

# operator'*' function <A>

> Makes a vector3 by applying InTransform to InVector.
> 用 InTransform（缩放＋旋转＋平移）变换 InVector。

`using { /Verse.org/SpatialMath }`

```verse
operator'*'<public>(InVector:vector3, InTransform:transform):vector3
```

## Parameters

operator'*' 接受以下参数：
| Name | Type | Description |
| InVector | vector3 |  |
| InTransform | transform |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
V2 := vector3{Forward:=1.0} * MyTransform
```
