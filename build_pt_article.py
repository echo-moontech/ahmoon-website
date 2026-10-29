# -*- coding: utf-8 -*-
"""Generate Karstedt platinum catalyst technical guide, reusing hmdso article style skeleton."""
import re, io

TPL = "articles/hmdso-hexamethyldisiloxane-technical-guide.html"
OUT = "articles/karstedt-platinum-catalyst-technical-guide.html"
tpl = io.open(TPL, encoding="utf-8").read()

# --- extract reusable blocks ---
m = re.search(r"(    <style>.*?</style>)", tpl, re.S)
STYLE_MAIN = m.group(1)

m = re.search(r"(    <style>\s*\.rel-sec\{.*?</style>)", tpl, re.S)
REL_STYLE = m.group(1)

i = tpl.index("    <footer>")
TAIL = tpl[i:]  # footer + back-top + </body></html>

SLUG = "karstedt-platinum-catalyst-technical-guide"
BASE = "https://moontechsilicone.com"

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Karstedt Catalyst (CAS 68478-92-2): Hydrosilylation Guide, Specs &amp; Dosage</title>
    <meta name="description" content="Karstedt catalyst (Pt(0)-divinyltetramethyldisiloxane, CAS 68478-92-2): 500&ndash;10000 ppm Pt grades for LSR, RTV-2, HTV &amp; addition-cure silicones. Activity data, poisoning guide, COA per batch, free sample.">
    <meta name="keywords" content="Karstedt catalyst, platinum catalyst, platinum(0)-1,3-divinyl-1,1,3,3-tetramethyldisiloxane, CAS 68478-92-2, hydrosilylation catalyst, platinum silicone catalyst, LSR catalyst, RTV-2 curing, addition cure silicone, China manufacturer">
    <link rel="canonical" href="https://moontechsilicone.com/articles/karstedt-platinum-catalyst-technical-guide">
    <link rel="alternate" hreflang="zh" href="https://moontechsilicone.com/zh/articles/karstedt-platinum-catalyst-technical-guide">
    <link rel="alternate" hreflang="es" href="https://moontechsilicone.com/es/articles/karstedt-platinum-catalyst-technical-guide">

    <!-- Open Graph -->
    <meta property="og:title" content="Karstedt Catalyst: The Platinum Hydrosilylation Catalyst Behind Addition-Cure Silicones">
    <meta property="og:description" content="Complete guide to Karstedt catalyst (CAS 68478-92-2): hydrosilylation mechanism, activity &amp; inhibition, catalyst poisoning, Pt concentration selection, specifications and packaging.">
    <meta property="og:url" content="https://moontechsilicone.com/articles/karstedt-platinum-catalyst-technical-guide">
    <meta property="og:image" content="https://moontechsilicone.com/images/pt8000-app-factory.jpg">
    <meta property="og:type" content="article">

    <!-- Schema.org Article -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "Karstedt Catalyst (Platinum(0)-DVTMDS, CAS 68478-92-2): Hydrosilylation Guide, Specs and Dosage",
      "description": "MOON Karstedt catalyst is Platinum(0)-1,3-divinyl-1,1,3,3-tetramethyldisiloxane (CAS 68478-92-2), supplied at 500&ndash;10000 ppm Pt in vinyl-terminated PDMS. The industry-standard hydrosilylation catalyst for addition-cure silicones: LSR, RTV-2, HTV, potting compounds and silicone coatings.",
      "author": {
        "@type": "Organization",
        "name": "Anhui Moon Technology Co., Ltd."
      },
      "publisher": {
        "@type": "Organization",
        "name": "Moon Technology",
        "url": "https://moontechsilicone.com"
      },
      "datePublished": "2026-10-29",
      "dateModified": "2026-10-29",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://moontechsilicone.com/articles/karstedt-platinum-catalyst-technical-guide"
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
          "name": "What is Karstedt catalyst?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Karstedt catalyst is platinum(0)-1,3-divinyl-1,1,3,3-tetramethyldisiloxane (CAS 68478-92-2), a Pt(0) complex dissolved in a vinyl-terminated siloxane carrier. It is the industry-standard catalyst for hydrosilylation (addition-cure) of silicones: it catalyzes the addition of Si-H groups across vinyl (C=C) groups to form Si-C bonds with no by-products. It is used in LSR, RTV-2, HTV molding and extrusion, potting compounds, silicone coatings and release coatings."
          }
        },
        {
          "@type": "Question",
          "name": "How much platinum catalyst should I add to silicone?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Catalyst level is usually expressed as ppm of platinum metal relative to the total formulation. Typical hydrosilylation systems run in the single-digit to tens-of-ppm Pt range, adjusted with an inhibitor to balance pot life and cure speed. As a worked example: adding 1 phr of an 8000 ppm (0.8% Pt) catalyst to a 100-part formulation contributes roughly 79 ppm Pt. We help customers select the concentration and dosage for their resin, filler loading and cure profile."
          }
        },
        {
          "@type": "Question",
          "name": "Why did my platinum catalyst stop working (cure inhibition)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Platinum catalysts are highly sensitive to poisons. Common inhibitors include amines, organotin (condensation-cure catalysts), sulfur and polysulfides, phosphorus compounds, tin-containing silicone sealants, some flame retardants, and residues from rubber cups, latex gloves or sulfur-containing tooling. Contaminated batches typically show delayed surface cure or tacky surfaces. Use clean tooling, segregate addition-cure from condensation-cure lines, and verify fillers are platinum-safe."
          }
        },
        {
          "@type": "Question",
          "name": "What Pt concentrations are available?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "We regularly supply 500, 1000, 2000, 3000, 4000, 5000, 6000, 8000 and 10000 ppm Pt grades dissolved in vinyl-terminated polydimethylsiloxane, and can customize any platinum content up to 200000 ppm concentrate. All grades are made from the same certified Pt(0) complex (assay &ge;20% active content), so activity is consistent across concentrations."
          }
        },
        {
          "@type": "Question",
          "name": "How should Karstedt catalyst be stored?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Store sealed in the dark at 20&ndash;30&deg;C for up to 12 months; catalytic activity and appearance remain unchanged. Protect from contamination with sulfur, phosphorus, amines and organotin compounds. The product has a flash point around 30&deg;C, so keep it away from ignition sources and store as a flammable liquid. For cold-climate shipments we include heat packs to keep the product above 10&deg;C."
          }
        },
        {
          "@type": "Question",
          "name": "Can I get a sample and COA of the platinum catalyst?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. We supply lab-evaluation samples with TDS, MSDS and a batch-specific COA (appearance, viscosity, T10 activity, RoHS compliance). Factory-direct pricing and MOQ are confirmed within 24 hours of inquiry, and we can match your required Pt concentration."
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
            <span>Karstedt Platinum Catalyst Technical Guide</span>
        </div>
    </div>

    <section class="article-hero">
        <div class="container">
            <div class="eyebrow">Technical Guide · Platinum Catalyst</div>
            <h1>Karstedt Catalyst (CAS 68478-92-2): The Platinum Hydrosilylation Catalyst Behind Addition-Cure Silicones</h1>
            <p class="subtitle">Platinum(0)-1,3-divinyl-1,1,3,3-tetramethyldisiloxane — the industry-standard catalyst that turns vinyl + Si–H into cross-linked silicone with zero by-products. Activity, inhibition, poisoning, Pt concentration selection and dosing, explained.</p>
            <div class="article-meta">
                <span>📅 October 29, 2026</span>
                <span>📂 LSR · RTV-2 · HTV · Potting &amp; Coating</span>
                <span>⏱️ 9 min read</span>
            </div>
        </div>
    </section>

    <main class="article-body">
        <div class="container">
            <div class="article-content">

                <figure style="margin: 0 0 40px; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">
                    <img src="/images/pt8000-app-factory.webp" alt="MOON Karstedt platinum catalyst 8000ppm bottle in a silicone production plant" width="1400" height="945" style="width:100%; height:auto; display:block;">
                    <figcaption style="background:#1a3a2a; color:rgba(255,255,255,0.8); padding:10px 16px; font-size:13px; text-align:center;">MOON-brand Karstedt platinum catalyst, 8000 ppm Pt grade — Anhui Moon Technology Co., Ltd.</figcaption>
                </figure>

                <h2 id="what-it-is">What Karstedt Catalyst Is</h2>
                <p><strong>Karstedt's catalyst</strong> is platinum(0)-1,3-divinyl-1,1,3,3-tetramethyldisiloxane (CAS 68478-92-2, EC 270-844-4, molecular weight 381.48 g/mol) — a Pt(0) complex in which the platinum atom is chelated by the two vinyl groups of a divinyltetramethyldisiloxane ligand. First described by Bruce Karstedt at General Electric in the 1970s, it has since become <em>the</em> default catalyst for silicone hydrosilylation worldwide.</p>
                <p>Commercially, it is not sold as the bare complex but as a <strong>solution in vinyl-terminated polydimethylsiloxane (VT-PDMS)</strong>, at a defined platinum concentration — typically 500 to 10,000 ppm Pt for ready-to-use grades, and up to 200,000 ppm for concentrate used in compounding. The vinyl-functional carrier is fully compatible with silicone formulations and keeps the catalyst stable and homogeneous.</p>
                <p>Why platinum? Because no other industrial catalyst can match its selectivity and activity for the reaction that defines addition-cure silicones: <strong>hydrosilylation</strong> — the addition of a Si–H bond across a carbon–carbon double bond to form a stable Si–C bond.</p>

                <h2 id="mechanism">How It Works: The Hydrosilylation Reaction</h2>
                <p>Addition-cure silicone chemistry combines two components:</p>
                <ul>
                    <li>a <strong>vinyl-functional</strong> siloxane (vinyl silicone oil, vinyl rubber, LSR base polymer), and</li>
                    <li>a <strong>hydrogen-functional</strong> crosslinker (hydrogen silicone oil, Si–H).</li>
                </ul>
                <p>Neither reacts on its own at room temperature in any useful timeframe. The Karstedt complex activates the Si–H bond through the classical Chalk–Harrod mechanism: oxidative addition of Si–H to Pt(0), coordination and insertion of the vinyl group, then reductive elimination to form the new Si–C bond. The net reaction is:</p>
                <p style="text-align:center; font-weight:600; background:rgba(10,58,74,0.06); border-radius:8px; padding:14px;">Si–H + CH₂=CH–Si ⇒ Si–CH₂–CH₂–Si &nbsp;(no by-products)</p>
                <p>Three consequences follow, and they are the reason addition-cure silicones dominate precision applications:</p>
                <ol>
                    <li><strong>Zero by-products</strong> — unlike condensation cure (which releases alcohol or acetic acid), nothing volatilizes off. Shrinkage is minimal, and thick sections cure through without bubbles.</li>
                    <li><strong>Depth-independent cure</strong> — the reaction is chemical, not moisture-driven, so 50 mm castings cure as fast at the core as at the surface.</li>
                    <li><strong>Heat-accelerated</strong> — with the right inhibitor package, the mix is stable for hours at 25&nbsp;°C yet gels in minutes at 100–120&nbsp;°C. That is the whole basis of LSR injection molding.</li>
                </ol>

                <figure style="margin: 0 0 40px; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">
                    <img src="/images/pt8000-app-tubes.webp" alt="Karstedt platinum catalyst used in silicone tube extrusion and molded parts production" width="1400" height="945" style="width:100%; height:auto; display:block;">
                    <figcaption style="background:#1a3a2a; color:rgba(255,255,255,0.8); padding:10px 16px; font-size:13px; text-align:center;">Karstedt catalyst vulcanizes extruded silicone tubing and molded elastomer parts.</figcaption>
                </figure>

                <h2 id="activity">Activity: How Cure Speed Is Measured</h2>
                <p>Two numbers from our specification describe real production behavior:</p>
                <ul>
                    <li><strong>Room-temperature activity (25&nbsp;°C thickening time): ≤ 10 minutes.</strong> After the catalyst and inhibitor are balanced, a catalyzed mix begins to thicken within this window — long enough to process, short enough to know the catalyst is alive.</li>
                    <li><strong>High-temperature activity (120&nbsp;°C × 25 min): entirely cured.</strong> A standard test coupon cures completely, confirming full crosslinking capability.</li>
                </ul>
                <p>Formulators more commonly track <strong>T10 activity</strong> — the time for viscosity to start rising in a defined test. A fresh batch of our PT5000 grade recently tested at <strong>T10 = 81 s against a ≤ 100 s specification</strong> (batch COA, May 2024), comfortably inside spec. A batch-specific COA with appearance, viscosity and T10 activity is issued with every shipment.</p>

                <h2 id="specifications">Technical Specifications</h2>
                <div class="spec-table-wrap">
                    <table class="spec-table">
                        <tr><th>Chemical Name</th><td>Platinum(0)-1,3-divinyl-1,1,3,3-tetramethyldisiloxane (Karstedt's catalyst)</td></tr>
                        <tr><th>CAS Number</th><td>68478-92-2</td></tr>
                        <tr><th>EC / EINECS Number</th><td>270-844-4</td></tr>
                        <tr><th>Molecular Weight</th><td>381.48 g/mol</td></tr>
                        <tr><th>Appearance</th><td>Light yellow to colorless transparent liquid</td></tr>
                        <tr><th>Active Content (Pt complex)</th><td>≥ 20% (concentrate); diluted grades 500–10000 ppm Pt in VT-PDMS</td></tr>
                        <tr><th>Specific Gravity (25 °C)</th><td>0.984 g/mL (concentrate)</td></tr>
                        <tr><th>Melting Point</th><td>12–13 °C</td></tr>
                        <tr><th>Boiling Point</th><td>138 °C</td></tr>
                        <tr><th>Flash Point</th><td>30 °C — handle as flammable liquid</td></tr>
                        <tr><th>Room-Temp Activity (25 °C)</th><td>Thickening within ≤ 10 min</td></tr>
                        <tr><th>High-Temp Activity (120 °C × 25 min)</th><td>Entirely cured</td></tr>
                        <tr><th>Pt Concentration Menu</th><td>500 / 1000 / 2000 / 3000 / 4000 / 5000 / 6000 / 8000 / 10000 ppm; 20000–200000 ppm concentrate on request</td></tr>
                        <tr><th>Storage</th><td>Sealed, 20–30 °C, dark place; 12 months shelf life</td></tr>
                    </table>
                </div>
                <p><strong>Typical batch quality</strong> (COA, lot 24051101, PT5000 grade): appearance <strong>conforms</strong>, kinematic viscosity (25&nbsp;°C) <strong>271 mPa·s</strong> (spec 100–500), T10 activity <strong>81 s</strong> (spec ≤ 100 s), RoHS <strong>compliant</strong>. We can customize any platinum content to your requirement.</p>

                <h2 id="concentration">Choosing the Right Pt Concentration &amp; Dosing</h2>
                <p>Catalyst level is almost always quoted as <strong>ppm of platinum metal relative to the total formulation</strong> — not as ppm of the catalyst solution. Converting is simple arithmetic:</p>
                <ol>
                    <li>Read the Pt concentration off the grade: 8000 ppm = 0.8% Pt by weight.</li>
                    <li>Dose by phr (parts per hundred rubber). Adding <strong>1 phr of an 8000 ppm catalyst</strong> to a 100-part formulation contributes 0.8 ÷ 101 × 100 ≈ <strong>79 ppm Pt</strong> in the cured mix.</li>
                    <li>Adjust upward for faster cure or thicker sections; adjust downward when inhibition risk is high or optical clarity matters.</li>
                </ol>
                <p><strong>Which grade to stock?</strong> A practical rule: choose one concentration and vary the phr, rather than stocking many concentrations. 5000–8000 ppm grades give comfortable dosing accuracy for most LSR, RTV-2 and potting work; 10000+ ppm suits high-speed molding; lower grades (500–2000 ppm) are easier to meter in sensitive optical or coating systems. Every concentration is prepared from the same certified Pt(0) complex, so activity is consistent across the menu.</p>

                <h2 id="applications">Typical Applications</h2>
                <div class="app-grid">
                    <div class="app-card">
                        <h4>🏭 HTV / Extrusion Vulcanizing</h4>
                        <p>Vulcanizing agent and catalyst for mixing-molding rubber, silicone tube extrusion and pacifier (nipple) grade compounds — addition-cure HTV cures fast with no peroxide by-products or post-cure odors.</p>
                    </div>
                    <div class="app-card">
                        <h4>🧴 Addition-Cure Potting &amp; Molding</h4>
                        <p>Pouring sealants, silicone sheeting, mold-making rubbers, RTV-2 systems, silicone gel inks and silicone resins — deep-section cure with zero shrinkage by-products makes Karstedt-catalyzed systems the default for electronics potting.</p>
                    </div>
                    <div class="app-card">
                        <h4>🧪 Modified Silicone Oil Synthesis</h4>
                        <p>Catalyst for hydrosilylation synthesis of modified polyether silicone oils and amino silicone oils — grafting PEG chains and amine functionality onto PDMS backbones for surfactants, textiles and personal care.</p>
                    </div>
                    <div class="app-card">
                        <h4>🎨 Coatings &amp; Defoamers</h4>
                        <p>Used as an auxiliary in polyurethane coatings, silicone coatings and antifoam formulations where Si–H / vinyl systems need controlled, catalyzed crosslinking.</p>
                    </div>
                </div>

                <h2 id="poisoning">Cure Inhibition: The Poisons That Kill Platinum</h2>
                <p>Karstedt catalyst is extraordinarily sensitive to trace contaminants. A batch that cures slowly, shows tacky surfaces or never gels is almost always <strong>poisoned</strong>, not under-dosed. The usual suspects:</p>
                <ul>
                    <li><strong>Amines</strong> — amine-containing additives, some epoxy hardeners, amine odors from nearby processes</li>
                    <li><strong>Organotin compounds</strong> — the dibutyltin / dioctyltin catalysts used in <em>condensation-cure</em> RTV-1; never share tooling between the two cure systems</li>
                    <li><strong>Sulfur &amp; polysulfides</strong> — sulfur-vulcanized rubber tooling, some gaskets, latex gloves</li>
                    <li><strong>Phosphorus compounds</strong> — certain flame retardants and plasticizers</li>
                    <li><strong>Unverified fillers</strong> — precipitated silica or pigments with residual amine or sulfur surface treatment</li>
                </ul>
                <p><strong>Prevention checklist:</strong> dedicated mixing equipment for addition-cure lines; platinum-safe fillers with COA; nitrile (not latex) gloves; separate curing ovens from condensation-cure production; and when in doubt, run a small inhibition test before committing a production batch. We provide inhibition-test guidance with every catalyst order.</p>

                <div class="cta-inline">
                    <h3>Selecting a Pt Grade for Your System?</h3>
                    <p>Tell us your polymer system, filler loading and cure profile — our technical team will recommend the concentration, inhibitor approach and dosage window, backed by batch COA data.</p>
                    <a href="mailto:echo@ahmoontech.com?subject=Karstedt Catalyst Technical Consultation" class="cta-btn">📩 Ask Our Technical Team</a>
                </div>

                <h2 id="packaging">Packaging, Storage &amp; Handling</h2>
                <ul>
                    <li><strong>Packaging:</strong> 1 kg / 5 kg / 20 kg / 50 kg pails; custom packaging available</li>
                    <li><strong>Storage:</strong> sealed, 20–30&nbsp;°C, dark place — 12 months with catalytic activity and appearance unchanged</li>
                    <li><strong>Flammability:</strong> flash point ≈ 30&nbsp;°C — store and transport as a flammable liquid, away from ignition sources</li>
                    <li><strong>Cold-weather shipping:</strong> heat packs included for shipments below 10&nbsp;°C; freezing does not irreversibly damage the product but cold liquid is harder to meter accurately</li>
                    <li><strong>Documentation:</strong> TDS and MSDS with every order; batch COA (appearance, viscosity, T10 activity, RoHS) per shipment</li>
                    <li><strong>MOQ &amp; Samples:</strong> factory-direct pricing and MOQ confirmed within 24 h; lab samples with COA available</li>
                </ul>

                <h2 id="faq">Frequently Asked Questions</h2>

                <div class="faq-item">
                    <div class="faq-q">Q: What is Karstedt catalyst?</div>
                    <div class="faq-a">Karstedt catalyst is platinum(0)-1,3-divinyl-1,1,3,3-tetramethyldisiloxane (CAS 68478-92-2), a Pt(0) complex in a vinyl-terminated siloxane carrier. It is the industry-standard catalyst for hydrosilylation (addition-cure) of silicones, catalyzing Si–H addition across vinyl groups with no by-products. It is used in LSR, RTV-2, HTV molding and extrusion, potting compounds, silicone coatings and release coatings.</div>
                </div>

                <div class="faq-item">
                    <div class="faq-q">Q: How much platinum catalyst should I add?</div>
                    <div class="faq-a">Catalyst level is quoted as ppm of platinum metal relative to the total formulation; typical hydrosilylation systems run in the single-digit to tens-of-ppm Pt range with an inhibitor balancing pot life and cure speed. Worked example: 1 phr of an 8000 ppm (0.8% Pt) catalyst in a 100-part formulation ≈ 79 ppm Pt. We help you select concentration and dosage for your system.</div>
                </div>

                <div class="faq-item">
                    <div class="faq-q">Q: Why did my catalyst stop working (no cure)?</div>
                    <div class="faq-a">Platinum is poisoned by traces of amines, organotin (condensation-cure catalysts), sulfur and polysulfides, phosphorus compounds and contaminated fillers — symptoms are delayed cure or tacky surfaces. Use clean dedicated tooling, segregate addition-cure from condensation-cure lines, verify fillers are platinum-safe, and run an inhibition test when in doubt.</div>
                </div>

                <div class="faq-item">
                    <div class="faq-q">Q: What Pt concentrations are available?</div>
                    <div class="faq-a">Standard grades: 500, 1000, 2000, 3000, 4000, 5000, 6000, 8000 and 10000 ppm Pt in vinyl-terminated PDMS; any content up to 200000 ppm concentrate can be customized. All grades derive from the same certified Pt(0) complex (assay ≥20%), so activity is consistent across concentrations.</div>
                </div>

                <div class="faq-item">
                    <div class="faq-q">Q: How should Karstedt catalyst be stored?</div>
                    <div class="faq-a">Sealed in the dark at 20–30°C for up to 12 months — activity and appearance stay unchanged. Keep away from sulfur, phosphorus, amine and organotin contamination. Flash point is around 30°C, so store as a flammable liquid away from ignition sources. Cold-climate shipments include heat packs.</div>
                </div>

                <div class="faq-item">
                    <div class="faq-q">Q: Can I get a sample and COA?</div>
                    <div class="faq-a">Yes. Lab-evaluation samples ship with TDS, MSDS and a batch-specific COA (appearance, viscosity, T10 activity, RoHS). Factory-direct pricing and MOQ are confirmed within 24 hours, and we can match your required Pt concentration.</div>
                </div>

                <!-- Final CTA -->
                <div class="cta-inline">
                    <h3>Ready to Source Karstedt Catalyst from the Factory?</h3>
                    <p>Request the TDS, MSDS, batch COA and a sample — we will confirm pricing, Pt concentration and lead time within 24 hours.</p>
                    <a href="mailto:echo@ahmoontech.com?subject=Karstedt Catalyst TDS and Sample Request" class="cta-btn">📩 Request TDS &amp; Sample</a>
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
                <a class="rel-card" href="/products/platinum-catalyst">
                    <span class="rel-t">Karstedt Catalyst Product Page</span>
                    <span class="rel-d">Pt(0) hydrosilylation catalyst, 500–10000 ppm</span>
                    <span class="rel-a">View product →</span>
                </a>
                <a class="rel-card" href="/articles/hmdso-hexamethyldisiloxane-technical-guide">
                    <span class="rel-t">HMDSO Technical Guide</span>
                    <span class="rel-d">End-capping, hydrophobic treatment &amp; plasma coating</span>
                    <span class="rel-a">Read guide →</span>
                </a>
                <a class="rel-card" href="/products/vinyl-silicone-oil">
                    <span class="rel-t">Vinyl Silicone Oil</span>
                    <span class="rel-d">Vi-PDMS polymers for addition-cure systems</span>
                    <span class="rel-a">View product →</span>
                </a>
                <a class="rel-card" href="/articles/how-to-use-silane-coupling-agents">
                    <span class="rel-t">How to Use Silane Coupling Agents</span>
                    <span class="rel-d">4 methods &amp; dosage guidelines</span>
                    <span class="rel-a">Read guide →</span>
                </a>
            </div>
        </div>
    </section>

"""

html = HEAD + STYLE_MAIN + "\n\n" + BODY + TAIL
io.open(OUT, "w", encoding="utf-8", newline="\n").write(html)
print("written", OUT, len(html), "bytes")

# sanity: ensure all key markers exist
for marker in ["pt8000-app-factory.webp", "pt8000-app-tubes.webp",
               "68478-92-2", "270-844-4", "381.48", "rel-sec", "</html>", "FAQPage", "spec-table", "faq-item"]:
    assert marker in html, marker
print("markers OK")
