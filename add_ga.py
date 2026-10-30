import glob, re

TAG_ID = "G-XQMVFP9P2R"
SNIPPET = """    <!-- Google tag (gtag.js) - Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', '%s');
    </script>
""" % (TAG_ID, TAG_ID)

files = glob.glob("**/*.html", recursive=True)
added, skipped = [], []
for f in files:
    html = open(f, encoding="utf-8").read()
    if TAG_ID in html:
        skipped.append(f)
        continue
    if "</title>" in html:
        html = html.replace("</title>", "</title>\n" + SNIPPET.rstrip(), 1)
    elif "</head>" in html:
        html = html.replace("</head>", SNIPPET + "</head>", 1)
    else:
        continue
    open(f, "w", encoding="utf-8", newline="").write(html)
    added.append(f)

print("added:", len(added))
for f in added: print("  +", f)
print("already had:", skipped)
