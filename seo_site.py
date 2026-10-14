"""Paws Answered SEO build (hand-authored HTML, edited in place, idempotent).
INDEXABLE gates robots meta and sitemap for the whole site. Run: python3 seo_site.py"""
import os, re, shutil, sys
from bs4 import BeautifulSoup
INDEXABLE = False
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT); import seo
LOGOS = "/workspace/atulit-logos/pawsanswered"
B = "Paws Answered"
HUB = {"cats/": "Plain answers to common cat questions: can cats drink milk, why cats throw up, and why cats knead. Each lists when to call a vet and cites ASPCA or VCA sources.",
       "dogs/": "Plain answers to common dog questions: can dogs eat grapes, why dogs eat grass, and how often to bathe a dog. Each says when to call a vet and cites sources."}

def hook(ctx):
    p, s, paths = ctx["path"], ctx["soup"], ctx["paths"]
    seg = p.strip("/").split("/") if p else []
    h1 = ctx["h1"]
    if p == "": return dict(titles=["Plain Pet Care Answers for Cats and Dogs", "Pet Care Answers for Cats and Dogs"])
    if seg[0] in ("cats", "dogs") and len(seg) == 2:
        ans = s.find(class_="answer"); words = len(ans.find("p").get_text().split()) if ans else 0
        meta = s.find(class_="meta")
        for old in s.find_all(attrs={"data-seo": "byline"}): old.decompose()
        if meta: meta.insert(0, BeautifulSoup(f'<span data-seo="byline">By the {B} editorial team · Published: Oct 13, 2026 ·</span>', "html.parser"))
        art = {"@type": "Article", "headline": h1, "datePublished": "2026-10-13", "dateModified": "2026-10-13",
               "author": {"@type": "Organization", "name": f"{B} editorial team"}, "publisher": {"@type": "Organization", "name": B}}
        sib = [q for q in paths if q.startswith(seg[0] + "/") and q.count("/") == 2 and q != p]
        oth = [q for q in paths if q.startswith(("dogs/", "cats/")) and q.count("/") == 2 and not q.startswith(seg[0])]
        q = h1 if h1.endswith("?") else h1 + "?"
        # index only when the direct answer is 40 to 60 words
        return dict(titles=[q], index=(40 <= words <= 60), article=True,
                    schema_filter=lambda x: x.get("@type") != "Article", schema_add=[art], related=(sib + [seg[0] + "/", "topics/health/"] + oth)[:6])
    if p in HUB: return dict(titles=[h1], desc=HUB[p])
    if seg[0] == "topics" and len(seg) == 2:
        t = h1 if h1.endswith("Questions for Cats and Dogs") else f"{h1} Questions for Cats and Dogs"
        return dict(titles=[t], h1=t,
                    desc=f"{h1.replace(' Questions for Cats and Dogs', '')} questions for cats and dogs, answered in plain words. Each answer starts short, lists when to see a vet, and cites its sources.")
    return dict(titles=[h1])

def build():
    for a, b in [("favicon.svg", "favicon.svg"), ("favicon-32.png", "favicon-32.png"), ("icon-180.png", "apple-touch-icon.png"), ("icon-512.png", "icon-512.png")]:
        shutil.copy(f"{LOGOS}/{a}", f"{ROOT}/img/brand/{b}")
    site = seo.Site(ROOT, B, "pawsanswered.com", "pet-care-answers-prototype", INDEXABLE, "Oct 13, 2026", "2026-10-13",
        "Not veterinary advice. If your pet is sick or hurt, contact a vet.",
        f"{LOGOS}/wordmark-1200.png", "img/brand/icon-512.png",
        ["Not veterinary advice.", "Vet sources cited.", "Updated Oct 13, 2026.", f"From {B}.", "Cited sources.", "When to see a vet.", "Plain answers with cited sources and clear signs of when to see a vet."], hook)
    return seo.run(site)
if __name__ == "__main__": build()
