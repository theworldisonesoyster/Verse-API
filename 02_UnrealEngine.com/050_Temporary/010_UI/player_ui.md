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

# player_ui class 🟦【S级·核心】

（本页官网无导语描述；player_ui 是每个玩家一块的 UI 根画布——往指定玩家屏幕上加/拆控件。通过 [GetPlayerUI function](getplayerui.md) 获取。）

`using { /UnrealEngine.com/Temporary/UI }`

## Members

This class has functions, but no data members.（此类只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| AddWidget | 使用默认 player_ui_slot 配置，把 Widget 添加到此 player_ui。 |
| AddWidget | 使用 Slot 配置，把 Widget 添加到此 player_ui。 |
| RemoveWidget | 把 Widget 从此 player_ui 移除。 |
| SetFocus | 把使用者的焦点设置到该 Widget。目标 Widget 必须可聚焦（focusable），否则无效果。若在 AddWidget 之前调用 SetFocus，则 AddWidget 之后该控件会获得焦点——除非在那之前又有别的 SetFocus 调用。 |

## Attributes, Specifiers, and Effects

（类成员函数各自的签名与效果见官网对应成员页；本页无统一标注。）

## 示例

```verse
using { /UnrealEngine.com/Temporary/UI }
using { /Verse.org/Simulation }

# 给玩家屏幕挂一个控件
Greet(P:player, W:widget):void =
    if (UI := GetPlayerUI[P]):
        UI.AddWidget(W)
```

## 补充说明

- `GetPlayerUI` 是可失败调用（玩家 UI 未必就绪），务必写在失败上下文里。
- 控件树与布局容器见 [widget class](widget.md)、[canvas class](canvas.md)、[stack_box class](stack_box.md)、[overlay class](overlay.md)。
