---
name: canvas_slot
slug: unrealenginedotcom/temporary/ui/canvas_slot
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/canvas_slot
kind: class
module: /UnrealEngine.com/temporary/ui
grade: A
depth: full
status: done
---

# canvas_slot struct <A>

> Slot for a canvas widget.
> 画布控件的槽位。

`using { /UnrealEngine.com/Temporary/UI }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| Anchors | anchors | 边距边界及控件随父级缩放的方式；取值 0.0~1.0。 |
| Offsets | margin | 定义控件大小与位置的偏移。锚点完整定义时，Offsets.Left 表示距 Anchors 最小 X 的像素距离、Offsets.Bottom 表示距 Anchors 最大 Y 的像素距离，从而控制期望的控件尺寸；锚点未完整定义时，Offsets.Left/Top 表示控件位置，Offsets.Right/Bottom 表示控件尺寸。 |
| SizeToContent | logic | 为 true 时使用控件期望尺寸，忽略由 Offsets 计算的尺寸。 |
| Alignment | vector2 | Alignment 是控件的轴心/原点：左上 (0.0,0.0) 到右下 (1.0,1.0)。 |
| ZOrder | int | 此槽位相对画布面板中其他槽位的 Z 序；值越大越后渲染（显示在最上层）。 |
| Widget | widget | 分配到此槽位的控件。 |
