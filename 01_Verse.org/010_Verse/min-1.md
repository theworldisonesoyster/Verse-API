---
name: Min
slug: versedotorg/verse/min-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/min-1
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Min function <A>

> Returns the minimum of X and Y unless either are NaN. Returns NaN if either X or Y are NaN.
> 返回 X 和 Y 中的较小值；任一为 NaN 时返回 NaN（float 版本）。

`using { /Verse.org/Verse }`

```verse
Min<public>(X:float, Y:float):float
```

## Parameters

Min 接受以下参数：
| Name | Type | Description |
| X | float |  |
| Y | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
F := Min(0.5, 1.5)   # 0.5
```
