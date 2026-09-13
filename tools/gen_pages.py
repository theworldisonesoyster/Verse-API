# -*- coding: utf-8 -*-
"""
gen_pages.py — 从 tools/_extracted/ 结构化官网内容 + 内容包（中文对照）批量生成页面
用法: python tools/gen_pages.py tools/content/<pack>.py
内容包格式 (python):
PACK = {
  "outdir": "01_Verse.org/010_Verse",          # 默认输出目录
  "overview": {"zh": "模块中文导语"},
  "entries": {
    "<完整slug>": {"zh": "中文一句话(导语翻译或页面说明)",
                   "example": "verse 代码(可选,仅full页)",
                   "notes": "补充说明(可选)"},
  },
}
规则见 STYLE_GUIDE §3：full/brief 复制官网段落（公共样板句自动译），oneliner 只写一句话；
发现未翻译的英文表格内容则跳过并报告（转手写）。
"""
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXT = os.path.join(ROOT, "tools", "_extracted")
BADGE = {"S": "S", "A": "A", "B": "B", "C": "C"}
KIND_DIR = {}  # 未用

BOILER = [
    (re.compile(r"^This function is a parametric type, meaning it returns a class or interface rather than a value or object instance\.$"),
     "此函数是参数化类型：它返回的是类或接口，而不是值或对象实例。"),
    (re.compile(r"^(.+?) returns the parametric class (.+)\.$"), r"\1 返回参数化类 \2。"),
    (re.compile(r"^(.+?) returns the parametric interface (.+)\.$"), r"\1 返回参数化接口 \2。"),
    (re.compile(r"^(This class|This interface|This struct) has no members\.$"), "没有成员。"),
    (re.compile(r"^(This class|This interface|This struct) has both data members and functions\.$"), "兼有数据成员和函数。"),
    (re.compile(r"^(This class|This interface|This struct) has functions, but no data members\.$"), "只有函数，没有数据成员。"),
    (re.compile(r"^(This class|This interface|This struct) has data members, but no functions\.$"), "只有数据成员，没有函数。"),
    (re.compile(r"^Module import path: (.+)$"), r"模块导入路径：\1"),
    (re.compile(r"^(.+?) takes the following parameters:?$"), r"\1 接受以下参数："),
    (re.compile(r"^(.+?) does not take any parameters\.$"), r"\1 不接受任何参数。"),
]
MEMBERS_HEAD = re.compile(r"^This (class|interface|struct) has")


