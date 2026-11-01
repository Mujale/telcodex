#!/usr/bin/env python3
"""Generate article HTML pages and the Articles index from a manifest.

Add an article in three steps:
  1. Write content as  articles/<slug>.md  (first heading becomes the page H1).
  2. Add an entry to ARTICLES below.
  3. Run:  python tools/articles.py   then   python tools/build.py

Each article becomes a real indexable page at /<slug>.html that loads
articles/<slug>.md via the shared page engine. An index is written to
articles.html linking them all.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# ---- ARTICLE MANIFEST: (slug, Title, description, keywords, index blurb) ----
ARTICLES = [
    ("sub-thz-6g", "What Is Sub-THz Spectrum in 6G? (100-300 GHz)",
     "Sub-THz spectrum (100-300 GHz) for 6G explained: why 3GPP studies it, the path-loss and near-field challenges, use cases, and how it differs from the FR3 upper mid-band.",
     "sub-THz, 6G spectrum, 100-300 GHz, FR3, terahertz, 3GPP, mmWave, 6G bands",
     "Why 3GPP studies the 100-300 GHz range, the physics challenges, and how it differs from FR3."),
    ("5g-core-vs-6g-core", "5G Core vs 6G Core - What Changes?",
     "5G Core vs the expected 6G core in 3GPP: the service-based architecture, the main network functions, and what the SA2 6G study is expected to change or add.",
     "5G core, 6G core, service-based architecture, SBA, AMF, SMF, UPF, NWDAF, 3GPP SA2",
     "How the service-based 5G Core compares with the 6G core direction being studied in 3GPP."),
    ("ambient-iot", "Ambient IoT - Battery-Free Devices Explained",
     "Ambient IoT (zero-energy devices) explained: how battery-free devices harvest energy, communicate by backscatter, the gNB-reader architecture, and 3GPP use cases.",
     "ambient IoT, zero-energy devices, battery-free IoT, backscatter, energy harvesting, 3GPP, 5G Advanced",
     "Battery-free devices that harvest energy and talk by backscatter - a building block for 6G scale."),
    ("isac-explained", "ISAC Explained - Sensing and Communication Together",
     "Integrated Sensing and Communication (ISAC) explained: how a 6G network senses the environment using its own radios, the Sensing Function, service categories and KPIs.",
     "ISAC, integrated sensing and communication, 6G sensing, SenF, 3GPP, joint sensing communication",
     "How a 6G network senses the physical world using the same radios that carry data."),
    ("ai-native-6g", "AI-Native 6G - What Does It Mean?",
     "AI-native 6G explained: how it differs from the AI already in 5G, what 3GPP studies for AI in the radio, core and operations, and why 6G needs it.",
     "AI-native, 6G AI, AI/ML, NWDAF, 3GPP, machine learning networks, AI RAN",
     "What 'AI-native' really means for 6G, and how it differs from the AI already in 5G."),
    ("6g-timeline", "6G Timeline - When Is 6G Coming?",
     "The 6G timeline in 3GPP: the approved Release 21 schedule, what each freeze milestone means, and why commercial 6G is expected around 2030.",
     "6G timeline, when is 6G coming, Release 21, 3GPP, 6G freeze dates, 6G 2030",
     "The approved Release 21 schedule, what each milestone means, and when commercial 6G arrives."),
]

CC_BLOCK = """<div class="cc-banner hidden" id="ccBanner" role="dialog" aria-live="polite" aria-label="Cookie consent"><div class="cc-inner">
  <div class="cc-text"><strong>We value your privacy</strong>We use strictly necessary cookies to make this site work. With your consent we would also use cookies for analytics and advertising (including Google AdSense). You can accept all, reject all non-essential cookies, or choose per category. See our <a href="policy.html?doc=cookie" target="_blank" rel="noopener">Cookie Policy</a>, <a href="policy.html?doc=privacy" target="_blank" rel="noopener">Privacy Policy</a> and <a href="policy.html?doc=terms" target="_blank" rel="noopener">Terms &amp; Conditions</a>.</div>
  <div class="cc-actions"><button type="button" class="btn btn-outline" id="ccReject">Reject all</button><button type="button" class="btn btn-outline" id="ccCustomize">Customize</button><button type="button" class="btn btn-primary" id="ccAccept">Accept all</button></div>
