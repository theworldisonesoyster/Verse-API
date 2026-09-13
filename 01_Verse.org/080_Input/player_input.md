---
name: player_input
slug: versedotorg/input/player_input
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/player_input
kind: class
module: /Verse.org/input
grade: A
depth: full
status: done
---

# player_input class <A>

> The per-player input manager. Get one for a player with 'GetPlayerInput', then use it to: Turn input mappings on or off for that player with 'AddInputMapping' / 'RemoveInputMapping'. Get the 'input_events' object for an 'input_action' with 'GetInputEvents', and subscribe to its events to react to that input. An input_action only generates events for a player while at least one input_mapping that references it is active on that player.
> 每个玩家一个的输入管理器：用 GetPlayerInput 获取，然后 AddInputMapping/RemoveInputMapping 开关该玩家的输入映射。

`using { /Verse.org/Input }`

## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [PreferredInputMethod](player_input_preferredinputmethod.md) | ?input_method | 玩家当前偏好的输入方式；在键鼠、手柄、触摸之间切换时更新。 |
| [AvailableInputDevices](player_input_availableinputdevices.md) | ?available_input_devices | 玩家当前可用的输入设备能力集合；设备连接/断开时实时更新。 |

### Functions
| Function Name | Description |
| [AddInputMapping](player_input_addinputmapping.md) | 把给定的 input_mapping 加到玩家身上，使其中的 input_action 得到处理并可触发事件。 |
| [RemoveInputMapping](player_input_removeinputmapping.md) | 把给定的 input_mapping 从玩家身上移除，其中的 input_action 不再处理、不再触发事件。 |
| [GetInputEvents](player_input_getinputevents.md) | 返回给定 input_action 的 input_events 对象，可绑定该动作的事件。 |
