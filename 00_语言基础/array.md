---
name: array——数组
slug: (补充)语言基础.array
url:
kind: class
module: /语言基础
grade: S
depth: full
status: done
supplement: true
---

# array——数组 🟦【S级·核心】〔补充·非官网镜像〕

> 数组是 Verse 内建的有序集合类型，官网 API Reference 没有为它单设页面（属于语言内建），本页为学习补充。
> 类型写作 `T[]`（如 `int[]`），字面量写作 `array{1, 2, 3}`。

## 这是什么

数组存放一组**同类型、有序**的值。三个要点：

1. **不可变长度**：Verse 数组创建后长度固定，没有 `Add`/`Remove`；"增删"靠生成新数组（`Arr + array{X}`、`Arr.RemoveLast[]` 等可失败操作）。
2. **索引可失败**：`Arr[I]` 在 I 越界时**失败**而不是崩溃——必须放在失败上下文里用。
3. **值类型拷贝语义**：赋值/传参是拷贝，修改副本不影响原数组。

## 最小示例

```verse
Arr:int[] := array{10, 20, 30}          # 定义
First:int = Arr[0]                      # 已知不越界时可这样断言
for (I := 0..Arr.Length - 1, V := Arr[I]):   # 安全遍历（带索引）
    Print("{I} = {V}")
for (V : Arr):                          # 不需要索引时更简洁
    Print("{V}")
Bigger:int[] = Arr + array{40}          # 新数组 = 旧 + 追加
Maybe := Arr[5] or -1                   # 越界兜底：失败时给默认值
```

## 常用操作

| 写法 | 说明 | 失败? |
|---|---|---|
| `Arr[I]` | 取第 I 个元素（0 起） | 越界则失败 |
| `Arr.Length` | 元素个数 | 否 |
| `A + B` | 两个数组连接成新数组 | 否 |
| `Arr.RemoveLast[]` | 去掉末尾元素的新数组（failable，`[]` 调用） | 空数组失败 |
| `for (V : Arr)` | 遍历 | — |

## 何时用 / 何时不用

- 用：固定一批同类对象（所有玩家、所有生成点、一串节拍时间）。
- 不用：需要频繁增删的动态集合——考虑 `map` 或重新设计为"每帧重建数组"。

## 常见坑

- **越界是失败不是错误**：`Arr[Arr.Length]` 永远失败，配合 `or 默认值` 或 `if` 处理。
- 数组没有"原地修改"，`set Arr += array{X}` 实际是整体替换变量。
- `Arr[0]` 在失败上下文之外会编译报错，别图省事裸写。

## 相关页面

- [map——映射](map.md)
- [可失败表达式与failure](failure.md)
- [option——可选值](option.md)
