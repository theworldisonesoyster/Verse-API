# -*- coding: utf-8 -*-
"""fill_pending.py — 为官网空描述格补名称语义中文注（按 _pending_translation.txt 定位）"""
import re

ZH = {
    "Group": "此成员信息关联的组。",
    "X0": "P1 控制点的 X 值；须在 0.0~1.0 之间。",
    "X1": "P2 控制点的 X 值；须在 0.0~1.0 之间。",
    "Y0": "P1 控制点的 Y 值。",
    "Y1": "P2 控制点的 Y 值。",
    "Evaluate": "在指定时间 t 求缓动曲线值并返回。",
    "ChangeMaxStackSizeEvent": "最大堆叠数变化时触发。",
    "ChangeStackSizeEvent": "堆叠数变化时触发。",
    "Split": "把当前堆叠拆分为两份。",
    "DrivingBlend": "驱动混合（DrivingBlend）的相机模式。",
    "Blend": "过渡所使用的混合模式。",
    "Extents": "碰撞盒的半尺寸（各轴范围）。",
    "Color": "此稀有度的代表颜色。",
    "Entity": "此原点所属的实体。",
    "GetTransform": "获取原点变换。",
    "Minimum": "范围最小值。",
    "Maximum": "范围最大值。",
    "CameraModifiers": "此组件持有的相机修饰符栈。",
    "Icon": "实体/技能的图标。",
    "Play": "播放粒子模拟。",
    "Stop": "停止粒子模拟。",
    "AutoPlay": "加入场景时是否自动播放。",
    "Enabled": "此组件是否启用。",
    "Gamepad": "手柄是否可用。",
    "Keyboard": "键盘是否可用。",
    "Mouse": "鼠标是否可用。",
    "Touch": "触摸屏是否可用。",
    "Await": "挂起等待此任务完成。",
    "Item": "相关物品实体。",
    "Inventory": "相关物品栏组件。",
    "Errors": "查询后收集到的错误列表。",
    "AddError": "添加物品阶段的错误。",
    "ItemComponent": "候选的物品栏组件。",
    "ChosenInventory": "被选中的物品栏。",
    "ChosenInventoryPriority": "被选中物品栏的优先级。",
    "GetEquippedItems": "返回当前已装备的物品。",
    "GetBody": "获取响应体。",
    "Get": "发送 GET 请求。",
    "HighlightEvent": "按钮高亮时触发。",
    "UnhighlightEvent": "取消高亮时触发。",
    "Instigator": "发起该技能的代理。",
    "Participants": "参与的代理列表。",
    "Targets": "技能目标列表。",
    "BeginUseEvent": "开始使用技能时触发。",
    "EndUseEvent": "停止使用技能时触发。",
    "ActiveEffects": "当前生效的效果列表。",
    "Use": "激活技能。",
    "CanUse": "判断当前能否使用（可失败）。",
    "MakeContext": "构造技能上下文。",
    "MakeAbility": "构造技能实例。",
    "AbilityComponent": "此效果所属的 ability_effect_component。",
    "Ability": "此组件处理的技能。",
    "Context": "技能上下文。",
    "CanCancel": "此效果可否被取消。",
    "Cancel": "取消此效果。",
    "EndUse": "结束使用。",
    "OnBeginUse": "开始使用时的回调。",
    "OnEndUse": "结束使用时的回调。",
    "AddInputMapping": "为该玩家添加输入映射。",
    "RemoveInputMapping": "移除该玩家的输入映射。",
    "GetInputEvents": "获取该玩家的输入事件容器。",
    "GetPassengers": "返回载具上的全部乘客。",
    "OnUpdateEvent": "目标信息更新时触发。",
}

pending = open('tools/_pending_translation.txt', encoding='utf-8').read().splitlines()
pages = {}  # path -> [(name, empty_desc)]
cur = None
for ln in pending:
    if ln.startswith('## '):
        cur = ln[3:].strip()
        pages.setdefault(cur, [])
    elif cur and '::' in ln:
        name = ln.strip().split('::')[0].strip()
        pages[cur].append(name)

patched_pages = filled = unmapped = 0
unmapped_names = set()
for path, names in pages.items():
    s = open(path, encoding='utf-8').read()
    changed = False
    for name in names:
        zh = ZH.get(name)
        if not zh:
            unmapped += 1
            unmapped_names.add(name)
            continue
        # 只填空描述格：| Name |  |  或 | Name | |（官方本就为空）
        pat = re.compile(r'(\| ' + re.escape(name) + r' \|[^|]*\|)\s*(\|)', re.M)
        new_s, n = pat.subn(lambda m: m.group(1) + ' ' + zh + ' ' + m.group(2), s)
        if n:
            s = new_s
            filled += n
            changed = True
    if changed:
        open(path, 'w', encoding='utf-8').write(s)
        patched_pages += 1

print(f'填充 {filled} 格 / {patched_pages} 页；未映射 {unmapped}')
if unmapped_names:
    print('未映射名:', sorted(unmapped_names))
