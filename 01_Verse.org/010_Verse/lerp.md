---
name: Lerp
slug: versedotorg/verse/lerp
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/lerp
kind: function
module: /Verse.org/verse
grade: B
depth: brief
status: done
---

# Lerp function <B>

> Used to linearly interpolate/extrapolate between From (when Parameter = 0.0) and To (when Parameter = 1.0). Expects that all arguments are finite. Returns From*(1 - Parameter) + To*Parameter.
> 在 From（t=0）与 To（t=1）之间线性插值/外推。

`using { /Verse.org/Verse }`

```verse
Lerp<public><native>(From:float, To:float, Parameter:float):float
```

## Parameters

Lerp 接受以下参数：
| Name | Type | Description |
| From | float |  |
| To | float |  |
| Parameter | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
