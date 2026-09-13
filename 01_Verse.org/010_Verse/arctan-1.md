---
name: ArcTan
slug: versedotorg/verse/arctan-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/arctan-1
kind: function
module: /Verse.org/verse
grade: B
depth: brief
status: done
---

# ArcTan function <B>

> Returns the angle in radians at the origin between a ray pointing to (X, Y) and the positive X axis such that -PiFloat < ArcTan(Y, X) <= PiFloat. Returns 0.0 if X=0.0 and Y=0.0.
> 返回原点到点 (X, Y) 连线与 X 轴的夹角（弧度）。

`using { /Verse.org/Verse }`

```verse
ArcTan<public><native>(Y:float, X:float):float
```

## Parameters

ArcTan 接受以下参数：
| Name | Type | Description |
| Y | float |  |
| X | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
