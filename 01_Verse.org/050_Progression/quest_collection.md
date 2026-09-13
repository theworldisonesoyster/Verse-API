---
name: quest_collection
slug: versedotorg/progression/quest_collection
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/progression/quest_collection
kind: class
module: /Verse.org/progression
grade: B
depth: brief
status: done
---

# quest_collection class <B>

> The source of truth for quest participation.
> 任务参与关系的唯一事实来源（source of truth）。

`using { /Verse.org/Progression }`

## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| JoinEvent | unknown | 有参与者加入此集合中任一任务时触发。 |
| AbandonEvent | unknown | 有参与者放弃此集合中任一任务时触发。 |
| CompleteEvent | unknown | 此集合中任一任务完成时触发。 |
| Quests | ?[quest][]quest_membership | 按任务索引的全部成员关系。 |
| Participants | ?[quest_participant][]quest_membership | 按参与者索引的全部成员关系。 |

### Functions
| Function Name | Description |
| JoinQuest | 以给定的参与信息把 Participant 加入 Quest。 |
| AbandonQuest | 把 Participant 从 Quest 中移除。 |
