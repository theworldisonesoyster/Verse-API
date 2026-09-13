---
name: SceneGraph module
slug: versedotorg/scenegraph
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph
kind: module
module: /versedotorg
grade: S
depth: brief
status: done
---

# SceneGraph module <S>

SceneGraph 是「实体＋组件」的下一代场景对象模型：entity 是节点，行为与数据挂在 component 上，transform_component 决定位置，辅以相机、灯光、碰撞、交互、骨骼动画等组件族。

## Classes and Structs

| Name | Description |
|---|---|
| [basic_interactable_component](basic_interactable_component.md) | 具有可组合特性集的交互组件。 |
| [interactable_component](interactable_component.md) | 用于处理通用交互。 |
| [interactable_cooldown](interactable_cooldown.md) | 设置交互后的冷却。 |
| [interactable_cooldown_per_agent](interactable_cooldown_per_agent.md) | 按代理分别设置交互冷却。 |
| [interactable_duration](interactable_duration.md) | 设置一次交互的持续时长。 |
| [interactable_success_limit](interactable_success_limit.md) | 设置可成功交互的次数上限。 |
| [camera_body](camera_body.md) | 相机机身设置，如传感器/胶片、快门速度等。 |
| [camera_component](camera_component.md) | 表示相机的物理机身、镜头及其他电影摄影属性：传感器尺寸、宽高比锁定/约束、焦距、对焦距离、位置等。 |
| [camera_director_component](camera_director_component.md) | 负责在活动相机变化时选择相机并进行混合；还可在不同相机之间共享全局设置（如后期处理设置）。 |
| [camera_lens](camera_lens.md) | 相机镜头设置。 |
| [camera_modifier_stack](camera_modifier_stack.md) | 相机状态的修饰符栈。 |
| [camera_modifier](camera_modifier.md) | 可修改相机状态的对象的基类。 |
| [camera_state](camera_state.md) | 相机的当前状态。 |
| [camera_transition](camera_transition.md) | 控制相机模式之间如何过渡。 |
| [camera_mode_blend](camera_mode_blend.md) | 两种相机模式之间的可配置混合。 |
| [camera_mode_blend_pop](camera_mode_blend_pop.md) | 瞬间切换（snap）到目标模式。 |
| [camera_mode_blend_linear](camera_mode_blend_linear.md) | 相机模式之间的线性混合。 |
| [camera_mode_blend_smoothstep](camera_mode_blend_smoothstep.md) | 使用 smoothstep 函数在两种相机模式之间混合。 |
| [camera_mode_blend_smootherstep](camera_mode_blend_smootherstep.md) | 使用 smootherstep 函数在两种相机模式之间混合。 |
| [camera_mode_blend_orbit](camera_mode_blend_orbit.md) | 两种相机模式之间的可配置混合（orbit 轨道变体）。 |
| [orthographic_camera_component](orthographic_camera_component.md) | 简单的正交相机。 |
| [perspective_camera_component](perspective_camera_component.md) | 简单的透视相机。 |
| [physical_camera_component](physical_camera_component.md) | 基于物理的相机：以更接近真实物理相机的方式决定取景属性。 |
| [skeletal_animation](skeletal_animation.md) | 骨架的修饰符：用骨骼动画驱动网格变形。 |
| [play_skeletal_animation_result](play_skeletal_animation_result.md) | 播放骨骼动画的结果。 |
| [skeleton](skeleton.md) | 骨架（skeleton）是骨骼与骨骼组/链（sets/chains）的集合。 |
| [capsule_light_component](capsule_light_component.md) | 胶囊灯：从指定半径与长度的胶囊形光源向场景四周发光；半径与长度为 0 时等效于点光源。 |
| [directional_light_component](directional_light_component.md) | 方向光：模拟来自无限远处的光源，投射的阴影相互平行。 |
| [light_component](light_component.md) | SceneGraph 中灯光组件的基类。依赖：实体上的 transform_component 决定灯的位置。 |
| [rect_light_component](rect_light_component.md) | 矩形面光灯：从指定宽高的矩形平面向场景发光，可用于模拟各类面光源。 |
| [sphere_light_component](sphere_light_component.md) | 球形灯：从指定半径的球形光源向四周发光；半径为 0 时为点光源。 |
| [spot_light_component](spot_light_component.md) | 聚光灯：从单点按锥形发光；锥形由内锥角（InnerConeAngleDegrees）与外锥角（OuterConeAngleDegrees）定义。 |
| [collision_channel](collision_channel.md) | 碰撞通道：每个体积都在其 collision_profile 中带有碰撞通道，用于决定两个体积如何交互。 |
| [collision_profile](collision_profile.md) | 碰撞轮廓：决定体积在 Overlap 查询、Sweep 查询与物理模拟中如何与其他体积交互。 |
| [overlap_hit](overlap_hit.md) | Overlap 查询的结果：SourceVolumes 中任一体积与其他体积的每个相交各产生一个 overlap_hit。见 entity.FindOverlapHits()。 |
| [sweep_hit](sweep_hit.md) | Sweep 查询的结果：每个相交产生一个 sweep_hit。见 entity.FindSweepHits()。 |
| [collision_volume](collision_volume.md) | 碰撞体积：表示网格的碰撞形状，可被 Overlap/Sweep 查询检测，并在物理模拟中产生碰撞。 |
| [collision_element](collision_element.md) | 由单一体积＋单一 collision_profile 与 collision_material 构成的碰撞体积基类，覆盖大多数体积类型。 |
| [collision_capsule](collision_capsule.md) | 沿 Z 轴对齐的碰撞胶囊体。 |
| [collision_sphere](collision_sphere.md) | 碰撞球体。 |
| [collision_point](collision_point.md) | 碰撞点。 |
| [collision_box](collision_box.md) | 轴对齐碰撞盒。 |
| [particle_system_component](particle_system_component.md) | 在实体位置生成 particle_system；组件在场景中期间粒子系统持续模拟。依赖：实体上的 transform_component。 |
| [sound_component](sound_component.md) | 在实体位置播放音效的组件。 |
| [mesh_component](mesh_component.md) | 在实体位置渲染网格。网格是一组多边形，可用于表现世界中的形状，如植被、地形装饰、建筑与道具等。 |
| [possessable_component](possessable_component.md) | 标记可被代理（agent）附身（possess）的实体。 |
| [entity_prefab](entity_prefab.md) | 编辑器定义的预制体（prefab）的引用类型；只有生成的 digest 代码才应引用此类型。 |
| [icon_component](icon_component.md) | 保存实体图标的组件。 |
| [entity_origin](entity_origin.md) | 为实体提供替代原点（默认为 transform_component）的类。 |
| [float_range](float_range.md) | 带最小值与最大值的范围；值要落在范围内须满足 min ≤ max。 |
| [execution_listenable](execution_listenable.md) | 订阅或等待组件 TickEvents 各阶段的 DeltaTime 回调。 |
| [rarity](rarity.md) | 稀有度：供玩法与表现系统对事物进行分类与分级。 |
| [common_rarity](common_rarity.md) | 稀有度：常见（Common）。 |
| [uncommon_rarity](uncommon_rarity.md) | 稀有度：非常见（Uncommon）。 |
| [rare_rarity](rare_rarity.md) | 稀有度：稀有（Rare）。 |
| [epic_rarity](epic_rarity.md) | 稀有度：史诗（Epic）。 |
| [legendary_rarity](legendary_rarity.md) | 稀有度：传说（Legendary）。 |
| [rarity_component](rarity_component.md) | 标注实体稀有度的组件。 |
| [stackable_component](stackable_component.md) | 挂到实体后，允许其与具有兼容组件的其他实体合并（堆叠）的组件。 |
| [change_stack_size_result](change_stack_size_result.md) | 更改堆叠数量的结果。 |
| [change_max_stack_size_result](change_max_stack_size_result.md) | 更改最大堆叠数量的结果。 |
| [basic_stackable_component](basic_stackable_component.md) | 基础堆叠组件。 |

