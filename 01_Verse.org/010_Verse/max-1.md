---
name: Max
slug: versedotorg/verse/max-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/max-1
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Max function <A>

> Returns the maximum of X and Y unless either are NaN. Returns NaN if either X or Y are NaN.
> 返回 X 和 Y 中的较大值；任一为 NaN 时返回 NaN（float 版本）。

`using { /Verse.org/Verse }`

```verse
Max<public>(X:float, Y:float):float
```

## Parameters

Max 接受以下参数：
| Name | Type | Description |
| X | float |  |
| Y | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
F := Max(0.5, 1.5)   # 1.5
```
