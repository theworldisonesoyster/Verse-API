---
name: subscribable
slug: versedotorg/verse/subscribable
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/subscribable
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# subscribable function <A>

> A parametric interface implemented by events with a payload that can be subscribed to. Matched with signalable.
> 带载荷、可被订阅（Subscribe 持续接收）的事件实现的参数化接口。

`using { /Verse.org/Verse }`

```verse
subscribable<public>(t:any):subscribable(t)
```

```verse
This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
```

## Parameters

subscribable 接受以下参数：
| Name | Type | Description |
| t | any |  |

### Generated Interface
subscribable 返回参数化接口 subscribable(t)。

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
E:event(int) = event(int){}
E.Subscribe(Handler)   # Handler 为类成员函数
```
