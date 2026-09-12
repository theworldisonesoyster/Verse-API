---
name: listenable
slug: versedotorg/verse/listenable-1
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/listenable-1
kind: function
module: /Verse.org/Verse
grade: S
depth: full
status: done
---

# listenable function（无载荷）🟦【S级·核心】

> A parameterless interface combining awaitable and subscribable.
> 无参数接口：组合了 awaitable（可等待）与 subscribable（可订阅），载荷类型由上下文推断。

`using { /Verse.org/Verse }`

```verse
listenable<public>():listenable(payload)
```

## Parameters

listenable does not take any parameters.（listenable 不接受任何参数。）

## Attributes, Specifiers, and Effects

`listenable<public>():listenable(payload)` —— 标签：public，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Verse }

Ping:listenable() = listenable(){}
```

## 补充说明

- 用法与 [listenable function](listenable.md) 完全一致，仅构造写法不同。
