---
name: OnBeginSimulation function
slug: versedotorg/scenegraph/sound_component/onbeginsimulation
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/sound_component
kind: function
module: /Verse.org/scenegraph
grade: A
depth: oneliner
status: done
order: 9
parent: versedotorg/scenegraph/sound_component
---

#
# OnBeginSimulation function <A>

当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。
