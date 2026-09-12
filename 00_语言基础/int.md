---
name: 数值类型 int/float/rational
slug: (补充)语言基础.int
url:
kind: class
module: /语言基础
grade: A
depth: brief
status: done
---

# 数值类型 int / float / rational 🟩【A级·常用】

> Verse 的三种数值类型；属于 Verse 语言内建。

## 这是什么

| 类型 | 写法 | 用途 | 注意 |
|---|---|---|---|
| `int` | `42` | 计数、索引、分数 | 除法 `/` 是**可失败**的整除（除数为 0 失败）；取模用 `Mod` |
| `float` | `3.14`、`1.0e-3` | 时间、坐标、比例 | 与 int 不隐式互转；`Int[]`/`Float[]` 显式转换且可失败 |
| `rational` | `Rational(1, 3)` | 精确分数（音频/节拍场景） | 避免浮点误差，音乐类玩法可用 |

## 最小示例

```verse
Half := 1.0 / 2.0              # 0.5
Q := Quotient(7, 2)            # 3（整数商）
R := Mod(7, 2)                 # 1（余数）
F := Float[3] or 0.0           # int→float 可失败转换 + 兜底
```

## 常见坑

- `7 / 2` 是整数除法（=3）；想得 3.5 要写 `7.0 / 2.0`。
- float 精度有限，节拍累加建议用 rational 或"目标时刻 + GetSimulationElapsedTime"比较。

## 相关页面

- [可失败表达式与failure](failure.md)
- [Verse 数学函数族](../01_Verse.org/010_Verse/_overview.md)
