"""Paws Answered SEO build (hand-authored HTML, edited in place, idempotent).
INDEXABLE gates robots meta and sitemap for the whole site. Run: python3 seo_site.py"""
import json, os, re, shutil, sys
from bs4 import BeautifulSoup
INDEXABLE = False
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT); import seo
LOGOS = "/workspace/atulit-logos/pawsanswered"
B = "Paws Answered"
ANSWER_DESC = {
 "dogs/can-dogs-eat-grapes/": "No. Grapes, raisins, sultanas and currants can cause vomiting and then kidney injury and failure in dogs. Call a vet or pet poison hotline if your dog eats any.",
 "dogs/how-often-should-i-bathe-my-dog/": "Less often than you might think. The ASPCA says most dogs need a bath no more than a few times a year, and regular brushing keeps them clean in between.",
 "dogs/can-dogs-eat-chocolate/": "No. Chocolate has theobromine and caffeine, which can cause vomiting, a racing heart, tremors and seizures in dogs. Call a vet or poison hotline if eaten.",
 "dogs/is-xylitol-toxic-to-dogs/": "Yes. Xylitol in sugar free gum, mints, candy and toothpaste can crash a dog's blood sugar within minutes or harm the liver. Call a vet or poison hotline now.",
 "dogs/how-often-should-i-feed-my-dog/": "Puppies need four meals a day at 8 to 12 weeks, then three, then two. Adult dogs usually need one meal, or two smaller ones for big dogs, says the ASPCA.",
 "dogs/can-dogs-eat-onions-or-garlic/": "No. Onions, garlic, chives and leeks can upset a dog's stomach and damage red blood cells, causing anemia. Call a vet or poison hotline if your dog eats any.",
 "dogs/can-dogs-eat-macadamia-nuts/": "No. Macadamia nuts can make dogs weak, wobbly, shaky and overheated within 12 hours, and may cause pancreatitis. Call your vet or poison hotline if eaten.",
 "dogs/is-ibuprofen-safe-for-dogs/": "No. Ibuprofen is a human pain reliever that can cause bleeding stomach ulcers and kidney damage in dogs. Never give it, and call a vet if your dog swallows any.",
 "dogs/is-marijuana-toxic-to-dogs/": "Yes. There is no safe dose of marijuana for dogs. Eating it or breathing the smoke can cause stumbling, leaking urine and seizures. Call a vet or hotline.",
 "dogs/can-dogs-eat-raw-bread-dough/": "No. Raw yeast dough can swell in a dog's stomach and cause bloat, and the yeast makes alcohol that can poison them. Call your vet or poison hotline right away.",
 "cats/can-cats-drink-milk/": "It is best not to give cats milk. The ASPCA explains pets have little lactase to break down lactose, so milk and dairy can cause diarrhea or stomach upset.",
 "cats/why-is-my-cat-throwing-up/": "Occasional vomiting and a hairball every week or two can be normal. See your vet if your cat vomits more than once a week or seems unwell, says Cornell.",
 "cats/why-does-my-cat-have-diarrhea/": "Cat diarrhea often follows a diet change or stress and passes quickly. If it lasts over a day or two and your cat seems unwell, see your vet soon, says Cornell.",
 "cats/why-is-my-cat-not-eating/": "A cat that stops eating can develop fatty liver, which can be fatal without prompt treatment, says Cornell. Overweight cats are at higher risk. Call your vet.",
 "cats/why-is-my-cat-so-itchy/": "Fleas are a top reason cats itch. Cornell says flea bites cause intense itching and scratching can lead to infection. Ask your vet about safe flea control.",
 "cats/how-often-should-i-feed-my-cat/": "Kittens do best with three meals a day until six months, then two until age one. Most adult cats do well fed once or twice a day, says Cornell Feline Health.",
 "cats/is-tylenol-toxic-to-cats/": "Yes. Acetaminophen in Tylenol and many cold, flu and allergy products is especially dangerous for cats and can cause liver failure. Call a vet if swallowed.",
 "cats/are-lilies-poisonous-to-cats/": "Yes. Any part of a true lily, even pollen or vase water, can cause kidney failure in cats. If your cat touches or chews a lily, get to a vet right away.",
 "cats/can-cats-eat-onions-or-garlic/": "No. Onions, garlic, chives and leeks can upset the stomach and damage red blood cells in cats, which are more sensitive than dogs. Call your vet if eaten.",
 "cats/can-cats-eat-chocolate/": "No. Chocolate has methylxanthines that can cause vomiting, abnormal heart rhythm, tremors and seizures in pets. Darker is worse. Call your vet if eaten."
}
HUB = {
 "cats/": "Plain cat care answers: lilies, chocolate, onions, milk, Tylenol, vomiting, diarrhea, not eating, fleas and how often to feed. Each one cites its sources.",
 "dogs/": "Plain dog care answers: chocolate, xylitol, grapes, onions, macadamia nuts, bread dough, ibuprofen, marijuana, feeding and bathing, with cited sources."
}

