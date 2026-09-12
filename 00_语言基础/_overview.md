---
name: 语言基础（补充）
slug: (补充)语言基础
url: 
kind: module
module: /语言基础
grade: S
depth: brief
status: done
---

# 语言基础〔补充·非官网镜像〕

> 官网 API Reference 只收录模块/类/函数，**语言内建类型与表达式没有独立页面**（array、map、option、failure 机制等都散在语言文档里）。为补齐学习链路，本章以"补充"形式撰写，页首一律标注〔补充·非官网镜像〕，与官网镜像内容明确区分。

## 页面一览

| 页面 | 一句话 | 级别 |
|---|---|---|
| [array——数组](array.md) | 有序集合 `T[]`，索引可失败 | 🟦 S |
| [map——映射](map.md) | 键值集合 `[K]V`，weak_map 全局变量 | 🟦 S |
| [option——可选值](option.md) | 可能没有值：`?T`、空值写作 `false` | 🟦 S |
| [可失败表达式与failure](failure.md) | Verse 的核心错误处理哲学 | 🟦 S |
| [string——字符串](string.md) | 插值 `{}`、Join、与 []char 转换 | 🟩 A |
| [数值类型 int/float/rational](int.md) | 整除可失败、rational 防浮点误差 | 🟩 A |
| [logic与void](logic_void.md) | 真/假值与无返回 | 🟨 B |
| [元组与子类型](tuple_subtype.md) | 打包多值、where 约束 | 🟨 B |

## 相关页面

- [Verse.org 总览](../01_Verse.org/_overview.md)
- [Intro 首页](../Intro.md)
