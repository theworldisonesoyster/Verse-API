---
name: AddComponents function
slug: unrealenginedotcom/abilities/ability_effect/addcomponents
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/abilities/ability_effect
kind: function
module: /Verse.org/abilities
grade: B
depth: oneliner
status: done
order: 1
parent: unrealenginedotcom/abilities/ability_effect
---

#
# AddComponents function <B>

把给定的组件添加到实体。若某组件不允许加到该实体则跳过。注意：在 AddedToScene 或 BeginSimulation 阶段调用时，会确保被加组件已达到对应阶段。添加规则：所有组件加入实体子列表；实体在场景中时各组件的 OnAddedToScene 被调用；实体正在模拟时各组件的 OnBeginSimulation 被调用。
