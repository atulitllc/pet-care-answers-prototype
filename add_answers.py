"""Build the answer pages listed in answers_data.py from the grapes page layout, then refresh hubs, topic pages,
related cards and photo credits. Idempotent. Run: python3 add_answers.py && python3 enhance.py"""
import os, re, glob, json, html as H
from bs4 import BeautifulSoup as BS
from answers_data import A, S
ROOT = os.path.dirname(os.path.abspath(__file__)); os.chdir(ROOT)
D = "Oct 13, 2026"
frag = lambda h: BS(h, "html.parser")
PPH = '<p><b>Pet Poison Helpline: <a href="tel:+18557647661">(855) 764-7661</a></b> (a fee applies)</p>'
PHOTOS = {  # slug: (commons title, url, author, license, license url)
 "dog-chocolate": ("Lazy Dog..jpg","https://commons.wikimedia.org/wiki/File:Lazy_Dog..jpg","ROVER_JP","CC BY 2.0","https://creativecommons.org/licenses/by/2.0"),
 "dog-xylitol": ("Teddy the dog.jpg","https://commons.wikimedia.org/wiki/File:Teddy_the_dog.jpg","ArtemisiaGentileschiFan","CC0","http://creativecommons.org/publicdomain/zero/1.0/deed.en"),
 "dog-diarrhea": ("Pug with his toy - panoramio (2307).jpg","https://commons.wikimedia.org/wiki/File:Pug_with_his_toy_-_panoramio_(2307).jpg","michaelannis","CC BY 3.0","https://creativecommons.org/licenses/by/3.0"),
 "dog-not-eating": ("Didja Ever Have One of Those Days . . . (3600198988).jpg","https://commons.wikimedia.org/wiki/File:Didja_Ever_Have_One_of_Those_Days_._._._(3600198988).jpg","Faith Goble from Kentucky, USA","CC BY 2.0","https://creativecommons.org/licenses/by/2.0"),
 "dog-limping": ("Black dog, black outfit, snow (16055837880).jpg","https://commons.wikimedia.org/wiki/File:Black_dog,_black_outfit,_snow_(16055837880).jpg","Billie Grace Ward from New York, USA","CC BY 2.0","https://creativecommons.org/licenses/by/2.0"),
 "dog-feeding": ("Green Spiral Slow Feeder Dog Bowl.jpg","https://commons.wikimedia.org/wiki/File:Green_Spiral_Slow_Feeder_Dog_Bowl.jpg","ELTORO.VET","CC0","http://creativecommons.org/publicdomain/zero/1.0/deed.en"),
 "dog-temperature": ("Bo, lies on a carpet in the White House on July 27, 2009.jpg","https://commons.wikimedia.org/wiki/File:Bo,_lies_on_a_carpet_in_the_White_House_on_July_27,_2009.jpg","The White House (Pete Souza)","Public domain",""),
 "cat-lilies": ("Lilium longiflorum (Easter lilies) 1.jpg","https://commons.wikimedia.org/wiki/File:Lilium_longiflorum_(Easter_lilies)_1.jpg","James St. John","CC BY 2.0","https://creativecommons.org/licenses/by/2.0"),
 "cat-onions": ("Cat - Flickr - bjimmy934.jpg","https://commons.wikimedia.org/wiki/File:Cat_-_Flickr_-_bjimmy934.jpg","Jimmy B from Chiba prefecture, Japan","CC BY 2.0","https://creativecommons.org/licenses/by/2.0"),
 "cat-chocolate": ("Kitten-stare.jpg","https://commons.wikimedia.org/wiki/File:Kitten-stare.jpg","Mrmiscellanious","Public domain",""),
 "cat-diarrhea": ("2008-11-28 a Calico kitten on the litter box.jpg","https://commons.wikimedia.org/wiki/File:2008-11-28_a_Calico_kitten_on_the_litter_box.jpg","MiNe","CC BY 2.0","https://creativecommons.org/licenses/by/2.0"),
 "cat-not-eating": ("A cat pauses over a bowl of food, 2011.jpg","https://commons.wikimedia.org/wiki/File:A_cat_pauses_over_a_bowl_of_food,_2011.jpg","Linda Hosek","Public domain",""),
 "cat-itchy": ("Cat Scratching.jpg","https://commons.wikimedia.org/wiki/File:Cat_Scratching.jpg","Asabae2752","CC0","http://creativecommons.org/publicdomain/zero/1.0/deed.en"),
 "cat-temperature": ("Cat dozing off on a blanket (Unsplash).jpg","https://commons.wikimedia.org/wiki/File:Cat_dozing_off_on_a_blanket_(Unsplash).jpg","Erik-Jan Leusink","CC0","http://creativecommons.org/publicdomain/zero/1.0/deed.en"),
}

