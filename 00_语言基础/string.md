---
name: string——字符串
slug: (补充)语言基础.string
url:
kind: class
module: /语言基础
grade: A
depth: full
status: done
---

# string——字符串 🟩【A级·常用】

> 字符串是 UTF-8 文本的内建类型；属于 Verse 语言内建。

## 这是什么

双引号字面量 `"..."` 即字符串。要点：

- **插值**：`"分数: {Score}"` 花括号内嵌任意表达式，是最常用输出手段。
- **连接**：`A + B` 拼接；重复拼接考虑 `Join`。
- 与 `[]char`（字符数组）互转：`ToUtf8[]`/`FromUtf8[]` 是可失败转换（官方 Print 的参数类型就是 `[]char`）。

## 最小示例

```verse
Name:string = "世界"
Msg := "你好, {Name}! {1 + 2}"      # 你好, 世界! 3
Joined := Join(array{"a", "b", "c"}, "-")   # a-b-c（Join 在 /Verse.org/Verse）
```

## 何时用 / 何时不用

- 用：日志、UI 文案（正式 UI 文案用 [message](../01_Verse.org/010_Verse/message.md) 做本地化）。
- 不用：大量拼接/高频修改的文本——每次拼接都生成新串。

## 常见坑

- 插值只认 `{表达式}`；想输出字面花括号需转义写法。
- 中文等多字节字符按"字符"而非"字节"处理时，注意与 `[]char` 转换的可失败性。

## 相关页面

- [Print](../01_Verse.org/010_Verse/print.md)
- [可失败表达式与failure](failure.md)
