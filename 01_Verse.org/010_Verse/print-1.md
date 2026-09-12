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

# Print (message 重载) 🟦【S级·核心】

> Writes Message to a dedicated Print log while displaying it in Color.
> Print 的 message 版本：可打印**可本地化**的 message 对象。

## 签名

```verse
Print<public><native>(Message:message, Duration:float, Color:color)<transacts>:void
```

## 这是什么

与 [print](print.md) 行为一致，区别是参数类型为 [message](message.md)——本地化文本对象（`Localize` 构造）。当你想调试"玩家实际看到的本地化文本"时用它。

## 最小示例

```verse
using { /Verse.org/Verse }

Greeting:message = Localize("hello.key", ["Name"], array["World"])
Print(Greeting)
```

## 相关页面

- [Print](print.md) —— 主版本
- [message](message.md)
