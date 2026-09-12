# STYLE_GUIDE.md —— 注解风格规范（阶段2执行合同）

> 本文件是全库唯一写作标准。阶段2每生成/修改一个页面都必须遵守。
> 数据来源：`manifest.json`（结构、分级、URL）＋ `sources/`（官方页面原文快照）。
> 铁律：**一切 API 事实以 `sources/` 快照为准，禁止凭记忆补写**。

---

## 1. 目录与文件约定

```
verse-api-zh/
├── 00_语言基础/          【补充章节】语言内建类型与表达式，官网 API Reference 无对应页，
│                          每页 frontmatter 标 supplement: true，正文标注〔补充·非官网镜像〕
├── 01_Verse.org/         下辖 NNN_模块名/ 文件夹，编号=官网出现顺序×10（10,20,30…留空隙）
├── 02_UnrealEngine.com/
├── 03_Fortnite.com/
├── 90_分级索引/          由 build_site.py 生成：S索引.md / A索引.md / B索引.md / C索引.md
├── _overview.md          每个模块文件夹内的模块总览页（下划线开头，排序置顶）
└── 成员页.md             文件名 = 官方 slug 末段（非法字符→_），显示名写在 frontmatter.name
```

- 文件名一律用 **slug 末段**（含官网消歧后缀 `-1`/`-2`），如 `print.md`、`print-1.md`、`operatorminus.md`；显示名（`Print`、`operator'-'`）写在 frontmatter 与 H1。
- **无链接 data 条目**（官网表格里无独立页，如 CollisionProfiles 常量、Input/UI 按键映射、AI/movement_types）不建文件，写进父模块 `_overview.md` 的成员表格，行内标注〔无独立页面〕。
- 官网标注为空的模块（Native、Predicts、Conversations 等）：只保留 `_overview.md`，正文写明"官方标注：此模块当前为空"，状态 done。

## 2. 分级与详略（分级已在 MANIFEST 定死，不得改判）

| 级别 | 徽标 | 含义 | 详略档位 depth |
|---|---|---|---|
| S 核心 | 🟦 | 几乎每个项目必用 / 迁移价值最高 | `full` 逐成员完整注解 |
| A 常用 | 🟩 | 多数项目会用 | `full` 逐成员完整注解 |
| B 进阶 | 🟨 | 特定场景才用 | `brief` 类级简注＋成员表 |
| C 参考 | ⬜ | 极少用/纯查询 | `oneliner` 一句话 |

- Devices 模块约定：全部设备类 C 级（一句话索引）；**例外**：`creative_device`（S，旗舰页）、`creative_device_base`/`creative_object`/`creative_prop`/`creative_object_interface`（A）——它们是脚本基类与对象操作入口，不属于"设备"。
- 模块总览页 `_overview.md` 一律 `brief`；grade 取该模块最高成员级。

## 3. 页面模板

### 3.1 frontmatter（每页必备，七字段）

```yaml
---
name: event(t)                                        # 官方显示名，原样保留
slug: versedotorg/verse/event/event(t)                # 官网相对路径
url: https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/event/event(t)
kind: class            # class|interface|enum|function|data|module
module: /Verse.org/Verse
grade: S               # S|A|B|C（与 MANIFEST 一致）
depth: full            # full|brief|oneliner
status: done           # placeholder|draft|done|reviewed
---
```

### 3.2 full 模板（S/A 级，类/接口）

```markdown
# event(t) 🟦【S级·核心】

> 官方英文原句（从 sources/ 页面复制第一句描述）。
> 中文翻译。

## 这是什么
2~5 句：作用、什么场合用、和哪些类型配合。面向"会一点编程但不了解 Verse"的读者。

## 签名
```verse
event(t)<public> := class<concrete>:
    # 成员签名逐行照抄 sources/
```

## 最小示例
```verse
# 中文注释说明意图
```

## 常用成员
| 成员 | 签名/形式 | 说明 | 级别 |
|---|---|---|---|

## 何时用 / 何时不用
## 常见坑
## 相关页面
- [player](../20_Simulation/player.md) —— 一句话说明关系
```

- **函数页**把「签名」放最前：```verse 函数名(参数:类型):返回类型``` ＋ effect 说明（如 `<suspends>`），无成员表。
- **枚举页**成员表列出全部枚举值＋一句话。
- **data 页**（常量）一句话＋值的类型说明。

