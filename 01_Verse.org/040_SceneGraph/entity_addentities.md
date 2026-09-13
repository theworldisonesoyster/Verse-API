---
name: AddEntities function
slug: versedotorg/scenegraph/entity/addentities
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/entity
kind: function
module: /Verse.org/scenegraph
grade: S
depth: oneliner
status: done
order: 3
parent: versedotorg/scenegraph/entity
---

#
# AddEntities function <S>

把给定的实体添加为子实体。若子实体已有父实体，会先从原父实体移除再加入新父。加入的子实体会沿各自的生命周期方法推进，直到与新父实体的状态一致。
