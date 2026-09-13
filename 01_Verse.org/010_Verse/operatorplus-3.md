---
name: operator'+'
slug: versedotorg/verse/operatorplus-3
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/operatorplus-3
kind: function
module: /Verse.org/verse
grade: B
depth: brief
status: done
---

# operator'+' function <B>

> Returns a new set that is the union of all elements in InSetL set and InSetR.
> 集合并集：返回包含 InSetL 与 InSetR 全部元素的新集合。

`using { /Verse.org/Verse }`

```verse
operator'+'<public><native>(InSetL:classifiable_subset(element_type), InSetR:classifiable_subset(element_type) where t:any)<transacts>:classifiable_subset(element_type)
```

## Parameters

operator'+' 接受以下参数：
| Name | Type | Description |
| InSetL | classifiable_subset(element_type) |  |
| InSetR | classifiable_subset(element_type) |  |
| t | any |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
