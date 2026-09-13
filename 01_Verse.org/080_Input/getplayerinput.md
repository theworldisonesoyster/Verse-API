---
name: GetPlayerInput
slug: versedotorg/input/getplayerinput
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/getplayerinput
kind: function
module: /Verse.org/input
grade: A
depth: full
status: done
---

# GetPlayerInput function <A>

> Access input-related data and settings for a player.
> 访问玩家的输入相关数据与设置。

`using { /Verse.org/Input }`

```verse
GetPlayerInput<public><native>(Player:player)<transacts><decides>:player_input
```

## Parameters

GetPlayerInput 接受以下参数：
| Name | Type | Description |
| Player | player |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
if (PI := GetPlayerInput[P]):
    PI.AddInputMapping(MyMapping)
```
