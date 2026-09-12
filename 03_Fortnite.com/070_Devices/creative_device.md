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

# creative_device 🟦【S级·核心】

> The base class for every Verse-authored script you place on the island.
> 所有自制脚本设备的基类——你在 UEFN 里写的每个 `@editable` 脚本都继承它。

## 这是什么

Verse 脚本要以"设备"形态放进岛屿，类必须继承 `creative_device`。它提供：

- **入口生命周期**：`OnBegin`（体验开始时调用，可挂起，初始化/订阅/启动循环都写这里）、`OnEnd`（体验结束时；官方特别注明：**在 OnEnd 里 spawn 的协程可能永远不会执行**）。
- **空间操作**：`GetTransform`（设备摆放位置，单位厘米）、`TeleportTo`（瞬移，两个重载）、`MoveTo`（在指定秒数内平滑移动）。
- 实现了 `creative_object_interface`（作为创意对象的通用能力）。

与其他设备（button_device 等）的区别：creative_device 是**你自己的代码的容器**，其它设备是系统提供的功能件，两者通过 `@editable` 引用互相连线。

## 签名

```verse
creative_device<public> := class<concrete>(creative_device_base):
    OnBegin<public>()<suspends>:void          # override 入口
    OnEnd<public>():void                      # override 出口
    GetTransform<public>():transform          # 摆放变换（cm 单位）
    TeleportTo<public>(Position:vector3, Rotation:rotation):void
    TeleportTo<public>(Transform:transform):void
    MoveTo<public>(Position:vector3, Rotation:rotation, Time:float):void
```

## 最小示例

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

# 最小可运行脚本骨架：每个项目的起点
hello_device := class(creative_device):

    @editable
    MyButton : button_device = button_device{}    # 在编辑器里连线

    OnBegin<override>()<suspends>:void =
        Print("设备已启动")
        MyButton.InteractedWithEvent.Subscribe(OnPress)

    OnPress(Agent:agent):void =
        Print("按钮被按下")
```

## 常用成员

| 成员 | 说明 | 级别 |
|---|---|---|
| `OnBegin<override>()<suspends>` | 一切的入口 | 🟦 S |
| `OnEnd<override>()` | 收尾（协程可能不执行！） | 🟩 A |
| `TeleportTo` / `MoveTo` | 移动设备本体 | 🟨 B |
| `GetTransform` | 读摆放位置 | 🟨 B |

## 何时用 / 何时不用

- 用：任何自定义逻辑的第一个类。
- 不用：一个设备能干的就别拆五个——设备数量有上限，但逻辑内聚优先。

## 常见坑

- 忘写 `OnBegin<override>()` 里的 `<suspends>` 会无法 Sleep/订阅异步流程。
- 类里 `@editable` 的字段必须是 devices 模块的具体类型（或 editable_\*），写成泛型/接口面板不显示。
- OnEnd 中 spawn 的协程官方明言可能不执行——收尾逻辑要同步完成。

## 相关页面

- [editable_number](../../01_Verse.org/100_Simulation/editable_number.md) —— 参数暴露
- [listenable](../../01_Verse.org/010_Verse/listenable.md) —— 订阅设备事件
- [Sleep](../../01_Verse.org/100_Simulation/sleep.md)
