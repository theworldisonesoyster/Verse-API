---
name: Progression module
slug: versedotorg/progression
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/progression
kind: module
module: /versedotorg
grade: B
depth: brief
status: done
---

# Progression module <B>

任务（quest）系统：定义可完成的目标，管理参与者与其成员关系，完成任务时触发事件。

## Classes and Structs

| Name | Description |
|---|---|
| [quest_participant_info](quest_participant_info.md) | 描述参与者与任务之间的关系。 |
| [quest_membership](quest_membership.md) | 把任务与参与者及其参与信息绑定在一起的记录。 |
| [join_quest_error](join_quest_error.md) | 参与者无法加入任务时返回的错误。 |
| [abandon_quest_error](abandon_quest_error.md) | 参与者无法放弃任务时返回的错误。 |
| [quest](quest.md) | 一个可完成的目标。调用 Complete() 把任务标记为完成并触发 CompleteEvent。 |
| [quest_collection](quest_collection.md) | 任务参与关系的唯一事实来源（source of truth）。 |
| [quest_participant](quest_participant.md) | 任务参与者的抽象基类。 |
| [agent_quest_participant](agent_quest_participant.md) | 以代理（agent）为载体的任务参与者——玩家、NPC、AI 等都适用。 |
