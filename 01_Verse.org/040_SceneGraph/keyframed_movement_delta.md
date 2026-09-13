---
name: keyframed_movement_delta
slug: versedotorg/scenegraph/keyframedmovement/keyframed_movement_delta
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/keyframedmovement/keyframed_movement_delta
kind: class
module: /Verse.org/scenegraph/keyframedmovement
grade: B
depth: brief
status: done
---

# keyframed_movement_delta class <B>

> Represents a change in pose and scale over a duration.
> 表示一段时间内姿态与缩放的变化量。

`using { /Verse.org/SceneGraph/KeyframedMovement }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| Transform | transform | 表示相对上一个关键帧（或动画初始位置）的变换变化量；Translation 与 Scale 按叠加方式解释。 |
| Duration | float | 此关键帧的时长（秒）。 |
| Easing | easing_function | 播放使用的缓动函数。 |
