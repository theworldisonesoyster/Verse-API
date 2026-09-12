---
name: Print
slug: versedotorg/verse/print
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/print
kind: function
module: /Verse.org/Verse
grade: S
depth: full
status: done
---

# Print function 🟦【S级·核心】

> Writes Message to a dedicated Print log while displaying it in Color on the client screen for Duration seconds. By default, Color is NamedColors.White and Duration is 2.0 seconds.
> 把 Message 写入专用的 Print 日志，同时在客户端屏幕上以 Color 颜色显示 Duration 秒。默认 Color 为 NamedColors.White（白色），Duration 为 2.0 秒。

`using { /Verse.org/Verse }`

```verse
Print<public><native>(Message:[]char, Duration:float, Color:color)<transacts>:void
```

## Parameters

Print takes the following parameters:（Print 接受以下参数：）

| Name | Type | Description |
|---|---|---|
| Message | []char | 要输出的消息（字符数组；字符串字面量可直接传入）。 |
| Duration | float | 在屏幕上显示的秒数。 |
| Color | color | 显示颜色，默认 NamedColors.White。 |

## Attributes, Specifiers, and Effects

`Print<public><native>(Message:[]char, Duration:float, Color:color)<transacts>` —— 标签：public / native / transacts，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Verse }
using { /Verse.org/Colors }
using { /Verse.org/Colors/NamedColors }

Score := 42
Print("分数: {Score}")                                    # 白色显示 2 秒
Print("出错了!", Duration := 5.0, Color := NamedColors.Red)  # 红色显示 5 秒
```

## 补充说明

- Print 输出进专用 Print 日志（UEFN 内查看），是调试与学习的主力工具；面向玩家的正式文案请用 UI/message 体系。
- 另有两个重载：[Print (message 重载)](print-1.md)、[Print (diagnostic 重载)](print-2.md)。
