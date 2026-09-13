---
name: agent_quest_participant
slug: versedotorg/progression/agent_quest_participant
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/progression/agent_quest_participant
kind: class
module: /Verse.org/progression
grade: B
depth: brief
status: done
---

# agent_quest_participant class <B>

> A quest participant backed by an agent (player, NPC, AI, etc.).
> 以代理（agent）为载体的任务参与者——玩家、NPC、AI 等都适用。

`using { /Verse.org/Progression }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| quest_participant | 任务参与者的抽象基类。 |


## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| AbandonEvent | unknown | 此参与者放弃任务时触发。 |
| Agent | agent | 此参与者所代表的代理。 |
| CompleteEvent | unknown | 此参与者所在的任务完成时触发。 |
| JoinEvent | unknown | 此参与者加入任务时触发。 |
