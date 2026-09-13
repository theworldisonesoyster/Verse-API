---
name: AddComponents function
slug: versedotorg/scenegraph/entity/addcomponents
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/entity
kind: function
module: /Verse.org/scenegraph
grade: S
depth: oneliner
status: done
order: 7
parent: versedotorg/scenegraph/entity
---

#
# AddComponents function <S>

把给定的组件添加到实体。若某组件不允许加到该实体，则跳过。注意：在 AddedToScene 或 BeginSimulation 阶段调用时，会确保被加组件已达到对应阶段。组件按以下规则添加：所有组件加入实体的子列表；若该实体在场景中，所有组件的 OnAddedToScene 被调用；若该实体正在模拟，所有组件的 OnBeginSimulation 被调用。
