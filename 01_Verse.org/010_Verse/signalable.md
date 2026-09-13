---
name: signalable
slug: versedotorg/verse/signalable
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/signalable
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# signalable function <A>

> A parametric interface implemented by events with a payload that can be signaled. Can be used with awaitable, subscribable, or both (see: listenable).
> 带载荷、可被触发（signal）的事件实现的参数化接口。

`using { /Verse.org/Verse }`

```verse
signalable<public>(payload:any):signalable(payload)
```

```verse
This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
```

## Parameters

signalable 接受以下参数：
| Name | Type | Description |
| payload | any |  |

### Generated Interface
signalable 返回参数化接口 signalable(payload)。

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
