---
name: Floor
slug: versedotorg/verse/floor-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/floor-1
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Floor function <A>

> Returns the largest int that is less than or equal to Val. Fails if not IsFinite(Val).
> 返回小于等于 Val 的最大 int（向下取整，float 输入版本）。非有限值时失败。

`using { /Verse.org/Verse }`

```verse
Floor<public><native>(Val:float):int
```

## Parameters

Floor 接受以下参数：
| Name | Type | Description |
| Val | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
N := Floor(1.8)   # 1
```
