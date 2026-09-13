---
name: GetRandomFloat
slug: versedotorg/random/getrandomfloat
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/random/getrandomfloat
kind: function
module: /Verse.org/random
grade: S
depth: full
status: done
---

# GetRandomFloat function <S>

> Returns a uniformly distributed, cryptographically-secure random float between Low and High, inclusive. (Low and High can be out of order.)
> 返回 Low 与 High 之间（含两端）均匀分布、密码学安全的随机 float。

`using { /Verse.org/Random }`

```verse
GetRandomFloat<public><native>(Low:float, High:float)<transacts>:float
```

## Parameters

GetRandomFloat 接受以下参数：
| Name | Type | Description |
| Low | float |  |
| High | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
F := GetRandomFloat(0.0, 1.0)
```
