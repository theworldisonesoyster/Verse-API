---
name: quest_category
slug: unrealenginedotcom/progression/quest_category
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/progression/quest_category
kind: class
module: /UnrealEngine.com/progression
grade: B
depth: brief
status: done
---

# quest_category class <B>

> A category in the quest UI.
> 任务 UI 中的分类。

`using { /UnrealEngine.com/Progression }`

## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| has_icon | 提供图标的接口。 |
| has_description | 提供描述性名称或文本的接口。 |


## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| [SortOrder](quest_category_sortorder.md) | rational | 在任务 UI 中的相对排序；值越小越靠前。 |
| [Parent](quest_category_parent.md) | ?quest_category | 此类别被视为嵌套于其下的上级类别。 |
