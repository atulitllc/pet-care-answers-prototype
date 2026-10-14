"""Ground the 6 PawsAnswered answers in cited vet sources (fetched Oct 13, 2026). Edits HTML in place, idempotent. Then run seo_site.py.
No dosing or home treatment amounts. Vet safety boxes are kept as is."""
from bs4 import BeautifulSoup
D="Oct 13, 2026"
ASPCA_FOODS=("ASPCA Animal Poison Control: People Foods to Avoid Feeding Your Pets","https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets")
VCA_GRAPES=("VCA Animal Hospitals: Grape, Raisin, and Currant Poisoning in Dogs (Pet Poison Helpline authors)","https://vcahospitals.com/know-your-pet/grape-raisin-and-currant-poisoning-in-dogs")
ASPCA_DOG=("ASPCA: General Dog Care","https://www.aspca.org/pet-care/dog-care/general-dog-care")
VCA_GRASS=("VCA Animal Hospitals: Why Do Dogs Eat Grass","https://vcahospitals.com/know-your-pet/why-do-dogs-eat-grass")
VCA_VOMIT=("VCA Animal Hospitals: Vomiting in Cats","https://vcahospitals.com/know-your-pet/vomiting-in-cats")
VCA_KNEAD=("VCA Animal Hospitals: Why do cats knead?","https://vcahospitals.com/resources/behavior-cat/true-or-false-do-cats-knead")
VCA_BISC=("VCA Animal Hospitals: Reasons pets make biscuits","https://vcahospitals.com/resources/behavior-dog/reasons-pets-make-biscuits")
A={
"dogs/can-dogs-eat-grapes/":dict(short="No. Grapes, raisins and Zante currants can cause kidney failure in dogs, and there is no known safe amount. Call a vet or a pet poison hotline right away if your dog eats any.",
  body=[("Grapes, raisins and Zante currants can cause kidney failure in dogs. Cases have involved seedless and seeded, red and green, homegrown and store bought grapes.",1),
        ("There is no well established toxic dose. Some dogs get sick after eating only a small amount.",1),
        ("Hidden sources include trail mix, cereal, granola bars, baked goods and some jams.",1),
        ("ASPCA Animal Poison Control lists grapes and raisins among foods to avoid, because they can lead to kidney damage.",0)],
  faq=[("What if my dog only ate one grape?","Call anyway. VCA notes there is no established safe amount and some dogs react to small amounts. Contact your vet or a pet poison helpline right away."),
       ("Are raisins in baked goods a problem?","Yes. VCA lists baked goods, cereal, trail mix and granola bars with raisins as possible sources.")],src=[ASPCA_FOODS,VCA_GRAPES]),
"dogs/how-often-should-i-bathe-my-dog/":dict(short="Less often than you might think. The ASPCA says most dogs do not need a bath more than a few times a year. Regular brushing helps keep them clean in between.",
  body=[("Most dogs do not need to be bathed more than a few times a year.",0),("Before a bath, comb or cut out mats from the coat.",0),("Rinse all soap out of the coat carefully, or dirt will stick to the leftover soap.",0),("Frequent brushing helps keep your dog clean and reduces shedding.",0),("If your dog has a skin problem or your vet prescribed a shampoo, follow your vet's instructions instead.",None)],
  faq=[("Does brushing replace bathing?","Brushing does a lot of the work. The ASPCA recommends frequent brushing to keep dogs clean and cut shedding."),("What if my dog smells or itches a lot?","Ask your vet. Odor and itching can be signs of a skin or ear problem.")],src=[ASPCA_DOG]),
"dogs/why-is-my-dog-eating-grass/":dict(short="It is very common, and usually not a sign of illness. VCA notes most grass eating dogs are not sick beforehand and do not vomit afterward. See a vet if your dog also shows stomach discomfort.",
  body=[("Vets hear this question all the time, because many dogs eat grass. Eating non food items is called pica.",0),("VCA cites studies showing less than 25% of dogs vomit after eating grass, and only about 10% show signs of illness before eating it.",0),("Grass is a source of fiber, which may help digestion. Boredom or wanting attention can also play a part.",0),("If your dog shows stomach discomfort, a medical problem such as gastric reflux, inflammatory bowel disease or pancreatitis is possible, so see your vet.",0)],
  faq=[("Do dogs eat grass because they are sick?","Usually not. VCA notes only about 10% of dogs show signs of illness before eating grass."),("When should I worry?","If your dog seems to have an upset stomach, vomits often, or eats grass frantically, see your vet.")],src=[VCA_GRASS]),
"cats/can-cats-drink-milk/":dict(short="It is best not to give it. The ASPCA explains that pets do not have much lactase, the enzyme that breaks down lactose, so milk and dairy can cause diarrhea or other stomach upset.",
  body=[("Pets do not make significant amounts of lactase, the enzyme that digests lactose in milk.",0),("Because of that, milk and other dairy foods can cause diarrhea or other digestive upset.",0),("Fresh water is the drink cats need. Ask your vet before adding any new food or drink.",None)],
  faq=[("What about cheese or yogurt?","The ASPCA groups milk and other dairy based products together as possible causes of diarrhea and digestive upset."),("My cat drank some milk. Is that an emergency?","Usually not, but watch for diarrhea or vomiting and call your vet if it continues.")],src=[ASPCA_FOODS]),
"cats/why-does-my-cat-knead/":dict(short="Kneading is normal. Kittens knead their mother to help milk flow, and many adult cats keep doing it when they feel relaxed, to make a comfy spot, or to mark you with scent from their paws.",
  body=[("Kittens knead their mother while nursing, which helps bring milk down. The comforting feeling seems to carry into adulthood.",0),("Cats also knead to make a resting spot more comfortable, to show affection, and to mark territory, since they have scent glands in their paws.",0),("Kneading can also be a stretch.",1),("A cat kneading and purring alone in an unusual place, such as under a bed, may be self soothing because it feels unwell. Talk to your vet if kneading suddenly increases or comes with hiding.",0)],
  faq=[("Is kneading a sign my cat likes me?","Often, yes. VCA notes cats usually do not knead on people or animals they do not like."),("Should I stop it?","It is normal behavior. VCA suggests redirecting a pet to chase a toy if kneading gets disruptive.")],src=[VCA_KNEAD,VCA_BISC]),
"cats/why-is-my-cat-throwing-up/":dict(short="Occasional vomiting in an otherwise healthy cat, especially of hairballs, may not mean anything is wrong. Vomiting can also be a sign of many illnesses, so call your vet if it happens often or comes with other signs.",
  body=[("Cats vomit fairly readily. An occasional episode in a healthy cat, mainly of hair, may be nothing abnormal.",0),("Cats swallow hair when grooming. VCA says to contact your vet if your cat vomits hairballs more than once a month.",0),("Vomiting is a sign, not a diagnosis. It can come with infections, swallowed objects stuck in the gut, toxins, urinary blockage, pancreatitis, liver or kidney disease, thyroid disease, inflammatory bowel disease or cancer.",0),("Vomiting is different from coughing and from regurgitation. A video can help your vet tell them apart.",0)],
  faq=[("Is it normal for a cat to throw up hairballs?","Now and then, yes. VCA says more than once a month is a reason to contact your vet."),("Should I stop feeding my cat after vomiting?","Ask your vet first. Vets usually guide feeding after vomiting, and cats should not go long without eating.")],src=[VCA_VOMIT]),
}
BANNER=None
for p,a in A.items():
    f=p+"index.html"; s=BeautifulSoup(open(f).read(),"html.parser")
    for x in s.select(".samplepill"): x.decompose()
    b=s.select_one(".sample")
    if b: b.decompose()
    s.select_one(".answer p").string=a["short"]
    h=[x for x in s.find_all("h2") if x.get_text().strip() in ("What is going on","What the sources say")][0]
    h.string="What the sources say"
    nxt=h.find_next_sibling()
    while nxt and nxt.name!="h2": n2=nxt.find_next_sibling(); nxt.decompose(); nxt=n2
    frag="".join(f'<p>{t}'+(f' <sup><a href="#ref{i+1}">[{i+1}]</a></sup>' if i is not None else "")+'</p>' for t,i in a["body"])
    h.insert_after(BeautifulSoup(frag,"html.parser"))
    fq=s.select_one(".faq")
    fq.clear(); fq.append(BeautifulSoup("".join(f"<details open><summary>{q}</summary><p>{x}</p></details>" for q,x in a["faq"]),"html.parser"))
    sh=[x for x in s.find_all("h2") if x.get_text().strip()=="Sources"][0]
    nxt=sh.find_next_sibling()
    while nxt and nxt.name!="h2": n2=nxt.find_next_sibling(); nxt.decompose(); nxt=n2
    refs="".join(f'<li id="ref{i+1}"><a href="{u}" rel="nofollow">{t}</a>, checked {D}</li>' for i,(t,u) in enumerate(a["src"]))
    sh.insert_after(BeautifulSoup(f'<ol class="refs">{refs}</ol><p class="muted small">We summarize these sources in our own words. Dosing or home treatment amounts are never given here. Ask your vet.</p>',"html.parser"))
    open(f,"w").write(str(s))
print("updated",len(A))
