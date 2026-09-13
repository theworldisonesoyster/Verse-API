---
name: MakeCanvasSlot
slug: unrealenginedotcom/temporary/ui/makecanvasslot
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/makecanvasslot
kind: function
module: /Verse.org/temporary/ui
grade: A
depth: full
status: done
---

# MakeCanvasSlot function <A>

> Make a canvas slot for fixed position widget. If Size is set, then the Offsets is calculated and the SizeToContent is set to false. If Size is not set, then Right and Bottom are set to zero and are not used. The widget size will be automatically calculated. The SizeToContent is set to true. The widget is not anchored and will not move if the parent is resized. The Anchors is set to zero.
> 为固定位置控件构造画布槽位。若设置 Size 则据此计算 Offsets 且 SizeToContent=false；未设 Size 则 Right/Bottom 置零不使用、控件尺寸自动计算且 SizeToContent=true。控件不设锚点，父级缩放时不移动（Anchors 置零）。

`using { /UnrealEngine.com/Temporary/UI }`

```verse
MakeCanvasSlot<public><native>(Widget:widget, Position:vector2, Size:vector2, ZOrder:int, Alignment:vector2):canvas_slot
```

## Parameters

MakeCanvasSlot 接受以下参数：
| Name | Type | Description |
| Widget | widget |  |
| Position | vector2 |  |
| Size | vector2 |  |
| ZOrder | int |  |
| Alignment | vector2 |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
