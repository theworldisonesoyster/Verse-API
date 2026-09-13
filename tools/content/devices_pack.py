# -*- coding: utf-8 -*-
# Fortnite.com/Devices 索引包：全部设备 C 级一句话（creative_device 族为 A/S 例外）
import json as _json
import os as _os

_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
_m = _json.load(open(_os.path.join(_ROOT, "manifest.json"), encoding="utf-8"))


def _find(n, name):
    if n.get("name") == name:
        return n
    for c in n.get("children", []):
        r = _find(c, name)
        if r:
            return r
    return None


_devices = _find(_m[2], "Devices")
_mem = {}


def _walk(n):
    if n["kind"] != "module" and n.get("linked", True):
        _mem[n["slug"]] = n
    for c in n.get("children", []):
        _walk(c)


_walk(_devices)

# 设备/成员中文名（按官网名称）
ZH = {
    "patchwork_device": "Patchwork 设备基类。",
    "lfo_modulator_device": "LFO 调制器：修改其他 Patchwork 设备的设置。",
    "drum_sequencer_device": "鼓音序器：为 Patchwork 创建鼓点节奏。",
    "song_sync_device": "歌曲同步设备。",
    "music_manager_device": "音乐管理器：为 Patchwork 提供共享的速度、调性与时间签名。",
    "value_setter_device": "数值设置器：修改其他 Patchwork 设备的设置。",
    "speaker_device": "扬声器：为玩家输出 Patchwork 音频。",
    "cable_splitter_device": "线缆分流器。",
    "note_trigger_device": "音符触发器：基于 Patchwork 输入向设备发送事件。",
    "echo_effect_device": "回声效果器：为 Patchwork 音频添加回声。",
    "distortion_effect_device": "失真效果器：为 Patchwork 音频添加失真。",
    "instrument_player_device": "乐器播放器：把 Patchwork 音符输入转为音频。",
    "omega_synthesizer_device": "Omega 合成器：把 Patchwork 音符输入转为音频。",
    "note_sequencer_device": "音符音序器：为 Patchwork 创建旋律音符模式。",
    "step_modulator_device": "步进调制器：修改其他 Patchwork 设备的设置。",
    "drum_player_device": "鼓播放器：把 Patchwork 音符输入转为音频。",
    "note_progressor_device": "音符推进器：按音阶转置 Patchwork 音符输入。",
    "creativeanimation_controller": "动画控制器：在创意物体上播放动画。",
    "cubic_bezier_parameters": "三次贝塞尔参数。",
    "keyframe_delta": "关键帧增量。",
    "linear": "插值类型：线性。",
    "ease": "插值类型：缓动。",
    "easein": "插值类型：缓入。",
    "easeout": "插值类型：缓出。",
    "easeinout": "插值类型：缓入缓出。",
    "vfx_spawner_device": "特效生成器。",
    "progress_based_mesh_device": "进度网格设备：随进度切换网格显示。",
    "vote_group_device": "投票组设备。",
    "vote_option_device": "投票选项设备。",
    "carryable_spawner_device": "可搬运物生成器。",
    "automated_turret_device": "自动炮塔。",
    "animated_mesh_device": "动画网格设备。",
    "reboot_van_device": "重生的士（复活车）。",
    "reboot_card_purchase_options": "重生的士卡片购买选项。",
    "post_process_device": "后期处理设备。",
    "item_remover_device": "物品移除设备。",
    "accolades_device": "成就设备。",
    "analytics_device": "分析统计设备。",
    "player_marker_device": "玩家标记设备。",
    "switch_device": "开关设备（多档选择器）。",
    "prop_mover_device": "道具移动设备。",
    "real_time_clock_device": "实时时钟设备。",
    "audio_mixer_device": "音频混音设备。",
    "audio_player_device": "音频播放设备。",
    "end_game_device": "结束游戏设备。",
    "elimination_feed_device": "淘汰信息流设备。",
    "firefly_spawner_device": "萤火虫生成器。",
    "input_trigger_device": "输入触发设备。",
    "item_placer_device": "物品放置设备。",
    "changing_booth_device": "更衣亭设备。",
    "customizable_light_device": "可自定义灯光设备。",
    "player_counter_device": "玩家计数设备。",
    "race_checkpoint_device": "竞速检查点设备。",
    "race_manager_device": "竞速管理设备。",
    "prop_manipulator_device": "道具操控设备。",
    "skydome_device": "天空穹顶设备。",
    "vfx_creator_device": "特效创作设备。",
    "map_controller_device": "地图控制器设备。",
    "volume_device": "体积设备。",
    "video_player_device": "视频播放设备。",
    "campfire_device": "篝火设备。",
    "barrier_device": "屏障设备。",
    "damage_volume_device": "伤害体积设备。",
    "effect_volume_device": "效果体积设备。",
    "fire_volume_device": "火焰体积设备。",
    "mutator_zone_device": "变异区域设备。",
    "skydive_volume_device": "跳伞体积设备。",
    "player_spawner_device": "玩家生成点。",
    "player_reference_device": "玩家引用设备。",
    "disguise_device": "伪装设备。",
    "crowd_volume_device": "人群体积设备。",
    "player_checkpoint_device": "玩家检查点设备。",
    "signal_remote_manager_device": "信号遥控管理设备。",
    "crash_pad_device": "缓冲垫（坠落保护）设备。",
    "fishing_zone_device": "钓鱼区域设备。",
    "hiding_prop_device": "隐藏道具设备。",
    "gameplay_controls_device": "玩法控制设备。",
    "gameplay_controls_side_scroller_device": "横版玩法控制设备。",
    "gameplay_controls_third_person_device": "第三人称玩法控制设备。",
    "spire_spike_device": "尖塔尖刺设备。",
    "dance_mannequin_device": "舞蹈人偶设备。",
    "creature_manager_device": "生物管理设备。",
    "creature_placer_device": "生物摆放设备。",
    "creature_spawner_device": "生物生成器。",
    "ai_patrol_path_device": "AI 巡逻路径设备。",
    "bouncer_device": "弹跳垫设备。",
    "service_station_device": "服务站设备（载具维修）。",
    "skilled_interaction_device": "技巧交互设备。",
    "gameplay_camera_device": "玩法相机设备。",
    "gameplay_camera_fixed_point_device": "固定点玩法相机。",
    "gameplay_camera_first_person_device": "第一人称玩法相机。",
    "gameplay_camera_fixed_angle_device": "固定角度玩法相机。",
    "gameplay_camera_orbit_device": "轨道环绕玩法相机。",
    "character_device": "角色设备。",
    "item_shop_device": "物品商店设备。",
    "advanced_storm_beacon_device": "高级风暴信标设备。",
    "advanced_storm_controller_device": "高级风暴控制器设备。",
    "air_vent_device": "通风口设备。",
    "attribute_evaluator_device": "属性评估设备。",
    "ball_spawner_device": "球生成器。",
    "base_item_spawner_device": "物品生成器基座。",
    "basic_storm_controller_device": "基础风暴控制器设备。",
    "beacon_device": "信标设备。",
    "billboard_device": "公告牌设备。",
    "button_device": "按钮设备。",
    "capture_area_device": "占领区域设备。",
    "capture_item_spawner_device": "占领物品生成器。",
    "channel_device": "频道设备。",
    "class_and_team_selector_device": "职业与队伍选择设备。",
    "class_designer_device": "职业设计器设备。",
    "collectible_object_device": "收集物设备。",
    "color_changing_tiles_device": "变色地砖设备。",
    "conditional_button_device": "条件按钮设备。",
    "damage_amplifier_powerup_device": "伤害放大强化道具。",
    "elimination_manager_device": "淘汰管理设备。",
    "experience_settings_device": "体验设置设备。",
    "explosive_device": "爆炸物设备。",
    "fuel_pump_device": "油泵设备。",
    "grind_powerup_device": "滑轨强化道具。",
    "holoscreen_device": "全息屏设备。",
    "hud_message_device": "HUD 消息设备。",
    "item_granter_device": "物品授予设备。",
    "item_spawner_device": "物品生成器。",
    "lock_device": "锁具设备。",
    "map_indicator_device": "地图指示器设备。",
    "matchmaking_portal_device": "匹配传送门设备。",
    "movement_modulator_device": "移动调制设备。",
    "objective_device": "目标设备。",
    "perception_trigger_device": "感知触发设备。",
    "pinball_bumper_device": "弹球缓冲器设备。",
    "pinball_flipper_device": "弹球挡板设备。",
    "powerup_device": "强化道具设备。",
    "prop_o_matic_device": "道具伪装（Prop-O-Matic）设备。",
    "prop_o_matic_manager_device": "道具伪装管理设备。",
    "prop_spawner_base_device": "道具生成器基座。",
    "pulse_trigger_device": "脉冲触发设备。",
    "radio_device": "广播设备。",
    "rng_device": "随机数（RNG）设备。",
    "round_settings_device": "回合设置设备。",
    "score_manager_device": "比分管理设备。",
    "shooting_range_target_device": "射击场靶标设备。",
    "shooting_range_target_track_device": "射击场靶轨设备。",
    "storm_controller_device": "风暴控制器设备。",
    "support_a_creator_device": "支持创作者设备。",
    "sword_in_the_stone_device": "石中剑设备。",
    "team_settings_and_inventory_device": "队伍设置与物品栏设备。",
    "teleporter_device": "传送器设备。",
    "timed_objective_device": "限时目标设备。",
    "timer_device": "计时器设备。",
    "tracker_device": "追踪器设备。",
    "trick_tile_device": "特技地砖设备。",
    "trigger_base_device": "触发器基类设备。",
    "trigger_device": "触发器设备。",
    "vending_machine_device": "自动售货机设备。",
    "visual_effect_powerup_device": "视觉特效强化道具。",
    "water_device": "水体设备。",
    "chair_device": "椅子设备。",
    "hud_controller_device": "HUD 控制器设备。",
    "vehicle_mod_box_spawner_device": "载具改装箱生成器。",
    "vehicle_mod_box_settings": "载具改装箱设置。",
    "vehicle_spawner_device": "载具生成器。",
    "player_movement_settings_device": "玩家移动设置设备。",
    "class_selector_ui_device": "职业选择 UI 设备。",
    "popup_dialog_device": "弹出对话框设备。",
    "stat_creator_device": "统计创建器设备。",
    "stat_powerup_device": "统计强化道具。",
    "physics_boulder_device": "物理巨石设备。",
    "physics_object_base_device": "物理对象基类设备。",
    "physics_tree_device": "物理树设备。",
    "health_powerup_device": "生命强化道具。",
    "roly_poly_spawner_device": "不倒翁生成器。",
    "roly_poly": "不倒翁。",
    "nitro_hoop_device": "氮气环设备。",
    "wilds_plant_device": "荒野植物设备。",
    "grind_rail_device": "滑轨设备。",
    "vine_rail_device": "藤蔓滑轨设备。",
    "sentry_device": "哨戒炮设备。",
    "rift_point_volume_device": "裂隙点体积设备。",
    "down_but_not_out_device": "倒地未淘汰设备。",
    "npc_spawner_device": "NPC 生成器。",
    "healing_cactus_device": "治疗仙人掌设备。",
    "wildlife_spawner_device": "野生动物生成器。",
    "hive_stash_device": "蜂巢储藏设备。",
    "scout_spire_device": "侦察尖塔设备。",
    "cinematic_sequence_device": "过场动画序列设备。",
    "bank_vault_device": "银行金库设备。",
    "hero_chest_device": "英雄宝箱设备。",
    "overlord_spire_device": "统领尖塔设备。",
    "supply_drop_spawner_device": "补给drop生成器。",
    "creative_object": "创意对象接口的类表示。",
    "creative_prop": "创意道具：场景中的物件。",
    "creative_prop_asset": "创意道具资产。",
    "creative_device_asset": "创意设备资产。",
    "device_ai_interaction_result": "设备 AI 交互结果。",
    "carryable_spawner_agent_impact_result": "可搬运物生成器的代理撞击结果。",
    "conversation_device": "对话设备。",
    "earth_sprite_device": "大地精灵（earth sprite）设备。",
    "guard_spawner_device": "Guard（守卫）生成器。",
    "nitro_barrel_spawner_device": "氮气桶生成器。",
    "vehicle_spawner_getaway_device": "逃亡载具生成器。",
    "emp_volume_hazard_rocketracing_device": "火箭竞速 EMP 体积危险设备。",
    "defaultcreativepropasset": "默认创意道具资产。",
    # 枚举/接口等
    "vote_option_interface": "投票选项接口。",
    "bank_vault_interface": "银行金库接口。",
    "reboot_van_interface": "重生的士接口。",
    "has_spire_functionality": "尖塔功能接口。",
    "creative_object_interface": "创意对象通用接口。",
    "progress_device_state": "进度设备状态枚举。",
    "reboot_progress_decay_behavior": "重生的士进度衰减行为枚举。",
    "spawn_on_enable_behavior": "启用时生成行为枚举。",
    "guard_spawner_accuracy": "Guard 生成器精度枚举。",
    "guard_spawner_visibility_range_restriction": "Guard 生成器视野范围限制枚举。",
    "hive_stash_style": "蜂巢储藏样式枚举。",
    "hero_chest_rank": "英雄宝箱等级枚举。",
    "spawn_prop_result": "生成道具的结果枚举。",
    "move_to_result": "MoveTo 的结果枚举。",
    "animation_mode": "动画模式枚举。",
    "animation_controller_state": "动画控制器状态枚举。",
    "await_next_keyframe_result": "等待下一关键帧的结果枚举。",
}

