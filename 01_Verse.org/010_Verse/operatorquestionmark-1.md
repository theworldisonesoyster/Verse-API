---
name: operator'?'
slug: versedotorg/verse/operatorquestionmark-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/operatorquestionmark-1
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# operator'?' function <A>

option 取值：Value 有值则成功并返回该值，为空则失败。

`using { /Verse.org/Verse }`

```verse
operator'?'(Value:?t where t:any)<decides>:t
```

## Parameters

operator'?' 接受以下参数：
| Name | Type | Description |
| Value | ?t |  |
| t | any |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
Opt:?int = option{7}
if (V := Opt?):
    Print("{V}")
```
