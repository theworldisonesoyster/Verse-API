---
name: bank_vault_interface
slug: fortnitedotcom/devices/bank_vault_interface
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/bank_vault_interface
kind: interface
module: /Fortnite.com/devices
grade: B
depth: brief
status: done
---

# bank_vault_interface interface <B>

银行金库接口。

`using { /Fortnite.com/Devices }`

## Exposed Interfaces

此 暴露以下接口：
| Name | Description |
| enableable | 由「实例可被启用/禁用」的类实现。 |


## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [StartSequenceEvent](bank_vault_interface_startsequenceevent.md) | listenable(payload) | 金库开启流程被玩家或事件启动时触发；如适用，载荷为触发该事件的代理。 |
| [OpenEvent](bank_vault_interface_openevent.md) | listenable(payload) | 金库被打开时触发（弱点被破坏或由事件触发）。载荷为最后伤害弱点的代理；无外部伤害时为启动流程的代理；由函数触发时为空。 |
| [ActivateWeakpointEvent](bank_vault_interface_activateweakpointevent.md) | listenable(payload) | 弱点被激活时触发；弱点开始发光，但在后续 WeakpointVulnerableEvent 之前不会变得可受击。载荷为激活金库的代理（由函数触发时为空）与按激活顺序的弱点序号（0-4）。 |
| [WeakpointVulnerableEvent](bank_vault_interface_weakpointvulnerableevent.md) | listenable(payload) | 弱点变得可受击时触发。载荷为激活金库的代理（由函数触发时为空）与按激活顺序的弱点序号（0-4）。 |
| [DestroyWeakpointEvent](bank_vault_interface_destroyweakpointevent.md) | listenable(payload) | 弱点被摧毁时触发。载荷为最后伤害该弱点的代理（无外部伤害时为启动流程的代理；由函数触发时为空）与按激活顺序的弱点序号（0-4）。 |
| [RequireThermite](bank_vault_interface_requirethermite.md) | ?logic | 玩家与门交互以启动开库流程时是否需要铝热剂（thermite）。 |
| [WeakpointDamagePerSecond](bank_vault_interface_weakpointdamagepersecond.md) | ?float | 每秒对当前弱点造成的伤害；负数为治疗弱点。只有金库流程激活时弱点才可受伤害。 |
| [WeakpointTakesExternalDamage](bank_vault_interface_weakpointtakesexternaldamage.md) | ?logic | 金库流程激活期间，弱点是否可被武器与物品伤害。 |
| [MaxWeakpointHealth](bank_vault_interface_maxweakpointhealth.md) | ?float | 此设备弱点的最大生命值。 |

### Functions
| Function Name | Description |
| [ForceOpen](bank_vault_interface_forceopen.md) | 摧毁剩余弱点并打开金库门。需要设备处于启用状态。 |
| [StartSequence](bank_vault_interface_startsequence.md) | 开始「不用铝热剂打开金库门」的事件流程；流程已暂停则取消暂停。需要设备启用。只有金库流程激活时弱点才可受伤害。 |
| [PauseSequence](bank_vault_interface_pausesequence.md) | 禁用弱点可受击状态并冻结各自进度。只有金库流程激活时弱点才可受伤害。 |
| [Reset](bank_vault_interface_reset.md) | 把金库恢复到默认状态、停用设备，并把所有弱点治愈到满血。需要设备启用。 |
| [IsSequenceActive](bank_vault_interface_issequenceactive.md) | 金库流程当前是否处于激活且未暂停状态。 |
| [DestroyActiveWeakpoint](bank_vault_interface_destroyactiveweakpoint.md) | 摧毁当前弱点。需要设备启用，且必须存在当前弱点。 |
| [RestoreActiveWeakpoint](bank_vault_interface_restoreactiveweakpoint.md) | 把当前弱点恢复到满血。需要设备启用，且必须存在当前弱点。 |
| [GetActiveWeakpointIndex](bank_vault_interface_getactiveweakpointindex.md) | 获取当前弱点的序号（从 0 起），与设备启用状态无关。没有当前弱点时（流程未激活或弱点刚被摧毁）返回失败。 |
| [GetWeakpointCount](bank_vault_interface_getweakpointcount.md) | 获取弱点总数。 |
| [GetActiveWeakpointHealth](bank_vault_interface_getactiveweakpointhealth.md) | 获取当前弱点的生命值；没有当前弱点则返回失败。 |
| [SetActiveWeakpointHealth](bank_vault_interface_setactiveweakpointhealth.md) | 设置当前弱点的生命值；设为 0.0 或 false 会摧毁弱点。会钳制到 WeakpointMaxHealth 上限。 |
