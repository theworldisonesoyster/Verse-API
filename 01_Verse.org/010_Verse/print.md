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

# Print 🟦【S级·核心】

> Writes Message to a dedicated Print log while displaying it in Color.
> 把消息写入专用的 Print 日志，并以指定颜色显示出来。

## 签名

```verse
Print<public><native>(Message:[]char, Duration:float, Color:color)<transacts>:void
```

另有两个重载（各占一页）：`Message:message`（[print-1](print-1.md)）与 `Message:diagnostic`（[print-2](print-2.md)）。

## 这是什么

Verse 里最常用的调试/反馈手段。消息显示在游戏画面的 Print 日志（UEFN 内按 `~` 或输出窗口查看）。参数 `Duration` 控制显示时长，`Color` 控制颜色（配合 `/Verse.org/Colors` 的常量，如 `NamedColors.Red`）。

字符串字面量会自动转成 `[]char`，所以 `Print("hello")` 直接可用；格式化用字符串插值 `"分数: {Score}"`。

## 最小示例

```verse
using { /Verse.org/Verse }
using { /Verse.org/Colors }
using { /Verse.org/Colors/NamedColors }

Score := 42
Print("分数: {Score}")                                   # 普通输出
Print("出错了!", Duration := 5.0, Color := NamedColors.Red)  # 红字显示 5 秒
```

## 何时用 / 何时不用

- 用：调试、学习、临时反馈。
- 不用：面向玩家的正式 UI 文案——用 widget/message；成体系日志用 `/UnrealEngine.com/Temporary/Diagnostics` 的 log。

## 常见坑

- Print 本身在开发版 UI 才可见，发行给玩家后看不到——别用它做玩法提示。
- 高频循环里狂 Print 会拖慢性能，调试完记得删。

## 相关页面

- [print-1](print-1.md) / [print-2](print-2.md) —— message / diagnostic 重载
- [string——字符串](../../00_语言基础/string.md) —— 插值语法
- [NamedColors](../120_Colors/_overview.md) —— 颜色常量
