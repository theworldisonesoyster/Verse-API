---
name: MakeColorFromTemperature
slug: versedotorg/colors/makecolorfromtemperature
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makecolorfromtemperature
kind: function
module: /Verse.org/colors
grade: B
depth: brief
status: done
---

# MakeColorFromTemperature function <B>

> Makes an ACES 2065-1 color from the chromaticity of a blackbody radiator at Temperature Kelvin. Temperature is clamped such that 0 <= Temperature.
> 从开尔文温度下黑体辐射的色度构造 ACES 2065-1 颜色；温度会被钳制为 ≥0。

`using { /Verse.org/Colors }`

```verse
MakeColorFromTemperature<public><native>(Temperature:float):color
```

## Parameters

MakeColorFromTemperature 接受以下参数：
| Name | Type | Description |
| Temperature | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
