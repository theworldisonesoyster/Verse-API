---
name: timeline_element
slug: versedotorg/timeline/timeline_element
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/timeline/timeline_element
kind: class
module: /Verse.org/timeline
grade: B
depth: brief
status: done
---

# timeline_element class <B>

> Abstract definition of any element that can be added to a timeline.See timeline_element_point and timeline_element_span.
> 可加入时间线的元素的抽象定义，见 timeline_element_point 与 timeline_element_span。

`using { /Verse.org/Timeline }`

## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| cancelable | 由「允许用户取消操作」的类实现：调用 subscribable.Subscribe 传回调会返回一个 cancelable 对象，对其调用 Cancel 即可取消订阅。 |


## Members

没有成员。
