---
name: AgentGroup module
slug: versedotorg/agentgroup
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/agentgroup
kind: module
module: /versedotorg
grade: B
depth: brief
status: done
---

# AgentGroup module <B>

代理组：把一组代理（agent）组织为共享同一所有权的分组，常用于聊天/语音频道成员管理。

## Classes and Structs

| Name | Description |
|---|---|
| [add_member_error](add_member_error.md) | agent_group.AddMember 返回的所有错误的基类。 |
| [remove_member_error](remove_member_error.md) | agent_group.RemoveMember 返回的所有错误的基类。 |

## Interfaces

| Name | Description |
|---|---|
| [member_info_interface](member_info_interface.md) | 定义「可作为代理组成员信息」的接口。 |

## Functions

| Name | Description |
|---|---|
| [agent_group_interface](agent_group_interface.md) | 定义「提供代理组」能力的接口。 |
| [agent_group](agent_group.md) | 参数化构造：创建代理组。代理组是共享同一所有权的代理集合。 |
