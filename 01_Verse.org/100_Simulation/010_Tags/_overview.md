---
name: Tags
slug: versedotorg/simulation/tags
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/tags
kind: module
module: /Verse.org/Simulation
grade: A
depth: brief
status: done
---

# Tags module <A>

> Verse path: `/Verse.org/Simulation` · Module import path: `/Verse.org/Simulation/Tags`
> 通用标签系统：给对象打上层级标签（如 `A.1` 属于 `A`），按标签查询、过滤、分组。

`using { /Verse.org/Simulation/Tags }`

- Verse.org
- Simulation
- Tags

## Classes and Structs

| Name | Description |
|---|---|
| [tag](tag.md) | 用于给对象打标签的基础类型，以便按层级评估对象的分类。 |
| [tag_key](tag_key.md) | 向实现了 has_tags 接口的容器添加标签的返回值，用于从同一容器中选择性移除该实例。 |
| [tag_search_criteria](tag_search_criteria.md) | 高级标签搜索条件。 |

## Interfaces

| Name | Description |
|---|---|
| [has_tags](has_tags.md) | 表示"可变标签集合"的接口。 |
| [tag_view](tag_view.md) | 表示"可查询标签集合"的接口。 |

## Enumerations

| Name | Description |
|---|---|
| [tag_search_sort_type](tag_search_sort_type.md) | （官网无描述。） |

## 补充说明

- 标签匹配是**层级向下**的：查询父标签会命中子标签（`{"A.1"}.Has("A")` 为真，反之不然），规则见 [tag_view interface](tag_view.md)。
- 实现了 [has_tags interface](has_tags.md) 的对象才能打标；entity/agent/player 等已自带整套标签函数。