def load_pack(path):
    spec = importlib.util.spec_from_file_location("pack", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.PACK


def parse_extract(slug):
    p = os.path.join(EXT, *slug.split("/")) + ".md"
    if not os.path.exists(p):
        return None
    lines = open(p, encoding="utf-8").read().splitlines()
    using, lead, sig_lines, sections = None, [], [], []
    cur = None
    seen_using_tbl = False
    for ln in lines:
        m = re.match(r"^\| Verse using statement \| (.*) \|\s*$", ln)
        if m:
            using = m.group(1).strip()
            seen_using_tbl = True
            continue
        if not seen_using_tbl and not ln.startswith("## "):
            if ln.strip() and not ln.startswith("|"):
                lead.append(ln.strip())
            continue
        if ln.startswith("## "):
            cur = ln[3:].strip()
            sections.append((cur, []))
            continue
        if seen_using_tbl:
            if ln.strip() == "|  |  |":
                continue
            if cur is None:
                if ln.strip():
                    sig_lines.append(ln.strip())
            else:
                sections[-1][1].append(ln)
    return {"lead": "\n".join(lead).strip(), "using": using,
            "sig": [x for x in sig_lines if not x.startswith("_（")],
            "spec_note": next((x for x in sig_lines if x.startswith("_（")), None),
            "sections": sections}


def translate_section(title, body):
    """返回 (ok, new_title, new_lines)；发现未翻译英文返回 ok=False"""
    out = []
    for ln in body:
        if ln.startswith("_（"):
            out.append(ln)
            continue
        if ln.startswith("### "):
            out.append(ln)  # 官网子标题（如 Generated Interface）
            continue
        if ln.startswith("```"):
            out.append(ln)
            continue
        done = False
        for pat, rep in BOILER:
            if pat.match(ln):
                out.append(pat.sub(rep, ln))
                done = True
                break
        if done:
            continue
        if ln.startswith("|"):
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if cells and cells[0] in ("Name", "Data Member Name", "Function Name", "Specifier", "Effect", "Enumerator"):
                out.append(ln)  # 表头（官网保留英文列名）
                continue
            if cells:
                last = cells[-1]  # 最后一列 = Description
                if last and re.search(r"[A-Za-z]{3}", last):
                    return False, title, body  # 描述列仍是英文 → 转手写
            out.append(ln)
            continue
        if ln.strip():
            return False, title, body  # 普通英文句子 → 转手写
        out.append(ln)
    return True, title, out


def rel_spec(page_path):
    return os.path.relpath(os.path.join(ROOT, "_Specifiers与Effects.md"),
                           os.path.join(ROOT, os.path.dirname(page_path))).replace("\\", "/")


def emit_page(member, pack_entry, extract, outdir):
    title = member.get("title") or member["name"]
    g = member["grade"]
    depth = member["depth"]
    zh = pack_entry["zh"].strip()
    rel = os.path.join(ROOT, outdir)
    os.makedirs(rel, exist_ok=True)
    fname = re.sub(r"[^a-z0-9_-]+", "_", member["slug"].rsplit("/", 1)[-1]).strip("_") + ".md"
    page_rel = f"{outdir}/{fname}"
    L = [f"# {title} <{G_BADGE[g]}>", ""]
    if depth == "oneliner":
        L += [zh, ""]
    else:
        if extract["lead"]:
            for seg in extract["lead"].split("\n"):
                L.append("> " + seg)
            for seg in zh.split("\n"):
                L.append("> " + seg)
        else:
            L.append(zh)
        L.append("")
        if extract["using"]:
            L += [f"`{extract['using']}`", ""]
        for s in extract["sig"]:
            if MEMBERS_HEAD.match(s):
                L += [s, ""]
            else:
                L += ["```verse", s, "```", ""]
        for title_s, body in extract["sections"]:
            ok, t2, body2 = translate_section(title_s, body)
            if not ok:
                return None, page_rel, f"EN content in section {title_s}"
            L += [f"## {t2}", ""]
            L += [x for x in body2]
            L.append("")
        if depth == "full":
            if pack_entry.get("example"):
                L += ["## 示例", "", "```verse", pack_entry["example"].strip(), "```", ""]
            if pack_entry.get("notes"):
                L += ["## 补充说明", ""]
                for ln in pack_entry["notes"].split("\n"):
                    L.append(ln)
                L.append("")
    page = "\n".join(L).rstrip() + "\n"
    front = (f"---\nname: {member['name']}\nslug: {member['slug']}\nurl: {member.get('url') or ''}\n"
             f"kind: {member['kind']}\nmodule: /Verse.org{'/' + '/'.join(member['slug'].split('/')[1:-1])}\ngrade: {g}\ndepth: {depth}\n"
             f"status: done\n---\n\n")
    open(os.path.join(rel, fname), "w", encoding="utf-8").write(front + page)
    return True, page_rel, None


G_BADGE = {"S": "S", "A": "A", "B": "B", "C": "C"}


def main():
    pack_path = sys.argv[1]
    pack = load_pack(pack_path)
    forest = json.load(open(os.path.join(ROOT, "manifest.json"), encoding="utf-8"))
    members = {}

    def walk(n):
        if n["kind"] != "module" and not n.get("out_of_scope"):
            members[n["slug"]] = n
        for c in n.get("children", []):
            walk(c)

    for t in forest:
        walk(t)

    done = skip_manual = missing = 0
    reports = []
    for slug, entry in pack["entries"].items():
        mem = members.get(slug)
        if not mem:
            missing += 1
            reports.append(f"MISSING in manifest: {slug}")
            continue
        ext = parse_extract(slug)
        if ext is None:
            if member_kind_is_data := (mem["kind"] == "data"):
                ext = {"lead": "", "using": "/Verse.org/Verse", "sig": [], "spec_note": None, "sections": []}
            else:
                skip_manual += 1
                reports.append(f"NO EXTRACT: {slug}")
                continue
        outdir = pack["outdir"]
        for prefix, d in pack.get("sub_outdirs", {}).items():
            if slug.startswith(prefix):
                outdir = d
        fp = os.path.join(ROOT, outdir, re.sub(r"[^a-z0-9_-]+", "_", slug.rsplit("/", 1)[-1]).strip("_") + ".md")
        if os.path.exists(fp) and "status: done" in open(fp, encoding="utf-8").read(300):
            done += 1
            continue
        ok, path, why = emit_page(mem, entry, ext, outdir)
        if ok:
            done += 1
        else:
            skip_manual += 1
            reports.append(f"MANUAL ({why}): {slug} -> {path}")
    # 模块总览
    if pack.get("overview"):
        emit_overview(pack, members)
    for so in pack.get("submodule_overviews", []):
        shim = dict(pack)
        shim.update({"module_slug": so["slug"], "outdir": so["outdir"],
                     "overview": so, "overview_title": so["title"]})
        emit_overview(shim, members)
    print(f"generated={done} manual={skip_manual} missing={missing}")
    for r in reports:
        print(" ", r)


def emit_overview(pack, members):
    outdir = pack["outdir"]
    zh = pack["overview"]["zh"]
    # 收集本模块直接成员（slug 以 module_slug + '/' 开头且无更深层子模块前缀）
    mod_slug = pack["module_slug"]
    rows = {"class": [], "interface": [], "function": [], "enum": [], "data": [], "struct": []}
    for slug, entry in pack["entries"].items():
        mem = members.get(slug)
        if not mem or mem.get("_in_overview"):
            continue
        parent = slug.rsplit("/", 1)[0]
        if parent != mod_slug:
            continue
        kind = "enum" if mem["kind"] == "enum" else mem["kind"]
        fname = re.sub(r"[^a-z0-9_-]+", "_", slug.rsplit("/", 1)[-1]).strip("_") + ".md"
        rows.setdefault(kind, []).append((mem, fname, entry["zh"]))
    K_TITLE = {"class": "Classes and Structs", "struct": "Classes and Structs",
               "interface": "Interfaces", "function": "Functions",
               "enum": "Enumerations", "data": "Data"}
    L = [f"# {(pack.get('overview_title') or 'Module')} <{G_BADGE[pack.get('overview_grade', 'B')]}>", "", zh, ""]
    for kind in ("class", "struct", "interface", "function", "enum", "data"):
        items = rows.get(kind, [])
        if not items:
            continue
        L += [f"## {K_TITLE[kind]}", "", "| Name | Description |", "|---|---|"]
        for mem, fname, zhx in items:
            L.append(f"| [{mem['name']}]({fname}) | {zhx} |")
        L.append("")
    subs = pack.get("submodules", [])
    if subs:
        L += ["## Submodules", "", "| Name | Description |", "|---|---|"]
        for s in subs:
            L.append(f"| [{s['name']}]({s['link']}) | {s['zh']} |")
        L.append("")
    ov = os.path.join(ROOT, outdir, "_overview.md")
    front = (f"---\nname: {pack.get('overview_title') or 'Module'}\nslug: {mod_slug}\n"
             f"url: {pack.get('overview_url') or ''}\nkind: module\nmodule: /{'/'.join(mod_slug.split('/')[:-1]) or mod_slug}\n"
             f"grade: {pack.get('overview_grade', 'B')}\ndepth: brief\nstatus: done\n---\n\n")
    open(ov, "w", encoding="utf-8").write(front + "\n".join(L).rstrip() + "\n")
    print("overview written:", outdir)


if __name__ == "__main__":
    main()
