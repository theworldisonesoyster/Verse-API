---
name: anchors
slug: unrealenginedotcom/temporary/ui/anchors
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/anchors
kind: class
module: /UnrealEngine.com/temporary/ui
grade: B
depth: brief
status: done
---

# anchors struct <B>

> The anchors of a widget determine its the position and sizing relative to its parent. anchors range from (0.0, 0.0) (left, top) to (1.0, 1.0) (right, bottom).
> widget 的锚点决定其相对父级的位置与尺寸；范围从 (0.0, 0.0)（左上）到 (1.0, 1.0)（右下）。

`using { /UnrealEngine.com/Temporary/UI }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| [Minimum](anchors_minimum.md) | vector2 | 最小锚点（left, top）；有效范围 0.0~1.0。 |
| [Maximum](anchors_maximum.md) | vector2 | 最大锚点（right, bottom）；有效范围 0.0~1.0。 |
