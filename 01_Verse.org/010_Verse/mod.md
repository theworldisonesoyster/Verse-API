---
name: Mod
slug: versedotorg/verse/mod
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/mod
kind: function
module: /Verse.org/verse
grade: B
depth: brief
status: done
---

# Mod function <B>

> Returns the remainder of X/Y as defined by Euclidean division, i.e.:
> - Mod[X,Y] = X - Quotient(X/Y)*Y
> - 0 <= Mod[X,Y] < Abs(Y) Fails if Y=0.
> 返回欧几里得除法 X/Y 的余数。

`using { /Verse.org/Verse }`

```verse
Mod<public><native>(X:int, Y:int):int
```

## Parameters

Mod 接受以下参数：
| Name | Type | Description |
| X | int |  |
| Y | int |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
