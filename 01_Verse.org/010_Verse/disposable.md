---
name: disposable
slug: versedotorg/verse/disposable
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/disposable
kind: interface
module: /Verse.org/Verse
grade: B
depth: brief
status: done
---

# disposable interface <B>

> Implemented by classes whose instances have limited lifetimes.
> 由「实例生命周期有限」的类实现。

`using { /Verse.org/Verse }`

## Members

This interface has functions, but no data members.（此接口只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| [Dispose](disposable_dispose.md) | 清理并释放此对象。 |

## 补充说明

- 对象被 Dispose 后不可再使用；长生命周期脚本持有此类对象时注意及时释放。
