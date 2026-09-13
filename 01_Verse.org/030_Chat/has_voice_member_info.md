---
name: has_voice_member_info
slug: versedotorg/chat/has_voice_member_info
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/chat/has_voice_member_info
kind: interface
module: /Verse.org
grade: B
depth: brief
status: done
---

> Used to specify permissions and other settings for a voice_channel.
> 用于为 voice_channel 指定权限等设置的接口。

`using { /Verse.org/Chat }`

## Exposed Interfaces

This interface exposes the following interfaces:（此接口暴露以下接口：）

| Name | Description |
|---|---|
| member_info_interface | 定义「可作为代理组成员信息」的接口。 |

## Members

This interface has data members, but no functions.（此接口只有数据成员，没有函数。）

### Data

| Data Member Name | Type | Description |
|---|---|---|
| [CanBroadcast](has_voice_member_info_canbroadcast.md) | ?logic | 决定参与者能否向频道发送语音消息。为 true 时，参与者仍能听到正在发言的成员，并在社交面板中看到相关用户。 |

## 补充说明

- 实现 [member_info_interface interface](member_info_interface.md) 后即可同时用于代理组与语音频道。
