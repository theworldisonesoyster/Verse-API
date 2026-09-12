---
name: Specifiers 与 Effects 对照
slug: (附录)specifiers
url: https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse
kind: module
module: /附录
grade: S
depth: brief
status: done
---

# Specifiers 与 Effects 对照

> 官网每个 API 页的「Attributes, Specifiers, and Effects」章节都重复同一批标准定义。本页把这些公共表格**完整翻译一次**，各 API 页只标注自己携带的标签，语义一律链接到这里。
> 下方全部定义译自官网 API 页面内嵌的标准表格（收集自本库 831 页快照的并集）。

## Specifiers（说明符，写在 `<` `>` 中修饰标识符）

| Specifier | 官方含义（中译） |
|---|---|
| `<public>` | 该标识符全局可访问。可用于模块、类、接口、结构体、枚举、方法与数据。 |
| `<native>` | 表示元素的实现细节由 C++ 完成。带 native 的 Verse 定义会自动生成 C++ 定义供引擎侧填充实现。可用于类、接口、枚举、方法与数据。 |
| `<native_callable>` | 表示该实例方法既是 native（C++ 实现），又可从 Verse 调用。 |

## Effects（效果，写在函数签名 `<` `>` 中声明行为契约）

| Effect | 官方含义（中译） |
|---|---|
| `<transacts>` | 表示函数执行的任何动作都可回滚。任何对可变变量（`var`）的写入都要求此效果。若把 transacts 加到实际不可回滚的函数上，编译器会提示（native 函数不做此检查）。 |
| `<decides>` | 表示该函数**可以失败**：调用它必须处于失败上下文（`if`/`or`/`not` 等），失败时整块表达式跳过而不报错。 |
| `<suspends>` | 表示该函数是异步的：为函数体创建异步上下文，内部可调用 Sleep、Await 等挂起操作。 |
| `<no_rollback>` | 未指定排他效果时的默认效果。表示函数执行的动作**不可撤销**，因此不能用于失败上下文。此效果不可手动指定。 |
| `<reads>` | 表示相同输入不保证产生相同写入/结果（读取外部可变状态）。 |
| `<predicts>` | 官网标准表中该条目描述为空（参见官方 Specifiers Page）。 |

## 签名里还会见到的其他标签

`<concrete>`、`<abstract>`、`<final>`、`<final_super>`、`<internal>`、`<epic_internal>` 等出现在类/接口定义的签名中（如 `agent := class<epic_internal>(entity)`）。它们的完整官方定义见官网 [Specifiers Page](https://dev.epicgames.com/documentation/fortnite/specifiers-and-attributes-in-verse)；在本库各页的「Attributes, Specifiers, and Effects」小节只列标签不重复释义。

## 相关页面

- [语言基础](00_语言基础/_overview.md) —— failure/option 等机制与本页 `<decides>` 直接相关
