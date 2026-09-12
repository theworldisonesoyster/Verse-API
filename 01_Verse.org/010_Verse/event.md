---
name: event(t) 构造函数
slug: versedotorg/verse/event
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/event
kind: function
module: /Verse.org/Verse
grade: S
depth: full
status: done
---

# event(t) 构造函数 🟦【S级·核心】

> event<public>(t:any):event(t) —— 参数化构造：按载荷类型创建事件实例。
> 官方说明：This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.

## 签名

```verse
event<public>(t:any):event(t)
```

## 这是什么

`event(t)` 类没有直接字面量构造，统一走这个构造函数：`event(int){}` 得到"int 载荷事件"，`event(tuple(agent, logic))` 得到复合载荷事件。类型参数决定 [event(t)](event_t.md) 的载荷类型。

## 最小示例

```verse
using { /Verse.org/Verse }

Gate:event(logic) = event(logic){}     # logic 载荷
DoorOpen:event() = event(){?}          # 无载荷版本见 event-1
```

## 相关页面

- [event(t) 类](event_t.md) —— Signal/Await 用法
- [event-1](event-1.md) —— 无载荷构造
