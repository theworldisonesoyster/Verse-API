---
name: fort_vehicle_seat
slug: fortnitedotcom/vehicles/fort_vehicle_seat
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/vehicles/fort_vehicle_seat
kind: class
module: /Fortnite.com/vehicles
grade: B
depth: brief
status: done
---

# fort_vehicle_seat class <B>

> Represents a seat in a fort_vehicle.
> 表示 fort_vehicle 中的一个座位。

`using { /Fortnite.com/Vehicles }`

## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [Occupant](fort_vehicle_seat_occupant.md) | ??agent | 当前占据此座位的代理（如有）。 |
| [Vehicle](fort_vehicle_seat_vehicle.md) | ?fort_vehicle | 此座位所属的 fort_vehicle。 |

### Functions
| Function Name | Description |
| [IsDriverSeat](fort_vehicle_seat_isdriverseat.md) | 这是驾驶座则成功。 |
| [SetOccupant](fort_vehicle_seat_setoccupant.md) | 尝试让 Agent 坐入此座位；座位被占或无法入座则失败。把占位者设为 false 会移除已入座的代理。 |
