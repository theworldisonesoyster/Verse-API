---
name: transform_component
slug: versedotorg/scenegraph/transform_component
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/transform_component
kind: class
module: /Verse.org/SceneGraph
grade: S
depth: full
status: done
---

# transform_component 🟦【S级·核心】

> Component holding the position/rotation/scale state of an entity.
> 保存实体"在哪、朝哪、多大"的组件——移动任何 SceneGraph 对象都要经过它。

## 这是什么

[entity](entity.md) 本身没有位置概念；挂上 `transform_component` 后才有。它维护：

- `LocalTransform`：相对父实体的局部变换（构造时可给初值）。
- `GlobalTransform`：世界坐标系的最终变换（由父链计算得出，构造时设置的值会被计算结果覆盖）。

变换类型是 `/Verse.org/SpatialMath` 的 [transform](../130_SpatialMath/rotation.md)（位置＋旋转＋缩放三合一）。读写局部变换、读取全局变换是移动/摆放物体的日常操作。

## 签名

```verse
transform_component<public><native> := class<native>(component):
    GlobalTransform<public>:?transform   # 世界变换（只读语义：由父链计算）
    LocalTransform<public>:?transform    # 局部变换（相对父实体）
    IsInScene<public>()<transacts><decides>:logic
    IsSimulating<public>()<transacts><decides>:logic
    # 继承自 component 的生命周期函数同样可用
```

## 最小示例

```verse
using { /Verse.org/SceneGraph }
using { /Verse.org/SpatialMath }
using { /Verse.org/Simulation }

# 让实体每帧上升一点（悬浮效果）
FloatUp(TC:transform_component)<suspends>:void =
    loop:
        if (T := TC.LocalTransform?):
            Up := T.Position + vector3{Up := 2.0}   # 每帧 +2 单位
            TC.SetLocalPosition(Up)                  # 以实际 API 名为准
        Sleep(0.0)
```

## 常用成员

| 成员 | 说明 | 级别 |
|---|---|---|
| `LocalTransform` / `GlobalTransform` | 读变换（`?` 可失败取出） | 🟦 S |
| `SetLocalPosition` / `SetLocalRotation` 等设置函数 | 改局部变换（以官方页函数表为准） | 🟦 S |
| `IsInScene[]` / `IsSimulating[]` | 状态断言（可失败） | 🟨 B |

## 何时用 / 何时不用

- 用：任何"移动/摆放/缩放 SceneGraph 对象"的需求。
- 不用：临时算坐标却不落盘——直接用 SpatialMath 计算，不必动组件。

## 常见坑

- `GlobalTransform` 是**计算结果**，构造时写的初值会被覆盖；要摆放请设 `LocalTransform`。
- 两个 `?transform` 字段都是可失败读取，失败上下文别忘了。

## 相关页面

- [entity](entity.md) / [component](component.md)
- [vector3](../130_SpatialMath/vector3.md) / [rotation](../130_SpatialMath/rotation.md)
