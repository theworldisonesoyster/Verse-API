---
name: 可失败表达式与failure
slug: (补充)语言基础.failure
url:
kind: class
module: /语言基础
grade: S
depth: full
status: done
---

# 可失败表达式与 failure 🟦【S级·核心】

> Verse 用"失败"代替"异常/空指针"：任何操作都可能成功或失败，失败不崩溃，只是"这条路不通"。
> 官网各 API 页签名中的 `<decides>` 即为此机制。

## 这是什么

这是 Verse 最独特、最重要的机制。带 `<decides>` 效果的函数/运算符是"可失败"的：调用它**必须**处在"失败上下文"里。失败上下文里的表达式从上到下尝试，**任何一个失败，整块代码跳过**（不是报错），程序继续走后面的路。

常见的失败上下文写法：

| 写法 | 说明 |
|---|---|
| `if (Expr)` | 表达式成功 → 执行块内代码；失败 → else/跳过 |
| `for (X : Arr)` | 遍历也算失败上下文 |
| `F[]` | 用 `[]` 调用可失败函数（无参 failable） |
| `A and B`, `not A` | 逻辑组合，短路求值 |
| `X := Expr` | 定义语句本身可失败（Expr 失败则不定义） |

## 最小示例

```verse
Score(Name:string):void =
    if:
        P := Players[Name]        # 1. 查到玩家才继续
        S := Scores[P]            # 2. 有分数才继续（任意一步失败 → 整块跳过）
        S > 10                    # 3. 条件判断也是可失败表达式
    then:
        Print("{Name} 是高手")

# 多个初始化挤一行也行：
if (A := Arr[0], B := Map[A] or 0, B > 0) { Print("ok") }
```

## 与"错误处理"的思维差异

- 传统语言：先写快乐路径，再 try/catch 兜底。
- Verse：把"可能失败"写进类型里（`<decides>`），调用方**被迫**处理失败——要么分支，要么 `or 默认值`，要么继续往上失败。编译器保证你漏不掉。

## 常用模式

| 模式 | 写法 |
|---|---|
| 取值兜底 | `V := M[K] or 默认` |
| agent 转 player | `if (P := player[Agent]) {…}` |
| 链式安全取值 | `if (C := Obj.GetComponent[], P := C.Position[]) {…}` |
| 断言已知安全 | 确定不会失败时可用 `X:calc` 上下文断言（慎用，失败会中断程序） |

## 何时用 / 何时不用

- 用：一切可能不成立的读取/查询/比较。
- 不用：不要为了"绕开失败"而把逻辑写成嵌套 if 泥球——善用 `or 默认值` 与提前返回。

## 常见坑

- 可失败函数用 `()` 调用会编译错误，无参 failable 必须写 `[]`（如 `GetTeam[]`）。
- 失败上下文里 `set` 变量后若整块失败，**回滚**该块内的修改（事务性）——这正是 `<decides>` 的设计，注意副作用函数别放进失败块。

## 相关页面

- [option——可选值](option.md)
- [array——数组](array.md)
- [operator'=](../01_Verse.org/010_Verse/operatorequals.md) —— 最常见的可失败运算符
