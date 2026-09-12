---
name: has_tags
slug: versedotorg/simulation/tags/has_tags
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/tags/has_tags
kind: interface
module: /Verse.org/Simulation/Tags
grade: A
depth: full
status: done
---

# has_tags interface 🟩【A级·常用】

> An interface representing a mutable collection of tags.
> 表示"可变标签集合"的接口：实现了它的对象即可打标、查标、摘标。

`using { /Verse.org/Simulation/Tags }`

## Members

This interface has functions, but no data members.（此接口只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| AddTag | 向此容器添加一个标签实例，返回与该实例唯一关联的 tag_key。 |
| RemoveTag | 移除与 tag_key 关联的标签实例；移除了实例则成功，否则失败。 |
| RemoveAllTags | 移除 tag_type 类型的全部标签实例；至少移除一个则成功，否则失败。 |
| RemoveAllTagsExcept | 移除不属于 tag_type 类型的全部标签实例；至少移除一个则成功，否则失败。 |
| RemoveAllTagsExcept | 移除不属于 tag_types 中任何类型的全部标签实例；至少移除一个则成功，否则失败。 |
| ContainsTag | 若容器中找到至少一个 tag_type 类型的标签则成功，否则失败。 |
| ContainsAllTags | 若 tag_types 中有任一类型在容器中找不到则失败，否则成功。注意 tag_types 为空时此调用成功。 |
| ContainsAnyTag | 若 tag_types 中至少一个类型在容器中找到则成功，否则失败。注意 tag_types 为空时此调用失败。 |

## 示例

```verse
using { /Verse.org/Simulation/Tags }

Unlock(Obj:has_tags):void =
    if (Obj.ContainsTag[LockTag]):
        Obj.RemoveAllTags[LockTag]   # 摘掉"上锁"标签
```

## 补充说明

- `Contains*` 是可失败查询（`<decides>`），必须写在失败上下文里。
- 精确移除某一次打标：用 AddTag 返回的 [tag_key struct](tag_key.md) 调 RemoveTag。
- 相关页面：[tag class](tag.md)、[tag_view interface](tag_view.md)。
