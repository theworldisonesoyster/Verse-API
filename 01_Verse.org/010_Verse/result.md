---
name: result
slug: versedotorg/verse/result
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/result
kind: function
module: /Verse.org/verse
grade: A
depth: full
status: done
---

# result function <A>

> Implemented by classes that provide a result for an operation, which can fail or be successful
> 由「可为成功或失败的操作」的结果类实现。

`using { /Verse.org/Verse }`

```verse
result<public>(success_type:any, error_type:any):result(success_type,error_type)
```

```verse
This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
```

## Parameters

result 接受以下参数：
| Name | Type | Description |
| success_type | any |  |
| error_type | any |  |

### Generated Interface
result 返回参数化接口 result(success_type,error_type)。

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_

## 示例

```verse
R := MakeError("存档失败")
if (E := result[Error, string][R]):
    Print("失败原因: {E}")
```
