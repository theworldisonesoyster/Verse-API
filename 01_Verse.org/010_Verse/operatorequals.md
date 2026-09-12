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

# operator'=' function 🟦【S级·核心】

（本页官网无导语描述；`=` 是可失败的相等比较运算符——相等则成功并返回左值，不相等则失败。）

`using { /Verse.org/Verse }`

```verse
operator'='(Lhs:t, Rhs:comparable where t:comparable)<decides>:t
```

## Parameters

operator'=' takes the following parameters:（operator'=' 接受以下参数：）

| Name | Type | Description |
|---|---|---|
| Lhs | t | 左操作数。 |
| Rhs | comparable | 右操作数。 |
| t | comparable | 操作数的公共类型，须满足 comparable 约束。 |

## Attributes, Specifiers, and Effects

`operator'='(Lhs:t, Rhs:comparable where t:comparable)<decides>:t` —— 标签：decides，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Verse }

Check(HP:int):void =
    if (HP = 0):                 # 相等判断接入失败上下文
        Print("角色倒下")
    if (Best := HP = 100):       # 相等时 Best 被绑定为 HP 的值
        Print("满血 {Best}")
```

## 补充说明

- Verse 中 `=` 判断、`:=` 定义、`set X =` 赋值三者各司其职；`<decides>` 使比较可失败——这是它与多数语言 `==` 的本质差异。
- 不等比较见 [operator'&lt;&gt; function](operatorlessgreater.md)；失败机制见 [可失败表达式与failure](../../00_语言基础/failure.md)。
