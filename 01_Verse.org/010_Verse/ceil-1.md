---
name: Ceil
slug: versedotorg/verse/ceil-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/ceil-1
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Ceil function <A>

> Returns the smallest int that is greater than or equal to Val. Fails if not IsFinite(Val).
> 返回大于等于 Val 的最小 int（向上取整，float 输入版本）。非有限值时失败。

`using { /Verse.org/Verse }`

```verse
Ceil<public><native>(Val:float):int
```

## Parameters

Ceil 接受以下参数：
| Name | Type | Description |
| Val | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
N := Ceil(1.2)   # 2
```
