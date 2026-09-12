---
name: tag_search_criteria
slug: versedotorg/simulation/tags/tag_search_criteria
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/tags/tag_search_criteria
kind: class
module: /Verse.org/Simulation/Tags
grade: B
depth: brief
status: done
---

# tag_search_criteria class 🟨【B级·进阶】

> Advanced tag search criteria
> 高级标签搜索条件。

`using { /Verse.org/Simulation/Tags }`

## Members

This class has data members, but no functions.（此类只有数据成员，没有函数。）

### Data

| Data Member Name | Type | Description |
|---|---|---|
| RequiredTags | []tag | 对象必须携带的标签。 |
| PreferredTags | []tag | 未指定必须标签时才使用的标签；它们被视为"任一满足即可"。 |
| ExclusionTags | []tag | 对象**不得**携带的标签；带这些标签的条目都会被搜索排除。 |
| SortType | tag_search_sort_type | 请求按标签排序结果的开关。 |

## 补充说明

- 排序方式枚举见 [tag_search_sort_type enumeration](tag_search_sort_type.md)。
