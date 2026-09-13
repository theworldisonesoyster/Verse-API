# STYLE_GUIDE.md —— 注解风格规范（阶段2执行合同 · v2 官网对齐版）

> 本文件是全库唯一写作标准，阶段2每生成/修改一个页面都必须遵守。v2 依据用户验收反馈重写：**页面结构完全对齐官网**。
> 数据来源三级：`tools/_extracted/`（官网页面结构化 Markdown，写作主素材）→ `sources/`（原始 HTML，存疑时仲裁）→ `manifest.json`（结构/官方标题/分级/URL）。
> 铁律1：**一切 API 事实以快照为准，禁止凭记忆补写。**
> 铁律2：**命名一律用官网正式标题**（manifest 的 `title` 字段，即官网 H1，如 `component class`、`Sleep function`、`Simulation module`）。
> 铁律3：**full 级页面的官网段落与表格必须逐行完整，一行不许省。**

---

## 1. 目录与文件约定

```
verse-api-zh/
├── 00_语言基础/          语言内建类型与表达式（官网无对应页）。章节与页面均不加任何
│                          "补充/镜像"类标注，写法与官网页一致
├── 01_Verse.org/ 02_UnrealEngine.com/ 03_Fortnite.com/   官网三大模块树
│     └── NNN_模块名/      编号=官网出现顺序×10；模块总览页 _overview.md 对应官网模块页
├── 90_分级索引/          S/A/B/C 四级快速索引
├── _Specifiers与Effects.md  公共说明附录（官网每页重复的标准表格统一译一次）
├── _overview.md          每个模块文件夹内的模块总览页（对应官网 "XXX module" 页）
└── 成员页.md             文件名 = 官方 slug 末段（非法字符→_，尾部 _ 去除）
```

- **文件名**用 slug 末段（`print.md`、`print-1.md`、`operatorminus.md`），**显示名/侧栏名/H1 一律用官网正式标题**（含类型后缀）：H1 写 `# component class 🟦`，侧栏条目、SUMMARY、相关链接文字同。
- **模块页表格内成员用裸名**（官网模块页表格即如此：`component`），点入后页面标题才是 `component class`。
- **无链接 data 条目**（官网表格无独立页，如 CollisionProfiles 常量、Input/UI 按键映射）：不建文件，写进父模块 `_overview.md` 的成员表格（裸名＋〔无独立页面〕注记）。
- 官网标注为空的模块（Native、Predicts、Conversations…）：`_overview.md` 写明"官方标注：此模块当前为空"，状态 done，不脑补。

## 2. 分级与详略（分级已在 MANIFEST 定死，不得改判）

| 级别 | 徽标 | depth | 页面构成 |
|---|---|---|---|
| S 核心 | 🟦 | full | 官网全部段落＋完整表格（Description 全译）＋末尾追加 示例/补充说明 |
| A 常用 | 🟩 | full | 同 S |
| B 进阶 | 🟨 | brief | 官网段落结构保留，Description 可摘译压缩；**无追加示例/补充说明**（最多一句提示） |
| C 参考 | `<C>` | oneliner | 标题＋官网描述一句话中译 |

- Devices 模块约定：全部设备类 C 级（一句话索引）；例外：`creative_device`（S）、`creative_device_base`/`creative_object`/`creative_prop`/`creative_object_interface`（A）。
- 模块总览页 `_overview.md` 对应官网模块页：官网有的段落/表格全译（成员表完整），可追加一小段"本模块怎么读"。

## 3. full 页模板（S/A 级）——官网结构在前，追加内容在后

以 `component class` 为例的骨架（**顺序不可调换、段落不可删**）：

```markdown
# component class 🟦【S级·核心】

> Base class for authoring logic and data in the SceneGraph. …
> （官网首段完整英中对照：原文一段、中文翻译一段。官网导语有 N 段就译 N 段，全文完整。）

`using { /Verse.org/SceneGraph }`

## Members
This class has both data members and functions.（官网原文＋中译）

### Data
| Data Member Name | 类型 | 描述 |
|---|---|---|
| Entity | entity | （官网 Description 中译，逐行完整） |
| TickEvents | ?tick_events | … |

### Functions
| Function Name | 描述 |
|---|---|
| OnAddedToScene | … |
| …（官网表的每一行都必须在） |

## Parameters（官网有则保留，全译）
## Enumerators / Exposed Interfaces / Inheritance Hierarchy（官网有则保留，全译）

## Attributes, Specifiers, and Effects
`Sleep<public><native>(Seconds:float)<transacts><suspends><no_rollback>` —— 标签：public / native / transacts / suspends / no_rollback
（语义不逐条复述，链接 [_Specifiers与Effects](_Specifiers与Effects.md)）

────────── 以下为追加内容，必须放在官网内容全部结束之后 ──────────

## 示例
```verse
# 可运行示例，1~2 个
```

## 补充说明
（便于理解的注解：何时用、与谁配合、常见坑。3~8 条，无依据不写。）
```

