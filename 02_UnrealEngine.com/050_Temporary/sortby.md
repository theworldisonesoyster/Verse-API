---
name: SortBy
slug: unrealenginedotcom/temporary/sortby
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/sortby
kind: function
module: /Verse.org/temporary
grade: A
depth: full
status: done
---

# SortBy function <A>

> Stably sort Array using Less where Less succeeding indicates Left should precede Right
> 用 Less 对 Array 稳定排序：Less 成功表示 Left 应排在 Right 之前。

`using { /UnrealEngine.com/Temporary }`

```verse
SortBy<public><native>(Array:[]t, Less:((t, t)):void where t:any):[]t
```

## Parameters

SortBy 接受以下参数：
| Name | Type | Description |
| Array | []t |  |
| Less | ((t, t)):void |  |
| t | any |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
