---
name: texture_block
slug: unrealenginedotcom/temporary/ui/texture_block
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/texture_block
kind: class
module: /UnrealEngine.com/temporary/ui
grade: A
depth: full
status: done
---

# texture_block class <A>

> A widget to display a texture.
> 显示贴图的控件。

`using { /UnrealEngine.com/Temporary/UI }`

## Inheritance Hierarchy

此类派生自 。
| Name | Description |
| widget | 绘制在玩家屏幕上的一切 UI 元素的基类。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [DefaultDesiredSize](texture_block_defaultdesiredsize.md) | vector2 | 控件期望的显示尺寸；仅在初始化时使用，SetDesiredSize 不会修改它。 |
| [DefaultHorizontalTiling](texture_block_defaulthorizontaltiling.md) | image_tiling | 水平平铺选项；仅在初始化时使用，SetTiling 不会修改它。 |
| [DefaultImage](texture_block_defaultimage.md) | texture | 要渲染的图像；仅在初始化时使用，SetImage 不会修改它。 |
| [DefaultTint](texture_block_defaulttint.md) | color | 应用于图像的着色；仅在初始化时使用，SetTint 不会修改它。 |
| [DefaultVerticalTiling](texture_block_defaultverticaltiling.md) | image_tiling | 垂直平铺选项；仅在初始化时使用，SetTiling 不会修改它。 |

### Functions
| Function Name | Description |
| [GetDesiredSize](texture_block_getdesiredsize.md) | 获取控件期望的显示尺寸。 |
| [GetImage](texture_block_getimage.md) | 获取要渲染的图像。 |
| [GetParentWidget](texture_block_getparentwidget.md) | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。 |
| [GetRootWidget](texture_block_getrootwidget.md) | 返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |
| [GetTiling](texture_block_gettiling.md) | 获取平铺选项。 |
| [GetTint](texture_block_gettint.md) | 获取图像的着色。 |
| [GetVisibility](texture_block_getvisibility.md) | 返回当前 widget_visibility 状态。 |
| [IsEnabled](texture_block_isenabled.md) | 若此 widget 可被玩家交互修改则返回 true。 |
| [SetDesiredSize](texture_block_setdesiredsize.md) | 设置控件期望的显示尺寸。 |
| [SetEnabled](texture_block_setenabled.md) | 启用或禁用玩家与此 widget 的交互。 |
| [SetImage](texture_block_setimage.md) | 设置要渲染的图像。 |
| [SetTiling](texture_block_settiling.md) | 设置图像小于分配空间时的平铺选项。 |
| [SetTint](texture_block_settint.md) | 设置图像的着色。 |
| [SetVisibility](texture_block_setvisibility.md) | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
