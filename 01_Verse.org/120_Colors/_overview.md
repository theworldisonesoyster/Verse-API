---
name: Colors module
slug: versedotorg/colors
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors
kind: module
module: /versedotorg
grade: A
depth: brief
status: done
---

# Colors module <A>

颜色系统：以 ACES 2065-1 色彩空间的 RGB 表示颜色，提供 sRGB/十六进制/HSV/色温等构造方式与 NamedColors 预设常量。

## Classes and Structs

| Name | Description |
|---|---|
| [color](color.md) | 以 ACES 2065-1 色彩空间的 RGB 三元组表示颜色；分量值为线性（gamma = 1.0）。 |
| [color_alpha](color_alpha.md) | ACES 2065-1 的 RGB 颜色＋附加 Alpha 通道；Color 与 Alpha (A) 各自独立处理。 |

## Functions

| Name | Description |
|---|---|
| [operator'+'](operatorplus.md) | c0 与 c1 逐分量相加，得到新的 ACES 2065-1 颜色。 |
| [operator'-'](operatorminus.md) | c0 与 c1 逐分量相减，得到新的 ACES 2065-1 颜色。 |
| [operator'*'](operatorstar.md) | c0 与 c1 逐分量相乘，得到新的 ACES 2065-1 颜色。 |
| [operator'*'](operatorstar-1.md) | c 的各分量乘以 factor，得到新颜色。 |
| [operator'*'](operatorstar-2.md) | c 的各分量乘以 factor，得到新颜色。 |
| [operator'*'](operatorstar-3.md) | c 的各分量乘以 factor，得到新颜色。 |
| [operator'*'](operatorstar-4.md) | c 的各分量乘以 factor，得到新颜色。 |
| [operator'/'](operatorslash.md) | c 的各分量除以 factor，得到新颜色。 |
| [operator'/'](operatorslash-1.md) | c 的各分量除以 factor，得到新颜色。 |
| [MakeColorFromSRGB](makecolorfromsrgb.md) | 从 sRGB 分量 Red/Green/Blue 构造 ACES 2065-1 颜色。正常取值 0.0~1.0，也可接受更大的值。 |
| [MakeSRGBFromColor](makesrgbfromcolor.md) | 把 InColor 从 ACES 2065-1 转换为 sRGB 元组。 |
| [MakeColorFromSRGBValues](makecolorfromsrgbvalues.md) | 从整数 sRGB 分量 Red/Green/Blue（0~255）构造 ACES 2065-1 颜色。 |
| [MakeColorFromHex](makecolorfromhex.md) | 从 CSS 风格的 sRGB 十六进制字符串构造 ACES 2065-1 颜色。支持 RGB / RRGGBB / RRGGBBAA 格式；无效字符串会失败。 |
| [MakeColorFromHSV](makecolorfromhsv.md) | 从色相/饱和度/明度（HSV，sRGB 空间模型）构造 ACES 2065-1 颜色。 |
| [MakeHSVFromColor](makehsvfromcolor.md) | 把 InColor 从 ACES 2065-1 转为 sRGB，再以 HSV 模型返回元组。 |
| [MakeColorFromTemperature](makecolorfromtemperature.md) | 从开尔文温度下黑体辐射的色度构造 ACES 2065-1 颜色；温度会被钳制为 ≥0。 |
| [MakeColorAlpha](makecoloralpha.md) | 由 R/G/B/A 各分量构造新的 color_alpha。 |
| [Over](over.md) | 以「CA1 置于 CA2 之上」混合两个非预乘 color_alpha；alpha 分量钳制在 0.0~1.0。 |

