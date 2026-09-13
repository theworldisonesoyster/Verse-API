---
name: log
slug: unrealenginedotcom/temporary/diagnostics/log
url: https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/diagnostics/log
kind: class
module: /UnrealEngine.com/temporary/diagnostics
grade: A
depth: full
status: done
---

# log class <A>

> log class to send messages to the default log
> 向默认日志发送消息的类。

`using { /UnrealEngine.com/Temporary/Diagnostics }`

## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [Channel](log_channel.md) | log_channel | 打印消息时会把通道类名作为前缀，例如「[log_channel]: #Message」。 |
| [DefaultLevel](log_defaultlevel.md) | log_level | 设置显示消息的默认日志级别。级别详情见 log_level 枚举；默认 log_level.Normal。 |

### Functions
| Function Name | Description |
| [Print](log_print.md) | 以给定日志级别打印 Message。 |
| [Print](log_print.md) | 以给定日志级别打印 Message 诊断。 |
| [PrintCallStack](log_printcallstack.md) | 以给定日志级别打印当前脚本调用栈。 |
