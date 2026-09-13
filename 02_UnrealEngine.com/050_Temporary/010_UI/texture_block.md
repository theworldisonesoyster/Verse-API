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
| DefaultDesiredSize | vector2 | 控件期望的显示尺寸；仅在初始化时使用，SetDesiredSize 不会修改它。 |
| DefaultHorizontalTiling | image_tiling | 水平平铺选项；仅在初始化时使用，SetTiling 不会修改它。 |
| DefaultImage | texture | 要渲染的图像；仅在初始化时使用，SetImage 不会修改它。 |
| DefaultTint | color | 应用于图像的着色；仅在初始化时使用，SetTint 不会修改它。 |
| DefaultVerticalTiling | image_tiling | 垂直平铺选项；仅在初始化时使用，SetTiling 不会修改它。 |

### Functions
| Function Name | Description |
| GetDesiredSize | 获取控件期望的显示尺寸。 |
| GetImage | 获取要渲染的图像。 |
| GetParentWidget | 返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。 |
| GetRootWidget | 返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。 |
| GetTiling | 获取平铺选项。 |
| GetTint | 获取图像的着色。 |
| GetVisibility | 返回当前 widget_visibility 状态。 |
| IsEnabled | 若此 widget 可被玩家交互修改则返回 true。 |
| SetDesiredSize | 设置控件期望的显示尺寸。 |
| SetEnabled | 启用或禁用玩家与此 widget 的交互。 |
| SetImage | 设置要渲染的图像。 |
| SetTiling | 设置图像小于分配空间时的平铺选项。 |
| SetTint | 设置图像的着色。 |
| SetVisibility | 显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。 |