entries = {}
for slug, mem in _mem.items():
    name_key = slug.rsplit("/", 1)[-1].replace("-", "")
    zh = ZH.get(name_key)
    if zh is None:
        base = name_key[:-2] if name_key.endswith("device") else name_key
        zh = ZH.get(base) or f"创意设备（Devices 索引）。"
    entries[slug] = {"zh": zh}

PACKS = [
    {
        "outdir": "03_Fortnite.com/070_Devices", "module_slug": "fortnitedotcom/devices",
        "overview_title": "Devices module", "overview_grade": "C",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices",
        "overview": {"zh": "创意设备索引（按约定仅一句话索引，不逐设备详解）：生成器、触发器、风暴、竞速、计分、载具生成等全套创意玩法设备；Patchwork 音乐设备族与创意动画控制器的基类例外（creative_device 另有 S 级详解页）。"},
        "known_cells": {
            "Base class for creative devices and props.": "创意设备与道具的基类。",
            "Triggered when a vote is cast by ‘agent’": "「agent」投票时触发。",
            "Triggers when Reboot Van has finished recharging. agent is the last interacting player.":
                "重生的士完成充能时触发；agent 为最后交互的玩家。",
            "Signaled each time a keyframe is reached. Callback(KeyframeIndex:int, InReverse:logic). Note that the KeyframeIndex in the callback payload is 0-indexed.":
                "每到达一个关键帧时触发。回调参数（关键帧序号:int, 是否反向:logic)；载荷中的序号从 0 起。",
            "Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is any doubt.":
                "返回 creative_object 的变换（厘米）。只要有疑问，调用前必须先检查 creative_object.IsValid。",
            "Implemented by objects to allow reading position information.": "由对象实现，允许读取位置信息。",
            "Implemented by classes whose instances can be enabled and disabled.": "由「实例可被启用/禁用」的类实现。",
        },
        "entries": entries,
    },
]

try:
    from devices_cells_extra import EXTRA_CELLS
    for _pk in PACKS:
        _pk.setdefault("known_cells", {}).update(EXTRA_CELLS)
except ImportError:
    pass
