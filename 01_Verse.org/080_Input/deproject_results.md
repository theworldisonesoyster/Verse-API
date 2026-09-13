---
name: deproject_results
slug: versedotorg/input/deproject_results
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/deproject_results
kind: class
module: /Verse.org/input
grade: B
depth: brief
status: done
---

# deproject_results struct <B>

> Holds the world-space ray produced by deprojecting a viewport coordinate.
> 保存视口坐标反投影得到的世界空间射线。

`using { /Verse.org/Input }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| Origin | vector3 | 相机的世界空间位置（射线起点）。这是相机眼睛点而非近裁剪面——从这里开始的检测可能撞上相机与近裁剪面之间屏幕上不可见的几何体。建议用碰撞过滤忽略玩家角色，或把起点沿 Direction 前移越过近裁剪距离。 |
| Direction | vector3 | 射线的归一化世界空间方向：从相机穿过给定视口坐标指向场景。 |
