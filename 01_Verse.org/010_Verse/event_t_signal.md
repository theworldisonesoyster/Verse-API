---
name: Signal function
slug: versedotorg/verse/event/event(t)/signal
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/event/event(t)
kind: function
module: /Verse.org/verse/event
grade: S
depth: oneliner
status: done
order: 2
parent: versedotorg/verse/event/event(t)
---

#
# Signal function <S>

并发恢复在此次 Signal 之前被 Await 挂起的任务。任务按挂起的先后顺序恢复；每个任务会尽可能执行直到遇到阻塞调用，随即把控制权交给下一个被挂起的任务。
