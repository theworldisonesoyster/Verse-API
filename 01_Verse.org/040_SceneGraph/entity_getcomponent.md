---
name: GetComponent function
slug: versedotorg/scenegraph/entity/getcomponent
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/entity
kind: function
module: /Verse.org/scenegraph
grade: S
depth: oneliner
status: done
order: 5
parent: versedotorg/scenegraph/entity
---

#
# GetComponent function <S>

若 component_type 类型的子组件存在且可从调用方上下文访问，则成功并返回该组件。注意：在 AddedToScene 或 BeginSimulation 阶段调用时，会确保返回的组件已达到对应阶段。若不存在或不可访问则失败。
