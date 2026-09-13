---
name: play_animation_instance
slug: fortnitedotcom/animation/playanimation/play_animation_instance
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/animation/playanimation/play_animation_instance
kind: class
module: /Fortnite.com/animation/playanimation
grade: A
depth: full
status: done
---

# play_animation_instance class <A>

> An animation instance created from play_animation_controller.Play that can be queried and manipulated.
> 由 play_animation_controller.Play 创建的动画实例，可查询与操控。

`using { /Fortnite.com/Animation/PlayAnimation }`

## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [CompletedEvent](play_animation_instance_completedevent.md) | listenable(payload) | 动画完成时触发的事件。 |
| [InterruptedEvent](play_animation_instance_interruptedevent.md) | listenable(payload) | 动画被打断时触发的事件。 |
| [BlendedInEvent](play_animation_instance_blendedinevent.md) | listenable(payload) | 动画完成混合淡出（blend out）时触发的事件。 |
| [BlendingOutEvent](play_animation_instance_blendingoutevent.md) | listenable(payload) | 动画开始混合淡出时触发的事件。 |

### Functions
| Function Name | Description |
| [GetState](play_animation_instance_getstate.md) | 返回动画播放状态。 |
| [Stop](play_animation_instance_stop.md) | 停止动画。 |
| [Await](play_animation_instance_await.md) | 辅助函数：等待动画完成或被打断。 |
| [IsPlaying](play_animation_instance_isplaying.md) | 辅助函数：状态为 Playing/BlendingIn/BlendingOut 时成功。 |
