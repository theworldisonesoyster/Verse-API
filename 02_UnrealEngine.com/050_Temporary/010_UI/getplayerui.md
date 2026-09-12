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

# GetPlayerUI 🟦【S级·核心】

> Returns the player_ui for the given player.
> 取指定玩家的 [player_ui](player_ui.md) 实例——所有 UI 操作的第一步。

## 签名

```verse
GetPlayerUI<public><native>(Player:player)<transacts><decides>:player_ui
```

## 这是什么

`<decides>` 说明它是**可失败**的：玩家 UI 尚未就绪时失败。所以标准写法是失败上下文＋`[]` 调用。拿到实例后 `AddWidget/RemoveWidget` 管理该玩家屏幕上的控件。

## 最小示例

```verse
using { /UnrealEngine.com/Temporary/UI }
using { /Verse.org/Simulation }

ShowScore(P:player, W:widget):void =
    if (UI := GetPlayerUI[P]):
        UI.AddWidget(W)          # 失败则静默跳过
```

## 何时用 / 何时不用

- 用：每个玩家首次交互/每局开始时获取并缓存；事件回调里按需获取。
- 不用：缓存引用后玩家退出会失效——长生命周期脚本建议每事件现取。

## 常见坑

- 无参或对 agent 调用都编译不过——参数必须先转成 player。
- 失败分支别忽略：UI 未就绪时静默失败会让"为什么没显示"很难排查，必要时在 else 里 Print 一条。

## 相关页面

- [player_ui](player_ui.md)
- [widget](widget.md)
