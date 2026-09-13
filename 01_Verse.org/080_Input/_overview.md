---
name: Input module
slug: versedotorg/input
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input
kind: module
module: /versedotorg
grade: A
depth: brief
status: done
---

# Input module <A>

玩家输入管理：按玩家开关输入映射、订阅输入事件、查询可用输入设备与当前输入方式。子模块 Gameplay/UI 提供常见界面的预设按键映射常量。

## Classes and Structs

| Name | Description |
|---|---|
| [available_input_devices](available_input_devices.md) | 玩家当前可用输入设备的标志位；设备连接/断开时实时更新。 |
| [player_input](player_input.md) | 每个玩家一个的输入管理器：用 GetPlayerInput 获取，然后 AddInputMapping/RemoveInputMapping 开关该玩家的输入映射。 |
| [deproject_results](deproject_results.md) | 保存视口坐标反投影得到的世界空间射线。 |

## Functions

| Name | Description |
|---|---|
| [GetPlayerInput](getplayerinput.md) | 访问玩家的输入相关数据与设置。 |
| [input_events](input_events.md) | 参数化构造：按输入值类型 t 创建 input_events 容器。 |

## Enumerations

| Name | Description |
|---|---|
| [input_method](input_method.md) | 表示玩家当前偏好的输入方式（键鼠/手柄/触摸等）。 |

| Gameplay/HotbarMapping 〔无独立页面〕 〔无独立页面〕 | 快捷栏（Hotbar）的预设按键映射。 |
| UI/MenuNavigationMapping 〔无独立页面〕 〔无独立页面〕 | 菜单导航的预设按键映射。 |
| UI/NextTab 〔无独立页面〕 〔无独立页面〕 | 「下一个标签页」的预设按键映射。 |
| UI/PreviousTab 〔无独立页面〕 〔无独立页面〕 | 「上一个标签页」的预设按键映射。 |
| UI/NextPage 〔无独立页面〕 〔无独立页面〕 | 「下一页」的预设按键映射。 |
| UI/PreviousPage 〔无独立页面〕 〔无独立页面〕 | 「上一页」的预设按键映射。 |
| UI/Back 〔无独立页面〕 〔无独立页面〕 | 「返回」的预设按键映射。 |
| UI/InventoryMenuMapping 〔无独立页面〕 〔无独立页面〕 | 物品栏菜单的预设按键映射。 |
| UI/Use 〔无独立页面〕 〔无独立页面〕 | 「使用」的预设按键映射。 |
| UI/Inspect 〔无独立页面〕 〔无独立页面〕 | 「查看」的预设按键映射。 |
| UI/Sort 〔无独立页面〕 〔无独立页面〕 | 「整理」的预设按键映射。 |
| UI/Drop 〔无独立页面〕 〔无独立页面〕 | 「丢弃」的预设按键映射。 |
| UI/CraftingMenuMapping 〔无独立页面〕 〔无独立页面〕 | 制作菜单的预设按键映射。 |
| UI/Craft 〔无独立页面〕 〔无独立页面〕 | 「制作」的预设按键映射。 |
| UI/Favorite 〔无独立页面〕 〔无独立页面〕 | 「收藏」的预设按键映射。 |
| UI/Scrap 〔无独立页面〕 〔无独立页面〕 | 「拆解」的预设按键映射。 |
| UI/MapMenuMapping 〔无独立页面〕 〔无独立页面〕 | 地图菜单的预设按键映射。 |
| UI/Track 〔无独立页面〕 〔无独立页面〕 | 「追踪」的预设按键映射。 |
| UI/Reset 〔无独立页面〕 〔无独立页面〕 | 「重置」的预设按键映射。 |
| UI/PlaceMarker 〔无独立页面〕 〔无独立页面〕 | 「放置标记」的预设按键映射。 |
| UI/ToggleView 〔无独立页面〕 〔无独立页面〕 | 「切换视图」的预设按键映射。 |
| UI/ZoomIn 〔无独立页面〕 〔无独立页面〕 | 「放大」的预设按键映射。 |
| UI/ZoomOut 〔无独立页面〕 〔无独立页面〕 | 「缩小」的预设按键映射。 |
| UI/TouchMapping 〔无独立页面〕 〔无独立页面〕 | 触摸操作的预设按键映射。 |
| UI/PointerSelect 〔无独立页面〕 〔无独立页面〕 | 「指针选择」的预设按键映射。 |
| UI/PointerZoom 〔无独立页面〕 〔无独立页面〕 | 「指针缩放」的预设按键映射。 |
