---
name: overlap_hit
slug: versedotorg/scenegraph/overlap_hit
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/overlap_hit
kind: class
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# overlap_hit struct <B>

> The results of an overlap query. See entity.FindOverlapHits(). We will get one overlap_hit for each intersection of any volume in SourceVolumes with any other volume.
> Overlap 查询的结果：SourceVolumes 中任一体积与其他体积的每个相交各产生一个 overlap_hit。见 entity.FindOverlapHits()。

`using { /Verse.org/SceneGraph }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| [SourceComponent](overlap_hit_sourcecomponent.md) | ?component | 来源组件与体积（查询输入）。对复合输入（如实体层级），这是层级中参与查询的组件/体积；SourceTransform 是本次 Overlap 测试所用 SourceVolume 的变换。对球体等单体积输入，体积与变换即查询输入本身，component 为 false。 |
| [SourceVolume](overlap_hit_sourcevolume.md) | collision_volume | 来源体积（查询输入） |
| [SourceGlobalTransform](overlap_hit_sourceglobaltransform.md) | transform | 来源体积变换 |
| [TargetComponent](overlap_hit_targetcomponent.md) | component | 被 SourceVolume 命中的组件 |
| [TargetVolume](overlap_hit_targetvolume.md) | collision_element | 被 SourceVolume 命中的体积 |
