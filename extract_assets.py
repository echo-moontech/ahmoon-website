# -*- coding: utf-8 -*-
"""
把 index.html 里的内联 CSS / JS 抽成外部文件，让浏览器可以缓存。

保留内联的部分：
  - gtag 配置片段（依赖全局 dataLayer，且很小）
  - 4 段 JSON-LD 结构化数据（Google 要求出现在文档里）

处理：
  - 两段 <style>         -> assets/main.css
  - 两段业务 <script>    -> assets/app.js
  - CSS 内的相对 url()   -> 改成以 / 开头的绝对路径（外置后基准目录变了）
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(ROOT, "index.html")
ASSETS = os.path.join(ROOT, "assets")

os.makedirs(ASSETS, exist_ok=True)

with open(HTML, "r", encoding="utf-8", errors="ignore") as fh:
    lines = fh.read().split("\n")


def block(start_tag_line, end_tag_line):
    """返回 (内容行列表, 起始行索引, 结束行索引) —— 均为 0-based，含标签本身"""
    s = start_tag_line - 1
    e = end_tag_line - 1
    return lines[s + 1:e], s, e


# ---------- 1. 抽出 CSS ----------
css1, s1, e1 = block(139, 1691)     # 第一个 <style>
css2, s2, e2 = block(1694, 1726)    # 第二个 <style>
css = "\n".join(css1).rstrip() + "\n\n/* ---- */\n\n" + "\n".join(css2).rstrip() + "\n"

# 外置后 CSS 里的相对路径基准从 / 变成 /assets/，必须改成绝对路径
css = css.replace("url('images/", "url('/images/")
css = css.replace('url("images/', 'url("/images/')
css = css.replace("url(images/", "url(/images/")

with open(os.path.join(ASSETS, "main.css"), "w", encoding="utf-8") as fh:
    fh.write(css)

# ---------- 2. 抽出 JS ----------
js1, j1s, j1e = block(3091, 4613)
js2, j2s, j2e = block(4622, 4715)
js = "\n".join(js1).rstrip() + "\n\n" + "\n".join(js2).rstrip() + "\n"

with open(os.path.join(ASSETS, "app.js"), "w", encoding="utf-8") as fh:
    fh.write(js)

# ---------- 3. 重建 index.html ----------
# 需要删掉的区间（按行号从大到小删，避免索引偏移）
ranges = sorted([(s1, e1), (s2, e2), (j1s, j1e), (j2s, j2e)], reverse=True)

new_lines = list(lines)
for s, e in ranges:
    del new_lines[s:e + 1]

out = "\n".join(new_lines)

# 在 </head> 前插入样式表
link_tag = '    <link rel="stylesheet" href="/assets/main.css">'
out = out.replace("</head>", link_tag + "\n</head>", 1)

# 在 </body> 前插入脚本（defer：等 DOM 解析完再执行，与原来放在 body 末尾的效果一致）
script_tag = '<script src="/assets/app.js" defer></script>'
out = out.replace("</body>", script_tag + "\n</body>", 1)

with open(HTML, "w", encoding="utf-8", newline="") as fh:
    fh.write(out)

print("main.css : %d 行, %.1f KB" % (css.count("\n"), len(css.encode("utf-8")) / 1024))
print("app.js   : %d 行, %.1f KB" % (js.count("\n"), len(js.encode("utf-8")) / 1024))
print("index.html: %.1f KB -> %.1f KB" % (
    len("\n".join(lines).encode("utf-8")) / 1024, len(out.encode("utf-8")) / 1024))
