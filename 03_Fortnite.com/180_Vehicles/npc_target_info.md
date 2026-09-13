---
name: npc_target_info
slug: fortnitedotcom/ai/npc_target_info
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/npc_target_info
kind: class
module: /Fortnite.com/ai
grade: B
depth: brief
status: done
---

# npc_target_info class <B>

> Information about a perceived target.
> 关于被感知目标的信息。

`using { /Fortnite.com/AI }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| [Target](npc_target_info_target.md) | entity | 被侦测到的实体。 |
| [HasLineOfSight](npc_target_info_haslineofsight.md) | ?logic | 目标可见则为 true。 |
| [Attitude](npc_target_info_attitude.md) | ?team_attitude | 对此目标的态度。 |
| [LastKnownPosition](npc_target_info_lastknownposition.md) | ?vector3 | 此目标最后已知位置。 |
| OnUpdateEvent | listenable(payload) | 目标信息更新时触发。 |
