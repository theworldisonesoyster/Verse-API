---
name: tag
slug: versedotorg/simulation/tags/tag
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/tags/tag
kind: class
module: /Verse.org/Simulation/Tags
grade: A
depth: full
status: done
---

# tag class 🟩【A级·常用】

> A base type used for tagging objects in order to hierarchically evaluate an objects classification.
> 用于给对象打标签的基础类型，以便按层级评估对象的分类。

`using { /Verse.org/Simulation/Tags }`

## Members

This class has no members.（此类没有成员。）

## 示例

```verse
using { /Verse.org/Simulation/Tags }

# tag 实例本身无字段；层级语义由使用方的 API 约定
EnemyTag:tag = tag{}
```

## 补充说明

- 标签的"值/层级"由使用标签系统的具体 API 决定；本页类型只是分类标识。
- 打标与查询走 [has_tags interface](has_tags.md)；层级匹配规则见 [tag_view interface](tag_view.md)。
