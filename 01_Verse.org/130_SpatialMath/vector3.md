---
name: vector3
slug: versedotorg/spatialmath/vector3
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/vector3
kind: class
module: /Verse.org/SpatialMath
grade: S
depth: full
status: done
---

# vector3 🟦【S级·核心】

> 三维向量：位置、方向、偏移的统一表示。

## 这是什么

所有 3D 空间计算的基本单位。**当前版本的分量名是 Left / Up / Forward**（官方标注由旧坐标轴 -Y/Z/X 更名而来）——这是和旧教程/旧代码最大的差异点，老代码里的 `.X/.Y/.Z` 要按语义映射成 `Left/Up/Forward`。

向量是 struct（值拷贝语义），支持 `+ - * /` 运算符与一组模块级函数（距离、点积、叉积、插值等，见 SpatialMath 总览）。

## 签名

```verse
vector3<public><native> := struct:
    Left<float>       # 左方向分量（旧 -Y）
    Up<float>         # 上方向分量（旧 Z）
    Forward<float>    # 前方向分量（旧 X）
```

## 最小示例

```verse
using { /Verse.org/SpatialMath }

Origin := vector3{Left := 0.0, Up := 0.0, Forward := 0.0}
Target := vector3{Forward := 100.0, Up := 50.0}

Dist := Distance(Origin, Target)        # 模块级函数
Shifted := Target + vector3{Up := 2.0}  # 向上平移 2 单位
```

## 常用成员 / 配套函数

| 名称 | 说明 | 级别 |
|---|---|---|
| `Left` / `Up` / `Forward` | 三分量 | 🟦 S |
| `Distance` / `DistanceSquared` | 两点距离 | 🟩 A |
| `DotProduct` / `CrossProduct` | 点积/叉积 | 🟩 A |
| `Lerp` | 线性插值（平滑移动常用） | 🟩 A |
| `operator'+' '-' '*'` | 向量运算符 | 🟨 B |

## 何时用 / 何时不用

- 用：坐标、方向、速度、偏移量。
- 不用：纯 2D 界面布局——UI 用自己的对齐系统，别拿向量硬算。

## 常见坑

- **分量名不是 X/Y/Z**；看到老代码 `.X` 要翻译成 `.Forward`（语义对应，不是位置对应）。
- struct 拷贝语义：`B := A` 后改 `B.Up` 不影响 A。

## 相关页面

- [rotation](rotation.md)
- [transform_component](../040_SceneGraph/transform_component.md) —— 向量的消费方
