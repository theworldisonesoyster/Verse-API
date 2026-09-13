# -*- coding: utf-8 -*-
# Fortnite.com 非 Devices 部分：UI / AI / Animation / Characters / Vehicles
HUD_ZH = {
    "all": "全部元素", "build_menu": "建造菜单", "crafting_resources": "制作资源",
    "elimination_counter": "淘汰计数", "equipped_item": "已装备物品",
    "experience_level": "经验等级", "experience_supercharged": "经验超载状态",
    "experience_ui": "经验 UI", "health": "生命值", "health_numbers": "生命值数字",
    "hud_info": "HUD 信息", "interaction_prompts": "交互提示", "map_prompts": "地图提示",
    "mimimap": "小地图（官网拼写变体）", "minimap": "小地图", "pickup_stream": "拾取提示流",
    "player_count": "玩家数量", "player_inventory": "玩家物品栏",
    "round_info": "回合信息", "round_timer": "回合计时", "shield_numbers": "护盾数字",
    "shileds": "护盾（官网拼写变体）", "shields": "护盾", "storm_notifications": "风暴通知",
    "storm_timer": "风暴计时", "team_info": "队伍信息",
}
entries = {}
for key, zh in HUD_ZH.items():
    entries[f"fortnitedotcom/ui/creative_hud_identifier_{key}"] = {"zh": f"创意 HUD 元素标识：{zh}。"}
for key, zh in [("all", "全部元素")]:
    entries[f"fortnitedotcom/ui/player_hud_identifier_{key}"] = {"zh": f"玩家 HUD 元素标识：{zh}。"}
for key, zh in [("wood", "木材"), ("stone", "石料"), ("metal", "金属"),
                ("permanite", "永久金属"), ("gold_currency", "金币货币"), ("ingredient", "配料")]:
    entries[f"fortnitedotcom/ui/hud_identifier_world_resource_{key}"] = {"zh": f"世界资源 HUD 标识：{zh}。"}
for key, zh in [("weapons", "武器"), ("loot", "战利品"), ("movement", "移动"),
                ("vehicle", "载具"), ("healing", "治疗"), ("all", "全部")]:
    entries[f"fortnitedotcom/ui/hud_identifier_visual_sound_effect_{key}"] = {"zh": f"视觉音效 HUD 标识：{zh}。"}

entries.update({
    # UI
    "fortnitedotcom/ui/text_button_base": {"zh": "带文本消息的按钮通用基类：显示一个带自定义消息文本的按钮。"},
    "fortnitedotcom/ui/button_loud": {"zh": "大号醒目（loud）样式的文本按钮。"},
    "fortnitedotcom/ui/button_regular": {"zh": "普通样式的文本按钮。"},
    "fortnitedotcom/ui/button_quiet": {"zh": "低调（quiet）样式的文本按钮。"},
    "fortnitedotcom/ui/hud_element_identifier": {"zh": "用于标识一个 HUD 元素。"},
    "fortnitedotcom/ui/slider_regular": {"zh": "带文本值的滑条：显示滑条、进度条与数值。"},
    "fortnitedotcom/ui/text_block": {"zh": "文本块控件：向用户显示文本。"},
    "fortnitedotcom/ui/fort_hud_controller": {"zh": "HUD 控制器：显示/隐藏各类 HUD 元素。"},
    # AI
    "fortnitedotcom/ai/movement_types/walking": {"zh": "移动类型：行走。"},
    "fortnitedotcom/ai/movement_types/running": {"zh": "移动类型：奔跑。"},
    "fortnitedotcom/ai/equipped_sidekick_component": {"zh": "管理代理已装备 Sidekick（伙伴）专属功能的组件。"},
    "fortnitedotcom/ai/spark_mode_component": {"zh": "管理支持 Spark 模式的实体的组件：Spark 模式会把实体变作漂浮的火花。"},
    "fortnitedotcom/ai/guard_actions_component": {"zh": "堡垒之夜 Guard（守卫）的 AI 行为管理。"},
    "fortnitedotcom/ai/guard_awareness_component": {"zh": "堡垒之夜 Guard 的感知管理。"},
    "fortnitedotcom/ai/navigation_target": {"zh": "导航目标。"},
    "fortnitedotcom/ai/npc_actions_component": {"zh": "堡垒之夜 NPC 的 AI 行为管理。"},
    "fortnitedotcom/ai/npc_awareness_component": {"zh": "堡垒之夜 NPC 的感知管理。"},
    "fortnitedotcom/ai/npc_behavior": {"zh": "继承它来创建自定义 NPC 行为。npc_behavior 可在 CharacterDefinition 资产或 npc_spawner_device 中为角色指定。"},
    "fortnitedotcom/ai/npc_target_info": {"zh": "关于被感知目标的信息。"},
    "fortnitedotcom/ai/sidekick_component": {"zh": "管理所有 Sidekick 类型共享功能的组件。"},
    "fortnitedotcom/ai/npc_sidekick_component": {"zh": "管理 NPC Sidekick 专属功能的组件。"},
    "fortnitedotcom/ai/focus_interface": {"zh": "关注（focus）能力接口。"},
    "fortnitedotcom/ai/fort_leashable": {"zh": "可被拴留（leash，限制活动范围）的接口。"},
    "fortnitedotcom/ai/navigatable": {"zh": "可寻路（navigatable）接口。"},
    "fortnitedotcom/ai/makenavigationtarget": {"zh": "从任意位置生成 navigation_target。"},
    "fortnitedotcom/ai/makenavigationtarget-1": {"zh": "从任意位置生成 navigation_target（重载）。"},
    "fortnitedotcom/ai/makenavigationtarget-2": {"zh": "从代理（agent）生成 navigation_target。"},
    "fortnitedotcom/ai/ai_action_error_type": {"zh": "AI 动作失败的结果类型。"},
    "fortnitedotcom/ai/navigation_result": {"zh": "导航请求的结果。"},
    "fortnitedotcom/ai/navigation_action_error_type": {"zh": "导航动作失败类型。"},
    "fortnitedotcom/ai/navigation_action_success_type": {"zh": "导航动作成功类型。"},
    "fortnitedotcom/ai/movement_type": {"zh": "移动类型枚举。"},
    "fortnitedotcom/ai/guard_alert_level": {"zh": "堡垒之夜 Guard 的各级警戒级别。"},
    "fortnitedotcom/ai/sidekick_mood": {"zh": "Sidekick 的情绪列表——情绪会改变其动画表现。"},
    "fortnitedotcom/ai/sidekick_reaction": {"zh": "Sidekick 可播放的反应动作集合。"},
    # Animation
    "fortnitedotcom/animation/playanimation/play_animation_instance": {"zh": "由 play_animation_controller.Play 创建的动画实例，可查询与操控。"},
    "fortnitedotcom/animation/playanimation/play_animation_controller": {"zh": "在对象上播放动画的接口。"},
    "fortnitedotcom/animation/playanimation/play_animation_result": {"zh": "PlayAndAwait 请求的结果。"},
    "fortnitedotcom/animation/playanimation/play_animation_state": {"zh": "播放动画实例的可能状态。"},
    # Characters
    "fortnitedotcom/characters/stasis_args": {"zh": "fort_character.PutInStasis 函数的参数（凝固时阻止哪些移动类型）。"},
    # Vehicles
    "fortnitedotcom/vehicles/fort_vehicle_seat": {"zh": "表示 fort_vehicle 中的一个座位。"},
    "fortnitedotcom/vehicles/fort_vehicle": {"zh": "由堡垒之夜载具实现的主 API。"},
})

