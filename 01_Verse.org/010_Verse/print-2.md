---
name: Print (diagnostic 重载)
slug: versedotorg/verse/print-2
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/print-2
kind: function
module: /Verse.org/Verse
grade: S
depth: brief
status: done
---

# Print (diagnostic 重载) 🟦【S级·核心】

> Writes Message to a dedicated Print log while displaying it in Color.
> Print 的 diagnostic 版本：可直接打印 [diagnostic](diagnostic.md) 对象。

## 签名

```verse
Print<public>(Message:diagnostic, Duration:float, Color:color)<transacts>:void
```

## 这是什么

与 [Print](print.md) 行为一致，接受 diagnostic（通常配合 `ToDiagnostic` 或诊断管道使用）。日常调试用主版本即可。

## 相关页面

- [Print](print.md)
- [diagnostic](diagnostic.md)
