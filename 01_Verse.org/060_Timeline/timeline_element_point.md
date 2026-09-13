---
name: timeline_element_point
slug: versedotorg/timeline/timeline_element_point
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/timeline/timeline_element_point
kind: class
module: /Verse.org
grade: B
depth: brief
status: done
---

> A timeline element that occupies a single point in time.
> 占据单个时间点的时间线元素。

`using { /Verse.org/Timeline }`

## Inheritance Hierarchy

This class is derived from `timeline_element`.（此类派生自 timeline_element——可加入时间线的元素的抽象定义，见 timeline_element_point 与 timeline_element_span。）

## Members

This class has both data members and functions.（此类兼有数据成员和函数。）

### Data

| Data Member Name | Type | Description |
|---|---|---|
| [Time](timeline_element_point_time.md) | ?float | 此时间点的时间。可为 ±Inf；NaN 永远不会被更新或查询。 |

### Functions

| Function Name | Description |
|---|---|
| [SetTime](timeline_element_point_settime.md) | 设置此时间点的时间。 |

## 补充说明

- 与 [timeline_element_span class](timeline_element_span.md)（区间元素）相对；两者都派生自 [timeline_element class](timeline_element.md)。
