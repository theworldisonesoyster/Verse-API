# -*- coding: utf-8 -*-
"""patch_scene.py — 向 scene_pack.py 追加已知句对照"""
import json

p = "tools/content/scene_pack.py"
s = open(p, encoding="utf-8").read()

NEW_CELLS = {
    "The number of seconds after a successful interaction, before being able to initiate a subsequent interaction for anyone. This is only used if duration is greater than 0.0. Modifying this does not affect the RemainingDuration. When a cooldown starts on the component all other interactions are canceled.":
        "成功交互后、任何人都可再次发起交互之前所需的秒数。仅在 duration > 0.0 时生效；修改它不影响 RemainingDuration。组件开始冷却时，其上的所有其他交互都会被取消。",
    "The remaining cooldown, in seconds, before new interactions can be initiated on this component.":
        "此组件上可再次发起新交互前的剩余冷却秒数。",
    "Event which fires when the shared cooldown expires.": "共享冷却到期时触发的事件。",
    "The duration in seconds after a successful interaction, before the interacting agent can initiate a subsequent interaction. This is only used if the duration is greater than 0.0. Modifying this does not affect any RemainingPerAgentCooldownDuration. This property gives other agents time to interact, when there is a limited number of Simultaneous Interactors.":
        "成功交互后、发起交互的代理可再次发起交互之前所需的秒数。仅在 duration > 0.0 时生效；修改不影响 RemainingPerAgentCooldownDuration。当可同时交互人数有限时，此属性给其他代理留出交互时间。",
    "The cooldown remaining, in seconds, before a particular agent is able to initiate an interaction on this component.":
        "特定代理在此组件上可再次发起交互前的剩余冷却秒数。",
    "Event which fires when the per agent cooldown expires. Sends the agent which was previously affected by the cooldown.":
        "按代理的冷却到期时触发；载荷为此前受冷却影响的代理。",
    "The number of seconds an agent must spend interacting with the object to successfully complete an interaction. 0.0 or less results in an immediate successful interaction. If set during an interaction, the value given will be used for the next interaction and the remaining duration will be updated subtracting the new given value with the current time elapsed. If the subtraction were zero or less it will immediately conclude.":
        "代理需与对象持续交互这么多秒才能完成一次交互；≤0.0 表示立即成功。若在交互进行中设置，新值将用于下一次交互，剩余时长按「新值减去已用时间」更新；差值 ≤0 则立即结束。",
    "The max number of simultaneous interactors. A value of false is unlimited. This value represents how many agents may have active interactions. If this changes to a value less than the current number of active interactions, those interactions are not canceled but new interactions will not start.":
        "可同时交互的最大人数；false 表示不限。表示有多少代理可同时处于交互中。若改成小于当前活跃交互数的值，已有交互不取消，但不会开始新交互。",
    "Returns an agent\u2019s remaining duration, in seconds, for interaction. Fails if the agent is not interacting with this component.Returns the same value when called multiple times within a transaction.":
        "返回某代理本次交互的剩余秒数；该代理未在交互则失败。同一事务内多次调用返回相同值。",
    "Sets an agent\u2019s remaining duration, in seconds, for interaction. Fails if the agent is not interacting with this component.":
        "设置某代理本次交互的剩余秒数；该代理未在交互则失败。",
    "The number of times the component can be successfully interacted with. A value of false is unlimited. When SuccessfulInteractionCount reaches MaxSuccessfulInteractions all active interactions are canceled, and the component cannot be interacted with.":
        "此组件可被成功交互的次数；false 表示不限。达到 MaxSuccessfulInteractions 后所有活跃交互被取消，组件无法再被交互。",
    "The number of times this component has had a successful interaction.": "此组件已成功交互的次数。",
    "Resets the counter for the times this component has had a successful interaction.": "重置成功交互次数计数。",
    "Width of camera sensor in millimeters.": "相机传感器宽度（毫米）。",
    "Height of camera sensor in millimeters.": "相机传感器高度（毫米）。",
    "Horizontal offset of camera sensor.": "相机传感器的水平偏移。",
    "Vertical offset of camera sensor.": "相机传感器的垂直偏移。",
    "The camera sensor sensitivity to light.": "相机对光的感光度。",
    "Camera shutter speed.": "相机快门速度。",
    "Focal length of the lens in millimeters.": "镜头焦距（毫米）。",
    "Aperture of the lens in FStop.": "镜头光圈（FStop）。",
    "Squeeze factor for anamorphic lenses.": "变形（anamorphic）镜头的挤压系数。",
    "Number of blades of diaphragm.": "光圈叶片数。",
    "Sets the duration of the camera transition": "设置相机过渡的时长。",
    "The collision channel for the owning object.": "所属对象的碰撞通道。",
    "The source volume (query input)": "来源体积（查询输入）",
    "The source volume transform": "来源体积变换",
    "The component that was hit by SourceVolume": "被 SourceVolume 命中的组件",
    "The volume that was hit by SourceVolume": "被 SourceVolume 命中的体积",
    "The source volume (query input).": "来源体积（查询输入）。",
    "The source volume transform at the start of the sweep.": "扫掠开始时来源体积的变换。",
    "The world-space translation (relative to SourceStartGlobalTransform) of SourceVolume when it touches TargetVolume.":
        "SourceVolume 触到 TargetVolume 时的世界位移（相对 SourceStartGlobalTransform）。",
    "The Distance along the sweep at which SourceVolume touches TargetVolume.":
        "扫掠路径上 SourceVolume 触到 TargetVolume 处的距离。",
    "The component that was hit by SourceVolume.": "被 SourceVolume 命中的组件。",
    "The volume that was hit by SourceVolume.": "被 SourceVolume 命中的体积。",
    "The point of contact between SourceVolume and TargetVolume.": "SourceVolume 与 TargetVolume 的接触点。",
    "The normal on TargetVolume at the HitPosition.": "HitPosition 处 TargetVolume 的法线。",
    "Rarity may be used by gameplay and presentation systems to classify and rank things.":
        "稀有度：供玩法与表现系统对事物进行分类与分级。",
    "Controls how the animation plays back.": "控制动画的播放方式。",
}

