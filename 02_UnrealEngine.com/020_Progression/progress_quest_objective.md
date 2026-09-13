---
name: progress_quest_objective
slug: unrealenginedotcom/progression/progress_quest_objective
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/progression/progress_quest_objective
kind: class
module: /UnrealEngine.com/progression
grade: B
depth: brief
status: done
---

# progress_quest_objective class <B>

> Tracks numeric progress toward a required count. Complete when Progress >= RequiredCount.
> 追踪到所需计数的数值进度；Progress ≥ RequiredCount 时完成。

`using { /UnrealEngine.com/Progression }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| quest_objective | 所有任务目标的抽象基类。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| CompleteEvent | listenable(payload) | 此目标被判定完成时触发。 |
| Progress | ?float | 距 RequiredCount 的当前进度。 |
| ProgressEvent | listenable(payload) | 此目标的进度变化时触发。载荷：此目标。 |
| RequiredCount | ?float | 完成所需的目标计数。 |

### Functions
| Function Name | Description |
| GetContributors | 决定哪些参与者可为此目标做贡献。可重写以自定义贡献者选择。默认：Info.Contributes = true 的所有参与者。 |
| GetProgress | 以 "X / Y" 格式返回进度。 |
| GetProgress | 返回进度消息（如 "3 / 10"）。 |
| IsComplete | Progress ≥ RequiredCount 则成功。 |
| IsComplete | 此目标当前已完成则成功。 |
| SetProgress | 设置当前进度；钳制到 [0, RequiredCount]。 |
| SetRequiredCount | 设置目标计数；钳制到 [1, MaxFloat]。 |
| SignalProgressEvent | 发出 ProgressEvent。在子类中调用以通知进度订阅者。 |