PACKS = [
    {
        "outdir": "03_Fortnite.com/010_UI", "module_slug": "fortnitedotcom/ui",
        "overview_title": "UI module", "overview_grade": "A",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ui",
        "overview": {"zh": "堡垒之夜风格的 UI 控件：文本按钮（三种样式）、滑条、文本块，以及用于隐藏/显示各类 HUD 元素的标识符族。"},
        "entries": entries,
    },
    {
        "outdir": "03_Fortnite.com/060_AI", "module_slug": "fortnitedotcom/ai",
        "overview_title": "AI module", "overview_grade": "B",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai",
        "overview": {"zh": "AI 相关：NPC/Guard 行为与感知组件、导航目标、Sidekick 伙伴，以及导航/动作的结果与错误类型。"},
        "submodules": [{"name": "movement_types", "link": "010_movement_types/_overview.md",
                        "zh": "移动类型常量（行走/奔跑）。"}],
        "sub_outdirs": {"fortnitedotcom/ai/movement_types": "03_Fortnite.com/060_AI/010_movement_types"},
        "entries": entries,
    },
    {
        "outdir": "03_Fortnite.com/110_Animation", "module_slug": "fortnitedotcom/animation",
        "overview_title": "Animation module", "overview_grade": "A",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/animation",
        "overview": {"zh": "动画播放：play_animation_controller 可在对象上播放动画，返回可查询/操控的动画实例。"},
        "submodules": [{"name": "PlayAnimation", "link": "010_PlayAnimation/_overview.md",
                        "zh": "播放动画的控制器、实例、结果与状态。"}],
        "sub_outdirs": {"fortnitedotcom/animation/playanimation": "03_Fortnite.com/110_Animation/010_PlayAnimation"},
        "entries": entries,
    },
    {
        "outdir": "03_Fortnite.com/130_Characters", "module_slug": "fortnitedotcom/characters",
        "overview_title": "Characters module", "overview_grade": "S",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/characters",
        "overview": {"zh": "角色（fort_character）：玩家/NPC 在世界中的身体，承担移动、跳跃、淘汰、生命等玩法。"},
        "entries": entries,
    },
    {
        "outdir": "03_Fortnite.com/180_Vehicles", "module_slug": "fortnitedotcom/vehicles",
        "overview_title": "Vehicles module", "overview_grade": "B",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/vehicles",
        "overview": {"zh": "载具：fort_vehicle 与其座位。"},
        "entries": entries,
    },
]

try:
    from fort_cells_extra import EXTRA_CELLS
    for _pk in PACKS:
        _pk.setdefault("known_cells", {}).update(EXTRA_CELLS)
except ImportError:
    pass
