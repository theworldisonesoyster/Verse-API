---
name: MakeColorFromSRGB
slug: versedotorg/colors/makecolorfromsrgb
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makecolorfromsrgb
kind: function
module: /Verse.org/colors
grade: A
depth: full
status: done
---

# MakeColorFromSRGB function <A>

> Makes an ACES 2065-1 color from sRGB components Red, Green, and Blue. Normal sRGB component values are between 0.0 and 1.0, but this can handle larger values.
> 从 sRGB 分量 Red/Green/Blue 构造 ACES 2065-1 颜色。正常取值 0.0~1.0，也可接受更大的值。

`using { /Verse.org/Colors }`

```verse
MakeColorFromSRGB<public><native>(Red:float, Green:float, Blue:float):color
```

## Parameters

MakeColorFromSRGB 接受以下参数：
| Name | Type | Description |
| Red | float |  |
| Green | float |  |
| Blue | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
