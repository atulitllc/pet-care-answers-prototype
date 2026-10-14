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
 "cats/can-cats-drink-milk/": "It is best not to give cats milk. The ASPCA explains pets have little lactase to break down lactose, so milk and dairy can cause diarrhea or stomach upset.",
 "cats/why-does-my-cat-knead/": "Kneading is normal. Kittens knead to help milk flow, and adult cats keep doing it when relaxed, to make a comfy spot, or to mark you with scent from their paws.",
 "cats/why-is-my-cat-throwing-up/": "Occasional vomiting, especially of hairballs, may be nothing in a healthy cat. Call your vet if it happens often or comes with other signs of illness.",
 "dogs/can-dogs-eat-grapes/": "No. Grapes, raisins and currants can cause kidney failure in dogs, with no known safe amount. Call a vet or pet poison hotline right away if your dog eats any.",
 "dogs/how-often-should-i-bathe-my-dog/": "Less often than you might think. The ASPCA says most dogs need a bath no more than a few times a year, and regular brushing keeps them clean in between.",
 "dogs/why-is-my-dog-eating-grass/": "Grass eating is very common in dogs and usually not a sign of illness, VCA notes. Most are not sick first. See a vet if your dog shows stomach discomfort.",
 "dogs/can-dogs-eat-chocolate/": "No. Chocolate has theobromine and caffeine, which can cause vomiting, a racing heart, tremors and seizures in dogs. Call a vet or poison hotline if eaten.",
 "dogs/is-xylitol-toxic-to-dogs/": "Yes. Xylitol in sugar free gum, mints, baked goods and some peanut butter can crash a dog's blood sugar or harm the liver. Call a vet or poison hotline now.",
 "dogs/why-does-my-dog-have-diarrhea/": "Dog diarrhea can come from diet changes, garbage, stress, parasites or infection. Call your vet if it lasts over two days or comes with blood or vomiting.",
 "dogs/why-is-my-dog-not-eating/": "A dog may stop eating due to illness, pain, nausea, mouth problems, stress or poisons. Poor appetite is strongly linked with illness, so call your vet.",
 "dogs/why-is-my-dog-limping/": "Sudden limping in dogs is often a broken nail, sprain, joint injury, fracture or dislocation. Ongoing limping can mean arthritis. See your vet to find out.",
 "dogs/how-often-should-i-feed-my-dog/": "Most adult dogs do well fed once or twice a day, or in two to three equal meals, says VCA. Young puppies may need three or four. Ask your vet how much.",
 "dogs/what-is-a-normal-temperature-for-a-dog/": "Normal rectal temperature for dogs is about 99.5 to 102.5°F per Merck, or 100.5 to 102.5°F per VCA. Learn the signs of fever and when to call your vet.",
 "cats/are-lilies-poisonous-to-cats/": "Yes. Any part of a true lily, even pollen or vase water, can cause kidney failure in cats. If your cat touches or chews a lily, get to a vet right away.",
 "cats/can-cats-eat-onions-or-garlic/": "No. Onions, garlic, chives and leeks can upset the stomach and damage red blood cells in cats, which are more sensitive than dogs. Call your vet if eaten.",
 "cats/can-cats-eat-chocolate/": "No. Chocolate has methylxanthines that can cause vomiting, abnormal heart rhythm, tremors and seizures in pets. Darker is worse. Call your vet if eaten.",
 "cats/why-does-my-cat-have-diarrhea/": "Cat diarrhea can come from parasites, infection, toxins, diet changes or food intolerance. Call your vet if it lasts over two days or has blood or vomiting.",
 "cats/why-is-my-cat-not-eating/": "Cats stop eating from illness, pain, mouth problems, nausea or stress. Not eating can lead to fatty liver, so call your vet early, and now after two days.",
 "cats/why-is-my-cat-so-itchy/": "Itching is the most common allergy sign in cats, and fleas are the top cause. Food allergies, mites and ringworm can look alike, so let your vet find out why.",
 "cats/what-is-a-normal-temperature-for-a-cat/": "A cat's normal rectal temperature is about 100.5 to 102.5°F (38.1 to 39.2°C), per Merck and VCA. Learn the signs of a fever and when to call your vet."
}
HUB = {
 "cats/": "Plain cat care answers: lilies, chocolate, onions, milk, diarrhea, vomiting, not eating, itching, kneading and normal temperature. Each cites vet sources.",
 "dogs/": "Plain dog care answers: chocolate, xylitol, grapes, diarrhea, not eating, limping, feeding, bathing, grass eating and normal temperature, with vet sources."
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
    return seo.run(site)
if __name__ == "__main__": build()
