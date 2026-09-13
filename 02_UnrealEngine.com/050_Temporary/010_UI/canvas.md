---
name: canvas
slug: unrealenginedotcom/temporary/ui/canvas
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/canvas
kind: class
module: /UnrealEngine.com/temporary/ui
grade: A
depth: full
status: done
---

# canvas class <A>

> Canvas is a container widget that allows for arbitrary positioning of widgets in the canvas' slots.
> 画布容器：允许在其槽位中任意摆放控件。

`using { /UnrealEngine.com/Temporary/UI }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| widget | 绘制在玩家屏幕上的一切 UI 元素的基类。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [Slots](canvas_slots.md) | []canvas_slot | 画布的子控件；仅在控件初始化时使用，Add/RemoveWidget 不会修改它。 |

### Functions
| Function Name | Description |
| [AddWidget](canvas_addwidget.md) | 向画布添加新的子槽位。 |
| [GetParentWidget](canvas_getparentwidget.md) | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。 |
| [GetRootWidget](canvas_getrootwidget.md) | 返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |
| [GetVisibility](canvas_getvisibility.md) | 返回当前 widget_visibility 状态。 |
| [IsEnabled](canvas_isenabled.md) | 若此 widget 可被玩家交互修改则返回 true。 |
| [RemoveWidget](canvas_removewidget.md) | 移除包含给定控件的槽位。 |
| [SetEnabled](canvas_setenabled.md) | 启用或禁用玩家与此 widget 的交互。 |
| [SetVisibility](canvas_setvisibility.md) | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
