---
name: has_quest_presentation
slug: unrealenginedotcom/progression/has_quest_presentation
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/progression/has_quest_presentation
kind: interface
module: /UnrealEngine.com/progression
grade: B
depth: brief
status: done
---

# has_quest_presentation interface <B>

> Implement on a quest class to customize how it displays in the quest UI.
> 在任务类上实现此接口，可自定义其在任务 UI 中的展示。

`using { /UnrealEngine.com/Progression }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| [ShowNotification](has_quest_presentation_shownotification.md) | ?logic | 此任务的发放/进度/完成时刻是否播放 HUD 通知。 |
| [AllowFavorite](has_quest_presentation_allowfavorite.md) | ?logic | 玩家是否可把此任务收藏到 HUD 任务追踪器。 |
| [Categories](has_quest_presentation_categories.md) | ?[]quest_category | 此任务在任务 UI 中归属的类别；空 = 未分类。 |