### 3.3 brief 模板（B 级）
`# 名称 🟨【B级·进阶】` → 官方原句＋翻译 → 「这是什么」1~3 句 → 签名 → 成员表（可不带示例）。

### 3.4 oneliner 模板（C 级）
`# 名称 ⬜【C级·参考】` → 官方原句＋中文一句话。**正文（除 frontmatter/H1）不超过 10 行。**

## 4. 术语表（正文必须统一；代码标识符一律不译）

| 英文 | 中文 | 备注 |
|---|---|---|
| agent | 代理 | 玩家的抽象，首次出现写「代理（agent）」 |
| player | 玩家 | |
| team | 队伍 | |
| session | 对局 | |
| round | 回合 | |
| device | 设备 | |
| widget | 控件 | |
| entity / component | 实体 / 组件 | SceneGraph |
| prefab | 预制体 | |
| mesh / texture / material | 网格 / 贴图 / 材质 | |
| spawn | 生成 | |
| failable / failure context | 可失败表达式 / 失败上下文 | |
| suspends | 可挂起 | 效果说明符 `<suspends>` 保留原文 |
| listens / listenable | 监听 / listenable（不译） | |
| quest | 任务 | |
| inventory | 物品栏 | |
| HUD | HUD | 不译 |

其余名词：能意译就意译并首现标英文；拿不准就保留英文原文。

## 5. 翻译与写作规则

1. **代码、类型名、函数名、参数名、报错信息原文一律不翻译。**
2. 每页保留官方描述首句英文原文（`>` 引用块），紧跟中文翻译；官方无描述时按页面内容自写，不加原文块。
3. 示例代码注释用中文；代码本身符合 §6 语法小抄。
4. 语气：面向"会一点编程、初次接触 Verse"的读者；少用"您"，用"你"；不堆形容词。
5. 「常见坑」只在确有依据时写（官方页明示、或语义从签名可推出），不臆造。
6. 相关页面用相对链接，2~4 条即可。

## 6. Verse 语法小抄（写示例必须遵守）

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
    @editable Slider : editable_number = editable_number{}   # 设备详情面板可调参数
    Handle<local_scope>:cancelable = event{}                 # 示意

# 异步
Sleep(0.5)                       # 仅 <suspends> 上下文可用
spawn{ Body() }                  # 新协程
Branch().race(Body(), Other())   # 并发与竞速

# 事件
E:event(signal_types) := event{}
E.Signal(A)                      # 触发
E.Await()                        # <suspends> 等待一次
E.Subscribe(Obj)                 # 持续订阅（类成员函数处理）

# for / loop
for (I := 0 .. 9, Item := Arr[I]) {}
loop:
    if (Done?) { break }
```

## 7. 每页自查清单（完成后逐项过）

1. frontmatter 七字段齐全，grade/depth 与 MANIFEST.md 一致。
2. 签名、成员、参数与 `sources/<slug>.html` 一致（对照原文，不是凭印象）。
3. 官方原句引用与原文相同；无描述页不硬造原文块。
4. 示例符合 §6；代码标识符未翻译。
5. 相关链接相对路径有效（相对本文件位置）。
6. C 级正文 ≤10 行；B 级无成员表时不超过 30 行。
7. 术语与 §4 一致。
8. status 置为 `done`。

## 8. 常见错误（阶段2随时追加到此处）

- **凭旧版本记忆写 API**：Sleep 在 `/Verse.org/Simulation`（不在 Verse 核心模块）；`fort_character` 是 interface 不是 class；SceneGraph 实体模型已升入 `/Verse.org`。一切以 sources/ 快照为准。
- **同名多页**：官网用 slug 后缀消歧（`print`/`print-1`/`print-2`），每页各写各的重载，文件名用 slug，别合并。
- **无链接 data 条目**：写进父模块 `_overview.md` 表格，不建文件、不进分级索引。
- **空模块**：Native、Predicts、Conversations、Temporary/SpatialMath、Fortnite.com/Input(部分) 官方标注为空或无内容页——只写 `_overview.md` 一段话，不要脑补成员。

## 9. 交付流程（阶段2每个批次）

1. 读 `PROGRESS.md` 取下一个未完成模块 → 读 `STYLE_GUIDE.md`（本文件）→ 按 MANIFEST 的 grade/depth 逐页生成。
2. 完成后跑 `python tools/build_site.py`（重建 SUMMARY/index.html）→ 更新 PROGRESS.md 状态。
3. 抽查反馈不返工原文，追加到 §8。
