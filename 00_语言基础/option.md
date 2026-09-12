---
name: option——可选值
slug: (补充)语言基础.option
url:
kind: class
module: /语言基础
grade: S
depth: full
status: done
supplement: true
---

# option——可选值 🟦【S级·核心】〔补充·非官网镜像〕

> option 表示"可能有一个值，也可能没有"，官网 API Reference 无单设页面，本页为学习补充。
> 类型写作 `?T`（如 `?int`），有值字面量 `option{7}`，空值 `false`。

## 这是什么

`?T` 解决"这个值可能不存在"的问题——比返回 -1 之类的哨兵值干净得多。它和失败上下文深度绑定：**取出 option 里的值本身就是一个可失败操作**（`Opt?`），于是"有值就继续、没值就走别路"成了一行代码。

## 最小示例

```verse
var Nickname:?string = option{"Alice"}
set Nickname = false            # 清空

Show():void =
    if (Name := Nickname?):     # 有值 → Name 是 string；无值 → 走 else
        Print("昵称 {Name}")
    else:
        Print("没有昵称")

Default():string =
    Nickname? or "无名氏"        # 取值失败给默认
```

## 常用操作

| 写法 | 说明 | 失败? |
|---|---|---|
| `Opt?` | 取出值 | 空则失败 |
| `Opt? or 默认` | 取值失败用默认 | 否 |
| `option{V}` / `false` | 构造有值/空 | — |
| `Opt = 值判断` | `if (Opt = option{7})` 比较 | 可失败 |

## 何时用 / 何时不用

- 用：查询可能无结果（map 里没有、玩家没设置昵称）；API 返回"可能空"的字段。
- 不用：值一定存在时别用 option，多一层失败上下文徒增噪音。

## 常见坑

- `?T` 的空值写作 `false`，不是 `null`/`none`——第一次见非常反直觉，记住即可。
- `Opt?` 之后变量类型是 `T`（脱掉了 `?`），可以直接当普通值用。

## 相关页面

- [可失败表达式与failure](failure.md)
- [array——数组](array.md)
