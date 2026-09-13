---
name: collision_point
slug: versedotorg/scenegraph/collision_point
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_point
kind: class
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# collision_point class <B>

> A collision point.
> 碰撞点。

`using { /Verse.org/SceneGraph }`

## Inheritance Hierarchy

此类派生自以下层级，起点为 ：
| Name | Description |
| collision_volume | 碰撞体积：表示网格的碰撞形状，可被 Overlap/Sweep 查询检测，并在物理模拟中产生碰撞。 |
| collision_element | 由单一体积构成的碰撞体积基类：整个体积共用单一 collision_profile 与 collision_material。它覆盖查询与物理中使用的大多数体积类型，但不含网格等复合类型。查询总是返回 element 而非一般体积：例如与网格碰撞时，返回的元素是 collision_triangle（属于 collision_element，有单一材质），而不是 collision_triangle_mesh（非 element，带材质调色板）。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [Collidable](collision_point_collidable.md) | ?logic | 启用/禁用此体积的碰撞。 |
| [CollisionProfile](collision_point_collisionprofile.md) | ?collision_profile | 此体积的碰撞轮廓。 |
| [Queryable](collision_point_queryable.md) | ?logic | 启用/禁用对此体积的空间查询。 |

### Functions
| Function Name | Description |
| [GetLocalTransform](collision_point_getlocaltransform.md) | 获取此体积在所有者空间（通常是实体上的组件）中的变换。 |
| [SetLocalTransform](collision_point_setlocaltransform.md) | 设置此体积在所有者空间中的变换。 |
