---
name: session_environment
slug: versedotorg/simulation/session_environment
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/session_environment
kind: enum
module: /Verse.org/Simulation
grade: B
depth: brief
status: done
---

# session_environment enumeration 🟨【B级·进阶】

> Specifies what type of environment the current session is in.
> 指明当前对局处于什么类型的环境。

`using { /Verse.org/Simulation }`

## Enumerators

The session_environment enumeration includes the following enumerators:（session_environment 枚举包含以下枚举值：）

| Name | Description |
|---|---|
| Edit | 当前对局处于体验的 Edit（编辑）环境，例如在 UEFN 内启动的会话。 |
| Private | 当前对局处于体验的 Private（私人）环境，例如试玩测试局。 |
| Live | 当前对局处于体验的 Live（线上）环境。 |

## 补充说明

- 与 [session class](session.md) 配合判断"代码正跑在哪种环境"，可对编辑测试与正式上线走不同逻辑。
