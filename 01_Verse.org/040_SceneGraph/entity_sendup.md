---
name: SendUp function
slug: versedotorg/scenegraph/entity/sendup
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/entity
kind: function
module: /Verse.org/scenegraph
grade: S
depth: oneliner
status: done
order: 8
parent: versedotorg/scenegraph/entity
---

#
# SendUp function <S>

向此实体发送场景事件并沿层级向上传播：先在本实体的每个组件上调用 SendDown/OnReceive，再对父实体调用 SendUp。任一环节消费该事件即停止传播。有参与者消费则返回 true。
