---
name: interactable_duration
slug: versedotorg/scenegraph/interactable_duration
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_duration
kind: class
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# interactable_duration class <B>

> Used to set an interaction duration.
> 设置一次交互的持续时长。

`using { /Verse.org/SceneGraph }`

## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| InteractDuration | ?float | 代理需与对象持续交互这么多秒才能完成一次交互；≤0.0 表示立即成功。若在交互进行中设置，新值将用于下一次交互，剩余时长按「新值减去已用时间」更新；差值 ≤0 则立即结束。 |
| MaxSimultaneousInteractors | ??int | 可同时交互的最大人数；false 表示不限。表示有多少代理可同时处于交互中。若改成小于当前活跃交互数的值，已有交互不取消，但不会开始新交互。 |

### Functions
| Function Name | Description |
| GetRemainingInteractDurationForAgent | 返回某代理本次交互的剩余秒数；该代理未在交互则失败。同一事务内多次调用返回相同值。 |
| SetRemainingInteractDurationForAgent | 设置某代理本次交互的剩余秒数；该代理未在交互则失败。 |
