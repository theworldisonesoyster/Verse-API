---
name: invalidatable
slug: versedotorg/verse/invalidatable
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/invalidatable
kind: interface
module: /Verse.org/Verse
grade: B
depth: brief
status: done
---

# invalidatable interface <B>

> Implemented by classes whose instances can become invalid at runtime.
> 由「实例可能在运行时失效」的类实现。

`using { /Verse.org/Verse }`

## Exposed Interfaces

This interface exposes the following interfaces:（此接口暴露以下接口：）

| Name | Description |
|---|---|
| disposable | 由实例生命周期有限的类实现。 |

## Members

This interface has functions, but no data members.（此接口只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| [IsValid](invalidatable_isvalid.md) | 若此对象仍然有效则成功。 |

## 补充说明

- 引用可能失效的对象（如已退出的玩家相关对象）时，先 IsValid[] 再用。
