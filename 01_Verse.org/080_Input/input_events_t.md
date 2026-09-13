---
name: input_events(t)
slug: versedotorg/input/input_events/input_events(t)
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/input_events/input_events(t)
kind: class
module: /Verse.org/input/input_events
grade: A
depth: full
status: done
---

# input_events(t) class <A>

> Input_events is a container for user input events which can be subscribed to.
> - Use the 'GetPlayerInput' and 'GetInputEvents' functions to retrieve an input_events object for a given player.
> - Low-level notifications of current user input: BeginDetectEvent, DetectionOngoingEvent, and EndDetectEvent.
> - High-level notifications of triggered events: TriggerActivationEvent and CancelActivationEvent. /—----------<-------\ BeginDetectEvent -> DetectionOngoingEvent -> TriggerActivationEvent -> EndDetectEvent /\ /\ / ---------------------> CancelActivationEvent ----------------------/
> 用户输入事件的容器，可订阅其中的事件；通过 GetPlayerInput / GetInput 获取。

`using { /Verse.org/Input }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| [TriggerActivationEvent](input_events_t_triggeractivationevent.md) | unknown | 此输入已满足全部触发条件并成功触发。多数情况下应绑定此事件。元组载荷：0——产生事件的玩家；1——物理输入产生的值。 |
| [CancelActivationEvent](input_events_t_cancelactivationevent.md) | unknown | 此输入在激活前被取消——例如在「按住」时长阈值到达前松开按键。元组载荷：0——玩家；1——物理输入产生的值；2——检测开始后经过的秒数。 |
| [BeginDetectEvent](input_events_t_begindetectevent.md) | unknown | 此输入的检测已开始，例如所需按键正被按住。注意：TriggerActivationEvent 也可能在本帧发生，但本事件总是先触发。无论输入最终成功或取消，BeginDetectEvent 与 EndDetectEvent 都会成对触发。元组载荷：0——玩家；1——物理输入产生的值。 |
| [DetectionOngoingEvent](input_events_t_detectionongoingevent.md) | unknown | 此输入的检测仍在进行中——例如时长阈值尚未满足。元组载荷：0——玩家；1——物理输入产生的值；2——检测开始后经过的秒数。 |
| [EndDetectEvent](input_events_t_enddetectevent.md) | unknown | 检测已结束，例如所需按键均已松开。总是与 BeginDetectEvent 成对触发。元组载荷：0——玩家；1——检测开始后经过的秒数。 |

## 示例

```verse
IE := GetPlayerInput[P].GetInputEvents[int]()
IE.PressedEvent.Subscribe(OnKeyPressed)
```
