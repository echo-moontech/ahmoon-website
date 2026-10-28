# -*- coding: utf-8 -*-
"""Generate HMDSO technical guide article, reusing kh-570 article style skeleton."""
import re, io

TPL = "articles/kh-570-methacryloxy-silane-technical-guide.html"
OUT = "articles/hmdso-hexamethyldisiloxane-technical-guide.html"
tpl = io.open(TPL, encoding="utf-8").read()

# --- extract reusable blocks ---
m = re.search(r"(    <style>.*?</style>)", tpl, re.S)
STYLE_MAIN = m.group(1)

m = re.search(r"(    <style>\s*\.rel-sec\{.*?</style>)", tpl, re.S)
REL_STYLE = m.group(1)

i = tpl.index("    <footer>")
TAIL = tpl[i:]  # footer + back-top + </body></html>

SLUG = "hmdso-hexamethyldisiloxane-technical-guide"
BASE = "https://moontechsilicone.com"

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HMDSO Hexamethyldisiloxane (CAS 107-46-0): Uses, Specs & Guide</title>
    <meta name="description" content="HMDSO (hexamethyldisiloxane, CAS 107-46-0) ≥99%: volatile end-capping agent for silicones, hydrophobic powder treatment and plasma coating precursor. 150 kg drums, COA per batch, free sample.">
    <meta name="keywords" content="HMDSO, hexamethyldisiloxane, CAS 107-46-0, MM siloxane, end-capping agent, silane blocking agent, plasma polymerization precursor, hydrophobic silica treatment, China manufacturer">
    <link rel="canonical" href="https://moontechsilicone.com/articles/hmdso-hexamethyldisiloxane-technical-guide">
    <link rel="alternate" hreflang="zh" href="https://moontechsilicone.com/zh/articles/hmdso-hexamethyldisiloxane-technical-guide">
    <link rel="alternate" hreflang="es" href="https://moontechsilicone.com/es/articles/hmdso-hexamethyldisiloxane-technical-guide">

    <!-- Open Graph -->
    <meta property="og:title" content="Hexamethyldisiloxane (HMDSO): End-Capping, Hydrophobic Treatment & Plasma Coating Guide">
    <meta property="og:description" content="Complete guide to HMDSO (hexamethyldisiloxane, CAS 107-46-0): chemistry, end-capping mechanism, plasma polymerization, HMDSO vs HMDS vs TMCS, specifications and packaging.">
    <meta property="og:url" content="https://moontechsilicone.com/articles/hmdso-hexamethyldisiloxane-technical-guide">
    <meta property="og:image" content="https://moontechsilicone.com/images/hmdso-batch.jpg">
    <meta property="og:type" content="article">

    <!-- Schema.org Article -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "Hexamethyldisiloxane (HMDSO, CAS 107-46-0): End-Capping, Hydrophobic Treatment and Plasma Coating Guide",
      "description": "MOON HMDSO is ≥99% hexamethyldisiloxane (CAS 107-46-0), the shortest siloxane chain (MM). A volatile, residue-free trimethylsilyl donor used as an end-capping agent for silicone polymers, a hydrophobic treatment for siliceous fillers and powders, and a widely used plasma polymerization (PECVD) precursor.",
      "author": {
        "@type": "Organization",
        "name": "Anhui Moon Technology Co., Ltd."
      },
      "publisher": {
        "@type": "Organization",
        "name": "Moon Technology",
        "url": "https://moontechsilicone.com"
      },
      "datePublished": "2026-10-28",
      "dateModified": "2026-10-28",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://moontechsilicone.com/articles/hmdso-hexamethyldisiloxane-technical-guide"
      }
    }
    </script>

    <!-- Schema.org FAQPage -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is HMDSO used for?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "HMDSO (hexamethyldisiloxane, CAS 107-46-0) is mainly used as an end-capping (blocking) agent for hydroxyl-terminated silicone polymers, as a hydrophobic surface treatment for silica, diatomite, talc and other siliceous fillers, as a cleaning and release agent, as a raw material for silazane production, and as a precursor for plasma polymerization (PECVD) coatings. It is also used in pharmaceutical synthesis, gas chromatography stationary phases and water-repellent treatments."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between HMDSO and HMDS?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "HMDSO is hexamethyldisiloxane (CAS 107-46-0): two trimethylsilyl groups bridged by oxygen. HMDS is hexamethyldisilazane (CAS 999-97-3): the same groups bridged by nitrogen. Both donate trimethylsilyl groups, but HMDS releases ammonia and is the stronger silylation reagent used for photoresist adhesion and pharmaceutical silylation, while HMDSO is neutral, volatile and residue-free — preferred for end-capping, cleaning, release applications and plasma coating. TMCS (trimethylchlorosilane, CAS 75-77-4) is the most reactive of the three but releases corrosive HCl."
          }
        },
        {
          "@type": "Question",
          "name": "Is HMDSO a dangerous good?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. HMDSO is classified as a Class 3 flammable liquid (H225: highly flammable liquid and vapour) with a flash point of 0°C. It must be transported and stored in accordance with flammable-liquid regulations, away from ignition sources. It is also classified as toxic to aquatic life, so releases to the environment must be avoided. We ship HMDSO worldwide in fully compliant DG packaging with complete transport documentation."
          }
        },
        {
          "@type": "Question",
          "name": "What purity and impurity control do you offer for HMDSO?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our specification is ≥99.0% HMDSO content with hydroxytrimethylsilane ≤1.0% and total chlorine ≤50 ppm. Typical production batches test at 99.9%+ purity with chloride around 18 μg/g and turbidity below 0.5 NTU. A batch-specific COA is issued with every shipment."
          }
        },
        {
          "@type": "Question",
          "name": "How is HMDSO packaged and stored?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Standard packaging is 150 kg net per 200 L iron drum with internal coating; plastic drums and custom packing are available on request. Store in the original sealed container in a ventilated, dry place away from open fire, heat and water. Shelf life is one year from the date of production; after that, re-inspection is required before use."
          }
        },
        {
          "@type": "Question",
          "name": "Can I get a free sample of HMDSO?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. We supply lab-evaluation samples together with TDS, MSDS and a batch COA so you can verify quality in your own application before committing to a commercial order. MOQ and factory-direct pricing are confirmed within 24 hours of inquiry."
          }
        }
      ]
    }
    </script>