- 追加内容**不得**插进官网段落之间；官网没有的标题不得出现在官网区域。
- 官网导语里的代码片段/列表/生命周期图示原样保留结构并翻译。
- **表格行数 = 提取件行数**（tools/_extracted/ 对应文件），缺行即错误。

## 4. brief（B 级）与 oneliner（C 级）模板

- brief：同上结构，但 Description 摘译（保留关键句），无 `## 示例`/`## 补充说明`，结尾最多一行"→ 详见官方页"。
- oneliner：`# 官网标题 `<C>`【C级·参考】` ＋ 官网描述一句话中译。正文 ≤10 行。

## 5. 术语表（正文必须统一；代码标识符一律不译）

| 英文 | 中文 | 备注 |
|---|---|---|
| agent | 代理 | 首次出现写「代理（agent）」 |
| player / team / session / round | 玩家 / 队伍 / 对局 / 回合 | |
| device | 设备 | |
| widget | 控件 | |
| entity / component | 实体 / 组件 | |
| prefab | 预制体 | |
| mesh / texture / material | 网格 / 贴图 / 材质 | |
| spawn | 生成 | |
| failable / failure context | 可失败表达式 / 失败上下文 | |
| suspends | 可挂起 | 效果说明符 `<suspends>` 保留原文 |
| listens / listenable | 监听 / listenable（不译） | |
| quest / inventory | 任务 / 物品栏 | |
| HUD | HUD（不译） | |

其余名词：能意译就意译并首现标英文；拿不准就保留英文。

## 6. 翻译与写作规则

1. **代码、类型名、函数名、参数名、报错原文一律不翻译。**
2. 官网导语：英文原文一段＋中文翻译一段，成对出现；表格 Description 直接中译（不保留英文行）。
3. 示例代码注释用中文，代码符合 §7 语法小抄。
4. 语气面向"会一点编程、初次接触 Verse"；用"你"；不堆形容词。
5. 「补充说明」只在有依据时写（官网页面明示、签名可推出、或官方论坛已知行为），不臆造。
6. 相关页面链接（追加区内）2~4 条，链接文字用官网标题。

## 7. Verse 语法小抄（写示例必须遵守）

```verse
# 定义与赋值
X:int := 5          # 定义常量
var Y:int := 0
set Y = 3

# 数组 / 映射 / 选项
Arr:int[] := array{1, 2, 3}
M:[string]int := map{"a" => 1}
Opt:?int := option{7}
if (V := Arr[0], W := Opt?) {}   # 失败上下文：任意一处失败则整块跳过

# 类与效果说明符
MyClass<public> := class<concrete>(BaseClass):
    @editable Slider : editable_number = editable_number{Default := 0.5}

# 异步
Sleep(0.5)                       # 仅 <suspends> 上下文
spawn{ Body() }
Branch().race(Body(), Other())

# 事件
E:event(int) = event(int){}
E.Signal(3)                      # 触发
N := E.Await()                   # <suspends> 等待一次
E.Subscribe(Obj)                 # 持续订阅
```

## 8. 每页自查清单

1. 标题/侧栏名 = manifest `title`（官网 H1）；frontmatter 七字段齐全，grade/depth 与 MANIFEST 一致。
2. 段落顺序与官网提取件一致；官网区域无自创标题。
3. Data/Functions 表逐行完整（行数=提取件），Description 已译。
4. 签名、参数与快照一致；Specifiers 段只列标签行＋附录链接。
5. 追加内容（示例/补充说明）在官网内容之后。
6. 示例符合 §7；代码标识符未翻译。
7. C 级正文 ≤10 行；B 级无追加区。
8. 术语与 §5 一致；status 置 `done`。

## 9. 常见错误（随批次追加）

- **凭旧版记忆写 API**：Sleep 在 /Verse.org/Simulation；fort_character 是 interface（伤害/治疗在 damageable/healable 等接口）；vector3 分量是 Left/Up/Forward。以 _extracted/ 为准。
- **漏表行**：官网 member 表常有 10+ 函数（如 entity、component），漏 GetComponents、RemoveFromEntity 之类即违反铁律3。
- **同名多页**：官网 slug 后缀消歧（print/print-1/print-2），每页各写各的重载，别合并。
- **无链接 data 条目**：并入父模块 _overview 表格，不建文件。
- **空模块**：Native、Predicts、Conversations 等只写 _overview 一段话。
- **给官网内容区加自创标题**（如"这是什么"）：禁止，追加区只能在官网内容结束后。

## 10. 交付流程（阶段2每个批次）

1. 读 `PROGRESS.md` 取下一个未完成模块 → 对照 `MANIFEST.md` 的 grade/depth → 逐页打开 `tools/_extracted/<slug>.md`（结构化官网内容）→ 按 §3/§4 模板成文。
2. 完成后跑 `python tools/build_site.py` → 更新 PROGRESS.md。
3. 抽查反馈不返工原文，追加到 §9。
