---
name: Quotient
slug: versedotorg/verse/quotient
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/quotient
kind: function
module: /Verse.org/verse
grade: B
depth: brief
status: done
---

# Quotient function <B>

> Returns the quotient X/Y as defined by Euclidean division, i.e.:
> - Quotient[X/Y] = Floor[X/Y] when Y > 0
> - Quotient[X/Y] = Ceil[X/Y] when Y < 0
> - Quotient[X/Y] * Y + Mod[X,Y] = X Fails if Y = 0.
> 返回欧几里得除法 X/Y 的商。

`using { /Verse.org/Verse }`

```verse
Quotient<public><native>(X:int, Y:int):int
```

## Parameters

Quotient 接受以下参数：
| Name | Type | Description |
| X | int |  |
| Y | int |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