</div></div>
<div class="cc-overlay hidden" id="ccOverlay" role="dialog" aria-modal="true" aria-label="Cookie preferences"><div class="cc-modal">
  <h2>Cookie preferences</h2><p>Choose which categories of cookies you allow. Strictly necessary cookies are always on. You can change these choices any time via Cookie settings in the footer.</p>
  <div class="cc-cat"><div class="cc-cat-head"><h3>Strictly necessary</h3><span class="locked">Always on</span></div><p>Required for core functionality and to remember your consent choices.</p></div>
  <div class="cc-cat"><div class="cc-cat-head"><h3>Analytics</h3><label class="sw"><input type="checkbox" id="catAnalytics" /><span class="slider"></span></label></div><p>Anonymous, aggregated usage. Loads only if enabled.</p></div>
  <div class="cc-cat"><div class="cc-cat-head"><h3>Advertising</h3><label class="sw"><input type="checkbox" id="catAds" /><span class="slider"></span></label></div><p>Google AdSense and personalised/limited ads. Loads only if enabled.</p></div>
  <div class="cc-modal-actions"><button type="button" class="btn btn-outline" id="ccModalReject">Reject all</button><button type="button" class="btn btn-primary" id="ccModalSave">Save choices</button></div>
</div></div>"""

TOPNAV = """<div class="topbar"><div class="inner"><nav><a href="/">Home</a><a href="articles.html">Articles</a><a href="glossary.html">Glossary</a><a href="about.html">About</a></nav></div></div>
<header class="site"><div class="inner">
  <a class="brandlink" href="/"><div class="brand"><span class="logo">6G</span><div><h1>6G Network Evolution</h1><div class="sub">The 6G Standards &amp; Architecture Codex</div></div></div></a>
</div></header>
<nav class="topics"><div class="inner">
  <a href="/" data-key="home">Home</a>
  <a href="standardization.html" data-key="standardization">Standardization &amp; Timeline</a>
  <a href="features.html" data-key="features">Features</a>
  <a href="architecture.html" data-key="architecture">Network Architecture</a>
  <a href="ran.html" data-key="ran">RAN</a>
  <a href="core.html" data-key="core">Core</a>
  <a href="management.html" data-key="management">Network Management</a>
</div></nav>"""

FOOTER = """<footer class="site"><div class="inner">
  <span>&copy; <span id="yr"></span> Telcodex.io &middot; The 6G Standards &amp; Architecture Codex.</span>
  <nav class="flinks">
    <a href="articles.html">Articles</a><a href="about.html">About</a><a href="contact.html">Contact</a>
    <a href="policy.html?doc=privacy" target="_blank" rel="noopener">Privacy Policy</a>
    <a href="policy.html?doc=cookie" target="_blank" rel="noopener">Cookie Policy</a>
    <a href="policy.html?doc=terms" target="_blank" rel="noopener">Terms &amp; Conditions</a>
    <button type="button" id="ccSettings">Cookie settings</button>
    <button type="button" id="ccDoNotSell">Do Not Sell or Share My Info</button>
  </nav>
</div></footer>"""

ARTICLE_TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} | Telcodex.io</title>
<meta name="description" content="{desc}" />
<meta name="keywords" content="{keywords}" />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="https://telcodex.io/{slug}.html" />
<meta property="og:type" content="article" />
<meta property="og:site_name" content="Telcodex.io" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:url" content="https://telcodex.io/{slug}.html" />
<meta name="twitter:card" content="summary" />
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{desc}","author":{{"@type":"Organization","name":"Telcodex.io"}},"publisher":{{"@type":"Organization","name":"Telcodex.io"}},"mainEntityOfPage":"https://telcodex.io/{slug}.html","inLanguage":"en"}}
</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1740697015974190" crossorigin="anonymous"></script>
<!-- STEP 2: Google Funding Choices (CMP) snippet -- paste here -->
<link rel="stylesheet" href="assets/page.css" />
</head>
<body>
{topnav}

<div class="layout">
  <main>
    <article class="doc" id="doc"><div class="loading">Loading...</div></article>
    <div class="ad ad-inline"><span class="ad-label">Advertisement</span></div>
  </main>
  <aside>
    <div class="side-card"><h4>On this page</h4><nav class="toc" id="toc"></nav></div>
    <div class="ad rail"><span class="ad-label">Advertisement</span></div>
  </aside>
</div>

{footer}

{cc}

<script>window.PAGE={{md:"articles/{slug}.md"}};</script>
<script src="assets/page.js"></script>
</body>
</html>
"""

