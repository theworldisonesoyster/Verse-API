---
name: Await function
slug: versedotorg/verse/event/event(t)/await
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
# Await function <S>

挂起当前任务，直到另一个任务调用 Signal。若在 Signal 的调用过程中调用 Await，任务仍会挂起，并等到**下一次** Signal 调用时恢复。
