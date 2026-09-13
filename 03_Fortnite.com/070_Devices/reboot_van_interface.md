---
name: reboot_van_interface
slug: fortnitedotcom/devices/reboot_van_interface
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/reboot_van_interface
kind: interface
module: /Fortnite.com/devices
grade: B
depth: brief
status: done
---

# reboot_van_interface interface <B>

重生的士接口。

`using { /Fortnite.com/Devices }`

## Members

兼有数据成员和函数。

### Data
| Data Member Name | Type | Description |
| [RechargeCompleteEvent](reboot_van_interface_rechargecompleteevent.md) | listenable(payload) | 重生的士完成充能时触发；agent 为最后交互的玩家。 |
| [RebootEvent](reboot_van_interface_rebootevent.md) | listenable(payload) | 重生的士完成一批玩家重生时触发；agent 为启动重生操作的玩家。 |
| [RechargeTimerLength](reboot_van_interface_rechargetimerlength.md) | ?float | 充能计时器时长（秒），与计时器当前状态无关；钳制在 0.0~3600.0。 |
| [RechargeTimer](reboot_van_interface_rechargetimer.md) | ?float | 充能计时器剩余时间（秒）；钳制在 0.0~3600.0。无激活计时器时读取返回 0.0、写入无效果。 |
| [RebootProgressDecay](reboot_van_interface_rebootprogressdecay.md) | ?reboot_progress_decay_behavior | 无人交互时重生进度的衰减速度：Custom Decay——自定义衰减倍率；Instant Reset——立即清零进度；Battle Royale——使用大逃杀模式的衰减速度。 |
| [DecayRateMultiplier](reboot_van_interface_decayratemultiplier.md) | ??float | 重生进度衰减速率的倍率；钳制在 0.1~2.0。仅在 RebootProgressDecay 设为 Custom Decay 时使用。 |
| [RebootCardPurchaseEvent](reboot_van_interface_rebootcardpurchaseevent.md) | listenable(payload) | 玩家购买重生的士卡片时触发；agent 为购买卡片的玩家。 |
| [CanPurchaseRebootCard](reboot_van_interface_canpurchaserebootcard.md) | ?logic | 决定玩家能否购买被淘汰玩家的重生的士卡片。 |
| [PurchaseRebootCardOptions](reboot_van_interface_purchaserebootcardoptions.md) | ??reboot_card_purchase_options | 购买重生的士卡片的选项；仅在 CanPurchaseRebootCard 为 true 时使用。 |

### Functions
| Function Name | Description |
| [EnableReboot](reboot_van_interface_enablereboot.md) | 启用该设备。 |
| [DisableReboot](reboot_van_interface_disablereboot.md) | 禁用该设备。 |
| [IsEnabledReboot](reboot_van_interface_isenabledreboot.md) | 设备处于启用状态则成功，禁用则失败。 |
