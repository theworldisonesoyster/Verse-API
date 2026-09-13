---
name: Assets module
slug: versedotorg/assets
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/assets
kind: module
module: /versedotorg
grade: A
depth: brief
status: done
---

# Assets module <A>

资产引用类型：网格、贴图、材质、音效、粒子、动画序列，以及输入动作与输入映射。

## Classes and Structs

| Name | Description |
|---|---|
| [animation_sequence](animation_sequence.md) | 动画序列资产。 |
| [material](material.md) | 材质资产。 |
| [particle_system](particle_system.md) | 粒子系统资产。 |
| [mesh](mesh.md) | 网格资产。 |
| [sound_wave](sound_wave.md) | 声波（音频）资产。 |
| [texture](texture.md) | 贴图资产。 |
| [input_mapping](input_mapping.md) | 输入映射：把物理输入绑定到 input_action，交给 player_input 启用/停用。 |

## Interfaces

| Name | Description |
|---|---|
| [has_icon](has_icon.md) | 提供图标的接口。 |

## Functions

| Name | Description |
|---|---|
| [input_action](input_action.md) | 参数化构造：创建 input_action(t) 输入动作。 |
