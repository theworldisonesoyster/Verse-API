---
name: fort_leashable
slug: fortnitedotcom/ai/fort_leashable
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ai/fort_leashable
kind: interface
module: /Fortnite.com/ai
grade: B
depth: brief
status: done
---

# fort_leashable interface <B>

可被拴留（leash，限制活动范围）的接口。

`using { /Fortnite.com/AI }`

## Members

只有函数，没有数据成员。

### Functions
| Function Name | Description |
| [SetLeashPosition](fort_leashable_setleashposition.md) | 设置自定义拴留位置。InnerRadius 范围 0.0~20000.0（厘米）；OuterRadius 范围 0.0~20000.0（厘米）且不小于 InnerRadius。 |
| [SetLeashAgent](fort_leashable_setleashagent.md) | 把该代理设为拴留的新中心。InnerRadius 范围 0.0~20000.0（厘米）；OuterRadius 范围 0.0~20000.0（厘米）且不小于 InnerRadius。 |
| [ClearLeash](fort_leashable_clearleash.md) | 解除当前拴留。 |
