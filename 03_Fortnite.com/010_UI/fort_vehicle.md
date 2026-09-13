---
name: fort_vehicle
slug: fortnitedotcom/vehicles/fort_vehicle
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/vehicles/fort_vehicle
kind: interface
module: /Fortnite.com/vehicles
grade: B
depth: brief
status: done
---

# fort_vehicle interface <B>

> Main API implemented by Fortnite vehicles.
> 由堡垒之夜载具实现的主 API。

`using { /Fortnite.com/Vehicles }`

## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| positional | 由对象实现，允许读取位置信息。 |
| healthful | 由拥有生命状态、可被淘汰的堡垒之夜对象实现。 |
| damageable | 由可被伤害的堡垒之夜对象实现。 |
| game_action_causer | 由可作为游戏动作事件（如伤害、治疗）载体传递的堡垒之夜对象实现，例如玩家、载具或武器。事件监听器常用 game_action_causer 传递「什么武器造成了伤害」等附加信息，供任务系统或玩法事件逻辑使用。 |
| showable | 由「实例可切换显示/隐藏」的类实现。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [Speed](fort_vehicle_speed.md) | ?float | 载具当前速度（米/秒）。 |
| [BoostRemaining](fort_vehicle_boostremaining.md) | ??float | 载具的推进（boost）状态；使用推进的载具该值在 0.0 与 BoostCapacity 之间，否则为 false。 |
| [BoostCapacity](fort_vehicle_boostcapacity.md) | ??float | 载具的最大推进容量；使用推进的载具该值在 1.0 与 Inf 之间，否则为 false。 |

### Functions
| Function Name | Description |
| [IsOnGround](fort_vehicle_isonground.md) | 此 fort_vehicle 在地面上则成功。 |
| [IsInAir](fort_vehicle_isinair.md) | 此 fort_vehicle 在空中则成功。 |
| [IsInWater](fort_vehicle_isinwater.md) | 此 fort_vehicle 在水中则成功。 |
| GetPassengers |  | 返回载具上的全部乘客。 | [GetOccupants](fort_vehicle_getoccupants.md) | 返回当前占据载具的全部代理数组。 |
| [GetDrivers](fort_vehicle_getdrivers.md) | 返回载具当前全部驾驶员的数组（通常只有一个代理）。 |
| [GetFuelRemaining](fort_vehicle_getfuelremaining.md) | 返回载具油量状态；用油的载具该值在 0.0 与 GetFuelCapacity 之间，否则为 -1.0。 |
| [GetFuelCapacity](fort_vehicle_getfuelcapacity.md) | 返回载具最大油箱容量；用油的载具该值在 1.0 与 Inf 之间，否则为 -1.0。 |
| [TeleportTo](fort_vehicle_teleportto.md) | 把 fort_vehicle 瞬移到指定的位置与旋转。 |
| [RemoveAgent](fort_vehicle_removeagent.md) | 把指定代理移下载具；代理不在车上则失败。 |
| [RemoveAll](fort_vehicle_removeall.md) | 移下载具上的所有代理。 |
| [AddAgent](fort_vehicle_addagent.md) | 尝试把代理加进 fort_vehicle；没有空座或无法安置则失败。 |
| [GetSeats](fort_vehicle_getseats.md) | 返回 fort_vehicle 中所有 fort_vehicle_seat 的数组。 |
