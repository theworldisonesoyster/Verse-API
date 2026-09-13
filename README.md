# Verse API Reference (verse-api-zh)

基于 [Epic 官方 Verse API Reference](https://dev.epicgames.com/documentation/fortnite/verse-api)（快照 42.10 / 2026-09-13）生成。

## 仓库结构

```
Intro.md            GitBook 首页（基于官方 Verse API 生成说明）
SUMMARY.md          GitBook 侧边栏（脚本生成的完整层级）
00_语言基础/         补充章节（语言内建类型，官网无对应页，已标注）
01_Verse.org/       全部 16 个子模块
02_UnrealEngine.com/ 全部 11 个子模块
03_Fortnite.com/    精选 5 模块 + Devices 纯索引
90_分级索引/         S/A/B/C 四级快速索引
MANIFEST.md         全量页面清单与分级（阶段执行合同）
STYLE_GUIDE.md      写作规范（模板/术语表/自查清单）
PROGRESS.md         生成进度
sources/            官方页面本地快照（1032 个 HTML）
tools/              抓取/解析/骨架/建站脚本（Python 3.13，无第三方依赖）
```

## 脚本用法

```bash
python tools/fetch_pages.py modules   # 抓取模块页（增量）
python tools/fetch_pages.py pending   # 抓取 manifest 中缺失的成员页
python tools/parse_modules.py         # 模块页 → manifest.json
python tools/gen_skeleton.py          # 应用分级，生成骨架/占位页
python tools/build_site.py            # 生成 SUMMARY.md 与 index.html
```
