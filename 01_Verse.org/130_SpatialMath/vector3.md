---
name: vector3
slug: versedotorg/spatialmath/vector3
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/vector3
kind: struct
module: /Verse.org/SpatialMath
grade: S
depth: full
status: done
---

# vector3 struct <S>

> 3-dimensional vector with float components.
> 带浮点分量的三维向量。

`using { /Verse.org/SpatialMath }`

## Members

This struct has data members, but no functions.（此结构体只有数据成员，没有函数。）

### Data

| Data Member Name | Type | Description |
|---|---|---|
| [Left](vector3_left.md) | float | 此向量的 Left（原 -Y）分量。 |
| [Up](vector3_up.md) | float | 此向量的 Up（原 Z）分量。 |
| [Forward](vector3_forward.md) | float | 此向量的 Forward（原 X）分量。 |

## 示例

```verse
using { /Verse.org/SpatialMath }

Origin := vector3{Left := 0.0, Up := 0.0, Forward := 0.0}
Target := vector3{Forward := 100.0, Up := 50.0}
Shifted := Target + vector3{Up := 2.0}   # 向上平移 2 单位
```

## 补充说明

- **分量名是 Left/Up/Forward**，不是 X/Y/Z——官方标注了与旧坐标轴的对应关系（Forward=旧 X、Left=旧 -Y、Up=旧 Z），读旧代码时按此翻译。
- struct 为值拷贝语义：`B := A` 后改 B 不影响 A。
- 距离/点积/插值等运算是 SpatialMath 模块的函数（Distance、DotProduct、Lerp 等，见 [SpatialMath module](../_overview.md)）。
