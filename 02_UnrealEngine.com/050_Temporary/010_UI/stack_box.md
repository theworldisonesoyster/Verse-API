---
name: stack_box
slug: unrealenginedotcom/temporary/ui/stack_box
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/stack_box
kind: class
module: /UnrealEngine.com/temporary/ui
grade: A
depth: full
status: done
---

# stack_box class <A>

> Stack box is a container of a list of widgets stacked either vertically or horizontally.
> 堆叠容器：将一组控件垂直或水平排列。

`using { /UnrealEngine.com/Temporary/UI }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| widget | 绘制在玩家屏幕上的一切 UI 元素的基类。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| Orientation | orientation | 堆叠容器的方向：水平或垂直排列控件。 |
| Slots | []stack_box_slot | 堆叠容器的子控件；仅在初始化时使用，Add/RemoveWidget 不会修改它。 |

### Functions
| Function Name | Description |
| AddWidget | 向堆叠容器添加新的子槽位；新槽位加在末尾。 |
| GetParentWidget | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。 |
| GetRootWidget | 返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |
| GetVisibility | 返回当前 widget_visibility 状态。 |
| IsEnabled | 若此 widget 可被玩家交互修改则返回 true。 |
| RemoveWidget | 移除包含给定控件的槽位 |
| SetEnabled | 启用或禁用玩家与此 widget 的交互。 |
| SetVisibility | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
