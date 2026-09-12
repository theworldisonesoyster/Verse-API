# -*- coding: utf-8 -*-
"""
parse_modules.py v2 — 解析 sources/ 模块页 → manifest.json
- 模块显示名取自父页面层级 <ul> 中的 <code> 名（保留大小写）
- 识别空模块（"currently empty" / "no content other than submodules"）
- Data 等分节中无链接的条目也收录（linked=False, url=None）
- 从层级 <ul> 自动发现未抓取的子模块 → 写入 tools/_new_modules.txt 供 fetch 闭包
"""
import html as htmllib
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "sources")
BASEURL = "https://dev.epicgames.com/documentation/fortnite/verse-api/"

TOPS = {"versedotorg": "Verse.org", "unrealenginedotcom": "UnrealEngine.com", "fortnitedotcom": "Fortnite.com"}
SECTION_KIND = {"classes and structs": "class", "classes": "class", "structs": "struct",
                "interfaces": "interface", "enumerations": "enum", "functions": "function", "data": "data"}

# Fortnite.com 收录白名单（前缀匹配）；其余顶层域全收
FN_SCOPE = ("fortnitedotcom/ui", "fortnitedotcom/ai", "fortnitedotcom/animation",
            "fortnitedotcom/characters", "fortnitedotcom/vehicles", "fortnitedotcom/devices")

EMPTY_MARKS = ("this module is currently empty", "this module has no content other than submodules")


def in_scope(slug: str) -> bool:
    top = slug.split("/", 1)[0]
    if top == "fortnitedotcom":
        return slug.startswith(FN_SCOPE)
    return top in TOPS


def strip_tags(s: str) -> str:
    return re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def load(slug: str) -> str:
    p = os.path.join(SRC, *slug.split("/")) + ".html"
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""


def _balanced_ul(text: str, start: int) -> str | None:
    """从 start 起取第一个完整配平的 <ul>...</ul>（含嵌套）"""
    i = text.find("<ul>", start)
    if i < 0:
        return None
    depth = 0
    for m in re.finditer(r"<ul>|</ul>", text[i:]):
        depth += 1 if m.group(0) == "<ul>" else -1
        if depth == 0:
            return text[i:i + m.end()]
    return None


def hierarchy_children(page: str, module_name: str) -> list[tuple[str, str]]:
    """层级 ul: 当前模块加粗条目之后的嵌套 <ul> 中【第一层】子模块链接"""
    out = []
    for m in re.finditer(r"<strong><code>([^<]+)</code></strong>", page):
        cur = m.group(1).strip()
        if cur.lower() != module_name.lower():
            continue
        inner = _balanced_ul(page, m.end())
        if not inner:
            continue
        # 去掉外层 <ul> 包装，只留下内容
        content = inner[4:-5]
        # 剥掉更深层嵌套的 <ul>，只留第一层 <li> 中的链接
        while True:
            stripped = re.sub(r"<ul>(?:(?!<ul>|</ul>).)*</ul>", "", content, flags=re.S)
            if stripped == content:
                break
            content = stripped
        for href, nm in re.findall(r'href="(/documentation/fortnite/verse-api/[^"]+)"[^>]*><code>([^<]+)</code>', content):
            nm = htmllib.unescape(nm).strip()
            out.append((href.replace("/documentation/fortnite/verse-api/", "").rstrip("/"), nm))
    return out


