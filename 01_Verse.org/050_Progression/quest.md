---
name: quest
slug: versedotorg/progression/quest
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/progression/quest
kind: class
module: /Verse.org/progression
grade: B
depth: brief
status: done
---

# quest class <B>

> A completable goal. Call Complete() to mark the quest as done and fire CompleteEvent.
> 一个可完成的目标。调用 Complete() 把任务标记为完成并触发 CompleteEvent。

`using { /Verse.org/Progression }`

## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [JoinEvent](quest_joinevent.md) | unknown | 有参与者加入此任务时触发。 |
| [AbandonEvent](quest_abandonevent.md) | unknown | 有参与者放弃此任务时触发。 |
| [CompleteEvent](quest_completeevent.md) | unknown | 此任务完成时触发。 |

### Functions
| Function Name | Description |
| [Complete](quest_complete.md) | 把任务标记为完成并触发 CompleteEvent。幂等：已完成时无操作。 |
| [IsComplete](quest_iscomplete.md) | 此任务已完成则成功。 |
