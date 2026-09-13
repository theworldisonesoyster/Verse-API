---
name: MakeColorFromHSV
slug: versedotorg/colors/makecolorfromhsv
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makecolorfromhsv
kind: function
module: /Verse.org/colors
grade: A
depth: full
status: done
---

# MakeColorFromHSV function <A>

> Makes an ACES 2065-1 color from Hue, Saturation, and Value components. Components use the HSV color model in the sRGB color space. Expected ranges:
> - 0.0 <= Hue <= 360.0
> - 0.0 <= Saturation <= 1.0
> - 0.0 <= Value <= 1.0 Values out of expected ranges will undergo range reduction and conversion.
> 从色相/饱和度/明度（HSV，sRGB 空间模型）构造 ACES 2065-1 颜色。

`using { /Verse.org/Colors }`

```verse
MakeColorFromHSV<public><native>(Hue:float, Saturation:float, Value:float):color
```

## Parameters

MakeColorFromHSV 接受以下参数：
| Name | Type | Description |
| Hue | float |  |
| Saturation | float |  |
| Value | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
