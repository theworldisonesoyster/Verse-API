---
name: operator'?'
slug: versedotorg/verse/operatorquestionmark
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/operatorquestionmark
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# operator'?' function <A>

logic 查询：Value 为 true 则成功，为 false 则失败——logic 接入失败上下文的标准写法。

`using { /Verse.org/Verse }`

```verse
operator'?'(Value:logic)<decides>:logic
```

## Parameters

operator'?' 接受以下参数：
| Name | Type | Description |
| Value | logic |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
Ready:logic = true
if (Ready?):
    Print("go")
```
