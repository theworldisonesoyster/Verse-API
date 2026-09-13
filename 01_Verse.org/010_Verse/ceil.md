---
name: Ceil
slug: versedotorg/verse/ceil
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/ceil
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Ceil function <A>

返回大于等于 Val 的最小 int（向上取整，rational 输入版本）。

`using { /Verse.org/Verse }`

```verse
Ceil(Value:rational):int
```

## Parameters

Ceil 接受以下参数：
| Name | Type | Description |
| Value | rational |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
N := Ceil(3.0)   # 3
```
