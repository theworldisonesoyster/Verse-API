Verse path: /Verse.org Module import path: /Verse.org/Simulation
- Verse.org
- Simulation Tags

## Classes and Structs
| Name | Description |
| agent |  |
| player |  |
| session | Type for which there is a single instance per round. Use GetSession to get the current round's session instance. May be used with weak_map to implement global variables. Note: may be changed in a future release to a single instance per game. Round-local behavior should not be relied upon. |
| team |  |

## Functions
| Name | Description |
| editable_slider |  |
| editable_number |  |
| editable_vector_slider |  |
| editable_vector_number |  |
| GetSession | Returns the session corresponding to the current round. The result can be used with weak_map to implement global variables. Note: may be changed in a future release to return a single instance per game. Round-local behavior should not be relied upon. |
| Sleep | Waits specified number of seconds and then resumes. If Seconds = 0.0 then it waits until next tick/frame/update. If Seconds = Inf then it waits forever and only calls back if canceled - such as via race. If Seconds < 0.0 then it completes immediately and does not yield to other aysnc expressions. Waiting until the next update (0.0) is especially useful in a loop of a coroutine that needs to do some work every update and this yields to other coroutines so that it doesn't hog a processor's resources. Waiting forever (Inf) will have any expression that follows never be evaluated. Occasionally it is desireable to have a task never complete such as the last expression in a race subtask where the task must never win the race though it still may be canceled earlier. Immediately completing (less than 0) is useful when you want programmatic control over whether an expression yields or not. |
| GetSimulationElapsedTime | Get the seconds that have elapsed since the world began simulating |

## Enumerations
| Name | Description |
| session_environment | Specifies what type of environment the current session is in. |
