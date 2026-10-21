# -*- coding: utf-8 -*-
"""
重建 sitemap.xml：
  - 加入新生成的 /zh/ 与 /es/ 首页
  - 首页三语用 xhtml:link 互指 hreflang（多语言站点的标准写法）
  - lastmod 统一更新为本次改版的日期（所有页面都做了图片优化）
"""
import os
import re
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "sitemap.xml")
SITE = "https://moontechsilicone.com"
TODAY = date.today().isoformat()

with open(SRC, "r", encoding="utf-8") as fh:
    raw = fh.read()

urls = re.findall(r'<loc>([^<]+)</loc>', raw)

# 首页三语
home_variants = [
    ("en", SITE + "/"),
    ("zh", SITE + "/zh/"),
    ("es", SITE + "/es/"),
]

out = []
out.append('<?xml version="1.0" encoding="UTF-8"?>')
out.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
out.append('        xmlns:xhtml="http://www.w3.org/1999/xhtml">')

# 先写三个首页，带 hreflang 互指
for lang, loc in home_variants:
    out.append("  <url>")
    out.append("    <loc>%s</loc>" % loc)
    out.append("    <lastmod>%s</lastmod>" % TODAY)
    out.append("    <changefreq>weekly</changefreq>")
    out.append('    <priority>%s</priority>' % ("1.0" if lang == "en" else "0.9"))
    for lg, l in home_variants:
        out.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (lg, l))
    out.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>' % SITE + "/")
    out.append("  </url>")

# 其余页面（产品页 / 文章页，目前只有英文版）
for u in urls:
    if u.rstrip("/") == SITE:
        continue          # 首页已单独写入
    priority = "0.9" if "/products/" in u else "0.7"
    freq = "monthly"
    if u.rstrip("/").endswith("/articles"):
        priority = "0.8"
        freq = "weekly"
    out.append("  <url>")
    out.append("    <loc>%s</loc>" % u)
    out.append("    <lastmod>%s</lastmod>" % TODAY)
    out.append("    <changefreq>%s</changefreq>" % freq)
    out.append("    <priority>%s</priority>" % priority)
    out.append('    <xhtml:link rel="alternate" hreflang="en" href="%s"/>' % u)
    out.append("  </url>")

out.append("</urlset>")

with open(SRC, "w", encoding="utf-8", newline="") as fh:
    fh.write("\n".join(out) + "\n")

print("sitemap.xml 已重建：%d 条 URL（含 /zh/ 与 /es/）" % (len(urls) + 2))
