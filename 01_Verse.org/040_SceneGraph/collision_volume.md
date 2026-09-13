---
name: collision_volume
slug: versedotorg/scenegraph/collision_volume
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_volume
kind: class
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# collision_volume class <B>

> Collision Volumes represent the collision shapes of meshes. They can be detected by Overlap and Sweep queries and generate collisions in the physics simulation.
> 碰撞体积：表示网格的碰撞形状，可被 Overlap/Sweep 查询检测，并在物理模拟中产生碰撞。

`using { /Verse.org/SceneGraph }`

## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| Collidable | ?logic | 启用/禁用此体积的碰撞。 |
| Queryable | ?logic | 启用/禁用对此体积的空间查询。 |

### Functions
| Function Name | Description |
| GetLocalTransform | 获取此体积在所有者空间（通常是实体上的组件）中的变换。 |
| SetLocalTransform | 设置此体积在所有者空间中的变换。 |
