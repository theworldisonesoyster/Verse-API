---
name: color_alpha
slug: versedotorg/colors/color_alpha
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/color_alpha
kind: class
module: /Verse.org/colors
grade: A
depth: full
status: done
---

# color_alpha struct <A>

> Represents colors as RGB triples in the ACES 2065-1 color space with an additional alpha channel A. This reasons about the Color and alpha (A) as separate concepts instead of as a single concept. All values are stored strictly as unopinionated floats but, when interpreted as a color with alpha, ranges for A are 0.0 (transparent) to 1.0 (opaque). Color values are not premultiplied. Component values are linear (i.e. *gamma* = 1.0).
> ACES 2065-1 的 RGB 颜色＋附加 Alpha 通道；Color 与 Alpha (A) 各自独立处理。

`using { /Verse.org/Colors }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| [Color](color_alpha_color.md) | color | 此 color_alpha 的颜色（Color）分量。 |
| [A](color_alpha_a.md) | float | 此 color_alpha 的透明度（Alpha）分量。 |
