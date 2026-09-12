log class to send messages to the default log
|  |  |
| Verse using statement | using { /UnrealEngine.com/Temporary/Diagnostics } |

## Members
This class has both data members and functions.

### Data
| Data Member Name | Type | Description |
| Channel | log_channel | Channel class name will be added as a prefix used when printing the message e.g. '[log_channel]: #Message |
| DefaultLevel | log_level | Sets the default log level of the displayed message. See log_level enum for more info on log levels. Defaults to log_level.Normal. |

### Functions
| Function Name | Description |
| Print | Print Message using the given log level. |
| Print | Print Message diagnostic using the given log level. |
| PrintCallStack | Prints the current script call stack using the given log level. |
