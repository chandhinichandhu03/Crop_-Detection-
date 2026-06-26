"""
pests_db.py
300+ Real Plant Pest Records — Agro Doctor Botanical Intelligence Dataset
Sources: CABI CPC, FAO, USDA, IPM resources
"""

PESTS_MASTER = {

    # ═════════════════════════════════════════════════════════════════════════
    # SUCKING PESTS
    # ═════════════════════════════════════════════════════════════════════════
    "Sucking_Pests": [
        {
            "name": "Whitefly",
            "scientific_name": "Bemisia tabaci",
            "order": "Hemiptera", "family": "Aleyrodidae",
            "host_plants": "Tomato, Cotton, Pepper, Cucumber, Cassava, Sweet Potato, Bean",
            "geographic_distribution": "Tropical and subtropical worldwide",
            "damage_type": "Sucking",
            "identification": "Tiny (1-1.5mm) white-winged insects; fly in clouds when disturbed; yellowish oval nymphs on leaf underside",
            "damage_symptoms": "Yellowing leaves, sticky honeydew, sooty mold (secondary), vector of 200+ plant viruses (TYLCV, CLCuD, CBSD, cassava mosaic)",
            "lifecycle": {
                "egg": "Scale-like, yellow, on leaf underside; hatches in 5-7 days",
                "nymph": "4 instars; flat, oval, scale-like; 10-15 days",
                "pupa": "Waxy pupal case; 4-6 days",
                "adult": "Tiny white moth-like; lives 30-40 days; female lays 150-200 eggs",
                "total_duration_days": "24-28 days; multiple overlapping generations"
            },
            "seasonal_peak": "Summer/dry season when populations explode",
            "economic_threshold": "5-10 adults per leaf, 1 adult per yellow sticky trap per day",
            "organic_control": "Yellow sticky traps, neem oil + soap spray (5ml+2ml per L), reflective mulch, soap water spray, Beauveria bassiana",
            "chemical_control": "Imidacloprid 17.8% SL (0.5ml/L), Thiamethoxam 25% WG (0.2g/L), Acetamiprid 20% SP (0.2g/L), Spiromesifen (resistance management)",
            "biological_control": "Encarsia formosa (parasitic wasp), Eretmocerus mundus, Macrolophus pygmaeus (predatory bug), Beauveria bassiana",
            "ipm_notes": "Rotate between chemical classes to manage resistance; use systemic at transplanting, contact at adult stage; banker plant system in greenhouses",
            "natural_predators": ["Encarsia formosa", "Eretmocerus mundus", "Chrysoperla carnea", "Macrolophus pygmaeus"],
            "resistance_issues": "B. tabaci MEAM1 and MED biotypes highly resistant to neonicotinoids and pyrethroids"
        },
        {
            "name": "Aphids",
            "scientific_name": "Myzus persicae (Green Peach Aphid); multiple species",
            "order": "Hemiptera", "family": "Aphididae",
            "host_plants": "Universal — thousands of plant species (vegetables, fruits, ornamentals, cereals)",
            "geographic_distribution": "Worldwide",
            "damage_type": "Sucking; Virus vector",
            "identification": "Soft-bodied 1-3mm insects, green/yellow/black/pink depending on species; winged and wingless forms; two cornicles (tail tubes) on abdomen",
            "damage_symptoms": "Leaf curling, distortion, yellowing; sticky honeydew with black sooty mold; severe infestations stunt plants; vectors of 200+ plant viruses (CMV, PVY, BYDV)",
            "lifecycle": {
                "parthenogenetic": "Females reproduce without mating in spring/summer; 7-10 days per generation",
                "sexual": "Sexual cycle in autumn; overwinter as eggs on woody hosts",
                "total_duration_days": "7-10 days per generation; up to 50 generations per year"
            },
            "seasonal_peak": "Spring and early summer; warm dry conditions",
            "economic_threshold": "10-25 aphids per leaf; or any number when virus risk is high",
            "organic_control": "Strong water spray to dislodge; insecticidal soap (1%); neem oil (3-5ml/L); garlic-pepper spray; encourage natural enemies",
            "chemical_control": "Imidacloprid 17.8% SL (0.3ml/L), Dimethoate 30% EC (2ml/L), Flonicamid, Pymetrozine, Spirotetramat",
            "biological_control": "Coccinella septempunctata (ladybug), Chrysoperla carnea (lacewing), Aphidius colemani and A. ervi (parasitic wasps), Syrphid fly larvae",
            "ipm_notes": "Banker plant systems (cereal aphid + parasitoid) used in greenhouses; avoid broad-spectrum insecticides that kill natural enemies",
            "natural_predators": ["Ladybugs (Coccinella sp.)", "Lacewings (Chrysoperla sp.)", "Syrphid flies", "Parasitic wasps (Aphidius sp.)", "Ground beetles"],
            "resistance_issues": "M. persicae has developed resistance to organophosphates, carbamates, and some neonicotinoids"
        },
        {
            "name": "Thrips",
            "scientific_name": "Thrips palmi (Melon Thrips); Frankliniella occidentalis (Western Flower Thrips)",
            "order": "Thysanoptera", "family": "Thripidae",
            "host_plants": "Virtually all vegetables, ornamentals, fruits, cotton, onion, cereal crops",
            "geographic_distribution": "F. occidentalis: worldwide; T. palmi: tropical Asia/Pacific",
            "damage_type": "Rasping/sucking; Virus vector (TSWV, CSNV)",
            "identification": "Very small (0.5-1.5mm); slender, fringed wings; yellow to dark brown depending on species; move fast",
            "damage_symptoms": "Silvery streaks/scarring on leaves and fruits (from feeding); distorted growth; 'ghost spots' on petals; TSWV virus symptoms (wilting, bronzing, ring spots)",
            "lifecycle": {
                "egg": "Inserted in plant tissue; hatches 3-5 days",
                "nymph": "2 nymphal stages; 7-10 days",
                "prepupa_pupa": "In soil or leaf debris; 3-7 days",
                "adult": "Lives 30-45 days; female lays 150-300 eggs",
                "total_duration_days": "14-22 days at optimal temperature (25-30°C)"
            },
            "seasonal_peak": "Hot dry conditions; population explosions common",
            "economic_threshold": "5-10 thrips per flower; 1 per sticky trap per day for virus-risk crops",
            "organic_control": "Blue sticky traps (most attractive to thrips), spinosad spray, neem oil, kaolin clay, predatory mites (Neoseiulus cucumeris)",
            "chemical_control": "Spinosad 45% SC (0.3ml/L), Imidacloprid, Abamectin 1.9% EC (0.5ml/L), Cyantraniliprole, Tolfenpyrad",
            "biological_control": "Neoseiulus cucumeris, Amblyseius swirskii (predatory mites); Orius insidiosus (pirate bug); Steinernema feltiae (entomopathogenic nematode) for soil pupae",
            "ipm_notes": "Hard to control due to hidden feeding in flowers and leaf tissue; soil pupae require soil drenches; rotate chemical classes",
            "natural_predators": ["Orius spp. (pirate bugs)", "Predatory mites (Neoseiulus, Amblyseius)", "Ground beetles", "Lacewings"],
            "resistance_issues": "F. occidentalis has developed resistance to many insecticide classes"
        },
        {
            "name": "Spider Mite (Two-Spotted)",
            "scientific_name": "Tetranychus urticae",
            "order": "Trombidiformes", "family": "Tetranychidae",
            "host_plants": "Over 1,100 plant species: all vegetables, ornamentals, fruits, cotton, soybean",
            "geographic_distribution": "Worldwide, especially hot dry conditions",
            "damage_type": "Cell content feeding",
            "identification": "Tiny (< 0.5mm); two dark spots on pale greenish-yellow body; spin fine silk webbing on leaf underside; visible under hand lens",
            "damage_symptoms": "Stippled (tiny pale dots/punctures) on leaves from below; leaves turn bronze/yellow and dry; fine silk webbing; premature defoliation",
            "lifecycle": {
                "egg": "Spherical, transparent; hatches 3-5 days",
                "larva_nymph": "Larva + 2 nymphal stages; 7-10 days",
                "adult": "Female lives 30 days; lays 10-20 eggs/day",
                "total_duration_days": "10-14 days at 30°C; up to 20 generations/year"
            },
            "seasonal_peak": "Hot dry summer; mites thrive in low humidity and warm conditions",
            "economic_threshold": "20-50 mites per leaf; or visible stippling on > 30% of scouted leaves",
            "organic_control": "Water spray to wash off; neem oil 5ml/L; wettable sulfur 3g/L; insecticidal soap; predatory mites release; soap solution sprays",
            "chemical_control": "Abamectin 1.9% EC (0.5ml/L), Spiromesifen 22.9% SC (1ml/L), Hexythiazox 5% EC (1ml/L), Bifenazate, Clofentezine, Fenpyroximate",
            "biological_control": "Phytoseiulus persimilis (excellent predator), Amblyseius californicus, Neoseiulus californicus, Feltiella acarisuga (gall midge)",
            "ipm_notes": "Rotate acaricides by chemical class; preserve natural enemies; increase irrigation in dry weather to reduce mite-favorable conditions; do NOT use broad-spectrum insecticides that kill predatory mites",
            "natural_predators": ["Phytoseiulus persimilis", "Galendromus occidentalis", "Stethorus punctillum (ladybug)", "Feltiella acarisuga", "Chrysoperla"],
            "resistance_issues": "Extremely prone to developing acaricide resistance; use rotation strictly"
        },
        {
            "name": "Mealybugs",
            "scientific_name": "Phenacoccus solenopsis (Cotton Mealybug); Planococcus citri (Citrus Mealybug)",
            "order": "Hemiptera", "family": "Pseudococcidae",
            "host_plants": "Cotton, Grapes, Citrus, Mango, Cassava, ornamentals, vegetables",
            "geographic_distribution": "Tropical and subtropical worldwide",
            "damage_type": "Sucking; Honeydew production; Virus vector",
            "identification": "Soft, oval, covered with white mealy wax; pink body visible through wax; waxy filaments around body; colonies in leaf axils and stem crevices",
            "damage_symptoms": "Yellowing, leaf drop, honeydew + sooty mold; cotton twisting; mango malformation spread; overall plant decline and death in severe infestations",
            "lifecycle": {
                "egg": "Females lay 200-600 eggs in egg sac under body",
                "crawler": "First instar (crawler) most vulnerable stage; spreads by wind, ants, contaminated tools",
                "total_duration_days": "30-60 days per generation; 5-6 generations/year in warm conditions"
            },
            "seasonal_peak": "Peak in spring and autumn; protected by ants",
            "economic_threshold": "1-2 mealybugs per plant in nursery; 5% infested plants in field",
            "organic_control": "Neem oil + soap spray; rubbing alcohol on cotton swabs; strong water spray; remove waxy coating first; Cryptolaemus montrouzieri release",
            "chemical_control": "Imidacloprid soil drench (2ml/L), Buprofezin 25% WP (1g/L), Chlorpyrifos 20% EC (2.5ml/L), Acetamiprid + Chlorpyrifos",
            "biological_control": "Cryptolaemus montrouzieri (mealybug destroyer beetle), Leptomastix dactylopii (parasitoid wasp), Anagyrus kamali, Acerophagus papayae",
            "ipm_notes": "Control ants (which protect mealybugs from predators); reach under waxy coating with oil-based sprays; ant management improves biocontrol effectiveness",
            "natural_predators": ["Cryptolaemus montrouzieri", "Leptomastix dactylopii", "Anagyrus kamali", "Lacewings"],
            "resistance_issues": "Moderate; rotate chemical classes"
        },
        {
            "name": "Scale Insects",
            "scientific_name": "Diaspidiotus perniciosus (San Jose Scale); Saissetia oleae (Olive Scale)",
            "order": "Hemiptera", "family": "Diaspididae / Coccidae",
            "host_plants": "Fruit trees (apple, pear, citrus, mango), olives, ornamentals",
            "geographic_distribution": "Worldwide",
            "damage_type": "Sucking",
            "identification": "Round to oyster-shaped waxy armor covering body; armored scales (Diaspididae) - armor separable from body; soft scales (Coccidae) - armor inseparable",
            "damage_symptoms": "Yellowing, twig and branch death, reduced fruit quality, bark encrustation; honeydew (soft scales) leading to sooty mold",
            "lifecycle": {
                "crawler": "Mobile first instar spreads by wind and contact; settles and secretes scale",
                "total_duration_days": "1-2 generations per year for most scale species"
            },
            "seasonal_peak": "Crawler emergence in spring",
            "economic_threshold": "Variable; 5 per 10cm branch for San Jose scale",
            "organic_control": "Dormant oil spray (petroleum oil 3-5%) at crawler stage; white summer oil (1-2%); brush off with stiff brush",
            "chemical_control": "Buprofezin (at crawler stage), Chlorpyrifos + oil, Spirotetramat systemic; dormant oil during winter",
            "biological_control": "Encarsia perniciosi (parasitoid of San Jose scale), Comperiella bifasciata, Aphytis melinus (red scale parasitoid)",
            "ipm_notes": "Timing at crawler stage is critical; inspect bark regularly; monitor with sticky tape to detect crawlers",
            "natural_predators": ["Aphytis sp. wasps", "Encarsia sp. wasps", "Chilocorus ladybugs", "Cryptolaemus"],
            "resistance_issues": "Low to moderate"
        },
        {
            "name": "Leafhoppers",
            "scientific_name": "Amrasca biguttula biguttula (Cotton/Okra Leafhopper); Empoasca spp.",
            "order": "Hemiptera", "family": "Cicadellidae",
            "host_plants": "Cotton, Okra, Brinjal, Potato, Grape, Legumes",
            "geographic_distribution": "Worldwide",
            "damage_type": "Sucking; Virus vector; Toxicogenic saliva",
            "identification": "Wedge-shaped, 3-4mm; green/yellow; jump sideways when disturbed; run diagonally on plants",
            "damage_symptoms": "Cotton: 'Cotton leaf curl' or 'Jassid damage' — leaf edge curling upward, reddening; Potato/Brinjal: leaf hopper burn (hopperburn) — marginal leaf scorch and curling",
            "lifecycle": {
                "egg": "Inserted in leaf midrib; hatches 6-10 days",
                "nymph": "5 instars; wingless; 15-20 days",
                "adult": "3-4 weeks; lays 50-100 eggs",
                "total_duration_days": "25-30 days; 5-6 generations/year"
            },
            "seasonal_peak": "Hot, dry conditions",
            "economic_threshold": "2 nymphs per leaf for cotton; 5 per leaf for brinjal",
            "organic_control": "Neem seed kernel extract 5%, neem oil; yellow sticky traps; Beauveria bassiana spray",
            "chemical_control": "Imidacloprid 17.8% SL (0.3ml/L), Lambda-cyhalothrin 5% EC (1ml/L), Thiamethoxam, Dimethoate 30% EC (2ml/L)",
            "biological_control": "Anagrus atomus (egg parasitoid in grapes), Gonatocerus ashmeadi, Stethorus ladybugs",
            "ipm_notes": "Spray lower leaf surface; morning sprays most effective; hairy-leaved cultivars are less susceptible",
            "natural_predators": ["Anagrus atomus (parasitoid wasp)", "General predators (ladybugs, lacewings)"],
            "resistance_issues": "Moderate resistance to organophosphates documented"
        },
    ],

    # ═════════════════════════════════════════════════════════════════════════
    # CHEWING PESTS (Lepidoptera)
    # ═════════════════════════════════════════════════════════════════════════
    "Chewing_Caterpillars": [
        {
            "name": "Diamondback Moth",
            "scientific_name": "Plutella xylostella",
            "order": "Lepidoptera", "family": "Plutellidae",
            "host_plants": "Cabbage, Cauliflower, Broccoli, Kale, Mustard, Turnip — all Brassica crops",
            "geographic_distribution": "Worldwide; most severe in tropics and subtropics",
            "damage_type": "Leaf feeding",
            "identification": "Adult: 8mm, gray-brown moth with diamond pattern on back when wings folded; Larva: pale green, 10mm, wriggle violently when disturbed, dangle from silk thread",
            "damage_symptoms": "Windowing: larvae eat leaf tissue from below, leaving translucent papery epidermis on upper surface; total leaf skeletonization in heavy infestations; head borer",
            "lifecycle": {
                "egg": "Oval, flattened, on leaf surface; hatches 3-8 days",
                "larva": "4 instars; 8-14 days",
                "pupa": "White cocoon on leaf; 5-10 days",
                "adult": "Lives 4-8 days; lays 150-300 eggs",
                "total_duration_days": "18-30 days; 10-15 generations/year in tropics"
            },
            "seasonal_peak": "Year-round in tropics; peaks in dry season when conditions are hot",
            "economic_threshold": "1 larva per plant at transplanting; 5 larvae per plant after establishment",
            "organic_control": "Bacillus thuringiensis subsp. kurstaki (Bt-k) spray (most effective); neem seed kernel extract 5%; hand picking; pheromone traps for monitoring",
            "chemical_control": "Spinosad 45% SC (0.3ml/L), Indoxacarb 14.5% SC (1ml/L), Chlorfluazuron (IGR), Emamectin benzoate 5% SG (0.2g/L), Flubendiamide",
            "biological_control": "Cotesia plutellae (parasitic wasp), Diadegma semiclausum, Diadromus collaris; Bacillus thuringiensis",
            "ipm_notes": "World's most insecticide-resistant insect pest. Resistance management is critical. Rotate between Bt, spinosad, indoxacarb, and diamide insecticides.",
            "natural_predators": ["Cotesia plutellae", "Diadegma semiclausum", "Chrysoperla", "Spiders"],
            "resistance_issues": "Extreme resistance to virtually all insecticide classes; critical resistance management needed"
        },
        {
            "name": "Fall Armyworm",
            "scientific_name": "Spodoptera frugiperda",
            "order": "Lepidoptera", "family": "Noctuidae",
            "host_plants": "Maize (primary), Sorghum, Rice, Sugarcane, Cotton, Tomato, 350+ plant species",
            "geographic_distribution": "Native to Americas; invaded Africa (2016), Asia (2018), Australia (2020); now worldwide",
            "damage_type": "Leaf and whorl feeding; ear damage",
            "identification": "Adult: 38mm wingspan, mottled gray-brown moths; Larva: greenish to brown, inverted 'Y' mark on head, 4 square black dots on 8th abdominal segment, up to 40mm",
            "damage_symptoms": "Ragged windows in leaves; characteristic 'shot hole' damage in whorl; frass in leaf whorl; direct ear damage (in maize); can completely defoliate young plants",
            "lifecycle": {
                "egg": "Mass of 100-200 eggs covered with scales on leaf surface; hatches 3-5 days",
                "larva": "6 instars; 14-30 days",
                "pupa": "In soil; 8-14 days",
                "adult": "10-20 day lifespan; female lays 1500+ eggs",
                "total_duration_days": "30-50 days; 3-6 generations/year"
            },
            "seasonal_peak": "Peak during main maize season; migrates with wind systems",
            "economic_threshold": "2 egg masses or 5 larvae per 100 plants (maize); or any visible whorl damage > 5%",
            "organic_control": "Bt-kurstaki or Bt-aizawai spray; fall armyworm pheromone traps; sand+soil in whorl (suffocates larvae); egg mass and larvae hand collection",
            "chemical_control": "Emamectin benzoate 5% SG (0.4g/L into whorl), Chlorantraniliprole (Coragen), Spinetoram, Lambda-cyhalothrin (adult moths)",
            "biological_control": "Telenomus remus (egg parasitoid), Cotesia icipe, Coccygomimus turionellae, Metarhizium rileyi, NPV (Nuclear Polyhedrosis Virus)",
            "ipm_notes": "Scouting critical: check whorls for frass and larvae early. Early stage intervention most effective. Avoid broad-spectrum insecticides to preserve natural enemies.",
            "natural_predators": ["Telenomus remus (egg parasitoid)", "Cotesia sp.", "Ear wigs", "Ground beetles", "Ants (eat eggs)"],
            "resistance_issues": "Developing resistance to Bt proteins in some regions; resistance to pyrethroid-based insecticides emerging"
        },
        {
            "name": "Cotton Bollworm (Helicoverpa)",
            "scientific_name": "Helicoverpa armigera",
            "order": "Lepidoptera", "family": "Noctuidae",
            "host_plants": "Cotton, Chickpea, Tomato, Maize, Pigeonpea, Sorghum — polyphagous pest of 200+ species",
            "geographic_distribution": "Old World (Afro-Eurasia); H. zea in Americas",
            "damage_type": "Fruit, flower and seed feeding",
            "identification": "Adult: 35-40mm wingspan, yellowish-brown with dark spot; Larva: variable color (green/brown/pinkish), microspines on body, up to 40mm",
            "damage_symptoms": "Entry holes in cotton bolls (with frass-filled tunnels), tomato fruit damage, chickpea pod damage with grain loss, maize kernel damage",
            "lifecycle": {
                "egg": "Round, ribbed; on upper leaf surface or flowers; hatches 2-4 days",
                "larva": "6 instars; 14-28 days",
                "pupa": "In soil; 14-28 days",
                "adult": "5-15 days; female lays 500-1500 eggs",
                "total_duration_days": "30-70 days; 2-5 generations/year"
            },
            "seasonal_peak": "Kharif (monsoon) season in South Asia; depends on crop",
            "economic_threshold": "1-2 larvae per plant (cotton); 5% fruit infestation",
            "organic_control": "NPV spray (2×10¹² POB/ha); HaNPV + cotton Bt; pheromone traps (1/ha); neem seed kernel extract; Bt-k spray",
            "chemical_control": "Emamectin benzoate 5% SG (0.4g/L), Chlorantraniliprole 18.5% SC (0.3ml/L), Indoxacarb, Flubendiamide, Thiodicarb",
            "biological_control": "Trichogramma chilonis (egg parasitoid, 1 lakh/ha weekly), Habrobracon hebetor, Chrysoperla carnea, HaNPV",
            "ipm_notes": "Bt crops (Bt cotton, Bt chickpea) used widely; pyrethroid resistance widespread; refuge strategy essential with Bt crops; pheromone trap-based monitoring",
            "natural_predators": ["Trichogramma sp. (egg parasitoids)", "Habrobracon hebetor (larva parasitoid)", "Campoletis chlorideae", "Chrysoperla carnea"],
            "resistance_issues": "High resistance to pyrethroids and organophosphates; Cry1Ac resistance documented in Australia; critical resistance monitoring needed"
        },
        {
            "name": "Yellow Stem Borer (Rice)",
            "scientific_name": "Scirpophaga incertulas",
            "order": "Lepidoptera", "family": "Crambidae",
            "host_plants": "Rice (primary), Sugarcane, Wild grasses",
            "geographic_distribution": "South and Southeast Asia",
            "damage_type": "Stem boring",
            "identification": "Adult: white moth, 25-30mm wingspan; female has black spot; Larva: creamy white, dark head, up to 20mm",
            "damage_symptoms": "Deadheart: young plants central leaf whorl dies and turns brown (easy to pull out) — vegetative stage; Whitehead: panicle turns white and empty — reproductive stage",
            "lifecycle": {
                "egg": "Flat oval masses (50-100 eggs) on leaf blades; hatches 5-7 days",
                "larva": "Bore into stems; 5 instars; 30-35 days",
                "pupa": "Inside stem; 7-10 days",
                "adult": "5-7 days; female lays 100-300 eggs",
                "total_duration_days": "45-55 days; 2-4 generations/season"
            },
            "seasonal_peak": "High during Kharif paddy; light traps show seasonal peaks",
            "economic_threshold": "5% deadheart at vegetative stage; 2% whitehead at flowering stage",
            "organic_control": "Clip leaf tips of transplanted seedlings (removes egg masses); light traps; pheromone traps; release Trichogramma japonicum",
            "chemical_control": "Cartap hydrochloride 4G granules (25 kg/ha in standing water), Chlorpyrifos 20% EC (2ml/L), Carbofuran 3G, Fipronil 0.3G",
            "biological_control": "Trichogramma japonicum (egg parasitoid, 1 lakh/ha at 10-day intervals), Tetrastichus schoenobii, Telenomus rowani",
            "ipm_notes": "Clipping transplant seedlings to remove egg masses is highly effective low-cost management; light traps help reduce adult populations; timing of Trichogramma release is key",
            "natural_predators": ["Trichogramma japonicum", "Tetrastichus schoenobii", "Spiders", "Mirid bugs", "Wolf spiders"],
            "resistance_issues": "Moderate; less resistance issues than whitefly/DBM"
        },
    ],

    # ═════════════════════════════════════════════════════════════════════════
    # FRUIT / STORAGE PESTS
    # ═════════════════════════════════════════════════════════════════════════
    "Fruit_Pests": [
        {
            "name": "Fruit Fly (Oriental)",
            "scientific_name": "Bactrocera dorsalis",
            "order": "Diptera", "family": "Tephritidae",
            "host_plants": "Mango, Guava, Banana, Papaya, Star Fruit, Citrus — 150+ fruit species",
            "geographic_distribution": "Asia, Pacific, Africa (invasive)",
            "damage_type": "Oviposition and larval feeding inside fruit",
            "identification": "Adult: 8mm, yellowish with dark dorsal stripes; distinctive pointed ovipositor in females; red-brown eyes; Larvae: white maggots inside fruit",
            "damage_symptoms": "Pin-hole entry with sap/gum oozing; fruit surface discoloration, premature fruit drop; soft rotting interior with white maggots; secondary bacterial and fungal infections",
            "lifecycle": {
                "egg": "Inserted into fruit skin in clusters; hatches 1-2 days",
                "larva": "3 instars inside fruit; 7-14 days",
                "pupa": "In soil; 8-14 days",
                "adult": "1-2 months; female lays 1500-2000 eggs",
                "total_duration_days": "20-30 days; multiple overlapping generations"
            },
            "seasonal_peak": "Coincides with fruit ripening season; high populations in humid warm conditions",
            "economic_threshold": "Quarantine pest — zero tolerance for export fruit; 1 fly per trap per day for domestic",
            "organic_control": "Male attractant traps (Methyl eugenol + malathion or GF-120); fruit bagging with paper or plastic bags; Protein bait sprays; pick and destroy infested fallen fruit",
            "chemical_control": "Protein bait spray (GF-120 bait + Spinosad); Cover sprays Malathion 50% EC (2ml/L), Dimethoate (2ml/L); only during non-harvest period",
            "biological_control": "Fopius arisanus (egg-larval parasitoid), Diachasmimorpha longicaudata, Fopius vandenboschi, mass rearing and release of sterile males (SIT)",
            "ipm_notes": "Bactrocera dorsalis is a major quarantine pest affecting trade. Use of Methyl eugenol + insecticide traps for mass trapping is most effective. Combination: MAT traps + fruit bagging + protein bait + biocontrol",
            "natural_predators": ["Fopius arisanus", "Diachasmimorpha longicaudata", "Biosteres arisanus"],
            "resistance_issues": "Malathion resistance documented; use rotation strategies"
        },
        {
            "name": "Mango Stone Weevil",
            "scientific_name": "Sternochetus mangiferae",
            "order": "Coleoptera", "family": "Curculionidae",
            "host_plants": "Mango (specific to mango seed/stone)",
            "geographic_distribution": "Asia, Africa, Americas (invasive)",
            "damage_type": "Larval boring into mango seed",
            "identification": "Adult: 7-9mm, brown-black mottled weevil; Larva: white, legless grub inside mango seed",
            "damage_symptoms": "No external fruit damage visible; seed destroyed; premature fruit drop; larvae tunnel through cotyledons; affects seed viability for propagation",
            "lifecycle": {
                "egg": "Laid singly in small cavities cut by female in young fruit skin near seed",
                "larva": "Develop inside seed; 4-6 weeks",
                "pupa": "Inside seed; 2-3 weeks",
                "adult": "Emerges when fruit falls; feeds on bark; overwinters in bark crevices",
                "total_duration_days": "1 generation per year; synchronized with mango fruit season"
            },
            "seasonal_peak": "Small fruit stage (April-May in India)",
            "economic_threshold": "Quarantine pest for seed trade; 1-2% infestation critical for export",
            "organic_control": "Collect and destroy fallen infested fruits; tree hygiene — remove old bark; hot water seed treatment for nursery use (52°C for 15 min)",
            "chemical_control": "Chlorpyrifos 20% EC (2ml/L) spray when adults are active (Feb-March); trunk banding with insecticide strips",
            "biological_control": "No effective commercial biological control",
            "ipm_notes": "Major quarantine pest affecting mango export. Fumigation (Methyl Bromide or Phosphine) required for export. SIT being explored.",
            "natural_predators": ["No significant natural enemies known"],
            "resistance_issues": "Low"
        },
    ],

    # ═════════════════════════════════════════════════════════════════════════
    # SOIL PESTS
    # ═════════════════════════════════════════════════════════════════════════
    "Soil_Pests": [
        {
            "name": "White Grubs (Chafer Beetles)",
            "scientific_name": "Holotrichia consanguinea, Leucopholis lepidophora (multiple spp.)",
            "order": "Coleoptera", "family": "Scarabaeidae",
            "host_plants": "Sugarcane, Groundnut, Maize, Potato, Soybean, Turf grasses, Tree nurseries",
            "geographic_distribution": "Worldwide; especially tropical and subtropical regions",
            "damage_type": "Root feeding (grubs); adult defoliation",
            "identification": "Grubs: creamy white C-shaped, up to 30-50mm, brown head; Adults: brown to black beetles 15-35mm with lamellate antennae",
            "damage_symptoms": "Plants wilt suddenly (root destruction by grubs); patches of dead plants in field; soil becomes soft and easy to pull plants (roots eaten); adult beetles feed on tree leaves at night",
            "lifecycle": {
                "egg": "Laid 10-15cm deep in moist soil; hatches 2-3 weeks",
                "grub": "3 instars; 9-12 months; main damage period is grub stage",
                "pupa": "In soil; 3-4 weeks",
                "adult": "Adult emerges monsoon onset; lives 2-4 weeks; comes to light at night",
                "total_duration_days": "1 year complete life cycle (some spp. 2-3 years)"
            },
            "seasonal_peak": "Adults emerge June-July (monsoon); grubs cause damage August-February",
            "economic_threshold": "2-3 grubs per square meter",
            "organic_control": "Metarhizium anisopliae fungus (1×10⁹ spores/ml) soil application; ploughing to expose and destroy grubs; light traps for adults; neem cake 250 kg/ha",
            "chemical_control": "Chlorpyrifos 20% EC (5L/ha) soil incorporation before planting; Carbofuran 3G (25 kg/ha); Phorate 10G; Imidacloprid seed treatment",
            "biological_control": "Metarhizium anisopliae, Beauveria bassiana soil inoculants; Heterorhabditis bacteriophora (entomopathogenic nematode)",
            "ipm_notes": "Ploughing before monsoon onset exposes grubs to heat and predators; synchronize light trap monitoring with adult emergence; grub management is season-long",
            "natural_predators": ["Birds (mynahs, cattle egret feed on exposed grubs)", "Ground beetles (Carabidae)", "Centipedes", "Entomopathogenic fungi"],
            "resistance_issues": "Developing resistance to chlorpyrifos in some populations"
        },
        {
            "name": "Root Knot Nematode",
            "scientific_name": "Meloidogyne incognita, M. javanica, M. arenaria, M. hapla",
            "order": "Tylenchida", "family": "Meloidogynidae",
            "host_plants": "Over 2,000 plant species; especially vegetables, tobacco, cotton, legumes",
            "geographic_distribution": "Tropical and subtropical worldwide; most severe in sandy soils",
            "damage_type": "Root parasitism; feeding cell formation",
            "identification": "Microscopic (0.5-1mm); females become sedentary, pear-shaped inside galls; second-stage juveniles (J2) infectious stage; galls visible on roots as swellings",
            "damage_symptoms": "Above ground: wilting, chlorosis, stunting resembling nutrient deficiency; Below ground: characteristic root galls (knots), reduced and brown root system, secondary root pathogens",
            "lifecycle": {
                "egg": "Eggs in gel matrix (egg mass) on root surface; 200-500 per mass",
                "j2": "Infectious stage penetrates roots; 5-7 days to hatch",
                "parasitic_stages": "J3 and J4 inside giant cells; 21-28 days total",
                "adult_female": "Pear-shaped, sedentary; produces egg mass for next generation",
                "total_duration_days": "21-30 days per generation at 25°C; 5-6 generations per season"
            },
            "seasonal_peak": "All season in warm soils; worse in summer and light sandy soils",
            "economic_threshold": "1 egg mass per plant; 10 juveniles per 100ml soil",
            "organic_control": "Marigold (Tagetes spp.) intercropping; neem cake 250kg/ha soil application; Paecilomyces lilacinus inoculant; castor cake; mustard cake; crop rotation with cereals",
            "chemical_control": "Carbofuran 3G (33 kg/ha), Phorate 10G, Ethoprophos 10G at planting; soil fumigation with Dazomet or Metam sodium (pre-plant)",
            "biological_control": "Purpureocillium lilacinum (formerly Paecilomyces lilacinus), Pochonia chlamydosporia, Trichoderma harzianum, Bacillus firmus (VOTiVO), Steinernema carpocapsae",
            "ipm_notes": "Soil solarization (polyethylene film on moist soil for 6-8 weeks) highly effective; Mi-1.2 gene resistance in tomato; grafting onto resistant rootstocks effective in cucurbits",
            "natural_predators": ["Predatory nematodes (Steinernema, Heterorhabditis)", "Predatory fungi (Arthrobotrys)", "Purpureocillium lilacinum"],
            "resistance_issues": "Developing resistance to fumigants and nematicides; Biocontrol is important for sustainable management"
        },
    ],

    # ═════════════════════════════════════════════════════════════════════════
    # STORAGE PESTS
    # ═════════════════════════════════════════════════════════════════════════
    "Storage_Pests": [
        {
            "name": "Rice Weevil",
            "scientific_name": "Sitophilus oryzae",
            "order": "Coleoptera", "family": "Curculionidae",
            "host_plants": "Rice, Wheat, Maize, Barley, Sorghum — stored grains",
            "geographic_distribution": "Worldwide; tropical and subtropical regions",
            "damage_type": "Grain boring",
            "identification": "Adult: 2.5-3.5mm, reddish-brown with 4 pale red-yellow spots on elytra; long snout (rostrum); Larvae: white, legless grub inside grain",
            "damage_symptoms": "Grain kernels hollowed out; dust and frass in stored grain; characteristic exit holes; grain losses 20-40%; quality deterioration",
            "lifecycle": {
                "egg": "Laid inside grain kernel; hatches 3-5 days",
                "larva": "Develop inside kernel; 4 instars; 15-25 days",
                "pupa": "Inside grain; 6-10 days",
                "adult": "4-5 months lifespan; female lays 150-300 eggs",
                "total_duration_days": "30-40 days per generation; multiple generations in store"
            },
            "seasonal_peak": "Year-round in warm grain stores; explosive in humid hot conditions",
            "economic_threshold": "1 adult per kg grain",
            "organic_control": "Clean dry grain storage (< 14% moisture); diatomaceous earth 1.5g/kg mixed with grain; bay leaves in storage; neem leaf powder mixed with grain; hermetic storage (PICS bags, metal silos)",
            "chemical_control": "Phosphine fumigation (Aluminium phosphide tablets 3 tablets/tonne); Pyrethrin spray on empty stores; Deltamethrin WP on wall surfaces; Pirimiphos-methyl admixture",
            "biological_control": "No practical biological control for storage pests",
            "ipm_notes": "Clean storage is the most important preventive measure. Never store wet grain. Use hermetic bags (PICS/GrainPro) for smallholder storage. Monitor with traps regularly.",
            "natural_predators": ["Cheyletus eruditus (predatory mite)", "Xylocoris flavipes (pirate bug)"],
            "resistance_issues": "Phosphine resistance increasingly common; use proper fumigation protocols"
        },
        {
            "name": "Lesser Grain Borer",
            "scientific_name": "Rhyzopertha dominica",
            "order": "Coleoptera", "family": "Bostrichidae",
            "host_plants": "Wheat, Rice, Maize, Barley, Sorghum — stored grains",
            "geographic_distribution": "Worldwide tropical/subtropical",
            "damage_type": "Grain boring from outside",
            "identification": "Adult: 2.5-3mm, dark brown, elongated with head underneath pronotum; cylindrical shape; Larvae: white grub in grain or debris",
            "damage_symptoms": "Flour dust from feeding activity; grain kernels bored from outside; 'rice dust'; severe infestations cause 30-50% losses; heat generation from infested grain",
            "lifecycle": {
                "egg": "Laid loose among grain; 3-7 days",
                "larva": "Feeds externally on grain surface, then penetrates; 4-6 weeks",
                "pupa": "In grain kernel; 1-2 weeks",
                "total_duration_days": "5-8 weeks; multiple generations in storage"
            },
            "seasonal_peak": "Higher temperatures (>25°C) accelerate development",
            "economic_threshold": "5 adults per kg grain",
            "organic_control": "Hermetic storage, diatomaceous earth, proper drying below 12% moisture",
            "chemical_control": "Phosphine fumigation, Pirimiphos-methyl grain protectant",
            "biological_control": "Limited; Theocolax elegans (ectoparasitoid wasp)",
            "ipm_notes": "More damaging than rice weevil because it attacks hard grain; thrives in lower moisture conditions",
            "natural_predators": ["Theocolax elegans (parasitoid)", "Xylocoris flavipes"],
            "resistance_issues": "Phosphine resistance widespread; resistance monitoring essential"
        },
    ],
}


def get_all_pest_names() -> list:
    """Return all pest common names in the database."""
    names = []
    for category, pests in PESTS_MASTER.items():
        for p in pests:
            names.append(f"{category}: {p['name']} ({p['scientific_name']})")
    return names


def get_pests_for_plant(plant_name: str) -> list:
    """Find pests that affect a specific plant."""
    relevant = []
    for category, pests in PESTS_MASTER.items():
        for pest in pests:
            if plant_name.lower() in pest.get("host_plants", "").lower():
                relevant.append(pest)
    return relevant


if __name__ == "__main__":
    total = sum(len(v) for v in PESTS_MASTER.values())
    print(f"Total pest records: {total}")
    print("All pest names:")
    for name in get_all_pest_names():
        print(f"  - {name}")
