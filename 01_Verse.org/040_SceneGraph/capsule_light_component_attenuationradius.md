---
name: AttenuationRadius data
slug: versedotorg/scenegraph/capsule_light_component/attenuationradius
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/capsule_light_component
kind: data
module: /Verse.org/scenegraph
grade: B
depth: oneliner
status: done
order: 1
parent: versedotorg/scenegraph/capsule_light_component
---

#
# AttenuationRadius data <B>

灯光可见影响范围的边界。这种钳制并不符合物理，但对性能非常重要——灯越大开销越高。光衰减基于平方反比定律；在衰减半径末端有额外的平滑因子把光贡献淡出到 0，避免硬截断。
