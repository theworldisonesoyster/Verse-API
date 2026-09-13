---
name: Shuffle
slug: versedotorg/random/shuffle
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/random/shuffle
kind: function
module: /Verse.org/random
grade: A
depth: full
status: done
---

# Shuffle function <A>

> Makes an array with the same elements as Input shuffled in a random order.
> 返回一个与 Input 元素相同、但顺序已随机打乱的新数组。

`using { /Verse.org/Random }`

```verse
Shuffle<public>(Input:[]t where t:any)<transacts>:[]t
```

## Parameters

Shuffle 接受以下参数：
| Name | Type | Description |
| Input | []t |  |
| t | any |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
Deck := Shuffle(array{1, 2, 3, 4, 5})
```
