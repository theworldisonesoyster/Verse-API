---
name: Floor
slug: versedotorg/verse/floor
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/floor
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Floor function <A>

返回小于等于 Val 的最大 int（向下取整，rational 输入版本）。

`using { /Verse.org/Verse }`

```verse
Floor(Value:rational):int
```

## Parameters

Floor 接受以下参数：
| Name | Type | Description |
| Value | rational |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
N := Floor(3.0)   # 3
```
