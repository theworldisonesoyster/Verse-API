---
name: ease_in_out_cubic_bezier_easing_function
slug: versedotorg/scenegraph/keyframedmovement/ease_in_out_cubic_bezier_easing_function
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/keyframedmovement/ease_in_out_cubic_bezier_easing_function
kind: class
module: /Verse.org/scenegraph/keyframedmovement
grade: B
depth: brief
status: done
---

# ease_in_out_cubic_bezier_easing_function class <B>

> EaseInOut animations are similar to Ease but the start and end animation speed is symmetric.
> 缓入缓出：类似 Ease，但首尾速度对称。

`using { /Verse.org/SceneGraph/KeyframedMovement }`

## Inheritance Hierarchy

此类派生自以下层级，起点为 ：
| Name | Description |
| easing_function | 动画缓动函数的基类。 |
| cubic_bezier_easing_function | 三次贝塞尔缓动函数。基础缓动值参见 CubicBezierEasingFunctions。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| X0 | float | P1 控制点的 X 值；须在 0.0~1.0 之间。 |
| X0 | float | P1 控制点的 X 值；须在 0.0~1.0 之间。 |
| X1 | float | P2 控制点的 X 值；须在 0.0~1.0 之间。 |
| X1 | float | P2 控制点的 X 值；须在 0.0~1.0 之间。 |
| Y0 | float | P1 控制点的 Y 值。 |
| Y0 | float | P1 控制点的 Y 值。 |
| Y1 | float | P2 控制点的 Y 值。 |
| Y1 | float | P2 控制点的 Y 值。 |

### Functions
| Function Name | Description |
| Evaluate |  | 在指定时间 t 求缓动曲线值并返回。 | Evaluate |  |
