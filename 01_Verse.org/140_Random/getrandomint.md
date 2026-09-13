---
name: GetRandomInt
slug: versedotorg/random/getrandomint
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/random/getrandomint
kind: function
module: /Verse.org/random
grade: S
depth: full
status: done
---

# GetRandomInt function <S>

> Returns a uniformly distributed, cryptographically-secure random int between Low and High, inclusive. (Low and High can be out of order.)
> 返回 Low 与 High 之间（含两端）均匀分布、密码学安全的随机 int。

`using { /Verse.org/Random }`

```verse
GetRandomInt<public><native>(Low:int, High:int)<transacts>:int
```

## Parameters

GetRandomInt 接受以下参数：
| Name | Type | Description |
| Low | int |  |
| High | int |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
N := GetRandomInt(1, 6)   # 掷骰子
```
