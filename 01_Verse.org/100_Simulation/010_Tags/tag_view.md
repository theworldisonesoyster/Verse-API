---
name: tag_view
slug: versedotorg/simulation/tags/tag_view
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/tags/tag_view
kind: interface
module: /Verse.org/Simulation/Tags
grade: A
depth: full
status: done
---

# tag_view interface <A>

> A queryable collection of tags.
> 表示"可查询标签集合"的接口：提供带层级匹配规则的只读查询。

`using { /Verse.org/Simulation/Tags }`

## Members

This interface has functions, but no data members.（此接口只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| Has | 判断 TagToCheck 是否存在于此容器中，同时会向上匹配父标签：`{"A.1"}.Has("A")` 返回 True；`{"A"}.Has("A.1")` 返回 False。若 TagToCheck 无效则恒返回 False。 |
| HasAny | 检查此容器是否包含指定容器中的**任意一个**标签，同样向上匹配父标签：`{"A.1"}.HasAny({"A","B"})` 返回 True；`{"A"}.HasAny({"A.1","B"})` 返回 False。若 InTags 为空/无效则恒返回 False。 |
| HasAll | 检查此容器是否包含指定容器中的**全部**标签，同样向上匹配父标签：`{"A.1","B.1"}.HasAll({"A","B"})` 返回 True；`{"A","B"}.HasAll({"A.1","B.1"})` 返回 False。若 InTags 为空/无效则恒返回 True，因为没有任何失败的检查。 |

## 示例

```verse
using { /Verse.org/Simulation/Tags }

IsHostile(View:tag_view):logic =
    View.Has(EnemyTag)   # "Enemy.Ranged" 也会命中 "Enemy"
```

## 补充说明

- 层级规则一句话：**查父命中子，查子不命中父**；空集合时 HasAny=false、HasAll=true。
- 相关页面：[has_tags interface](has_tags.md)、[tag class](tag.md)。
