---
name: color
slug: versedotorg/colors/color
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/color
kind: class
module: /Verse.org/colors
grade: A
depth: full
status: done
---

# color struct <A>

> Represents colors as RGB triples in the ACES 2065-1 color space. Component values are linear (i.e. *gamma* = 1.0).
> 以 ACES 2065-1 色彩空间的 RGB 三元组表示颜色；分量值为线性（gamma = 1.0）。

`using { /Verse.org/Colors }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| [R](color_r.md) | float | 此颜色的红色（Red）分量。 |
| [G](color_g.md) | float | 此颜色的绿色（Green）分量。 |
| [B](color_b.md) | float | 此颜色的蓝色（Blue）分量。 |

## 示例

```verse
C := MakeColorFromHex("#422439")
```
