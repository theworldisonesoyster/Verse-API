---
name: OnSimulate function
slug: unrealenginedotcom/abilities/ability_effect_component/onsimulate
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/abilities/ability_effect_component
kind: function
module: /Verse.org/abilities
grade: B
depth: oneliner
status: done
order: 10
parent: unrealenginedotcom/abilities/ability_effect_component
---

#
# OnSimulate function <B>

当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。
