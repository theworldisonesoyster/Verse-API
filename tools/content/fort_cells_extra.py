# -*- coding: utf-8 -*-
# Fortnite UI/AI/Animation/Vehicles 表内描述补充对照
EXTRA_CELLS = {
    "Request to play a given reaction on the Sidekick. This reaction is not guaranteed to play immediately; instead, the StartPlayReactionEvent should be used to monitor this. This will fail if the Sidekick cannot play the given reaction.":
        "请求在 Sidekick 上播放给定反应。不保证立即播放；应通过 StartPlayReactionEvent 监视。无法播放该反应则失败。",

    "Used to identify a HUD element.": "用于标识一个 HUD 元素。",
    "Base class for all UI elements drawn on the player's screen.": "绘制在玩家屏幕上的一切 UI 元素的基类。",
    "The text to display to the user. Used only during initialization of the widget and not modified by SetText.":
        "展示给用户的文本；仅在初始化时使用，SetText 不会修改它。",
    "The UI input action that will trigger the Click event of this button.": "将触发此按钮 Click 事件的 UI 输入动作。",
    "Returns the widget's parent widget. Fails if no parent exists, such as if this widget is not in the player_ui or is itself the root widget.":
        "返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。",
    "Returns the widget that added this widget to the player_ui. The root widget will return itself. Fails if this widget is not in the player_ui.":
        "返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。",
    "Gets the text currently in the widget.": "获取控件中的当前文本。",
    "Returns the current widget_visibility state.": "返回当前 widget_visibility 状态。",
    "true if this widget can be modified interactively by the player.": "若此 widget 可被玩家交互修改则返回 true。",
    "Subscribable event that fires when the button is clicked.": "按钮被点击时触发的可订阅事件。",
    "Enables or disables whether the player can interact with this widget.": "启用或禁用玩家与此 widget 的交互。",
    "Sets the text displayed in the widget.": "设置控件中显示的文本。",
    "Shows or hides the widget without removing itself from the containing player_ui. See widget_visibility for details.":
        "显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。",
    "Button with text message common base class. Displays a button with a custom message string.":
        "带文本消息的按钮通用基类：显示一个带自定义消息文本的按钮。",
    "The maximum value that the slider can haver. Used only during initialization of the widget and not modified by SetMaxValue.":
        "滑条的最大值；仅在初始化时使用，SetMaxValue 不会修改它。",
    "The minimum value that the slider can haver. Used only during initialization of the widget and not modified by SetMinValue.":
        "滑条的最小值；仅在初始化时使用，SetMinValue 不会修改它。",
    "The amount to adjust the value by, when using a controller or keyboard. Used only during initialization of the widget and not modified by SetStepSize.":
        "使用手柄/键盘时的调节步长；仅在初始化时使用，SetStepSize 不会修改它。",
    "The value to display to the user. Used only during initialization of the widget and not modified by SetValue.":
        "展示给用户的值；仅在初始化时使用，SetValue 不会修改它。",
    "Gets the maximum value of the slider.": "获取滑条最大值。",
    "Gets the minimum value of the slider.": "获取滑条最小值。",
    "Gets the amount to adjust the value by.": "获取调节步长。",
    "Gets the value of the slider.": "获取滑条当前值。",
    "Subscribable event that fires when the value of the slider has changed.": "滑条值变化时触发的可订阅事件。",
    "Sets the maximum value of the slider, will enforce that the sliders maximum value is always larger than or equal to the minimum value.":
        "设置滑条最大值；会保证最大值始终 ≥ 最小值。",
    "Sets the minimum value of the slider, will enforce that the sliders maximum value is always larger than or equal to the minimum value.":
        "设置滑条最小值；会保证最大值始终 ≥ 最小值。",
    "Sets the amount to adjust the value by, when using a controller or keyboard.": "设置使用手柄/键盘时的调节步长。",
    "Sets the value of the slider, will clamp the value to be within the sliders minimum and maximum value.":
        "设置滑条值；数值会被钳制在最小值与最大值之间。",
    "Base widget for text widget.": "文本控件的基类。",
    "Whether the text should be automatically wrapped.": "文本是否自动换行。",
    "The justification to display to the user. Used only during initialization of the widget and not modified by SetJustification.":
        "展示给用户的对齐方式；仅在初始化时使用，SetJustification 不会修改它。",
    "The policy that determine what happens when the text is longer than its allowed length. Used only during initialization of the widget and not modified by SetOverflowPolicy.":
        "文本超长处理策略；仅在初始化时使用，SetOverflowPolicy 不会修改它。",
    "The color of the shadow. Used only during initialization of the widget and not modified by SetShadowColor.":
        "阴影颜色；仅在初始化时使用，SetShadowColor 不会修改它。",
    "The direction the shadow is cast. Used only during initialization of the widget and not modified by SetShadowOffset.":
        "阴影投射方向；仅在初始化时使用，SetShadowOffset 不会修改它。",
    "The opacity of the shadow. Used only during initialization of the widget and not modified by SetShadowOpacity.":
        "阴影不透明度；仅在初始化时使用，SetShadowOpacity 不会修改它。",
    "The color of the displayed text. Used only during initialization of the widget and not modified by SetTextColor.":
        "显示文本的颜色；仅在初始化时使用，SetTextColor 不会修改它。",
    "The opacity of the displayed text. Used only during initialization of the widget and not modified by SetTextOpacity.":
        "显示文本的不透明度；仅在初始化时使用，SetTextOpacity 不会修改它。",
    "The size of the displayed text. Used only during initialization of the widget and not modified by SetTextSize.":
        "显示文本的字号；仅在初始化时使用，SetTextSize 不会修改它。",
    "The wrapping policy to determine where the line can be broken.": "决定可在何处断行的换行策略。",
    "Whether text wraps onto a new line when it's length exceeds this width; if this value is zero or negative, no wrapping occurs.":
        "文本长度超过此宽度时是否换行；值为零或负数则不换行。",
    "Gets the text justification in the widget.": "获取控件中的文本对齐方式。",
    "Gets the policy that determine what happens when the text is longer than its allowed length.": "获取文本超长处理策略。",
    "Gets the color of the shadow.": "获取阴影颜色。",
    "Gets the direction the shadow is cast.": "获取阴影投射方向。",
    "Gets the opacity of the shadow.": "获取阴影不透明度。",
    "Gets the color of the displayed text.": "获取显示文本的颜色。",
    "Gets the opacity of the displayed text.": "获取显示文本的不透明度。",
    "Gets the size of the displayed text.": "获取显示文本的字号。",
    "Sets the text justification in the widget.": "设置控件中的文本对齐方式。",
    "Sets the policy that determine what happens when the text is longer than its allowed length.": "设置文本超长处理策略。",
    "Sets the color of the shadow.": "设置阴影颜色。",
    "Sets the direction the shadow is cast.": "设置阴影投射方向。",
    "Sets the opacity of the shadow.": "设置阴影不透明度。",
    "Sets the color of the displayed text.": "设置显示文本的颜色。",
    "Sets the opacity of the displayed text.": "设置显示文本的不透明度。",
    "Sets the size of the displayed text.": "设置显示文本的字号。",
    "Shows a set of HUD elements for every player. Note: This can be overridden by rules set by 'ForPlayer' functions since player specific rules are prioritized over general rules.":
        "为所有玩家显示一组 HUD 元素。注意：可被 ForPlayer 系列函数设置的规则覆盖——玩家级规则优先于通用规则。",
    "Hides a set of HUD elements for every player. Note: This can be overridden by rules set by 'ForPlayer' functions since player specific rules are prioritized over general rules.":
        "为所有玩家隐藏一组 HUD 元素。注意：可被 ForPlayer 系列函数设置的规则覆盖——玩家级规则优先于通用规则。",
    "Resets the visibility for a set of HUD elements for every player. Note: This will not clear player specific rules set by the 'ForPlayer' functions which can only be reset by calling 'ResetElementsForPlayer'.":
        "为所有玩家重置一组 HUD 元素的可见性。注意：不会清除 ForPlayer 系列函数设置的玩家级规则——那只能调用 ResetElementsForPlayer 重置。",
    "Shows a set of HUD elements for a single player. Note: This overrides general rules set by non-player functions for the given elements. Call 'ResetElementsForPlayer' in order to return the player to general behavior":
        "为单个玩家显示一组 HUD 元素。注意：对该元素会覆盖非玩家函数设置的通用规则；调用 ResetElementsForPlayer 可恢复通用行为。",
    "Hides a set of HUD elements for a single player. Note: This overrides general rules set by non-player functions for the given elements. Call 'ResetElementsForPlayer' in order to return the player to general behavior":
        "为单个玩家隐藏一组 HUD 元素。注意：对该元素会覆盖非玩家函数设置的通用规则；调用 ResetElementsForPlayer 可恢复通用行为。",
    "Resets the player-specific visibility rules of a set of HUD elements for a single player. Note: This will not reset rules that have been set by means other than the 'PerPlayer' functions.":
        "为单个玩家重置一组 HUD 元素的玩家级可见性规则。注意：不会重置通过非 PerPlayer 函数设置的规则。",
    "Component to manage functionality shared by all Sidekick types.": "管理所有 Sidekick 类型共享功能的组件。",
    "Implemented by classes whose instances can change visibility to be shown or hidden.": "由「实例可切换显示/隐藏」的类实现。",
    "The Sidekick will run animations to react to the state of the player. Is this system enabled?":
        "Sidekick 是否运行动画以响应玩家状态？（该系统是否启用）",
    "Signaled whenever the Sidekick's mood changes, either via the underlying mood system, or an override is applied. Returns (Previous Mood, New Mood).":
        "Sidekick 情绪变化时触发（无论是情绪系统自动变化还是手动覆盖）。载荷为（旧情绪, 新情绪）。",
    "Signaled whenever the Sidekick's mood changes, either via the underlying mood system, or an override is applied. Returns the previous and new mood.":
        "Sidekick 情绪变化时触发；返回旧情绪与新情绪。",
    "Sidekicks have a built-in player interaction; this can be disabled by setting this to false.":
        "Sidekick 自带玩家交互；设为 false 可禁用。",
    "Enable or disable antics (idle personality animations) on the Sidekick. Enabled by default.":
        "启用/禁用 Sidekick 的滑稽动作（待机个性动画）；默认启用。",
    "By default, Sidekicks will change their mood depending on actions in the game. This value will lock the Sidekick into the mood passed in, overriding the automatic mood system.":
        "默认情况下 Sidekick 会根据游戏中的行为改变情绪；设置此值可把 Sidekick 锁定到指定情绪，覆盖自动情绪系统。",
    "Is the Sidekick visible?": "Sidekick 是否可见？",
    "Signaled when the Sidekick starts to play a reaction, returns the reaction that started playing.": "Sidekick 开始播放反应动作时触发；返回开始播放的反应。",
    "Signaled when the Sidekick ends playing a reaction, returns the reaction that played.": "Sidekick 结束播放反应动作时触发；返回播放过的反应。",
    "Get the Sidekick's current mood.": "获取 Sidekick 当前情绪。",
    "Get the agent that owns this Sidekick.": "获取拥有此 Sidekick 的代理。",
    "Request to play a given reaction on the sidekick. This reaction is not guaranteed to play immediately; instead, the StartPlayReactionEvent should be used to monitor this. This will fail if the Sidekick cannot play the given reaction.":
        "请求在 Sidekick 上播放给定反应。不保证立即播放；应通过 StartPlayReactionEvent 监视。无法播放该反应则失败。",
    "Signaled when the Sidekick enters spark mode.": "Sidekick 进入 Spark 模式时触发。",
    "Signaled when the Sidekick exits spark mode": "Sidekick 退出 Spark 模式时触发。",
    "Automatic switching in and out of spark mode can be turned off, forcing spark mode always, by setting this value to true.":
        "设为 true 可关闭 Spark 模式的自动进出，强制始终处于 Spark 模式。",
    "Fortnite NPC AI actions management": "堡垒之夜 NPC 的 AI 行为管理。",
    "Fortnite Guard perception management": "堡垒之夜 Guard 的感知管理。",
    "Multiplier on the movement speed (value is clamped between 0.5 and 2).": "移动速度倍率（钳制在 0.5~2 之间）。",
    "Attack the target. The target must have been detected.": "攻击目标；目标必须已被侦测。",
    "Change stance to crouch. Will never complete unless interrupted.": "切换为蹲伏姿态；不中断则永不完成。",
    "Look at the specified location. If LockFocus is false, the action stops once the NPC is facing the position.":
        "看向指定位置。LockFocus 为 false 时，NPC 面向该位置后动作即停止。",
    "Look at the specified Entity. If LockFocus is false, the action stops once the NPC is facing the entity.":
        "看向指定实体。LockFocus 为 false 时，NPC 面向该实体后动作即停止。",
    "Return the current destination of the character": "返回角色当前的导航目的地。",
    "Return the current destination of the character": "返回角色当前的导航目的地。",
    "Stay idle for a specific duration.": "保持空闲指定时长。",
    "Trigger a jump.": "触发一次跳跃。",
    "Move in range to attack the current target.": "移动到可攻击当前目标的范围内。",
    "Navigate toward the specified navigation target.": "向指定的导航目标移动。",
    "Navigate toward the specified target": "向指定目标移动。",
    "Play a random emote from the character emotes bank.": "从角色表情库中随机播放一个表情。",
    "Revive the specified target.": "复活指定目标。",
    "Roam around the current position. Use 'Tether' to specify the radius; otherwise, the Fortnite guard will roam anywhere.":
        "在当前位置附近游荡。可用 Tether 指定半径；否则 Guard 会随处游荡。",
    "Trigger a slide.": "触发一次滑铲。",
    "Go back to standing.": "回到站立状态。",
    "Stop navigation": "停止导航。",
    "Stop navigation.": "停止导航。",
    "Return the current destination of the character.": "返回角色当前的导航目的地。",
    "Request to play a given reaction on the sidekick. This reaction is not guaranteed to play immediately; instead, the StartPlayReactionEvent should be used to monitor this. This will fail if the Sidekick cannot play the given reaction":
        "请求在 sidekick 上播放给定反应。不保证立即播放；应通过 StartPlayReactionEvent 监视。无法播放该反应则失败。",
    "Tether the NPC to a position. 'Radius' is in centimeters.": "把 NPC 拴定到某个位置。Radius 单位为厘米。",
    "Tether the NPC to an entity. 'Radius' is in centimeters.": "把 NPC 拴定到某个实体。Radius 单位为厘米。",
    "Untether the NPC.": "解除 NPC 的拴定。",
    "Wait for a specific duration": "等待指定时长。",
    "Apply a multiplier on the movement speed (Multiplier is clamped between 0.5 and 2)": "对移动速度施加倍率（钳制在 0.5~2）。",
    "Fortnite NPC perception management": "堡垒之夜 NPC 的感知管理。",
    "Current alert level.": "当前警戒级别。",
    "Event when the alert level has changed.": "警戒级别变化时的事件。",
    "Potentially detected obstacle.": "可能被侦测到的障碍物。",
    "Information about all detected targets.": "所有已侦测目标的信息。",
    "Event when a new obstacle is detected.": "侦测到新障碍物时的事件。",
    "Event when a target was detected.": "侦测到目标时的事件。",
    "Event when the current obstacle was forgotten.": "当前障碍物被遗忘时的事件。",
    "Event when a target was forgotten.": "目标被遗忘时的事件。",
    "Event when a target is heard. Hearing sense must be active.": "听到目标时的事件（听觉感知须处于激活状态）。",
    "Information about the primary threat.": "主要威胁的信息。",
    "Event when the primary threat has changed.": "主要威胁变化时的事件。",
    "Event when a target is seen. Sight sense must be active.": "看到目标时的事件（视觉感知须处于激活状态）。",
    "Event when a target is touched. Touch sense must be active.": "触到目标时的事件（触觉感知须处于激活状态）。",
    "Get the current alert level for a specific target.": "获取对特定目标的当前警戒级别。",
    "This function is called when the NPC is added to the simulation.": "NPC 被加入模拟时调用此函数。",
    "This function is called when the NPC is removed from the simulation.": "NPC 被移出模拟时调用此函数。",
    "Returns the agent associated with this behavior.": "返回与此行为关联的代理。",
    "Returns the entity associated with this behavior.": "返回与此行为关联的实体。",
    "The entity that was detected.": "被侦测到的实体。",
    "True if the target can be seen.": "目标可见则为 true。",
    "Attitude toward this target.": "对此目标的态度。",
    "Last known position of this target.": "此目标最后已知位置。",
    "Apply the look and customizations of agent's currently equipped Sidekick to this Sidekick NPC. This will fail if the NPC does not use the FortniteSidekick cosmetic look or if the given agent does not have a Sidekick equipped in their locker.":
        "把该代理当前装备的 Sidekick 的外观与自定义应用到这个 Sidekick NPC。若 NPC 未使用 FortniteSidekick 外观，或该代理的柜子中没有装备 Sidekick，则失败。",
    "Look At specified location. Will never complete unless interrupted.": "看向指定位置；不中断则永不完成。",
    "Look At specified Agent. Will never complete unless interrupted.": "看向指定代理；不中断则永不完成。",
    "Set custom leash position. 'InnerRadius' ranges from 0.0 to 20000.0 (in centimeters). 'OuterRadius' ranges from 0.0 to 20000.0 (in centimeters) and no less than 'InnerRadius'.":
        "设置自定义拴留位置。InnerRadius 范围 0.0~20000.0（厘米）；OuterRadius 范围 0.0~20000.0（厘米）且不小于 InnerRadius。",
    "Set the agent to be the new center of the leash. 'InnerRadius' ranges from 0.0 to 20000.0 (in centimeters). 'OuterRadius' ranges from 0.0 to 20000.0 (in centimeters) and no less than 'InnerRadius'.":
        "把该代理设为拴留的新中心。InnerRadius 范围 0.0~20000.0（厘米）；OuterRadius 范围 0.0~20000.0（厘米）且不小于 InnerRadius。",
    "Removes the current leash.": "解除当前拴留。",
    "The action has failed during its execution.": "动作在执行过程中失败。",
    "The action has been canceled before completion.": "动作在完成前被取消。",
    "The action was not allowed to start.": "动作未被允许开始。",
    "The destination has been reached": "已到达目的地",
    "The destination has been reached.": "已到达目的地。",
    "The destination was partially reached (the destination is currently not reachable).": "部分到达（目的地当前不可达）。",
    "The destination has been partially reached (AllowPartialPath was used)": "部分到达（使用了 AllowPartialPath）。",
    "Navigation has been interrupted before completion": "导航在完成前被打断",
    "Navigation has been interrupted before completion.": "导航在完成前被打断。",
    "The navigating agent is blocked": "导航中的代理被阻挡",
    "The navigating agent is blocked.": "导航中的代理被阻挡。",
    "The destination cannot be reached": "目的地无法到达",
    "The destination cannot be reached.": "目的地无法到达。",
    "The navigation request is invalid.": "导航请求无效。",
    "The guard has not detected any hostile target.": "Guard 未侦测到任何敌对目标。",
    "The guard has seen a hostile target but hasn't identified it yet.": "Guard 看到了敌对目标但尚未辨识。",
    "The guard has identified a hostile target but can't see it any more.": "Guard 已辨识出敌对目标但已看不到它。",
    "The guard has identified a hostile target.": "Guard 已辨识出敌对目标。",
    "Event triggered when the animation is completed.": "动画完成时触发的事件。",
    "Event triggered when the animation is interrupted.": "动画被打断时触发的事件。",
    "Event triggered when the animation has finished to blend out.": "动画完成混合淡出（blend out）时触发的事件。",
    "Event triggered when the animation is beginning to blend out.": "动画开始混合淡出时触发的事件。",
    "Returns the state of the animation playback.": "返回动画播放状态。",
    "Stops the animation.": "停止动画。",
    "Helper function that waits for the animation to complete or be interrupted.": "辅助函数：等待动画完成或被打断。",
    "Helper function that succeeds if the state is Playing, BlendingIn, or BlendingOut.": "辅助函数：状态为 Playing/BlendingIn/BlendingOut 时成功。",
    "Play an animation sequence.": "播放动画序列。",
    "Start an animation sequence and obtain an instance to query and manipulate.": "开始一个动画序列，并取得可查询与操控的实例。",
    "The animation completed successfully.": "动画成功完成。",
    "The animation was interrupted whilst playing.": "动画在播放中被中断。",
    "The animation encountered an error during initialization or whilst playing.": "动画在初始化或播放中遇到错误。",
    "The animation is blending in.": "动画正在混合淡入。",
    "The animation has blended in, is playing, and has not begun blending out.": "动画已完成淡入、正在播放、尚未开始淡出。",
    "The animation is playing and is blending out.": "动画正在播放并正在淡出。",
    "The animation was stopped internally.": "动画被内部停止。",
    "The animation was interrupted externally.": "动画被外部中断。",
    "An error occurred at creation or during playback.": "创建或播放期间发生错误。",
    "Controls if fort_character can still turn while in stasis.": "控制 fort_character 在凝固期间是否仍可转身。",
    "Controls if fort_character can still fall while in stasis.": "控制 fort_character 在凝固期间是否仍可下落。",
    "Controls if fort_character can still perform emotes while in stasis.": "控制 fort_character 在凝固期间是否仍可做表情。",
    "The agent currently occupying this seat, if any.": "当前占据此座位的代理（如有）。",
    "The fort_vehicle this seat belongs to.": "此座位所属的 fort_vehicle。",
    "Succeeds if this is a driver seat.": "这是驾驶座则成功。",
    "Attempts to seat Agent into this seat. Fails if the seat is occupied or the agent cannot be seated. Setting the occupant to false will remove any seated agent.":
        "尝试让 Agent 坐入此座位；座位被占或无法入座则失败。把占位者设为 false 会移除已入座的代理。",
    "Implemented by objects to allow reading position information.": "由对象实现，允许读取位置信息。",
    "Implemented by Fortnite objects that have health state and can be eliminated.": "由拥有生命状态、可被淘汰的堡垒之夜对象实现。",
    "Implemented by Fortnite objects that can be damaged.": "由可被伤害的堡垒之夜对象实现。",
    "Implemented by Fortnite objects that can be passed through game action events, such as damage and heal. For example: player, vehicle, or weapon. Event Listeners often use game_action_causer to pass along additional information about what weapon caused the damage. Systems will then use that information for completing quests or processing game specific event logic.":
        "由可作为游戏动作事件（如伤害、治疗）载体传递的堡垒之夜对象实现，例如玩家、载具或武器。事件监听器常用 game_action_causer 传递「什么武器造成了伤害」等附加信息，供任务系统或玩法事件逻辑使用。",
    "The current speed of the vehicle in m/s.": "载具当前速度（米/秒）。",
    "The boost state of the vehicle. If the vehicle uses boost, this value will be between 0.0 and BoostCapacity. Otherwise, this value will be false.":
        "载具的推进（boost）状态；使用推进的载具该值在 0.0 与 BoostCapacity 之间，否则为 false。",
    "The maximum boost capacity of the vehicle. If the vehicle uses boost, this value will be between 1.0 and Inf. Otherwise, this value will be false.":
        "载具的最大推进容量；使用推进的载具该值在 1.0 与 Inf 之间，否则为 false。",
    "Succeeds if this fort_vehicle is standing on ground.": "此 fort_vehicle 在地面上则成功。",
    "Succeeds if this fort_vehicle is standing in air.": "此 fort_vehicle 在空中则成功。",
    "Succeeds if this fort_vehicle is standing in water.": "此 fort_vehicle 在水中则成功。",
    "Returns an array with all agent currently occupying the vehicle.": "返回当前占据载具的全部代理数组。",
    "Returns an array with all the current drivers of the vehicle, which is usually a single agent.": "返回载具当前全部驾驶员的数组（通常只有一个代理）。",
    "Returns the fuel state of the vehicle. If the vehicle uses fuel, this value will be between 0.0 and GetFuelCapacity. Otherwise, this value will be -1.0.":
        "返回载具油量状态；用油的载具该值在 0.0 与 GetFuelCapacity 之间，否则为 -1.0。",
    "Returns the maximum fuel capacity of the vehicle. If the vehicle uses fuel, this value will be between 1.0 and Inf. Otherwise, this value will be -1.0.":
        "返回载具最大油箱容量；用油的载具该值在 1.0 与 Inf 之间，否则为 -1.0。",
    "Teleports the fort_vehicle to the specified Position and Rotation.": "把 fort_vehicle 瞬移到指定的位置与旋转。",
    "Removes the specified agent from the vehicle. Fails if the agent is not in the vehicle.": "把指定代理移下载具；代理不在车上则失败。",
    "Removes all occupying agents from the vehicle.": "移下载具上的所有代理。",
    "Attempts to add the agent to the fort_vehicle. If there are no empty seats, or the agent cannot otherwise be placed in the vehicle, the operation fails.":
        "尝试把代理加进 fort_vehicle；没有空座或无法安置则失败。",
    "Returns an array of all fort_vehicle_seats in the fort_vehicle.": "返回 fort_vehicle 中所有 fort_vehicle_seat 的数组。",
}
