---
name: MakeHSVFromColor
slug: versedotorg/colors/makehsvfromcolor
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makehsvfromcolor
kind: function
module: /Verse.org/colors
grade: A
depth: full
status: done
---

# MakeHSVFromColor function <A>

> Makes an HSV tuple by converting InColor from an ACES 2065-1 color to sRGB and applying the HSV color model.
> 把 InColor 从 ACES 2065-1 转为 sRGB，再以 HSV 模型返回元组。

`using { /Verse.org/Colors }`

```verse
MakeHSVFromColor<public><native>(InColor:color)<transacts><no_rollback>:(float, float, float)
```

## Parameters

MakeHSVFromColor 接受以下参数：
| Name | Type | Description |
| InColor | color |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
