---
name: RemoveFromParent function
slug: versedotorg/scenegraph/entity/removefromparent
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/entity
kind: function
module: /Verse.org/scenegraph
grade: S
depth: oneliner
status: done
order: 2
parent: versedotorg/scenegraph/entity
---

#
# RemoveFromParent function <S>

把此实体从父实体移除，用于将实体移出场景。该实体及其子级上的组件会依次走 OnEndSimulation → OnRemovingFromScene。之后可用 NewParent.AddEntities 再加回。
