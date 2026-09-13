---
name: entitlement_quest_reward
slug: unrealenginedotcom/progression/entitlement_quest_reward
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/progression/entitlement_quest_reward
kind: class
module: /UnrealEngine.com/progression
grade: B
depth: brief
status: done
---

# entitlement_quest_reward class <B>

> Grants an entitlement to each eligible participant.
> 向每个符合条件的参与者授予一个 entitlement（授权项目）。

`using { /UnrealEngine.com/Progression }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| quest_reward | 所有任务奖励的抽象基类。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| Entitlement | ?concrete_subtype(entitlement) | 要授予的 entitlement 类型。 |
| GrantEvent | listenable(payload) | 此奖励发放给接收者之后触发。 |
| Quantity | ?int | 每个参与者的数量。 |

### Functions
| Function Name | Description |
| GetRecipients | 决定哪些参与者应获得此奖励。可重写以自定义接收者选择。默认：Info.Receives = true 的所有参与者。 |
| GrantReward | 遍历 EligibleParticipants，把每个参与者的代理解析为玩家，并通过平台授权服务发放 entitlement。 |
| GrantReward | 把此奖励发放给符合条件的参与者。 |
