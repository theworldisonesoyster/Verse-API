---
name: button_loud
slug: fortnitedotcom/ui/button_loud
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ui/button_loud
kind: class
module: /Fortnite.com/ui
grade: A
depth: full
status: done
---

# button_loud class <A>

> Text button with big and loud styling applied.
> 大号醒目（loud）样式的文本按钮。

`using { /Fortnite.com/UI }`

## Inheritance Hierarchy

此类派生自以下层级，起点为 ：
| Name | Description |
| widget | 绘制在玩家屏幕上的一切 UI 元素的基类。 |
| text_button_base | 带文本消息的按钮通用基类：显示一个带自定义消息文本的按钮。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [DefaultText](button_loud_defaulttext.md) | message | 展示给用户的文本；仅在初始化时使用，SetText 不会修改它。 |
| [TriggeringInputAction](button_loud_triggeringinputaction.md) | ??input_action(t) | 将触发此按钮 Click 事件的 UI 输入动作。 |

### Functions
| Function Name | Description |
| [GetParentWidget](button_loud_getparentwidget.md) | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。 |
| [GetRootWidget](button_loud_getrootwidget.md) | 返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |
| [GetText](button_loud_gettext.md) | 获取控件中的当前文本。 |
| [GetVisibility](button_loud_getvisibility.md) | 返回当前 widget_visibility 状态。 |
| [IsEnabled](button_loud_isenabled.md) | 若此 widget 可被玩家交互修改则返回 true。 |
| [OnClick](button_loud_onclick.md) | 按钮被点击时触发的可订阅事件。 |
| [SetEnabled](button_loud_setenabled.md) | 启用或禁用玩家与此 widget 的交互。 |
| [SetText](button_loud_settext.md) | 设置控件中显示的文本。 |
| [SetVisibility](button_loud_setvisibility.md) | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
