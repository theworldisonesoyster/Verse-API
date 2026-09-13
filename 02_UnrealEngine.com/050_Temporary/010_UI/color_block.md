---
name: color_block
slug: unrealenginedotcom/temporary/ui/color_block
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/color_block
kind: class
module: /UnrealEngine.com/temporary/ui
grade: A
depth: full
status: done
---

# color_block class <A>

> A solid color widget.
> 纯色控件。

`using { /UnrealEngine.com/Temporary/UI }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| widget | 绘制在玩家屏幕上的一切 UI 元素的基类。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [DefaultColor](color_block_defaultcolor.md) | color | 控件颜色；仅在控件初始化时使用，SetColor 不会修改它。 |
| [DefaultDesiredSize](color_block_defaultdesiredsize.md) | vector2 | 控件期望的显示尺寸；仅在初始化时使用，SetDesiredSize 不会修改它。 |
| [DefaultOpacity](color_block_defaultopacity.md) | float | 控件不透明度；仅在初始化时使用，SetOpacity 不会修改它。 |

### Functions
| Function Name | Description |
| [GetColor](color_block_getcolor.md) | 获取控件颜色。 |
| [GetDesiredSize](color_block_getdesiredsize.md) | 获取控件期望的显示尺寸。 |
| [GetOpacity](color_block_getopacity.md) | 获取控件不透明度。 |
| [GetParentWidget](color_block_getparentwidget.md) | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。 |
| [GetRootWidget](color_block_getrootwidget.md) | 返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |
| [GetVisibility](color_block_getvisibility.md) | 返回当前 widget_visibility 状态。 |
| [IsEnabled](color_block_isenabled.md) | 若此 widget 可被玩家交互修改则返回 true。 |
| [SetColor](color_block_setcolor.md) | 设置控件颜色。 |
| [SetDesiredSize](color_block_setdesiredsize.md) | 设置控件期望的显示尺寸。 |
| [SetEnabled](color_block_setenabled.md) | 启用或禁用玩家与此 widget 的交互。 |
| [SetOpacity](color_block_setopacity.md) | 设置控件不透明度。 |
| [SetVisibility](color_block_setvisibility.md) | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
