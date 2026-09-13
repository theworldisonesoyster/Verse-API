---
name: creative_prop
slug: fortnitedotcom/devices/creative_prop
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop
kind: class
module: /Fortnite.com/devices
grade: A
depth: full
status: done
---

# creative_prop class <A>

> A Fortnite prop that has been placed or spawned in the island.
> 创意道具：场景中的物件。

`using { /Fortnite.com/Devices }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| creative_object | 创意设备与道具的基类。 |


## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| invalidatable | 由「实例可能在运行时失效」的类实现。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| CanBeDamaged | ?logic | 启用/禁用此道具可否被伤害；禁用后创意道具不会受到攻击伤害。 |

### Functions
| Function Name | Description |
| ApplyAngularImpulse | 对 creative_prop 施加角冲量（单位：牛顿·米·秒）。物理被禁用时无效果。 |
| ApplyForce | 对 creative_prop 施加力（单位：牛顿）。物理被禁用时无效果。 |
| ApplyLinearImpulse | 对 creative_prop 施加线冲量（单位：牛顿·秒）。物理被禁用时无效果。 |
| ApplyTorque | 对 creative_prop 施加扭矩（单位：牛顿·米）。物理被禁用时无效果。 |
| Dispose | 销毁 creative_prop 并将其从岛屿移除。 |
| GetAngularVelocity | 返回 creative_prop 的角速度（弧度/秒）。 |
| GetDynamic | 获取 creative_prop 是否为动态（受物理函数影响）。 |
| GetGlobalTransform | 获取此对象的全局变换。 |
| GetLinearVelocity | 返回 creative_prop 的线速度（米/秒）。 |
| GetMass | 返回 creative_prop 的质量（千克）。 |
| GetTransform | 返回 creative_object 的变换（厘米）。若对象可能已在玩法中被销毁，调用前必须检查 creative_object.IsValid，否则会产生运行时错误。 |
| Hide | 在世界中隐藏 creative_prop 并禁用碰撞。 |
| IsDisposed | 此对象已通过 Dispose() 或外部系统被销毁则成功。 |
| IsValid | 此对象尚未通过 Dispose() 或外部系统被销毁则成功。 |
| MoveTo | 在指定的秒数内把 creative_object 移动到指定的 Position 与 Rotation。若对象当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| MoveTo | 在指定的秒数内把 creative_object 移动到指定的 Transform。若对象当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| MoveTo | 在指定的秒数内把 creative_device 移动到指定的 Transform。若设备当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| SetAngularVelocity | 设置 creative_prop 的角速度（弧度/秒）。物理被禁用时无效果。 |
| SetDynamic | 设置 creative_prop 是否为动态（受物理函数影响）。物理被禁用或道具没有 FortPhysicsComponent 时无效果。 |
| SetGlobalTransform | 设置此对象的全局变换。 |
| SetLinearVelocity | 设置 creative_prop 的线速度（米/秒）。物理被禁用时无效果。 |
| SetMaterial | 更改此实例所用网格的材质。可指定材质应用到的网格元素索引；不指定则默认为 0 号网格元素。 |
| SetMesh | 更改此实例使用的网格。 |
| Show | 在世界中显示 creative_prop 并启用碰撞。 |
| TeleportTo | 将 creative_object 瞬移到指定的 Position 与 Rotation。 |
| TeleportTo | 将 creative_object 瞬移到 Transform 指定的位置，同时相应地应用旋转与缩放。 |
| TeleportTo | 将 creative_device 瞬移到 Transform 指定的位置，同时相应地应用旋转与缩放。 |
