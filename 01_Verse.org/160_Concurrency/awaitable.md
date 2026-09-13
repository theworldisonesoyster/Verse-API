---
name: awaitable
slug: versedotorg/concurrency/awaitable
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/concurrency/awaitable
kind: function
module: /Verse.org/concurrency
grade: B
depth: brief
status: done
---

# awaitable function <B>

> A parametric interface implemented by events with a payload that can be waited on. Matched with signalable.
> 带载荷、可被等待（Await）的事件实现的参数化接口；与 signalable 配对。

`using { /Verse.org/Concurrency }`

```verse
awaitable<public>(payload:any):awaitable(payload)
```

```verse
This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
```

## Parameters

awaitable 接受以下参数：
| Name | Type | Description |
| payload | any |  |

### Generated Interface
awaitable 返回参数化接口 awaitable(payload)。

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
