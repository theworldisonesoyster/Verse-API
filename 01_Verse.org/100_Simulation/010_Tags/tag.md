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

# tag 🟩【A级·常用】

> tag is a classification that can be added to objects to identify, filter, or group them.
> tag 是一种可加到对象上的"分类标记"，用于识别、过滤、分组对象。

## 这是什么

`tag` 是标签系统的类型本体。标签值为层级字符串：`"Enemy.Ranged"` 属于 `"Enemy"`。它通常以 `tag{}` 实例配合 [has_tags](has_tags.md) 接口使用：先 AddTag 打标，再用 [tag_view](tag_view.md) 或搜索接口按标签找对象。

## 签名

```verse
tag<public> := class<concrete>:
    # 标签实例；层级语义由字符串值决定
```

## 最小示例

```verse
using { /Verse.org/Simulation/Tags }

var Tags:weak_map[session, tag] = map{}

MakeEnemyTag():tag =
    tag{}   # 具体标签值由使用场景的 API 决定
```

## 何时用 / 何时不用

- 用：给一批对象做"逻辑分组"，之后按组批量操作。
- 不用：对象已能用引用直接访问时，不必绕道标签。

## 常见坑

- 标签匹配是**层级向下**的：父标签查询命中子标签，子标签查询不命中父标签。

## 相关页面

- [has_tags](has_tags.md) —— 打标/查询入口
- [tag_view](tag_view.md) —— 查询视图