"""

BODY = """    <div class="lang-bar">
        <div class="container">
            <a href="?lang=en" class="active">English</a>
            <a href="?lang=zh">中文</a>
            <a href="?lang=es">Español</a>
        </div>
    </div>

    <nav>
        <div class="container">
            <a href="/" class="logo">MOON<span>Tech</span></a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/products/">Products</a></li>
                <li><a href="/articles/">Articles</a></li>
                <li><a href="/#about">About</a></li>
                <li><a href="mailto:echo@ahmoontech.com" class="nav-cta">Get Quote</a></li>
            </ul>
        </div>
    </nav>

    <div class="breadcrumb">
        <div class="container">
            <a href="/">Home</a>
            <span>›</span>
            <a href="/articles/">Articles</a>
            <span>›</span>
            <span>Hexamethyldisiloxane (HMDSO) Technical Guide</span>
        </div>
    </div>

    <section class="article-hero">
        <div class="container">
            <div class="eyebrow">Technical Guide · Siloxane</div>
            <h1>Hexamethyldisiloxane (HMDSO, CAS 107-46-0): End-Capping, Hydrophobic Treatment &amp; Plasma Coating Guide</h1>
            <p class="subtitle">The shortest siloxane chain — MM. A volatile, residue-free trimethylsilyl donor that caps silicone polymers, renders fillers water-repellent and builds plasma coatings — without corrosive by-products.</p>
            <div class="article-meta">
                <span>📅 October 28, 2026</span>
                <span>📂 Silicone Rubber · Coatings · Pharma · Electronics</span>
                <span>⏱️ 8 min read</span>
            </div>
        </div>
    </section>

    <main class="article-body">
        <div class="container">
            <div class="article-content">

                <figure style="margin: 0 0 40px; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">
                    <img src="/images/hmdso-batch.webp" alt="MOON HMDSO hexamethyldisiloxane packed bottles ready for dispatch" width="1400" height="1049" style="width:100%; height:auto; display:block;">
                    <figcaption style="background:#1a3a2a; color:rgba(255,255,255,0.8); padding:10px 16px; font-size:13px; text-align:center;">MOON-brand HMDSO packed and ready for dispatch — Anhui Moon Technology Co., Ltd.</figcaption>
                </figure>

                <h2 id="what-it-is">What HMDSO Is and How It Works</h2>
                <p><strong>Hexamethyldisiloxane</strong> (HMDSO), often abbreviated <strong>MM</strong> in silicone nomenclature, is the simplest member of the siloxane family: two trimethylsilyl groups joined by a single oxygen bridge, (CH₃)₃Si–O–Si(CH₃)₃. It is produced industrially by the controlled dechlorination–condensation of trimethylchlorosilane (TMCS) with water.</p>
                <p>What makes it useful is what it <em>lacks</em>: there is no Si–H, no Si–OH and no Si–Cl in the molecule. It is chemically neutral, highly volatile (boiling point 101&nbsp;°C) and leaves no residue after evaporation. At the same time, the Si–O bonds are polarizable, so HMDSO readily delivers trimethylsilyl groups to active sites — capping silanol groups (Si–OH) on polymer chains, pigment and filler surfaces with a thin, extremely hydrophobic trimethylsilyl layer.</p>
                <p>That combination — <em>a clean, volatile trimethylsilyl donor with no corrosive by-products</em> — explains why HMDSO shows up everywhere from silicone rubber plants to plasma coating reactors and pharmaceutical synthesis.</p>

                <h2 id="specifications">Technical Specifications</h2>
                <div class="spec-table-wrap">
                    <table class="spec-table">
                        <tr><th>Chemical Name</th><td>Hexamethyldisiloxane (HMDSO, MM)</td></tr>
                        <tr><th>CAS Number</th><td>107-46-0</td></tr>
                        <tr><th>EC Number</th><td>203-492-7</td></tr>
                        <tr><th>Molecular Formula</th><td>C₆H₁₈OSi₂</td></tr>
                        <tr><th>Molecular Weight</th><td>162.38 g/mol</td></tr>
                        <tr><th>Appearance</th><td>Colorless transparent liquid, no visible impurities</td></tr>
                        <tr><th>HMDSO Content</th><td>≥ 99.0%</td></tr>
                        <tr><th>Hydroxytrimethylsilane Content</th><td>≤ 1.0%</td></tr>
                        <tr><th>Total Chlorine (Cl)</th><td>≤ 50 ppm</td></tr>
                        <tr><th>Density (20 °C)</th><td>0.764 g/mL</td></tr>
                        <tr><th>Boiling Point</th><td>101 °C</td></tr>
                        <tr><th>Flash Point</th><td>0 °C (closed cup) — Class 3 flammable liquid</td></tr>
                        <tr><th>Kinematic Viscosity (20 °C)</th><td>0.51 cSt</td></tr>
                        <tr><th>Water Solubility (25 °C)</th><td>0.93 mg/L (practically insoluble)</td></tr>
                        <tr><th>Log Kow</th><td>4.2</td></tr>
                        <tr><th>Vapour Pressure (25 °C)</th><td>≈ 42 mmHg</td></tr>
                        <tr><th>Packaging</th><td>150 kg net / 200 L internally-coated iron drum, or plastic drum on request</td></tr>
                    </table>
                </div>
                <p><strong>Typical batch quality</strong> (COA, lot 2023012002, 9,000 kg production batch): HMDSO content <strong>99.91%</strong>, total chlorine <strong>18 μg/g</strong>, turbidity <strong>0.33 NTU</strong> — comfortably inside the specification above. A batch-specific COA is issued with every shipment.</p>

                <h2 id="hmso-vs-hmds">HMDSO vs HMDS vs TMCS: Which Trimethylsilyl Donor?</h2>
                <p>HMDSO is one of three common trimethylsilyl donors, and buyers frequently mix them up. They are not interchangeable — the by-product each one releases determines where it can be used:</p>
                <div class="comparison-table-wrap">
                    <table class="comparison-table">
                        <tr><th></th><th>HMDSO<br>(hexamethyldisiloxane)</th><th>HMDS<br>(hexamethyldisilazane)</th><th>TMCS<br>(trimethylchlorosilane)</th></tr>
                        <tr><td>CAS Number</td><td>107-46-0</td><td>999-97-3</td><td>75-77-4</td></tr>
                        <tr><td>Bridge atom</td><td>Oxygen (Si–O–Si)</td><td>Nitrogen (Si–N–Si)</td><td>Chlorine (Si–Cl)</td></tr>
                        <tr><td>By-product released</td><td>Water / methanol — neutral</td><td>Ammonia</td><td>Hydrogen chloride — corrosive</td></tr>
                        <tr><td>Handling</td><td>Mild; flammable liquid only</td><td>Flammable; ammonia ventilation needed</td><td>Corrosive; fumes, acid scavenger required</td></tr>
                        <tr><td>Volatility / residue</td><td>Highly volatile, zero residue</td><td>Medium</td><td>Highly volatile, but HCl contamination risk</td></tr>
                        <tr><td>Typical role</td><td>End-capping, filler treatment, cleaning, release agent, plasma precursor</td><td>Strong silylation reagent, photoresist adhesion promoter, pharma synthesis</td><td>Most aggressive silylation where chloride is acceptable</td></tr>
                    </table>
                </div>
                <p><strong>Rule of thumb:</strong> if your process cannot tolerate corrosive or basic by-products — silicone polymer finishing, powder treatment, plasma work, precision cleaning — HMDSO is usually the right choice. If you need a stronger silylation reagent for drug intermediates or wafer priming, look at HMDS instead.</p>

                <h2 id="applications">Typical Applications</h2>
                <div class="app-grid">
                    <div class="app-card">
                        <h4>🔗 Silicone End-Capping (Blocking Agent)</h4>
                        <p>Caps the terminal silanol groups of hydroxyl-terminated PDMS in 107 rubber and silicone fluid production, precisely controlling molecular weight. Because excess HMDSO evaporates completely, the finished polymer contains no residual capping-agent contamination.</p>
                    </div>
                    <div class="app-card">
                        <h4>🧪 Hydrophobic Powder &amp; Filler Treatment</h4>
                        <p>Treats fumed and precipitated silica, diatomite, talc and kaolin: surface Si–OH groups are capped with trimethylsilyl groups, converting hydrophilic powders into free-flowing, water-repellent grades for coatings, sealants and rubber compounds.</p>
                    </div>
                    <div class="app-card">
                        <h4>💡 Plasma Polymerization (PECVD) Precursor</h4>
                        <p>HMDSO vapour polymerizes under low-pressure plasma into SiOCH organosilicon films; with an O₂ feed, the film shifts toward hard silica-like glassy coatings. Used for anti-scratch optical coatings, hydrophobic glass, barrier layers on polymers and biomedical surface modification.</p>
                    </div>
                    <div class="app-card">
                        <h4>🧴 Release &amp; Cleaning Agent</h4>
                        <p>Works as a mould release agent in rubber and plastics processing and as a precision cleaning / degreasing solvent in electronics, where complete evaporation without residue is essential.</p>
                    </div>
                    <div class="app-card">
                        <h4>💊 Pharmaceutical &amp; Analytical</h4>
                        <p>Used in pharmaceutical synthesis, as a gas-chromatography stationary phase (silicone type) and as an analytical reagent in laboratory practice.</p>
                    </div>
                    <div class="app-card">
                        <h4>🏭 Silazane Raw Material</h4>
                        <p>Serves as a feedstock for producing hexamethyldisilazane (HMDS) and polysilazane resins — the route to ceramic-forming coatings such as 9H hard coats.</p>
                    </div>
                </div>

                <figure style="margin: 0 0 40px; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">
                    <img src="/images/hmdso-app-rubber.webp" alt="HMDSO used in silicone rubber extrusion production" width="1280" height="1280" style="width:100%; height:auto; display:block;">
                    <figcaption style="background:#1a3a2a; color:rgba(255,255,255,0.8); padding:10px 16px; font-size:13px; text-align:center;">HMDSO is a standard end-capping agent in silicone rubber and elastomer production.</figcaption>
                </figure>

                <h2 id="how-to-use">How to Use It</h2>
                <p>The right process depends on the application, but three patterns cover most uses:</p>
                <ol>
                    <li><strong>End-capping of silicone polymers</strong> — dose HMDSO against the measured hydroxyl (Si–OH) content of the polymer: the capping ratio of MM to Si–OH determines the final molecular weight. Reaction proceeds with an acid or alkaline (e.g. KOH) catalyst at elevated temperature; afterwards, unreacted MM and volatile by-products are stripped off, and because HMDSO is fully volatile the stripping step leaves no residue in the polymer.</li>
                    <li><strong>Filler / powder surface treatment</strong> — apply HMDSO neat (vapour-phase or direct dosing in a mixer) or as a solution onto the siliceous filler, then heat at 100–120&nbsp;°C to complete the silylation reaction and remove volatiles. Dosage is governed by filler surface area; start with a small trial treating three loading levels to find the minimum dose that reaches the target hydrophobicity (methanol-wettable → water-repellent transition).</li>
                    <li><strong>Plasma deposition</strong> — feed HMDSO vapour with a carrier gas (Ar, N₂ or He) into a low-pressure RF plasma. A pure HMDSO plasma yields soft, polymer-like SiOCH films; adding O₂ increases in-film oxygen and produces harder, more silica-like, transparent coatings. Film properties are tuned through monomer flow, power and pressure — we can share starting parameter windows for your reactor geometry on request.</li>
                </ol>
                <p><strong>Safety note:</strong> HMDSO is a Class 3 flammable liquid with a flash point of 0&nbsp;°C. Ground and bond containers, use explosion-proof equipment and non-sparking tools, and prevent static discharge during transfer. Avoid release to the environment — it is classified as toxic to aquatic life.</p>

                <figure style="margin: 0 0 40px; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">
                    <img src="/images/hmdso-app-plasma.webp" alt="HMDSO as precursor for plasma coating and electronics treatment" width="1280" height="1280" style="width:100%; height:auto; display:block;">
                    <figcaption style="background:#1a3a2a; color:rgba(255,255,255,0.8); padding:10px 16px; font-size:13px; text-align:center;">HMDSO plasma coatings protect electronics, optics and precision components.</figcaption>
                </figure>

                <div class="cta-inline">
                    <h3>Matching HMDSO to Your Process?</h3>
                    <p>Tell us your application — end-capping, powder treatment or plasma coating — and our technical team will recommend the right grade, dosage approach and documentation package.</p>
                    <a href="mailto:echo@ahmoontech.com?subject=HMDSO Technical Consultation" class="cta-btn">📩 Ask Our Technical Team</a>
                </div>

                <h2 id="packaging">Packaging, Quality &amp; Lead Time</h2>
                <ul>
                    <li><strong>Packaging:</strong> 150 kg net per 200 L internally-coated iron drum · plastic drum on request · custom packing available</li>
                    <li><strong>Batch Testing:</strong> content, total chlorine and turbidity checked against internal Q/LXAXJM standards; COA issued per batch</li>
                    <li><strong>Documentation:</strong> TDS and MSDS (UN GHS rev. 8) supplied with every order; batch COA on request</li>
                    <li><strong>Regulatory:</strong> listed on EINECS, TSCA, IECSC, KECL, NZIoC, PICCS and the Vietnam chemical inventory</li>
                    <li><strong>Transport:</strong> Class 3 flammable liquid — shipped in fully compliant DG packaging with complete transport documentation</li>
                    <li><strong>Storage:</strong> original sealed container, ventilated and dry, away from open fire, heat and water; protect from sunshine and rain. Shelf life 1 year from production date; re-inspect before use after that period.</li>
                    <li><strong>MOQ &amp; Samples:</strong> factory-direct pricing and MOQ confirmed within 24 h; lab-evaluation samples available with TDS / MSDS / COA</li>
                </ul>

                <h2 id="faq">Frequently Asked Questions</h2>

                <div class="faq-item">
                    <div class="faq-q">Q: What is HMDSO used for?</div>
                    <div class="faq-a">HMDSO is mainly used as an end-capping (blocking) agent for hydroxyl-terminated silicone polymers, as a hydrophobic surface treatment for silica, diatomite, talc and other siliceous fillers, as a cleaning and release agent, as a raw material for silazane production, and as a precursor for plasma polymerization (PECVD) coatings. It is also used in pharmaceutical synthesis, GC stationary phases and water-repellent treatments.</div>
                </div>

                <div class="faq-item">
                    <div class="faq-q">Q: What is the difference between HMDSO and HMDS?</div>
                    <div class="faq-a">HMDSO is hexamethyldisiloxane (CAS 107-46-0) — two trimethylsilyl groups bridged by oxygen. HMDS is hexamethyldisilazane (CAS 999-97-3) — the same groups bridged by nitrogen. HMDS releases ammonia and is the stronger silylation reagent (photoresist priming, pharma synthesis); HMDSO is neutral, volatile and residue-free, preferred for end-capping, cleaning, release and plasma work. TMCS (CAS 75-77-4) is the most reactive of the three but releases corrosive HCl.</div>
                </div>

                <div class="faq-item">
                    <div class="faq-q">Q: Is HMDSO a dangerous good?</div>
                    <div class="faq-a">Yes — Class 3 flammable liquid (H225), flash point 0°C. It must be transported and stored under flammable-liquid regulations, away from ignition sources, using grounded and bonded equipment. It is also toxic to aquatic life, so environmental release must be avoided. We ship worldwide in compliant DG packaging with full documentation.</div>
                </div>

                <div class="faq-item">
                    <div class="faq-q">Q: What purity and impurity control do you offer?</div>
                    <div class="faq-a">Specification: ≥99.0% HMDSO, hydroxytrimethylsilane ≤1.0%, total chlorine ≤50 ppm. Typical batches test at 99.9%+ purity with chloride around 18 μg/g and turbidity below 0.5 NTU. A batch-specific COA accompanies every shipment.</div>
                </div>

                <div class="faq-item">
                    <div class="faq-q">Q: How is HMDSO packaged and stored?</div>
                    <div class="faq-a">Standard packing is 150 kg net per 200 L internally-coated iron drum; plastic drums and custom packing are available. Store sealed, in a ventilated dry place away from fire, heat and water. Shelf life is one year from production; re-inspect before use afterwards.</div>
                </div>

                <div class="faq-item">
                    <div class="faq-q">Q: Can I get a free sample of HMDSO?</div>
                    <div class="faq-a">Yes. We supply lab-evaluation samples with TDS, MSDS and batch COA so you can verify quality in your own application first. MOQ and factory-direct pricing are confirmed within 24 hours of inquiry.</div>
                </div>

                <!-- Final CTA -->
                <div class="cta-inline">
                    <h3>Ready to Source HMDSO from the Factory?</h3>
                    <p>Request the TDS, MSDS, COA and a sample — we will confirm pricing, DG packaging and lead time within 24 hours.</p>
                    <a href="mailto:echo@ahmoontech.com?subject=HMDSO TDS and Sample Request" class="cta-btn">📩 Request TDS &amp; Sample</a>
                </div>

            </div>
        </div>
    </main>

