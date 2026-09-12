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

# widget 🟦【S级·核心】

> Base class for all UI widgets.
> 一切 UI 控件的基类——canvas、按钮、文本……都继承它。

## 这是什么

`widget` 定义了所有控件的公共能力，核心是"可见性"与"可交互性"：

- `SetVisibility` / `GetVisibility`：显示/隐藏（枚举 [widget_visibility](widget_visibility.md)），**隐藏不等于移除**——控件仍挂在 player_ui 上。
- `SetEnabled` / `IsEnabled`：允许/禁止玩家交互（按钮变灰）。
- `GetParentWidget` / `GetRootWidget`：查询控件树位置（不在树上则失败）。

具体长相由子类决定：布局容器（[canvas](canvas.md)、[stack_box](stack_box.md)、[overlay](overlay.md)）、内容（text_block、color_block…）、交互（[button](button.md) 族、[slider_regular](../../../../03_Fortnite.com/010_UI/slider_regular.md)）。

## 签名

```verse
widget<public><native> := class<native>:
    SetVisibility<public>(Visibility:widget_visibility)<transacts>:void
    GetVisibility<public>()<transacts>:widget_visibility
    SetEnabled<public>(InEnabled:logic)<transacts>:void
    IsEnabled<public>()<transacts>:logic
    GetParentWidget<public>()<transacts><decides>:widget
    GetRootWidget<public>()<transacts><decides>:widget
```

## 最小示例

```verse
using { /UnrealEngine.com/Temporary/UI }

TogglePanel(Panel:widget, Show:logic):void =
    Panel.SetEnabled(Show)
    Panel.SetVisibility(if (Show?) then widget_visibility.Visible else widget_visibility.Hidden)
```

## 常用成员

| 成员 | 说明 | 级别 |
|---|---|---|
| `SetVisibility` / `GetVisibility` | 显隐控制（Hidden≠移除） | 🟦 S |
| `SetEnabled` / `IsEnabled` | 交互开关 | 🟩 A |
| `GetRootWidget[]` | 取根控件（可失败） | 🟨 B |

## 何时用 / 何时不用

- 用：作为成员类型统一持有控件；写"接收任意控件"的工具函数。
- 不用：直接实例化基类没意义——用具体子类。

## 常见坑

- `Hidden` 只是看不见，仍占 slot；真正拿掉要 `RemoveWidget`。
- 子类构造参数（如文本内容）在构造处设置，widget 基类只管公共行为。

## 相关页面

- [player_ui](player_ui.md) / [GetPlayerUI](getplayerui.md)
- [canvas](canvas.md) / [stack_box](stack_box.md) / [overlay](overlay.md)
