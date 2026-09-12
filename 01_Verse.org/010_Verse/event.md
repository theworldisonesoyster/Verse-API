---
name: event
slug: versedotorg/verse/event
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/event
kind: function
module: /Verse.org/Verse
grade: S
depth: full
status: done
---

# event function 🟦【S级·核心】

> A recurring, successively signaled parametric event with a payload allowing a simple mechanism to coordinate between concurrent tasks.
> 可重复、按次序触发的参数化事件，带有载荷，为并发任务之间的协调提供简单机制。

`using { /Verse.org/Verse }`

```verse
event<public>(t:any):event(t)
```

This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
（此函数是参数化类型：它返回的是类或接口，而不是值或对象实例。）

## Parameters

event takes the following parameters:（event 接受以下参数：）

| Name | Type | Description |
|---|---|---|
| t | any | 事件载荷的类型。 |

### Generated Class

event returns the parametric class `event(t)`.（event 返回参数化类 event(t)。）

## Attributes, Specifiers, and Effects

`event<public>(t:any):event(t)` —— 标签：public，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Verse }

Gate:event(logic) = event(logic){}   # 生成 logic 载荷的 event(t) 实例
```

## 补充说明

- 本页是构造函数；Signal/Await 的行为见 [event(t) class](event_t.md)。
- 无载荷构造重载见 [event function（无载荷）](event-1.md)。