NEW_PREFIX = [
    ["Represents the physical body, lens of the camera and other cinematographic qualities",
     "表示相机的物理机身、镜头及其他电影摄影属性（传感器尺寸、宽高比锁定、焦距、对焦距离、位置等）。"],
    ["Base class for light components in the SceneGraph. Dependencies: transform_component on the entity positions the light.",
     "SceneGraph 中灯光组件的基类。依赖：实体上的 transform_component 决定灯的位置。"],
    ["Collision Volumes represent the collision shapes of meshes.",
     "碰撞体积：表示网格的碰撞形状，可被 Overlap/Sweep 查询检测，并在物理模拟中产生碰撞。"],
    ["The source component and volume (query input). For compound inputs (like an entity hierarchy) this will be a component/volume in that hierarchy. The SourceTransform is the transform of SourceVolume used for the overlap test. For single volume inputs like a sphere, the Source volume and transform are just the inputs to the overlap test, and the component is false.",
     "来源组件与体积（查询输入）。对复合输入（如实体层级），这是层级中参与查询的组件/体积；SourceTransform 是本次 Overlap 测试所用 SourceVolume 的变换。对球体等单体积输入，体积与变换即查询输入本身，component 为 false。"],
    ["The source component and volume (query input). For compound inputs (like an entity hierarchy) this will be a component/volume in that hierarchy. The SourceGlobalTransform is the transform of SourceVolume at the start of the sweep. For single volume inputs like a sphere, the volume and transform are just the inputs to the sweep, and the component is false.",
     "来源组件与体积（查询输入）。对复合输入（如实体层级），这是层级中参与查询的组件/体积；SourceGlobalTransform 是扫掠开始时 SourceVolume 的变换。对球体等单体积输入，体积与变换即查询输入本身，component 为 false。"],
]

anchor = '"known_cells": {'
assert anchor in s, "anchor missing"

def fmt_dict(d):
    items = []
    for k, v in d.items():
        items.append("        %s: %s," % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False)))
    return "\n".join(items)

def fmt_list(lst):
    items = []
    for k, v in lst:
        items.append("        [%s, %s]," % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False)))
    return "\n".join(items)

block = ('"known_prefix": [\n' + fmt_list(NEW_PREFIX) + "\n    ],\n"
         '    "known_cells": {\n' + fmt_dict(NEW_CELLS) + ",\n    ",)
s = s.replace(anchor, block[0] + '"known_cells_ORIG": {', 1)
open(p, "w", encoding="utf-8").write(s)
print("patched (orig cells preserved as known_cells_ORIG — merging next)")
