---
name: GetSimulationElapsedTime
slug: versedotorg/simulation/getsimulationelapsedtime
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/simulation/getsimulationelapsedtime
kind: function
module: /Verse.org/Simulation
grade: A
depth: full
status: done
---

# GetSimulationElapsedTime function 🟩【A级·常用】

> Get the seconds that have elapsed since the world began simulating
> 获取世界开始模拟以来经过的秒数。

`using { /Verse.org/Simulation }`

```verse
GetSimulationElapsedTime<public><native>()<transacts>:float
```

## Parameters

GetSimulationElapsedTime does not take any parameters.（GetSimulationElapsedTime 不接受任何参数。）

## Attributes, Specifiers, and Effects

`GetSimulationElapsedTime<public><native>()<transacts>:float` —— 标签：public / native / transacts，语义见 [Specifiers 与 Effects 对照](../../_Specifiers与Effects.md)。

## 示例

```verse
using { /Verse.org/Simulation }

# 时钟驱动的节拍调度：每 0.5 秒一拍，不受循环体耗时影响
var NextBeat:float = 0.0
BeatLoop()<suspends>:void =
    loop:
        Now := GetSimulationElapsedTime()
        if (Now >= NextBeat):
            PlayBeat()
            set NextBeat += 0.5
        Sleep(0.0)
```

## 补充说明

- 这是"世界模拟时间"（单调增长的秒数），不是现实墙钟；UTC 时间戳请用 [GetSecondsSinceEpoch function](../010_Verse/getsecondssinceepoch.md)。
- 做"到点做事"的调度器时，比较世界时间比 `Sleep(固定值)` 更抗抖动（循环体耗时不影响节拍间隔）。
- 相关页面：[Sleep function](sleep.md)。
