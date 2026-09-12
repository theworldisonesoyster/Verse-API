# -*- coding: utf-8 -*-
"""
gen_skeleton.py — 应用分级并生成:
  1. manifest.json 内写回 grade/depth
  2. 目录树骨架 + 全部占位 .md（status: placeholder）
  3. MANIFEST.md（全量清单，阶段2对照执行）
  4. PROGRESS.md（模块级进度表）
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grades import grade_of, DEPTH, GRADE_ORDER  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BADGE = {"S": "🟦【S级·核心】", "A": "🟩【A级·常用】", "B": "🟨【B级·进阶】", "C": "⬜【C级·参考】"}
TOPDIR = {"versedotorg": "01_Verse.org", "unrealenginedotcom": "02_UnrealEngine.com",
          "fortnitedotcom": "03_Fortnite.com"}

# 00_语言基础 补充章节（官网API Reference无对应页）
SUPPLEMENTS = [
    ("array——数组", "S"), ("map——映射", "S"), ("option——可选值", "S"),
    ("可失败表达式与failure", "S"), ("string——字符串", "A"), ("数值类型 int/float/rational", "A"),
    ("logic与void", "B"), ("元组与子类型", "B"),
]


def sanitize(seg: str) -> str:
    return re.sub(r"[^a-z0-9_-]+", "_", seg.lower()).strip("_") or "page"


def folder_of(node, parent_dir, order):
    return os.path.join(parent_dir, f"{order*10:03d}_{node['name'].replace('.', '')}")


def walk(node, parent_dir, order, rows):
    """为 module 节点建文件夹与 _overview.md，返回 (dir, 文件数)"""
    node["grade"] = grade_of(node["slug"], node["name"], "module")
    node["depth"] = "brief"
    dirp = folder_of(node, parent_dir, order)
    os.makedirs(dirp, exist_ok=True)
    n_files = 0
    rel = os.path.relpath(dirp, ROOT).replace("\\", "/")

    members = [c for c in node.get("children", []) if c["kind"] != "module" and not c.get("out_of_scope")]
    subs = [c for c in node.get("children", []) if c["kind"] == "module" and not c.get("out_of_scope")]
    unlinked = [m for m in members if not m.get("linked", True)]
    linked = [m for m in members if m.get("linked", True)]

    if not node.get("empty"):
        for m in linked + unlinked:
            m["grade"] = grade_of(m["slug"], m["name"], m["kind"])
            m["depth"] = DEPTH[m["grade"]]
        for m in linked:
            fn = sanitize(m["slug"].rsplit("/", 1)[-1]) + ".md"
            fp = os.path.join(dirp, fn)
            if not os.path.exists(fp):
                with open(fp, "w", encoding="utf-8") as f:
                    f.write(frontmatter(m, rel) + f"\n# {m['name']} {BADGE[m['grade']]}\n\n"
                            f"<!-- 待生成（阶段2）。官方快照: sources/{m['slug']}.html -->\n")
            m["_file"] = f"{rel}/{fn}"
            n_files += 1
        rows.append((rel, node, len(linked), len(unlinked), len(subs)))

    ov = os.path.join(dirp, "_overview.md")
    if not os.path.exists(ov):
        with open(ov, "w", encoding="utf-8") as f:
            f.write(frontmatter(node, rel) + f"\n# {node['name']} {BADGE[node['grade']]}\n\n"
                    f"<!-- 模块总览，待生成（阶段2）"
                    + (f"；官方标注此模块为空" if node.get("empty") else "")
                    + f" -->\n")
    n_files += 1
    for s in subs:
        n_files += walk(s, dirp, s["order"], rows)
    return n_files


def frontmatter(n, rel):
    mod_path = "/" + n["slug"].replace("/", ".", 1).replace("/", "/") if n.get("slug") else ""
    module_field = ("/" + n["slug"].split("/", 1)[0].replace("versedotorg", "Verse.org")
                    .replace("unrealenginedotcom", "UnrealEngine.com")
                    .replace("fortnitedotcom", "Fortnite.com")) if n.get("slug") else ""
    lines = ["---",
             f"name: {n['name']}",
             f"slug: {n.get('slug', '')}",
             f"url: {n.get('url') or ''}",
             f"kind: {n['kind']}",
             f"module: {module_field}",
             f"grade: {n.get('grade', 'C')}",
             f"depth: {n.get('depth', 'brief')}",
             "status: placeholder",
             "---"]
    return "\n".join(lines) + "\n"


def main():
    forest = json.load(open(os.path.join(ROOT, "manifest.json"), encoding="utf-8"))
    rows = []
    total = 0
    for i, top in enumerate(forest, 1):
        dirp = os.path.join(ROOT, TOPDIR[top["slug"]])
        os.makedirs(dirp, exist_ok=True)
        for s in top.get("children", []):
            if s.get("out_of_scope"):
                continue
            total += walk(s, dirp, s["order"], rows) if s["kind"] == "module" else 0
        # 顶层 _overview.md
        ov = os.path.join(dirp, "_overview.md")
        top["grade"] = grade_of(top["slug"], top["name"], "module")
        if not os.path.exists(ov):
            open(ov, "w", encoding="utf-8").write(
                frontmatter(top, TOPDIR[top["slug"]]) + f"\n# {top['name']} {BADGE[top['grade']]}\n\n<!-- 待生成 -->\n")

    # 00_语言基础
    base = os.path.join(ROOT, "00_语言基础")
    os.makedirs(base, exist_ok=True)
    if not os.path.exists(os.path.join(base, "_overview.md")):
        open(os.path.join(base, "_overview.md"), "w", encoding="utf-8").write(
            "---\nname: 语言基础\nslug: (补充章节)\nurl: \nkind: module\nmodule: /补充\ngrade: S\ndepth: brief\n"
            "status: placeholder\n---\n\n# 语言基础〔补充·非官网镜像〕\n\n<!-- 待生成 -->\n")
    for nm, g in SUPPLEMENTS:
        fp = os.path.join(base, sanitize(nm.split("——")[0].split("/")[0]) + ".md")
        if not os.path.exists(fp):
            open(fp, "w", encoding="utf-8").write(
                f"---\nname: {nm}\nslug: (补充)\nurl: \nkind: class\nmodule: /语言基础\ngrade: {g}\n"
                f"depth: {DEPTH[g]}\nstatus: placeholder\nsupplement: true\n---\n\n"
                f"# {nm} {BADGE[g]}〔补充·非官网镜像〕\n\n<!-- 待生成 -->\n")

    json.dump(forest, open(os.path.join(ROOT, "manifest.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    # ---- MANIFEST.md ----
    stats = {g: 0 for g in GRADE_ORDER}
    lines = ["# MANIFEST —— 全量页面清单与分级",
             "",
             "> 阶段2按此执行：grade/depth 不得改判；status 从占位页 frontmatter 读取。",
             "> 〔无独立页面〕= 官网无独立页，内容并入父模块 _overview.md；Devices 设备类按约定 C 级索引。",
             "",
             "| 页面 | 名称 | 类型 | 级别 | 详略 | 官网 |",
             "|---|---|---|---|---|---|"]

    def add_rows(dir_rel, node):
        for c in node.get("children", []):
            if c.get("out_of_scope"):
                continue
            if c["kind"] == "module":
                add_rows(c["_dir_rel"], c)
                continue
            if not c.get("linked", True):
                lines.append(f"| {dir_rel}/_overview.md | {c['name']} 〔无独立页面〕 | {c['kind']} "
                             f"| {c['grade']} | oneliner(并入总览) | - |")
                continue
            stats[c["grade"]] += 1
            lines.append(f"| {c.get('_file','')} | {c['name']} | {c['kind']} | {c['grade']} | {c['depth']} "
                         f"| [官网]({c['url']}) |")

    def set_dir(node, rel):
        node["_dir_rel"] = rel
        for c in node.get("children", []):
            if c["kind"] == "module" and not c.get("out_of_scope"):
                set_dir(c, f"{TOPDIR[node['slug']].split('_')[0] if False else rel}/{c['order']*10:03d}_{c['name'].replace('.','')}")

    for top in forest:
        set_dir(top, TOPDIR[top["slug"]])
        add_rows(TOPDIR[top["slug"]], top)

    total_pages = sum(stats.values())
    lines.insert(4, f"> 成员页合计 **{total_pages}**：S={stats['S']}，A={stats['A']}，B={stats['B']}，C={stats['C']}"
                    f"（另有 00_语言基础 补充 8 页、模块总览页约 50 页）")
    open(os.path.join(ROOT, "MANIFEST.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

    # ---- PROGRESS.md ----
    pl = ["# PROGRESS —— 生成进度", "",
          "> 状态: ☐ 未开始 / ◐ 部分完成 / ☑ 已生成待审 / ✓✓ 已审核通过。阶段2完成一个模块就把 ☐ 改 ☑。", ""]
    grand = 0
    for top in forest:
        mods = [c for c in top.get("children", []) if not c.get("out_of_scope")]

        def count(n):
            k = 1
            for c in n.get("children", []):
                if c["kind"] == "module" and not c.get("out_of_scope"):
                    k += count(c)
                else:
                    k += 1
            return k
        for m in mods:
            c = count(m)
            grand += c
            pl.append(f"- ☐ {TOPDIR[top['slug']]}/{m['order']*10:03d}_{m['name'].replace('.','')}（约{c}页）")
    pl.insert(3, f"> 总计约 {grand} 个模块文件夹。00_语言基础（8页）与 90_分级索引 由脚本生成/阶段1完成。")
    pl.insert(4, "")
    pl += ["", "## 阶段1产出", "",
           "- [x] 抓取与解析（sources/ + manifest.json）",
           "- [x] STYLE_GUIDE.md / MANIFEST.md / PROGRESS.md / 目录骨架",
           "- [ ] 样板模块：01_Verse.org/100_Simulation",
           "- [ ] S级旗舰页（见 MANIFEST 中 S 级核心条目）",
           "- [ ] 仓库脚手架（.gitbook.yaml/Intro/README/.nojekyll）与 build_site.py"]
    open(os.path.join(ROOT, "PROGRESS.md"), "w", encoding="utf-8").write("\n".join(pl) + "\n")

    print(f"skeleton done: member pages={total_pages}, grades={stats}, module folders listed={grand}")


if __name__ == "__main__":
    main()
