---
name: input_events
slug: unrealenginedotcom/controlinput/input_events
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/controlinput/input_events
kind: function
module: /Verse.org/controlinput
grade: B
depth: brief
status: done
---

# input_events function <B>

> Input_events is a container for user input events which can be subscribed to.
> - Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player.
> - Low-level notifications of current user input: DetectionBeginEvent, DetectionOngoingEvent, and DetectionEndEvent.
> - High-level notifications of triggered events: ActivationTriggeredEvent and ActivationCanceledEvent. /—----------<-------\ DetectionBeginEvent -> DetectionOngoingEvent -> ActivationTriggeredEvent -> DetectionEndEvent /\ /\ / ---------------------> ActivationCanceledEvent ----------------------/
> 用户输入事件容器的构造重载（同 input_events(t)）。

`using { /UnrealEngine.com/ControlInput }`

```verse
input_events<public>(t:any):input_events(t)
```

```verse
This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
```

## Parameters

input_events 接受以下参数：
| Name | Type | Description |
| t | any |  |

### Generated Class
input_events 返回参数化类 input_events(t)。

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
