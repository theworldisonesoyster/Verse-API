---
name: input_events(t)
slug: unrealenginedotcom/controlinput/input_events/input_events(t)
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/controlinput/input_events/input_events(t)
kind: class
module: /UnrealEngine.com/controlinput/input_events
grade: B
depth: brief
status: done
---

# input_events(t) class <B>

> Input_events is a container for user input events which can be subscribed to.
> - Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player.
> - Low-level notifications of current user input: DetectionBeginEvent, DetectionOngoingEvent, and DetectionEndEvent.
> - High-level notifications of triggered events: ActivationTriggeredEvent and ActivationCanceledEvent. /—----------<-------\ DetectionBeginEvent -> DetectionOngoingEvent -> ActivationTriggeredEvent -> DetectionEndEvent /\ /\ / ---------------------> ActivationCanceledEvent ----------------------/
> 用户输入事件的容器，可订阅。用 GetPlayerInput / GetInputEvents 获取某玩家的 input_events；低层通知：DetectionBeginEvent/DetectionOngoingEvent/DetectionEndEvent；高层通知：ActivationTriggeredEvent/ActivationCanceledEvent。

`using { /UnrealEngine.com/ControlInput }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| ActivationTriggeredEvent | listenable(payload) | 此输入已满足全部触发条件并成功触发。多数情况下应绑定此事件。元组载荷：0——产生事件的玩家；1——物理输入产生的值。 |
| ActivationCanceledEvent | listenable(payload) | 此输入在激活前被取消——例如在「按住」时长阈值到达前松开按键。元组载荷：0——玩家；1——物理输入产生的值；2——检测开始后经过的秒数。 |
| DetectionBeginEvent | listenable(payload) | 此输入的检测已开始，例如所需按键正被按住。注意：ActivationTriggeredEvent 也可能在本帧发生，但本事件总是先触发。无论输入成功或取消，DetectionBegin 与 DetectionEnd 都会触发。元组载荷：0——玩家；1——物理输入产生的值。 |
| DetectionOngoingEvent | listenable(payload) | 此输入的检测仍在进行中——例如时长阈值尚未满足。元组载荷：0——玩家；1——物理输入产生的值；2——检测开始后经过的秒数。 |
| DetectionEndEvent | listenable(payload) | 检测已结束，例如所需按键均已松开。总是与 DetectionBegin 成对触发。元组载荷：0——玩家；1——检测开始后经过的秒数。 |
