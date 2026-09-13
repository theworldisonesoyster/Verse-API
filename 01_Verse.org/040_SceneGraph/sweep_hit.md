---
name: sweep_hit
slug: versedotorg/scenegraph/sweep_hit
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/scenegraph/sweep_hit
kind: class
module: /Verse.org/scenegraph
grade: B
depth: brief
status: done
---

# sweep_hit struct <B>

> The results of a sweep query. See entity.FindSweepHits(). We will get one sweep_hit for each intersection of any volume in SourceVolumes with any other volume.
> Sweep 查询的结果：每个相交产生一个 sweep_hit。见 entity.FindSweepHits()。

`using { /Verse.org/SceneGraph }`

## Members

只有数据成员，没有函数。

### Data
| Data Member Name | Type | Description |
| [SourceComponent](sweep_hit_sourcecomponent.md) | ?component | 来源组件与体积（查询输入）。对复合输入（如实体层级），这是层级中参与查询的组件/体积；SourceGlobalTransform 是扫掠开始时 SourceVolume 的变换。对球体等单体积输入，体积与变换即查询输入本身，component 为 false。 |
| [SourceVolume](sweep_hit_sourcevolume.md) | collision_volume | 来源体积（查询输入）。 |
| [SourceStartGlobalTransform](sweep_hit_sourcestartglobaltransform.md) | transform | 扫掠开始时来源体积的变换。 |
| [SourceHitTranslation](sweep_hit_sourcehittranslation.md) | vector3 | SourceVolume 触到 TargetVolume 时的世界位移（相对 SourceStartGlobalTransform）。 |
| [SourceHitDistance](sweep_hit_sourcehitdistance.md) | float | 扫掠路径上 SourceVolume 触到 TargetVolume 处的距离。 |
| [TargetComponent](sweep_hit_targetcomponent.md) | component | 被 SourceVolume 命中的组件。 |
| [TargetVolume](sweep_hit_targetvolume.md) | collision_element | 被 SourceVolume 命中的体积。 |
| [ContactPosition](sweep_hit_contactposition.md) | vector3 | SourceVolume 与 TargetVolume 的接触点。 |
| [ContactNormal](sweep_hit_contactnormal.md) | vector3 | HitPosition 处 TargetVolume 的法线。 |
| [ContactFaceNormal](sweep_hit_contactfacenormal.md) | vector3 | 若 TargetVolume 是多边形物体（网格、凸包等）且接触点位于边或顶点上，此值为共享该边/顶点的面中最相对的面法线；否则与 HitNormal 相同。 |
