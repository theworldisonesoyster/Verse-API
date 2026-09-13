---
name: MakeError
slug: versedotorg/verse/makeerror
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/makeerror
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# MakeError function <A>

构造一个携带错误信息的失败 result 实例。

`using { /Verse.org/Verse }`

```verse
MakeError<public>(Result:error_type where error_type:any):result(success_type,error_type)
```

## Parameters

MakeError 接受以下参数：
| Name | Type | Description |
| Result | error_type |  |
| error_type | any |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
Bad:result[string, string] = MakeError("oops")
```
