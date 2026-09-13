---
name: tick_events
slug: versedotorg/scenegraph/tick_events
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/tick_events
kind: class
module: /Verse.org/scenegraph
grade: S
depth: full
status: done
---

> Describes discrete phases of a frame update. Subscribe to members of the tick_events object to run code before or after the physics system has updated your object, allowing you to affect or react to those updates.
> 描述一次帧更新的各个离散阶段。订阅 tick_events 对象的成员，即可在物理系统更新你的对象之前或之后运行代码，从而影响或响应这些更新。

`using { /Verse.org/SceneGraph }`

## Members

（成员详见官方页：PrePhysics / PostPhysics 等阶段回调。）

## 示例

```verse
# 组件中注册帧回调（配合 component.TickEvents 使用）
```

## 补充说明

- [component class](tick_events.md) 的 TickEvents 字段即此类型；物理前/后两个阶段对应 PrePhysics/PostPhysics。
