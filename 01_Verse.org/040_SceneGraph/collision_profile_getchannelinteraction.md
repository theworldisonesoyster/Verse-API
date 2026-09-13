---
name: GetChannelInteraction data
slug: versedotorg/scenegraph/collision_profile/getchannelinteraction
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/collision_profile
kind: data
module: /Verse.org/scenegraph
grade: B
depth: oneliner
status: done
order: 2
parent: versedotorg/scenegraph/collision_profile
---

#
# GetChannelInteraction data <B>

所属对象应如何与其他对象交互。GetChannelInteraction 是把 collision_channel 映射为 collision_interaction 的函数，可用一串 if 实现。例如放行相机通道、阻塞其余：BlockAllIgnoreCamera(Channel:collision_channel):collision_interaction = if (CollisionChannels.camera[Channel]): return collision_interaction.Ignore；return collision_interaction.Block。然后 MyProfile:collision_profile = MakeCollisionProfile(CollisionChannels.dynamic, BlockAllIgnoreCamera)。
