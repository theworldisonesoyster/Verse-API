---
name: npc_behavior
slug: fortnitedotcom/ai/npc_behavior
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/npc_behavior
kind: class
module: /Fortnite.com/ai
grade: A
depth: full
status: done
---

# npc_behavior class <A>

> Inherit from this to create a custom NPC behavior. The npc_behavior can be defined for a character in a CharacterDefinition asset, or in a npc_spawner_device.
> 继承它来创建自定义 NPC 行为。npc_behavior 可在 CharacterDefinition 资产或 npc_spawner_device 中为角色指定。

`using { /Fortnite.com/AI }`

## Members

只有函数，没有数据成员。

### Functions
| Function Name | Description |
| OnBegin | NPC 被加入模拟时调用此函数。 |
| OnEnd | NPC 被移出模拟时调用此函数。 |
| GetAgent | 返回与此行为关联的代理。 |
| GetEntity | 返回与此行为关联的实体。 |
