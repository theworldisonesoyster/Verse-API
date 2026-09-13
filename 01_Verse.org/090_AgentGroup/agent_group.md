---
name: agent_group
slug: versedotorg/agentgroup/agent_group
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/agentgroup/agent_group
kind: function
module: /Verse.org/agentgroup
grade: B
depth: brief
status: done
---

# agent_group function <B>

> An agent group is defined as a set of agents that share a common ownership.This class stores agents and specific information about each member via the member_info type provided.
> 参数化构造：创建代理组。代理组是共享同一所有权的代理集合。

`using { /Verse.org/AgentGroup }`

```verse
agent_group<public>(member_info:member_info_interface):agent_group(member_info)
```

```verse
This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
```

## Parameters

agent_group 接受以下参数：
| Name | Type | Description |
| member_info | member_info_interface |  |

### Generated Class
agent_group 返回参数化类 agent_group(member_info)。

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
