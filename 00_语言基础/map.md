---
name: map——映射
slug: (补充)语言基础.map
url:
kind: class
module: /语言基础
grade: S
depth: full
status: done
---

# map——映射 <S>

> 映射是"键 → 值"的内建关联容器，属于 Verse 语言内建。
> 类型写作 `[K]V`（如 `[string]int`），字面量写作 `map{"a" => 1, "b" => 2}`。

## 这是什么

映射按**键**存取值，就像字典。三个要点：

1. **取值可失败**：`M[K]` 在键不存在时失败，必须放在失败上下文里。
2. **不可变**：和数组一样，"修改"是生成新映射再 `set` 回去；`ConcatenateMaps` 可合并。
3. **键需可比较**：常用 int/string/player 等作键；配合 `weak_map` 可以用对象当键（见 session 页的全局变量模式）。

## 最小示例

```verse
Scores:[string]int = map{"Anna" => 3, "Ben" => 7}

AddPoint(Name:string):void =
    Old := Scores[Name] or 0                     # 不存在则 0
    if (set Scores = ConcatenateMaps(Scores, map{Name => Old + 1})) {}
    # 单键更新也可以直接: if (set Scores[Name] = Old + 1) {}

Lookup(Name:string):string =
    "{Name} 的分数: {Scores[Name] or 0}"
```

## 常用操作

| 写法 | 说明 | 失败? |
|---|---|---|
| `M[K]` | 取键对应的值 | 缺键失败 |
| `M[K] = V` | （在 `set` 中）设置/更新键 | — |
| `ConcatenateMaps(A, B)` | 合并两个映射（B 优先） | 否 |
| `for (K -> V : M)` | 遍历键值对 | — |
| `weak_map[K, V]` | 键为"弱引用对象"的映射（可存 player/session 等） | — |

## 何时用 / 何时不用

- 用：按 ID/名字/玩家查数据——记分板、配置表、`weak_map[player]` 状态。
- 不用：只需顺序遍历的集合用数组；需要"每回合清空的全局表"配 session 用。

## 常见坑

- `set M[K] = V` 对不存在的键是**新增**还是失败取决于写法——统一用 `or 默认值` 先读后写的模式最稳。
- 遍历顺序不保证与你插入的顺序一致。

## 相关页面

- [array——数组](array.md)
- [session](../01_Verse.org/100_Simulation/session.md) —— weak_map 全局变量标准用法
- [可失败表达式与failure](failure.md)
