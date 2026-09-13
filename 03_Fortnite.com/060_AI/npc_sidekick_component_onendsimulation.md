---
name: OnEndSimulation function
slug: fortnitedotcom/ai/npc_sidekick_component/onendsimulation
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/npc_sidekick_component
kind: function
module: /Verse.org/ai
grade: B
depth: oneliner
status: done
order: 19
parent: fortnitedotcom/ai/npc_sidekick_component
---

#
# OnEndSimulation function <B>

当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。
