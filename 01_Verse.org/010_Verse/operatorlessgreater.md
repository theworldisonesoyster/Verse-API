---
name: operator'<>'
slug: versedotorg/verse/operatorlessgreater
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/operatorlessgreater
kind: function
module: /Verse.org/verse
grade: S
depth: full
status: done
---

# operator'<>' function <S>

不相等比较：Lhs 与 Rhs 不相等则成功，相等则失败。与 [operator'=](operatorequals.md) 语义相反。

`using { /Verse.org/Verse }`

```verse
operator'<>'(Lhs:t, Rhs:comparable where t:comparable)<decides>:t
```

## Parameters

operator'<>' 接受以下参数：
| Name | Type | Description |
| Lhs | t |  |
| Rhs | comparable |  |
| t | comparable |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
