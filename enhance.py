"""PawsAnswered has no page generator (HTML is the source). This idempotent pass adds Lucide icons,
the theme script and toggle, then reruns the SEO step. Run: python3 enhance.py"""
import glob, os, re
from bs4 import BeautifulSoup as BS
from atulit_gfx import icon, THEME_HEAD, toggle, CREDIT, install_css
ROOT = os.path.dirname(os.path.abspath(__file__)); os.chdir(ROOT)
NAV = {"cats/": "cat", "dogs/": "dog", "about/": "info"}
TOP = {"health": "stethoscope", "behavior": "paw-print", "food": "bone", "grooming": "bath", "new-pet": "house", "toys": "sparkles"}
H2 = {"Popular questions": ("circle-help", "#E8743B"), "Browse by topic": ("layers", "#5B3A29")}
frag = lambda h: BS(h, "html.parser")
for f in glob.glob("**/*.html", recursive=True):
    s = BS(open(f).read(), "html.parser"); ch = False
    if s.head and not s.head.find("script", string=re.compile("localStorage.getItem\\('theme'\\)")):
        s.head.insert(2, frag(THEME_HEAD)); ch = True
    hdr = s.select_one("header.top .nav")
    if hdr and not hdr.select_one(".thm"):
        for a in hdr.select("nav a"):
            k = a.get("href", "").split("/")[-2] + "/" if "/" in a.get("href", "") else ""
            if k in NAV: a.insert(0, frag(icon(NAV[k], 16)))
        hdr.append(frag(toggle())); ch = True
    for t in s.select("a.topic"):
        k = t.get("href", "").rstrip("/").split("/")[-1]
        if k in TOP and not t.select_one(".tico"):
            ph = t.select_one(".tphoto")
            (ph or t).insert_after(frag(f'<span class="tico">{icon(TOP[k], 18)}</span>')); ch = True
    for tg in s.select(".tag.cats, .tag.dogs"):
        if not tg.find("svg"):
            tg.insert(0, frag(icon("cat" if "cats" in tg["class"] else "dog", 14))); ch = True
    for h in s.select("main h2, section > h2"):
        t = h.get_text(strip=True)
        if t in H2 and not h.select_one(".ibadge"):
            n, c = H2[t]; h["class"] = h.get("class", []) + ["secdeco"]; h["style"] = f"--c:{c}"
            h.insert(0, frag(f'<span class="ibadge soft">{icon(n, 20)}</span>')); ch = True
    ft = s.select_one("footer .wrap")
    if ft and not ft.select_one(".gfx-credit"):
        ft.append(frag(f'<p class="small gfx-credit">{CREDIT}</p>')); ch = True
    if f == "credits/index.html" and "lucide.dev" not in str(s.select_one("main") or ""):
        m = s.select_one("main") or s.body
        m.append(frag('<section class="wrap"><h2>Icons</h2><p>Interface icons are from <a href="https://lucide.dev" rel="nofollow">Lucide</a>, used under the ISC/MIT license.</p></section>')); ch = True
    if ch: open(f, "w").write(str(s))
install_css("assets/style.css", """.tico{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:#fff;color:var(--acc);margin:-28px auto 0;position:relative;z-index:1;box-shadow:0 4px 12px -4px rgba(0,0,0,.25)}
.tag .ic{margin-right:4px;vertical-align:-.15em}nav a .ic{color:var(--acc);opacity:1}.thm{margin-left:10px}.gfx-credit{color:var(--mut);margin-top:8px}.gfx-credit a{text-decoration:underline}
@media(max-width:800px){nav a .ic{display:none}}
@media(max-width:520px){.wm{height:22px}.top nav a{padding:6px 5px;font-size:13px}.top nav a[href$="about/"]{display:none}.thm{width:32px;height:32px;margin-left:4px}}
h2.secdeco::before{display:none}h2.secdeco{padding-left:0}
html[data-theme=dark] .tico{background:#1a1e26}html[data-theme=dark] .wm{background:#fff;border-radius:9px;padding:4px 8px;box-sizing:content-box}
""")
import seo_site; seo_site.build()
