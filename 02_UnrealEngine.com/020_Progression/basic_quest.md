---
name: basic_quest
slug: unrealenginedotcom/progression/basic_quest
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/progression/basic_quest
kind: class
module: /UnrealEngine.com/progression
grade: B
depth: brief
status: done
---

# basic_quest class <B>

> Standard quest that follows the "do x, get y" paradigm. Auto-completion: when Objective.IsComplete() succeeds, calls Complete() automatically. Auto-rewarding: on completion, rewards are granted to eligible participants via GetRecipients() then GrantReward().
> 标准任务：遵循「做 X 得 Y」范式。自动完成——当 Objective.IsComplete() 成功时自动调用 Complete()；自动发奖——完成时经 GetRecipients() 与 GrantReward() 向符合条件的参与者发放奖励。

`using { /UnrealEngine.com/Progression }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| quest | 一个可完成的目标。调用 Complete() 把任务标记为完成并触发 CompleteEvent。 |


## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| has_icon | 提供图标的接口。 |
| has_description | 提供描述性名称或文本的接口。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [AbandonEvent](basic_quest_abandonevent.md) | unknown | 有参与者放弃此任务时触发。 |
| [CompleteEvent](basic_quest_completeevent.md) | unknown | 此任务完成时触发。 |
| [JoinEvent](basic_quest_joinevent.md) | unknown | 有参与者加入此任务时触发。 |
| [Objective](basic_quest_objective.md) | ?quest_objective | 任务的进度模型。 |
| [Rewards](basic_quest_rewards.md) | ?[]quest_reward | 完成时向符合条件的参与者发放的奖励。 |

### Functions
| Function Name | Description |
| [Complete](basic_quest_complete.md) | 把任务标记为完成并触发 CompleteEvent。幂等：已完成时无操作。 |
| [IsComplete](basic_quest_iscomplete.md) | 此任务已完成则成功。 |
| [SetObjective](basic_quest_setobjective.md) | 替换进行中任务的进度模型；新目标已完成时自动完成。 |
