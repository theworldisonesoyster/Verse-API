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
| JoinEvent | unknown | 有参与者加入此任务时触发。 |
| AbandonEvent | unknown | 有参与者放弃此任务时触发。 |
| CompleteEvent | unknown | 此任务完成时触发。 |

### Functions
| Function Name | Description |
| Complete | 把任务标记为完成并触发 CompleteEvent。幂等：已完成时无操作。 |
| IsComplete | 此任务已完成则成功。 |
