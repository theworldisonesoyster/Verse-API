---
name: operator'+='
slug: versedotorg/verse/operatorplusequals-2
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/operatorplusequals-2
kind: function
module: /Verse.org/verse
grade: B
depth: brief
status: done
---

# operator'+=' function <B>

数组累加：把 Rhs 的元素追加进 Lhs 数组。

`using { /Verse.org/Verse }`

```verse
operator'+='(Lhs:[]t, Rhs:[]t where t:any)<transacts><predicts>:[]t
```

## Parameters

operator'+=' 接受以下参数：
| Name | Type | Description |
| Lhs | []t |  |
| Rhs | []t |  |
| t | any |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