def img_tag(pre, slug, alt, eager=False):
    return (f'<img alt="{H.escape(alt)}" decoding="async" height="533" loading="{"eager" if eager else "lazy"}" sizes="(max-width:800px) 100vw, 50vw" '
            f'src="{pre}img/{slug}-800.webp" srcset="{pre}img/{slug}-800.webp 800w, {pre}img/{slug}.webp 1600w" width="800"/>')

# 1. build new answer pages from the grapes page
TPL = open("dogs/can-dogs-eat-grapes/index.html").read()
for p, a in A.items():
    pet = p.split("/")[0]; Pet = "Cat" if pet == "cats" else "Dog"
    s = BS(TPL, "html.parser")
    s.title.string = a["h1"] + " | Paws Answered"
    cr = s.select_one("nav.crumbs"); cr.select("a")[1]["href"] = f"../../{pet}/"; cr.select("a")[1].string = pet.capitalize()
    cr.select_one('[aria-current="page"]').string = a["h1"]
    s.select_one(".qtxt .tag").replace_with(frag(f'<span class="tag {pet}">{Pet} · {a["topic"]}</span>'))
    s.select_one(".qtxt h1").string = a["h1"]
    s.select_one("figure.qfig").clear(); s.select_one("figure.qfig").append(frag(img_tag("../../", a["img"], a["alt"], True)))
    s.select_one(".answer p").string = a["short"]
    fl = s.select_one(".flags"); red = fl.select_one(".red")
    red.select_one("h2").string = "🚩 When to see a vet"
    red.select_one("ul").replace_with(frag("<ul>" + "".join(f"<li>{H.escape(x)}</li>" for x in a["vet"]) + "</ul>"))
    em = fl.select_one(".emerg")
    if a["toxic"]:
        em.select_one("h2").string = "🚨 Poison emergency: call now"
        em.append(frag(PPH))
    art = s.select_one("article.qa")
    fl = fl.extract()
    for x in art.select_one(".answer").find_next_siblings(): x.extract()
    srcs = [S[k] for k in a["src"]]
    body = "".join(f'<p>{H.escape(t)}' + (f' <sup><a href="#ref{i+1}">[{i+1}]</a></sup>' if i is not None else "") + "</p>" for t, i in a["body"])
    rest = (f'<h2>What the sources say</h2>{body}'
            + ("" if a["toxic"] else '<div id="flagslot"></div>')
            + '<h2>FAQ</h2><div class="faq">' + "".join(f"<details open><summary>{H.escape(q)}</summary><p>{H.escape(x)}</p></details>" for q, x in a["faq"]) + "</div>"
            + '<h2>Sources</h2><ol class="refs">' + "".join(f'<li id="ref{i+1}"><a href="{u}" rel="nofollow">{H.escape(t)}</a>, checked {D}</li>' for i, (t, u) in enumerate(srcs)) + "</ol>"
            + '<p class="muted small">We summarize these sources in our own words. Dosing or home treatment amounts are never given here. Ask your vet.</p>'
            + '<h2>Related</h2><div class="qgrid"></div>')
    if a["toxic"]: s.select_one(".disc").insert_after(fl)
    art.append(frag(rest))
    if not a["toxic"]:
        art.select_one("#flagslot").replace_with(fl)
    for x in s.select('[data-seo="related"]'): x.decompose()
    os.makedirs(p, exist_ok=True); open(p + "index.html", "w").write(str(s))

# 2. collect all answers
def info(p):
    s = BS(open(p + "index.html").read(), "html.parser")
    im = s.select_one("figure.qfig img"); tag = s.select_one(".qtxt .tag").get_text(" ", strip=True)
    return dict(p=p, pet=p.split("/")[0], h1=s.select_one("h1").get_text(strip=True), topic=tag.split("·")[-1].strip().lower().replace(" ", "-"),
                img=re.sub(r"^.*img/|-800\.webp$", "", im["src"]), alt=im["alt"])
