# -*- coding: utf-8 -*-
"""
fetch_pages.py — 抓取 Epic 官网 Verse API 页面到 sources/ 本地快照。
用法:
  python tools/fetch_pages.py modules   # 抓取收录范围内的全部模块页
  python tools/fetch_pages.py urls <file>  # 按 URL 列表文件抓取(每行一个路径, 如 versedotorg/simulation/agent)
  python tools/fetch_pages.py pending   # 抓取 manifest.json 中 status=todo 且无本地快照的成员页
页面保存为 sources/<url路径>.html，与官网路径一一对应。
"""
import json
import os
import re
import sys
import time
import urllib.request

BASE = "https://dev.epicgames.com/documentation/fortnite/verse-api/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "sources")
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# 阶段1收录范围：Verse.org 全部 + UnrealEngine.com 全部 + Fortnite.com 精选
# 顺序 = 官网页面出现顺序
MODULES = [
    # Verse.org (16)
    "versedotorg", "versedotorg/verse", "versedotorg/native", "versedotorg/chat",
    "versedotorg/scenegraph", "versedotorg/scenegraph/collisionchannels",
    "versedotorg/scenegraph/collisionprofiles", "versedotorg/scenegraph/keyframedmovement",
    "versedotorg/progression", "versedotorg/timeline", "versedotorg/presentation",
    "versedotorg/input", "versedotorg/agentgroup", "versedotorg/simulation",
    "versedotorg/simulation/tags", "versedotorg/assets", "versedotorg/colors",
    "versedotorg/spatialmath", "versedotorg/random", "versedotorg/predicts",
    "versedotorg/concurrency",
    # UnrealEngine.com (11 + Temporary 子模块 4)
    "unrealenginedotcom", "unrealenginedotcom/conversations",
    "unrealenginedotcom/progression", "unrealenginedotcom/itemization",
    "unrealenginedotcom/webapi", "unrealenginedotcom/temporary",
    "unrealenginedotcom/temporary/ui", "unrealenginedotcom/temporary/curves",
    "unrealenginedotcom/temporary/diagnostics", "unrealenginedotcom/temporary/spatialmath",
    "unrealenginedotcom/social", "unrealenginedotcom/json",
    "unrealenginedotcom/basicshapes", "unrealenginedotcom/abilities",
    "unrealenginedotcom/controlinput", "unrealenginedotcom/assets",
    # Fortnite.com (精选 5 + Devices 索引页)
    "fortnitedotcom", "fortnitedotcom/ui", "fortnitedotcom/ai",
    "fortnitedotcom/animation", "fortnitedotcom/characters",
    "fortnitedotcom/vehicles", "fortnitedotcom/devices",
]


def slug_to_path(slug: str) -> str:
    return os.path.join(SRC, *slug.split("/")) + ".html"


def fetch(slug: str, retries: int = 3) -> tuple[bool, int]:
    dest = slug_to_path(slug)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(BASE + slug, headers=UA)
            data = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "replace")
            if len(data) < 5000 or "Page Not Found" in data:
                return False, len(data)
            with open(dest, "w", encoding="utf-8") as f:
                f.write(data)
            return True, len(data)
        except Exception as e:
            if attempt == retries - 1:
                print(f"  FAIL {slug}: {e}")
                return False, 0
            time.sleep(1.5 * (attempt + 1))
    return False, 0


def load_manifest_slugs() -> list[str]:
    mf = os.path.join(ROOT, "manifest.json")
    if not os.path.exists(mf):
        return []
    slugs = []

    def walk(node):
        if node.get("kind") != "module" and node.get("slug"):
            slugs.append(node["slug"])
        for c in node.get("children", []):
            walk(c)

    for top in json.load(open(mf, encoding="utf-8")):
        walk(top)
    return slugs


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "modules"
    if mode == "modules":
        slugs = MODULES
    elif mode == "urls":
        slugs = [ln.strip().strip("/") for ln in open(sys.argv[2], encoding="utf-8") if ln.strip()]
    elif mode == "pending":
        slugs = [s for s in load_manifest_slugs() if not os.path.exists(slug_to_path(s))]
    else:
        sys.exit("unknown mode")
    ok = fail = skip = 0
    for i, slug in enumerate(slugs):
        dest = slug_to_path(slug)
        if mode == "modules" and os.path.exists(dest) and os.path.getsize(dest) > 5000:
            skip += 1
            continue
        ok1, size = fetch(slug)
        ok += ok1
        fail += not ok1
        print(f"[{i+1}/{len(slugs)}] {'OK ' if ok1 else 'ERR'} {slug} ({size//1024}KB)")
        time.sleep(0.35)
    print(f"done: ok={ok} fail={fail} skip={skip}")


if __name__ == "__main__":
    main()
