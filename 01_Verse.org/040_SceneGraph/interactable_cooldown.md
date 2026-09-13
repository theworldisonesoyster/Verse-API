---
name: interactable_cooldown
slug: versedotorg/scenegraph/interactable_cooldown
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_cooldown
kind: class
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# interactable_cooldown class <B>

> Used to set a cooldown when interacted.
> 设置交互后的冷却。

`using { /Verse.org/SceneGraph }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| [Duration](interactable_cooldown_duration.md) | ?float | 成功交互后、任何人都可再次发起交互之前所需的秒数。仅在 duration > 0.0 时生效；修改它不影响 RemainingDuration。组件开始冷却时，其上的所有其他交互都会被取消。 |
| [RemainingDuration](interactable_cooldown_remainingduration.md) | ?float | 此组件上可再次发起新交互前的剩余冷却秒数。 |
| [ExpiredEvent](interactable_cooldown_expiredevent.md) | unknown | 共享冷却到期时触发的事件。 |
