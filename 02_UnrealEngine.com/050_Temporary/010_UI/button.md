---
name: button
slug: unrealenginedotcom/temporary/ui/button
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/button
kind: class
module: /UnrealEngine.com/temporary/ui
grade: A
depth: full
status: done
---

# button class <A>

> Button is a container of a single child widget slot and fires the OnClick event when the button is clicked.
> 按钮容器：包含单个子控件槽，点击时触发 OnClick 事件。

`using { /UnrealEngine.com/Temporary/UI }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| widget | 绘制在玩家屏幕上的一切 UI 元素的基类。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| Slot | button_slot | 按钮的子控件；仅在控件初始化时使用，SetSlot 不会修改它。 |
| TriggeringInputAction | ??input_action(t) | 将触发此按钮 Click 事件的 UI 输入动作。 |

### Functions
| Function Name | Description |
| GetParentWidget | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。 |
| GetRootWidget | 返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |
| GetVisibility | 返回当前 widget_visibility 状态。 |
| HighlightEvent |  |
| IsEnabled | 若此 widget 可被玩家交互修改则返回 true。 |
| OnClick | 按钮被点击时触发的可订阅事件。 |
| SetEnabled | 启用或禁用玩家与此 widget 的交互。 |
| SetVisibility | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
| SetWidget | 设置子控件槽位。 |
| UnhighlightEvent |  |
