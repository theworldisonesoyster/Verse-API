---
name: Tags
slug: versedotorg/simulation/tags
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/tags
kind: module
module: /Verse.org/Simulation/Tags
grade: A
depth: brief
status: done
---

# Tags（标签系统）🟩【A级·常用】

> 官网对本子模块无单独描述；本页为模块总览。
> Tags 提供一个通用"标签"系统：给对象打上字符串层级标签（如 `Door.Locked`），之后按标签查询、过滤、分组。

## 这是什么

标签是层级式的：`"A.1"` 被视为 `"A"` 的子标签，查询父标签会命中子标签（`{"A.1"}.Has("A")` 为真，反之不然）。给实体/组件实现 [has_tags](has_tags.md) 接口后即可打标与查询；[tag_view](tag_view.md) 提供只读查询视图；[tag_search_criteria](tag_search_criteria.md) 描述"按什么条件搜"。

## 使用前提

```verse
using { /Verse.org/Simulation/Tags }
```

## 成员一览

| 成员 | 类型 | 一句话 | 级别 |
|---|---|---|---|
| [tag](tag.md) | 类 | 标签类型本体 | 🟩 A |
| [tag_key](tag_key.md) | 类 | 一次打标返回的句柄，用于精确移除 | 🟩 A |
| [has_tags](has_tags.md) | 接口 | "可以打标"的能力契约 | 🟩 A |
| [tag_view](tag_view.md) | 类 | 只读查询视图（Has/HasAny/HasAll） | 🟩 A |
| [tag_search_criteria](tag_search_criteria.md) | 类 | 搜索条件描述 | 🟨 B |
| [tag_search_sort_type](tag_search_sort_type.md) | 枚举 | 搜索结果排序方式 | ⬜ C |

## 相关页面

- [Simulation 总览](../_overview.md)
