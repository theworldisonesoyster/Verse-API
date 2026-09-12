---
name: 元组与子类型
slug: (补充)语言基础.tuple_subtype
url:
kind: class
module: /语言基础
grade: B
depth: brief
status: done
supplement: true
---

# 元组与子类型 🟨【B级·进阶】〔补充·非官网镜像〕

> 元组把几个值打包成一个；子类型 `subtype` 描述"某类型的子集"。官网 API Reference 无单设页面。

## 这是什么

- **元组**：`(A, B)` 类型写作 `tuple(A, B)`，事件载荷常见（如 fort_character 的蹲起事件回传 `(角色, 是否蹲)`）。
- **子类型**：`where` 子句约束类型参数，如 `t:comparable` 表示"任何可比较类型"——这是泛型 API（Min/Max、event(t)）的基础。

## 最小示例

```verse
Pair := (1, "one")                  # tuple(int, string)
N:int = Pair(0)                     # 按位置取分量
M := event(tuple(agent, logic))     # 元组作事件载荷
```

## 常见坑

- 元组按位置而非名字取值，分量多时可读性骤降——三个以上考虑 class。

## 相关页面

- [event(t)](../01_Verse.org/010_Verse/event_t_.md)
