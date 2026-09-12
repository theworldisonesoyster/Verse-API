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

# Sleep 🟦【S级·核心】

> Waits specified number of seconds and then resumes.
> 暂停当前协程指定秒数，然后从暂停处继续执行。

## 签名

```verse
Sleep<public><native>(Seconds:float)<transacts><suspends><no_rollback>:void
```

## 这是什么

Sleep 是 Verse 里"等待"的基本手段。它只暂停**当前这条协程**，不影响其他协程和对局本身的运行。任何被标记 `<suspends>` 的函数（比如 `OnBegin<override>()<suspends>`）里都可以直接调用。倒计时、间隔刷怪、节拍等待、让子弹飞一会儿——都从它开始。

参数 `Seconds` 有三个特殊值，官方明确定义了不同行为：

| 取值 | 行为 |
|---|---|
| `Seconds > 0` | 等待指定秒数后继续 |
| `Seconds = 0.0` | 等到**下一帧**（tick）才继续，并把执行权让给其他协程 |
| `Seconds = Inf` | 永远等待，只有被 `race` 等机制取消时才会返回 |
| `Seconds < 0` | 立即完成，且**不让出**执行权给其他协程 |

## 最小示例

```verse
# 每 0.5 秒打印一次节拍，共 8 拍（节奏游戏的"节拍器"雏形）
Countdown()<suspends>:void =
    for (Beat := 0..7):
        Sleep(0.5)
        Print("♪ 第 {Beat} 拍")

# 每帧做一次事：Sleep(0.0) 让出执行权，避免死循环卡死对局
EveryFrame()<suspends>:void =
    loop:
        DoWork()
        Sleep(0.0)   # 等到下一帧再继续
```

## 何时用 / 何时不用

- 用：协程内的定时等待、节流、等待下一帧、制造"永不结束"的守卫任务（`Sleep(Inf)` 常放在 `race` 的陪跑分支里）。
- 不用：需要"到点自动回调"而不想占住一条协程时，用 [event](../010_Verse/event.md) 的 `Await()` 或 listenable 的 `Subscribe()` 更合适。

## 常见坑

- 只能在 `<suspends>` 上下文里调用；在普通函数里写 `Sleep` 会直接编译错误。
- `Sleep(0.0)` 和 `Sleep(0.001)` 不同：前者是"下一帧"，后者是真实计时等待。
- 循环里忘写 `Sleep` 会把协程跑成死循环，冻结该协程所在的执行流。

## 相关页面

- [GetSimulationElapsedTime](getsimulationelapsedtime.md) —— 拿"世界时间"做计时
- [event](../010_Verse/event.md) —— 事件驱动的另一种等待方式
- [agent](agent.md) —— 常与 Sleep 组成"对每个玩家轮流做什么"的循环