## Interfaces

| Name | Description |
|---|---|
| [has_camera_modifier](has_camera_modifier.md) | 拥有相机修饰符栈的类实现的接口。 |
| [easeable](easeable.md) | 用于触发缓动行为的接口。 |
| [scene_event](scene_event.md) | 可通过场景图发送的事件。 |
| [origin](origin.md) | 为实体提供替代原点的接口（默认原点为其父实体），见 transform_component。 |
| [has_merge_rules](has_merge_rules.md) | 想参与实体可合并性检查的组件实现的「合并规则」接口。 |

## Enumerations

| Name | Description |
|---|---|
| [camera_projection_mode](camera_projection_mode.md) | 相机投影模式（正交/透视等）。 |
| [camera_transition_initial_orientation](camera_transition_initial_orientation.md) | 控制相机模式过渡时的初始朝向。 |
| [collision_interaction](collision_interaction.md) | 指定一对碰撞体积应如何交互，见 collision_profile。 |
| [entity_streaming_policy](entity_streaming_policy.md) | 实体的客户端流送模式。 |
| [children_streaming_policy](children_streaming_policy.md) | 子实体的客户端流送模式。 |

| GlobalModifierPosition 〔无独立页面〕 | （无独立页面）全局修饰符位置常量。 |
| VisualModifierPosition 〔无独立页面〕 | （无独立页面）视觉修饰符位置常量。 |
