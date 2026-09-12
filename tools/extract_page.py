# -*- coding: utf-8 -*-
"""
extract_page.py — 官网快照 HTML → 结构化 Markdown（保持官网段落顺序与完整表格）
用法:
  python tools/extract_page.py <slug>              # 单页, 输出到 stdout
  python tools/extract_page.py all                 # 全量 → tools/_extracted/<slug>.md
输出规则: h2/h3 → ##/###; 表格 → MD表格; <pre><code> → ```verse 块; 其余文本按段落。
"""
import html as H
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "tools", "_extracted")


def clean(s: str) -> str:
    s = re.sub(r"<br\s*/?>", " ", s)
    s = H.unescape(re.sub(r"<[^>]+>", "", s))
    return re.sub(r"\s+", " ", s).strip().replace("\xa0", " ")


def conv_table(tbl: str) -> str:
    rows = re.findall(r"<tr>(.*?)</tr>", tbl, re.S)
    if not rows:
        return ""
    out_rows = []
    header = None
    if re.search(r"<thead", tbl):
        pass
    for r in rows:
        cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", r, re.S)
        vals = [clean(c) for c in cells]
        if any(re.search(r"<th[ >]", c) for c in cells) and header is None:
            header = vals
            continue
        out_rows.append(vals)
    lines = []
    if header:
        lines.append("| " + " | ".join(header) + " |")
        lines.append("|" + "---|" * len(header))
    for vals in out_rows:
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)


def conv_block(seg: str) -> list[str]:
    """把一段 HTML（不含 h2/h3 标题）转成 MD 行"""
    out = []
    pos = 0
    pattern = re.compile(r"<table.*?</table>|<pre>.*?</pre>|<ul>.*?</ul>|<p>.*?</p>|<blockquote>.*?</blockquote>", re.S)
    for m in pattern.finditer(seg):
        gap = clean(seg[pos:m.start()])
        if gap:
            out.append(gap)
        piece = m.group(0)
        if piece.startswith("<table"):
            out.append(conv_table(piece))
        elif piece.startswith("<pre"):
            code = clean(re.sub(r"^<pre>(<code[^>]*>)?|(</code>)?</pre>$", "", piece.strip(), flags=re.S))
            out.append("```verse\n" + code + "\n```")
        elif piece.startswith("<ul"):
            for li in re.findall(r"<li>(.*?)</li>", piece, re.S):
                out.append("- " + clean(li))
        elif piece.startswith("<blockquote"):
            out.append("> " + clean(piece))
        else:
            t = clean(piece)
            if t:
                out.append(t)
        pos = m.end()
    gap = clean(seg[pos:])
    if gap:
        out.append(gap)
    return [x for x in out if x.strip()]


def extract(slug: str) -> str:
    p = os.path.join(ROOT, "sources", *slug.split("/")) + ".html"
    page = open(p, encoding="utf-8").read()
    m = re.search(r'class="block-markdown">(.*?)</block-markdown>', page, re.S)
    if not m:
        return f"(页面无正文: {slug})"
    body = m.group(1)
    parts = re.split(r"(<h[23][^>]*>.*?</h[23]>)", body, flags=re.S)
    lines = []
    lead = conv_block(parts[0])
    if lead:
        lines.extend(lead)
        lines.append("")
    for i in range(1, len(parts), 2):
        head = clean(parts[i])
        level = "##" if parts[i].startswith("<h2") else "###"
        lines.append(f"{level} {head}")
        seg = parts[i + 1] if i + 1 < len(parts) else ""
        blk = conv_block(seg)
        if blk:
            lines.extend(blk)
        lines.append("")
    text = "\n".join(lines)
    # Specifiers/Effects 公共长表压缩为标签行（语义统一见附录）
    text = re.sub(r"## Attributes, Specifiers, and Effects.*?(?=\n## |\Z)",
                  "_（Attributes/Specifiers/Effects 公共说明见《Specifiers 与 Effects 对照》，此处不重复官网公共表格）_\n",
                  text, flags=re.S)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == "all":
        n = 0
        for dirpath, _, files in os.walk(os.path.join(ROOT, "sources")):
            for fn in files:
                if not fn.endswith(".html"):
                    continue
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, os.path.join(ROOT, "sources"))[:-5].replace("\\", "/")
                page = open(full, encoding="utf-8").read()
                if 'class="block-markdown"' not in page:
                    continue
                dest = os.path.join(OUT, *rel.split("/")) + ".md"
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                open(dest, "w", encoding="utf-8").write(extract(rel))
                n += 1
        print(f"extracted {n} pages -> {OUT}")
    else:
        print(extract(sys.argv[1].strip("/")))


if __name__ == "__main__":
    main()
