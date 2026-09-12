---
name: tag_key
slug: versedotorg/simulation/tags/tag_key
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/tags/tag_key
kind: struct
module: /Verse.org/Simulation/Tags
grade: A
depth: full
status: done
---

# tag_key struct 🟩【A级·常用】

> A tag_key is the return value from adding a tag to a container implementing the has_tags interface, and is used to selectively remove such an instance from the same container.
> tag_key 是向实现了 has_tags 接口的容器添加标签后的返回值，用于从同一容器中**选择性地移除**那一个标签实例。

`using { /Verse.org/Simulation/Tags }`

## Members

This struct has no members.（此结构体没有成员。）

## 示例

```verse
using { /Verse.org/Simulation/Tags }

# 保存 AddTag 返回的 key，之后精确撤销那一次打标
Stamp(Obj:has_tags):tag_key =
    Obj.AddTag(TempTag)
```

## 补充说明

- 同一对象打了三个同类型标签就有三个不同的 tag_key；按类型整体清除用 [has_tags interface](has_tags.md) 的 RemoveAllTags 即可，无需保存 key。
- 相关页面：[tag class](tag.md)。
