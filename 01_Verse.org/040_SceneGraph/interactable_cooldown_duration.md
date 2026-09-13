---
name: Duration data
slug: versedotorg/scenegraph/interactable_cooldown/duration
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/interactable_cooldown
kind: data
module: /Verse.org/scenegraph
grade: B
depth: oneliner
status: done
order: 1
parent: versedotorg/scenegraph/interactable_cooldown
---

#
# Duration data <B>

成功交互后、任何人都可再次发起交互之前所需的秒数。仅在 duration > 0.0 时生效；修改它不影响 RemainingDuration。组件开始冷却时，其上的所有其他交互都会被取消。
