---
name: text_base
slug: unrealenginedotcom/temporary/ui/text_base
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/text_base
kind: class
module: /UnrealEngine.com/temporary/ui
grade: A
depth: full
status: done
---

# text_base class <A>

> Base widget for text widget.
> 文本控件的基类。

`using { /UnrealEngine.com/Temporary/UI }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| widget | 绘制在玩家屏幕上的一切 UI 元素的基类。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| AutoWrap | ?logic | 文本是否自动换行。 |
| DefaultJustification | text_justification | 展示给用户的对齐方式；仅在初始化时使用，SetJustification 不会修改它。 |
| DefaultOverflowPolicy | text_overflow_policy | 文本超出允许长度时的处理策略；仅在初始化时使用，SetOverflowPolicy 不会修改它。 |
| DefaultText | message | 展示给用户的文本；仅在初始化时使用，SetText 不会修改它。 |
| DefaultTextColor | color | 显示文本的颜色；仅在初始化时使用，SetTextColor 不会修改它。 |
| DefaultTextOpacity | float | 显示文本的不透明度；仅在初始化时使用，SetTextOpacity 不会修改它。 |
| DefaultTextSize | float | 显示文本的字号；仅在初始化时使用，SetTextSize 不会修改它。 |
| WrappingPolicy | ?text_wrapping_policy | 决定可在何处断行的换行策略。 |
| WrapWidth | ?float | 文本长度超过此宽度时是否换行；值为零或负数则不换行。 |

### Functions
| Function Name | Description |
| GetJustification | 获取控件中的文本对齐方式。 |
| GetOverflowPolicy | 获取文本超长处理策略。 |
| GetParentWidget | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。 |
| GetRootWidget | 返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |
| GetText | 获取控件中的当前文本。 |
| GetTextColor | 获取显示文本的颜色。 |
| GetTextOpacity | 获取显示文本的不透明度。 |
| GetTextSize | 获取显示文本的字号。 |
| GetVisibility | 返回当前 widget_visibility 状态。 |
| IsEnabled | 若此 widget 可被玩家交互修改则返回 true。 |
| SetEnabled | 启用或禁用玩家与此 widget 的交互。 |
| SetJustification | 设置控件中的文本对齐方式。 |
| SetOverflowPolicy | 设置文本超长处理策略。 |
| SetText | 设置控件中显示的文本。 |
| SetTextColor | 设置显示文本的颜色。 |
| SetTextOpacity | 设置显示文本的不透明度。 |
| SetTextSize | 设置显示文本的字号。 |
| SetVisibility | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
