---
name: Chat module
slug: versedotorg/chat
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/chat
kind: module
module: /versedotorg
grade: B
depth: brief
status: done
---

# Chat module <B>

语音/文本聊天频道管理：创建频道、指定成员权限、处理加/退频道错误。

## Classes and Structs

| Name | Description |
|---|---|
| [add_channel_error](add_channel_error.md) | 通过 AddChatChannel 添加频道失败时返回的错误。 |
| [remove_channel_error](remove_channel_error.md) | 通过 RemoveChatChannel 移除频道失败时返回的错误。 |

## Interfaces

| Name | Description |
|---|---|
| [has_voice_member_info](has_voice_member_info.md) | 用于为 voice_channel 指定权限等设置的接口（如是否可发言）。 |

## Functions

| Name | Description |
|---|---|
| [chat_channel](chat_channel.md) | 参数化构造：按 member_info 类型创建文本聊天频道。 |
| [voice_channel](voice_channel.md) | 参数化构造：创建语音频道。语音频道定义一组可通过语音交流的代理；一个代理可同时属于多个频道，频道最多容纳 80 名成员，参与者也可能因家长控制/用户设置被限制语音。 |
