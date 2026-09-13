---
name: enableable
slug: versedotorg/verse/enableable
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/enableable
kind: interface
module: /Verse.org/Verse
grade: B
depth: brief
status: done
---

# enableable interface <B>

> Implemented by classes whose instances can be enabled and disabled.
> 由「实例可被启用/禁用」的类实现。

`using { /Verse.org/Verse }`

## Members

This interface has functions, but no data members.（此接口只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| [Enable](enableable_enable.md) | 启用此对象。 |
| [Disable](enableable_disable.md) | 禁用此对象。 |
| [IsEnabled](enableable_isenabled.md) | 对象处于启用状态则成功，禁用则失败。 |

## 补充说明

- IsEnabled 是可失败断言（`<decides>`），要写在失败上下文里。