INDEX_TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>6G Articles &amp; Explainers - 3GPP Topics | Telcodex.io</title>
<meta name="description" content="In-depth 6G articles and explainers built from 3GPP material: sub-THz spectrum, 5G vs 6G core, ambient IoT, ISAC, AI-native 6G and the 6G timeline." />
<meta name="keywords" content="6G articles, 6G explained, 3GPP, sub-THz, 6G core, ambient IoT, ISAC, AI-native, 6G timeline" />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="https://telcodex.io/articles.html" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="Telcodex.io" />
<meta property="og:title" content="6G Articles & Explainers - 3GPP Topics" />
<meta property="og:description" content="In-depth 6G articles and explainers built from 3GPP material." />
<meta property="og:url" content="https://telcodex.io/articles.html" />
<meta name="twitter:card" content="summary" />
<link rel="stylesheet" href="assets/page.css" />
<style>
  .grid-wrap{{max-width:var(--shell);margin:0 auto;padding:clamp(24px,4vw,44px) var(--pad);background:var(--bg);}}
  .grid-wrap h2.sec{{font-size:22px;font-weight:800;letter-spacing:-.3px;margin-bottom:6px;}}
  .grid-wrap p.lead{{color:var(--ink-soft);font-size:15px;margin-bottom:20px;max-width:66ch;}}
  .cardgrid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;}}
  .tcard{{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:20px 22px;text-decoration:none;transition:border-color .15s,transform .15s;display:block;}}
  .tcard:hover{{border-color:var(--brand);transform:translateY(-3px);text-decoration:none;}}
  .tcard .k{{font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--brand);}}
  .tcard h4{{font-size:17px;font-weight:700;margin:7px 0 6px;color:var(--ink);}}
  .tcard p{{font-size:14px;color:var(--ink-soft);line-height:1.55;margin:0;}}
</style>
</head>
<body>
{topnav}

<div class="grid-wrap">
  <h2 class="sec">Articles &amp; explainers</h2>
  <p class="lead">In-depth, plain-language explainers on 6G topics, built from public 3GPP material. New articles are added regularly.</p>
  <div class="cardgrid">
    {cards}
  </div>
</div>

{footer}

{cc}

<script>window.PAGE={{key:"articles"}};</script>
<script src="assets/page.js"></script>
</body>
</html>
"""


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    print("Generating article pages...")
    for slug, title, desc, keywords, _blurb in ARTICLES:
        if not os.path.exists(os.path.join(ROOT, "articles", slug + ".md")):
            print(f"  !! missing articles/{slug}.md - skipped")
            continue
        html = ARTICLE_TPL.format(slug=slug, title=esc(title), desc=esc(desc),
                                  keywords=esc(keywords), topnav=TOPNAV, footer=FOOTER, cc=CC_BLOCK)
        with open(os.path.join(ROOT, slug + ".html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  OK {slug}.html")

    cards = "\n    ".join(
        f'<a class="tcard" href="{s}.html"><div class="k">Article</div><h4>{esc(t)}</h4><p>{esc(b)}</p></a>'
        for (s, t, _d, _k, b) in ARTICLES
    )
    idx = INDEX_TPL.format(cards=cards, topnav=TOPNAV, footer=FOOTER, cc=CC_BLOCK)
    with open(os.path.join(ROOT, "articles.html"), "w", encoding="utf-8") as f:
        f.write(idx)
    print("  OK articles.html (index)")
    print("\nDone. Now run: python tools/build.py")


if __name__ == "__main__":
    main()
