---
name: creative_device
slug: fortnitedotcom/devices/creative_device
url: https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_device
kind: class
module: /Fortnite.com/Devices
grade: S
depth: full
status: done
---

# creative_device class <S>

> Inherit from this to create a custom creative device. Inherited classes will appear in the UEFN content browser the next time Verse compiles. Instances of your derived creative_device can then be placed in the island by dragging them from the content browser into the scene.
> 继承此类来创建自定义创意设备。Verse 下次编译后，派生类会出现在 UEFN 内容浏览器中；把派生的 creative_device 实例从内容浏览器拖入场景，即可摆放到岛屿上。

`using { /Fortnite.com/Devices }`

## Exposed Interfaces

This class exposes the following interfaces:（此类暴露以下接口：）

| Name | Description |
|---|---|
| creative_object_interface | （官网无描述。） |

## Members

This class has functions, but no data members.（此类只有函数，没有数据成员。）

### Functions

| Function Name | Description |
|---|---|
| [OnBegin](creative_device_onbegin.md) | 重写以在游戏体验开始时添加自定义逻辑。 |
| [OnEnd](creative_device_onend.md) | 重写以在游戏体验结束时添加自定义逻辑。在 OnEnd 内 spawn 的协程可能永远不会执行。 |
| [GetTransform](creative_device_gettransform.md) | 返回 creative_device 的变换，单位为厘米（cm）。 |
| [TeleportTo](creative_device_teleportto.md) | 将 creative_device 瞬移到指定的 Position 与 Rotation。 |
| [TeleportTo](creative_device_teleportto.md) | 将 creative_device 瞬移到 Transform 指定的位置，同时相应地应用旋转与缩放。 |
| [MoveTo](creative_device_moveto.md) | 在指定的秒数内把 creative_device 移动到指定的 Position 与 Rotation。若设备当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| [MoveTo](creative_device_moveto.md) | 在指定的秒数内把 creative_device 移动到指定的 Transform。若设备当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| [GetGlobalTransform](creative_device_getglobaltransform.md) | 获取此设备的全局变换。 |
| [SetGlobalTransform](creative_device_setglobaltransform.md) | 设置此设备的全局变换。 |
| [TeleportTo](creative_device_teleportto.md) | 将 creative_device 瞬移到 Transform 指定的位置，同时相应地应用旋转与缩放。 |
| [MoveTo](creative_device_moveto.md) | 在指定的秒数内把 creative_device 移动到指定的 Transform。若设备当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。 |
| [Show](creative_device_show.md) | 在世界中显示此设备。 |
| [Hide](creative_device_hide.md) | 在世界中隐藏此设备。 |

## 示例

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

# 最小可运行脚本骨架：每个项目的起点
hello_device := class(creative_device):

    @editable
    MyButton : button_device = button_device{}

    OnBegin<override>()<suspends>:void =
        Print("设备已启动")
        MyButton.InteractedWithEvent.Subscribe(OnPress)

    OnPress(Agent:agent):void =
        Print("按钮被按下")
```

## 补充说明

- 每个自制脚本的第一个类：继承 creative_device 后，Verse 编译即出现在内容浏览器，拖入场景生效。
- `OnBegin<override>()<suspends>` 是一切入口；OnEnd 里 spawn 的协程官方明示可能不执行，收尾逻辑要同步完成。
- `@editable` 字段用于在详情面板连线其他设备/控件（控件类型族见 [editable_number function](../../01_Verse.org/100_Simulation/editable_number.md)）。
- 表中 TeleportTo/MoveTo 各出现多次，是官网对不同参数形态分别建页所致（对应多份成员页）。
