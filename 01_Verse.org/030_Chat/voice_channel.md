---
name: voice_channel
slug: versedotorg/chat/voice_channel
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/chat/voice_channel
kind: function
module: /Verse.org/chat
grade: B
depth: brief
status: done
---

# voice_channel function <B>

> A voice_channel defines a group of agents who can communicate via voice chat. An agent can be a member of more than one voice_channel.Voice channels can accommodate 80 members of the channel's Group. Agents beyond this limit are not included in the chat.A chat participant in a voice_channel may be restricted from voice chat based on parental controls and/or user settings.
> 参数化构造：创建语音频道。语音频道定义一组可通过语音交流的代理；一个代理可同时属于多个频道，频道最多容纳 80 名成员，参与者也可能因家长控制/用户设置被限制语音。

`using { /Verse.org/Chat }`

```verse
voice_channel<public>(member_info:has_voice_member_info):voice_channel(member_info)
```

```verse
This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
```

## Parameters

voice_channel 接受以下参数：
| Name | Type | Description |
| member_info | has_voice_member_info |  |

### Generated Class
voice_channel 返回参数化类 voice_channel(member_info)。

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