""" + REL_STYLE + """

    <section class="rel-sec">
        <div class="container">
            <h2 class="rel-h2">Related Products &amp; Guides</h2>
            <p class="rel-sub">Continue exploring the Moon Tech silicone portfolio</p>
            <div class="rel-grid">
                <a class="rel-card" href="/products/hmds">
                    <span class="rel-t">HMDSO Product Page</span>
                    <span class="rel-d">MOON HMDSO ≥99%, CAS 107-46-0</span>
                    <span class="rel-a">View product →</span>
                </a>
                <a class="rel-card" href="/articles/how-to-use-silane-coupling-agents">
                    <span class="rel-t">How to Use Silane Coupling Agents</span>
                    <span class="rel-d">4 methods &amp; dosage guidelines</span>
                    <span class="rel-a">Read guide →</span>
                </a>
                <a class="rel-card" href="/products/opsz9150">
                    <span class="rel-t">OPSZ9150 Polysilazane</span>
                    <span class="rel-d">Ceramic-forming resin for 9H hard coatings</span>
                    <span class="rel-a">View product →</span>
                </a>
                <a class="rel-card" href="/products/dimethyl-silicone-oil">
                    <span class="rel-t">Dimethyl Silicone Oil</span>
                    <span class="rel-d">End-capped PDMS fluids, 50–10,000 cSt</span>
                    <span class="rel-a">View product →</span>
                </a>
            </div>
        </div>
    </section>

"""

html = HEAD + STYLE_MAIN + "\n\n" + BODY + TAIL
io.open(OUT, "w", encoding="utf-8", newline="\n").write(html)
print("written", OUT, len(html), "bytes")

# sanity: ensure all key markers exist
for marker in ["hmdso-batch.webp", "hmdso-app-rubber.webp", "hmdso-app-plasma.webp",
               "107-46-0", "rel-sec", "</html>", "FAQPage", "spec-table", "faq-item"]:
    assert marker in html, marker
print("markers OK")
