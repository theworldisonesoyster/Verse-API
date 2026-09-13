---
name: OnSimulate function
slug: versedotorg/scenegraph/camera_component/onsimulate
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/camera_component
kind: function
module: /Verse.org/scenegraph
grade: A
depth: oneliner
status: done
order: 14
parent: versedotorg/scenegraph/camera_component
---

#
# OnSimulate function <A>

当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。
