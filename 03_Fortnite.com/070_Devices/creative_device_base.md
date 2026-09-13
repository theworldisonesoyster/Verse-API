---
name: creative_device_base
slug: fortnitedotcom/devices/creative_device_base
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_device_base
kind: class
module: /Fortnite.com/devices
grade: A
depth: full
status: done
---

# creative_device_base class <A>

> Base class for creative_device.
> 创意设备（Devices 索引）。

`using { /Fortnite.com/Devices }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| creative_object | 创意设备与道具的基类。 |


## Members

只有函数，没有数据成员。

### Functions
| Function Name | Description |
| [GetGlobalTransform](creative_device_base_getglobaltransform.md) | 获取此对象的全局变换。 |
| [GetTransform](creative_device_base_gettransform.md) | 返回 creative_object 的变换（厘米）。若对象可能已在玩法中被销毁，调用前必须检查 creative_object.IsValid，否则会产生运行时错误。 |
| [MoveTo](creative_device_base_moveto.md) | 在指定的秒数内把 creative_object 移动到指定的 Position 与 Rotation。若对象当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| [MoveTo](creative_device_base_moveto.md) | 在指定的秒数内把 creative_object 移动到指定的 Transform。若对象当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| [MoveTo](creative_device_base_moveto.md) | 在指定的秒数内把 creative_device 移动到指定的 Transform。若设备当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| [SetGlobalTransform](creative_device_base_setglobaltransform.md) | 设置此对象的全局变换。 |
| [TeleportTo](creative_device_base_teleportto.md) | 将 creative_object 瞬移到指定的 Position 与 Rotation。 |
| [TeleportTo](creative_device_base_teleportto.md) | 将 creative_object 瞬移到 Transform 指定的位置，同时相应地应用旋转与缩放。 |
| [TeleportTo](creative_device_base_teleportto.md) | 将 creative_device 瞬移到 Transform 指定的位置，同时相应地应用旋转与缩放。 |
