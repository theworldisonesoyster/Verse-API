---
name: operator'='
slug: versedotorg/verse/operatorequals
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/operatorequals
kind: function
module: /Verse.org/Verse
grade: S
depth: full
status: done
---

# operator'='（相等比较）🟦【S级·核心】

> 比较 Lhs 与 Rhs 是否相等；相等则成功（返回 Lhs），不相等则失败。
> 这是把"相等性"接入 Verse 失败机制的运算符——签名里的 `<decides>` 是关键。

## 签名

```verse
operator'='(Lhs:t, Rhs:comparable)<decides>:t where t:comparable
```

对应的不等运算符 [operator'&lt;&gt;](operatorlessgreater.md) 语义相反。

## 这是什么

`A = B` 在 Verse 里不是"赋值"而是**可失败的相等判断**（赋值是 `set`）。它可以：

1. 出现在失败上下文的条件位：`if (X = 5) {…}` 等价于传统 `if (X == 5)`。
2. **兼作取值**：`if (Y := X = 5)`——相等时 Y 被绑定为 X，一条语句完成判断＋取值。

## 最小示例

```verse
using { /Verse.org/Verse }

Check(HP:int):void =
    if (HP = 0):
        Print("角色倒下")
    if (Best := HP = 100):      # 相等时 Best = 100
        Print("满血 {Best}")

Unequal(HP:int):void =
    if (HP <> 0):               # 不等：不相等则成功
        Print("还活着")
```

## 何时用 / 何时不用

- 用：一切相等/不等判断；想在判断的同时拿值时用 `:= X = Rhs` 形式。
- 不用：赋值请用 `set X = V`（语句，不是可失败表达式）。

## 常见坑

- 来自其他语言的肌肉记忆：`=` 判断、`:=` 定义、`set … =` 赋值，三者各司其职，写错位置直接编译错误。
- 参与比较的类型需满足 `comparable`；自定义 class 要可比较需满足相应接口。

## 相关页面

- [可失败表达式与failure](../../00_语言基础/failure.md)
- [operator'&lt;&gt;](operatorlessgreater.md)
