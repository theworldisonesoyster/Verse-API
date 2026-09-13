# PROGRESS —— 生成进度

> 状态: ☐ 未开始 / ◐ 部分完成 / ☑ 已生成待审 / ✓✓ 已审核通过。阶段2按模块逐个生成，完成即改状态。
> 总计约 1027 个模块文件夹。00_语言基础（8页）与 90_分级索引 由脚本生成/阶段1完成。


- ☐ 01_Verse.org/010_Verse（约137页）
- ☑ 01_Verse.org/020_Native（空模块）（约1页）
- ☑ 01_Verse.org/030_Chat（8页）
- ☐ 01_Verse.org/040_SceneGraph（约110页）
- ☐ 01_Verse.org/050_Progression（约9页）
- ☑ 01_Verse.org/060_Timeline（4页）
- ☑ 01_Verse.org/070_Presentation（3页）
- ☐ 01_Verse.org/080_Input（约36页）
- ☑ 01_Verse.org/090_AgentGroup（7页）
- ☐ 01_Verse.org/100_Simulation（约20页）
- ☐ 01_Verse.org/110_Assets（约11页）
- ☐ 01_Verse.org/120_Colors（约169页）
- ☐ 01_Verse.org/130_SpatialMath（约42页）
- ☑ 01_Verse.org/140_Random（4页）
- ☑ 01_Verse.org/150_Predicts（空模块）（约1页）
- ☑ 01_Verse.org/160_Concurrency（5页）
- ☐ 02_UnrealEngine.com/010_Conversations（约1页）
- ☐ 02_UnrealEngine.com/020_Progression（约9页）
- ☐ 02_UnrealEngine.com/030_Itemization（约19页）
- ☐ 02_UnrealEngine.com/040_WebAPI（约6页）
- ☐ 02_UnrealEngine.com/050_Temporary（约42页）
- ☐ 02_UnrealEngine.com/060_Social（约2页）
- ☐ 02_UnrealEngine.com/070_JSON（约3页）
- ☐ 02_UnrealEngine.com/080_BasicShapes（约6页）
- ☐ 02_UnrealEngine.com/090_Abilities（约10页）
- ☐ 02_UnrealEngine.com/100_ControlInput（约5页）
- ☐ 02_UnrealEngine.com/110_Assets（约3页）
- ☐ 03_Fortnite.com/010_UI（约48页）
- ☐ 03_Fortnite.com/060_AI（约29页）
- ☐ 03_Fortnite.com/070_Devices（约265页）
- ☐ 03_Fortnite.com/110_Animation（约6页）
- ☐ 03_Fortnite.com/130_Characters（约3页）
- ☐ 03_Fortnite.com/180_Vehicles（约3页）

## v2 改版（2026-09-13，用户验收反馈）

- [x] 全站官网对齐：H1/侧栏用官网正式标题（component class 等）；页面结构=官网段落顺序+完整成员表；追加内容（示例/补充说明）置于官网内容之后
- [x] 主题色 #422439 / 正文背景 #1c1c1c；侧栏树可折叠（默认全展开）；标题 Verse API Reference
- [x] 去除全部〔补充·非官网镜像〕标注；"语言基础（补充）"→"语言基础"
- [x] 新增 tools/extract_page.py（官网页→结构化MD，831页已提取至 tools/_extracted/，阶段2主素材）与《Specifiers 与 Effects 对照》附录
- [x] 样板模块 20 页 + 旗舰页 19 页已按 v2 重写（fort_character 28 函数、component 10 函数等完整表格）

## 阶段2批次记录

- 批次1-2（已完成）：010_Verse 全模块 + Chat/Timeline/Presentation/AgentGroup/Random/Concurrency —— gen_pages.py + content/{verse_pack,small_pack}.py
- 批次3（本轮）：040_SceneGraph 76/91 页（content/scene_pack.py + scene_cells_extra.py）；GitHub 已推送（theworldisonesoyster/Verse-API，main）
- 批次4（下一轮）：完成 SceneGraph 剩余 19 页（_scene_flags.txt 有全部待译单元格原文）→ 050_Progression → 080_Input → 110_Assets → 120_Colors → 130_SpatialMath → 02_UnrealEngine.com → 03_Fortnite.com

 + Native/Predicts/Chat/Timeline/Presentation/AgentGroup/Random/Concurrency —— gen_pages.py + content/{verse_pack,small_pack}.py；正文 198/837
- 下一批次：040_SceneGraph（86页）→ 050_Progression → 080_Input → 110_Assets → 120_Colors → 130_SpatialMath → 02_UnrealEngine.com → 03_Fortnite.com → 010_Verse 外的 Verse.org 顶层页

## 阶段1产出

- [x] 抓取与解析（sources/ + manifest.json）
- [x] STYLE_GUIDE.md / MANIFEST.md / PROGRESS.md / 目录骨架
- [x] 样板模块：01_Verse.org/100_Simulation（20页全注解）
- [x] S级旗舰页 24 页（语言基础8 + Verse核心9 + SceneGraph3 + SpatialMath2 + UI3 + fort_character + creative_device，含 00_语言基础 总览）
- [x] 仓库脚手架（.gitbook.yaml/Intro/README/.nojekyll）与 build_site.py（SUMMARY 859行 + index.html 755KB，浏览器实测过滤/搜索/树/上下页通过）
