---
name: showable
slug: versedotorg/verse/showable
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/showable
kind: interface
module: /Verse.org/Verse
grade: B
depth: brief
status: done
---

> Implemented by classes whose instances can change visibility to be shown or hidden.
> 由「实例可切换显示/隐藏」的类实现。

`using { /Verse.org/Verse }`

## Members

This interface has data members, but no functions.（此接口只有数据成员，没有函数。）

### Data

| Data Member Name | Type | Description |
|---|---|---|
| Show | ?logic | 设置此值以隐藏或显示该对象（true 显示 / false 隐藏）。 |

## 补充说明

- `?logic` 赋值写法：`if (set Obj.Show = true) {}`。

