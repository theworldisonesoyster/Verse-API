---
name: quest_reward
slug: unrealenginedotcom/progression/quest_reward
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/progression/quest_reward
kind: class
module: /UnrealEngine.com/progression
grade: B
depth: brief
status: done
---

# quest_reward class <B>

> Abstract base class for all quest rewards.
> 所有任务奖励的抽象基类。

`using { /UnrealEngine.com/Progression }`

## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| has_icon | 提供图标的接口。 |
| has_description | 提供描述性名称或文本的接口。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| GrantEvent | listenable(payload) | 此奖励发放给接收者之后触发。 |

### Functions
| Function Name | Description |
| GetRecipients | 决定哪些参与者应获得此奖励。可重写以自定义接收者选择。默认：Info.Receives = true 的所有参与者。 |
| GrantReward | 把此奖励发放给符合条件的参与者。 |
