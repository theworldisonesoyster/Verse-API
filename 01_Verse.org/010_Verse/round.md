---
name: Round
slug: versedotorg/verse/round
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/round
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Round function <A>

> Returns Val rounded to the nearest int. When the fractional part of Val is 0.5, rounds to the nearest even int (per the IEEE-754 default rounding mode). Fails if not IsFinite(Val).
> 返回 Val 四舍五入到最近整数的 int；小数部分恰为 0.5 时取最近的偶数（IEEE-754 默认舍入）。非有限值时失败。

`using { /Verse.org/Verse }`

```verse
Round<public><native>(Val:float):int
```

## Parameters

Round 接受以下参数：
| Name | Type | Description |
| Val | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
N := Round(1.5)   # 2（取偶）
```
