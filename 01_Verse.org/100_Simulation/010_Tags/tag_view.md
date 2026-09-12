---
name: tag_view
slug: versedotorg/simulation/tags/tag_view
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/tags/tag_view
kind: class
module: /Verse.org/Simulation/Tags
grade: A
depth: full
status: done
---

# tag_view 🟩【A级·常用】

> A read-only view for checking tags, with hierarchical matching.
> 标签的只读查询视图，支持层级匹配。

## 这是什么

`tag_view` 把一组标签包装成"只读查询对象"，提供 `Has / HasAny / HasAll` 三个判断函数。与 `has_tags` 的 `Contains*` 相比，它显式支持**父标签命中子标签**的层级规则，官方文档直接给出了判定示例。

## 签名

```verse
tag_view<public><native> := class<native>:
```

## 常用成员

| 函数 | 语义（官方示例编译） | 级别 |
|---|---|---|
| `Has(TagToCheck)` | `{"A.1"}.Has("A")` → true；`{"A"}.Has("A.1")` → false；无效参数恒 false | 🟩 A |
| `HasAny(InTags)` | 任一命中即真；`InTags` 为空恒 false | 🟩 A |
| `HasAll(InTags)` | 全部命中才真；`InTags` 为空恒 true | 🟩 A |

## 最小示例

```verse
using { /Verse.org/Simulation/Tags }

IsHostile(View:tag_view):logic =
    View.Has(EnemyTag)     # "Enemy.Ranged" 也会命中 "Enemy"
```

## 相关页面

- [has_tags](has_tags.md)
- [tag](tag.md)
