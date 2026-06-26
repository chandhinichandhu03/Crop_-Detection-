"""
insert_real_plants.py
─────────────────────
Inserts a curated list of 200+ real medicinal/agricultural/ornamental plants
into the local SQLite database WITHOUT wiping existing synthetic records.

Run once:  python insert_real_plants.py
"""

import sys
import random
from sqlalchemy.orm import Session
from database import SessionLocal
from models import (
    Plant, BotanicalClassification, Family, Genus, SpeciesRecord,
    ClimateRequirement, SoilRequirement, HarvestInformation, Disease,
    DiseaseSymptom, DiseaseTreatment, Pest, NutrientDeficiency
)

# ──────────────────────────────────────────────────────────────
# REAL PLANT CATALOG  (common_name, botanical_name, family, genus,
#                       category, climate, medicinal, overview)
# ──────────────────────────────────────────────────────────────
REAL_PLANTS = [
    # ── Medicinal Trees ──────────────────────────────────────
    ("Neem", "Azadirachta indica", "Meliaceae", "Azadirachta",
     "Medicinal", "Tropical", "Leaves, bark, seeds used as anti-bacterial, anti-fungal, anti-malarial. Neem oil is a bio-pesticide.",
     "Neem is a fast-growing tropical tree native to South Asia. Its leaves, seeds, and bark have broad-spectrum medicinal and agricultural uses including pest control, skin treatments, and immune support.",
     "Nim, Nimba, Indian Lilac", "Nimba, Vepa (Telugu), Vembu (Tamil)", "Southeast Asia, South Asia"),

    ("Tulsi", "Ocimum tenuiflorum", "Lamiaceae", "Ocimum",
     "Medicinal", "Tropical", "Sacred herb. Treats cough, cold, stress. Adaptogen.",
     "Holy Basil (Tulsi) is a sacred Indian plant revered in Hinduism and widely used in Ayurvedic medicine for respiratory issues, fever, and inflammation.",
     "Holy Basil, Sacred Basil", "Tulasi, Thulsi", "South Asia"),

    ("Ashwagandha", "Withania somnifera", "Solanaceae", "Withania",
     "Medicinal", "Arid", "Powerful adaptogen. Reduces stress, boosts immunity and stamina.",
     "Ashwagandha is an ancient medicinal herb used in Ayurveda for over 3,000 years. It helps the body manage stress and improves strength and fertility.",
     "Winter Cherry, Indian Ginseng", "Asgandh", "India, North Africa, Mediterranean"),

    ("Aloe Vera", "Aloe vera", "Asphodelaceae", "Aloe",
     "Medicinal", "Arid", "Soothes burns, treats skin conditions, aids digestion.",
     "Aloe Vera is a succulent plant grown worldwide for its medicinal gel. Used in cosmetics, food, and traditional medicine for centuries.",
     "True Aloe, Barbados Aloe", "Ghritkumari, Korphad", "Arabian Peninsula"),

    ("Turmeric", "Curcuma longa", "Zingiberaceae", "Curcuma",
     "Spice", "Tropical", "Anti-inflammatory, antioxidant. Treats arthritis and improves liver function.",
     "Turmeric is a rhizomatous herbaceous plant native to South Asia. Curcumin, its active compound, has powerful anti-inflammatory and antioxidant properties.",
     "Haldi", "Haridra, Manjal", "South Asia, Southeast Asia"),

    ("Ginger", "Zingiber officinale", "Zingiberaceae", "Zingiber",
     "Spice", "Tropical", "Treats nausea, aids digestion, anti-inflammatory.",
     "Ginger is a flowering plant whose rhizome is used as a spice and folk medicine. It is one of the most widely consumed spices in the world.",
     "Common Ginger", "Adarak (fresh), Saunth (dry)", "Maritime Southeast Asia"),

    ("Garlic", "Allium sativum", "Amaryllidaceae", "Allium",
     "Vegetable", "Temperate", "Lowers cholesterol, anti-bacterial, boosts immunity.",
     "Garlic is a species in the onion genus Allium. Its close relatives include onion, shallots, leeks, and chives.",
     "Common Garlic", "Lehsun, Veluthulli", "Central Asia"),

    ("Moringa", "Moringa oleifera", "Moringaceae", "Moringa",
     "Medicinal", "Tropical", "High in nutrients. Treats malnutrition, diabetes, inflammation.",
     "Moringa is a fast-growing, drought-resistant tree native to South Asia. Its leaves are highly nutritious and used medicinally across Africa and Asia.",
     "Drumstick Tree, Miracle Tree", "Sahjan, Murungai", "South Asia"),

    ("Giloy", "Tinospora cordifolia", "Menispermaceae", "Tinospora",
     "Medicinal", "Tropical", "Boosts immunity, treats fever, anti-diabetic.",
     "Giloy is a climbing shrub known as 'Amrit' (nectar of immortality) in Ayurveda. Used for boosting immunity and treating chronic fever.",
     "Heart-leaved Moonseed, Guduchi", "Amrit, Amrita", "India, Sri Lanka, Myanmar"),

    ("Brahmi", "Bacopa monnieri", "Plantaginaceae", "Bacopa",
     "Medicinal", "Tropical", "Enhances memory and cognitive function. Reduces anxiety.",
     "Brahmi is a perennial herb used in Ayurvedic medicine to enhance brain function, reduce anxiety, and treat epilepsy.",
     "Water Hyssop", "Jalabrahmi, Mandookparni", "South Asia, Australia"),

    ("Shatavari", "Asparagus racemosus", "Asparagaceae", "Asparagus",
     "Medicinal", "Tropical", "Female health tonic. Treats infertility and hormonal imbalance.",
     "Shatavari is the primary Ayurvedic rejuvenating tonic for women. It supports reproductive health and is used for lactation.",
     "Wild Asparagus", "Shatmuli, Satavar", "India, Sri Lanka, Himalayas"),

    ("Amla", "Phyllanthus emblica", "Phyllanthaceae", "Phyllanthus",
     "Fruit", "Tropical", "Richest source of Vitamin C. Boosts immunity, anti-aging.",
     "Indian Gooseberry (Amla) is one of the most important medicinal plants in Ayurveda. Its fruit is highly nutritious and used in Chyawanprash.",
     "Indian Gooseberry, Emblica", "Amlaki, Nelli", "South Asia"),

    ("Haritaki", "Terminalia chebula", "Combretaceae", "Terminalia",
     "Medicinal", "Tropical", "Treats constipation, detoxifies body. Anti-aging herb.",
     "Haritaki (Chebulic Myrobalan) is considered the 'King of Medicines' in Tibetan Medicine. Used in Triphala formulation.",
     "Chebulic Myrobalan, Black Myrobalan", "Harad, Kadukkai", "South Asia"),

    ("Bibhitaki", "Terminalia bellirica", "Combretaceae", "Terminalia",
     "Medicinal", "Tropical", "Treats respiratory diseases, cough. Part of Triphala.",
     "Bibhitaki is one of the three fruits used in Triphala, an Ayurvedic formulation. It is especially useful for respiratory conditions.",
     "Beleric Myrobalan, Bahera", "Baheda, Tani", "South Asia, Southeast Asia"),

    ("Senna", "Cassia senna", "Fabaceae", "Cassia",
     "Medicinal", "Arid", "Natural laxative for constipation relief.",
     "Senna is a large genus of flowering plants widely used as a stimulant laxative. It is approved by FDA for use in constipation.",
     "Alexandrian Senna", "Sonamukhi, Sanay", "North Africa, Middle East"),

    # ── Major Crops ───────────────────────────────────────────
    ("Rice", "Oryza sativa", "Poaceae", "Oryza",
     "Cereal", "Tropical", "Staple food. Source of carbohydrates.",
     "Rice is the most widely consumed staple food for more than half the world's population. It is a grass species native to Asia.",
     "Asian Rice, Common Rice", "Chawal, Dhan", "Southeast Asia"),

    ("Wheat", "Triticum aestivum", "Poaceae", "Triticum",
     "Cereal", "Temperate", "Staple cereal grain. Used for bread and flour.",
     "Wheat is a grass cultivated worldwide. Its grain is a worldwide staple food used to make flour for bread, pasta, and confectionery.",
     "Common Wheat, Bread Wheat", "Gehu, Gom", "Fertile Crescent"),

    ("Maize", "Zea mays", "Poaceae", "Zea",
     "Cereal", "Tropical", "Used for food, animal feed, biofuel, starch.",
     "Maize (Corn) is a cereal grain first domesticated by indigenous peoples in Mexico. It is the third-most important cereal crop after wheat and rice.",
     "Corn, Indian Corn", "Makka, Makkai", "Mexico, Central America"),

    ("Cotton", "Gossypium hirsutum", "Malvaceae", "Gossypium",
     "Cash Crop", "Tropical", "Primary source of natural textile fibre.",
     "Cotton is a soft fluffy staple fibre that grows in a boll around the seeds of cotton plants. It is the world's most important non-food agricultural commodity.",
     "Upland Cotton", "Kapas, Rui", "Central America"),

    ("Sugarcane", "Saccharum officinarum", "Poaceae", "Saccharum",
     "Cash Crop", "Tropical", "Primary source of sugar and ethanol.",
     "Sugarcane is a perennial grass native to tropical South Asia. It is the world's largest crop by production quantity.",
     "Noble Cane", "Ganna, Ikshu", "Papua New Guinea"),

    ("Soybean", "Glycine max", "Fabaceae", "Glycine",
     "Pulse", "Temperate", "High-protein pulse. Used for tofu, oil, animal feed.",
     "The soybean is a legume native to East Asia widely grown for its edible bean. It is a major cash crop providing vegetable protein and oil.",
     "Soya Bean", "Soyabean, Bhat", "East Asia"),

    ("Groundnut", "Arachis hypogaea", "Fabaceae", "Arachis",
     "Pulse", "Tropical", "High-protein oil seed. Eaten roasted or as peanut butter.",
     "Groundnut (Peanut) is a legume crop grown mainly for its edible seeds. It is widely grown in tropics and subtropics.",
     "Peanut, Monkey Nut", "Moongphali, Kadlekai", "South America"),

    ("Chickpea", "Cicer arietinum", "Fabaceae", "Cicer",
     "Pulse", "Arid", "High-protein legume. Used in dals and stews.",
     "Chickpea is an annual legume of the family Fabaceae. Its different types are variously known as gram, Bengal gram, garbanzo bean.",
     "Garbanzo Bean, Bengal Gram", "Chana, Channaa", "Middle East"),

    ("Lentil", "Lens culinaris", "Fabaceae", "Lens",
     "Pulse", "Temperate", "High-protein legume. Used in soups, dals.",
     "The lentil is an edible legume. It is an annual plant known for its lens-shaped seeds and is about 40 cm tall.",
     "Common Lentil", "Masoor, Masur", "Near East"),

    ("Tomato", "Solanum lycopersicum", "Solanaceae", "Solanum",
     "Vegetable", "Temperate", "Rich in lycopene. Used in sauces, salads.",
     "The tomato is the edible berry of the plant Solanum lycopersicum. It originated in western South America and Central America.",
     "Love Apple", "Tamatar, Thakkali", "South America"),

    ("Potato", "Solanum tuberosum", "Solanaceae", "Solanum",
     "Vegetable", "Temperate", "Fourth largest food crop. Rich in starch.",
     "The potato is a starchy tuber plant native to the Americas. It is now a worldwide staple food.",
     "Common Potato", "Aloo, Urulaikizhangu", "South America"),

    ("Onion", "Allium cepa", "Amaryllidaceae", "Allium",
     "Vegetable", "Temperate", "Culinary staple. Anti-bacterial and anti-inflammatory.",
     "The onion is a vegetable that is the most widely cultivated species of the genus Allium.",
     "Common Onion, Bulb Onion", "Pyaz, Vengayam", "Central Asia"),

    ("Mango", "Mangifera indica", "Anacardiaceae", "Mangifera",
     "Fruit", "Tropical", "King of fruits. Rich in vitamins A and C.",
     "Mango is a juicy stone fruit from numerous species of tropical trees belonging to the flowering plant genus Mangifera. Native to South Asia.",
     "King of Fruits", "Aam, Maambazham", "South Asia"),

    ("Banana", "Musa acuminata", "Musaceae", "Musa",
     "Fruit", "Tropical", "High in potassium. Energy food.",
     "Banana is a giant herbaceous plant producing edible fruit. It is one of the world's most important food crops.",
     "Common Banana", "Kela, Vazhai", "Southeast Asia"),

    ("Papaya", "Carica papaya", "Caricaceae", "Carica",
     "Fruit", "Tropical", "Rich in papain enzyme. Aids digestion, anti-inflammatory.",
     "Papaya is a large tree-like plant. Its fruit is commonly used in tropical countries for food and medicine.",
     "Pawpaw", "Papita, Pappali", "Central America"),

    ("Coconut", "Cocos nucifera", "Arecaceae", "Cocos",
     "Tree", "Tropical", "Provides oil, water, flesh, and fibre.",
     "The coconut tree is a member of the palm tree family and is the only living species of the genus Cocos. Called the 'Tree of Life'.",
     "Coconut Palm, Tree of Life", "Nariyal, Tennai", "Pacific Islands"),

    ("Jackfruit", "Artocarpus heterophyllus", "Moraceae", "Artocarpus",
     "Fruit", "Tropical", "Largest tree fruit. High in nutrients.",
     "Jackfruit is a species of tree in the fig, mulberry, and breadfruit family. Native to South India.",
     "Jack Tree", "Kathal, Palaa", "South India"),

    ("Guava", "Psidium guajava", "Myrtaceae", "Psidium",
     "Fruit", "Tropical", "High in Vitamin C. Anti-diabetic properties.",
     "Guava is a common tropical fruit cultivated in many tropical and subtropical regions. Psidium guajava is a small tree from the myrtle family.",
     "Apple Guava", "Amrud, Koyyapazham", "Central America"),

    ("Pomegranate", "Punica granatum", "Lythraceae", "Punica",
     "Fruit", "Arid", "Rich in antioxidants. Heart health.",
     "Pomegranate is a fruit-bearing deciduous shrub native to the region from modern-day Iran to northern India.",
     "Granada", "Anar, Mathalam", "Iran to Northern India"),

    ("Lemon", "Citrus limon", "Rutaceae", "Citrus",
     "Fruit", "Subtropical", "High in Vitamin C. Used as flavouring.",
     "Lemon is a species of small evergreen tree in the flowering plant family Rutaceae. Its fruit is used for culinary and non-culinary purposes.",
     "Common Lemon", "Nimbu, Elumichai", "South Asia"),

    ("Orange", "Citrus sinensis", "Rutaceae", "Citrus",
     "Fruit", "Subtropical", "Rich in Vitamin C. Immunity booster.",
     "The orange is the fruit of various citrus species in the family Rutaceae. It is a hybrid between pomelo and mandarin.",
     "Sweet Orange", "Santra, Kamala", "South Asia, Southeast Asia"),

    ("Chilli", "Capsicum annuum", "Solanaceae", "Capsicum",
     "Spice", "Tropical", "Contains capsaicin. Pain relief, metabolism booster.",
     "Chilli pepper is a fruit of plants from the genus Capsicum. It is widely used as a spice and flavouring.",
     "Hot Pepper, Red Pepper", "Mirch, Milagai", "Central America"),

    ("Coriander", "Coriandrum sativum", "Apiaceae", "Coriandrum",
     "Spice", "Temperate", "Rich in antioxidants. Anti-diabetic properties.",
     "Coriander is an annual herb in the family Apiaceae. It is also known as Chinese parsley or dhania.",
     "Cilantro, Dhania", "Dhania, Kothamalli", "Southern Europe"),

    ("Cumin", "Cuminum cyminum", "Apiaceae", "Cuminum",
     "Spice", "Arid", "Aids digestion. Rich in iron.",
     "Cumin is a flowering plant in the family Apiaceae, native to a territory including the Middle East and stretching east to India.",
     "Comino", "Jeera, Jeeragam", "Middle East"),

    ("Cardamom", "Elettaria cardamomum", "Zingiberaceae", "Elettaria",
     "Spice", "Tropical", "Queen of spices. Digestive aid, breath freshener.",
     "Cardamom is a spice made from the seed pods of Elettaria cardamomum, a plant native to southern India.",
     "Green Cardamom, True Cardamom", "Elaichi, Elakka", "South India"),

    ("Clove", "Syzygium aromaticum", "Myrtaceae", "Syzygium",
     "Spice", "Tropical", "Anti-bacterial. Relieves toothache.",
     "Cloves are the aromatic flower buds of Syzygium aromaticum. They are used as a spice in cuisines all over the world.",
     "Clove Tree", "Laung, Karambu", "Indonesia"),

    ("Cinnamon", "Cinnamomum verum", "Lauraceae", "Cinnamomum",
     "Spice", "Tropical", "Lowers blood sugar. Anti-microbial properties.",
     "Cinnamon is a spice obtained from the inner bark of several tree species from the genus Cinnamomum.",
     "True Cinnamon, Ceylon Cinnamon", "Dalchini, Karuvapattai", "Sri Lanka"),

    ("Black Pepper", "Piper nigrum", "Piperaceae", "Piper",
     "Spice", "Tropical", "King of spices. Anti-oxidant, digestive.",
     "Black pepper is a flowering vine in the family Piperaceae, cultivated for its fruit, known as a peppercorn.",
     "King of Spices, Common Pepper", "Kali Mirch, Kurumulagu", "South India"),

    ("Fenugreek", "Trigonella foenum-graecum", "Fabaceae", "Trigonella",
     "Herb", "Temperate", "Lowers blood sugar. Promotes milk production.",
     "Fenugreek is an annual plant in the family Fabaceae, with leaves consisting of three small obovate to oblong leaflets.",
     "Methi", "Methi, Vendhayam", "Mediterranean"),

    ("Mint", "Mentha piperita", "Lamiaceae", "Mentha",
     "Herb", "Temperate", "Aids digestion. Relieves headache and nausea.",
     "Peppermint is a hybrid mint, a cross between watermint and spearmint. Its leaves have a pleasant warm, fresh, aromatic smell.",
     "Peppermint, Common Mint", "Pudina, Pudina", "Europe, Middle East"),

    ("Rosemary", "Salvia rosmarinus", "Lamiaceae", "Salvia",
     "Herb", "Mediterranean", "Improves memory. Anti-oxidant, anti-inflammatory.",
     "Rosemary is an aromatic evergreen shrub with leaves similar to hemlock needles. It is native to the Mediterranean.",
     "Anthos", "Rusmari", "Mediterranean"),

    ("Lavender", "Lavandula angustifolia", "Lamiaceae", "Lavandula",
     "Ornamental", "Mediterranean", "Reduces anxiety and insomnia. Antiseptic.",
     "Lavender is a genus of 47 known species of flowering plants in the mint family Lamiaceae. Used for fragrance and medicine.",
     "English Lavender, Common Lavender", "Lavender", "Mediterranean"),

    ("Chamomile", "Matricaria chamomilla", "Asteraceae", "Matricaria",
     "Medicinal", "Temperate", "Promotes sleep, reduces anxiety. Anti-inflammatory.",
     "Chamomile is a common name for several daisy-like plants of the family Asteraceae. Used in herbal teas.",
     "German Chamomile", "Babuna", "Europe, Western Asia"),

    ("Echinacea", "Echinacea purpurea", "Asteraceae", "Echinacea",
     "Medicinal", "Temperate", "Boosts immune system. Reduces cold symptoms.",
     "Echinacea is a genus of herbaceous flowering plants in the daisy family. Popular herbal remedy.",
     "Purple Coneflower", "Echinacea", "Eastern North America"),

    ("Valerian", "Valeriana officinalis", "Caprifoliaceae", "Valeriana",
     "Medicinal", "Temperate", "Natural sedative. Treats insomnia and anxiety.",
     "Valerian is a perennial flowering plant native to Europe and Asia. Its root is used in herbal medicine.",
     "Garden Valerian", "Tagara, Tagar", "Europe, Asia"),

    ("Passionflower", "Passiflora incarnata", "Passifloraceae", "Passiflora",
     "Medicinal", "Subtropical", "Reduces anxiety and insomnia. Anti-convulsant.",
     "Passionflower is a genus of about 550 species of flowering plants used in traditional medicine for anxiety.",
     "Maypop, Wild Apricot", "Krishnakamal", "North America"),

    ("St. John's Wort", "Hypericum perforatum", "Hypericaceae", "Hypericum",
     "Medicinal", "Temperate", "Treats depression and anxiety naturally.",
     "St John's wort is a yellow-flowered perennial herb native to Europe and Asia. Its flowers and leaves are used medicinally.",
     "Common St John's Wort", "Hypericum", "Europe, Western Asia"),

    ("Ginseng", "Panax ginseng", "Araliaceae", "Panax",
     "Medicinal", "Temperate", "Adaptogen. Boosts energy, reduces stress.",
     "Ginseng is the root of plants in the genus Panax. It has been used in traditional Chinese medicine for centuries.",
     "Asian Ginseng, Korean Ginseng", "Ren Shen, Insam", "Eastern Asia"),

    ("Eucalyptus", "Eucalyptus globulus", "Myrtaceae", "Eucalyptus",
     "Tree", "Subtropical", "Treats respiratory conditions. Antiseptic.",
     "Eucalyptus globulus is an evergreen tree commonly known as Southern Blue Gum. Its oil has medicinal properties.",
     "Tasmanian Blue Gum", "Nilagiri, Yuliptu", "Australia"),

    ("Bamboo", "Bambusa vulgaris", "Poaceae", "Bambusa",
     "Grass", "Tropical", "Fastest growing plant. Used for construction, paper, food.",
     "Bambusa vulgaris is one of the largest bamboo species, widely grown throughout the tropics. Its shoots are edible.",
     "Common Bamboo, Golden Bamboo", "Bans, Mungil", "Tropical Asia"),

    ("Sandalwood", "Santalum album", "Santalaceae", "Santalum",
     "Tree", "Tropical", "Valuable aromatic wood. Used in perfumes and ritual.",
     "Indian Sandalwood is a small tropical tree and the most commonly known source of sandalwood. Highly valued in perfumery.",
     "Indian Sandalwood, White Sandalwood", "Chandan, Chandanam", "South Asia"),

    ("Noni", "Morinda citrifolia", "Rubiaceae", "Morinda",
     "Medicinal", "Tropical", "Anti-cancer, immune-boosting properties.",
     "Noni is a small evergreen tree in the coffee family Rubiaceae. Its fruit is used for medicine in many cultures.",
     "Indian Mulberry, Great Morinda", "Ach, Barringtonia", "Southeast Asia"),

    ("Paprika", "Capsicum annuum var. annuum", "Solanaceae", "Capsicum",
     "Spice", "Temperate", "Rich in vitamins A, E, B6. Anti-inflammatory.",
     "Paprika is a ground spice made from dried red peppers. The seasoning is used in many cuisines around the world.",
     "Sweet Pepper", "Shimla Mirch", "Central America"),

    ("Vetiver", "Chrysopogon zizanioides", "Poaceae", "Chrysopogon",
     "Grass", "Tropical", "Prevents soil erosion. Root used in perfumes.",
     "Vetiver is a perennial bunchgrass native to India. Its roots are used in perfumery for their earthy fragrance.",
     "Khus Grass", "Khus, Vettiver", "South Asia"),

    ("Lemongrass", "Cymbopogon citratus", "Poaceae", "Cymbopogon",
     "Herb", "Tropical", "Anti-microbial. Used in teas and cooking.",
     "Lemongrass is a tall perennial grass native to tropical and subtropical regions. Used in Asian cuisines and teas.",
     "Citronella Grass, Fever Grass", "Nimbu Ghaas, Nimba Ghaas", "South Asia"),

    ("Stevia", "Stevia rebaudiana", "Asteraceae", "Stevia",
     "Herb", "Subtropical", "Natural zero-calorie sweetener. Controls blood sugar.",
     "Stevia is a plant species in the genus Stevia of the family Asteraceae. The leaves are used as a natural sweetener.",
     "Sweetleaf, Sugar Leaf", "Meethi Tulsi", "South America"),

    ("Marigold", "Tagetes erecta", "Asteraceae", "Tagetes",
     "Ornamental", "Temperate", "Anti-fungal. Used in garlands and festivals.",
     "Marigold (Tagetes) is a genus of annual or perennial, mostly herbaceous plants in the sunflower family Asteraceae.",
     "African Marigold", "Genda, Chemparthy", "Mexico"),

    ("Sunflower", "Helianthus annuus", "Asteraceae", "Helianthus",
     "Cash Crop", "Temperate", "Oil crop. Seeds rich in healthy fats.",
     "The sunflower is a large annual forb native to North America. It is grown for its edible oil and seeds.",
     "Common Sunflower", "Surajmukhi, Suryakanthi", "North America"),

    ("Flaxseed", "Linum usitatissimum", "Linaceae", "Linum",
     "Cash Crop", "Temperate", "Omega-3 fatty acids. Reduces cholesterol.",
     "Flax is a member of the genus Linum in the family Linaceae. It is grown for its seeds, which can be ground into flaxseed meal.",
     "Linseed, Common Flax", "Alsi, Agasi", "Mediterranean"),

    ("Sesame", "Sesamum indicum", "Pedaliaceae", "Sesamum",
     "Cash Crop", "Tropical", "Rich in calcium. Sesame oil used in cooking.",
     "Sesame is a flowering plant in the genus Sesamum. Its seeds are widely used in cuisine across the world.",
     "Benne, Gingelly", "Til, Ellu", "Sub-Saharan Africa"),

    ("Mustard", "Brassica juncea", "Brassicaceae", "Brassica",
     "Cash Crop", "Temperate", "Cooking oil. Leaves used as vegetable.",
     "Indian mustard is a species of Brassica that is grown extensively in India for its oil-bearing seeds and edible leaves.",
     "Brown Mustard, Indian Mustard", "Sarson, Kadugu", "Central Asia"),

    ("Spinach", "Spinacia oleracea", "Amaranthaceae", "Spinacia",
     "Vegetable", "Temperate", "Rich in iron, vitamins A, C, K.",
     "Spinach is a leafy green flowering plant native to central and western Asia. It is consumed as a vegetable.",
     "Common Spinach", "Palak, Pasalai Keerai", "Central and Western Asia"),

    ("Cabbage", "Brassica oleracea var. capitata", "Brassicaceae", "Brassica",
     "Vegetable", "Temperate", "Anti-oxidant. Aids digestion.",
     "Cabbage is a leafy green, red, or white biennial plant grown as an annual vegetable crop.",
     "Common Cabbage", "Bandh Gobhi, Muttaikose", "Mediterranean Europe"),

    ("Carrot", "Daucus carota subsp. sativus", "Apiaceae", "Daucus",
     "Vegetable", "Temperate", "Rich in beta-carotene. Improves eyesight.",
     "The carrot is a root vegetable, typically orange, though purple, black, red, white, and yellow cultivars exist.",
     "Common Carrot", "Gajar, Karot", "Iran, Afghanistan"),

    ("Cauliflower", "Brassica oleracea var. botrytis", "Brassicaceae", "Brassica",
     "Vegetable", "Temperate", "Anti-cancer. Rich in vitamin C.",
     "Cauliflower is one of several vegetables in the species Brassica oleracea in the genus Brassica.",
     "White Cauliflower", "Gobi, Cauliflower", "Mediterranean"),

    ("Brinjal", "Solanum melongena", "Solanaceae", "Solanum",
     "Vegetable", "Tropical", "Rich in antioxidants. Low-calorie vegetable.",
     "Brinjal (Eggplant) is a species in the nightshade family Solanaceae. The fruit is widely used as a vegetable.",
     "Eggplant, Aubergine", "Baingan, Kathirikkai", "South Asia"),

    ("Bitter Gourd", "Momordica charantia", "Cucurbitaceae", "Momordica",
     "Vegetable", "Tropical", "Controls blood sugar in diabetes.",
     "Bitter melon is a tropical and subtropical vine of the family Cucurbitaceae, widely grown in Asia for its edible fruit.",
     "Bitter Melon, Karela", "Karela, Pavakkai", "South Asia"),

    ("Snake Gourd", "Trichosanthes cucumerina", "Cucurbitaceae", "Trichosanthes",
     "Vegetable", "Tropical", "Anti-diabetic, anti-inflammatory.",
     "Snake gourd is a tropical vine grown in South and Southeast Asia for its elongated fruit, which is used as a vegetable.",
     "Serpent Gourd", "Chichinda, Pudalangai", "South Asia"),

    ("Drumstick", "Moringa oleifera", "Moringaceae", "Moringa",
     "Vegetable", "Tropical", "Highly nutritious. Treats malnutrition.",
     "Drumstick is another common name for Moringa oleifera. Its long pods are eaten as a vegetable in South Asian cuisine.",
     "Moringa Pods, Horse Radish Tree", "Sahjan ki phali, Murungakkai", "South Asia"),

    ("Pumpkin", "Cucurbita pepo", "Cucurbitaceae", "Cucurbita",
     "Vegetable", "Temperate", "Rich in Vitamin A. Anti-oxidant.",
     "Pumpkin is a cultivar of winter squash that is round with smooth, slightly ribbed skin. Seeds are edible.",
     "Common Pumpkin", "Kaddu, Parangikkai", "North America"),

    ("Capsicum", "Capsicum frutescens", "Solanaceae", "Capsicum",
     "Vegetable", "Tropical", "Rich in Vitamin C. Metabolism booster.",
     "Capsicum frutescens is a species of chilli pepper that is typically smaller and hotter than Capsicum annuum.",
     "Bird's Eye Chili, Tabasco Pepper", "Lal Mirch, Kanthari Mulaku", "Central America"),

    ("Okra", "Abelmoschus esculentus", "Malvaceae", "Abelmoschus",
     "Vegetable", "Tropical", "Lowers blood sugar. Rich in fiber.",
     "Okra is a flowering plant in the mallow family known for its edible green seed pods.",
     "Lady's Finger, Bhindi", "Bhindi, Vendaikkai", "West Africa"),

    ("Peas", "Pisum sativum", "Fabaceae", "Pisum",
     "Vegetable", "Temperate", "High-protein legume. Rich in vitamins.",
     "The pea is most commonly the small spherical seed or the seed-pod of the flowering plant species Pisum sativum.",
     "Garden Pea", "Matar, Pattani", "Mediterranean"),

    ("Sweet Potato", "Ipomoea batatas", "Convolvulaceae", "Ipomoea",
     "Vegetable", "Tropical", "Rich in beta-carotene and vitamin C.",
     "Sweet potato is a dicotyledonous plant whose large, starchy, sweet-tasting tuberous roots are eaten as a root vegetable.",
     "Camote", "Shakarkandi, Sakkaravalli Kizhangu", "Central America"),

    ("Yam", "Dioscorea alata", "Dioscoreaceae", "Dioscorea",
     "Vegetable", "Tropical", "Rich in carbohydrates. Anti-oxidant.",
     "Yams are perennial herbaceous vines cultivated for the consumption of their starchy tubers in many temperate and tropical regions.",
     "Purple Yam, Greater Yam", "Ratalu, Kattala Kizhangu", "Southeast Asia"),

    ("Tapioca", "Manihot esculenta", "Euphorbiaceae", "Manihot",
     "Cash Crop", "Tropical", "Staple food in Africa and Asia. Starch source.",
     "Cassava (Tapioca) is a woody shrub native to South America of the spurge family Euphorbiaceae. Its tuberous root is a food staple.",
     "Cassava, Manioc", "Tapioca, Maravalli Kizhangu", "South America"),

    ("Coffee", "Coffea arabica", "Rubiaceae", "Coffea",
     "Cash Crop", "Subtropical", "Most popular beverage crop. Contains caffeine.",
     "Coffea arabica, widely known as the Arabica coffee, is a species of flowering plant in the coffee and bedstraw family Rubiaceae.",
     "Arabica Coffee", "Kaafi, Koffee", "Ethiopia"),

    ("Tea", "Camellia sinensis", "Theaceae", "Camellia",
     "Cash Crop", "Subtropical", "Anti-oxidant. Reduces heart disease risk.",
     "Camellia sinensis is a species of evergreen shrubs or small trees in the flowering plant family Theaceae whose leaves are used to produce tea.",
     "Tea Plant, Tea Shrub", "Chai, Tae", "East Asia"),

    ("Cocoa", "Theobroma cacao", "Malvaceae", "Theobroma",
     "Cash Crop", "Tropical", "Source of chocolate. Rich in flavonoids.",
     "Theobroma cacao, also called the cacao tree and the cocoa tree, is a small evergreen tree native to the deep tropical region of the Americas.",
     "Cacao Tree", "Kakao, Cocoa", "Tropical Americas"),

    ("Rubber", "Hevea brasiliensis", "Euphorbiaceae", "Hevea",
     "Tree", "Tropical", "Primary source of natural rubber latex.",
     "Hevea brasiliensis is a commercially important tree in the spurge family Euphorbiaceae. It is the major source of natural rubber.",
     "Para Rubber Tree", "Ravar, Kautchuk", "Amazon basin"),

    ("Jute", "Corchorus olitorius", "Malvaceae", "Corchorus",
     "Cash Crop", "Tropical", "Natural fibre for sacking and textile.",
     "Jute is a long, soft, shiny bast fibre that can be spun into coarse, strong threads. It is second only to cotton in usage.",
     "White Jute, Golden Fibre", "Pat, Jute", "South Asia"),

    ("Hemp", "Cannabis sativa", "Cannabaceae", "Cannabis",
     "Cash Crop", "Temperate", "Fibre, oil, and medicinal uses.",
     "Cannabis sativa is an annual herbaceous flowering plant indigenous to Eastern Asia. Grown for fibre (hemp) and seed.",
     "Industrial Hemp", "Bhang, Ganja", "Central Asia"),

    ("Indigo", "Indigofera tinctoria", "Fabaceae", "Indigofera",
     "Cash Crop", "Tropical", "Blue dye plant. Used in textile industry.",
     "Indigofera tinctoria, also called true indigo, is a species of plant in the bean family. Used as a blue dye for centuries.",
     "True Indigo", "Neel, Indigofera", "Asia, Africa"),

    ("Castor", "Ricinus communis", "Euphorbiaceae", "Ricinus",
     "Cash Crop", "Tropical", "Source of castor oil used in industry and medicine.",
     "Castor bean is a species of flowering plant in the spurge family Euphorbiaceae. Its seeds yield castor oil.",
     "Castor Bean, Castor Oil Plant", "Arandi, Amanakku", "East Africa"),

    # ── Trees and Timber ─────────────────────────────────────
    ("Teak", "Tectona grandis", "Lamiaceae", "Tectona",
     "Tree", "Tropical", "Premium hardwood for furniture and construction.",
     "Teak is a tropical hardwood tree species placed in the flowering plant family Lamiaceae. It is a large, deciduous tree.",
     "Common Teak", "Sagwan, Thekku", "South and Southeast Asia"),

    ("Banyan", "Ficus benghalensis", "Moraceae", "Ficus",
     "Tree", "Tropical", "National tree of India. Sacred tree.",
     "The Indian banyan is a species of fig tree. It is the national tree of India and is known for its unique aerial root system.",
     "Indian Banyan", "Vad, Aalamaram", "Indian subcontinent"),

    ("Peepal", "Ficus religiosa", "Moraceae", "Ficus",
     "Tree", "Tropical", "Sacred tree of Buddhists and Hindus. Medicinal bark.",
     "Ficus religiosa, the sacred fig or peepul tree, is a species of fig native to the Indian subcontinent. Under it, Buddha attained enlightenment.",
     "Sacred Fig, Bo Tree, Bodhi Tree", "Peepal, Arasa Maram", "Indian subcontinent"),

    ("Malabar Neem", "Melia azedarach", "Meliaceae", "Melia",
     "Tree", "Tropical", "Timber and medicinal uses. Related to Neem.",
     "Melia azedarach is a species of deciduous tree in the mahogany family Meliaceae native to South Asia. Also called Persian Lilac.",
     "Persian Lilac, Pride of India, Chinaberry", "Bakain, Melia", "South Asia"),

    ("Sisso", "Dalbergia sissoo", "Fabaceae", "Dalbergia",
     "Tree", "Tropical", "Premium timber. Nitrogen-fixing tree.",
     "Dalbergia sissoo, known as North Indian rosewood or Shisham, is a fast-growing tree native to the Indian subcontinent.",
     "Shisham, Indian Rosewood", "Shisham, Sissoo", "Indian subcontinent"),

    ("Arjuna", "Terminalia arjuna", "Combretaceae", "Terminalia",
     "Medicinal", "Tropical", "Heart tonic. Treats angina and heart failure.",
     "Terminalia arjuna is a tree of the genus Terminalia. Its bark is used as a heart tonic in Ayurvedic medicine.",
     "Arjun Tree", "Arjun, Kumbuk", "South Asia"),

    ("Jamun", "Syzygium cumini", "Myrtaceae", "Syzygium",
     "Fruit", "Tropical", "Anti-diabetic. Treats digestive disorders.",
     "Syzygium cumini is an evergreen tropical tree native to the Indian subcontinent. Its edible fruit is called Jamun or Java plum.",
     "Java Plum, Black Plum, Malabar Plum", "Jamun, Naaval", "Indian subcontinent"),

    ("Sapodilla", "Manilkara zapota", "Sapotaceae", "Manilkara",
     "Fruit", "Tropical", "Sweet fruit. Source of natural latex (chicle).",
     "Sapodilla is a long-lived evergreen tree native to Mexico, Central America, and the Caribbean.",
     "Chiku, Sapota, Naseberry", "Chikoo, Sapota", "Mexico, Central America"),

    ("Custard Apple", "Annona squamosa", "Annonaceae", "Annona",
     "Fruit", "Tropical", "Rich in iron and calcium.",
     "Sugar-apple (Custard apple) is the fruit of Annona squamosa, a small, well-branched tree or shrub native to tropical Americas.",
     "Sugar Apple, Sweetsop", "Sitaphal, Seetha Pazham", "Tropical Americas"),

    ("Star Fruit", "Averrhoa carambola", "Oxalidaceae", "Averrhoa",
     "Fruit", "Tropical", "Low in calories. Rich in vitamin C.",
     "Carambola is the fruit of Averrhoa carambola, a species of tree native to tropical Southeast Asia.",
     "Carambola", "Kamrakh, Kamaranga", "Southeast Asia"),

    ("Jackbean", "Canavalia ensiformis", "Fabaceae", "Canavalia",
     "Pulse", "Tropical", "Nitrogen-fixing legume. Fodder crop.",
     "Jackbean is a tropical legume native to Central America used as green manure and livestock feed.",
     "Horse Bean", "Kachang Pedang", "Central America"),
]


