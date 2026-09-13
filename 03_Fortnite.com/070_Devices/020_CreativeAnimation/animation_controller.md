---
name: animation_controller
slug: fortnitedotcom/devices/creativeanimation/animation_controller
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creativeanimation/animation_controller
kind: class
module: /Fortnite.com/devices/creativeanimation
grade: B
depth: brief
status: done
---

# animation_controller class <B>

> Used to move and animate the position of creative_prop objects.
> - See creative_prop.GetAnimationController for information on acquiring an instance of an animation_controller for a given creative_prop.
> - See SetAnimation for details on authoring movement and animations.
> 创意设备（Devices 索引）。

`using { /Fortnite.com/Devices/CreativeAnimation }`

## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| KeyframeReachedEvent | listenable(payload) | 每到达一个关键帧时触发。回调参数（关键帧序号:int, 是否反向:logic)。载荷中的序号一般在 [1, NumDeltaKeyframes]；PingPong 动画中反向播放的最后一个关键帧记为 0——因为 SetAnimation 接收的是增量关键帧，而此事件通知的是「到达了某个特定关键帧」。 |
| MovementCompleteEvent | listenable(payload) | 整个动画完成时触发；仅对 OneShot（单次）动画触发。 |
| StateChangedEvent | listenable(payload) | 状态变化时触发；用 GetState 获取新状态。 |

### Functions
| Function Name | Description |
| AwaitNextKeyframe | 在调用处挂起，直到下一个 keyframe_delta 完成；动画被中止或未播放时也会返回。若代码需要根据 AwaitNextKeyframe 的返回原因走不同分支，参见 await_next_keyframe_result。 |
| Play | 开始或恢复动画播放。 |
| Pause | 若动画正在播放则暂停。 |
| Stop | 停止播放并把动画重置到第一个关键帧，同时重置道具变换。动画处于 Playing 或 Paused 状态时调用有效。 |
| GetState | 返回此 animation_controller 的当前状态。 |
| IsValid | 若此 animation_controller 的目标仍有效则成功（即目标尚未通过 Dispose 或任何外部系统被销毁）。 |
| SetAnimation | 为 animation_controller 设置动画。动画按 Keyframes 给出的顺序处理；控制细节见 keyframe_delta 与 animation_mode 的说明。 |
