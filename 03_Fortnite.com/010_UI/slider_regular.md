---
name: slider_regular
slug: fortnitedotcom/ui/slider_regular
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ui/slider_regular
kind: class
module: /Fortnite.com/ui
grade: A
depth: full
status: done
---

# slider_regular class <A>

> Slider with a text value. Displays a slider, its progress bar and value.
> 带文本值的滑条：显示滑条、进度条与数值。

`using { /Fortnite.com/UI }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| widget | 绘制在玩家屏幕上的一切 UI 元素的基类。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [DefaultMaxValue](slider_regular_defaultmaxvalue.md) | float | 滑条的最大值；仅在初始化时使用，SetMaxValue 不会修改它。 |
| [DefaultMinValue](slider_regular_defaultminvalue.md) | float | 滑条的最小值；仅在初始化时使用，SetMinValue 不会修改它。 |
| [DefaultStepSize](slider_regular_defaultstepsize.md) | float | 使用手柄/键盘时的调节步长；仅在初始化时使用，SetStepSize 不会修改它。 |
| [DefaultValue](slider_regular_defaultvalue.md) | float | 展示给用户的值；仅在初始化时使用，SetValue 不会修改它。 |

### Functions
| Function Name | Description |
| [GetMaxValue](slider_regular_getmaxvalue.md) | 获取滑条最大值。 |
| [GetMinValue](slider_regular_getminvalue.md) | 获取滑条最小值。 |
| [GetParentWidget](slider_regular_getparentwidget.md) | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。 |
| [GetRootWidget](slider_regular_getrootwidget.md) | 返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |
| [GetStepSize](slider_regular_getstepsize.md) | 获取调节步长。 |
| [GetValue](slider_regular_getvalue.md) | 获取滑条当前值。 |
| [GetVisibility](slider_regular_getvisibility.md) | 返回当前 widget_visibility 状态。 |
| [IsEnabled](slider_regular_isenabled.md) | 若此 widget 可被玩家交互修改则返回 true。 |
| [OnValueChanged](slider_regular_onvaluechanged.md) | 滑条值变化时触发的可订阅事件。 |
| [SetEnabled](slider_regular_setenabled.md) | 启用或禁用玩家与此 widget 的交互。 |
| [SetMaxValue](slider_regular_setmaxvalue.md) | 设置滑条最大值；会保证最大值始终 ≥ 最小值。 |
| [SetMinValue](slider_regular_setminvalue.md) | 设置滑条最小值；会保证最大值始终 ≥ 最小值。 |
| [SetStepSize](slider_regular_setstepsize.md) | 设置使用手柄/键盘时的调节步长。 |
| [SetValue](slider_regular_setvalue.md) | 设置滑条值；数值会被钳制在最小值与最大值之间。 |
| [SetVisibility](slider_regular_setvisibility.md) | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
