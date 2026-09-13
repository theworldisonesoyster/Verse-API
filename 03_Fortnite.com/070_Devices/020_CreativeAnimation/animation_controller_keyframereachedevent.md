---
name: KeyframeReachedEvent data
slug: fortnitedotcom/devices/creativeanimation/animation_controller/keyframereachedevent
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creativeanimation/animation_controller
kind: data
module: /Verse.org/devices/creativeanimation
grade: B
depth: oneliner
status: done
order: 1
parent: fortnitedotcom/devices/creativeanimation/animation_controller
---

#
# KeyframeReachedEvent data <B>

每到达一个关键帧时触发。回调参数（关键帧序号:int, 是否反向:logic)。载荷中的序号一般在 [1, NumDeltaKeyframes]；PingPong 动画中反向播放的最后一个关键帧记为 0——因为 SetAnimation 接收的是增量关键帧，而此事件通知的是「到达了某个特定关键帧」。
