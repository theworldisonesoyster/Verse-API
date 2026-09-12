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

# session_environment 🟨【B级·进阶】

> Specifies what type of environment the current session is in.
> 指明当前对局处于什么环境（编辑 / 私人 / 线上）。

## 这是什么

配合 [session](session.md) 判断"现在这段代码跑在哪"：编辑器里试玩、私人测试局、正式上线局，可以走不同逻辑（比如只在正式局里上报数据）。

## 签名

```verse
session_environment<public><native> := enum:
    Edit     # 编辑环境（如 UEFN 内启动的会话）
    Private  # 私人环境（如试玩测试局）
    Live     # 线上正式环境
```

## 最小示例

```verse
if (SessionInfo := GetSession().GetSessionEnvironment?):
    Print("当前环境: {SessionInfo}")
```

## 相关页面

- [session](session.md)
