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

# has_tags 🟩【A级·常用】

> Interface for containers that can hold tag instances.
> "可持有标签"的接口：实现了它的对象就能打标、查标、摘标。

## 这是什么

这是标签系统的能力契约：只要对象实现了 `has_tags`，就能对它调用下面这组函数。SceneGraph 的实体/组件体系中的可标签对象都实现了它。`AddTag` 返回 [tag_key](tag_key.md)，想精确摘掉某一次打的标就留着这个 key。

## 签名

```verse
has_tags<public><native> := interface<native>:
```

## 常用成员（函数）

| 函数 | 说明（官方描述编译） | 级别 |
|---|---|---|
| `AddTag(Tag)` | 加一个标签实例，返回唯一 tag_key | 🟩 A |
| `RemoveTag(Key)` | 按 tag_key 摘标；摘掉成功否则失败 | 🟩 A |
| `RemoveAllTags[TagType]` | 摘掉该类型的全部标签 | 🟩 A |
| `RemoveAllTagsExcept[TagType]` | 摘掉除指定类型外的全部标签（有两个重载：单类型/类型数组） | 🟨 B |
| `ContainsTag[TagType]` | 是否含至少一个该类型标签（可失败） | 🟩 A |
| `ContainsAllTags[TagTypes]` | 是否全部包含（空数组视为成功） | 🟩 A |
| `ContainsAnyTag[TagTypes]` | 是否包含任一（空数组视为失败） | 🟩 A |

## 最小示例

```verse
using { /Verse.org/Simulation/Tags }

Unlock(Obj:has_tags):void =
    if (Obj.ContainsTag[LockTag]):
        Obj.RemoveAllTags[LockTag]   # 摘掉"上锁"标签
```

## 常见坑

- `Contains*` 是可失败查询，要写在 `if` 等失败上下文里。
- 精确移除某次打标用 `RemoveTag(AddTag 返回的 key)`；按类型清用 `RemoveAllTags`。

## 相关页面

- [tag](tag.md) / [tag_key](tag_key.md)
- [tag_view](tag_view.md) —— 只读查询视图
