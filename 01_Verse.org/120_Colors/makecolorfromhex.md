---
name: MakeColorFromHex
slug: versedotorg/colors/makecolorfromhex
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makecolorfromhex
kind: function
module: /Verse.org/colors
grade: A
depth: full
status: done
---

# MakeColorFromHex function <A>

> Makes an ACES 2065-1 color from a CSS-style sRGB hexString. Supported formats are:
> - RGB
> - RRGGBB
> - RRGGBBAA
> - RGB
> - RRGGBB
> - RRGGBBAA An invalid hex string will return Black.
> 从 CSS 风格的 sRGB 十六进制字符串构造 ACES 2065-1 颜色。支持 RGB / RRGGBB / RRGGBBAA 格式；无效字符串会失败。

`using { /Verse.org/Colors }`

```verse
MakeColorFromHex<public><native>(hexString:[]char):color
```

## Parameters

MakeColorFromHex 接受以下参数：
| Name | Type | Description |
| hexString | []char |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
C := MakeColorFromHex("#FF8800")
```
