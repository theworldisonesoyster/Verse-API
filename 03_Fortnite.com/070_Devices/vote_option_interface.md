---
name: vote_option_interface
slug: fortnitedotcom/devices/vote_option_interface
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/vote_option_interface
kind: interface
module: /Fortnite.com/devices
grade: B
depth: brief
status: done
---

# vote_option_interface interface <B>

> Represents an individual choice in a poll. For example, in a poll “What to have for lunch?” an option might be “Tacos” Tracks how many times each agent has voted for this option. An option is associated with only one group device (or “poll”) via an internal ID.
> 投票选项接口。

`using { /Fortnite.com/Devices }`

## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| CastVoteEvent | listenable(payload) | 「agent」投票时触发。 |
| WinVoteEvent | listenable(payload) | 此选项赢得投票时触发。 |

### Functions
| Function Name | Description |
| CastVote | 尝试为 Agent 投票。若投票代理还有剩余票数且投票组已开始投票，则投票成功；代理没有剩余票数或投票未开始则失败。 |
| GetVoteCount | 返回此选项获得的总票数。 |
| GetVoteGroup | 返回此选项对应的组设备（如有）；选项不在组中，或没有同 ID 的对应组设备则失败。 |
| HasAgentVoted | Agent 已为此选项投票则成功，否则失败。 |
| GetOptionDescription | 玩家选择选项时展示给它的文本。 |
