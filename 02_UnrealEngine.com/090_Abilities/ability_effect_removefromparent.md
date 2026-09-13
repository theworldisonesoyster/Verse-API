---
name: RemoveFromParent function
slug: unrealenginedotcom/abilities/ability_effect/removefromparent
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/abilities/ability_effect
kind: function
module: /Verse.org/abilities
grade: B
depth: oneliner
status: done
order: 14
parent: unrealenginedotcom/abilities/ability_effect
---

#
# RemoveFromParent function <B>

把此实体从父实体移除，用于将实体移出场景。该实体及其子级上的组件会依次走 OnEndSimulation → OnRemovingFromScene。之后可用 NewParent.AddEntities 再加回。
