---
name: Parse
slug: unrealenginedotcom/json/parse
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/json/parse
kind: function
module: /Verse.org/json
grade: A
depth: full
status: done
---

# Parse function <A>

> Parse a JSON string returning a value with its contents
> 解析 JSON 字符串，返回包含其内容的 value。

`using { /UnrealEngine.com/JSON }`

```verse
Parse<public><native>(JSONString:[]char)<transacts><decides>:value
```

## Parameters

Parse 接受以下参数：
| Name | Type | Description |
| JSONString | []char |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
if (V := Parse("{\"a\":1}")):\n    Print("解析成功")
```
