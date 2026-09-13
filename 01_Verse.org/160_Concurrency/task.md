---
name: task
slug: versedotorg/concurrency/task
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/concurrency/task
kind: function
module: /Verse.org/concurrency
grade: A
depth: full
status: done
---

# task function <A>

参数化构造：按返回值类型 t 创建 task 类型。

`using { /Verse.org/Concurrency }`

```verse
task<public>(t:any):task(t)
```

```verse
This function is a parametric type, meaning it returns a class or interface rather than a value or object instance.
```

## Parameters

task 接受以下参数：
| Name | Type | Description |
| t | any |  |

### Generated Class
task 返回参数化类 task(t)。

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
