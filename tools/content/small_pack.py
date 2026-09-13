# -*- coding: utf-8 -*-
# Verse.org 小模块批次：Chat / Timeline / Presentation / AgentGroup / Concurrency / Random
PACKS = [
    {
        "outdir": "01_Verse.org/030_Chat", "module_slug": "versedotorg/chat",
        "overview_title": "Chat module", "overview_grade": "B",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/chat",
        "overview": {"zh": "语音/文本聊天频道管理：创建频道、指定成员权限、处理加/退频道错误。"},
        "entries": {
            "versedotorg/chat/chat_channel/chat_channel(member_info)": {"zh": "文本聊天频道：以 member_info 参数化的频道类。"},
            "versedotorg/chat/voice_channel/voice_channel(member_info)": {"zh": "语音频道：定义一组可通过语音交流的代理（agent）。一个代理可同时属于多个语音频道；频道最多容纳 80 名成员，超出者不被纳入聊天。频道参与者也可能因家长控制或用户设置而被限制语音。"},
            "versedotorg/chat/add_channel_error": {"zh": "通过 AddChatChannel 添加频道失败时返回的错误。"},
            "versedotorg/chat/remove_channel_error": {"zh": "通过 RemoveChatChannel 移除频道失败时返回的错误。"},
            "versedotorg/chat/has_voice_member_info": {"zh": "用于为 voice_channel 指定权限等设置的接口（如是否可发言）。"},
            "versedotorg/chat/chat_channel": {"zh": "参数化构造：按 member_info 类型创建文本聊天频道。"},
            "versedotorg/chat/voice_channel": {"zh": "参数化构造：创建语音频道。语音频道定义一组可通过语音交流的代理；一个代理可同时属于多个频道，频道最多容纳 80 名成员，参与者也可能因家长控制/用户设置被限制语音。"},
        },
    },
    {
        "outdir": "01_Verse.org/060_Timeline", "module_slug": "versedotorg/timeline",
        "overview_title": "Timeline module", "overview_grade": "B",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/timeline",
        "overview": {"zh": "时间线元素：把「时间点」或「时间区间」加入时间轴，驱动按时间发生的玩法。"},
        "entries": {
            "versedotorg/timeline/timeline_element": {"zh": "可加入时间线的元素的抽象定义，见 timeline_element_point 与 timeline_element_span。"},
            "versedotorg/timeline/timeline_element_point": {"zh": "占据单个时间点的时间线元素。"},
            "versedotorg/timeline/timeline_element_span": {"zh": "跨越一段时间范围的时间线元素。"},
        },
    },
    {
        "outdir": "01_Verse.org/070_Presentation", "module_slug": "versedotorg/presentation",
        "overview_title": "Presentation module", "overview_grade": "C",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/presentation",
        "overview": {"zh": "实体展示信息：为实体提供名称/描述等呈现细节。"},
        "entries": {
            "versedotorg/presentation/description_component": {"zh": "保存实体呈现细节（如名称与描述）的组件。"},
            "versedotorg/presentation/has_description": {"zh": "提供描述性名称或文本的接口。"},
        },
    },
    {
        "outdir": "01_Verse.org/090_AgentGroup", "module_slug": "versedotorg/agentgroup",
        "overview_title": "AgentGroup module", "overview_grade": "B",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/agentgroup",
        "overview": {"zh": "代理组：把一组代理（agent）组织为共享同一所有权的分组，常用于聊天/语音频道成员管理。"},
        "entries": {
            "versedotorg/agentgroup/agent_group/agent_group(member_info)": {"zh": "代理组类：共享同一所有权的代理集合，存储代理与成员信息。"},
            "versedotorg/agentgroup/add_member_error": {"zh": "agent_group.AddMember 返回的所有错误的基类。"},
            "versedotorg/agentgroup/remove_member_error": {"zh": "agent_group.RemoveMember 返回的所有错误的基类。"},
            "versedotorg/agentgroup/member_info_interface": {"zh": "定义「可作为代理组成员信息」的接口。"},
            "versedotorg/agentgroup/agent_group_interface": {"zh": "定义「提供代理组」能力的接口。"},
            "versedotorg/agentgroup/agent_group": {"zh": "参数化构造：创建代理组。代理组是共享同一所有权的代理集合。"},
        },
    },
    {
        "outdir": "01_Verse.org/160_Concurrency", "module_slug": "versedotorg/concurrency",
        "overview_title": "Concurrency module", "overview_grade": "A",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/concurrency",
        "overview": {"zh": "异步并发支持：task 表示已启动的异步任务，awaitable 定义「可等待」能力。"},
        "entries": {
            "versedotorg/concurrency/task/task(t)": {"zh": "表示一个已启动的异步任务（spawn 的产物），可查询/控制其执行。"},
            "versedotorg/concurrency/task": {"zh": "参数化构造：按返回值类型 t 创建 task 类型。"},
            "versedotorg/concurrency/awaitable": {"zh": "带载荷、可被等待（Await）的事件实现的参数化接口；与 signalable 配对。"},
            "versedotorg/concurrency/awaitable-1": {"zh": "awaitable 的无参数构造重载。"},
        },
    },
    {
        "outdir": "01_Verse.org/140_Random", "module_slug": "versedotorg/random",
        "overview_title": "Random module", "overview_grade": "S",
        "overview_url": "https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/random",
        "overview": {"zh": "密码学安全的均匀随机数：随机整数/浮点与数组洗牌。"},
        "entries": {
            "versedotorg/random/getrandomfloat": {"zh": "返回 Low 与 High 之间（含两端）均匀分布、密码学安全的随机 float。",
                "example": "F := GetRandomFloat(0.0, 1.0)"},
            "versedotorg/random/getrandomint": {"zh": "返回 Low 与 High 之间（含两端）均匀分布、密码学安全的随机 int。",
                "example": "N := GetRandomInt(1, 6)   # 掷骰子"},
            "versedotorg/random/shuffle": {"zh": "返回一个与 Input 元素相同、但顺序已随机打乱的新数组。",
                "example": "Deck := Shuffle(array{1, 2, 3, 4, 5})"},
        },
    },
]
