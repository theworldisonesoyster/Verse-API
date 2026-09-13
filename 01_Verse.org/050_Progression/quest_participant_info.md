---
name: quest_participant_info
slug: versedotorg/progression/quest_participant_info
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/progression/quest_participant_info
kind: class
module: /Verse.org/progression
grade: B
depth: brief
status: done
---

# quest_participant_info class <B>

> Describes how a participant relates to a quest.
> 描述参与者与任务之间的关系。

`using { /Verse.org/Progression }`

## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| member_info_interface | 定义「可作为代理组成员信息」的接口。 |


## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| [Contributes](quest_participant_info_contributes.md) | ?logic | 该参与者能否在此任务上取得进展。 |
| [Observes](quest_participant_info_observes.md) | ?logic | 该参与者能否观察任务状态。 |
| [Receives](quest_participant_info_receives.md) | ?logic | 任务完成时该参与者能否获得奖励。 |
