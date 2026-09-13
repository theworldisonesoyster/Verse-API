---
name: SpawnProp
slug: fortnitedotcom/devices/spawnprop
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/spawnprop
kind: function
module: /Fortnite.com/devices
grade: A
depth: full
status: done
---

# SpawnProp function <A>

> Spawns a creative_prop at the specified Position and Rotation. Position and Rotation units are in cm. The relative scale defined in the creative_prop_asset will be applied upon spawn. Returns tuple: 0: Instance of a creative_prop. False if no creative_prop could be created. See spawn_prop_result for failure cases. 1: Success or failure results.
> 创意设备（Devices 索引）。

`using { /Fortnite.com/Devices }`

```verse
SpawnProp<public><native>(Asset:creative_prop_asset, Position:vector3, Rotation:rotation)<transacts>:(?creative_prop, spawn_prop_result)
```

## Parameters

SpawnProp 接受以下参数：
| Name | Type | Description |
| Asset | creative_prop_asset |  |
| Position | vector3 |  |
| Rotation | rotation |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
