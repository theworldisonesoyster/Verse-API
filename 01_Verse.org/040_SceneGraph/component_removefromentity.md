---
name: RemoveFromEntity function
slug: versedotorg/scenegraph/component/removefromentity
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/component
kind: function
module: /Verse.org/scenegraph
grade: S
depth: oneliner
status: done
order: 8
parent: versedotorg/scenegraph/component
---

#
# RemoveFromEntity function <S>

把组件从实体上移除。被移除的组件会离开场景，且之后只能加回**同一个**实体。流程经过 OnEndSimulation → OnRemovingFromScene。
