---
name: tag_key
slug: versedotorg/simulation/tags/tag_key
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/tags/tag_key
kind: class
module: /Verse.org/Simulation/Tags
grade: A
depth: full
status: done
---

# tag_key 🟩【A级·常用】

> A key returned by AddTag that uniquely identifies one added tag instance.
> AddTag 返回的句柄，唯一标识"某一次打的标签"，用于精确移除。

## 这是什么

每次调用 `AddTag` 都会返回一个 `tag_key`。同一对象打了三个同类型标签就有三个不同的 key。想摘掉**其中某一个**（而不是按类型全清）时，把对应的 key 传给 `RemoveTag`。它本身没有成员，是一个"取牌凭证"。

## 签名

```verse
tag_key<public><native> := class<native>:
    # 无自有成员
```

## 最小示例

```verse
using { /Verse.org/Simulation/Tags }

var MyKeys:[]tag_key = array{}

Stamp(Obj:has_tags):void =
    Key := Obj.AddTag(TempTag)
    set MyKeys += array{Key}     # 留着 key，之后可精确撤销

Unstamp(Obj:has_tags):void =
    for (K : MyKeys):
        Obj.RemoveTag(K)
```

## 何时用 / 何时不用

- 用：需要"撤销某一次打标"的场合（临时状态标记）。
- 不用：只想按类型整体清空时直接 `RemoveAllTags[TagType]`，不必保存 key。

## 相关页面

- [has_tags](has_tags.md) —— AddTag/RemoveTag
- [tag](tag.md)
