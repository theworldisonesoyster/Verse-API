---
name: Over
slug: versedotorg/colors/over
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/over
kind: function
module: /Verse.org/colors
grade: B
depth: brief
status: done
---

# Over function <B>

> Blend colors CA1 and CA2 with CA1 over CA2 using two non-premultiplied color_alpha values. Alpha components are clamped between 0.0 and 1.0. Fails if the value of both clamped Alpha components are 0.0.
> 以「CA1 置于 CA2 之上」混合两个非预乘 color_alpha；alpha 分量钳制在 0.0~1.0。

`using { /Verse.org/Colors }`

```verse
Over<public>(CA1:color_alpha, CA2:color_alpha):color_alpha
```

## Parameters

Over 接受以下参数：
| Name | Type | Description |
| CA1 | color_alpha |  |
| CA2 | color_alpha |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
