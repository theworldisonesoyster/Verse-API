# -*- coding: utf-8 -*-
"""
build_site.py — 生成 SUMMARY.md（GitBook 侧边栏）与 index.html（单文件交互版）
- 遍历 00_/01_/02_/03_/90_ 目录树（数字前缀=官网顺序）
- 读取每页 frontmatter（name/grade/status）用于显示与过滤
- index.html 内嵌全部 md 内容与树 JSON：双击即开，无需服务器
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_DIRS = ("00_语言基础", "01_Verse.org", "02_UnrealEngine.com", "03_Fortnite.com", "90_分级索引")
GRADE_NAMES = {"S": "核心", "A": "常用", "B": "进阶", "C": "参考"}
TOP_TITLES = {"00_语言基础": "语言基础", "01_Verse.org": "Verse.org",
              "02_UnrealEngine.com": "UnrealEngine.com", "03_Fortnite.com": "Fortnite.com",
              "90_分级索引": "分级索引"}
APPENDIX = [("MANIFEST.md", "MANIFEST 全量清单"), ("STYLE_GUIDE.md", "写作规范 STYLE_GUIDE"), ("PROGRESS.md", "生成进度 PROGRESS"), ("_Specifiers与Effects.md", "Specifiers 与 Effects 对照")]


def frontmatter(path):
    try:
        head = open(path, encoding="utf-8").read(1500)
    except OSError:
        return {}
    m = re.match(r"---\n(.*?)\n---", head, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip()
    return out


def title_map():
    """slug → 官网正式标题（H1）"""
    tm = {}
    try:
        forest = json.load(open(os.path.join(ROOT, "manifest.json"), encoding="utf-8"))
    except OSError:
        return tm

    def walk(n):
        if n.get("title"):
            tm[n["slug"]] = n["title"]
        for c in n.get("children", []):
            walk(c)

    for t in forest:
        walk(t)
    return tm


TITLES = title_map()


def order_map():
    """slug → 官网页面顺序（来自 manifest.json）"""
    om = {}

    def walk(n):
        if n.get("slug"):
            om[n["slug"]] = n.get("order", 0)
        for c in n.get("children", []):
            walk(c)

    try:
        forest = json.load(open(os.path.join(ROOT, "manifest.json"), encoding="utf-8"))
    except OSError:
        return om
    for t in forest:
        walk(t)
    return om


ORDERS = order_map()


def load_node(dirpath, title, rel_dir):
    """目录 → {title, children:[...]}；成员页按 manifest 顺序（官网顺序），子目录按编号前缀"""
    entries = []
    for name in os.listdir(dirpath):
        p = os.path.join(dirpath, name)
        rel = f"{rel_dir}/{name}".replace("\\", "/")
        if os.path.isdir(p) and re.match(r"^\d{3}_", name):
            node = load_node(p, re.sub(r"^\d{3}_", "", name).replace(".", ""), rel)
            ov_slug = frontmatter(os.path.join(p, "_overview.md")).get("slug", "")
            node["title"] = TITLES.get(ov_slug, node["title"])
            entries.append((int(name[:3]) * 100000, node))
        elif name.endswith(".md") and name != "SUMMARY.md":
            fm = frontmatter(p)
            slug = fm.get("slug", "")
            disp = TITLES.get(slug) or fm.get("name") or os.path.splitext(name)[0]
            if name == "_overview.md":
                continue
            # 用 frontmatter 的 slug 反查官网顺序；无则排最后（按名称）
            slug = fm.get("slug", "")
            key = ORDERS.get(slug, 900000 + abs(hash(disp)) % 90000)
            entries.append((key, {"title": disp, "path": rel, "grade": fm.get("grade", ""),
                                  "supplement": fm.get("supplement", "") == "true",
                                  "status": fm.get("status", "done"), "children": None}))
    entries.sort(key=lambda e: e[0])
    node = {"title": title, "path": f"{rel_dir}/_overview.md",
            "children": [e[1] for e in entries],
            "grade": "", "supplement": False,
            "status": frontmatter(os.path.join(dirpath, "_overview.md")).get("status", "done") if os.path.exists(os.path.join(dirpath, "_overview.md")) else "placeholder"}
    return node


def build_tree():
    top = {"title": "Verse API 中文注解", "path": "Intro.md", "children": [], "grade": "", "status": "done", "supplement": False}
    for d in MD_DIRS:
        full = os.path.join(ROOT, d)
        if os.path.isdir(full):
            top["children"].append(load_node(full, TOP_TITLES.get(d, d), d))
    return top


def summary_lines(node, depth=0):
    pad = "  " * depth
    title = node["title"]
    lines = [f"{pad}- [{title}]({node['path']})"]
    for c in node.get("children") or []:
        lines.extend(summary_lines(c, depth + 1))
    return lines


def make_summary(tree):
    lines = ["# Summary", "", summary_lines(tree, 0)[0]]
    for child in tree["children"]:
        lines.extend(summary_lines(child, 0))
    lines.append("")
    lines.append("## 附录")
    for path, title in APPENDIX:
        lines.append(f"- [{title}]({path})")
    lines.append("- [Intro 首页](Intro.md)")
    return "\n".join(lines) + "\n"


def collect_markdown(tree, acc):
    p = os.path.join(ROOT, tree["path"])
    if os.path.exists(p):
        acc[tree["path"]] = open(p, encoding="utf-8").read()
    for c in tree.get("children") or []:
        collect_markdown(c, acc)
    return acc


PAGE_HTML = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Verse API Reference</title>
<style>
:root{--bg:#1c1c1c;--panel:#212121;--panel2:#282828;--fg:#e2e2e2;--dim:#96989e;--acc:#422439;--acc2:#c795b3;--line:#3a3a3a;
--s:#422439;--a:#37c98b;--b:#e8c34a;--c:#6b7280}
*{box-sizing:border-box}body{margin:0;font:15px/1.65 "Segoe UI",system-ui,sans-serif;background:var(--bg);color:var(--fg)}
#app{display:grid;grid-template-columns:330px 1fr;height:100vh}
#side{background:var(--panel);border-right:1px solid var(--line);display:flex;flex-direction:column}
#side header{padding:14px 14px 10px}
#side h1{font-size:15px;margin:0 0 10px}
#search{width:100%;padding:7px 10px;background:var(--panel2);border:1px solid var(--line);color:var(--fg);border-radius:8px;outline:none}
#grades{display:flex;gap:6px;padding:10px 14px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.gbtn{cursor:pointer;border:1px solid var(--line);background:var(--panel2);color:var(--fg);padding:4px 10px;border-radius:20px;font-size:12.5px;user-select:none}
.gbtn.on{background:var(--acc);border-color:#7a4a67;color:#fff}
#tree{flex:1;overflow:auto;padding:8px 6px 30px}
#tree ul{list-style:none;margin:0;padding-left:14px}
#tree>ul{padding-left:6px}
#tree li{margin:1px 0}
#tree li.d>span.t{font-weight:600;cursor:pointer;display:block;padding:3px 8px;border-radius:6px}
#tree li.d>span.t::before{content:"▾ ";color:var(--dim)}
#tree li.d.closed>span.t::before{content:"▸ "}
#tree li.d.closed>ul{display:none}
#tree li.d>span.t:hover{background:var(--panel2)}
#tree a{color:var(--fg);text-decoration:none;display:block;padding:3px 8px;border-radius:6px;cursor:pointer}
#tree a:hover{background:var(--panel2)}
#tree a.cur{background:var(--acc);color:#fff}
#tree a .g{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:6px;vertical-align:1px}
.gS{background:var(--s)}.gA{background:var(--a)}.gB{background:var(--b)}.gC{background:var(--c)}
.pend{color:var(--dim);font-size:11px;margin-left:5px}
#main{overflow:auto;position:relative}
#content{max-width:900px;margin:0 auto;padding:34px 40px 90px}
#content h1{font-size:26px;border-bottom:1px solid var(--line);padding-bottom:10px}
#content h2{font-size:20px;margin-top:34px}
#content code{background:var(--panel2);border:1px solid var(--line);padding:1px 5px;border-radius:5px;font-size:13px;font-family:Consolas,monospace}
#content pre{background:var(--panel2);border:1px solid var(--line);padding:14px;border-radius:10px;overflow:auto}
#content pre code{border:none;background:none;padding:0;font-size:13.5px;line-height:1.55}
#content blockquote{margin:0;padding:6px 14px;border-left:3px solid var(--acc);color:var(--dim);background:var(--panel2);border-radius:0 8px 8px 0}
#content table{border-collapse:collapse;margin:14px 0;width:100%}
#content th,#content td{border:1px solid var(--line);padding:6px 10px;text-align:left;font-size:14px}
#content th{background:var(--acc);color:#f2e7ee;border-color:var(--line)}
#content a{color:var(--acc2);text-decoration:none}
#content a:hover{text-decoration:underline}
#nav{position:fixed;bottom:0;left:330px;right:0;display:flex;justify-content:space-between;padding:10px 40px;background:linear-gradient(transparent,var(--bg) 40%)}
#nav a{color:var(--acc2);cursor:pointer;background:var(--panel2);border:1px solid #5a3a4e;padding:6px 14px;border-radius:8px}
.pending-box{border:1px dashed var(--line);border-radius:10px;padding:18px;color:var(--dim);margin:20px 0;text-align:center}
@media(max-width:900px){#app{grid-template-columns:1fr}#side{display:none}#nav{left:0}}
</style>
</head>
<body>
<div id="app">
  <div id="side">
    <header><h1>Verse API Reference</h1><input id="search" placeholder="搜索 API 名称…"></header>
    <div id="grades"></div>
    <nav id="tree"></nav>
  </div>
  <div id="main"><article id="content"></article></div>
</div>
<div id="nav"><a id="prev">← 上一页</a><a id="next">下一页 →</a></div>
<script id="tree-data" type="application/json">__TREE__</script>
<script id="md-data" type="application/json">__MD__</script>
<script>
const TREE=JSON.parse(document.getElementById('tree-data').textContent);
const MD=JSON.parse(document.getElementById('md-data').textContent);
const $=s=>document.querySelector(s);
let active=null, flat=[];

// ---------- 树展开 ----------
(function flatten(n,depth){n._depth=depth;flat.push(n);(n.children||[]).forEach(c=>flatten(c,depth+1));})(TREE,0);
const byPath=new Map();flat.forEach(n=>{if(n.path)byPath.set(n.path,n)});

// ---------- 渲染侧栏 ----------
function renderGrades(){
  const box=$('#grades');box.innerHTML='';
  for(const g of ['S','A','B','C']){
    const b=document.createElement('span');b.className='gbtn'+(state.grades.has(g)?' on':'');
    b.textContent=g+' '+({S:'核心',A:'常用',B:'进阶',C:'参考'}[g]);
    b.onclick=()=>{state.grades.has(g)?state.grades.delete(g):state.grades.add(g);renderAll()};box.appendChild(b);
  }
}
const state={q:'',grades:new Set()};

function match(n){
  if(state.q && !n.title.toLowerCase().includes(state.q))return false;
  if(state.grades.size===0)return true;
  if(!state.grades.size)return true;
  const g=n.grade||'';
  if(n.children)return n.children.some(match)||state.grades.has(g)&&g!=='';
  return state.grades.has(g);
}
function nodeHtml(n){
  const kids=(n.children||[]).filter(match);
  if(!match(n))return '';
  let cls=n.children?'d':'leaf';
  let g=n.grade?`<span class="g g${n.grade}"></span>`:'';
  let pend=(n.status==='placeholder')?'<span class="pend">待生成</span>':'';
  let inner=g+htmlEsc(n.title)+pend;
  let s=`<li class="${cls}">`;
  s+=n.children?`<span class="t">${inner}</span>`:`<a data-p="${n.path}" class="${active===n.path?'cur':''}">${inner}</a>`;
  if(kids.length)s+='<ul>'+kids.map(nodeHtml).join('')+'</ul>';
  return s+'</li>';
}
function renderTree(){
  const kids=(TREE.children||[]).filter(match);
  $('#tree').innerHTML='<ul>'+kids.map(nodeHtml).join('')+'</ul>';
  $('#tree').querySelectorAll('li.d>span.t').forEach(sp=>sp.onclick=()=>sp.parentElement.classList.toggle('closed'));
  $('#tree').querySelectorAll('a').forEach(a=>a.onclick=()=>show(a.dataset.p));
}
function renderAll(){renderGrades();renderTree()}

// ---------- 极简 Markdown 渲染 ----------
function htmlEsc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}
function esc(s){return htmlEsc(s)}
function inline(s){
  s=esc(s);
  s=s.replace(/`([^`]+)`/g,'<code>$1</code>');
  s=s.replace(/\\*\\*([^*]+)\\*\\*/g,'<b>$1</b>');
  s=s.replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g,(m,t,p)=>{
    if(p.endsWith('.md'))return `<a data-p="${p}" href="javascript:void(0)">${t}</a>`;
    return `<a href="${p}" target="_blank">${t}</a>`});
  return s;
}
function md2html(md){
  const lines=md.split('\\n');let out=[],i=0,inCode=false,code=[],list=null,tbl=null,quote=null;
  const flushList=()=>{if(list){out.push(`<ul>${list.map(x=>'<li>'+x+'</li>').join('')}</ul>`);list=null}};
  const flushTbl=()=>{if(tbl){let h='';tbl.forEach((r,ri)=>{const t=ri===0?'th':'td';h+='<tr>'+r.map(c=>`<${t}>${inline(c)}</${t}>`).join('')+'</tr>'});out.push(`<table>${h}</table>`);tbl=null}};
  const flushQ=()=>{if(quote){out.push('<blockquote>'+quote.map(x=>inline(x)).join('<br>')+'</blockquote>');quote=null}};
  for(;i<lines.length;i++){
    const L=lines[i];
    if(L.startsWith('```')){flushList();flushTbl();flushQ();
      if(inCode){out.push('<pre><code>'+code.join('\\n')+'</code></pre>');code=[];inCode=false}
      else inCode=true;continue}
    if(inCode){code.push(L);continue}
    if(!L.trim()){flushList();flushTbl();flushQ();continue}
    if(L.startsWith('|')){const cells=L.split('|').slice(1,-1).map(x=>x.trim());
      if(cells.every(c=>/^-+$/.test(c)))continue;flushList();flushQ();tbl=tbl||[];tbl.push(cells);continue}
    if(L.startsWith('# ')){flushList();flushTbl();flushQ();out.push('<h1>'+inline(L.slice(2))+'</h1>');continue}
    if(L.startsWith('## ')){flushList();flushTbl();flushQ();out.push('<h2>'+inline(L.slice(3))+'</h2>');continue}
    if(L.startsWith('### ')){flushList();flushTbl();flushQ();out.push('<h3>'+inline(L.slice(4))+'</h3>');continue}
    if(/^>\s*$/.test(L)){flushList();flushTbl();flushQ();continue}
    if(L.startsWith('> ')){flushList();flushTbl();quote=quote||[];quote.push(L.slice(2).replace(/^- /,'• '));continue}
    if(/^[-*] /.test(L)){flushTbl();flushQ();list=list||[];list.push(inline(L.slice(2)));continue}
    if(/^\d+\. /.test(L)){flushTbl();flushQ();list=list||[];list.push(inline(L.replace(/^\\d+\\. /,'')));continue}
    if(L.startsWith('---')){flushList();flushTbl();flushQ();out.push('<hr>');continue}
    flushList();flushTbl();flushQ();out.push('<p>'+inline(L)+'</p>');
  }
  flushList();flushTbl();flushQ();
  if(inCode)out.push('<pre><code>'+code.join('\\n')+'</code></pre>');
  return out.join('\\n');
}

// ---------- 内容与导航 ----------
const leaves=flat.filter(n=>n.children===null||n.children&&n.children.length===0&&false);
const order=flat.filter(n=>!n.children&&n.path&&MD[n.path]);
function show(path){
  active=path;
  const n=byPath.get(path)||{};
  let body=MD[path]||'';
  const isPending=/status: placeholder/.test(body.split('---')[1]||'')||n.status==='placeholder';
  let htmlOut=md2html(body);
  if(isPending)htmlOut+='<div class="pending-box">⏳ 本页在阶段1为占位页，正文将由批量生成阶段填充。<br>官方原文快照已保存在仓库 sources/ 目录。</div>';
  htmlOut=htmlOut.replace(/status: placeholder\\n?/g,'');
  $('#content').innerHTML=htmlOut;
  $('#content').querySelectorAll('a[data-p]').forEach(a=>a.onclick=()=>show(a.getAttribute('data-p')));
  $('#content').scrollTop=0;document.querySelector('#main').scrollTop=0;
  renderTree();
}
$('#prev').onclick=()=>step(-1);$('#next').onclick=()=>step(1);
function step(d){
  const i=order.findIndex(n=>n.path===active);
  const j=Math.min(order.length-1,Math.max(0,(i<0?0:i)+d));
  if(order[j])show(order[j].path);
}
$('#search').oninput=e=>{state.q=e.target.value.trim().toLowerCase();renderTree()};

// frontmatter 剥离
for(const k in MD){MD[k]=MD[k].replace(/^---\\n[\\s\\S]*?\\n---\\n?/,'')}
renderAll();show('Intro.md');
</script>
</body>
</html>
"""


