---
name: player_ui
slug: unrealenginedotcom/temporary/ui/player_ui
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/player_ui
kind: class
module: /UnrealEngine.com/Temporary/UI
grade: S
depth: full
status: done
---

# player_ui 🟦【S级·核心】

> Per-player UI root: add/remove widgets on a specific player's screen.
> 每个玩家一块的 UI 根画布：往指定玩家的屏幕上加控件、拆控件。

## 这是什么

 Temporary/UI 的入口类。每个 [player](../../../01_Verse.org/100_Simulation/player.md) 对应一个 `player_ui` 实例，通过 [GetPlayerUI](getplayerui.md) 获取。它管理两件事：

- **挂载**：`AddWidget(控件)` 把 [widget](widget.md)（canvas/stack_box/button/text…）摆上屏，可选 [player_ui_slot](player_ui_slot.md) 配置；`RemoveWidget` 摘下。
- **焦点**：`SetFocus` 把键盘/手柄焦点交给某控件（需 focusable）。

注意模块前缀 `Temporary`：这是"过渡期 UI"，官方已在 Verse.org 侧推进 Presentation/SceneGraph 体系；但当前版本它仍是写 UI 的主力 API。

## 签名

```verse
player_ui<public><native> := class<native>:
    AddWidget<public>(Widget:widget)<transacts>:void
    AddWidget<public>(Widget:widget, Slot:player_ui_slot)<transacts>:void
    RemoveWidget<public>(Widget:widget)<transacts>:void
    SetFocus<public>(Widget:widget)<transacts>:void
```

## 最小示例

```verse
using { /UnrealEngine.com/Temporary/UI }
using { /Verse.org/Simulation }

# 玩家加入时给他屏幕上挂一个文本控件
Greet(P:player):void =
    UI := GetPlayerUI[P]           # 可失败：取玩家 UI
    NewWidget := widget{}
    UI.AddWidget(NewWidget)
```

## 常用成员

| 成员 | 说明 | 级别 |
|---|---|---|
| `AddWidget` | 上屏（默认 slot 或自定义 slot 两个重载） | 🟦 S |
| `RemoveWidget` | 下屏 | 🟦 S |
| `SetFocus` | 交焦点给控件 | 🟨 B |

## 何时用 / 何时不用

- 用：记分板、倒计时、商店面板——一切"画在玩家屏幕上"的东西。
- 不用：HUD 提示文字这类简单场景可直接用 hud_message_device；Temporary/UI 控件间搭配见 widget 族。

## 常见坑

- `GetPlayerUI` 是可失败调用（玩家可能还没就绪），务必写失败分支。
- AddWidget 前构造好的控件树要在**添加前**配置好层级；对已上屏控件的父子改动行为以实测为准。

## 相关页面

- [GetPlayerUI](getplayerui.md) —— 获取实例
- [widget](widget.md) —— 控件基类
- [canvas](canvas.md) / [stack_box](stack_box.md) —— 布局容器
