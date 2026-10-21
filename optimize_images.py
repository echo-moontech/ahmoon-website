# -*- coding: utf-8 -*-
"""
图片优化脚本：
  1. 把 jpg / png 转成 webp（仅在 webp 确实更小时才采用）
  2. 给所有 <img> 补 width / height，消除 CLS 布局偏移
  3. 用 <picture> 提供 webp + 原图兜底

可重复执行；已处理过的标签会被跳过。
"""
import os
import re
import sys
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
IMGDIR = os.path.join(ROOT, "images")

HTML_FILES = ["index.html", "404.html"]
for d in ("products", "articles"):
    p = os.path.join(ROOT, d)
    if os.path.isdir(p):
        for f in sorted(os.listdir(p)):
            if f.endswith(".html"):
                HTML_FILES.append(os.path.join(d, f).replace("\\", "/"))

QUALITY = 82
MIN_SAVE_RATIO = 0.95   # webp 至少要小 5% 才采用


def gather_sizes_and_convert():
    sizes = {}
    use_webp = {}
    stats = {"converted": 0, "skipped_exists": 0, "too_big": 0, "failed": 0}

    for name in sorted(os.listdir(IMGDIR)):
        path = os.path.join(IMGDIR, name)
        if not os.path.isfile(path):
            continue
        ext = os.path.splitext(name)[1].lower()

        try:
            with Image.open(path) as im:
                sizes[name] = im.size
        except Exception:
            stats["failed"] += 1
            continue

        if ext not in (".jpg", ".jpeg", ".png"):
            continue

        webp_name = os.path.splitext(name)[0] + ".webp"
        webp_path = os.path.join(IMGDIR, webp_name)

        # 已存在同名 webp：直接复用，不覆盖（避免误替换手工优化过的图）
        if os.path.exists(webp_path):
            use_webp[name] = webp_name
            stats["skipped_exists"] += 1
            continue

        try:
            with Image.open(path) as im:
                im.load()
                if im.mode in ("RGBA", "LA", "P"):
                    im = im.convert("RGBA")
                else:
                    im = im.convert("RGB")
                im.save(webp_path, "WEBP", quality=QUALITY, method=4)
            old = os.path.getsize(path)
            new = os.path.getsize(webp_path)
            if new < old * MIN_SAVE_RATIO:
                use_webp[name] = webp_name
                stats["converted"] += 1
            else:
                os.remove(webp_path)
                stats["too_big"] += 1
        except Exception:
            stats["failed"] += 1

    return sizes, use_webp, stats


IMG_RE = re.compile(r'<img\s[^>]*>', re.IGNORECASE)


def process_html(relpath, sizes, use_webp):
    full = os.path.join(ROOT, relpath)
    with open(full, "r", encoding="utf-8", errors="ignore") as fh:
        html = fh.read()

    changed_dim = 0
    changed_pic = 0

    def repl(m):
        nonlocal changed_dim, changed_pic
        tag = m.group(0)
        srcm = re.search(r'\bsrc\s*=\s*"([^"]+)"', tag, re.IGNORECASE)
        if not srcm:
            return tag
        src = srcm.group(1).strip()
        if not src or src.startswith("data:") or src.startswith("http"):
            return tag

        base = os.path.basename(src)
        dims = sizes.get(base)

        new_tag = tag
        if dims and 'width=' not in tag.lower():
            new_tag = new_tag[:-1].rstrip() + ' width="%d" height="%d">' % dims
            changed_dim += 1

        # 已经是 webp 或没有对应 webp 就不包 picture
        if base.lower().endswith(".webp"):
            return new_tag
        wname = use_webp.get(base)
        if not wname:
            return new_tag
        if "<picture" in m.string[max(0, m.start() - 12):m.start()].lower():
            return new_tag

        webp_src = src[:src.rfind(".")] + ".webp"
        changed_pic += 1
        return ('<picture><source srcset="%s" type="image/webp">%s</picture>'
                % (webp_src, new_tag))

    out = IMG_RE.sub(repl, html)

    if out != html:
        with open(full, "w", encoding="utf-8", newline="") as fh:
            fh.write(out)

    return changed_dim, changed_pic


def main():
    print("扫描 images/ ...")
    sizes, use_webp, stats = gather_sizes_and_convert()
    print("  尺寸已读取: %d 张" % len(sizes))
    print("  新转换 webp: %d / 复用已有: %d / 体积未更优而放弃: %d / 失败: %d"
          % (stats["converted"], stats["skipped_exists"],
             stats["too_big"], stats["failed"]))

    print("\n处理 HTML ...")
    total_d = total_p = 0
    for rel in HTML_FILES:
        if not os.path.exists(os.path.join(ROOT, rel)):
            continue
        d, p = process_html(rel, sizes, use_webp)
        if d or p:
            print("  %-58s 补尺寸:%-3d 转picture:%d" % (rel, d, p))
        total_d += d
        total_p += p

    print("\n完成：补 width/height %d 处，picture 包裹 %d 处" % (total_d, total_p))


if __name__ == "__main__":
    main()
