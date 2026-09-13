---
name: GetPlayerUI
slug: unrealenginedotcom/temporary/ui/getplayerui
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/getplayerui
kind: function
module: /UnrealEngine.com/Temporary/UI
grade: S
depth: full
status: done
---

# GetPlayerUI function <S>

（本页官网无导语描述；返回指定玩家的 [player_ui class](player_ui.md) 实例——所有 UI 操作的第一步。）

`using { /UnrealEngine.com/Temporary/UI }`

```verse
GetPlayerUI<public><native>(Player:player)<transacts><decides>:player_ui
```

## Parameters

GetPlayerUI takes the following parameters:（GetPlayerUI 接受以下参数：）

| Name | Type | Description |
|---|---|---|
| Player | player | 目标玩家。 |

## Attributes, Specifiers, and Effects

`GetPlayerUI<public><native>(Player:player)<transacts><decides>:player_ui` —— 标签：public / native / transacts / decides，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /UnrealEngine.com/Temporary/UI }
using { /Verse.org/Simulation }

Show(P:player, W:widget):void =
    if (UI := GetPlayerUI[P]):   # <decides>：玩家 UI 未就绪则失败
        UI.AddWidget(W)
```

## 补充说明

- `<decides>` 表示可失败：必须写在失败上下文，用 `GetPlayerUI[P]` 形式调用。
- 参数必须是 player（不是 agent）；从 agent 先做 `player[A]` 转换。
