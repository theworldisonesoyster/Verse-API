---
name: logic与void
slug: (补充)语言基础.logic_void
url:
kind: class
module: /语言基础
grade: B
depth: brief
status: done
---

# logic 与 void 🟨【B级·进阶】

> 两个基础类型：logic 是"真/假"，void 是"无返回值"；官网 API Reference 无单设页面。

## 这是什么

- `logic`：只有 `true` / `false`。注意它**与失败上下文不同**——`logic` 是值，失败是"路不通"。API 里很多状态查询返回 logic（如 `IsCrouching()`），而"可失败查询"（`IsCrouching[]`）走失败分支，两者别混。
- `void`：函数不返回值时的返回类型，如 `Sleep(1.0):void`。

## 最小示例

```verse
IsReady:logic = true
if (IsReady?):      # logic 可用 ? 转为可失败判断
    Print("ready")
```

## 常见坑

- `logic` 参与失败上下文要写 `If?`；直接 `if (IsReady)` 不合法。
- "返回 logic 的函数"与"`<decides>` 可失败函数"在 API 页签名一眼可辨：后者带 `<decides>`。

## 相关页面

- [可失败表达式与failure](failure.md)
