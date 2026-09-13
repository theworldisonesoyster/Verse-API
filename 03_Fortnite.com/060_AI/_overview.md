---
name: AI module
slug: fortnitedotcom/ai
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai
kind: module
module: /fortnitedotcom
grade: B
depth: brief
status: done
---

# AI module <B>

AI 相关：NPC/Guard 行为与感知组件、导航目标、Sidekick 伙伴，以及导航/动作的结果与错误类型。

## Classes and Structs

| Name | Description |
|---|---|
| [equipped_sidekick_component](equipped_sidekick_component.md) | 管理代理已装备 Sidekick（伙伴）专属功能的组件。 |
| [spark_mode_component](spark_mode_component.md) | 管理支持 Spark 模式的实体的组件：Spark 模式会把实体变作漂浮的火花。 |
| [guard_actions_component](guard_actions_component.md) | 堡垒之夜 Guard（守卫）的 AI 行为管理。 |
| [guard_awareness_component](guard_awareness_component.md) | 堡垒之夜 Guard 的感知管理。 |
| [navigation_target](navigation_target.md) | 导航目标。 |
| [npc_actions_component](npc_actions_component.md) | 堡垒之夜 NPC 的 AI 行为管理。 |
| [npc_awareness_component](npc_awareness_component.md) | 堡垒之夜 NPC 的感知管理。 |
| [npc_behavior](npc_behavior.md) | 继承它来创建自定义 NPC 行为。npc_behavior 可在 CharacterDefinition 资产或 npc_spawner_device 中为角色指定。 |
| [npc_target_info](npc_target_info.md) | 关于被感知目标的信息。 |
| [sidekick_component](sidekick_component.md) | 管理所有 Sidekick 类型共享功能的组件。 |
| [npc_sidekick_component](npc_sidekick_component.md) | 管理 NPC Sidekick 专属功能的组件。 |

## Interfaces

| Name | Description |
|---|---|
| [focus_interface](focus_interface.md) | 关注（focus）能力接口。 |
| [fort_leashable](fort_leashable.md) | 可被拴留（leash，限制活动范围）的接口。 |
| [navigatable](navigatable.md) | 可寻路（navigatable）接口。 |

## Functions

| Name | Description |
|---|---|
| [MakeNavigationTarget](makenavigationtarget.md) | 从任意位置生成 navigation_target。 |
| [MakeNavigationTarget](makenavigationtarget-1.md) | 从任意位置生成 navigation_target（重载）。 |
| [MakeNavigationTarget](makenavigationtarget-2.md) | 从代理（agent）生成 navigation_target。 |

## Enumerations

| Name | Description |
|---|---|
| [ai_action_error_type](ai_action_error_type.md) | AI 动作失败的结果类型。 |
| [navigation_result](navigation_result.md) | 导航请求的结果。 |
| [navigation_action_error_type](navigation_action_error_type.md) | 导航动作失败类型。 |
| [navigation_action_success_type](navigation_action_success_type.md) | 导航动作成功类型。 |
| [movement_type](movement_type.md) | 移动类型枚举。 |
| [guard_alert_level](guard_alert_level.md) | 堡垒之夜 Guard 的各级警戒级别。 |
| [sidekick_mood](sidekick_mood.md) | Sidekick 的情绪列表——情绪会改变其动画表现。 |
| [sidekick_reaction](sidekick_reaction.md) | Sidekick 可播放的反应动作集合。 |

## Submodules

| Name | Description |
|---|---|
| [movement_types](010_movement_types/_overview.md) | 移动类型常量（行走/奔跑）。 |
