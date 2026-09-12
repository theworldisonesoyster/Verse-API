Waits specified number of seconds and then resumes. If Seconds = 0.0 then it waits until next tick/frame/update. If Seconds = Inf then it waits forever and only calls back if canceled - such as via race. If Seconds < 0.0 then it completes immediately and does not yield to other aysnc expressions. Waiting until the next update (0.0) is especially useful in a loop of a coroutine that needs to do some work every update and this yields to other coroutines so that it doesn't hog a processor's resources. Waiting forever (Inf) will have any expression that follows never be evaluated. Occasionally it is desireable to have a task never complete such as the last expression in a race subtask where the task must never win the race though it still may be canceled earlier. Immediately completing (less than 0) is useful when you want programmatic control over whether an expression yields or not.
|  |  |
| Verse using statement | using { /Verse.org/Simulation } |
Sleep<public><native>(Seconds:float)<transacts><suspends><no_rollback>:void

## Parameters
Sleep takes the following parameters:
| Name | Type | Description |
| Seconds | float |  |

_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_
