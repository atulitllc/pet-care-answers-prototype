"""Content for all 20 Paws Answered answers. Grounded only in the cited ASPCA, Cornell Feline Health Center and Pet Poison Helpline pages
(fetched Oct 13, 2026). No dosing. Used by add_answers.py. Each body item is (text, source index or None for general safety advice)."""
CB = "https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/"
S = dict(
 ASPCA_FOODS=("ASPCA Animal Poison Control: People Foods to Avoid Feeding Your Pets","https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
 ASPCA_DOG=("ASPCA: General Dog Care","https://www.aspca.org/pet-care/dog-care/general-dog-care"),
 ASPCA_CAT=("ASPCA: General Cat Care","https://www.aspca.org/pet-care/cat-care/general-cat-care"),
 ASPCA_LILY=("ASPCA Animal Poison Control: Toxic and Non-toxic Plants, Lily","https://www.aspca.org/pet-care/animal-poison-control/toxic-and-non-toxic-plants/lily"),
 PPH_CHOC=("Pet Poison Helpline: Chocolate","https://www.petpoisonhelpline.com/poison/chocolate/"),
 PPH_XYL=("Pet Poison Helpline: Xylitol","https://www.petpoisonhelpline.com/poison/xylitol/"),
 PPH_GRAPES=("Pet Poison Helpline: Grapes","https://www.petpoisonhelpline.com/poison/grapes/"),
 PPH_RAISINS=("Pet Poison Helpline: Raisins","https://www.petpoisonhelpline.com/poison/raisins/"),
 PPH_ONION=("Pet Poison Helpline: Onions","https://www.petpoisonhelpline.com/poison/onion/"),
 PPH_GARLIC=("Pet Poison Helpline: Garlic","https://www.petpoisonhelpline.com/poison/garlic/"),
 PPH_MACA=("Pet Poison Helpline: Macadamia Nuts","https://www.petpoisonhelpline.com/poison/macadamia-nuts/"),
 PPH_IBU=("Pet Poison Helpline: Ibuprofen","https://www.petpoisonhelpline.com/poison/ibuprofen/"),
 PPH_MJ=("Pet Poison Helpline: Marijuana","https://www.petpoisonhelpline.com/poison/marijuana/"),
 PPH_DOUGH=("Pet Poison Helpline: Bread Dough","https://www.petpoisonhelpline.com/poison/bread-dough/"),
 PPH_ACET=("Pet Poison Helpline: Acetaminophen","https://www.petpoisonhelpline.com/poison/acetaminophen/"),
 PPH_LILY=("Pet Poison Helpline: Lilies","https://www.petpoisonhelpline.com/poison/lilies/"),
 CORNELL_HAZ=("Cornell Feline Health Center: Common Cat Hazards",CB+"common-cat-hazards"),
 CORNELL_FEED=("Cornell Feline Health Center: Feeding Your Cat",CB+"feeding-your-cat"),
 CORNELL_OFTEN=("Cornell Feline Health Center: How Often Should You Feed Your Cat?","https://www.vet.cornell.edu/departments/cornell-feline-health-center/health-information/feline-health-topics/how-often-should-you-feed-your-cat"),
 CORNELL_VOMIT=("Cornell Feline Health Center: Vomiting",CB+"vomiting"),
 CORNELL_DIA=("Cornell Feline Health Center: Diarrhea",CB+"diarrhea"),
 CORNELL_HL=("Cornell Feline Health Center: Hepatic Lipidosis",CB+"hepatic-lipidosis"),
 CORNELL_FLEAS=("Cornell Feline Health Center: Fleas",CB+"fleas"),
)
A = {
 "dogs/can-dogs-eat-grapes/": {
  "h1": "Can dogs eat grapes?",
  "topic": "Food",
  "img": "dog-grapes",
  "alt": "A golden retriever puppy lying on the carpet at home",
  "toxic": True,
  "src": [
   "PPH_GRAPES",
   "PPH_RAISINS",
   "ASPCA_FOODS"
  ],
  "short": "No. Grapes, raisins, sultanas and currants are toxic to dogs. Pet Poison Helpline says eating them can cause vomiting, belly pain or diarrhea, followed quickly by kidney injury and kidney failure. The ASPCA also lists grapes and raisins as foods to keep away from pets. Call a vet or a pet poison hotline if your dog eats any.",
  "body": [
   [
    "Pet Poison Helpline lists common grapes, muscadines, raisins, sultanas and Zante or Corinthian currants as toxic for dogs.",
    0
   ],
   [
    "Poisoning starts with stomach and gut upset such as vomiting, belly pain and diarrhea, and is followed rapidly by kidney injury and kidney failure.",
    1
   ],
   [
    "Tartaric acid in grapes and raisins is the suspected toxin, but this has not been proven. Most reported poisonings are in dogs.",
    1
   ],
   [
    "The ASPCA notes that dogs cannot process tartaric acid, so grapes and raisins can lead to kidney damage.",
    2
   ]
  ],
  "vet": [
   "Your dog ate any grapes, raisins, sultanas or currants",
   "Vomiting, diarrhea or belly pain",
   "Drinking or peeing much more or less than usual"
  ],
  "faq": [
   [
    "What if my dog only ate one or two?",
    "Call anyway. Pet Poison Helpline notes that many factors, including the amount eaten and the size of the dog, decide what is toxic for a pet, so let an expert judge."
   ],
   [
    "Are cats at risk too?",
    "Pet Poison Helpline says poisoning is mainly reported in dogs, but it refers to companion animals in general, so keep grapes and raisins away from all pets."
   ]
  ]
 },
 "dogs/how-often-should-i-bathe-my-dog/": {
  "h1": "How often should I bathe my dog?",
  "topic": "Grooming",
  "img": "dog-bath",
  "alt": "A happy wet shepherd dog during a bath",
  "toxic": False,
  "src": [
   "ASPCA_DOG"
  ],
  "short": "Less often than you might think. The ASPCA says most dogs do not need a bath more than a few times a year. Regular brushing helps keep them clean in between. Before a bath, comb or cut out any mats, and rinse out all the soap so dirt does not stick to leftovers.",
  "body": [
   [
    "Most dogs do not need to be bathed more than a few times a year.",
    0
   ],
   [
    "Before a bath, comb or cut out mats from the coat.",
    0
   ],
   [
    "Rinse all soap out of the coat carefully, or dirt will stick to the leftover soap.",
    0
   ],
   [
    "Frequent brushing helps keep your dog clean and reduces shedding.",
    0
   ],
   [
    "Check for fleas and ticks every day in warm weather.",
    0
   ],
   [
    "If your dog has a skin problem or your vet prescribed a shampoo, follow your vet's instructions instead.",
    None
   ]
  ],
  "vet": [
   "Itching, redness, sores or hair loss",
   "A strong smell from the skin or ears",
   "Fleas or ticks you cannot get under control"
  ],
  "faq": [
   [
    "Does brushing replace bathing?",
    "Brushing does a lot of the work. The ASPCA recommends frequent brushing to keep dogs clean and cut shedding."
   ],
   [
    "What if my dog smells or itches a lot?",
    "Ask your vet. Odor and itching can be signs of a skin or ear problem."
   ]
  ]
 },
 "dogs/can-dogs-eat-chocolate/": {
  "h1": "Can dogs eat chocolate?",
  "topic": "Food",
  "img": "dog-chocolate",
  "alt": "A white dog stretched out asleep on a white couch",
  "toxic": True,
  "src": [
   "ASPCA_FOODS",
   "PPH_CHOC"
  ],
  "short": "No. Chocolate contains theobromine and caffeine, which can cause vomiting, diarrhea, panting, thirst, hyperactivity, an abnormal heart rhythm, tremors and seizures in dogs. Baking chocolate, cocoa powder and other dark chocolate are the most dangerous. If your dog eats chocolate, call your vet or a pet poison hotline right away.",
  "body": [
   [
    "Chocolate, coffee and caffeine contain methylxanthines. Pet Poison Helpline names the two in chocolate as theobromine and caffeine.",
    0
   ],
   [
    "In pets, methylxanthines can cause vomiting and diarrhea, panting, heavy thirst and peeing, hyperactivity, abnormal heart rhythm, tremors, seizures and even death.",
    0
   ],
   [
    "The darker the chocolate, the higher the risk. Baking chocolate and cocoa powder have the most methylxanthines. White chocolate has the least.",
    0
   ],
   [
    "How sick a dog gets depends on the amount and type of chocolate and the dog's size and health.",
    1
   ],
   [
    "Watch for less obvious sources such as cocoa mulch, hot cocoa, chocolate syrup, fudge and chocolate covered espresso beans.",
    1
   ],
   [
    "Chocolate candy and baked goods can also contain other poisons, such as macadamia nuts, raisins or xylitol.",
    1
   ]
  ],
  "vet": [
   "Your dog ate any chocolate, cocoa powder or chocolate baked goods",
   "Vomiting, diarrhea, panting or restlessness",
   "Tremors, seizures or a racing heart"
  ],
  "faq": [
   [
    "What if it was only milk or white chocolate?",
    "Call anyway. Risk depends on the type and amount and your dog's size. White chocolate has the least methylxanthine, but treats can hide other poisons."
   ],
   [
    "Is there a safe amount?",
    "Our sources do not give one for pet owners. Pet Poison Helpline asks you to call for a professional assessment."
   ]
  ]
 },
 "dogs/is-xylitol-toxic-to-dogs/": {
  "h1": "Is xylitol toxic to dogs?",
  "topic": "Food",
  "img": "dog-xylitol",
  "alt": "A fluffy brown dog sleeping on a kitchen floor",
  "toxic": True,
  "src": [
   "PPH_XYL",
   "ASPCA_FOODS"
  ],
  "short": "Yes. Xylitol is a sugar free sweetener found in gum, mints, candy, baked goods, toothpaste and some vitamins. In dogs it can cause a dangerous drop in blood sugar, sometimes within 10 to 15 minutes, and liver failure. If your dog eats anything with xylitol, call your vet or a pet poison hotline right away.",
  "body": [
   [
    "Xylitol is found in sugar free gum and mints, candy, puddings, sauces, syrups and jams, toothpaste, mouth rinses, chewable vitamins and other supplements, some nasal sprays and even makeup.",
    0
   ],
   [
    "The amount varies widely between products. Even different flavors of one gum brand can contain different amounts.",
    0
   ],
   [
    "If enough is eaten, xylitol can cause life threatening low blood sugar, sometimes within 10 to 15 minutes, and acute liver failure.",
    0
   ],
   [
    "First signs include vomiting, lethargy and loss of coordination, which can progress to seizures.",
    1
   ],
   [
    "Liver damage can happen within 12 to 24 hours and can lead to abnormal bleeding.",
    1
   ]
  ],
  "vet": [
   "Your dog ate gum, mints, candy or any product that may contain xylitol",
   "Vomiting, tiredness or wobbly walking",
   "Seizures or collapse"
  ],
  "faq": [
   [
    "How fast does xylitol work?",
    "Fast. Pet Poison Helpline says blood sugar can drop within 10 to 15 minutes, so call as soon as you know."
   ],
   [
    "Can I use my own toothpaste on my dog?",
    "The ASPCA lists toothpaste among products that can contain xylitol. Ask your vet which toothpaste to use."
   ]
  ]
 },
 "dogs/how-often-should-i-feed-my-dog/": {
  "h1": "How often should I feed my dog?",
  "topic": "Food",
  "img": "dog-feeding",
  "alt": "A green spiral slow feeder dog bowl seen from above",
  "toxic": False,
  "src": [
   "ASPCA_DOG"
  ],
  "short": "It depends on age. The ASPCA says puppies 8 to 12 weeks old need four meals a day, three to six months old need three, and six months to one year need two. After the first birthday, one meal a day is usually enough, but larger dogs and dogs prone to bloat do better with two smaller meals.",
  "body": [
   [
    "Puppies eight to 12 weeks old need four meals a day. From three to six months, feed three meals a day. From six months to one year, feed two.",
    0
   ],
   [
    "Once your dog turns one, one meal a day is usually enough. For larger dogs or dogs prone to bloat, two smaller meals are better.",
    0
   ],
   [
    "Extras such as cottage cheese, cooked egg, fruit or vegetables should be no more than ten percent of the daily food.",
    0
   ],
   [
    "Limit people food. It can cause vitamin and mineral imbalances, bone and teeth problems, picky eating and obesity.",
    0
   ],
   [
    "Keep clean, fresh water out at all times, and wash food and water dishes often.",
    0
   ],
   [
    "Ask your vet how much your dog should eat.",
    None
   ]
  ],
  "vet": [
   "Sudden weight loss or weight gain",
   "Your dog stops eating or eats much less than usual",
   "Vomiting or diarrhea after meals"
  ],
  "faq": [
   [
    "Why do big dogs get two meals?",
    "The ASPCA says larger dogs and dogs prone to bloat do better with two smaller meals than one big one."
   ],
   [
    "Can I add people food?",
    "Keep it small. The ASPCA says extras should be no more than ten percent of daily food, and too much people food can cause problems."
   ]
  ]
 },
 "dogs/can-dogs-eat-onions-or-garlic/": {
  "h1": "Can dogs eat onions or garlic?",
  "topic": "Food",
  "img": "dog-grass",
  "alt": "A Bernese Mountain Dog nibbling grass in a garden",
  "toxic": True,
  "src": [
   "ASPCA_FOODS",
   "PPH_ONION",
   "PPH_GARLIC"
  ],
  "short": "No. Onions, garlic, chives and leeks belong to the Allium family, which is poisonous to dogs. They can upset the stomach and damage red blood cells, leading to anemia. Risk depends on the amount eaten, and Japanese breeds such as Akitas and Shiba Inus are more sensitive. If your dog eats any, call your vet or a pet poison hotline.",
  "body": [
   [
    "Onion, garlic, chives and leeks are members of the Allium family. All are poisonous to dogs, cats and livestock.",
    1
   ],
   [
    "Alliums can irritate the stomach and gut and damage red blood cells, which can lead to anemia, meaning too few red blood cells.",
    0
   ],
   [
    "Pet Poison Helpline lists nausea, vomiting and diarrhea among the effects of a poisonous dose.",
    1
   ],
   [
    "Cats are more sensitive than dogs, but dogs are also at risk depending on the amount eaten.",
    0
   ],
   [
    "Some dog breeds are more sensitive, including Japanese breeds such as the Akita and Shiba Inu.",
    2
   ]
  ],
  "vet": [
   "Your dog ate onion, garlic, chives or leeks, or food made with them",
   "Vomiting or diarrhea",
   "Your dog seems weak or unwell after eating them"
  ],
  "faq": [
   [
    "Is garlic as risky as onion?",
    "Pet Poison Helpline lists garlic in the same Allium family with the same kind of red blood cell damage."
   ],
   [
    "Are green onions and shallots included?",
    "Yes. Pet Poison Helpline lists green onions and shallots among the alternate names for onion poisoning."
   ]
  ]
 },
 "dogs/can-dogs-eat-macadamia-nuts/": {
  "h1": "Can dogs eat macadamia nuts?",
  "topic": "Food",
  "img": "dog-diarrhea",
  "alt": "A pug sitting on a red patterned rug with a toy",
  "toxic": True,
  "src": [
   "ASPCA_FOODS",
   "PPH_MACA"
  ],
  "short": "No. Macadamia nuts can make dogs weak, wobbly and shaky, raise their body temperature and cause vomiting. The ASPCA says signs usually appear within 12 hours, and dogs usually recover within 24 to 72 hours. Their high oil content can also cause pancreatitis. Call your vet or a pet poison hotline if your dog eats any.",
  "body": [
   [
    "Macadamia nuts can cause weakness, poor coordination, depression, vomiting, tremors and overheating in dogs.",
    0
   ],
   [
    "Signs usually appear within 12 hours of eating them, with recovery expected within 24 to 72 hours.",
    0
   ],
   [
    "Pet Poison Helpline adds joint stiffness and being unable to walk because of weak back legs. How bad it gets depends on the amount eaten.",
    1
   ],
   [
    "The cause of the poisoning is unknown, but it can affect nerves and muscles. The high oil content can also cause pancreatitis.",
    1
   ],
   [
    "Other nuts such as almonds, pecans and walnuts are high in fat and can cause vomiting, diarrhea and possibly pancreatitis.",
    0
   ]
  ],
  "vet": [
   "Your dog ate macadamia nuts or cookies or candy containing them",
   "Weakness, wobbling, tremors or trouble walking",
   "Vomiting or feeling hot"
  ],
  "faq": [
   [
    "Will my dog be OK?",
    "The ASPCA says recovery is usually expected within 24 to 72 hours, but call so a vet can check the amount and watch for problems."
   ],
   [
    "What about chocolate covered macadamias?",
    "Call right away. Pet Poison Helpline warns chocolate treats can contain macadamia nuts, and chocolate is toxic too."
   ]
  ]
 },
 "dogs/is-ibuprofen-safe-for-dogs/": {
  "h1": "Is ibuprofen safe for dogs?",
  "topic": "Health",
  "img": "dog-temperature",
  "alt": "A black and white dog lying on an orange rug",
  "toxic": True,
  "src": [
   "PPH_IBU",
   "ASPCA_DOG"
  ],
  "short": "No. Pet Poison Helpline says ibuprofen is a human pain reliever that should not be given to pets. In toxic amounts it can cause stomach ulcers with bloody vomiting or diarrhea, kidney damage and coma. Never give your dog medicine your vet did not prescribe, and call a vet or poison hotline if your dog swallows any.",
  "body": [
   [
    "Ibuprofen is a non steroidal anti inflammatory drug, or NSAID, made for people. It should not be given to companion animals.",
    0
   ],
   [
    "In toxic amounts it can cause stomach and gut ulcers, with vomiting and diarrhea that may contain blood.",
    0
   ],
   [
    "It can also harm the kidneys. Dogs may pee much more at first, then little or not at all.",
    0
   ],
   [
    "Severe cases can affect the brain and nervous system, causing depression, coma and death.",
    0
   ],
   [
    "The ASPCA advises never giving your dog medication that has not been prescribed by a veterinarian.",
    1
   ]
  ],
  "vet": [
   "Your dog chewed into a pill bottle or swallowed any ibuprofen",
   "Vomiting, diarrhea or blood in vomit or stool",
   "Peeing much more or much less than usual, or seeming dull or weak"
  ],
  "faq": [
   [
    "What can I give my dog for pain?",
    "Only what your vet prescribes. The ASPCA says never to give a dog medication a vet has not prescribed."
   ],
   [
    "My dog only ate one pill. Is that OK?",
    "Call anyway. Pet Poison Helpline says the amount eaten and the size of the animal decide what is toxic, so let an expert judge."
   ]
  ]
 },
 "dogs/is-marijuana-toxic-to-dogs/": {
  "h1": "Is marijuana toxic to dogs?",
  "topic": "Health",
  "img": "dog-not-eating",
  "alt": "Two dogs resting under a blanket on a bed",
  "toxic": True,
  "src": [
   "PPH_MJ"
  ],
  "short": "Yes. Pet Poison Helpline says there is no safe dose of psychoactive marijuana for pets. Eating it or breathing the smoke can cause stomach upset, stumbling, a dazed or aggressive state, sudden flinching and leaking urine. Severe cases can lead to collapse, seizures or trouble breathing. Call your vet or a pet poison hotline right away.",
  "body": [
   [
    "Eating psychoactive marijuana can cause stomach and gut upset in pets.",
    0
   ],
   [
    "Nervous system signs include a stumbling walk, a dazed or aggressive mental state and sudden flinching. Pets may also leak urine.",
    0
   ],
   [
    "Severe signs can include collapse, seizures and difficulty breathing.",
    0
   ],
   [
    "Breathing in marijuana smoke can also poison a pet.",
    0
   ],
   [
    "There is no safe dose of psychoactive marijuana for companion animals.",
    0
   ]
  ],
  "vet": [
   "Your dog ate or was exposed to marijuana in any form",
   "Stumbling, a dazed look, flinching or leaking urine",
   "Collapse, seizures or trouble breathing"
  ],
  "faq": [
   [
    "Is secondhand smoke a risk?",
    "Yes. Pet Poison Helpline says inhaling psychoactive marijuana smoke can poison a pet."
   ],
   [
    "Is a small amount OK?",
    "No. Pet Poison Helpline says there is no safe dose of psychoactive marijuana for pets."
   ]
  ]
 },
 "dogs/can-dogs-eat-raw-bread-dough/": {
  "h1": "Can dogs eat raw bread dough?",
  "topic": "Food",
  "img": "dog-limping",
  "alt": "A person walking a black dog on a leash down a snowy street",
  "toxic": True,
  "src": [
   "ASPCA_FOODS",
   "PPH_DOUGH"
  ],
  "short": "No. Raw yeast dough keeps rising in a dog's warm stomach, which can cause painful bloating and, less often, a twisted stomach that is life threatening. The yeast also makes alcohol, which can cause alcohol poisoning with low blood sugar, weakness and seizures. If your dog eats raw dough, call your vet or a pet poison hotline right away.",
  "body": [
   [
    "Unbaked bread dough expands in the warm, moist stomach and can cause a bloated, swollen belly.",
    1
   ],
   [
    "Less often, this can progress to a twisted stomach, called gastric dilatation volvulus or bloat, which is life threatening.",
    1
   ],
   [
    "Signs of bloat include vomiting, retching with nothing coming up, a swollen belly, a fast heart rate, weakness and collapse.",
    1
   ],
   [
    "As yeast ferments the dough, it makes alcohol, which is quickly absorbed. Alcohol can cause dangerous drops in blood sugar, blood pressure and body temperature, and severe cases can lead to seizures.",
    1
   ],
   [
    "The ASPCA says to seek veterinary care promptly after any alcohol exposure, because alcohol is absorbed so fast.",
    0
   ]
  ],
  "vet": [
   "Your dog ate any raw yeast dough",
   "A swollen belly or retching with nothing coming up",
   "Staggering, weakness, vomiting or seeming drunk"
  ],
  "faq": [
   [
    "Is baked bread OK?",
    "Our sources warn about unbaked dough. The danger comes from the dough rising and the yeast making alcohol."
   ],
   [
    "Are cats at risk too?",
    "Yes. Pet Poison Helpline says unbaked bread dough can be dangerous for both dogs and cats."
   ]
  ]
 },
 "cats/can-cats-drink-milk/": {
  "h1": "Can cats drink milk?",
  "topic": "Food",
  "img": "cat-milk",
  "alt": "A tabby cat in a red holiday hat sitting by a little gnome figure",
  "toxic": False,
  "src": [
   "ASPCA_FOODS",
   "ASPCA_CAT"
  ],
  "short": "It is best not to give it. The ASPCA explains that pets do not have much lactase, the enzyme that breaks down lactose, so milk and dairy can cause diarrhea or other stomach upset. Fresh water is the drink cats need, so ask your vet before adding any new food or drink.",
  "body": [
   [
    "Pets do not make significant amounts of lactase, the enzyme that digests lactose in milk.",
    0
   ],
   [
    "Because of that, milk and other dairy foods can cause diarrhea or other digestive upset.",
    0
   ],
   [
    "Provide fresh, clean water at all times, and wash and refill your cat's water bowls daily.",
    1
   ],
   [
    "Treats should be no more than 5 to 10 percent of the diet.",
    1
   ]
  ],
  "vet": [
   "Diarrhea that lasts more than a day or two",
   "Vomiting along with diarrhea",
   "Your cat stops eating or seems tired"
  ],
  "faq": [
   [
    "What about cheese or yogurt?",
    "The ASPCA groups milk and other dairy based products together as possible causes of diarrhea and digestive upset."
   ],
   [
    "My cat drank some milk. Is that an emergency?",
    "Usually not, but watch for diarrhea or vomiting and call your vet if it continues."
   ]
  ]
 },
 "cats/why-is-my-cat-throwing-up/": {
  "h1": "Why is my cat throwing up?",
  "topic": "Health",
  "img": "cat-throwing-up",
  "alt": "A calm older tabby cat resting with eyes half closed",
  "toxic": False,
  "src": [
   "CORNELL_VOMIT"
  ],
  "short": "Even healthy cats vomit now and then, and bringing up a hairball every week or two is not unusual, says Cornell. See your vet promptly if your cat vomits more than once a week, or if vomiting comes with lethargy, weakness, poor appetite, blood, more thirst, changes in peeing or diarrhea.",
  "body": [
   [
    "Many cats vomit on occasion, and in many cases there is nothing to worry about.",
    0
   ],
   [
    "Hairballs are a common and usually harmless cause. A hairball every week or two is not unusual.",
    0
   ],
   [
    "Other common causes include eating poisonous plants, spoiled food, human medicines, string or yarn, antifreeze, human foods such as chocolate or onions, and small objects like rubber bands.",
    0
   ],
   [
    "Vomiting can also come from parasites, constipation, inflammatory bowel disease, a blockage, growths in the gut, diabetes, kidney disease or an overactive thyroid.",
    0
   ],
   [
    "Your vet will usually start with a history, an exam, bloodwork and a stool test, and may suggest X-rays or ultrasound.",
    0
   ]
  ],
  "vet": [
   "Vomiting more than once a week",
   "Lethargy, weakness or poor appetite",
   "Blood in the vomit, more thirst, changes in peeing, or diarrhea at the same time"
  ],
  "faq": [
   [
    "Are hairballs normal?",
    "Often, yes. Cornell says bringing up a hairball every week or two is not uncommon."
   ],
   [
    "Could my cat have swallowed something?",
    "Possibly. Cornell lists string, yarn, paper clips and rubber bands among things cats swallow. See your vet if you suspect it."
   ]
  ]
 },
 "cats/why-does-my-cat-have-diarrhea/": {
  "h1": "Why does my cat have diarrhea?",
  "topic": "Health",
  "img": "cat-diarrhea",
  "alt": "A calico kitten sitting in a green litter box",
  "toxic": False,
  "src": [
   "CORNELL_DIA"
  ],
  "short": "Often it is short lived. Cornell says a sudden diet change or stress, such as a long car trip, can cause a few days of loose stools. Diarrhea can also signal infection, inflammation, thyroid, kidney or liver disease, or cancer. Seek veterinary care soon if it lasts more than a day or two and your cat seems unwell.",
  "body": [
   [
    "Diarrhea means frequent, watery and often foul smelling stools that may look gray or yellow.",
    0
   ],
   [
    "In most cases it is short lived and either clears up by itself or improves with a change of diet.",
    0
   ],
   [
    "A sudden diet change or a stressful event, like a long car ride or a stay at a clinic, can cause a brief bout. Kittens may be at higher risk as they start solid food.",
    0
   ],
   [
    "Long lasting or repeated diarrhea can point to an overactive thyroid, kidney or liver disease, viral infection, panleukopenia, immune problems or lymphoma.",
    0
   ],
   [
    "Do not give over the counter medicines. Cornell warns some can be harmful to cats.",
    0
   ]
  ],
  "vet": [
   "Diarrhea that lasts more than a day or two",
   "Poor appetite, lethargy or vomiting along with diarrhea",
   "Blood or mucus in the stool"
  ],
  "faq": [
   [
    "Can stress cause diarrhea in cats?",
    "Yes. Cornell says a stressful event such as a long car trip can bring on a brief bout."
   ],
   [
    "Can I give my cat a human diarrhea medicine?",
    "No. Cornell warns some over the counter medicines can be harmful to cats. Ask your vet."
   ]
  ]
 },
 "cats/why-is-my-cat-not-eating/": {
  "h1": "Why is my cat not eating?",
  "topic": "Health",
  "img": "cat-not-eating",
  "alt": "An orange cat crouched beside a blue food bowl outdoors",
  "toxic": False,
  "src": [
   "CORNELL_HL",
   "CORNELL_FEED",
   "CORNELL_OFTEN"
  ],
  "short": "A cat that avoids food needs attention. Cornell explains that when cats stop eating, fat moves into the liver and can cause hepatic lipidosis, or fatty liver, which can be fatal if not treated promptly. It is more common in overweight cats and often follows another illness. Call your vet if your cat refuses food.",
  "body": [
   [
    "Hepatic lipidosis is almost always preceded by or comes with a cat nearly stopping eating. Fat that the body moves to the liver builds up in the liver cells.",
    0
   ],
   [
    "In more than 90 percent of cases it follows another problem, such as obesity, diabetes, cancer, an overactive thyroid, pancreatitis or kidney disease.",
    0
   ],
   [
    "Affected cats may hide, avoid the food bowl, drool, and show a yellow tinge in the ears and gums.",
    0
   ],
   [
    "Cornell says any cat that refuses to eat and is losing weight should be examined by a vet.",
    1
   ],
   [
    "Dental disease is common and can make dry food hard to chew. Wet food or smaller kibble may help.",
    2
   ]
  ],
  "vet": [
   "Your cat refuses food or barely eats",
   "Weight loss, hiding or drooling",
   "Yellow tinge to the gums, skin or ears"
  ],
  "faq": [
   [
    "Why are overweight cats at higher risk?",
    "Cornell notes fatty liver is seen in cats of all sizes, but it seems much more common in obese cats."
   ],
   [
    "My cat is just picky. What can I do?",
    "Cornell suggests offering two or three different cat foods for variety, but a cat that refuses to eat should see a vet."
   ]
  ]
 },
 "cats/why-is-my-cat-so-itchy/": {
  "h1": "Why is my cat so itchy?",
  "topic": "Health",
  "img": "cat-itchy",
  "alt": "A tabby cat lying on fallen leaves beside a garden path",
  "toxic": False,
  "src": [
   "CORNELL_FLEAS"
  ],
  "short": "Fleas are one of the most common reasons cats itch. Cornell says flea bites can cause intense itching, and constant scratching can open the skin to infection. Cats with flea allergy may get red, crusty bumps. Ask your vet about flea control, because some products can harm cats if used wrongly.",
  "body": [
   [
    "Cat fleas are tiny, from the size of a pinhead to about an eighth of an inch.",
    0
   ],
   [
    "Flea bites can cause intense itching, and a sensitive cat's constant scratching can open wounds that may become infected.",
    0
   ],
   [
    "Cats are bitten mostly on the back of the neck and at the base of the tail. Cats with flea allergy may get red, crusty bumps even where they have not scratched.",
    0
   ],
   [
    "Fleas can carry tapeworm eggs and bacteria, and heavy infestations can cause anemia in kittens.",
    0
   ],
   [
    "Treating the cat is not enough. Vacuum furniture, rugs and carpets carefully, and treat the home as well.",
    0
   ],
   [
    "Flea products can harm cats or people if misused, so use them only with your vet's guidance.",
    0
   ]
  ],
  "vet": [
   "Scratching that causes sores, scabs or hair loss",
   "Fleas on a kitten, or a kitten that seems weak or pale",
   "Itching that continues after flea control"
  ],
  "faq": [
   [
    "Can cat fleas affect people?",
    "Yes. Cornell says cat fleas can carry germs that cause cat scratch disease, murine typhus and plague in people."
   ],
   [
    "Why treat the house too?",
    "Cornell says skipping the home lets fleas come back, so the problem never fully goes away."
   ]
  ]
 },
 "cats/how-often-should-i-feed-my-cat/": {
  "h1": "How often should I feed my cat?",
  "topic": "Food",
  "img": "cat-knead",
  "alt": "An orange kitten stretching across a soft blanket",
  "toxic": False,
  "src": [
   "CORNELL_OFTEN",
   "ASPCA_CAT"
  ],
  "short": "It depends on age. Cornell says kittens usually do best with three meals a day until six months old, then two meals a day until they turn one. Most adult cats do well fed once or twice a day. Keep fresh water out at all times, and ask your vet how much your cat should eat.",
  "body": [
   [
    "Kittens need more food for their weight than adults, so they should eat more often. Until six months, three meals a day usually works best. From six months to one year, twice a day is generally best.",
    0
   ],
   [
    "From about one year old, feeding once or twice a day suits most cats. Senior cats can usually keep the same routine unless your vet says otherwise.",
    0
   ],
   [
    "Free feeding dry food works for some cats, but others overeat and gain weight. Replace any food left out with fresh food every day.",
    0
   ],
   [
    "Pick a feeding time that fits your schedule and keep it consistent.",
    0
   ],
   [
    "Provide fresh, clean water at all times. Treats should be no more than 5 to 10 percent of the diet.",
    1
   ]
  ],
  "vet": [
   "Your cat refuses food or eats much less",
   "Sudden weight loss or weight gain",
   "Trouble chewing or dropping food"
  ],
  "faq": [
   [
    "Should I leave dry food out all day?",
    "Cornell says it may be fine for some cats, but others overeat. Any food left out should be replaced daily."
   ],
   [
    "Does my senior cat need a different schedule?",
    "Cornell says cats 10 and older can usually keep the same routine unless your vet advises a change."
   ]
  ]
 },
 "cats/is-tylenol-toxic-to-cats/": {
  "h1": "Is Tylenol (acetaminophen) toxic to cats?",
  "topic": "Health",
  "img": "cat-temperature",
  "alt": "A tabby cat dozing on a fluffy white blanket",
  "toxic": True,
  "src": [
   "PPH_ACET",
   "ASPCA_CAT"
  ],
  "short": "Yes. Acetaminophen, the pain and fever reducer in Tylenol and many cold, flu and allergy products, is especially dangerous for cats, says Pet Poison Helpline. It can cause stomach upset, blood problems and liver failure. Never give your cat any medicine your vet did not prescribe, and call a vet or poison hotline if your cat swallows any.",
  "body": [
   [
    "Acetaminophen is a common over the counter medicine that reduces pain and fever. It is also in some prescription pain medicines.",
    0
   ],
   [
    "Check labels on products for cold and flu symptoms, allergies and fever, which may contain acetaminophen.",
    0
   ],
   [
    "It is safe for people, has a narrower margin of safety in dogs, and is especially dangerous for cats.",
    0
   ],
   [
    "Signs can include stomach and gut upset, blood problems and liver failure.",
    0
   ],
   [
    "The ASPCA advises never giving your cat medication that has not been prescribed by a veterinarian.",
    1
   ]
  ],
  "vet": [
   "Your cat swallowed any acetaminophen or a cold, flu or allergy medicine",
   "Vomiting or drooling",
   "Your cat seems weak, tired or unwell"
  ],
  "faq": [
   [
    "Is Tylenol safe for my dog instead?",
    "Ask your vet. Pet Poison Helpline says acetaminophen has a narrower margin of safety in dogs than in people."
   ],
   [
    "Which products contain acetaminophen?",
    "Pet Poison Helpline says to look for it in products labeled for cold and flu, allergies and fever."
   ]
  ]
 },
 "cats/are-lilies-poisonous-to-cats/": {
  "h1": "Are lilies poisonous to cats?",
  "topic": "Health",
  "img": "cat-lilies",
  "alt": "White Easter lily flowers in bloom",
  "toxic": True,
  "src": [
   "PPH_LILY",
   "ASPCA_LILY",
   "CORNELL_HAZ"
  ],
  "short": "Yes. Lilies from the Lilium genus, such as Easter, tiger and stargazer lilies, are highly toxic to cats. Any amount of the leaf, stem, flower, pollen or even the vase water can cause kidney failure. If your cat touches or chews a lily, take your cat to a vet immediately.",
  "body": [
   [
    "All parts of lilies in the Lilium genus are toxic to cats, including any amount of leaf, stem, flower, pollen, vase water or root.",
    0
   ],
   [
    "Eating them can lead to vomiting, belly pain, dehydration and acute kidney failure. Early treatment is vital after any exposure.",
    0
   ],
   [
    "Pet Poison Helpline lists Easter, Madonna, Oriental, Stargazer and Tiger lilies among the dangerous types.",
    0
   ],
   [
    "The ASPCA lists lilies as toxic to cats, with kidney failure as the main sign.",
    1
   ],
   [
    "Cornell says lilies can cause life threatening kidney failure even in tiny amounts. The safest choice is to keep lilies out of homes with cats.",
    2
   ]
  ],
  "vet": [
   "Your cat chewed, licked or touched any part of a lily, or drank vase water",
   "Vomiting, belly pain or not eating",
   "Drinking or peeing much more or less than usual"
  ],
  "faq": [
   [
    "My cat only licked some pollen. Is that a problem?",
    "Yes. Pet Poison Helpline says any amount of pollen can be toxic. Go to a vet right away."
   ],
   [
    "Are lilies dangerous to dogs too?",
    "The ASPCA lists Lilium lilies as non toxic to dogs. The serious kidney risk is for cats."
   ]
  ]
 },
 "cats/can-cats-eat-onions-or-garlic/": {
  "h1": "Can cats eat onions or garlic?",
  "topic": "Food",
  "img": "cat-onions",
  "alt": "A calico cat sitting on a dark rug looking up",
  "toxic": True,
  "src": [
   "ASPCA_FOODS",
   "PPH_ONION",
   "PPH_GARLIC"
  ],
  "short": "No. Onions, garlic, chives and leeks belong to the Allium family, which is poisonous to cats. Cats are more sensitive than dogs. These foods can upset the stomach and damage red blood cells, which can lead to anemia. If your cat eats any, call your vet or a pet poison hotline.",
  "body": [
   [
    "Onion, garlic, chives and leeks belong to the Allium family, and all are poisonous to dogs, cats and livestock.",
    1
   ],
   [
    "Allium plants can irritate the stomach and gut and damage red blood cells, which can lead to anemia, meaning too few red blood cells.",
    0
   ],
   [
    "Cats are more sensitive than dogs, although dogs are also at risk depending on the amount eaten.",
    0
   ],
   [
    "Pet Poison Helpline lists nausea, vomiting and diarrhea among the effects of a poisonous dose.",
    1
   ],
   [
    "Garlic is in the same family and carries the same risk.",
    2
   ]
  ],
  "vet": [
   "Your cat ate onion, garlic, chives or leeks, or food made with them",
   "Vomiting or diarrhea",
   "Your cat seems unwell in any way after eating them"
  ],
  "faq": [
   [
    "Is a little garlic in food OK for cats?",
    "Our sources say Alliums are poisonous to cats and cats are more sensitive than dogs. Ask your vet or a poison hotline about any amount."
   ],
   [
    "Are cooked or powdered onions safer?",
    "Our sources list onion, garlic, chives and leeks as toxic without exceptions for cooking. Call your vet."
   ]
  ]
 },
 "cats/can-cats-eat-chocolate/": {
  "h1": "Can cats eat chocolate?",
  "topic": "Food",
  "img": "cat-chocolate",
  "alt": "A small tabby kitten staring at the camera",
  "toxic": True,
  "src": [
   "CORNELL_HAZ",
   "ASPCA_FOODS",
   "PPH_CHOC"
  ],
  "short": "No. Cornell lists chocolate among human foods that are off limits for cats. Chocolate contains methylxanthines, which can cause vomiting, diarrhea, hyperactivity, an abnormal heart rhythm, tremors and seizures in pets. Darker chocolate is more dangerous. If your cat eats chocolate, call your vet or a pet poison hotline.",
  "body": [
   [
    "Cornell lists chocolate, along with grapes, raisins, onions, avocados and anything with xylitol, as foods that are off limits for cats.",
    0
   ],
   [
    "Chocolate, coffee and caffeine contain methylxanthines. In pets these can cause vomiting and diarrhea, panting, thirst and peeing more, hyperactivity, abnormal heart rhythm, tremors, seizures and even death.",
    1
   ],
   [
    "The darker the chocolate, the higher the risk. Baking chocolate and cocoa powder have the most methylxanthines. White chocolate has the least.",
    1
   ],
   [
    "How sick a pet gets depends on the amount and type of chocolate and the pet's size and health. Chocolate treats can also contain other poisons such as raisins or xylitol.",
    2
   ]
  ],
  "vet": [
   "Your cat ate chocolate, cocoa powder or chocolate baked goods",
   "Vomiting, diarrhea, restlessness or panting",
   "Tremors, seizures or a racing heart"
  ],
  "faq": [
   [
    "Is white chocolate safe for cats?",
    "No. It has the least methylxanthine, but the ASPCA still lists chocolate as a food to avoid, and treats may have other harmful ingredients."
   ],
   [
    "What about coffee or tea?",
    "The ASPCA groups coffee and caffeine with chocolate because they contain the same type of compound."
   ]
  ]
 }
}
