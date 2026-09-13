---
name: Min
slug: versedotorg/verse/min
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/min
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Min function <A>

> Returns the minimum of X and Y.
> 返回 X 和 Y 中的较小值（int 版本）。

`using { /Verse.org/Verse }`

```verse
Min<public>(X:int, Y:int):int
```

## Parameters

Min 接受以下参数：
| Name | Type | Description |
| X | int |  |
| Y | int |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
N := Min(3, 7)   # 3
```
