---
name: Print (diagnostic 重载)
slug: versedotorg/verse/print-2
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/print-2
kind: function
module: /Verse.org/Verse
grade: S
depth: full
status: done
---

# Print function（diagnostic 重载）<S>

> Writes Message to a dedicated Print log while displaying it in Color on the client screen for Duration seconds. By default, Color is NamedColors.White and Duration is 2.0 seconds.
> 把 Message 写入专用的 Print 日志，同时在客户端屏幕上以 Color 颜色显示 Duration 秒。默认 Color 为 NamedColors.White，Duration 为 2.0 秒。本重载的 Message 为 diagnostic（诊断）类型。

`using { /Verse.org/Verse }`

```verse
Print<public>(Message:diagnostic, Duration:float, Color:color)<transacts>:void
```

## Parameters

Print takes the following parameters:（Print 接受以下参数：）

| Name | Type | Description |
|---|---|---|
| Message | diagnostic | 要输出的诊断对象。 |
| Duration | float | 在屏幕上显示的秒数。 |
| Color | color | 显示颜色，默认 NamedColors.White。 |

## Attributes, Specifiers, and Effects

`Print<public>(Message:diagnostic, Duration:float, Color:color)<transacts>` —— 标签：public / transacts，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Verse }

Print(ToDiagnostic("检查点到达"))
```

## 补充说明

- 日常调试用 [Print function](print.md) 主重载即可；diagnostic 相关见 [diagnostic class](diagnostic.md)。
