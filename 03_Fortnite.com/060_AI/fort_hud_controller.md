---
name: fort_hud_controller
slug: fortnitedotcom/ui/fort_hud_controller
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ui/fort_hud_controller
kind: interface
module: /Fortnite.com/ui
grade: B
depth: brief
status: done
---

# fort_hud_controller interface <B>

> A HUD controller that allows for showing and hiding of HUD elements.
> HUD 控制器：显示/隐藏各类 HUD 元素。

`using { /Fortnite.com/UI }`

## Members

只有函数，没有数据成员。

### Functions
| Function Name | Description |
| [ShowElements](fort_hud_controller_showelements.md) | 为所有玩家显示一组 HUD 元素。注意：可被 ForPlayer 系列函数设置的规则覆盖——玩家级规则优先于通用规则。 |
| [HideElements](fort_hud_controller_hideelements.md) | 为所有玩家隐藏一组 HUD 元素。注意：可被 ForPlayer 系列函数设置的规则覆盖——玩家级规则优先于通用规则。 |
| [ResetElementVisibility](fort_hud_controller_resetelementvisibility.md) | 为所有玩家重置一组 HUD 元素的可见性。注意：不会清除 ForPlayer 系列函数设置的玩家级规则——那只能调用 ResetElementsForPlayer 重置。 |
| [ShowElementsForPlayer](fort_hud_controller_showelementsforplayer.md) | 为单个玩家显示一组 HUD 元素。注意：对该元素会覆盖非玩家函数设置的通用规则；调用 ResetElementsForPlayer 可恢复通用行为。 |
| [HideElementsForPlayer](fort_hud_controller_hideelementsforplayer.md) | 为单个玩家隐藏一组 HUD 元素。注意：对该元素会覆盖非玩家函数设置的通用规则；调用 ResetElementsForPlayer 可恢复通用行为。 |
| [ResetElementsForPlayer](fort_hud_controller_resetelementsforplayer.md) | 为单个玩家重置一组 HUD 元素的玩家级可见性规则。注意：不会重置通过非 PerPlayer 函数设置的规则。 |
