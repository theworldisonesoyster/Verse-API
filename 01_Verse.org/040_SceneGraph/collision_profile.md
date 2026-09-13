---
name: collision_profile
slug: versedotorg/scenegraph/collision_profile
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_profile
kind: class
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# collision_profile class <B>

> A collision profile determines how a volume interacts with other volumes for Overlap queries, Sweep queries, and physics simulation. When two volumes are being tested to see how they interact, the algorithm looks like this: GetInteraction(A:collision_profile, B:collision_profile):collision_interaction = InteractionA = B.GetChannelInteraction(A.Channel) InteractionB = A.GetChannelInteraction(B.Channel) return Min(InteractionA, InteractionB)
> 碰撞轮廓：决定体积在 Overlap 查询、Sweep 查询与物理模拟中如何与其他体积交互。

`using { /Verse.org/SceneGraph }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| Channel | collision_channel | 所属对象的碰撞通道。 |
| GetChannelInteraction | (collision_channel):collision_interaction | 所属对象应如何与其他对象交互。GetChannelInteraction 是把 collision_channel 映射为 collision_interaction 的函数，可用一串 if 实现。例如放行相机通道、阻塞其余：BlockAllIgnoreCamera(Channel:collision_channel):collision_interaction = if (CollisionChannels.camera[Channel]): return collision_interaction.Ignore；return collision_interaction.Block。然后 MyProfile:collision_profile = MakeCollisionProfile(CollisionChannels.dynamic, BlockAllIgnoreCamera)。 |
