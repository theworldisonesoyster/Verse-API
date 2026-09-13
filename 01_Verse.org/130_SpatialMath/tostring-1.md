---
name: ToString
slug: versedotorg/spatialmath/tostring-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/tostring-1
kind: function
module: /Verse.org/spatialmath
grade: B
depth: brief
status: done
---

# ToString function <B>

> Makes a string representation of InTransform where the result is on the form. "{Translation = {ToString(InTransform.Translation)}, Rotation = {ToString(InTransform.Rotation)}, Scale = {ToString(InTransform.Scale`)}}".
> 返回 InTransform 的字符串表示（Translation/Rotation/Scale 形式）。

`using { /Verse.org/SpatialMath }`

```verse
ToString<public>(InTransform:transform):[]char
```

## Parameters

ToString 接受以下参数：
| Name | Type | Description |
| InTransform | transform |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