def parse_module(slug: str, name: str) -> dict:
    page = load(slug)
    node = {"name": name, "slug": slug, "kind": "module", "url": BASEURL + slug if slug else None,
            "desc": "", "order": 0, "children": []}
    if not page:
        node["missing"] = True
        return node
    m = re.search(r'class="block-markdown">(.*?)</block-markdown>', page, re.S)
    body = m.group(1) if m else ""
    intro = re.split(r"<h2", body)[0]
    node["desc"] = strip_tags(intro)[:300]
    low = strip_tags(body).lower()
    if any(k in low for k in EMPTY_MARKS):
        node["empty"] = True

    kids = hierarchy_children(page, name)
    child_names = {s: n for s, n in kids}
    node["_child_modules"] = [s for s, _ in kids]

    order = 0
    for s, nm in kids:
        order += 1
        node["children"].append({"name": nm, "slug": s, "kind": "module", "url": BASEURL + s,
                                 "desc": "", "order": order, "children": []})

    for h2 in re.finditer(r"<h2[^>]*>(.*?)</h2>", body):
        sec = strip_tags(h2.group(1))
        if sec.lower() not in SECTION_KIND:
            continue
        start = h2.end()
        nxt = re.search(r"<h2", body[start:])
        secbody = body[start:start + nxt.start()] if nxt else body[start:]
        rows = re.findall(r"<tr>(.*?)</tr>", secbody, re.S)
        for r in rows[1:]:
            link = re.search(r'href="(/documentation/fortnite/verse-api/[^"]+)"[^>]*><code>([^<]+)</code>', r)
            if link:
                mslug = link.group(1).replace("/documentation/fortnite/verse-api/", "").rstrip("/")
                nm = htmllib.unescape(link.group(2)).strip()
                linked = True
            else:
                cm = re.search(r"<code>([^<]+)</code>", r)
                if not cm:
                    continue
                nm = cm.group(1).strip()
                mslug = slug + "/" + re.sub(r"[^a-z0-9]+", "", nm.lower()) if slug else nm.lower()
                linked = False
            desc = strip_tags(r)
            desc = desc.replace(nm, "", 1).strip()[:300]
            order += 1
            node["children"].append({"name": nm, "slug": mslug, "kind": SECTION_KIND[sec.lower()],
                                     "url": BASEURL + mslug if linked else None, "desc": desc,
                                     "order": order, "linked": linked})
    return node


def build() -> tuple[list, set]:
    """从三大顶层模块递归解析；in_scope 但未抓取的子模块 → new_slugs"""
    forest, new_slugs, visited = [], set(), set()

    def recurse(node):
        if node["slug"] in visited:
            return
        visited.add(node["slug"])
        depth = node["slug"].count("/")
        node["children"] = [
            c for c in node.get("children", [])
            if not (c["kind"] == "module" and (c["slug"] in visited or c["slug"].count("/") != depth + 1))
        ]
        for c in node.get("children", []):
            if c["kind"] != "module":
                continue
            if not in_scope(c["slug"]):
                c["out_of_scope"] = True
                continue
            if load(c["slug"]):
                parsed = parse_module(c["slug"], c["name"])
                for k in ("desc", "empty", "missing"):
                    if k in parsed:
                        c[k] = parsed[k]
                c["children"] = parsed["children"]
                recurse(c)
            else:
                new_slugs.add(c["slug"])

    for top_slug, top_name in TOPS.items():
        top = parse_module(top_slug, top_name)
        recurse(top)
        forest.append(top)
    return forest, new_slugs


def main():
    import sys
    forest, new = build()
    if new:
        open(os.path.join(ROOT, "tools", "_new_modules.txt"), "w", encoding="utf-8").write("\n".join(sorted(new)))
        print("NEW modules to fetch:", sorted(new))
        sys.exit(2)

    def renumber(nodes):
        for i, n in enumerate(nodes, 1):
            n["order"] = i
            renumber(n.get("children", []))

    for top in forest:
        renumber(top["children"])
        for sub in top["children"]:
            renumber(sub.get("children", []))

    def stats(n, acc):
        if n["kind"] != "module":
            acc[n["kind"]] = acc.get(n["kind"], 0) + 1
            if not n.get("linked", True):
                acc["unlinked"] = acc.get("unlinked", 0) + 1
        for c in n.get("children", []):
            stats(c, acc)
        return acc

    total = 0
    for top in forest:
        st = stats(top, {})
        cnt = sum(v for k, v in st.items() if k != "unlinked")
        total += cnt
        print(f"{top['name']}: {cnt} members {st}")
    print("TOTAL members:", total)
    def clean(n):
        n.pop("_child_modules", None)
        for c in n.get("children", []):
            clean(c)
    for t in forest:
        clean(t)
    json.dump(forest, open(os.path.join(ROOT, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("manifest.json written")


if __name__ == "__main__":
    main()
