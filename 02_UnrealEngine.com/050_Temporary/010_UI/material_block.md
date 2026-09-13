---
name: material_block
slug: unrealenginedotcom/temporary/ui/material_block
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/material_block
kind: class
module: /UnrealEngine.com/temporary/ui
grade: A
depth: full
status: done
---

# material_block class <A>

> A widget to display a material.
> 显示材质的控件。

`using { /UnrealEngine.com/Temporary/UI }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| widget | 绘制在玩家屏幕上的一切 UI 元素的基类。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [DefaultDesiredSize](material_block_defaultdesiredsize.md) | vector2 | 控件期望的显示尺寸；仅在初始化时使用，SetDesiredSize 不会修改它。 |
| [DefaultImage](material_block_defaultimage.md) | material | 要渲染的图像；仅在初始化时使用，SetImage 不会修改它。 |
| [DefaultTint](material_block_defaulttint.md) | color | 应用于图像的着色；仅在初始化时使用，SetTint 不会修改它。 |

### Functions
| Function Name | Description |
| [GetDesiredSize](material_block_getdesiredsize.md) | 获取控件期望的显示尺寸。 |
| [GetImage](material_block_getimage.md) | 获取要渲染的图像。 |
| [GetParentWidget](material_block_getparentwidget.md) | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。 |
| [GetRootWidget](material_block_getrootwidget.md) | 返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |
| [GetTint](material_block_gettint.md) | 获取图像的着色。 |
| [GetVisibility](material_block_getvisibility.md) | 返回当前 widget_visibility 状态。 |
| [IsEnabled](material_block_isenabled.md) | 若此 widget 可被玩家交互修改则返回 true。 |
| [SetDesiredSize](material_block_setdesiredsize.md) | 设置控件期望的显示尺寸。 |
| [SetEnabled](material_block_setenabled.md) | 启用或禁用玩家与此 widget 的交互。 |
| [SetImage](material_block_setimage.md) | 设置要渲染的图像。 |
| [SetTint](material_block_settint.md) | 设置图像的着色。 |
| [SetVisibility](material_block_setvisibility.md) | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
