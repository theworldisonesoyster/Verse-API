---
name: OnBeginSimulation function
slug: versedotorg/scenegraph/basic_interactable_component/onbeginsimulation
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/basic_interactable_component
kind: function
module: /Verse.org/scenegraph
grade: A
depth: oneliner
status: done
order: 23
parent: versedotorg/scenegraph/basic_interactable_component
---

#
# OnBeginSimulation function <A>

当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。
