---
name: MakeColorFromSRGBValues
slug: versedotorg/colors/makecolorfromsrgbvalues
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makecolorfromsrgbvalues
kind: function
module: /Verse.org/colors
grade: A
depth: full
status: done
---

# MakeColorFromSRGBValues function <A>

> Makes an ACES 2065-1 color from the integer sRGB components Red, Green, and Blue. Valid sRGB component values are between '0' and '255', inclusive.
> 从整数 sRGB 分量 Red/Green/Blue（0~255）构造 ACES 2065-1 颜色。

`using { /Verse.org/Colors }`

```verse
MakeColorFromSRGBValues<public><native>(Red:int, Green:int, Blue:int):color
```

## Parameters

MakeColorFromSRGBValues 接受以下参数：
| Name | Type | Description |
| Red | int |  |
| Green | int |  |
| Blue | int |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
