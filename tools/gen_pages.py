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
    (re.compile(r"^This class is derived from (.+)\.$"), r"此类派生自 。"),
    (re.compile(r"^This class is derived from the following hierarchy, starting with (.+):$"), r"此类派生自以下层级，起点为 ："),
    (re.compile(r"^This (class|interface|struct) exposes the following interfaces:$"), r"此 暴露以下接口："),
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
    (re.compile(r"^(.+?) enumeration includes the following enumerators:$"), r"\1 枚举包含以下枚举值："),
]

KNOWN_CELL = {
    "Base class for authoring logic and data in the SceneGraph. Using components you can author re-usable building blocks of logic and data which can then be added to entities in the scene.":
        "在 SceneGraph 中编写逻辑与数据的基类。通过组件，你可以创作可复用的逻辑与数据构件，然后添加到场景中的实体上。",
    "The parent entity of this component. Components must have a parent entity pointer provided when being constructed. Components cannot be moved between parents.":
        "此组件的父实体。组件构造时必须提供父实体指针；组件不能在父实体之间移动。",
    "Set callbacks to TickEvents.PrePhysics and TickEvents.PostPhysics to receive per-frame updates before and after physics is updated on your object.":
        "设置 TickEvents.PrePhysics 与 TickEvents.PostPhysics 回调，在对象物理更新前/后接收逐帧更新。",
    "Succeeds if the component is currently in the scene. After OnAddedToScene is called this call succeeds. After OnRemovingFromScene is called this call fails.":
        "若组件当前在场景中则成功。OnAddedToScene 调用后成功；OnRemovingFromScene 调用后失败。",
    "Succeeds if the component is currently simulating. After OnBeginSimulation is called this call succeeds. After OnEndSimulation is called this call fails.":
        "若组件当前正在模拟则成功。OnBeginSimulation 调用后成功；OnEndSimulation 调用后失败。",
    "Called when the component is added to the scene by parenting it under the simulation entity or another entity already in the scene. Querying for components in the scene is valid after this phase completes.":
        "当组件通过挂到 simulation 实体（或已在场景中的其他实体）之下而被加入场景时调用。该阶段完成后，查询场景中的组件才是有效的。",
    "Called when the component begins simulating within the scene. Use this to set up TickEvent callbacks or other setup that must be guaranteed to complete immediately. OnAddedToScene is guaranteed to run before OnBeginSimulation.":
        "当组件在场景中开始模拟时调用。用它设置 TickEvent 回调或其他必须保证立即完成的初始化。OnAddedToScene 保证先于 OnBeginSimulation 运行。",
    "Called when the component ends simulation within the scene. Simulation ends on a component when the experience resets, the parent entity is removed from the scene. Cached TickEvents cancelables should be canceled in OnEndSimulation. OnSimulate task will be canceled before OnEndSimulation is called. OnEndSimulation is only called on components that have already had OnBeginSimulation called.":
        "当组件在场景中结束模拟时调用。体验重置或父实体被移出场景时组件的模拟即结束。缓存的 TickEvents cancelable 应在 OnEndSimulation 中取消；OnSimulate 任务会在 OnEndSimulation 被调用前取消。只有已调用过 OnBeginSimulation 的组件才会收到 OnEndSimulation。",
    "Respond to a scene event. Return true to consume the event and halt propagation to the next entity.":
        "响应场景事件。返回 true 表示消费该事件并阻止向下一个实体继续传播。",
    "Called when the component is about to be removed from the scene. Components are removed from a scene when the parent entity is removed from the scene. OnRemovingFromScene is only called on components that have already had OnAddedToScene called.":
        "当组件即将被移出场景时调用。父实体被移出场景时其上的组件随之移除。只有已调用过 OnAddedToScene 的组件才会收到 OnRemovingFromScene。",
    "Called when the component begins simulating within the scene. Use this to add asynchronous/suspends update logic for a component. OnBeginSimulation is guaranteed to run before OnSimulate. OnSimulate will be cancelled before OnEndSimulation":
        "当组件在场景中开始模拟时调用。用它为组件添加异步/可挂起的更新逻辑。OnBeginSimulation 保证先于 OnSimulate 运行；OnSimulate 会在 OnEndSimulation 之前被取消。",
    "Removes the component from the entity. Removed components are removed from the scene and can only be added back to the same entity. Flows through OnEndSimulation-> OnRemovingFromScene.":
        "把组件从实体上移除。被移除的组件会离开场景，且之后只能加回同一个实体。流程经过 OnEndSimulation → OnRemovingFromScene。",
    "Send a scene event to this component, invoking OnReceive. Returns true if any participant consumed the event.":
        "向此组件发送场景事件，触发 OnReceive。有参与者消费该事件则返回 true。",

    "Abstract definition of any element that can be added to a timeline.See timeline_element_point and timeline_element_span.":
        "可加入时间线的元素的抽象定义，见 timeline_element_point 与 timeline_element_span。",
    "Implemented by classes that allow users to cancel an operation. For example, calling subscribable.Subscribe with a callback returns a cancelable object. Calling Cancel on the return object unsubscribes the callback.":
        "由「允许用户取消操作」的类实现：调用 subscribable.Subscribe 传回调会返回一个 cancelable 对象，对其调用 Cancel 即可取消订阅。",
    "Interface that defines a class as being usable as member info in an agent group":
        "定义「可作为代理组成员信息」的接口。",
    "Interface that defines a class as providing an agent group.":
        "定义「提供代理组」能力的接口。",
    "A parametric interface implemented by events with a payload that can be signaled. Can be used with awaitable, subscribable, or both (see: listenable).":
        "带载荷、可被触发（signal）的事件实现的参数化接口；可与 awaitable、subscribable 配合使用（参见 listenable）。",
    "A parametric interface implemented by events with a payload that can be waited on. Matched with signalable.":
        "带载荷、可被等待（Await）的事件实现的参数化接口；与 signalable 配对。",
    "A parametric interface implemented by events with a payload that can be subscribed to. Matched with signalable.":
        "带载荷、可被订阅的事件实现的参数化接口；与 signalable 配对。",
    "Used to specify permissions and other settings for a voice_channel.":
        "用于为 voice_channel 指定权限等设置。",
    "An agent group is defined as a set of agents that share a common ownership.This class stores agents and other data for the group.":
        "代理组：共享同一所有权的代理集合；此类为该组存储代理与其他数据。",
}

