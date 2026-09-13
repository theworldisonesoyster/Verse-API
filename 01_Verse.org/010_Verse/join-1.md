---
name: Join
slug: versedotorg/verse/join-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/join-1
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Join function <A>

> Makes a string by concatenating Separator between the elements of Strings.
> 用 Separator 把 Element 数组拼接成一个字符串。

`using { /Verse.org/Verse }`

```verse
Join<public><native>(Strings:[][]char, Separator:[]char):[]char
```

## Parameters

Join 接受以下参数：
| Name | Type | Description |
| Strings | [][]char |  |
| Separator | []char |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
S := Join(array{"a", "b", "c"}, "-")   # a-b-c
```
