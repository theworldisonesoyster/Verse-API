---
name: interactable_success_limit
slug: versedotorg/scenegraph/interactable_success_limit
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_success_limit
kind: class
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# interactable_success_limit class <B>

> Used to set a limit of times to interact.
> 设置可成功交互的次数上限。

`using { /Verse.org/SceneGraph }`

## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [MaxSuccessfulInteractions](interactable_success_limit_maxsuccessfulinteractions.md) | ??int | 此组件可被成功交互的次数；false 表示不限。达到 MaxSuccessfulInteractions 后所有活跃交互被取消，组件无法再被交互。 |
| [SuccessfulInteractionCount](interactable_success_limit_successfulinteractioncount.md) | ?int | 此组件已成功交互的次数。 |

### Functions
| Function Name | Description |
| [ClearSuccessfulInteractionCount](interactable_success_limit_clearsuccessfulinteractioncount.md) | 重置成功交互次数计数。 |
