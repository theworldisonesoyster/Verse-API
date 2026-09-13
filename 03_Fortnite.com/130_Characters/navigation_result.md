---
name: navigation_result
slug: fortnitedotcom/ai/navigation_result
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/navigation_result
kind: enum
module: /Fortnite.com/ai
grade: B
depth: brief
status: done
---

# navigation_result enumeration <B>

> Result of a navigation request
> 导航请求的结果。

`using { /Fortnite.com/AI }`

## Enumerators

The navigation_result 枚举包含以下枚举值：
| Name | Description |
| Reached | 已到达目的地 |
| PartiallyReached | 部分到达（使用了 AllowPartialPath）。 |
| Interrupted | 导航在完成前被打断 |
| Blocked | 导航中的代理被阻挡 |
| Unreachable | 目的地无法到达 |
