---
name: Max
slug: versedotorg/verse/max
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/max
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Max function <A>

> Returns the maximum of X and Y.
> 返回 X 和 Y 中的较大值（int 版本）。

`using { /Verse.org/Verse }`

```verse
Max<public>(X:int, Y:int):int
```

## Parameters

Max 接受以下参数：
| Name | Type | Description |
| X | int |  |
| Y | int |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
N := Max(3, 7)   # 7
```