TOPICS = json.load(open(os.path.join(ROOT, "answer_topics.json")))  # written by add_answers.py

def related_for(p):
    pet, tp = p.split("/")[0], TOPICS.get(p)
    ans = sorted(TOPICS)
    same_topic = [q for q in ans if q.startswith(pet + "/") and TOPICS[q] == tp and q != p]
    same_pet = [q for q in ans if q.startswith(pet + "/") and q not in same_topic and q != p]
    other = [q for q in ans if not q.startswith(pet + "/") and TOPICS[q] == tp]
    return (same_topic + same_pet)[:4] + other[:1]

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
        return dict(titles=[q], desc=ANSWER_DESC.get(p), index=(40 <= words <= 60), article=True,
                    schema_filter=lambda x: x.get("@type") != "Article", schema_add=[art], related=related_for(p) + [seg[0] + "/", "topics/" + TOPICS.get(p, "health") + "/"])
    if p in HUB: return dict(titles=[h1], desc=HUB[p])
    if seg[0] == "topics" and len(seg) == 2:
        t = h1 if h1.endswith("Questions for Cats and Dogs") else f"{h1} Questions for Cats and Dogs"
        return dict(titles=[t], h1=t, index=seg[1] in set(TOPICS.values()),  # empty "coming soon" topics stay noindex
                    desc=f"{h1.replace(' Questions for Cats and Dogs', '')} questions for cats and dogs, answered in plain words. Each answer starts short, lists when to see a vet, and cites its sources.")
    return dict(titles=[h1])

def build():
    for a, b in [("favicon.svg", "favicon.svg"), ("favicon-32.png", "favicon-32.png"), ("icon-180.png", "apple-touch-icon.png"), ("icon-512.png", "icon-512.png")]:
        shutil.copy(f"{LOGOS}/{a}", f"{ROOT}/img/brand/{b}")
    site = seo.Site(ROOT, B, "pawsanswered.com", "pet-care-answers-prototype", INDEXABLE, "Oct 13, 2026", "2026-10-13",
        "Not veterinary advice. If your pet is sick or hurt, contact a vet.",
        f"{LOGOS}/wordmark-1200.png", "img/brand/icon-512.png",
        ["Not veterinary advice.", "Vet sources cited.", "Updated Oct 13, 2026.", f"From {B}.", "Cited sources.", "When to see a vet.", "Plain answers with cited sources and clear signs of when to see a vet."], hook)
    r = seo.run(site)
    build_search()
    return r

def build_search():
    """Write search.json (all answers, hubs, topic pages) for the live search in assets/app.js."""
    from atulit_gfx import icon
    items = []
    for p in seo.pages_of(ROOT):
        seg = p.strip("/").split("/") if p else []
        if not seg or seg[0] not in ("cats", "dogs", "topics"): continue
        s = seo.load(ROOT, p); h1 = s.find("h1").get_text(" ", strip=True)
        if seg[0] == "topics" and not s.select("main .qcard"): continue  # empty "coming soon" topic
        ans = s.select_one(".answer p"); tag = s.select_one(".qtxt .tag")
        kind = "answer" if len(seg) == 2 and seg[0] != "topics" else ("hub" if len(seg) == 1 else "topic")
        pet = seg[0] if seg[0] in ("cats", "dogs") else ""
        kw = set(re.findall(r"[a-z]+", " ".join(seg).replace("-", " ")))
        if tag: kw |= set(re.findall(r"[a-z]+", tag.get_text(" ").lower()))
        for h in s.select("article.qa h2 + p, .faq summary"): kw |= set(re.findall(r"[a-z]{4,}", h.get_text(" ").lower()))
        items.append(dict(t=h1, u=p, pet=pet, topic=TOPICS.get(p, seg[1] if kind == "topic" else ""), kind=kind,
                          a=(ans.get_text(" ", strip=True) if ans else (s.select_one("p.lead").get_text(" ", strip=True) if s.select_one("p.lead") else "")),
                          k=" ".join(sorted(kw))))
    data = dict(icons={"cats": icon("cat", 18), "dogs": icon("dog", 18), "": icon("list", 18)}, items=items)
    open(os.path.join(ROOT, "search.json"), "w").write(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    print(f"search.json: {len(items)} entries")

if __name__ == "__main__": build()
