# -*- coding: utf-8 -*-
# SceneGraph 组件表内描述的补充对照（known_cells 追加）
EXTRA_CELLS = {
    "Event fires when an interaction has ended before completing successfully. Sends the formerly interacting agent. interactable_component cannot be canceled, this event is provided for subclasses to fire where appropriate.":
        "交互在成功完成前被中断时触发；载荷为此前交互的代理。interactable_component 本身不可取消，此事件供子类在合适时机触发。",
    "Message shown if CanInteract succeeds.": "CanInteract 成功时显示的消息。",
    "Message shown if CanInteract fails.": "CanInteract 失败时显示的消息。",
    "Cooldowns begin elapsing on successful interactions. A cooldown which applies for all attempts to interact on this component.":
        "冷却在成功交互后开始计时；作用于该组件上的所有交互尝试（全局冷却）。",
    "Cooldowns begin elapsing on successful interactions. A cooldown which applies for future attempts to interact on this component by the agent which succeeded.":
        "冷却在成功交互后开始计时；仅作用于成功者的后续交互尝试（按代理冷却）。",
    "An interaction with a duration does not succeed until the duration has elapsed, and success is not guaranteed as it can be canceled while the duration is active.":
        "带时长的交互要等时长走完才算成功；期间可被取消，不保证成功。",
    "The agents which are currently interacting with this interactable.": "当前正在与此可交互物交互的代理。",
    "Event fires when a successful interaction starts. Sends the interacting agent. InteractDuration at or below 0 makes this event identical to InteractSucceededEvent.":
        "成功交互开始时触发；载荷为交互代理。InteractDuration ≤ 0 时本事件与 InteractSucceededEvent 相同。",
    "Event fires when an interaction has completed successfully. Sends the formerly interacting agent. InteractDuration at or below 0 makes this event identical to InteractStartedEvent.":
        "交互成功完成时触发；载荷为此前交互的代理。InteractDuration ≤ 0 时本事件与 InteractStartedEvent 相同。",
    "Success limits prevent new interactions once the component has been successfully interacted with a specified number of times.":
        "成功次数上限：达到指定成功次数后阻止新的交互。",
    "Attempt to cancel an interaction. Fails if the supplied agent is not currently interacting with the component.":
        "尝试取消一次交互；给定代理当前未在交互则失败。",
    "Returns whether the specified agent can interact.": "返回指定代理当前能否交互。",
    "Disable interaction with the component. Disabled components do not provide interaction prompts.":
        "禁用与该组件的交互。禁用后不显示交互提示。",
    "Enable interaction with the component.": "启用与该组件的交互。",
    "Get the remaining cooldown of the interactable for the supplied agent. This returns the duration left in seconds of either the shared or per agent cooldown, whichever is greater. Returns the same value when called multiple times within a transaction.":
        "获取给定代理的剩余冷却：返回共享冷却与按代理冷却中较大者的剩余秒数；同一事务内多次调用返回相同值。",
    "Returns an appropriate message to display to players to communicate the current state of the interactable.":
        "返回适合展示给玩家、说明当前交互状态的消息。",
    "Called from Start if CanInteract pass successfully to start the interaction. Overriding this function will allow you to create a custom interaction behaviour.":
        "当 CanInteract 通过后由 Start 调用以开始交互；重写它可实现自定义交互行为。",
    "Fires the CanceledEvent event.": "触发 CanceledEvent 事件。",
    "Fires the StartedEvent event.": "触发 StartedEvent 事件。",
    "Fires the SucceededEvent event.": "触发 SucceededEvent 事件。",
    "Attempt to start an interaction. Fails if the agent does not pass the CanInteract function.":
        "尝试开始交互；代理未通过 CanInteract 则失败。",
    "Attempt to succeed at an interaction. Success will also happen automatically after InteractDuration has elapsed after starting an interaction. Fails if the supplied agent is not currently interacting with the component.":
        "尝试使交互成功。开始交互后经过 InteractDuration 也会自动成功；给定代理当前未在交互则失败。",
    "Interface for classes that own a camera modifier stack.": "拥有相机修饰符栈的类实现的接口。",
    "Optionally override the far clipping plane distance. If value is Inf then use the default settings":
        "可选覆盖远裁剪面距离；值为 Inf 时使用默认设置。",
    "Optionally override the near clipping plane distance. If value is <= 0.0 then use the default settings":
        "可选覆盖近裁剪面距离；值 ≤ 0.0 时使用默认设置。",
    "Get transition to use when entering this camera mode to transition to the specified camera mode":
        "获取进入此相机模式、过渡到指定相机模式时所用的过渡。",
    "Get transition to use when exiting this camera mode to transition to the destination camera mode":
        "获取退出此相机模式、过渡到目标相机模式时所用的过渡。",
    "Add a camera to the director. The camera with the highest priority will be chosen to be the active camera":
        "把相机加入导演（director）；优先级最高的相机将被选为活动相机。",
    "Render location of the camera. This render location can be modified by camera directions (like camera shakes), without modifying the physical location of any camera entity":
        "相机渲染位置。该位置可被相机指令（如镜头震动）修改，而不改变任何相机实体的物理位置。",
    "Render rotation of the camera. This render rotation can be modified by camera directions (like camera shakes), without modifying the physical location of any camera entity":
        "相机渲染朝向。该朝向可被相机指令（如镜头震动）修改，而不改变任何相机实体的物理位置。",
    "Determines how wide the camera projects in orthographic mode, in centimeters - Used only if projection mode is orthographic":
        "正交模式下相机投影的宽度（厘米）——仅在投影模式为正交时使用。",
    "Physical camera body settings": "物理相机机身设置。",
    "Physical camera lens settings": "物理相机镜头设置。",
    "Projection mode - perspective or orthographic": "投影模式：透视（perspective）或正交（orthographic）。",
    "How much to apply physical camera settings between 0.0 and 1.0": "物理相机设置的生效程度（0.0~1.0）。",
    "Determines how wide the camera projects in orthographic mode, in centimeters": "正交模式下相机投影的宽度（厘米）。",
    "Horizontal field of view in degrees, specified for an aspect ratio of 16:9 /nThis is then to calculate an effective horizontal field of view for the display’s real aspect ratio /nIf for example the screen is an ultrawide (21:9, or 32:9 being common ultrawide aspect ratios) then in practice the actual field of view will be wider. This is known as the Hor+ view scaling method and is generally accepted to be the best solution for ultrawide displays.":
        "水平视场角（度），按 16:9 宽高比指定；再据此计算显示器真实宽高比下的有效水平视场角。例如屏幕是超宽屏（常见的 21:9 或 32:9），实际视场会更宽——即 Hor+ 视野缩放法，通常被认为是超宽屏的最佳方案。",
    "Camera’s body settings. This contains sensor settings, e.g. film or digital camera sensor, shutter speed, etc":
        "相机机身设置：包含传感器设置（胶片或数码传感器）、快门速度等。",
    "Lens of the camera": "相机镜头。",
    "The skeletal_animation that was played": "所播放的骨骼动画。",
    "An easeable interface used to control blending": "用于控制混合的 easeable 接口。",
    "The bounds of the light's visible influence. This clamping of the light's influence is not physically correct but very important for performance, larger lights cost more. The light falloff is based on Inverse Square law. Towards the tail end of the AttenuationRadius, there is an additional smoothing factor to fade out the light contribution to 0 to avoid a hard cutoff.":
        "灯光可见影响范围的边界。这种钳制并不符合物理，但对性能非常重要——灯越大开销越高。光衰减基于平方反比定律；在衰减半径末端有额外的平滑因子把光贡献淡出到 0，避免硬截断。",
    "Set the filter color of the light. This acts as a colored filter in front of the light source. Note that this can change the light's effective intensity. In normalized range 0-1.":
        "设置灯的滤色颜色：相当于放在光源前的彩色滤镜。注意这会改变灯的有效强度。取值范围 0~1（归一化）。",
    "Multiplier on diffuse lighting. Any value besides 1.0 is not physical. 0.0 means no diffuse contribution from this light.":
        "漫反射系数。除 1.0 外的值都不符合物理；0.0 表示此灯无漫反射贡献。",
    "Set the visible light intensity emitted in SI unit Candela. Specified before ColorFilter (which multiplies each color component after the intensity calculation and can change the effective intensity of the light).":
        "以国际单位坎德拉（Candela）设置可见光发光强度。在 ColorFilter 之前指定（滤镜会在强度计算后乘到各颜色分量上，可能改变灯的有效强度）。",
    "Length of the source capsule shape in centimeters along the local Z axis. Note that light shapes which intersect shadow casting geometry can cause shadowing artifacts.":
        "胶囊光源沿局部 Z 轴的长度（厘米）。注意：光源形状若与投射阴影的几何相交，可能产生阴影瑕疵。",
    "Radius of the source capsule shape in centimeters around the local Z axis. Note that light shapes which intersect shadow casting geometry can cause shadowing artifacts.":
        "胶囊光源绕局部 Z 轴的半径（厘米）。注意：光源形状与投射阴影的几何相交可能产生阴影瑕疵。",
    "Multiplier on specular highlights. Can be used to artistically remove highlights mimicking polarizing filters or photo touch up. Any value besides 1.0 is not physical. 0.0 means no specular contribution from this light.":
        "高光系数。可用于艺术化地去除高光（模拟偏振滤镜或修图）。除 1.0 外都不符合物理；0.0 表示此灯无高光贡献。",
    "Disables rendering of this light.": "禁用此灯的渲染。",
    "Enables rendering of this light.": "启用此灯的渲染。",
    "Intensity of the light hitting the surface. In Lux (Lumen per square meter).": "照射到表面的光强度，单位勒克斯（Lux，流明/平方米）。",
    "Angle subtended by light source in degrees (also known as angular diameter). Defaults to 0.5357 which is the angle for our sun.":
        "光源张角（度），亦称角直径。默认 0.5357，即太阳的张角。",
    "The bounds of the light's visible influence, in centimeters. This clamping of the light's influence is not physically correct but very important for performance, larger lights cost more. The light falloff is based on Inverse Square law. Towards the tail end of the AttenuationRadius, there is an additional smoothing factor to fade out the light contribution to 0 to avoid a hard cutoff.":
        "灯光可见影响范围的边界（厘米）。这种钳制不符合物理但对性能很重要——灯越大开销越高。光衰减基于平方反比；衰减半径末端有平滑因子把光贡献淡出到 0，避免硬截断。",
    "The angle of the barn door in degrees attached to the light source rect. Clamped between 0.0 and 90.0 degrees.":
        "矩形光源上挡光板（barn door）的角度（度），钳制在 0.0~90.0。",
    "The length of the barn door attached to the light source rect, in centimeters.": "矩形光源挡光板的长度（厘米）。",
    "The height of the light source rect, in centimeters. Note that light source's shapes which intersect shadow casting geometry can cause shadowing artifacts.":
        "矩形光源的高度（厘米）。注意：光源形状与投射阴影的几何相交可能产生阴影瑕疵。",
    "The width of the light source rect, in centimeters. Note that light source shapes which intersect shadow casting geometry can cause shadowing artifacts.":
        "矩形光源的宽度（厘米）。注意：光源形状与投射阴影的几何相交可能产生阴影瑕疵。",
    "Radius of the source shape, in centimeters. Note that light shapes which intersect shadow casting geometry can cause shadowing artifacts.":
        "光源形状的半径（厘米）。注意：光源形状与投射阴影的几何相交可能产生阴影瑕疵。",
    "The light's inner cone shaped angle in degrees. Clamped between 0.0 and 80.0.": "灯的内锥角（度），钳制在 0.0~80.0。",
    "The light's outer cone shaped angle in degrees. Clamped between 1.0 and 80.0.": "灯的外锥角（度），钳制在 1.0~80.0。",
    "How the owning object should interact with other objects.GetChannelInteraction is a function which maps a collision_channel to a collision_interaction. It can be implemented as an simple sequence of if statements. For example, to block all channels except camera: BlockAllIgnoreCamera(Channel:collision_channel):collision_interaction = if (CollisionChannels.camera[Channel]): return collision_interaction.Ignore return collision_interaction.Block MyProfile:collision_profile = MakeCollisionProfile(CollisionChannels.dynamic, BlockAllIgnoreCamera)":
        "所属对象应如何与其他对象交互。GetChannelInteraction 是把 collision_channel 映射为 collision_interaction 的函数，可用一串 if 实现。例如放行相机通道、阻塞其余：BlockAllIgnoreCamera(Channel:collision_channel):collision_interaction = if (CollisionChannels.camera[Channel]): return collision_interaction.Ignore；return collision_interaction.Block。然后 MyProfile:collision_profile = MakeCollisionProfile(CollisionChannels.dynamic, BlockAllIgnoreCamera)。",
    "If TargetVolume is a polygonal object (mesh, convex hull, etc.) and the contact point is on an edge or vertex, this is the most-opposing face normal of the faces that share that edge or vertex. Otherwise it is the same as HitNormal.":
        "若 TargetVolume 是多边形物体（网格、凸包等）且接触点位于边或顶点上，此值为共享该边/顶点的面中最相对的面法线；否则与 HitNormal 相同。",
    "The collision_profile for this volume.": "此体积的碰撞轮廓。",
    "Base class for collision_volumes that consist of a single volume with a single collision_profile and collision_material for the whole volume. This covers most volume types used in queries and physics, except compound types like a mesh. A query will always return an element rather than a general volume. For example when colliding with a mesh, the element will be a collision_triangle, which is a collision_element and has a single material, rather than a collision_triangle_mesh, which is not an element and has a material palette.":
        "由单一体积构成的碰撞体积基类：整个体积共用单一 collision_profile 与 collision_material。它覆盖查询与物理中使用的大多数体积类型，但不含网格等复合类型。查询总是返回 element 而非一般体积：例如与网格碰撞时，返回的元素是 collision_triangle（属于 collision_element，有单一材质），而不是 collision_triangle_mesh（非 element，带材质调色板）。",
    "The length of the capsule's cylindrical section (distance between the two end cap centers)": "胶囊圆柱段的长度（两个端帽中心之间的距离）。",
    "The radius of the capsule": "胶囊半径。",
    "The radius of the sphere": "球体半径。",
    "The pair will not be detected by Overlap and Sweep queries. The pair will not collide in the physics simulation.":
        "该配对不会被 Overlap/Sweep 查询检测到，也不会在物理模拟中碰撞。",
    "The pair will be detected by Overlap and Sweep queries. The pair will not collide in the physics simulation.":
        "该配对会被 Overlap/Sweep 查询检测到，但不会在物理模拟中碰撞。",
    "The pair will be detected by Overlap and Sweep queries. The pair will collide in the physics simulation.":
        "该配对会被 Overlap/Sweep 查询检测到，并在物理模拟中碰撞。",
    "Controls if the particle_system_component should play the simulation automatically when added to the scene, or when enabled from a disabled state.":
        "控制粒子系统组件是在加入场景时自动播放模拟，还是在从禁用变为启用时播放。",
    "Controls if the particle_system_component should start enabled.": "控制粒子系统组件是否以启用状态开始。",
    "Disables the simulation and rendering of this particle_system.": "禁用此粒子系统的模拟与渲染。",
    "Enables the simulation and rendering of this particle_system.": "启用此粒子系统的模拟与渲染。",
    "Disable the sound component.": "禁用声音组件。",
    "Enable the sound component.": "启用声音组件。",
    "Succeeds if the sound component is enabled, fails if it is disabled.": "声音组件处于启用状态则成功，禁用则失败。",
    "Play the sound asset": "播放音效资产。",
    "Stop the sound asset": "停止音效资产。",
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
    "Which agent is this entity currently possessed by.": "此实体当前被哪个代理附身。",
    "Interface that provides an icon.": "提供图标的接口。",
    "Interface to provide alternative origin to an entity which is defaulted to its parent. See transform_component":
        "为实体提供替代原点的接口（默认原点为其父实体），见 transform_component。",
    "The rarity of this entity. An entity can have only one rarity.": "此实体的稀有度；一个实体只能有一个稀有度。",
    "The maximum amount this component can hold. If unset, it holds an unlimited amount.": "此组件可容纳的最大数量；未设置则不限。",
    "The current amount of this entity held in the stack.": "此实体当前堆叠的数量。",
    "Succeeds if this entity can be merged into the target entity. Merging an entity with itself will always fail. Note that merging should be checked in both directions!":
        "若此实体可合并进目标实体则成功；与自己合并恒失败。注意合并检查应当双向进行！",
    "Attempts to merge this entity into the specified entity. Fails if entities cannot be merged. If TargetAmount is specified, only that amount will try to be merged into this entity. By default, the entire stack will try to merge. If the specified amount is invalid, the merge will fail.":
        "尝试把此实体合并进指定实体；无法合并则失败。指定 TargetAmount 时只合并该数量（默认合并整叠）；数量无效则失败。",
    "Sets the maximum stack size for this component. If NewMaxStackSize is false, stack size is unlimited. If ClampStackSize is true, StackSize will be clamped to NewMaxStackSize.":
        "设置此组件的最大堆叠数。NewMaxStackSize 为 false 表示不限；ClampStackSize 为 true 时会把当前堆叠数钳制到新上限。",
    "Sets the stack size of this component. If the provided stack size is invalid, e.g. negative or exceeding MaxStackSize, stack size will not change.":
        "设置此组件的堆叠数。给定值无效（负数或超过 MaxStackSize）时堆叠数不变。",
    "A component that when attached to an entity allows for it to merge or 'stack' with other entities with compatible components.":
        "挂到实体后，允许其与具有兼容组件的其他实体合并（堆叠）的组件。",
    "The prefab used when this entity merges with another or when it is split into a new instance.":
        "此实体与其他实体合并、或被拆分为新实例时使用的预制体。",
    "Succeeds if this entity can be merged into the target entity. Merging an entity with itself will always fail.":
        "若此实体可合并进目标实体则成功；与自己合并恒失败。",
    "Trigger an ease-out. Triggering an ease-out again when already easing-out, or when fully eased-out has no effect":
        "触发一次缓出（ease-out）；已在缓出或已完全缓出时再次触发无效果。",
    "Trigger an ease-out. If an easing_window is provided here, then it will override any previously provided window. Triggering an ease-out again when already easing-out, or when fully eased-out has no effect":
        "触发一次缓出；若此处提供 easing_window，将覆盖之前提供的窗口。已在缓出或已完全缓出时再次触发无效果。",
    "Entity will be spatially loaded.": "实体会被空间化加载。",
    "Entity will be non-spatially loaded.": "实体会被非空间化加载。",
    "Entity will be always loaded.": "实体总是加载。",
    "Child entities are loaded atomically with their parent.": "子实体随父实体原子化加载。",
    "Child entities are loaded independently from their parent.": "子实体独立于父实体加载。",
    "Every volume has a collision channel as part of its collision_profile. It is used to determine how two volumes interact. See collision_profile.":
        "每个体积都在其 collision_profile 中带有碰撞通道，用于决定两个体积如何交互，见 collision_profile。",
    "Represents a change in the transform relative to the previous keyframe or initial animation position. Translation and Scale are interpreted additively.":
        "表示相对上一个关键帧（或动画初始位置）的变换变化量；Translation 与 Scale 按叠加方式解释。",
    "Duration of this keyframe in seconds.": "此关键帧的时长（秒）。",
    "Easing function to use for playback.": "播放使用的缓动函数。",
    "Gets the duration in seconds this keyframed movement will take. Fails if a fixed duration is not known (ex: looping animations).":
        "获取此关键帧动画将花费的秒数；无固定时长时（如循环动画）失败。",
    "Get the event that fires when the animations ends, failing if the animation is of infinite duration":
        "获取动画结束时触发的事件；动画时长无限则失败。",
    "Signaled when any keyframe is reached. (Keyframe:int, IsReversed:logic).": "到达任一关键帧时触发。载荷：（关键帧序号:int, 是否反向:logic）。",
    "Get the event that fires when the animation is Paused.": "获取动画暂停时触发的事件。",
    "Get the event that fires when the animation begins or resumes Playing.": "获取动画开始或恢复播放时触发的事件。",
    "Get the event that fires when the animation is Stopped.": "获取动画停止时触发的事件。",
    "Is there a valid set of playable keyframes?": "是否存在可播放的有效关键帧集？",
    "Is the animation paused?": "动画是否已暂停？",
    "Is the animation currently playing?": "动画是否正在播放？",
    "Pause movement. Subsequently calling Play() will resume from the point in the animation when it was paused.":
        "暂停运动；之后调用 Play() 会从暂停处继续。",
    "Begin or resume playback.": "开始或恢复播放。",
    "Stop any ongoing animation, sets the animation path and rebases it relative to the actor's current transform. Does not start playing until you call Play().":
        "停止进行中的动画，设置动画路径并以其当前变换为基准重定基；调用 Play() 前不会开始播放。",
    "Stop and reset transform to the initial state. Subsequently calling Play() will begin the animation anew.":
        "停止并把变换重置到初始状态；之后调用 Play() 将从头开始动画。",
}
