---
name: stack_box_slot
slug: unrealenginedotcom/temporary/ui/stack_box_slot
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/stack_box_slot
kind: class
module: /UnrealEngine.com/temporary/ui
grade: A
depth: full
status: done
---

# stack_box_slot struct <A>

> Slot for a stack_box widget
> 堆叠控件的槽位。

`using { /UnrealEngine.com/Temporary/UI }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| Widget | widget | 分配到此槽位的控件。 |
| HorizontalAlignment | horizontal_alignment | 控件在槽位内的水平对齐；只有在槽位布局空间创建后才生效，决定控件在该空间内的对齐。 |
| VerticalAlignment | vertical_alignment | 控件在槽位内的垂直对齐；只有在槽位布局空间创建后才生效，决定控件在该空间内的对齐。 |
| Padding | margin | 槽位内围绕控件的留白（像素）；按 1080p 分辨率计。 |
| Distribution | ?float | 可用空间将按比例分配；未设置时槽位使用控件期望尺寸。 |