ANS = [info(f[:-10]) for f in sorted(glob.glob("cats/*/index.html") + glob.glob("dogs/*/index.html"))]
json.dump({x["p"]: x["topic"] for x in ANS}, open("answer_topics.json", "w"), indent=1)

def related(p):  # same logic as seo_site.related_for
    me = next(x for x in ANS if x["p"] == p)
    same_topic = [x for x in ANS if x["pet"] == me["pet"] and x["topic"] == me["topic"] and x["p"] != p]
    same_pet = [x for x in ANS if x["pet"] == me["pet"] and x not in same_topic and x["p"] != p]
    other = [x for x in ANS if x["pet"] != me["pet"] and x["topic"] == me["topic"]]
    return (same_topic + same_pet)[:4] + other[:1]

def card(x, pre):
    Pet = "Cat" if x["pet"] == "cats" else "Dog"
    return (f'<a class="qcard" data-pet="{x["pet"]}" data-q="{H.escape(x["h1"].lower())}" href="{pre}{x["p"]}"><span class="thumb">{img_tag(pre, x["img"], x["alt"])}</span>'
            f'<span class="qbody"><span class="tag {x["pet"]}">{Pet}</span><b>{H.escape(x["h1"])}</b><span class="arrow">→</span></span></a>')

# 3. visible related cards on every answer page (3 cards)
for x in ANS:
    f = x["p"] + "index.html"; s = BS(open(f).read(), "html.parser")
    h = [h for h in s.select("article.qa h2") if h.get_text(strip=True) == "Related"][0]
    g = h.find_next_sibling("div", class_="qgrid"); g.clear(); g.append(frag("".join(card(r, "../../") for r in related(x["p"])[:3])))
    open(f, "w").write(str(s))

# 4. hubs and topic pages
for pet in ("cats", "dogs"):
    f = f"{pet}/index.html"; s = BS(open(f).read(), "html.parser")
    s.select_one("main .qgrid").clear(); s.select_one("main .qgrid").append(frag("".join(card(x, "../") for x in ANS if x["pet"] == pet)))
    open(f, "w").write(str(s))
for f in glob.glob("topics/*/index.html"):
    t = f.split("/")[1]; mine = [x for x in ANS if x["topic"] == t]
    s = BS(open(f).read(), "html.parser"); g = s.select_one("main .qgrid")
    for x in s.select("main p.soon"): x.decompose()
    if g is None:
        g = frag('<div class="qgrid"></div>').div; s.select_one("main").append(g)
    g.clear(); g.append(frag("".join(card(x, "../../") for x in mine)))
    for x in s.select("main > p.muted"):
        if "coming soon" in x.get_text(): x.decompose()
    if not mine: g.insert_after(frag('<p class="muted soon">Questions on this topic are coming soon.</p>'))
    open(f, "w").write(str(s))

# home "Popular questions": 3 dog and 3 cat answers
HOME = ["dogs/can-dogs-eat-chocolate/", "cats/are-lilies-poisonous-to-cats/", "dogs/can-dogs-eat-grapes/",
        "cats/why-is-my-cat-throwing-up/", "dogs/how-often-should-i-feed-my-dog/", "cats/why-is-my-cat-not-eating/"]
s = BS(open("index.html").read(), "html.parser")
h = [h for h in s.find_all("h2") if h.get_text(strip=True) == "Popular questions"][0]
g = h.find_next("div", class_="qgrid"); g.clear()
g.append(frag("".join(card(next(x for x in ANS if x["p"] == q), "") for q in HOME))); open("index.html", "w").write(str(s))

# 5. credits
s = BS(open("credits/index.html").read(), "html.parser")
ul = s.find("a", href=re.compile("commons.wikimedia.org")).find_parent("ol")
md = open("img/CREDITS.md").read()
for slug, (t, u, au, lic, lu) in PHOTOS.items():
    if f"img/{slug}.webp" not in str(ul):
        ul.append(frag(f'<li><a href="{u}">{H.escape(t)}</a><br/><span class="muted">Photographer: {H.escape(au)} · License: {lic} · Wikimedia Commons · used as img/{slug}.webp</span></li>'))
    if f"img/{slug}.webp" not in md: md += f"- img/{slug}.webp: [{t}]({u}), {au}, {lic} {lu}\n"
open("credits/index.html", "w").write(str(s)); open("img/CREDITS.md", "w").write(md)
print("answers", len(ANS))
