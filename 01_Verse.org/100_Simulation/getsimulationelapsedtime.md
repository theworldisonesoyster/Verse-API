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

# GetSimulationElapsedTime 🟩【A级·常用】

> Get the seconds that have elapsed since the world began simulating.
> 获取世界开始模拟以来经过的秒数（世界时间）。

## 签名

```verse
GetSimulationElapsedTime<public><native>():float<transacts>
```

## 这是什么

返回一个不断增长的秒数（世界时钟）。和 `Sleep(t)` 配合可以做"每次循环剩余多少秒"的节流，和上一帧时间差分可以算帧间隔——做音乐同步、按时间驱动的玩法（比如节拍调度）时它是你的基准钟。

## 最小示例

```verse
using { /Verse.org/Simulation }

# 按 0.5 秒一拍调度，不受循环体耗时影响（时钟驱动而非"睡够"驱动）
var NextBeat:float = 0.0
BeatLoop()<suspends>:void =
    loop:
        Now := GetSimulationElapsedTime()
        if (Now >= NextBeat):
            PlayBeat()
            set NextBeat += 0.5
        Sleep(0.0)   # 下一帧再来
```

## 何时用 / 何时不用

- 用：计时基准、帧间隔计算、时间驱动的调度器。
- 不用：想"等一段时间"直接用 [Sleep](sleep.md)，不要写 `loop + 比较` 模拟 Sleep。

## 常见坑

- 它是"世界模拟时间"，不是现实墙钟；对局暂停/未开始时的行为以实际表现为准，别拿它当 UTC 时间（那是 [GetSecondsSinceEpoch](../010_Verse/getsecondssinceepoch.md)）。

## 相关页面

- [Sleep](sleep.md)
- [GetSession](getsession.md)
