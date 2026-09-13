---
name: timeline_element_span
slug: versedotorg/timeline/timeline_element_span
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/timeline/timeline_element_span
kind: class
module: /Verse.org
grade: B
depth: brief
status: done
---

> A timeline element that spans a range of time.
> 跨越一段时间范围的时间线元素。

`using { /Verse.org/Timeline }`

## Inheritance Hierarchy

This class is derived from `timeline_element`.（此类派生自 timeline_element——可加入时间线的元素的抽象定义。）

## Members

This class has both data members and functions.（此类兼有数据成员和函数。）

### Data

| Data Member Name | Type | Description |
|---|---|---|
| BeginTime | ?float | 区间开始的时间。默认 0.0；须非 NaN 且 ≤ EndTime 才会被更新或查询；可为 ±Inf。 |
| EndTime | ?float | 区间结束的时间。默认 Inf；须非 NaN 且 ≥ BeginTime 才会被更新或查询；可为 ±Inf。 |

### Functions

| Function Name | Description |
|---|---|
| SetRange | 通过赋值起止时间来修改时间线的范围。 |

## 相关页面

- [timeline_element_point class](timeline_element_point.md) / [timeline_element class](timeline_element.md)
