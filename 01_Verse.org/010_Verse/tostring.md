---
name: ToString
slug: versedotorg/verse/tostring
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/tostring
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# ToString function <A>

> Makes a string representation of Val.
> 把 Val（float）转成字符串表示。

`using { /Verse.org/Verse }`

```verse
ToString<public><native>(Val:float):[]char
```

## Parameters

ToString 接受以下参数：
| Name | Type | Description |
| Val | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
S := ToString(3.14)
```
