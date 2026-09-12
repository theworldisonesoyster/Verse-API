# -*- coding: utf-8 -*-
"""
grades.py — 分级判定（阶段1强模型审定结果，阶段2不得改判）
匹配顺序: EXACT(slug精确) → RULES(模块前缀+名称正则,按序) → MODULE_DEFAULT(模块默认)
grade: S核心/A常用/B进阶/C参考  depth: S,A→full  B→brief  C→oneliner
"""
import re

EXACT = {
    # ---- Simulation（样板模块）----
    "versedotorg/simulation/sleep": "S",
    "versedotorg/simulation/agent": "S",
    "versedotorg/simulation/player": "S",
    "versedotorg/simulation/team": "A",
    "versedotorg/simulation/session": "A",
    "versedotorg/simulation/getsession": "A",
    "versedotorg/simulation/getsimulationelapsedtime": "A",
    "versedotorg/simulation/editable_slider": "S",
    "versedotorg/simulation/editable_number": "S",
    "versedotorg/simulation/editable_vector_slider": "A",
    "versedotorg/simulation/editable_vector_number": "A",
    "versedotorg/simulation/session_environment": "B",
    # ---- Verse 核心函数 ----
    "versedotorg/verse/print": "S", "versedotorg/verse/print-1": "S", "versedotorg/verse/print-2": "S",
    "versedotorg/verse/event/event(t)": "S", "versedotorg/verse/event": "S", "versedotorg/verse/event-1": "S",
    "versedotorg/verse/listenable": "S", "versedotorg/verse/listenable-1": "S",
    "versedotorg/verse/subscribable": "A", "versedotorg/verse/subscribable-1": "A",
    "versedotorg/verse/signalable": "A",
    "versedotorg/verse/result": "A", "versedotorg/verse/makesuccess": "A", "versedotorg/verse/makeerror": "A",
    "versedotorg/verse/tostring": "A", "versedotorg/verse/tostring-1": "A",
    "versedotorg/verse/tostring-2": "A", "versedotorg/verse/tostring-3": "A",
    "versedotorg/verse/join": "A", "versedotorg/verse/join-1": "A",
    "versedotorg/verse/concatenate": "A", "versedotorg/verse/concatenatemaps": "B",
    "versedotorg/verse/localize": "B", "versedotorg/verse/message": "B", "versedotorg/verse/locale": "B",
    "versedotorg/verse/getsecondssinceepoch": "B",
    "versedotorg/verse/weak_map": "B", "versedotorg/verse/fitsinplayermap": "C",
    "versedotorg/verse/classifiable_subset": "C",
    "versedotorg/verse/classifiable_subset/classifiable_subset(element_type)": "C",
    "versedotorg/verse/makeclassifiablesubset": "C",
    "versedotorg/verse/diagnostic": "B", "versedotorg/verse/todiagnostic": "B", "versedotorg/verse/err": "B",
    "versedotorg/verse/modifier": "C", "versedotorg/verse/modifier_stack": "C",
    "versedotorg/verse/modifier_stack/modifier_stack(t)": "C",
    "versedotorg/verse/abs": "A", "versedotorg/verse/abs-1": "A",
    "versedotorg/verse/min": "A", "versedotorg/verse/min-1": "A",
    "versedotorg/verse/max": "A", "versedotorg/verse/max-1": "A",
    "versedotorg/verse/clamp": "A", "versedotorg/verse/clamp-1": "A",
    "versedotorg/verse/ceil": "A", "versedotorg/verse/ceil-1": "A",
    "versedotorg/verse/floor": "A", "versedotorg/verse/floor-1": "A",
    "versedotorg/verse/round": "A", "versedotorg/verse/int": "A",
    "versedotorg/verse/operatorequals": "S", "versedotorg/verse/operatorlessgreater": "S",
    "versedotorg/verse/operatorquestionmark": "A", "versedotorg/verse/operatorquestionmark-1": "A",
    # ---- Random ----
    "versedotorg/random/getrandomint": "S", "versedotorg/random/getrandomfloat": "S",
    "versedotorg/random/shuffle": "A",
    # ---- SpatialMath ----
    "versedotorg/spatialmath/vector3": "S", "versedotorg/spatialmath/rotation": "S",
    "versedotorg/spatialmath/transform": "S",
    "versedotorg/spatialmath/distance": "A", "versedotorg/spatialmath/distance-1": "A",
    "versedotorg/spatialmath/dotproduct": "A", "versedotorg/spatialmath/crossproduct": "A",
    "versedotorg/spatialmath/crossproductlefthanded": "A", "versedotorg/spatialmath/lerp": "A",
    "versedotorg/spatialmath/degreesradians": "A",
    # ---- SceneGraph ----
    "versedotorg/scenegraph/entity": "S", "versedotorg/scenegraph/component": "S",
    "versedotorg/scenegraph/transform_component": "S", "versedotorg/scenegraph/mesh_component": "S",
    "versedotorg/scenegraph/tick_events": "S",
    "versedotorg/scenegraph/entity_prefab": "A", "versedotorg/scenegraph/sound_component": "A",
    "versedotorg/scenegraph/particle_system_component": "A",
    "versedotorg/scenegraph/skeletal_animation": "A", "versedotorg/scenegraph/skeleton": "A",
    "versedotorg/scenegraph/camera_component": "A",
    "versedotorg/scenegraph/interactable_component": "A",
    "versedotorg/scenegraph/basic_interactable_component": "A",
    # ---- Concurrency / Assets ----
    "versedotorg/concurrency/task/task(t)": "A", "versedotorg/concurrency/task": "A",
    "versedotorg/assets/mesh": "A", "versedotorg/assets/texture": "A", "versedotorg/assets/material": "A",
    "versedotorg/assets/sound_wave": "A", "versedotorg/assets/animation_sequence": "A",
    "versedotorg/assets/particle_system": "A",
    "versedotorg/assets/input_action/input_action(t)": "A", "versedotorg/assets/input_action": "A",
    "versedotorg/assets/input_mapping": "A",
    # ---- Temporary/UI ----
    "unrealenginedotcom/temporary/ui/player_ui": "S",
    "unrealenginedotcom/temporary/ui/widget": "S",
    "unrealenginedotcom/temporary/ui/getplayerui": "S",
    # ---- UE.com 其他 ----
    "unrealenginedotcom/temporary/sortby": "A",
    "unrealenginedotcom/json/value": "A", "unrealenginedotcom/json/parse": "A",
    "unrealenginedotcom/controlinput/player_input": "A",
    "unrealenginedotcom/controlinput/getplayerinput": "A",
    "unrealenginedotcom/temporary/diagnostics/log": "A",
    "unrealenginedotcom/itemization/inventory_component": "A",
    "unrealenginedotcom/itemization/item_component": "A",
    # ---- Fortnite.com ----
    "fortnitedotcom/characters/fort_character": "S",
    "fortnitedotcom/animation/playanimation/playanimation": "S",
    "fortnitedotcom/devices/creative_device": "S",
    "fortnitedotcom/devices/creative_device_base": "A",
    "fortnitedotcom/devices/creative_object": "A",
    "fortnitedotcom/devices/creative_prop": "A",
    "fortnitedotcom/devices/creative_object_interface": "A",
    "fortnitedotcom/devices/spawnprop": "A", "versedotorg/devices/spawnprop-1": "A",
    "fortnitedotcom/devices/getcreativeobjectswithtag": "A",
    "fortnitedotcom/devices/getcreativeobjectswithtags": "A",
    "fortnitedotcom/ui/text_button_base": "A",
    "fortnitedotcom/ui/button_loud": "A", "fortnitedotcom/ui/button_regular": "A",
    "fortnitedotcom/ui/button_quiet": "A", "fortnitedotcom/ui/slider_regular": "A",
    "fortnitedotcom/ui/text_block": "A",
    "fortnitedotcom/ai/navigatable": "A", "fortnitedotcom/ai/npc_behavior": "A",
    "fortnitedotcom/ai/maketarget": "A", "fortnitedotcom/ai/maketarget-1": "A", "fortnitedotcom/ai/maketarget-2": "A",
}

