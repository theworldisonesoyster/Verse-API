---
name: Sleep
slug: versedotorg/simulation/sleep
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/sleep
kind: function
module: /Verse.org/Simulation
grade: S
depth: full
status: done
---

# Sleep function 🟦【S级·核心】

> Waits specified number of seconds and then resumes. If `Seconds = 0.0` then it waits until next tick/frame/update. If `Seconds = Inf` then it waits forever and only calls back if canceled - such as via `race`. If `Seconds < 0.0` then it completes immediately and does not yield to other async expressions.
> 暂停指定的秒数后恢复执行。`Seconds = 0.0` 时等到下一帧（tick）才继续；`Seconds = Inf` 时永远等待，只有被取消（例如通过 `race`）才会返回；`Seconds < 0.0` 时立即完成，且不让出执行权给其他异步表达式。
>
> Waiting until the next update (0.0) is especially useful in a loop of a coroutine that needs to do some work every update and this yields to other coroutines so that it doesn't hog a processor's resources. Waiting forever (Inf) will have any expression that follows never be evaluated. Occasionally it is desirable to have a task never complete such as the last expression in a `race` subtask where the task must never win the race though it still may be canceled earlier. Immediately completing (less than 0) is useful when you want programmatic control over whether an expression yields or not.
> 「等到下一帧更新（0.0）」特别适合需要每帧做一点事的协程循环——它会把执行权让给其他协程，避免独占处理器资源。「永远等待（Inf）」会让其后的表达式永远不被求值；偶尔你正需要某个任务永不完成，比如 `race` 里放在最后的陪跑分支——它绝不能赢，但仍可被提前取消。「立即完成（小于 0）」适合想自己控制表达式是否让出执行权的场合。

`using { /Verse.org/Simulation }`

```verse
Sleep<public><native>(Seconds:float)<transacts><suspends><no_rollback>:void
```

## Parameters

Sleep takes the following parameters.（Sleep 接受以下参数：）

| Name | Type | Description |
|---|---|---|
| Seconds | float | 要等待的秒数。 |

## Attributes, Specifiers, and Effects

`Sleep<public><native>(Seconds:float)<transacts><suspends><no_rollback>` —— 标签：public / native / transacts / suspends / no_rollback，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Simulation }

# 每 0.5 秒打印一次节拍，共 8 拍（节奏游戏的"节拍器"雏形）
Countdown()<suspends>:void =
    for (Beat := 0..7):
        Sleep(0.5)
        Print("♪ 第 {Beat} 拍")

# 每帧做一次事：Sleep(0.0) 让出执行权，避免死循环卡死
EveryFrame()<suspends>:void =
    loop:
        DoWork()
        Sleep(0.0)
```

## 补充说明

- 只能在 `<suspends>` 上下文中调用；普通函数里写 `Sleep` 会直接编译错误。
- `Sleep(0.0)` 与 `Sleep(0.001)` 语义不同：前者是"下一帧"，后者是真实计时等待。
- 官方说明明确了四种取值的行为（0 / Inf / 负数 / 正数），这是罕见的写得这么全的标准库函数——按表使用即可。
- 相关页面：[GetSimulationElapsedTime](getsimulationelapsedtime.md)（拿世界时间做调度）、[event(t) class](../010_Verse/event_t.md)（事件驱动的另一种等待）。
