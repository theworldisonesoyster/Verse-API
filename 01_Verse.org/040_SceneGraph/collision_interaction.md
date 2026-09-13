---
name: collision_interaction
slug: versedotorg/scenegraph/collision_interaction
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_interaction
kind: enum
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# collision_interaction enumeration <B>

> Specifies how a collision volume pair should interact. See collision_profile.
> 指定一对碰撞体积应如何交互，见 collision_profile。

`using { /Verse.org/SceneGraph }`

## Enumerators

The collision_interaction 枚举包含以下枚举值：
| Name | Description |
| Ignore | 该配对不会被 Overlap/Sweep 查询检测到，也不会在物理模拟中碰撞。 |
| Overlap | 该配对会被 Overlap/Sweep 查询检测到，但不会在物理模拟中碰撞。 |
| Block | 该配对会被 Overlap/Sweep 查询检测到，并在物理模拟中碰撞。 |
