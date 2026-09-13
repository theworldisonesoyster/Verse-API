---
name: quest_objective
slug: unrealenginedotcom/progression/quest_objective
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/progression/quest_objective
kind: class
module: /UnrealEngine.com/progression
grade: B
depth: brief
status: done
---

# quest_objective class <B>

> Abstract base class for all quest objectives.
> 所有任务目标的抽象基类。

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
| CompleteEvent | listenable(payload) | 此目标被判定完成时触发。 |
| ProgressEvent | listenable(payload) | 此目标的进度变化时触发。载荷：此目标。 |

### Functions
| Function Name | Description |
| GetProgress | 返回进度消息（如 "3 / 10"）。 |
| GetContributors | 决定哪些参与者可为此目标做贡献。可重写以自定义贡献者选择。默认：Info.Contributes = true 的所有参与者。 |
| IsComplete | 此目标当前已完成则成功。 |
| SignalProgressEvent | 发出 ProgressEvent。在子类中调用以通知进度订阅者。 |
