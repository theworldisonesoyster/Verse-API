---
name: creative_object
slug: fortnitedotcom/devices/creative_object
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object
kind: class
module: /Fortnite.com/devices
grade: A
depth: full
status: done
---

# creative_object class <A>

> Base class for creative devices and props.
> 创意对象接口的类表示。

`using { /Fortnite.com/Devices }`

## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| creative_object_interface |  |


## Members

只有函数，没有数据成员。

### Functions
| Function Name | Description |
| GetTransform | 返回 creative_object 的变换（厘米）。若对象可能已在玩法中被销毁，调用前必须检查 creative_object.IsValid，否则会产生运行时错误。 |
| TeleportTo | 将 creative_object 瞬移到指定的 Position 与 Rotation。 |
| TeleportTo | 将 creative_object 瞬移到 Transform 指定的位置，同时相应地应用旋转与缩放。 |
| MoveTo | 在指定的秒数内把 creative_object 移动到指定的 Position 与 Rotation。若对象当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| MoveTo | 在指定的秒数内把 creative_object 移动到指定的 Transform。若对象当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| GetGlobalTransform | 获取此对象的全局变换。 |
| SetGlobalTransform | 设置此对象的全局变换。 |
| TeleportTo | 将 creative_device 瞬移到 Transform 指定的位置，同时相应地应用旋转与缩放。 |
| MoveTo | 在指定的秒数内把 creative_device 移动到指定的 Transform。若设备当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
