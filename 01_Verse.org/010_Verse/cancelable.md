---
name: cancelable
slug: versedotorg/verse/cancelable
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/cancelable
kind: interface
module: /Verse.org/Verse
grade: B
depth: brief
status: done
---

> Implemented by classes that allow users to cancel an operation. For example, calling subscribable.Subscribe with a callback returns a cancelable object. Calling Cancel on the return object unsubscribes the callback.
> 由「允许用户取消操作」的类实现。例如调用 subscribable.Subscribe 传回调时会返回一个 cancelable 对象；对该对象调用 Cancel 即可取消订阅回调。

`using { /Verse.org/Verse }`

## Members

This interface has functions, but no data members.（此接口只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| Cancel | 阻止该操作当前或未来的任何工作完成（即取消）。 |

## 补充说明

- 典型来源：`Subscribe` 的返回值——留着它即可随时退订事件。
- 相关页面：[subscribable function](subscribable.md)、[listenable function](listenable.md)。
