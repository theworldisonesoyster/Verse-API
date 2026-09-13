---
name: text_block
slug: fortnitedotcom/ui/text_block
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ui/text_block
kind: class
module: /Fortnite.com/ui
grade: A
depth: full
status: done
---

# text_block class <A>

> Text block widget. Displays text to the user.
> 文本块控件：向用户显示文本。

`using { /Fortnite.com/UI }`

## Inheritance Hierarchy

此类派生自以下层级，起点为 ：
| Name | Description |
| widget | 绘制在玩家屏幕上的一切 UI 元素的基类。 |
| text_base | 文本控件的基类。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [AutoWrap](text_block_autowrap.md) | ?logic | 文本是否自动换行。 |
| [DefaultJustification](text_block_defaultjustification.md) | text_justification | 展示给用户的对齐方式；仅在初始化时使用，SetJustification 不会修改它。 |
| [DefaultOverflowPolicy](text_block_defaultoverflowpolicy.md) | text_overflow_policy | 文本超长处理策略；仅在初始化时使用，SetOverflowPolicy 不会修改它。 |
| [DefaultShadowColor](text_block_defaultshadowcolor.md) | color | 阴影颜色；仅在初始化时使用，SetShadowColor 不会修改它。 |
| [DefaultShadowOffset](text_block_defaultshadowoffset.md) | ?vector2 | 阴影投射方向；仅在初始化时使用，SetShadowOffset 不会修改它。 |
| [DefaultShadowOpacity](text_block_defaultshadowopacity.md) | float | 阴影不透明度；仅在初始化时使用，SetShadowOpacity 不会修改它。 |
| [DefaultText](text_block_defaulttext.md) | message | 展示给用户的文本；仅在初始化时使用，SetText 不会修改它。 |
| [DefaultTextColor](text_block_defaulttextcolor.md) | color | 显示文本的颜色；仅在初始化时使用，SetTextColor 不会修改它。 |
| [DefaultTextOpacity](text_block_defaulttextopacity.md) | float | 显示文本的不透明度；仅在初始化时使用，SetTextOpacity 不会修改它。 |
| [DefaultTextSize](text_block_defaulttextsize.md) | float | 显示文本的字号；仅在初始化时使用，SetTextSize 不会修改它。 |
| [WrappingPolicy](text_block_wrappingpolicy.md) | ?text_wrapping_policy | 决定可在何处断行的换行策略。 |
| [WrapWidth](text_block_wrapwidth.md) | ?float | 文本长度超过此宽度时是否换行；值为零或负数则不换行。 |

### Functions
| Function Name | Description |
| [GetJustification](text_block_getjustification.md) | 获取控件中的文本对齐方式。 |
| [GetOverflowPolicy](text_block_getoverflowpolicy.md) | 获取文本超长处理策略。 |
| [GetParentWidget](text_block_getparentwidget.md) | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。 |
| [GetRootWidget](text_block_getrootwidget.md) | 返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |
| [GetShadowColor](text_block_getshadowcolor.md) | 获取阴影颜色。 |
| [GetShadowOffset](text_block_getshadowoffset.md) | 获取阴影投射方向。 |
| [GetShadowOpacity](text_block_getshadowopacity.md) | 获取阴影不透明度。 |
| [GetText](text_block_gettext.md) | 获取控件中的当前文本。 |
| [GetTextColor](text_block_gettextcolor.md) | 获取显示文本的颜色。 |
| [GetTextOpacity](text_block_gettextopacity.md) | 获取显示文本的不透明度。 |
| [GetTextSize](text_block_gettextsize.md) | 获取显示文本的字号。 |
| [GetVisibility](text_block_getvisibility.md) | 返回当前 widget_visibility 状态。 |
| [IsEnabled](text_block_isenabled.md) | 若此 widget 可被玩家交互修改则返回 true。 |
| [SetEnabled](text_block_setenabled.md) | 启用或禁用玩家与此 widget 的交互。 |
| [SetJustification](text_block_setjustification.md) | 设置控件中的文本对齐方式。 |
| [SetOverflowPolicy](text_block_setoverflowpolicy.md) | 设置文本超长处理策略。 |
| [SetShadowColor](text_block_setshadowcolor.md) | 设置阴影颜色。 |
| [SetShadowOffset](text_block_setshadowoffset.md) | 设置阴影投射方向。 |
| [SetShadowOpacity](text_block_setshadowopacity.md) | 设置阴影不透明度。 |
| [SetText](text_block_settext.md) | 设置控件中显示的文本。 |
| [SetTextColor](text_block_settextcolor.md) | 设置显示文本的颜色。 |
| [SetTextOpacity](text_block_settextopacity.md) | 设置显示文本的不透明度。 |
| [SetTextSize](text_block_settextsize.md) | 设置显示文本的字号。 |
| [SetVisibility](text_block_setvisibility.md) | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
