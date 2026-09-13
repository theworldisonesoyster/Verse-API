---
name: SendDown function
slug: unrealenginedotcom/abilities/ability_effect/senddown
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/abilities/ability_effect
kind: function
module: /Verse.org/abilities
grade: B
depth: oneliner
status: done
order: 16
parent: unrealenginedotcom/abilities/ability_effect
---

#
# SendDown function <B>

向此实体发送场景事件并沿层级向下传播：先在本实体的每个组件上调用 SendDown/OnReceive，再对每个子实体调用 SendDown。任一环节消费该事件即停止传播。有参与者消费则返回 true。
