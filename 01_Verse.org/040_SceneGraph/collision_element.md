---
name: collision_element
slug: versedotorg/scenegraph/collision_element
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_element
kind: class
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# collision_element class <B>

> Base class for collision_volumes that consist of a single volume with a single collision_profile and collision_material for the whole volume. This covers most volume types used in queries and physics, except compound types like a mesh. A query will always return an element rather than a general volume. For example when colliding with a mesh, the element will be a collision_triangle, which is a collision_element and has a single material, rather than a collision_triangle_mesh, which is not an element and has a material palette.
> 由单一体积＋单一 collision_profile 与 collision_material 构成的碰撞体积基类，覆盖大多数体积类型。

`using { /Verse.org/SceneGraph }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| collision_volume | 碰撞体积：表示网格的碰撞形状，可被 Overlap/Sweep 查询检测，并在物理模拟中产生碰撞。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| Collidable | ?logic | 启用/禁用此体积的碰撞。 |
| CollisionProfile | ?collision_profile | 此体积的碰撞轮廓。 |
| Queryable | ?logic | 启用/禁用对此体积的空间查询。 |

### Functions
| Function Name | Description |
| GetLocalTransform | 获取此体积在所有者空间（通常是实体上的组件）中的变换。 |
| SetLocalTransform | 设置此体积在所有者空间中的变换。 |
