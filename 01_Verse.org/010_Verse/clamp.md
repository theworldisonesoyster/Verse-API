---
name: Clamp
slug: versedotorg/verse/clamp
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/clamp
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Clamp function <A>

> Constrains the value of Val between A and B. Robustly handles different argument orderings. Returns the median of Val, A, and B, such that comparisons with NaN operate as if NaN > +Inf.
> 把 Val 限制在 A 与 B 之间（int 版本；健壮处理 A、B 顺序）。

`using { /Verse.org/Verse }`

```verse
Clamp<public>(Val:float, A:float, B:float):float
```

## Parameters

Clamp 接受以下参数：
| Name | Type | Description |
| Val | float |  |
| A | float |  |
| B | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
N := Clamp(V, 0, 10)
```
