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
| DefaultMaxValue | float | 滑条的最大值；仅在初始化时使用，SetMaxValue 不会修改它。 |
| DefaultMinValue | float | 滑条的最小值；仅在初始化时使用，SetMinValue 不会修改它。 |
| DefaultStepSize | float | 使用手柄/键盘时的调节步长；仅在初始化时使用，SetStepSize 不会修改它。 |
| DefaultValue | float | 展示给用户的值；仅在初始化时使用，SetValue 不会修改它。 |

### Functions
| Function Name | Description |
| GetMaxValue | 获取滑条最大值。 |
| GetMinValue | 获取滑条最小值。 |
| GetParentWidget | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。 |
| GetRootWidget | 返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |
| GetStepSize | 获取调节步长。 |
| GetValue | 获取滑条当前值。 |
| GetVisibility | 返回当前 widget_visibility 状态。 |
| IsEnabled | 若此 widget 可被玩家交互修改则返回 true。 |
| OnValueChanged | 滑条值变化时触发的可订阅事件。 |
| SetEnabled | 启用或禁用玩家与此 widget 的交互。 |
| SetMaxValue | 设置滑条最大值；会保证最大值始终 ≥ 最小值。 |
| SetMinValue | 设置滑条最小值；会保证最大值始终 ≥ 最小值。 |
| SetStepSize | 设置使用手柄/键盘时的调节步长。 |
| SetValue | 设置滑条值；数值会被钳制在最小值与最大值之间。 |
| SetVisibility | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
