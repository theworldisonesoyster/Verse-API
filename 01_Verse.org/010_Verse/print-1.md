---
name: Print (message 重载)
slug: versedotorg/verse/print-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/print-1
kind: function
module: /Verse.org/Verse
grade: S
depth: full
status: done
---

# Print function（message 重载）🟦【S级·核心】

> Writes Message to a dedicated Print log while displaying it in Color on the client screen for Duration seconds. By default, Color is NamedColors.White and Duration is 2.0 seconds.
> 把 Message 写入专用的 Print 日志，同时在客户端屏幕上以 Color 颜色显示 Duration 秒。默认 Color 为 NamedColors.White，Duration 为 2.0 秒。本重载的 Message 为 message（可本地化文本）类型。

`using { /Verse.org/Verse }`

```verse
Print<public><native>(Message:message, Duration:float, Color:color)<transacts>:void
```

## Parameters

Print takes the following parameters:（Print 接受以下参数：）

| Name | Type | Description |
|---|---|---|
| Message | message | 要输出的可本地化文本。 |
| Duration | float | 在屏幕上显示的秒数。 |
| Color | color | 显示颜色，默认 NamedColors.White。 |

## Attributes, Specifiers, and Effects

`Print<public><native>(Message:message, Duration:float, Color:color)<transacts>` —— 标签：public / native / transacts，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Verse }

Greeting:message = Localize("hello.key", ["Name"], array["World"])
Print(Greeting)
```

## 补充说明

- 与 [Print function](print.md) 行为一致，区别是接受 message 对象；相关类型见 [message class](message.md)。
