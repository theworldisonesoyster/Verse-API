---
name: Join
slug: versedotorg/verse/join
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/join
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Join function <A>

> Makes a message by concatenating Separator between the elements of Messages.
> 用 Separator 把 Element 数组拼接成一个 message（可本地化文本）。

`using { /Verse.org/Verse }`

```verse
Join<public><native>(Messages:[]message, Separator:message)<transacts>:message
```

## Parameters

Join 接受以下参数：
| Name | Type | Description |
| Messages | []message |  |
| Separator | message |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
M := Join(array{"a", "b"}, "-")   # a-b
```
