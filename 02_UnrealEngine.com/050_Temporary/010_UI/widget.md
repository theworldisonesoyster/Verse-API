---
name: widget
slug: unrealenginedotcom/temporary/ui/widget
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget
kind: class
module: /UnrealEngine.com/Temporary/UI
grade: S
depth: full
status: done
---

# widget class <S>

（本页官网无导语描述；widget 是一切 UI 控件的基类——canvas、按钮、文本等都派生自它。）

`using { /UnrealEngine.com/Temporary/UI }`

## Members

This class has functions, but no data members.（此类只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| SetVisibility | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
| GetVisibility | 返回当前 widget_visibility 状态。 |
| SetEnabled | 启用或禁用玩家与此 widget 的交互。 |
| IsEnabled | 若此 widget 可被玩家交互修改则返回 true。 |
| GetParentWidget | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget（无父）则失败。 |
| GetRootWidget | 返回当初把该 widget 加进 player_ui 的根 widget。根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |

## Attributes, Specifiers, and Effects

（类成员函数各自的签名与效果见官网对应成员页；本页无统一标注。）

## 示例

```verse
using { /UnrealEngine.com/Temporary/UI }

TogglePanel(Panel:widget, Show:logic):void =
    Panel.SetEnabled(Show)
    Panel.SetVisibility(if (Show?) then widget_visibility.Visible else widget_visibility.Hidden)
```

## 补充说明

- `Hidden` 只是看不见，控件仍挂在 player_ui 上；真正移除要用 player_ui 的 RemoveWidget。
- 具体控件子类：布局（[canvas class](canvas.md) / [stack_box class](stack_box.md) / [overlay class](overlay.md)）、内容（text_block、color_block…）、交互（button 族、[slider_regular class](../../../03_Fortnite.com/010_UI/slider_regular.md)）。
