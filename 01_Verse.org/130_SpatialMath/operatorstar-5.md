---
name: operatorstar-5
slug: versedotorg/spatialmath/operatorstar-5
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/spatialmath/operatorstar-5
kind: function
module: /Verse.org/spatialmath
grade: A
depth: full
status: done
---

> Makes a vector3 by multiplying the components of Right by Left.
> 用 Right 的各分量乘以 Left，得到新的 vector3（标量乘向量的重载）。

`using { /Verse.org/SpatialMath }`

```verse
operator'%'(Left:float, Right:vector3):vector3
```

## 示例

```verse
V := 2.0 * vector3{Forward:=1.0}   # Forward 分量变为 2.0
```
