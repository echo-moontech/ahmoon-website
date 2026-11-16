# -*- coding: utf-8 -*-
"""Give every silicone-oil product page a link to its technical guide.
Weight flow: product pages (highest traffic) ->深文章.
"""
import io, os, re

BASE = os.path.dirname(os.path.abspath(__file__))

LINKS = {
    "D5.html": (
        "Decamethylcyclopentasiloxane (D5) Technical Guide",
        "CAS 541-02-6 &middot; specification table &middot; real batch COA (99.97% purity, D4 29 ppm) &middot; dosage per application &middot; EU wash-off restriction notes",
        "/articles/d5-decamethylcyclopentasiloxane-technical-guide",
    ),
    "methyl-phenyl-silicone-oil.html": (
        "Phenyl Methyl Silicone Oil Technical Guide",
        "250-30 / 255 grades &middot; diffusion-pump fluids 274 / 275 (vacuum to 6.65E-8 Pa) &middot; real batch COA &middot; Dow Corning &amp; Shin-Etsu equivalents",
        "/articles/phenyl-methyl-silicone-oil-technical-guide",
    ),
    "dimethyl-silicone-oil.html": (
        "Silicone Oil 201 / 107 / Vinyl Technical Guide",
        "201 and 107 PDMS grades, vinyl-terminated series &middot; end-group chemistry &middot; how to read a batch COA &middot; viscosity selection",
        "/articles/silicone-oil-201-107-vinyl-technical-guide",
    ),
    "vinyl-silicone-oil.html": (
        "Vinyl Silicone Oil &amp; 201 / 107 Technical Guide",
        "Vinyl-terminated PDMS end-group chemistry, vinyl content and batch COA &middot; part of our full silicone-oil selection guide",
        "/articles/silicone-oil-201-107-vinyl-technical-guide",
    ),
}

BLOCK = """    <section class="rel-sec" style="background:#fff;">
        <div class="container">
            <h2 class="rel-h2">Technical Guide</h2>
            <p class="rel-sub">Specifications, batch COA data, dosage and handling &mdash; the detail behind the datasheet.</p>
            <a class="rel-card" href="{href}" style="max-width:780px;">
                <span class="rel-t">{title}</span>
                <span class="rel-d">{desc}</span>
                <span class="rel-a">Read the technical guide &rarr;</span>
            </a>
        </div>
    </section>

"""

for fn, (title, desc, href) in LINKS.items():
    path = os.path.join(BASE, "products", fn)
    with io.open(path, encoding="utf-8") as f:
        html = f.read()
    if "Read the technical guide" in html:
        print("skip (already has guide):", fn)
        continue
    if '<section class="rel-sec">' not in html:
        print("!! no rel-sec anchor:", fn)
        continue
    block = BLOCK.format(title=title, desc=desc, href=href)
    html = html.replace('<section class="rel-sec">', block + '<section class="rel-sec">', 1)
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("ok:", fn)