def html_esc(s):
    return html.escape(s, quote=True)


def main():
    tree = build_tree()
    # 90_分级索引 若未生成则占位
    idx_dir = os.path.join(ROOT, "90_分级索引")
    os.makedirs(idx_dir, exist_ok=True)
    for g, name in GRADE_NAMES.items():
        p = os.path.join(idx_dir, f"{g}索引.md")
        if not os.path.exists(p):
            open(p, "w", encoding="utf-8").write(
                f"---\nname: {g}索引\nslug: 90_分级索引/{g}\nurl: \nkind: module\nmodule: /分级索引\n"
                f"grade: {g}\ndepth: brief\nstatus: placeholder\n---\n\n"
                f"# {g} 级（{name}）索引\n\n<!-- 由阶段2按 MANIFEST 填充全部 {g} 级页面链接 -->\n")

    summary = make_summary(tree)
    open(os.path.join(ROOT, "SUMMARY.md"), "w", encoding="utf-8").write(summary)

    md = collect_markdown(tree, {})
    md["Intro.md"] = open(os.path.join(ROOT, "Intro.md"), encoding="utf-8").read()
    for path, _ in APPENDIX:
        p = os.path.join(ROOT, path)
        if os.path.exists(p):
            md[path] = open(p, encoding="utf-8").read()

    page = PAGE_HTML.replace("__TREE__", json.dumps(tree, ensure_ascii=False)) \
                    .replace("__MD__", json.dumps(md, ensure_ascii=False))
    out = os.path.join(ROOT, "index.html")
    open(out, "w", encoding="utf-8").write(page)

    # 简单校验
    n_pages = len(md)
    n_entries = [json.dumps(tree).count('"path"')]
    print(f"SUMMARY.md: {len(summary.splitlines())} 行; index.html: {len(page)//1024} KB, 内嵌文档 {n_pages} 页")


if __name__ == "__main__":
    main()