# (模块slug前缀, 名称正则, grade) —— 按序首条命中
RULES = [
    # Verse 运算符/位运算/三角超越
    ("versedotorg/verse", r"^operator", "B"),
    ("versedotorg/verse", r"^(bitand|bitor|bitxor|bitnot)$", "C"),
    ("versedotorg/verse", r"^(sqrt|sin|cos|tan|arcsin|arccos|arctan|sinh|cosh|tanh|arsinh|arcosh|artanh|pow|quotient|mod|exp|ln|log|lerp|sgn|isalmostequal)$", "B"),
    ("versedotorg/verse", r"^(inf|nan|pifloat)$", "B"),
    # Verse 类/接口
    ("versedotorg/verse", r"^(cancelable|disposable|enableable|invalidatable|showable)$", "B"),
    # Verse.org 各子模块默认细化
    ("versedotorg/verse/easing", r".", "B"),
    ("versedotorg/chat", r"error|interface", "C"),
    ("versedotorg/chat", r".", "B"),
    ("versedotorg/scenegraph", r"error|result|_state$", "C"),
    ("versedotorg/scenegraph", r"^(icon_component|float_range|easing_window|entity_origin|execution_listenable|possessable_component)$", "B"),
    ("versedotorg/scenegraph", r"^(rarity|common_rarity|uncommon_rarity|rare_rarity|epic_rarity|legendary_rarity|rarity_component|stackable_component|basic_stackable_component|change_stack_size_result|change_max_stack_size_result)$", "B"),
    ("versedotorg/scenegraph", r"camera_|collision_|overlap_hit|sweep_hit", "B"),
    ("versedotorg/scenegraph", r"light_component|_light_component", "B"),
    ("versedotorg/scenegraph", r"interactable_", "B"),
    ("versedotorg/scenegraph", r"^(has_camera_modifier|easeable|scene_event|origin|has_merge_rules)$", "C"),
    ("versedotorg/scenegraph/collisionchannels", r".", "B"),
    ("versedotorg/scenegraph/collisionprofiles", r".", "C"),
    ("versedotorg/scenegraph/keyframedmovement", r"keyframed_movement_component", "A"),
    ("versedotorg/scenegraph/keyframedmovement", r".", "B"),
    ("versedotorg/progression", r"error", "C"),
    ("versedotorg/progression", r".", "B"),
    ("versedotorg/timeline", r".", "B"),
    ("versedotorg/presentation", r".", "C"),
    ("versedotorg/input", r"^(getplayerinput|player_input|input_events|input_events\(t\))$", "A"),
    ("versedotorg/input", r".", "B"),
    ("versedotorg/input/gameplay", r".", "C"),
    ("versedotorg/input/ui", r".", "C"),
    ("versedotorg/agentgroup", r"error|interface", "C"),
    ("versedotorg/agentgroup", r".", "B"),
    ("versedotorg/simulation/tags", r"^(tag|tag_key|has_tags|tag_view)$", "A"),
    ("versedotorg/simulation/tags", r"tag_search_criteria", "B"),
    ("versedotorg/simulation/tags", r".", "C"),
    ("versedotorg/colors", r"^operator", "C"),
    ("versedotorg/colors", r"makecolorfromtemperature|over", "B"),
    ("versedotorg/colors", r".", "A"),
    ("versedotorg/colors/namedcolors", r".", "C"),
    ("versedotorg/spatialmath", r"^(slerp|reflectvector|angulardistance.*|distance.*forward.*|isalmostequal|tostring)$", "B"),
    ("versedotorg/spatialmath", r"^operator|^(makerotation|degreestoradians|radianstodegrees|identityrotation|distance)", "A"),
    ("versedotorg/spatialmath", r".", "A"),
    ("versedotorg/random", r".", "A"),
    ("versedotorg/concurrency", r"awaitable", "B"),
    ("versedotorg/assets", r"has_icon", "C"),
    ("versedotorg/assets", r".", "A"),
    # UnrealEngine.com
    ("unrealenginedotcom/progression", r"error", "C"),
    ("unrealenginedotcom/progression", r".", "B"),
    ("unrealenginedotcom/itemization", r"error|_result$", "C"),
    ("unrealenginedotcom/itemization", r".", "B"),
    ("unrealenginedotcom/webapi", r"client_id", "C"),
    ("unrealenginedotcom/webapi", r".", "B"),
    ("unrealenginedotcom/temporary/ui", r"^u?i?_?slot$|slot", "A"),
    ("unrealenginedotcom/temporary/ui", r"^(anchors|margin|widget_message)$", "B"),
    ("unrealenginedotcom/temporary/ui", r"^(ui_input_mode|widget_visibility|orientation|horizontal_alignment|vertical_alignment|image_tiling|text_justification|text_overflow_policy|text_wrapping_policy)$", "B"),
    ("unrealenginedotcom/temporary/ui", r".", "A"),
    ("unrealenginedotcom/temporary/curves", r".", "B"),
    ("unrealenginedotcom/temporary/diagnostics", r"^(debug_draw_channel|debug_draw_duration_policy|log_level|log_channel)$", "C"),
    ("unrealenginedotcom/temporary/diagnostics", r".", "B"),
    ("unrealenginedotcom/social", r".", "C"),
    ("unrealenginedotcom/basicshapes", r".", "C"),
    ("unrealenginedotcom/abilities", r"^(cancel_reason|ability_removed_from_scene)$", "C"),
    ("unrealenginedotcom/abilities", r".", "B"),
    ("unrealenginedotcom/controlinput", r".", "B"),
    ("unrealenginedotcom/controlinput", r"^(player_input|getplayerinput)$", "A"),
    ("unrealenginedotcom/assets", r".", "B"),
    # Fortnite.com
    ("fortnitedotcom/ui", r"^(creative_hud_identifier|player_hud_identifier|hud_identifier)", "C"),
    ("fortnitedotcom/ui", r"^(hud_element_identifier|fort_hud_controller)$", "B"),
    ("fortnitedotcom/ui", r".", "A"),
    ("fortnitedotcom/ai", r"^(equipped_sidekick_component|spark_mode_component)$", "C"),
    ("fortnitedotcom/ai", r"_error_type$|_success_type$|movement_type|alert_level|mood|reaction", "C"),
    ("fortnitedotcom/ai", r".", "B"),
    ("fortnitedotcom/ai/movement_types", r".", "C"),
    ("fortnitedotcom/animation", r".", "A"),
    ("fortnitedotcom/characters", r"stasis_args", "C"),
    ("fortnitedotcom/characters", r".", "A"),
    ("fortnitedotcom/vehicles", r".", "B"),
    ("fortnitedotcom/devices/patchwork", r".", "C"),
    ("fortnitedotcom/devices/creativeanimation", r"^(animation_controller)$", "B"),
    ("fortnitedotcom/devices/creativeanimation", r".", "C"),
    ("fortnitedotcom/devices/creativeanimation/interpolationtypes", r".", "C"),
    ("fortnitedotcom/devices", r"_device$", "C"),
    ("fortnitedotcom/devices", r"_device_|_settings$", "C"),
    ("fortnitedotcom/devices", r"error|_result$|_state$|_behavior$|_accuracy$|_style$|_rank$", "C"),
    ("fortnitedotcom/devices", r"interface$", "B"),
    ("fortnitedotcom/devices", r".", "C"),
]

