---
name: play_animation_state
slug: fortnitedotcom/animation/playanimation/play_animation_state
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/animation/playanimation/play_animation_state
kind: enum
module: /Fortnite.com/animation/playanimation
grade: A
depth: full
status: done
---

# play_animation_state enumeration <A>

> The potential states of a play animation instance.
> 播放动画实例的可能状态。

`using { /Fortnite.com/Animation/PlayAnimation }`

## Enumerators

The play_animation_state 枚举包含以下枚举值：
| Name | Description |
| BlendingIn | 动画正在混合淡入。 |
| Playing | 动画已完成淡入、正在播放、尚未开始淡出。 |
| BlendingOut | 动画正在播放并正在淡出。 |
| Completed | 动画成功完成。 |
| Stopped | 动画被内部停止。 |
| Interrupted | 动画被外部中断。 |
| Error | 创建或播放期间发生错误。 |
