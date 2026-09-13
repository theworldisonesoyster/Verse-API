---
name: MakeSuccess
slug: versedotorg/verse/makesuccess
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/makesuccess
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# MakeSuccess function <A>

构造一个表示成功的 result 实例。

`using { /Verse.org/Verse }`

```verse
MakeSuccess<public>(Result:success_type where success_type:any):result(success_type,error_type)
```

## Parameters

MakeSuccess 接受以下参数：
| Name | Type | Description |
| Result | success_type |  |
| success_type | any |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
OK:result[string, string] = MakeSuccess("done")
```