| AliceBlue 〔无独立页面〕 | 预设颜色常量。 |
| AntiqueWhite 〔无独立页面〕 | 预设颜色常量。 |
| Aqua 〔无独立页面〕 | 预设颜色常量。 |
| Aquamarine 〔无独立页面〕 | 预设颜色常量。 |
| Azure 〔无独立页面〕 | 预设颜色常量。 |
| Beige 〔无独立页面〕 | 预设颜色常量。 |
| Bisque 〔无独立页面〕 | 预设颜色常量。 |
| Black 〔无独立页面〕 | 预设颜色常量。 |
| BlanchedAlmond 〔无独立页面〕 | 预设颜色常量。 |
| Blue 〔无独立页面〕 | 预设颜色常量。 |
| BlueViolet 〔无独立页面〕 | 预设颜色常量。 |
| Brown 〔无独立页面〕 | 预设颜色常量。 |
| Burlywood 〔无独立页面〕 | 预设颜色常量。 |
| CadetBlue 〔无独立页面〕 | 预设颜色常量。 |
| Chartreuse 〔无独立页面〕 | 预设颜色常量。 |
| Chocolate 〔无独立页面〕 | 预设颜色常量。 |
| Coral 〔无独立页面〕 | 预设颜色常量。 |
| CornflowerBlue 〔无独立页面〕 | 预设颜色常量。 |
| Cornsilk 〔无独立页面〕 | 预设颜色常量。 |
| Crimson 〔无独立页面〕 | 预设颜色常量。 |
| Cyan 〔无独立页面〕 | 预设颜色常量。 |
| DarkBlue 〔无独立页面〕 | 预设颜色常量。 |
| DarkCyan 〔无独立页面〕 | 预设颜色常量。 |
| DarkGoldenrod 〔无独立页面〕 | 预设颜色常量。 |
| DarkGray 〔无独立页面〕 | 预设颜色常量。 |
| DarkGreen 〔无独立页面〕 | 预设颜色常量。 |
| DarkGrey 〔无独立页面〕 | 预设颜色常量。 |
| DarkKhaki 〔无独立页面〕 | 预设颜色常量。 |
| DarkMagenta 〔无独立页面〕 | 预设颜色常量。 |
| DarkOliveGreen 〔无独立页面〕 | 预设颜色常量。 |
| DarkOrange 〔无独立页面〕 | 预设颜色常量。 |
| DarkOrchid 〔无独立页面〕 | 预设颜色常量。 |
| DarkRed 〔无独立页面〕 | 预设颜色常量。 |
| DarkSalmon 〔无独立页面〕 | 预设颜色常量。 |
| DarkSeaGreen 〔无独立页面〕 | 预设颜色常量。 |
| DarkSlateBlue 〔无独立页面〕 | 预设颜色常量。 |
| DarkSlateGray 〔无独立页面〕 | 预设颜色常量。 |
| DarkSlateGrey 〔无独立页面〕 | 预设颜色常量。 |
| DarkTurquoise 〔无独立页面〕 | 预设颜色常量。 |
| DarkViolet 〔无独立页面〕 | 预设颜色常量。 |
| DeepPink 〔无独立页面〕 | 预设颜色常量。 |
| DeepSkyBlue 〔无独立页面〕 | 预设颜色常量。 |
| DimGray 〔无独立页面〕 | 预设颜色常量。 |
| DimGrey 〔无独立页面〕 | 预设颜色常量。 |
| DodgerBlue 〔无独立页面〕 | 预设颜色常量。 |
| Firebrick 〔无独立页面〕 | 预设颜色常量。 |
| FloralWhite 〔无独立页面〕 | 预设颜色常量。 |
| ForestGreen 〔无独立页面〕 | 预设颜色常量。 |
| Fuchsia 〔无独立页面〕 | 预设颜色常量。 |
| Gainsboro 〔无独立页面〕 | 预设颜色常量。 |
| GhostWhite 〔无独立页面〕 | 预设颜色常量。 |
| Gold 〔无独立页面〕 | 预设颜色常量。 |
| Goldenrod 〔无独立页面〕 | 预设颜色常量。 |
| Gray 〔无独立页面〕 | 预设颜色常量。 |
| Green 〔无独立页面〕 | 预设颜色常量。 |
| GreenYellow 〔无独立页面〕 | 预设颜色常量。 |
| Grey 〔无独立页面〕 | 预设颜色常量。 |
| Honeydew 〔无独立页面〕 | 预设颜色常量。 |
| Hotpink 〔无独立页面〕 | 预设颜色常量。 |
| IndianRed 〔无独立页面〕 | 预设颜色常量。 |
| Indigo 〔无独立页面〕 | 预设颜色常量。 |
| Ivory 〔无独立页面〕 | 预设颜色常量。 |
| Khaki 〔无独立页面〕 | 预设颜色常量。 |
| Lavender 〔无独立页面〕 | 预设颜色常量。 |
| LavenderBlush 〔无独立页面〕 | 预设颜色常量。 |
| LawnGreen 〔无独立页面〕 | 预设颜色常量。 |
| LemonChiffon 〔无独立页面〕 | 预设颜色常量。 |
| LightBlue 〔无独立页面〕 | 预设颜色常量。 |
| LightCoral 〔无独立页面〕 | 预设颜色常量。 |
| LightCyan 〔无独立页面〕 | 预设颜色常量。 |
| LightGoldenrodYellow 〔无独立页面〕 | 预设颜色常量。 |
| LightGray 〔无独立页面〕 | 预设颜色常量。 |
| LightGreen 〔无独立页面〕 | 预设颜色常量。 |
| LightGrey 〔无独立页面〕 | 预设颜色常量。 |
| LightPink 〔无独立页面〕 | 预设颜色常量。 |
| LightSalmon 〔无独立页面〕 | 预设颜色常量。 |
| LightSeaGreen 〔无独立页面〕 | 预设颜色常量。 |
| LightSkyBlue 〔无独立页面〕 | 预设颜色常量。 |
| LightSlateGray 〔无独立页面〕 | 预设颜色常量。 |
| LightSlateGrey 〔无独立页面〕 | 预设颜色常量。 |
| LightSteelBlue 〔无独立页面〕 | 预设颜色常量。 |
| LightYellow 〔无独立页面〕 | 预设颜色常量。 |
| Lime 〔无独立页面〕 | 预设颜色常量。 |
| LimeGreen 〔无独立页面〕 | 预设颜色常量。 |
| Linen 〔无独立页面〕 | 预设颜色常量。 |
| Magenta 〔无独立页面〕 | 预设颜色常量。 |
| Maroon 〔无独立页面〕 | 预设颜色常量。 |
| MediumAquamarine 〔无独立页面〕 | 预设颜色常量。 |
| MediumBlue 〔无独立页面〕 | 预设颜色常量。 |
| MediumOrchid 〔无独立页面〕 | 预设颜色常量。 |
| MediumPurple 〔无独立页面〕 | 预设颜色常量。 |
| MediumSeaGreen 〔无独立页面〕 | 预设颜色常量。 |
| MediumSlateBlue 〔无独立页面〕 | 预设颜色常量。 |
| MediumSpringGreen 〔无独立页面〕 | 预设颜色常量。 |
| MediumTurquoise 〔无独立页面〕 | 预设颜色常量。 |
| MediumVioletRed 〔无独立页面〕 | 预设颜色常量。 |
| MidnightBlue 〔无独立页面〕 | 预设颜色常量。 |
| MintCream 〔无独立页面〕 | 预设颜色常量。 |
| MistyRose 〔无独立页面〕 | 预设颜色常量。 |
| Moccasin 〔无独立页面〕 | 预设颜色常量。 |
| NavajoWhite 〔无独立页面〕 | 预设颜色常量。 |
| Navy 〔无独立页面〕 | 预设颜色常量。 |
| OldLace 〔无独立页面〕 | 预设颜色常量。 |
| Olive 〔无独立页面〕 | 预设颜色常量。 |
| OliveDrab 〔无独立页面〕 | 预设颜色常量。 |
| Orange 〔无独立页面〕 | 预设颜色常量。 |
| OrangeRed 〔无独立页面〕 | 预设颜色常量。 |
| Orchid 〔无独立页面〕 | 预设颜色常量。 |
| PaleGoldenrod 〔无独立页面〕 | 预设颜色常量。 |
| PaleGreen 〔无独立页面〕 | 预设颜色常量。 |
| PaleTurquoise 〔无独立页面〕 | 预设颜色常量。 |
| PaleVioletred 〔无独立页面〕 | 预设颜色常量。 |
| PapayaWhip 〔无独立页面〕 | 预设颜色常量。 |
| PeachPuff 〔无独立页面〕 | 预设颜色常量。 |
| Peru 〔无独立页面〕 | 预设颜色常量。 |
| Pink 〔无独立页面〕 | 预设颜色常量。 |
| Plum 〔无独立页面〕 | 预设颜色常量。 |
| PowderBlue 〔无独立页面〕 | 预设颜色常量。 |
| Purple 〔无独立页面〕 | 预设颜色常量。 |
| Red 〔无独立页面〕 | 预设颜色常量。 |
| RosyBrown 〔无独立页面〕 | 预设颜色常量。 |
| RoyalBlue 〔无独立页面〕 | 预设颜色常量。 |
| SaddleBrown 〔无独立页面〕 | 预设颜色常量。 |
| Salmon 〔无独立页面〕 | 预设颜色常量。 |
| SandyBrown 〔无独立页面〕 | 预设颜色常量。 |
| SeaGreen 〔无独立页面〕 | 预设颜色常量。 |
| SeaShell 〔无独立页面〕 | 预设颜色常量。 |
| Sienna 〔无独立页面〕 | 预设颜色常量。 |
| Silver 〔无独立页面〕 | 预设颜色常量。 |
| SkyBlue 〔无独立页面〕 | 预设颜色常量。 |
| SlateBlue 〔无独立页面〕 | 预设颜色常量。 |
| SlateGray 〔无独立页面〕 | 预设颜色常量。 |
| SlateGrey 〔无独立页面〕 | 预设颜色常量。 |
| Snow 〔无独立页面〕 | 预设颜色常量。 |
| SpringGreen 〔无独立页面〕 | 预设颜色常量。 |
| SteelBlue 〔无独立页面〕 | 预设颜色常量。 |
| Tan 〔无独立页面〕 | 预设颜色常量。 |
| Teal 〔无独立页面〕 | 预设颜色常量。 |
| Thistle 〔无独立页面〕 | 预设颜色常量。 |
| Tomato 〔无独立页面〕 | 预设颜色常量。 |
| Turquoise 〔无独立页面〕 | 预设颜色常量。 |
| Violet 〔无独立页面〕 | 预设颜色常量。 |
| Wheat 〔无独立页面〕 | 预设颜色常量。 |
| White 〔无独立页面〕 | 预设颜色常量。 |
| WhiteSmoke 〔无独立页面〕 | 预设颜色常量。 |
| Yellow 〔无独立页面〕 | 预设颜色常量。 |
| YellowGreen 〔无独立页面〕 | 预设颜色常量。 |
