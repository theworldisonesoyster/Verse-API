---
name: Int
slug: versedotorg/verse/int
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/int
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Int function <A>

> Returns the int that equals Val without the fractional part. Fails if not IsFinite(val).
> 返回等于 Val 去掉小数部分的 int（向零取整）。

`using { /Verse.org/Verse }`

```verse
Int<public><native>(Val:float):int
```

## Parameters

Int 接受以下参数：
| Name | Type | Description |
| Val | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
N := Int(2.9)   # 2
```
