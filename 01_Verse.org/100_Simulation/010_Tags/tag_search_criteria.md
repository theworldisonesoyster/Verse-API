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

# tag_search_criteria 🟨【B级·进阶】

> Describes the criteria used when searching for tagged objects.
> 描述"按标签搜索对象"时的条件（搜什么、怎么匹配）。

## 这是什么

配合标签搜索接口使用：声明要找的标签、匹配方式（层级/精确）等条件，交给搜索调用返回符合的对象集合。一般与 [tag_search_sort_type](tag_search_sort_type.md) 一起构成一次完整搜索请求。

## 签名

```verse
tag_search_criteria<public><native> := class<native>:
```

## 相关页面

- [tag](tag.md)
- [has_tags](has_tags.md)
