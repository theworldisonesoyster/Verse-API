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
| [CanBeDamaged](creative_prop_canbedamaged.md) | ?logic | 启用/禁用此道具可否被伤害；禁用后创意道具不会受到攻击伤害。 |

### Functions
| Function Name | Description |
| [ApplyAngularImpulse](creative_prop_applyangularimpulse.md) | 对 creative_prop 施加角冲量（单位：牛顿·米·秒）。物理被禁用时无效果。 |
| [ApplyForce](creative_prop_applyforce.md) | 对 creative_prop 施加力（单位：牛顿）。物理被禁用时无效果。 |
| [ApplyLinearImpulse](creative_prop_applylinearimpulse.md) | 对 creative_prop 施加线冲量（单位：牛顿·秒）。物理被禁用时无效果。 |
| [ApplyTorque](creative_prop_applytorque.md) | 对 creative_prop 施加扭矩（单位：牛顿·米）。物理被禁用时无效果。 |
| [Dispose](creative_prop_dispose.md) | 销毁 creative_prop 并将其从岛屿移除。 |
| [GetAngularVelocity](creative_prop_getangularvelocity.md) | 返回 creative_prop 的角速度（弧度/秒）。 |
| [GetDynamic](creative_prop_getdynamic.md) | 获取 creative_prop 是否为动态（受物理函数影响）。 |
| [GetGlobalTransform](creative_prop_getglobaltransform.md) | 获取此对象的全局变换。 |
| [GetLinearVelocity](creative_prop_getlinearvelocity.md) | 返回 creative_prop 的线速度（米/秒）。 |
| [GetMass](creative_prop_getmass.md) | 返回 creative_prop 的质量（千克）。 |
| [GetTransform](creative_prop_gettransform.md) | 返回 creative_object 的变换（厘米）。若对象可能已在玩法中被销毁，调用前必须检查 creative_object.IsValid，否则会产生运行时错误。 |
| [Hide](creative_prop_hide.md) | 在世界中隐藏 creative_prop 并禁用碰撞。 |
| [IsDisposed](creative_prop_isdisposed.md) | 此对象已通过 Dispose() 或外部系统被销毁则成功。 |
| [IsValid](creative_prop_isvalid.md) | 此对象尚未通过 Dispose() 或外部系统被销毁则成功。 |
| [MoveTo](creative_prop_moveto.md) | 在指定的秒数内把 creative_object 移动到指定的 Position 与 Rotation。若对象当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| [MoveTo](creative_prop_moveto.md) | 在指定的秒数内把 creative_object 移动到指定的 Transform。若对象当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| [MoveTo](creative_prop_moveto.md) | 在指定的秒数内把 creative_device 移动到指定的 Transform。若设备当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| [SetAngularVelocity](creative_prop_setangularvelocity.md) | 设置 creative_prop 的角速度（弧度/秒）。物理被禁用时无效果。 |
| [SetDynamic](creative_prop_setdynamic.md) | 设置 creative_prop 是否为动态（受物理函数影响）。物理被禁用或道具没有 FortPhysicsComponent 时无效果。 |
| [SetGlobalTransform](creative_prop_setglobaltransform.md) | 设置此对象的全局变换。 |
| [SetLinearVelocity](creative_prop_setlinearvelocity.md) | 设置 creative_prop 的线速度（米/秒）。物理被禁用时无效果。 |
| [SetMaterial](creative_prop_setmaterial.md) | 更改此实例所用网格的材质。可指定材质应用到的网格元素索引；不指定则默认为 0 号网格元素。 |
| [SetMesh](creative_prop_setmesh.md) | 更改此实例使用的网格。 |
| [Show](creative_prop_show.md) | 在世界中显示 creative_prop 并启用碰撞。 |
| [TeleportTo](creative_prop_teleportto.md) | 将 creative_object 瞬移到指定的 Position 与 Rotation。 |
| [TeleportTo](creative_prop_teleportto.md) | 将 creative_object 瞬移到 Transform 指定的位置，同时相应地应用旋转与缩放。 |
| [TeleportTo](creative_prop_teleportto.md) | 将 creative_device 瞬移到 Transform 指定的位置，同时相应地应用旋转与缩放。 |
