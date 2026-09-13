---
name: Concurrency module
slug: versedotorg/concurrency
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/concurrency
kind: module
module: /versedotorg
grade: A
depth: brief
status: done
---

# Concurrency module <A>

异步并发支持：task 表示已启动的异步任务，awaitable 定义「可等待」能力。

## Functions

| Name | Description |
|---|---|
| [task](task.md) | 参数化构造：按返回值类型 t 创建 task 类型。 |
| [awaitable](awaitable.md) | 带载荷、可被等待（Await）的事件实现的参数化接口；与 signalable 配对。 |
| [awaitable](awaitable-1.md) | awaitable 的无参数构造重载。 |
