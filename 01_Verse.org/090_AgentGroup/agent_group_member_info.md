---
name: agent_group(member_info)
slug: versedotorg/agentgroup/agent_group/agent_group(member_info)
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/agentgroup/agent_group/agent_group(member_info)
kind: class
module: /Verse.org
grade: B
depth: brief
status: done
---

> An agent group is defined as a set of agents that share a common ownership.
> 代理组：共享同一所有权的代理集合。此类为该组存储代理与其他数据。

`using { /Verse.org/AgentGroup }`

## Exposed Interfaces

This class exposes the following interfaces:（此类暴露以下接口：）

| Name | Description |
|---|---|
| member_info_interface | 定义「可作为代理组成员信息」的接口。 |

## Members

### Functions

| Function Name | Description |
|---|---|
| AddMember | 尝试把给定代理加入此代理组；返回一个 result——成功或返回错误。 |
| RemoveMember | 尝试把给定代理移出此代理组；返回一个 result——成功或返回错误。 |
| GetMembers | 获取此代理组的成员及其成员信息。 |
| JoinEvent | 每当有代理成功加入此代理组时触发；载荷为加入的代理及其 member_info。 |
| LeaveEvent | 每当有代理成功离开此代理组时触发；载荷为离开的代理及其 member_info。 |
| MemberInfoUpdatedEvent | 每当某代理的 MemberInfo 类被重新实例化时触发；载荷为被更新的代理及其新 member_info。 |

## 相关页面

- [member_info_interface interface](member_info_interface.md)
- Chat 模块的 [voice_channel](../030_Chat/voice_channel_member_info.md) 使用同一套成员信息机制。
