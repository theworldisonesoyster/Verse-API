---
name: BeginDetectEvent data
slug: versedotorg/input/input_events/input_events(t)/begindetectevent
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/input/input_events/input_events(t)
kind: data
module: /Verse.org/input/input_events
grade: A
depth: oneliner
status: done
order: 3
parent: versedotorg/input/input_events/input_events(t)
---

#
# BeginDetectEvent data <A>

此输入的检测已开始，例如所需按键正被按住。注意：TriggerActivationEvent 也可能在本帧发生，但本事件总是先触发。无论输入最终成功或取消，BeginDetectEvent 与 EndDetectEvent 都会成对触发。元组载荷：0——玩家；1——物理输入产生的值。
