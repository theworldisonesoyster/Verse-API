---
name: Concatenate
slug: versedotorg/verse/concatenate
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/concatenate
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# Concatenate function <A>

> Makes a flattened array by concatenating the elements of Arrays.
> 把嵌套数组压平：按顺序连接 Arr 里每个子数组的元素，返回一个新数组。

`using { /Verse.org/Verse }`

```verse
Concatenate<public>(Arrays:[][]t where t:any):[]t
```

## Parameters

Concatenate 接受以下参数：
| Name | Type | Description |
| Arrays | [][]t |  |
| t | any |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
Flat:int[] = Concatenate(array{array{1,2}, array{3}})   # {1, 2, 3}
```
