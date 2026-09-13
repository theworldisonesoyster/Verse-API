---
name: OnSimulate function
slug: fortnitedotcom/ai/guard_actions_component/onsimulate
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/guard_actions_component
kind: function
module: /Verse.org/ai
grade: B
depth: oneliner
status: done
order: 20
parent: fortnitedotcom/ai/guard_actions_component
---

#
# OnSimulate function <B>

当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。
