---
name: ToString
slug: versedotorg/spatialmath/tostring
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/tostring
kind: function
module: /Verse.org/spatialmath
grade: B
depth: brief
status: done
---

# ToString function <B>

> Makes a string representation of rotation in axis/degrees format with a right-handed sign convention. ToString(MakeRotationRadians(vector3{Left:=0.0, Up:=0.0, Forward:=1.0}, PiFloat/2.0)) produces the string: "{Axis = {Left=0.000000, Up=0.000000, Forward=1.000000}, Angle = 90.000000}".
> 以轴/角度格式（右手系）返回旋转的字符串表示。

`using { /Verse.org/SpatialMath }`

```verse
ToString<public>(Rotation:rotation):[]char
```

## Parameters

ToString 接受以下参数：
| Name | Type | Description |
| Rotation | rotation |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
