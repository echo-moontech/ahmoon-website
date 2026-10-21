# -*- coding: utf-8 -*-
"""
多语言 SEO 改造：
  1. 语言改为「URL 优先」：/ = 英文，/zh/ = 中文，/es/ = 西语
     —— 原来只认 localStorage，页面加载时会把静态化的中文页覆盖回英文
  2. switchLang() 改为跳转对应语言 URL（内页跳该语言首页）
  3. 生成 /zh/index.html 与 /es/index.html（内容硬编码成对应语言）
  4. 三个页面互相标注 hreflang + canonical + x-default

生成的页面仍然是完整可用的页面：访问 /zh/ 直接就是中文，
不再依赖 JS 二次渲染，搜索引擎也能抓到中文内容。
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
APPJS = os.path.join(ROOT, "assets", "app.js")
INDEX = os.path.join(ROOT, "index.html")
SITE = "https://moontechsilicone.com"

LANGS = {"en": "", "zh": "/zh", "es": "/es"}


# ------------------------------------------------------------------ 工具
def esc(s):
    """写入 HTML 文本时转义裸 & ，但不动已有的实体"""
    return re.sub(r'&(?![a-zA-Z]+;|#\d+;)', '&amp;', s)


KV_RE = re.compile(r'^\s*([A-Za-z_$][\w$]*)\s*:\s*"(.*)",?\s*$')


def parse_dict(lines, start, end):
    """逐行解析 JS 对象字面量的 key: "value"（不能用 json，JS 的 key 没有引号）"""
    out = {}
    for raw in lines[start:end]:
        line = raw.strip()
        if line.startswith("//") or not line:
            continue
        # 去掉行尾注释（只在引号结束后出现的 // 才算）
        m = KV_RE.match(line)
        if not m:
            continue
        key, val = m.group(1), m.group(2)
        try:
            val = json.loads('"%s"' % val)   # 处理 \" 之类的转义
        except Exception:
            pass
        out[key] = val
    return out


# ------------------------------------------------------------------ 1. 改 app.js
with open(APPJS, "r", encoding="utf-8") as fh:
    js = fh.read()

old_init = "        window.currentLang = localStorage.getItem('moonLang') || 'en';"
new_init = """        // 语言以 URL 为准：/ = en，/zh/ = zh，/es/ = es
        // 这样静态化的 /zh/、/es/ 页面不会被 localStorage 覆盖回英文
        window.currentLang = (function () {
            var p = location.pathname;
            if (p.indexOf('/zh/') === 0) return 'zh';
            if (p.indexOf('/es/') === 0) return 'es';
            return localStorage.getItem('moonLang') || 'en';
        })();"""

if old_init in js:
    js = js.replace(old_init, new_init, 1)
    print("app.js: 初始化改为 URL 优先 ✓")
else:
    print("app.js: 未找到初始化语句，跳过")

old_sw = """        function switchLang(lang) {
            window.currentLang = lang;
            localStorage.setItem('moonLang', lang);"""
new_sw = """        function switchLang(lang) {
            // 切换语言 = 跳转到对应语言的 URL（内页跳该语言首页）
            var _p = location.pathname;
            var _isHome = (_p === '/' || _p === '/index.html'
                           || _p === '/zh/' || _p === '/zh/index.html'
                           || _p === '/es/' || _p === '/es/index.html');
            var _target;
            if (_isHome) {
                _target = lang === 'en' ? '/' : '/' + lang + '/';
            } else {
                _target = lang === 'en' ? '/' : '/' + lang + '/';
            }
            if (_target !== _p && _target !== _p.replace(/index\\.html$/, '')) {
                try { localStorage.setItem('moonLang', lang); } catch (e) {}
                location.href = _target;
                return;
            }
            window.currentLang = lang;
            localStorage.setItem('moonLang', lang);"""

if old_sw in js:
    js = js.replace(old_sw, new_sw, 1)
    print("app.js: switchLang 改为跳转 URL ✓")
else:
    print("app.js: 未匹配 switchLang 开头，跳过")

with open(APPJS, "w", encoding="utf-8", newline="") as fh:
    fh.write(js)


# ------------------------------------------------------------------ 2. 读字典
with open(APPJS, "r", encoding="utf-8") as fh:
    jslines = fh.read().split("\n")

# 重新定位（app.js 已被修改，行号会变，按关键字找）
def find_lang_block(lang):
    for i, ln in enumerate(jslines):
        if re.match(r'^\s*' + lang + r':\s*\{\s*$', ln):
            return i
    return None


en_i = find_lang_block("en")
zh_i = find_lang_block("zh")
es_i = find_lang_block("es")
end_i = next(i for i, ln in enumerate(jslines) if re.match(r'^\s*\};\s*$', ln) and i > es_i)

DICT = {
    "en": parse_dict(jslines, en_i + 1, zh_i),
    "zh": parse_dict(jslines, zh_i + 1, es_i),
    "es": parse_dict(jslines, es_i + 1, end_i),
}
for k, v in DICT.items():
    print("字典 %s: %d 条" % (k, len(v)))


# ------------------------------------------------------------------ 3. 生成页面
with open(INDEX, "r", encoding="utf-8") as fh:
    base_html = fh.read()

I18N_RE = re.compile(
    r'(<([a-zA-Z0-9]+)([^>]*?)\sdata-i18n="([^"]+)"([^>]*)>)(.*?)(</\2>)',
    re.S)


def apply_translation(html, lang):
    d = DICT[lang]

    def repl(m):
        open_tag, tagname, pre, key, post, inner, close_tag = m.groups()
        if key not in d:
            return m.group(0)
        val = esc(d[key])
        # 与 switchLang 保持一致：如果里面有 <a>，只改 <a> 的文字
        am = re.search(r'(<a\s[^>]*>)(.*?)(</a>)', inner, re.S)
        if am:
            new_inner = inner[:am.start(2)] + val + inner[am.end(2):]
        else:
            new_inner = val
        return open_tag + new_inner + close_tag

    out = I18N_RE.sub(repl, html)

    # data-i18n-placeholder
    def repl_ph(m):
        key = m.group(2)
        if key in d:
            return re.sub(r'placeholder="[^"]*"', 'placeholder="%s"' % esc(d[key]), m.group(0), count=1)
        return m.group(0)
    out = re.sub(r'(<[a-zA-Z0-9]+[^>]*\sdata-i18n-placeholder="([^"]+)"[^>]*>)', repl_ph, out)

    # data-i18n-alt
    def repl_alt(m):
        key = m.group(2)
        if key in d:
            return re.sub(r'alt="[^"]*"', 'alt="%s"' % esc(d[key]), m.group(0), count=1)
        return m.group(0)
    out = re.sub(r'(<[a-zA-Z0-9]+[^>]*\sdata-i18n-alt="([^"]+)"[^>]*>)', repl_alt, out)

    return out


def build_hreflang(rel_path):
    """rel_path: ''（英文首页）或 'zh' / 'es'"""
    tags = []
    for lg, prefix in LANGS.items():
        url = SITE + (prefix + "/" if prefix else "/")
        tags.append('    <link rel="alternate" hreflang="%s" href="%s">' % (lg, url))
    tags.append('    <link rel="alternate" hreflang="x-default" href="%s/">' % SITE)
    self_url = SITE + (("/" + rel_path + "/") if rel_path else "/")
    tags.append('    <link rel="canonical" href="%s">' % self_url)
    return "\n".join(tags)


def add_hreflang(html, rel_path):
    if 'hreflang=' in html:
        html = re.sub(r'\n\s*<link rel="alternate"[^>]*hreflang[^>]*>', '', html)
        html = re.sub(r'\n\s*<link rel="canonical"[^>]*>', '', html)
    return html.replace("</head>", "\n" + build_hreflang(rel_path) + "\n</head>", 1)


# --- 英文首页：只加 hreflang ---
en_html = add_hreflang(base_html, "")
with open(INDEX, "w", encoding="utf-8", newline="") as fh:
    fh.write(en_html)
print("index.html: 已加 hreflang ✓")

# --- 中文 / 西语首页 ---
for lang, folder in (("zh", "zh"), ("es", "es")):
    out = apply_translation(base_html, lang)

    # title
    if "pageTitle" in DICT[lang]:
        out = re.sub(r'<title>[^<]*</title>',
                     '<title>%s</title>' % esc(DICT[lang]["pageTitle"]), out, count=1)

    # meta description：字典里没有现成的描述，用首屏文案 heroDesc
    if "heroDesc" in DICT[lang]:
        out = re.sub(r'(<meta name="description" content=")[^"]*(")',
                     lambda m: m.group(1) + esc(DICT[lang]["heroDesc"]) + m.group(2),
                     out, count=1)

    # html lang
    out = re.sub(r'<html lang="[^"]*">', '<html lang="%s">' % lang, out, count=1)

    # 页面位于 /zh/ 或 /es/ 下，相对路径会被解析到 /zh/images/... 而 404
    # 统一改成以 / 开头的绝对路径
    def to_abs(m):
        attr, val = m.group(1), m.group(2)
        if val.startswith(("http://", "https://", "/", "#", "mailto:", "tel:",
                           "data:", "javascript:")):
            return m.group(0)
        return '%s="/%s"' % (attr, val)

    out = re.sub(r'(src|href|srcset)="([^"]+)"', to_abs, out)

    out = add_hreflang(out, folder)

    d = os.path.join(ROOT, folder)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="") as fh:
        fh.write(out)
    print("/%s/index.html 已生成 (%d KB)" % (folder, len(out.encode("utf-8")) // 1024))

print("\n完成：/ (en) · /zh/ (中文) · /es/ (西语) 三语互指 hreflang")