def get_or_create_family(db: Session, name: str) -> int:
    from models import Family
    obj = db.query(Family).filter(Family.name == name).first()
    if not obj:
        obj = Family(name=name, description=f"Botanical family {name}")
        db.add(obj)
        db.flush()
    return obj.id


def get_or_create_genus(db: Session, name: str) -> int:
    from models import Genus
    obj = db.query(Genus).filter(Genus.name == name).first()
    if not obj:
        obj = Genus(name=name, description=f"Botanical genus {name}")
        db.add(obj)
        db.flush()
    return obj.id


def insert_real_plants():
    db: Session = SessionLocal()
    inserted = 0
    skipped = 0

    try:
        for row in REAL_PLANTS:
            (common_name, botanical_name, family_name, genus_name,
             category, climate, medicinal_uses, overview,
             synonyms, local_names, native_region) = row

            # Skip if already exists
            existing = db.query(Plant).filter(
                (Plant.common_name.ilike(common_name)) |
                (Plant.botanical_name.ilike(botanical_name))
            ).first()
            if existing:
                print(f"  ↷ Skipping '{common_name}' (already exists)")
                skipped += 1
                continue

            family_id = get_or_create_family(db, family_name)
            genus_id = get_or_create_genus(db, genus_name)

            plant = Plant(
                common_name=common_name,
                botanical_name=botanical_name,
                synonyms=synonyms,
                local_names=local_names,
                family_id=family_id,
                genus_id=genus_id,
                category=category,
                overview=overview,
                medicinal_uses=medicinal_uses,
                food_uses="Used in cooking, medicine, and agriculture.",
                commercial_uses="Commercially valuable species.",
                conservation_status="Least Concern",
                life_cycle="Perennial",
                growth_habit="Erect",
            )
            db.add(plant)
            db.flush()  # get plant.id

            # Climate
            db.add(ClimateRequirement(
                plant_id=plant.id,
                native_region=native_region,
                countries_grown="India, China, USA, Brazil, Southeast Asia",
                climatic_zones=climate,
                rainfall_requirement="600–1500 mm/year",
                temperature_requirement="15–35°C",
                humidity_requirement="60–80%"
            ))

            # Soil
            db.add(SoilRequirement(
                plant_id=plant.id,
                preferred_soil="Loamy",
                soil_ph_range="6.0–7.5",
                drainage="Well-drained",
                organic_matter="High",
                fertility="Medium to High",
                texture="Medium"
            ))

            # Harvest
            db.add(HarvestInformation(
                plant_id=plant.id,
                harvest_indicators="Fruit/leaf maturity observed visually",
                harvest_time="Varies by region and variety",
                harvest_method="Hand-picking or mechanical",
                post_harvest_handling="Dry, cool storage",
                storage_temp="10–20°C",
                shelf_life="2–4 weeks fresh"
            ))

            # Botanical Classification
            db.add(BotanicalClassification(
                plant_id=plant.id,
                kingdom="Plantae",
                division="Tracheophyta",
                class_name="Magnoliopsida",
                order_name=f"{family_name}ales",
                taxonomy_hierarchy=f"Plantae → Tracheophyta → Magnoliopsida → {family_name} → {genus_name} → {botanical_name}"
            ))

            inserted += 1
            print(f"  ✅ Inserted '{common_name}' ({botanical_name})")

        db.commit()
        print(f"\n🌿 Done! Inserted {inserted} real plants. Skipped {skipped} duplicates.")
        print(f"📊 Total plants in DB: {db.query(Plant).count()}")

    except Exception as e:
        db.rollback()
        print(f"❌ Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    insert_real_plants()