# 模块级默认（成员无规则命中时）与模块总览页 grade
MODULE_DEFAULT = {
    "versedotorg": "S", "versedotorg/verse": "B", "versedotorg/verse/easing": "B",
    "versedotorg/chat": "B", "versedotorg/scenegraph": "B",
    "versedotorg/scenegraph/collisionchannels": "B",
    "versedotorg/scenegraph/collisionprofiles": "C",
    "versedotorg/scenegraph/keyframedmovement": "B",
    "versedotorg/progression": "B", "versedotorg/timeline": "B",
    "versedotorg/presentation": "C", "versedotorg/input": "A",
    "versedotorg/agentgroup": "B", "versedotorg/simulation": "S",
    "versedotorg/simulation/tags": "A", "versedotorg/assets": "A",
    "versedotorg/colors": "A", "versedotorg/colors/namedcolors": "C",
    "versedotorg/spatialmath": "A", "versedotorg/random": "A",
    "versedotorg/predicts": "C", "versedotorg/concurrency": "A",
    "unrealenginedotcom": "B", "unrealenginedotcom/conversations": "C",
    "unrealenginedotcom/progression": "B", "unrealenginedotcom/itemization": "B",
    "unrealenginedotcom/webapi": "B", "unrealenginedotcom/temporary": "A",
    "unrealenginedotcom/temporary/ui": "S", "unrealenginedotcom/temporary/curves": "B",
    "unrealenginedotcom/temporary/diagnostics": "B",
    "unrealenginedotcom/temporary/spatialmath": "C", "unrealenginedotcom/social": "C",
    "unrealenginedotcom/json": "A", "unrealenginedotcom/basicshapes": "C",
    "unrealenginedotcom/abilities": "B", "unrealenginedotcom/controlinput": "A",
    "unrealenginedotcom/assets": "B",
    "fortnitedotcom": "B", "fortnitedotcom/ui": "C", "fortnitedotcom/ai": "B",
    "fortnitedotcom/animation": "A", "fortnitedotcom/characters": "S",
    "fortnitedotcom/vehicles": "B", "fortnitedotcom/devices": "C",
    "fortnitedotcom/devices/patchwork": "C",
    "fortnitedotcom/devices/creativeanimation": "C",
    "fortnitedotcom/devices/creativeanimation/interpolationtypes": "C",
}

GRADE_ORDER = ["S", "A", "B", "C"]
DEPTH = {"S": "full", "A": "full", "B": "brief", "C": "oneliner"}


def grade_of(slug: str, name: str, kind: str) -> str:
    if kind == "module":
        return MODULE_DEFAULT.get(slug, "C")
    if slug in EXACT:
        return EXACT[slug]
    for prefix, pat, g in RULES:
        if slug.startswith(prefix) and re.search(pat, name, re.I):
            return g
    # 找最近父模块默认
    parts = slug.split("/")
    while parts:
        parts.pop()
        key = "/".join(parts)
        if key in MODULE_DEFAULT:
            return MODULE_DEFAULT[key]
    return "C"
