# -*- coding: utf-8 -*-
# UE.com 组件表内描述的补充对照
EXTRA_CELLS = {
    "Relative ordering among categories in the quest UI; lower values sort first.": "在任务 UI 中的相对排序；值越小越靠前。",
    "The owning category that this category is considered nested under.": "此类别被视为嵌套于其下的上级类别。",
    "Signaled when a participant abandons this quest.": "有参与者放弃此任务时触发。",
    "Signaled when this quest completes.": "此任务完成时触发。",
    "Signaled when a participant joins this quest.": "有参与者加入此任务时触发。",
    "Progression model for the quest.": "任务的进度模型。",
    "Rewards granted to eligible participants on completion.": "完成时向符合条件的参与者发放的奖励。",
    "Marks this quest as completed. Fires CompleteEvent. Idempotent — no-op if already completed.":
        "把任务标记为完成并触发 CompleteEvent。幂等：已完成时无操作。",
    "Succeeds if this quest is completed.": "此任务已完成则成功。",
    "Replaces the progression model on a live quest. Auto-completes if the new objective is already completed.":
        "替换进行中任务的进度模型；新目标已完成时自动完成。",
    "Signaled when this objective's progress changes. Payload: this objective.": "此目标的进度变化时触发。载荷：此目标。",
    "Returns a progress message (e.g. \"3 / 10\").": "返回进度消息（如 \"3 / 10\"）。",
    "Determines which participants can contribute to this objective. Override to customize contributor selection. Default: all participants where Info.Contributes = true.":
        "决定哪些参与者可为此目标做贡献。可重写以自定义贡献者选择。默认：Info.Contributes = true 的所有参与者。",
    "Succeeds if this objective is currently complete.": "此目标当前已完成则成功。",
    "Signals ProgressEvent. Call from a subclass to notify progress subscribers.": "发出 ProgressEvent。在子类中调用以通知进度订阅者。",
    "Signaled after this reward has been granted to recipients.": "此奖励发放给接收者之后触发。",
    "Determines which participants should receive this reward. Override to customize recipient selection. Default: all participants where Info.Receives = true.":
        "决定哪些参与者应获得此奖励。可重写以自定义接收者选择。默认：Info.Receives = true 的所有参与者。",
    "Grants this reward to the eligible participants.": "把此奖励发放给符合条件的参与者。",
    "Quantity per participant.": "每个参与者的数量。",
    "Iterates EligibleParticipants, resolves each participant's agent as a player, and grants the entitlement via the platform entitlement service.":
        "遍历 EligibleParticipants，把每个参与者的代理解析为玩家，并通过平台授权服务发放 entitlement。",
    "Current progress toward RequiredCount.": "距 RequiredCount 的当前进度。",
    "Target count for completion.": "完成所需的目标计数。",
    "Returns progress in \"X / Y\" format.": "以 \"X / Y\" 格式返回进度。",
    "Succeeds if Progress >= RequiredCount.": "Progress ≥ RequiredCount 则成功。",
    "Sets current progress. Clamped to [0, RequiredCount].": "设置当前进度；钳制到 [0, RequiredCount]。",
    "Sets the target count. Clamped to [1, MaxFloat].": "设置目标计数；钳制到 [1, MaxFloat]。",
    "The categories this quest is grouped under in the quest UI. Empty = uncategorized.": "此任务在任务 UI 中归属的类别；空 = 未分类。",
    "Items that were newly added to this inventory as a result of the transaction.": "此次事务中新加入此物品栏的物品。",
    "Items whose stack size changed as a result of the transaction, and the previous stack size value.": "此次事务中堆叠数发生变化的物品，及其先前堆叠数。",
    "The inventory which the item was removed from.": "物品被移出的那个物品栏。",
    "Total stack count of items removed as a result of this transaction.": "此次事务中移除物品的堆叠总数。",
    "Items that were removed from this inventory as a result of the transaction.": "此次事务中从此物品栏移除的物品。",
    "Item whose stack size changed as a result of the transaction.": "此次事务中堆叠数发生变化的物品。",
    "Triggered when an item is removed. Fires on this inventory, then propagates up to all ancestor inventories.":
        "物品被移除时触发。先在本物品栏触发，再向上传播到所有祖先物品栏。",
    "Triggered when an item is unequipped. Fires on this inventory, then propagates up to all ancestor inventories.":
        "物品被卸下时触发。先在本物品栏触发，再向上传播到所有祖先物品栏。",
    "Adds the item to this inventory only, ignoring sub-inventories. Fails if no items could be added.":
        "只把物品加入此物品栏本身（忽略子物品栏）；一件都加不进去则失败。",
    "Adds the item to this inventory, including sub-inventories. Fails if no items could be added.":
        "把物品加入此物品栏（含子物品栏）；一件都加不进去则失败。",
    "Returns a list of all sub-inventories within this inventory and its descendant inventories.":
        "返回此物品栏及其后代物品栏中的全部子物品栏。",
    "Returns a list of all items within this inventory and its descendant inventories.":
        "返回此物品栏及其后代物品栏中的全部物品。",
    "Returns a list of all items (of a specific type) within this inventory and its descendant inventories.":
        "返回此物品栏及其后代物品栏中指定类型的全部物品。",
    "Returns a list of sub-inventories of this inventory only.": "仅返回此物品栏自身的子物品栏。",
    "Returns a list of items within this inventory only.": "仅返回此物品栏自身的物品。",
    "Returns a list of items (of a specific type) within this inventory only.": "仅返回此物品栏自身中指定类型的物品。",
    "Removes an item from this inventory or its descendent inventories. Fails if the item could not be removed.":
        "从此物品栏或其后代物品栏移除物品；移除失败则失败。",
    "Broadcast when this item changes inventory.": "此物品更换物品栏时广播。",
    "Removes the item from its inventory and places it in the simulation world. Works on orphaned items i.e. outside the world or any inventory. Fails if the item is already a pickup. The transform of the item will not be altered except to unparent it from any inventory.":
        "把物品从物品栏移出并放入模拟世界。也适用于「孤儿」物品（不在世界或任何物品栏中）。物品已是拾取物则失败。除与物品栏解除父子关系外，不改变物品的变换。",
    "Removes the item from its inventory and places it in the simulation world. Works on orphaned items i.e. outside the world or any inventory. Fails if the item is already in the world. The transform of the dropped item will be set to WorldTransform.":
        "把物品从物品栏移出并放入模拟世界。也适用于孤儿物品。物品已在世界中则失败。被丢弃物品的变换会设为 WorldTransform。",
    "Attempts to equip this item within the inventory it is currently in. Fails if not in an inventory or if equip_item_query_event contains any errors after querying.":
        "尝试在物品当前所在物品栏中装备它；不在物品栏中，或 equip_item_query_event 查询后仍含错误，则失败。",
    "Returns the inventory_component this item currently resides in. Fails if it cannot find a valid parent inventory.":
        "返回此物品当前所在的 inventory_component；找不到有效父物品栏则失败。",
    "Succeeds if this item is considered currently within an inventory and equipped.": "若此物品当前在物品栏中且已装备则成功。",
    "Fails if this item is already in an inventory, or the inventory cannot accept the item.": "物品已在某物品栏中，或该物品栏无法接收此物品，则失败。",
    "Attempts to unequip this item. Fails if not in an inventory, not currently equipped or if unequip_item_query_event contains any errors after querying.":
        "尝试卸下此物品；不在物品栏、未装备，或 unequip_item_query_event 查询后仍含错误，则失败。",
    "Retrieve an integer value or fail if value is not a json number": "取出整数值；value 不是 json 数字则失败。",
    "Retrieve a float value or fail if value is not a json number": "取出浮点值；value 不是 json 数字则失败。",
    "Retrieve an object value or fail if value is not a string": "取出对象值；value 不是字符串则失败。",
    "Retrieve an object value or fail if value is not null": "取出对象值；value 不是 null 则失败。",
    "Used to render a mesh at the location of this entity. A mesh is a set of polygons that can be used to represent shapes in the world such as: foliage and terrain decorations movers (for example, doors and lifts) procedurally created buildings Dependencies: transform_component on the entity positions the mesh.":
        "在实体位置渲染网格。网格是一组多边形，可用于表现世界中的形状：植被与地形装饰、可动件（如门和升降机）、程序化生成的建筑等。依赖：实体上的 transform_component 决定网格位置。",
    "Enable/disable collision on this mesh. If enabled, meshes may collide in the physics simulation.":
        "启用/禁用此网格的碰撞。启用后网格可能在物理模拟中发生碰撞。",
    "Triggered at the beginning of each tick when another entity first overlaps this entity.":
        "每 tick 开始时，当其他实体首次与该实体重叠时触发。",
    "Triggered at the beginning of each tick when another entity is no longer overlapping this entity":
        "每 tick 开始时，当其他实体不再与该实体重叠时触发。",
    "Enable/disable spatial queries against this mesh. Disabling this field will also disable EntityEnteredEvent/EntityExitedEvent.":
        "启用/禁用对此网格的空间查询。禁用后 EntityEnteredEvent/EntityExitedEvent 也会失效。",
    "Enable/disable visibility of this mesh.": "启用/禁用此网格的可见性。",
    "Disables rendering of this mesh.": "禁用此网格的渲染。",
    "Enables rendering of this mesh.": "启用此网格的渲染。",
    "Succeeds if the component is enabled, fails if it's disabled.": "组件处于启用状态则成功，禁用则失败。",
    "Adds the provided components to the entity. If a component is not allowed to be added to this entity it is skipped. Note: When called during the AddedToScene or BeginSimulation phase, it will make sure the added component has achieved the corresponding phase. Components are added following these rules: All components are added to the entity child list. All components have OnAddedToScene called (if this entity is in the scene). All components have OnBeginSimulation called (if this entity is simulating).":
        "把给定的组件添加到实体。若某组件不允许加到该实体则跳过。注意：在 AddedToScene 或 BeginSimulation 阶段调用时，会确保被加组件已达到对应阶段。添加规则：所有组件加入实体子列表；实体在场景中时各组件的 OnAddedToScene 被调用；实体正在模拟时各组件的 OnBeginSimulation 被调用。",
    "Adds the provided entities as children of this entity. If child entity already has a parent, removes the entity from its current parent and adds it to the new one. Added child entities will move through their lifetime methods until they match the state of the new parent.":
        "把给定的实体添加为子实体。若子实体已有父实体，会先从原父实体移除再加入新父。加入的子实体会沿各自的生命周期方法推进，直到与新父实体的状态一致。",
    "Adds a tag instance to this entity. Returns a tag_key that is uniquely associated with the added instance.":
        "向此实体添加一个标签实例，返回与该实例唯一关联的 tag_key。",
    "Fails if at least one type in tag_types cannot be found in this container, succeeds otherwise. Note that this means that if tag_types is empty this call succeeds.":
        "若 tag_types 中有任一类型在容器中找不到则失败，否则成功。注意 tag_types 为空时此调用成功。",
    "Succeeds if at least of the types in tag_types is found in this container, fails otherwise. Note that this means that if tag_types is empty this call fails.":
        "若 tag_types 中至少一个类型在容器中找到则成功，否则失败。注意 tag_types 为空时此调用失败。",
    "Succeeds if at least one tag of type tag_type is found in this container, fails otherwise.":
        "若容器中找到至少一个 tag_type 类型的标签则成功，否则失败。",
    "Succeeds and returns the child component of type component_type if it exists and is accessible from the calling context. Note: When called during the AddedToScene or BeginSimulation phase, it will make sure the returned component has achieved the corresponding phase. Fails if no component of component_type exists or can be accessed.":
        "若 component_type 类型的子组件存在且可访问，则成功并返回它。注意：在 AddedToScene 或 BeginSimulation 阶段调用时，会确保返回的组件已达到对应阶段。不存在或不可访问则失败。",
    "Returns the child components belonging to this entity which are accessible from the calling context.": "返回此实体下属、可从调用方上下文访问的子组件。",
    "Returns the child entities belonging to this entity which are accessible from the calling context. This method only gets the direct entity children. To query multiple levels down the entity structure use the Find* query methods instead.":
        "返回此实体下属、可从调用方上下文访问的子实体。只取直接子实体；跨多层查询请用 Find* 系列。",
    "Returns the parent entity of this entity. The parent entity controls the lifetime of its child entities and components. When an entity is removed from the scene, all its child entities and components will be removed as well. Method fails if there is currently no parent entity.":
        "返回此实体的父实体。父实体掌控其子实体与组件的生命周期——实体从场景移除时其所有子实体和组件也会一并移除。当前没有父实体时此方法失败。",
    "Removes all tag instances of type tag_type, succeeds if at least one instance was removed, fails otherwise.":
        "移除 tag_type 类型的全部标签实例；至少移除一个则成功，否则失败。",
    "Removes all tag instances that are not of type tag_type, succeeds if at least one instance was removed, fails otherwise.":
        "移除不属于 tag_type 类型的全部标签实例；至少移除一个则成功，否则失败。",
    "Removes all tag instances that are not of any of the types in tag_types, succeeds if at least one instance was removed, fails otherwise.":
        "移除不属于 tag_types 中任何类型的全部标签实例；至少移除一个则成功，否则失败。",
    "Removes this entity from its parent. This is used to remove entities from the scene. Components on this entity and its children will run through OnEndSimulation -> OnRemovingFromScene. Entity can be added back later by using NewParent.AddEntities.":
        "把此实体从父实体移除，用于将实体移出场景。该实体及其子级上的组件会依次走 OnEndSimulation → OnRemovingFromScene。之后可用 NewParent.AddEntities 再加回。",
    "Removes the tag instance associated with the tag_key, succeeds if an instance was removed, fails otherwise.":
        "移除与 tag_key 关联的标签实例；移除成功则成功，否则失败。",
    "Send a scene event to this entity and then down the hierarchy. First, SendDown/OnReceive will be invoked on each component on this entity. Next, SendDown will be invoked on each child entity. Consuming the event at any point will halt propagation. Returns true if any participant consumed the event.":
        "向此实体发送场景事件并沿层级向下传播：先在本实体的每个组件上调用 SendDown/OnReceive，再对每个子实体调用 SendDown。任一环节消费该事件即停止传播。有参与者消费则返回 true。",
    "Send a scene event to this entity and then up the hierarchy. First, SendDown/OnReceive will be invoked on each component on this entity. Next, SendUp will be invoked on this entity's parent. Consuming the event at any point will halt propagation. Returns true if any participant consumed the event.":
        "向此实体发送场景事件并沿层级向上传播：先在本实体的每个组件上调用 SendDown/OnReceive，再对父实体调用 SendUp。任一环节消费该事件即停止传播。有参与者消费则返回 true。",
    "Detection has started for this input e.g. a required key is now held down. Note: ActivationTriggeredEvent may also occur this frame, but this event will always be fired first. DetectionBegin and DetectionEnd will always fire, regardless of whether the input is successful or canceled. Tuple payload: 0: the player generating this event 1: the value generated by the physical input":
        "此输入的检测已开始，例如所需按键正被按住。注意：ActivationTriggeredEvent 也可能在本帧发生，但本事件总是先触发。无论输入成功或取消，DetectionBegin 与 DetectionEnd 都会触发。元组载荷：0——玩家；1——物理输入产生的值。",
    "Detection for this input is still being processed. For example, a time threshold may not be met. Tuple payload: 0: the player generating this event 1: the value generated by the physical input 2: elapsed seconds since detection began":
        "此输入的检测仍在进行中——例如时长阈值尚未满足。元组载荷：0——玩家；1——物理输入产生的值；2——检测开始后经过的秒数。",
    "Detection has finished e.g. no required keys are now down. Will always fire as a pair with DetectionBegin. Tuple payload: 0: the player generating this event 1: elapsed seconds since detection began":
        "检测已结束，例如所需按键均已松开。总是与 DetectionBegin 成对触发。元组载荷：0——玩家；1——检测开始后经过的秒数。",
    "Adds Widget to this player_ui using default player_ui_slot configuration options.": "使用默认 player_ui_slot 配置，把 Widget 添加到此 player_ui。",
    "Adds Widget to this player_ui using Slot for configuration options.": "使用 Slot 配置，把 Widget 添加到此 player_ui。",
    "Removes Widget from this player_ui.": "把 Widget 从此 player_ui 移除。",
    "Sets the user's focus on this Widget. The target Widgetmust be focusable, otherwise this has no effect. If SetFocus is called before AddWidget, the widget will be focused after AddWidget is called, unless a SetFocus is called on a different widget by the time AddWidget is called.":
        "把使用者焦点设置到该 Widget。目标 Widget 必须可聚焦，否则无效果。若在 AddWidget 之前调用 SetFocus，则 AddWidget 之后该控件获得焦点——除非在那之前又对别的控件调用了 SetFocus。",
    "Shows or hides the widget without removing itself from the containing player_ui. See widget_visibility for details.": "显示或隐藏该 widget，而不把它从所在 player_ui 中移除。详见 widget_visibility。",
    "Returns the current widget_visibility state.": "返回当前 widget_visibility 状态。",
    "Enables or disables whether the player can interact with this widget.": "启用或禁用玩家与此 widget 的交互。",
    "true if this widget can be modified interactively by the player.": "若此 widget 可被玩家交互修改则返回 true。",
    "Returns the widget's parent widget. Fails if no parent exists, such as if this widget is not in the player_ui or is itself the root widget.":
        "返回该 widget 的父 widget。若它不在 player_ui 中或自身就是根 widget 则失败。",
    "Returns the widget that added this widget to the player_ui. The root widget will return itself. Fails if this widget is not in the player_ui.":
        "返回当初把该 widget 加进 player_ui 的根 widget；根 widget 返回它自己。若该 widget 不在 player_ui 中则失败。",
    "Controls widget input event consumption.": "控制 widget 对输入事件的消费。",
    "The player that triggered the event.": "触发事件的玩家。",
    "The widget that triggered the event.": "触发事件的控件。",
    "Holds the minimum anchors, (left, top). The valid range is between 0.0 and 1.0.": "最小锚点（left, top）；有效范围 0.0~1.0。",
    "Holds the maximum anchors, (right, bottom). The valid range is between 0.0 and 1.0.": "最大锚点（right, bottom）；有效范围 0.0~1.0。",
    "The left edge spacing.": "左边距。",
    "The top edge spacing.": "上边距。",
    "The right edge spacing.": "右边距。",
    "The bottom edge spacing.": "下边距。",
    "Base class for all UI elements drawn on the player's screen.": "绘制在玩家屏幕上的一切 UI 元素的基类。",
    "The child widget of the button. Used only during initialization of the widget and not modified by SetSlot.":
        "按钮的子控件；仅在控件初始化时使用，SetSlot 不会修改它。",
    "The UI input action that will trigger the Click event of this button.": "将触发此按钮 Click 事件的 UI 输入动作。",
    "Subscribable event that fires when the button is clicked.": "按钮被点击时触发的可订阅事件。",
    "Sets the child widget slot.": "设置子控件槽位。",
    "The widget assigned to this slot.": "分配到此槽位的控件。",
    "Horizontal alignment of the widget inside the slot.": "控件在槽位内的水平对齐。",
    "Vertical alignment of the widget inside the slot.": "控件在槽位内的垂直对齐。",
    "Empty distance in pixels that surrounds the widget inside the slot. Assumes 1080p resolution.": "槽位内围绕控件的留白（像素）；按 1080p 分辨率计。",
    "The child widgets of the canvas. Used only during initialization of the widget and not modified by Add/RemoveWidget.":
        "画布的子控件；仅在控件初始化时使用，Add/RemoveWidget 不会修改它。",
    "Adds a new child slot to the canvas.": "向画布添加新的子槽位。",
    "Removes a slot containing the given widget.": "移除包含给定控件的槽位。",
    "The border for the margin and how the widget is resized with its parent. Values are defined between 0.0 and 1.0.": "边距边界及控件随父级缩放的方式；取值 0.0~1.0。",
    "The offset that defined the size and position of the widget. When the anchors are well defined, the Offsets.Left represent the distance in pixels from the Anchors Minimum.X, the Offsets.Bottom represent the distance in pixel from the Anchors Maximum.Y, effectively controlling the desired widget size. When the anchors are not well defined, the Offsets.Left and Offsets.Top represent the widget position and Offsets.Right and Offset.Bottom represent the widget size.":
        "定义控件大小与位置的偏移。锚点完整定义时，Offsets.Left 表示距 Anchors 最小 X 的像素距离、Offsets.Bottom 表示距 Anchors 最大 Y 的像素距离，从而控制期望的控件尺寸；锚点未完整定义时，Offsets.Left/Top 表示控件位置，Offsets.Right/Bottom 表示控件尺寸。",
    "When true we use the widget's desired size. The size calculated by the Offsets is ignored.":
        "为 true 时使用控件期望尺寸，忽略由 Offsets 计算的尺寸。",
    "Alignment is the pivot/origin point of the widget. Starting in the upper left at (0.0,0.0), ending in the lower right at (1.0,1.0).":
        "Alignment 是控件的轴心/原点：左上 (0.0,0.0) 到右下 (1.0,1.0)。",
    "Z Order of this slot relative to other slots in this canvas panel. Higher values are rendered last (and so they will appear to be on top)":
        "此槽位相对画布面板中其他槽位的 Z 序；值越大越后渲染（显示在最上层）。",
    "The color of the widget. Used only during initialization of the widget and not modified by SetColor.":
        "控件颜色；仅在控件初始化时使用，SetColor 不会修改它。",
    "The size this widget desired to be displayed in. Used only during initialization of the widget and not modified by SetDesiredSize.":
        "控件期望的显示尺寸；仅在初始化时使用，SetDesiredSize 不会修改它。",
    "The opacity of the widget. Used only during initialization of the widget and not modified by SetOpacity.":
        "控件不透明度；仅在初始化时使用，SetOpacity 不会修改它。",
    "Gets the widget's color.": "获取控件颜色。",
    "Gets the size this widget desired to be displayed in.": "获取控件期望的显示尺寸。",
    "Gets the widget's opacity.": "获取控件不透明度。",
    "Sets the widget's color.": "设置控件颜色。",
    "Sets the size this widget desired to be displayed in.": "设置控件期望的显示尺寸。",
    "Sets the widgets's opacity.": "设置控件不透明度。",
    "The horizontal tiling option. Used only during initialization of the widget and not modified by SetTiling.":
        "水平平铺选项；仅在初始化时使用，SetTiling 不会修改它。",
    "The image to render. Used only during initialization of the widget and not modified by SetImage.":
        "要渲染的图像；仅在初始化时使用，SetImage 不会修改它。",
    "Tinting applied to the image. Used only during initialization of the widget and not modified by SetTint.":
        "应用于图像的着色；仅在初始化时使用，SetTint 不会修改它。",
    "The vertical tiling option. Used only during initialization of the widget and not modified by SetTiling.":
        "垂直平铺选项；仅在初始化时使用，SetTiling 不会修改它。",
    "Gets the image to render.": "获取要渲染的图像。",
    "Gets the tiling option.": "获取平铺选项。",
    "Gets the tint applied to the image.": "获取图像的着色。",
    "Sets the image to render.": "设置要渲染的图像。",
    "Sets the tiling option when the image is smaller than the allocated size.": "设置图像小于分配空间时的平铺选项。",
    "Sets the tint applied to the image.": "设置图像的着色。",
    "The child widgets of the overlay. Used only during initialization of the widget and not modified by Add/RemoveWidget.":
        "叠层的子控件；仅在初始化时使用，Add/RemoveWidget 不会修改它。",
    "Add a new child slot to the overlay. Slots are added at the end.": "向叠层添加新的子槽位；新槽位加在末尾。",
    "Removes a slot containing the given widget": "移除包含给定控件的槽位",
    "Horizontal alignment of the widget inside the slot. This alignment is only applied after the layout space for the widget slot is created and determines the widget alignment within that space.":
        "控件在槽位内的水平对齐；只有在槽位布局空间创建后才生效，决定控件在该空间内的对齐。",
    "Vertical alignment of the widget inside the slot. This alignment is only applied after the layout space for the widget slot is created and determines the widget alignment within that space.":
        "控件在槽位内的垂直对齐；只有在槽位布局空间创建后才生效，决定控件在该空间内的对齐。",
    "The orientation of the stack box. Either stack widgets horizontal or vertical.": "堆叠容器的方向：水平或垂直排列控件。",
    "The child widgets of the stack box. Used only during initialization of the widget and not modified by Add/RemoveWidget.":
        "堆叠容器的子控件；仅在初始化时使用，Add/RemoveWidget 不会修改它。",
    "Add a new child slot to the stack box. Slots are added at the end.": "向堆叠容器添加新的子槽位；新槽位加在末尾。",
    "The available space will be distributed proportionally. If not set, the slot will use the desired size of the widget.":
        "可用空间将按比例分配；未设置时槽位使用控件期望尺寸。",
    "Whether the text should be automatically wrapped.": "文本是否自动换行。",
    "The justification to display to the user. Used only during initialization of the widget and not modified by SetJustification.":
        "展示给用户的对齐方式；仅在初始化时使用，SetJustification 不会修改它。",
    "The policy that determine what happens when the text is longer than its allowed length. Used only during initialization of the widget and not modified by SetOverflowPolicy.":
        "文本超出允许长度时的处理策略；仅在初始化时使用，SetOverflowPolicy 不会修改它。",
    "The text to display to the user. Used only during initialization of the widget and not modified by SetText.":
        "展示给用户的文本；仅在初始化时使用，SetText 不会修改它。",
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
    "Gets the text currently in the widget.": "获取控件中的当前文本。",
    "Gets the color of the displayed text.": "获取显示文本的颜色。",
    "Gets the opacity of the displayed text.": "获取显示文本的不透明度。",
    "Gets the size of the displayed text.": "获取显示文本的字号。",
    "Sets the text justification in the widget.": "设置控件中的文本对齐方式。",
    "Sets the policy that determine what happens when the text is longer than its allowed length.": "设置文本超长处理策略。",
    "Sets the text displayed in the widget.": "设置控件中显示的文本。",
    "Sets the color of the displayed text.": "设置显示文本的颜色。",
    "Sets the opacity of the displayed text.": "设置显示文本的不透明度。",
    "Sets the size of the displayed text.": "设置显示文本的字号。",
    "widget does not consume any input.": "widget 不消费任何输入。",
    "widget consumes all inputs": "widget 消费所有输入。",
    "The widget is visible and occupies layout space.": "控件可见并占据布局空间。",
    "The widget is invisible and does not occupy layout space.": "控件不可见且不占据布局空间。",
    "The widget is invisible and occupies layout space.": "控件不可见但仍占据布局空间。",
    "Orient widgets from left to right.": "控件从左到右排列。",
    "Orient widgets from top to bottom.": "控件从上到下排列。",
    "Center widget horizontally within the slot.": "控件在槽位内水平居中。",
    "Align widget to the left of the slot.": "控件靠槽位左侧对齐。",
    "Align widget to the right of the slot.": "控件靠槽位右侧对齐。",
    "widget fills the slot horizontally.": "控件水平填满槽位。",
    "Center widget vertically within the slot.": "控件在槽位内垂直居中。",
    "Align widget to the top of the slot.": "控件靠槽位顶部对齐。",
    "Align widget to the bottom of the slot.": "控件靠槽位底部对齐。",
    "widget fills the slot vertically.": "控件垂直填满槽位。",
    "Stretch the image to fit the available space.": "拉伸图像以填满可用空间。",
    "Repeat/Wrap the image to fill the available space.": "重复/平铺图像以填满可用空间。",
    "Evaluates this float curve at the specified time and returns the result as a float": "在指定时间求此浮点曲线的值，返回 float 结果。",
    "Channel will be used to clear specific debug draw.": "该通道将用于清除特定的调试绘制。",
    "Show Debug Draw for the channel for all users.": "为所有用户显示该通道的调试绘制。",
    "Hide Debug Draw for the channel for all users.": "为所有用户隐藏该通道的调试绘制。",
    "Clears all debug draw for the channel.": "清除该通道的所有调试绘制。",
    "Clears all debug draw from this debug_draw instance.": "清除此 debug_draw 实例的所有调试绘制。",
    "Draws a sphere at the named location, and using the provided draw parameters.": "在指定位置按给定绘制参数画一个球体。",
    "Draws a box at the named location, and using the provided draw parameters": "在指定位置按给定绘制参数画一个盒体。",
    "Draws a capsule at the named location, and using the provided draw parameters.": "在指定位置按给定绘制参数画一个胶囊体。",
    "Draws a cone at the named location, and using the provided draw parameters.": "在指定位置按给定绘制参数画一个圆锥。",
    "Draws a cylinder at the named location, and using the provided draw parameters.": "在指定位置按给定绘制参数画一个圆柱。",
    "Draws a line from Start to End locations, and using the provided draw parameters.": "按给定绘制参数从 Start 到 End 画一条线。",
    "Draws a point at the named location, and using the provided draw parameters.": "在指定位置按给定绘制参数画一个点。",
    "Draws an arrow pointing from Start to End locations, and using the provided draw parameters.": "按给定绘制参数画一个由 Start 指向 End 的箭头。",
    "Draws a 3D text using the provided draw parameters.": "按给定绘制参数绘制 3D 文本。",
    "Channel class name will be added as a prefix used when printing the message e.g. '[log_channel]: #Message": "打印消息时会把通道类名作为前缀，例如「[log_channel]: #Message」。",
    "Sets the default log level of the displayed message. See log_level enum for more info on log levels. Defaults to log_level.Normal.":
        "设置显示消息的默认日志级别。级别详情见 log_level 枚举；默认 log_level.Normal。",
    "Print Message using the given log level.": "以给定日志级别打印 Message。",
    "Print Message diagnostic using the given log level.": "以给定日志级别打印 Message 诊断。",
    "Prints the current script call stack using the given log level.": "以给定日志级别打印当前脚本调用栈。",
    "Relative ordering among categories in the quest UI; lower values sort first.": "在任务 UI 中的相对排序；值越小越靠前。",
    "The owning category that this category is considered nested under.": "此类别被视为嵌套于其下的上级类别。",
}