MEMBERS_HEAD = re.compile(r"^This (class|interface|struct) has")


KNOWN_PREFIX = [
    ("Base class for authoring logic and data in the SceneGraph.",
     "在 SceneGraph 中编写逻辑与数据的基类。通过组件可创作可复用的逻辑与数据构件并添加到场景中的实体上。组件是非常底层的构件：可暴露网格/声音等引擎概念、添加伤害/交互等玩法能力、存储物品栏；用一个大组件还是拆成多个小组件由体验需求决定。派生自 component 的类必须指定 <final_super> 才能添加到实体；同一子类组在同一实体上只能有一个实例。生命周期：OnAddedToScene → OnBeginSimulation → OnSimulate → OnEndSimulation → OnRemovingFromScene。"),
]

import sys as _sys2
_sys2.path.insert(0, os.path.join(ROOT, 'tools', 'content'))
try:
    from common_cells import COMMON_CELLS
    KNOWN_CELL.update(COMMON_CELLS)
except ImportError:
    pass

def load_pack(path):
    spec = importlib.util.spec_from_file_location("pack", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.PACKS if hasattr(mod, "PACKS") else [mod.PACK]


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


def translate_section(title, body, member=None):
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
                if last in KNOWN_CELL:
                    cells[-1] = KNOWN_CELL[last]
                    out.append("| " + " | ".join(cells) + " |")
                    continue
                matched = False
                for pref, zh2 in KNOWN_PREFIX:
                    if last.startswith(pref):
                        cells[-1] = zh2
                        out.append("| " + " | ".join(cells) + " |")
                        matched = True
                        break
                if matched:
                    continue
                if last and re.search(r"[A-Za-z]{3}", last):
                    print(f"    CELL[{title}] {member['slug'].rsplit('/',1)[-1]}: {last[:130]}")
                    return False, title, body  # 描述列仍是英文 → 转手写
            out.append(ln)
            continue
        if ln.strip():
            print(f"    LINE[{title}] {member['slug'].rsplit('/',1)[-1]}: {ln[:130]}")
            return False, title, body  # 普通英文句子 → 转手写
        out.append(ln)
    return True, title, out


def rel_spec(page_path):
    return os.path.relpath(os.path.join(ROOT, "_Specifiers与Effects.md"),
                           os.path.join(ROOT, os.path.dirname(page_path))).replace("\\", "/")



def emit_children(member, extract, outdir, zh_map=None):
    """把类/接口页 Members 内的 Data/Functions 表行生成为独立 oneliner 子页。
    返回 (生成数, 文件名列表[(fname,row,title,zh)])"""
    import html as _h
    made = []
    parent_last = re.sub(r"[^a-z0-9_-]+", "_", member["slug"].rsplit("/", 1)[-1]).strip("_")
    rel_dir = outdir
    title = member.get("title") or member["name"]
    g_ = member["grade"]
    parent_file = os.path.join(ROOT, rel_dir,
        re.sub(r"[^a-z0-9_-]+", "_", member["slug"].rsplit("/", 1)[-1]).strip("_") + ".md")
    if not os.path.exists(parent_file):
        return 0, []
    rows = []
    subkind = None
    for ln in open(parent_file, encoding="utf-8").read().splitlines():
        if ln.startswith("### "):
            t = ln[4:].strip().lower()
            subkind = "data" if t == "data" else ("function" if t == "functions" else None)
            continue
        if ln.startswith("## "):
            subkind = None
            continue
        if not ln.startswith("|") or subkind is None:
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if cells and cells[0] in ("Name", "Data Member Name", "Function Name"):
            continue
        if len(cells) < 2:
            continue
        if cells[0].startswith("-") or cells[0].startswith("—"):
            continue  # 表格分隔行
        name = cells[0]
        zh = cells[-1]
        if not name or not zh or name.startswith("["):
            continue
        rows.append((subkind, name, zh))
    for idx, (kind, name, zh) in enumerate(rows, 1):
        suffix = "function" if kind == "function" else "data"
        child_title = f"{name} {suffix}"
        cslug = member["slug"] + "/" + re.sub(r"[^a-z0-9]+", "", name.lower())
        fname = f"{parent_last}_{re.sub(r'[^a-z0-9_-]+', '_', name.lower()).strip('_')}.md"
        mod_disp = "/Verse.org" + ("/" + "/".join(member["slug"].split("/")[1:-1]) if member["slug"].count("/") > 1 else "")
        NL = chr(10)
        front = ("---" + NL +
                 f"name: {child_title}" + NL +
                 f"slug: {cslug}" + NL +
                 f"url: {member.get('url') or ''}" + NL +
                 f"kind: {suffix}" + NL +
                 f"module: {mod_disp}" + NL +
                 f"grade: {g_}" + NL +
                 "depth: oneliner" + NL +
                 "status: done" + NL +
                 f"order: {idx}" + NL +
                 f"parent: {member['slug']}" + NL +
                 "---" + NL + NL)

        body = ("#" + NL + f"# {child_title} <{G_BADGE[g_]}>" + NL + NL + zh + NL)
        open(os.path.join(ROOT, rel_dir, fname), "w", encoding="utf-8").write(front + body)
        made.append(fname)
    return len(made), made


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
            ok, t2, body2 = translate_section(title_s, body, member)
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
             f"kind: {member['kind']}\nmodule: {'/' + member['slug'].split('/')[0].replace('versedotorg','Verse.org').replace('unrealenginedotcom','UnrealEngine.com').replace('fortnitedotcom','Fortnite.com') + '/' + '/'.join(member['slug'].split('/')[1:-1])}\ngrade: {g}\ndepth: {depth}\n"
             f"status: done\n---\n\n")
    open(os.path.join(rel, fname), "w", encoding="utf-8").write(front + page)
    return True, page_rel, None


G_BADGE = {"S": "S", "A": "A", "B": "B", "C": "C"}


def main():
    pack_path = sys.argv[1]
    for pack in load_pack(pack_path):
        run_single(pack)


def run_single(pack):
    KNOWN_CELL.update(pack.get('known_cells', {}))
    KNOWN_CELL.update(pack.get('known_cells_ORIG', {}))
    KNOWN_PREFIX.extend(pack.get('known_prefix', []))
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
    # 成员子页（类/接口页的 Data/Functions 行 → 独立 oneliner 子页）
    child_total = 0
    for slug, entry in pack["entries"].items():
        mem = members.get(slug)
        if not mem or mem["depth"] == "oneliner":
            continue
        ext = parse_extract(slug)
        if ext is None:
            continue
        outdir2 = pack["outdir"]
        for prefix, d in pack.get("sub_outdirs", {}).items():
            if slug.startswith(prefix):
                outdir2 = d
        n, _ = emit_children(mem, ext, outdir2)
        child_total += n
    if child_total:
        print(f"  children={child_total}")
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
    for name, zhx in pack.get("overview_data_rows", []):
        L.append(f"| {name} 〔无独立页面〕 | {zhx} |")
    if pack.get("overview_data_rows"):
        pass
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
