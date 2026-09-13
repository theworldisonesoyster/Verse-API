---
name: interactable_cooldown_per_agent
slug: versedotorg/scenegraph/interactable_cooldown_per_agent
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_cooldown_per_agent
kind: class
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# interactable_cooldown_per_agent class <B>

> Used to set a cooldown per agent when interacted.
> 按代理分别设置交互冷却。

`using { /Verse.org/SceneGraph }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| [Duration](interactable_cooldown_per_agent_duration.md) | ?float | 成功交互后、发起交互的代理可再次发起交互之前所需的秒数。仅在 duration > 0.0 时生效；修改不影响 RemainingPerAgentCooldownDuration。当可同时交互人数有限时，此属性给其他代理留出交互时间。 |
| [RemainingDuration](interactable_cooldown_per_agent_remainingduration.md) | ?[agent]float | 特定代理在此组件上可再次发起交互前的剩余冷却秒数。 |
| [ExpiredEvent](interactable_cooldown_per_agent_expiredevent.md) | unknown | 按代理的冷却到期时触发；载荷为此前受冷却影响的代理。 |
