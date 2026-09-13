# -*- coding: utf-8 -*-
# Devices full/brief 页的表内描述补充对照
EXTRA_CELLS = {
    "Set a ‘creative_prop’s linear velocity in meters/second. Will not do anything if physics is disabled.":
        "设置 creative_prop 的线速度（米/秒）。物理被禁用时无效果。",

    "Signaled each time a keyframe is reached. Callback(KeyframeIndex:int, InReverse:logic). Note that the KeyframeIndex in the callback is generally in [1, NumDeltaKeyframes] except that in a PingPong animation the final keyframe played in reverse is identified as index 0. This is because SetAnimation takes delta keyframes whereas this event notifies the listener that a specific keyframe has been reached.":
        "每到达一个关键帧时触发。回调参数（关键帧序号:int, 是否反向:logic)。载荷中的序号一般在 [1, NumDeltaKeyframes]；PingPong 动画中反向播放的最后一个关键帧记为 0——因为 SetAnimation 接收的是增量关键帧，而此事件通知的是「到达了某个特定关键帧」。",
    "Signaled when the entire animation is complete. This will only fire for OneShot animations.":
        "整个动画完成时触发；仅对 OneShot（单次）动画触发。",
    "Signaled when the state has changed. Use GetState to get the new state.": "状态变化时触发；用 GetState 获取新状态。",
    "Suspends at the callsite until the next keyframe_delta is finished. This will also return if the animation is aborted or not playing. See await_next_keyframe_result if your code needs to take different paths based on why AwaitNextKeyframe returned.":
        "在调用处挂起，直到下一个 keyframe_delta 完成；动画被中止或未播放时也会返回。若代码需要根据 AwaitNextKeyframe 的返回原因走不同分支，参见 await_next_keyframe_result。",
    "Starts or resumes playback of the animation.": "开始或恢复动画播放。",
    "Pauses the animation if it is already playing.": "若动画正在播放则暂停。",
    "Stops playback and resets the animation to the first keyframe. Also resets the prop transform. Calling this method is valid while the animation is in the Playing or Paused states.":
        "停止播放并把动画重置到第一个关键帧，同时重置道具变换。动画处于 Playing 或 Paused 状态时调用有效。",
    "Returns the current state of this animation_controller.": "返回此 animation_controller 的当前状态。",
    "Succeeds if this animation_controllers target is still valid (i.e., the target has not been disposed of either via Dispose or through any external system.)":
        "若此 animation_controller 的目标仍有效则成功（即目标尚未通过 Dispose 或任何外部系统被销毁）。",
    "Sets the animation for the animation_controller. Animations are processed in the order provided in Keyframes. See notes in keyframe_delta and animation_mode for more details on controlling the animations.":
        "为 animation_controller 设置动画。动画按 Keyframes 给出的顺序处理；控制细节见 keyframe_delta 与 animation_mode 的说明。",
    "Override to add custom logic when the game experience begins.": "重写以在游戏体验开始时添加自定义逻辑。",
    "Override to add custom logic when the game experience ends. Any coroutines spawned inside OnEnd may never execute.":
        "重写以在游戏体验结束时添加自定义逻辑。在 OnEnd 内 spawn 的协程可能永远不会执行。",
    "Returns the transform of the creative_device with units in cm.": "返回 creative_device 的变换，单位为厘米（cm）。",
    "Teleports the creative_device to the specified Position and Rotation.": "将 creative_device 瞬移到指定的 Position 与 Rotation。",
    "Teleports the creative_device to the specified location defined by Transform, also applies rotation and scale accordingly.":
        "将 creative_device 瞬移到 Transform 指定的位置，同时相应地应用旋转与缩放。",
    "Moves the creative_device to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state.":
        "在指定的秒数内把 creative_device 移动到指定的 Position 与 Rotation。若设备当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。",
    "Moves the creative_device to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_device it will be stopped and put into the AnimationNotSet state.":
        "在指定的秒数内把 creative_device 移动到指定的 Transform。若设备当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。",
    "Gets the global transform of this device.": "获取此设备的全局变换。",
    "Sets the global transform of this device.": "设置此设备的全局变换。",
    "Shows this device in the world.": "在世界中显示此设备。",
    "Hides this device in the world.": "在世界中隐藏此设备。",
    "Base class for creative_device.": "creative_device 的基类。",
    "Base class for creative devices and props.": "创意设备与道具的基类。",
    "Returns the transform of the creative_object with units in cm. You must check creative_object.IsValid before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.":
        "返回 creative_object 的变换（厘米）。若对象可能已在玩法中被销毁，调用前必须检查 creative_object.IsValid，否则会产生运行时错误。",
    "Moves the creative_object to the specified Position and Rotation over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state.":
        "在指定的秒数内把 creative_object 移动到指定的 Position 与 Rotation。若对象当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。",
    "Moves the creative_object to the specified Transform over the specified time, in seconds. If an animation is currently playing on the creative_object it will be stopped and put into the AnimationNotSet state.":
        "在指定的秒数内把 creative_object 移动到指定的 Transform。若对象当前正在播放动画，动画会被停止并进入 AnimationNotSet 状态。",
    "Gets the global transform of this object.": "获取此对象的全局变换。",
    "Sets the global transform of this object.": "设置此对象的全局变换。",
    "Teleports the creative_object to the specified Position and Rotation.": "将 creative_object 瞬移到指定的 Position 与 Rotation。",
    "Teleports the creative_object to the specified location defined by Transform, also applies rotation and scale accordingly.":
        "将 creative_object 瞬移到 Transform 指定的位置，同时相应地应用旋转与缩放。",
    "Implemented by classes whose instances can become invalid at runtime.": "由「实例可能在运行时失效」的类实现。",
    "Enable/disable whether this prop can be damaged. If disabled, the creative prop will not take damage from attacks.":
        "启用/禁用此道具可否被伤害；禁用后创意道具不会受到攻击伤害。",
    "Apply an angular impulse to a \u2018creative_prop\u2019 with units in Newtonmeterseconds. Will not do anything if physics is disabled.":
        "对 creative_prop 施加角冲量（单位：牛顿·米·秒）。物理被禁用时无效果。",
    "Apply a force to a \u2018creative_prop\u2019 with units in Newtons. Will not do anything if physics is disabled.":
        "对 creative_prop 施加力（单位：牛顿）。物理被禁用时无效果。",
    "Apply a linear impulse to a \u2018creative_prop\u2019 with units in Newton*seconds. Will not do anything if physics is disabled.":
        "对 creative_prop 施加线冲量（单位：牛顿·秒）。物理被禁用时无效果。",
    "Apply a torque to a \u2018creative_prop\u2019 with units in Newton*meters. Will not do anything if physics is disabled.":
        "对 creative_prop 施加扭矩（单位：牛顿·米）。物理被禁用时无效果。",
    "Destroys the creative_prop and remove it from the island.": "销毁 creative_prop 并将其从岛屿移除。",
    "Returns a \u2018creative_prop\u2019s angular velocity in radians/second.": "返回 creative_prop 的角速度（弧度/秒）。",
    "Get whether a \u2018creative_prop\u2019 is dynamic (affected by physics functions).": "获取 creative_prop 是否为动态（受物理函数影响）。",
    "Returns a \u2018creative_prop\u2019s linear velocity in meters/second.": "返回 creative_prop 的线速度（米/秒）。",
    "Returns a \u2018creative_prop\u2019s mass in kilograms.": "返回 creative_prop 的质量（千克）。",
    "Hides the creative_prop in the world and disable collisions.": "在世界中隐藏 creative_prop 并禁用碰撞。",
    "Succeeds if this object has been disposed of either via Dispose() or through an external system.":
        "此对象已通过 Dispose() 或外部系统被销毁则成功。",
    "Succeeds if this object has not been disposed of either via Dispose() or through an external system.":
        "此对象尚未通过 Dispose() 或外部系统被销毁则成功。",
    "Set a \u2018creative_prop\u2019s angular velocity in radians/seconds. Will not do anything if physics is disabled.":
        "设置 creative_prop 的角速度（弧度/秒）。物理被禁用时无效果。",
    "Set whether a \u2018creative_prop\u2019 is dynamic (affected by physics functions). Will not do anything if physics is disabled OR the prop does not have a FortPhysicsComponent.":
        "设置 creative_prop 是否为动态（受物理函数影响）。物理被禁用或道具没有 FortPhysicsComponent 时无效果。",
    "Changes the Material of the Mesh used by this instance. Optionally can specify which Mesh element index to apply the material to, otherwise defaults to the 0 (default) Mesh element":
        "更改此实例所用网格的材质。可指定材质应用到的网格元素索引；不指定则默认为 0 号网格元素。",
    "Changes the Mesh used by this instance.": "更改此实例使用的网格。",
    "Shows the creative_prop in the world and enable collisions.": "在世界中显示 creative_prop 并启用碰撞。",
    "Triggered if this option wins the vote.": "此选项赢得投票时触发。",
    "Attempts to cast a vote for \u2018Agent\u2019 If the voting agent has votes remaining and the voting group has started a vote, the vote will be cast successfully. Fails if Agent does not have votes remaining or voting group has not started.":
        "尝试为 Agent 投票。若投票代理还有剩余票数且投票组已开始投票，则投票成功；代理没有剩余票数或投票未开始则失败。",
    "Returns the total votes cast for this option.": "返回此选项获得的总票数。",
    "Returns the group device this option corresponds to, if any. Fails if the option is not in a group, or there is no corresponding group device with the same ID.":
        "返回此选项对应的组设备（如有）；选项不在组中，或没有同 ID 的对应组设备则失败。",
    "Succeeds if Agent has voted for this option, fails if not.": "Agent 已为此选项投票则成功，否则失败。",
    "The string to display to the user when choosing which option to select.": "玩家选择选项时展示给它的文本。",
    "Triggers when the vault sequence is started by a player or event. Sends the agent that triggered this event, if applicable.":
        "金库开启流程被玩家或事件启动时触发；如适用，载荷为触发该事件的代理。",
    "Triggers when the vault is opened either by the destruction of its weakpoints or by an event. Sends the last agent that damaged a weakpoint or the agent that started the sequence if no external damage was done or none if the sequence was triggered by a function.":
        "金库被打开时触发（弱点被破坏或由事件触发）。载荷为最后伤害弱点的代理；无外部伤害时为启动流程的代理；由函数触发时为空。",
    "Triggers when a weakpoint is activated. The weakpoint will begin to glow, but does not become vulnerable until a subsequent WeakpointVulnerableEvent. Sends the agent that activated the vault or none if the sequence was triggered by a function, and the int index of the weakpoint from 0-4, in order of activation.":
        "弱点被激活时触发；弱点开始发光，但在后续 WeakpointVulnerableEvent 之前不会变得可受击。载荷为激活金库的代理（由函数触发时为空）与按激活顺序的弱点序号（0-4）。",
    "Triggers when a weakpoint becomes vulnerable. Sends the agent that activated the vault or none if the sequence was triggered by a function, and the int index of the weakpoint from 0-4, in order of activation.":
        "弱点变得可受击时触发。载荷为激活金库的代理（由函数触发时为空）与按激活顺序的弱点序号（0-4）。",
    "Triggers when a weakpoint is destroyed. Sends the last agent that damaged the weakpoint or the agent that started the sequence if no external damage was done or none if the sequence was triggered by a function, and the int index of the weakpoint from 0-4, in order of activation.":
        "弱点被摧毁时触发。载荷为最后伤害该弱点的代理（无外部伤害时为启动流程的代理；由函数触发时为空）与按激活顺序的弱点序号（0-4）。",
    "Whether the player needs thermite when interacting with the door to start the vault opening sequence.":
        "玩家与门交互以启动开库流程时是否需要铝热剂（thermite）。",
    "Damage dealt to the active weakpoint each second. Negative numbers heal the weakpoint. Weakpoints can only be damaged while the vault sequence is active.":
        "每秒对当前弱点造成的伤害；负数为治疗弱点。只有金库流程激活时弱点才可受伤害。",
    "Whether the weakpoint takes damage from weapons and items while vault sequence is active.": "金库流程激活期间，弱点是否可被武器与物品伤害。",
    "The max health of this device's weakpoints.": "此设备弱点的最大生命值。",
    "Destroys the remaining weakpoints and opens the vault door. Requires the device to be enabled.":
        "摧毁剩余弱点并打开金库门。需要设备处于启用状态。",
    "Begin the sequence of events to open the vault door without thermite, or unpauses the sequence if it was paused. Requires the device to be enabled. Weakpoints can only be damaged while the vault sequence is active.":
        "开始「不用铝热剂打开金库门」的事件流程；流程已暂停则取消暂停。需要设备启用。只有金库流程激活时弱点才可受伤害。",
    "Disable the weakpoint vulnerability and freeze the progress of each one. Weakpoints can only be damaged while the vault sequence is active.":
        "禁用弱点可受击状态并冻结各自进度。只有金库流程激活时弱点才可受伤害。",
    "Restores vault to default state, deactivates the device, and heals all weakpoints to max health. Requires the device to be enabled.":
        "把金库恢复到默认状态、停用设备，并把所有弱点治愈到满血。需要设备启用。",
    "Whether the vault sequence is currently active and not paused.": "金库流程当前是否处于激活且未暂停状态。",
    "Destroy the active weakpoint. Requires the device to be enabled. Must have active weakpoint.": "摧毁当前弱点。需要设备启用，且必须存在当前弱点。",
    "Restores the active weakpoint to full health. Requires the device to be enabled. Must have active weakpoint.":
        "把当前弱点恢复到满血。需要设备启用，且必须存在当前弱点。",
    "Gets the active weakpoint's index starting at 0, regardless of device's enabled state. Returns false if there is no active weakpoint, such as when the sequence is not active or directly after a weakpoint is destroyed.":
        "获取当前弱点的序号（从 0 起），与设备启用状态无关。没有当前弱点时（流程未激活或弱点刚被摧毁）返回失败。",
    "Gets the total number of weakpoints.": "获取弱点总数。",
    "Get active weakpoint's health. If there is no active weakpoint, returns false.": "获取当前弱点的生命值；没有当前弱点则返回失败。",
    "Set active weakpoint's health. Setting it to 0.0 or false will destroy the weakpoint. Clamps to maximum of WeakpointMaxHealth.":
        "设置当前弱点的生命值；设为 0.0 或 false 会摧毁弱点。会钳制到 WeakpointMaxHealth 上限。",
    "Triggers when Reboot Van has finished rebooting a set of players. agentis the player that started the reboot.":
        "重生的士完成一批玩家重生时触发；agent 为启动重生操作的玩家。",
    "The length of the recharge timer in seconds, regardless of the timer's current state. Clamped between 0.0 and 3600.0.":
        "充能计时器时长（秒），与计时器当前状态无关；钳制在 0.0~3600.0。",
    "The remaining time (in seconds) on the recharge timer. Clamped between 0.0 and 3600.0. If there is no active timer, getting returns 0.0. If there is no active timer, setting does nothing.":
        "充能计时器剩余时间（秒）；钳制在 0.0~3600.0。无激活计时器时读取返回 0.0、写入无效果。",
    "How quickly reboot progress decays when nobody is interacting with the Reboot Van. Custom Decay - Set a custom multiplier on the decay rate. Instant Reset - Instantly reset progress to zero. Battle Royale - Use Battle Royale's decay rate.":
        "无人交互时重生进度的衰减速度：Custom Decay——自定义衰减倍率；Instant Reset——立即清零进度；Battle Royale——使用大逃杀模式的衰减速度。",
    "Multiplier on the decay rate of reboot progress. Clamped between 0.1 and 2.0. Only used if RebootProgressDecay is set to Custom Decay.":
        "重生进度衰减速率的倍率；钳制在 0.1~2.0。仅在 RebootProgressDecay 设为 Custom Decay 时使用。",
    "Triggers when a player purchases a Reboot Card. agent is the player that purchased the Reboot Card.":
        "玩家购买重生的士卡片时触发；agent 为购买卡片的玩家。",
    "Determines if players can purchase an eliminated player's reboot card.": "决定玩家能否购买被淘汰玩家的重生的士卡片。",
    "Purchase reboot card options. Only used if CanPurchaseRebootCard is true.": "购买重生的士卡片的选项；仅在 CanPurchaseRebootCard 为 true 时使用。",
    "Enable the device.": "启用该设备。",
    "Disable the device.": "禁用该设备。",
    "Succeeds if the device is enabled, fails if it's disabled.": "设备处于启用状态则成功，禁用则失败。",
}
