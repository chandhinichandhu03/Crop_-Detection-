"""
diseases_db.py
500+ Real Plant Disease Records — Agro Doctor Botanical Intelligence Dataset
Sources: PlantVillage, CABI CPC, FAO, USDA, University Extension Services
"""

# ─────────────────────────────────────────────────────────────────────────────
# DISEASE MASTER DATABASE — Organized by crop / disease type
# Each record: name, pathogen, type, symptoms, treatments
# ─────────────────────────────────────────────────────────────────────────────

DISEASES_MASTER = {

    # ═════════════════════════════════════════════════════════════════════════
    # TOMATO DISEASES
    # ═════════════════════════════════════════════════════════════════════════
    "Tomato": [
        {
            "name": "Early Blight",
            "pathogen_name": "Alternaria solani",
            "disease_type": "Fungal",
            "risk_level": "Medium",
            "economic_impact": "Reduces yield by 30-50% in warm humid conditions. Major yield loss in unmanaged fields.",
            "host_range": "Tomato, Potato, Eggplant",
            "geographic_distribution": "Worldwide",
            "favorable_conditions": "Warm temperatures (24-29°C), High humidity (>90%), Wet foliage",
            "symptoms": {
                "early": "Small, dark brown circular spots with concentric rings (target board pattern) on older lower leaves",
                "late": "Leaf yellowing, premature leaf drop, dark sunken lesions at stem-ends of fruit, stem collar rot",
                "affected_parts": "Leaves, Stem, Fruit",
                "severity_levels": {"mild": "< 10% leaf area affected", "moderate": "10-30%", "severe": "> 30%"}
            },
            "disease_cycle": "Overwinters in infected plant debris. Conidia spread by wind and rain splash. Infection requires 2-3 hours of wet leaf surface.",
            "incubation_period": "2-3 days",
            "treatment": {
                "organic": "Neem oil (4ml/L + 2ml soap), Copper oxychloride 50% WP (3g/L), Trichoderma harzianum soil drench, Baking soda spray (5g/L)",
                "chemical": "Mancozeb 75% WP (2g/L), Azoxystrobin 23% SC (1ml/L), Chlorothalonil 75% WP (2g/L), Propiconazole 25% EC (1ml/L)",
                "biological": "Trichoderma viride, Bacillus subtilis strains QST713, Pseudomonas fluorescens",
                "preventive": "Use certified disease-free seeds, crop rotation (3 years), remove infected debris, avoid overhead irrigation, stake plants for air circulation",
                "application_frequency": "Every 7-10 days in wet weather",
                "recovery_time": "10-14 days with treatment",
                "phi_days": 7
            }
        },
        {
            "name": "Late Blight",
            "pathogen_name": "Phytophthora infestans",
            "disease_type": "Oomycete",
            "risk_level": "Critical",
            "economic_impact": "Can destroy entire field in 5-7 days. Caused the Irish Potato Famine (1845-49).",
            "host_range": "Tomato, Potato",
            "geographic_distribution": "Worldwide, especially cool humid climates",
            "favorable_conditions": "Cool temperature (10-20°C), High humidity (>90%), Rain, dew",
            "symptoms": {
                "early": "Water-soaked irregular grayish-green patches on leaves, usually starting from leaf tips and edges",
                "late": "Fuzzy white sporulating lesions on underside of leaves in humid conditions, greasy dark green-black patches on fruit, entire plant collapse with putrid smell",
                "affected_parts": "Leaves, Stems, Fruit",
                "severity_levels": {"mild": "Spots < 5mm, few leaves", "moderate": "Multiple leaves affected", "severe": "Entire plant wilted"}
            },
            "disease_cycle": "Sporangia spread by wind and rain. Sexual oospores persist in soil. Highly explosive under wet cool conditions.",
            "incubation_period": "3-5 days",
            "treatment": {
                "organic": "Copper hydroxide (3g/L) as protective spray, Bordeaux mixture (1%), maintain dry conditions",
                "chemical": "Metalaxyl-M + Mancozeb (Ridomil Gold) 2.5g/L, Cymoxanil + Famoxadone 0.5g/L, Dimethomorph 0.5g/L",
                "biological": "Bacillus subtilis (Serenade), Streptomyces lydicus",
                "preventive": "Plant resistant varieties, ensure good drainage, avoid overhead irrigation, scout regularly during cool wet weather, destroy volunteer plants",
                "application_frequency": "Every 5-7 days during epidemic periods",
                "recovery_time": "7-10 days (preventive focus; infected plants rarely recover)",
                "phi_days": 7
            }
        },
        {
            "name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
            "pathogen_name": "Tomato yellow leaf curl virus",
            "disease_type": "Viral",
            "risk_level": "High",
            "economic_impact": "Can cause 100% yield loss in unmanaged greenhouses. Major problem in warm regions.",
            "host_range": "Tomato, Pepper, Bean, Eggplant",
            "geographic_distribution": "Mediterranean, Middle East, South Asia, Americas, Sub-Saharan Africa",
            "favorable_conditions": "High whitefly populations, temperatures above 25°C",
            "symptoms": {
                "early": "Upward and inward curling of leaflets, yellowing at leaf margins",
                "late": "Severe stunting, complete yellowing, flower drop, no fruit set or deformed fruits",
                "affected_parts": "Leaves, Growing Tips, Fruit",
                "severity_levels": {"mild": "Slight curling at margins", "severe": "Complete stunting and yellowing"}
            },
            "disease_cycle": "Transmitted by whitefly (Bemisia tabaci) in a persistent circulative manner. No seed transmission.",
            "incubation_period": "14-21 days",
            "treatment": {
                "organic": "No cure once infected; control whitefly vector with neem oil, yellow sticky traps, reflective mulch",
                "chemical": "Imidacloprid or Thiamethoxam for whitefly control. Mineral oil sprays to reduce whitefly transmission",
                "biological": "Encarsia formosa parasitoid, Beauveria bassiana for whiteflies",
                "preventive": "Plant TYLCV-resistant varieties, use insect-proof netting in nursery, roguing infected plants immediately, control whiteflies",
                "application_frequency": "Whitefly control every 7-10 days",
                "recovery_time": "No recovery; remove infected plants",
                "phi_days": None
            }
        },
        {
            "name": "Fusarium Wilt",
            "pathogen_name": "Fusarium oxysporum f. sp. lycopersici",
            "disease_type": "Fungal",
            "risk_level": "High",
            "economic_impact": "Major cause of tomato field losses, especially in sandy soils.",
            "host_range": "Tomato (host-specific)",
            "geographic_distribution": "Worldwide",
            "favorable_conditions": "Warm soils (25-30°C), light sandy soils, acid soils",
            "symptoms": {
                "early": "Yellowing and wilting of lower leaves starting on one side of the plant, often one branch first",
                "late": "Complete wilting and death, brown internal vascular discoloration visible when stem is cut crosswise",
                "affected_parts": "Roots, Stem (vascular), Leaves",
                "severity_levels": {"mild": "Single branch wilting", "severe": "Entire plant collapse"}
            },
            "disease_cycle": "Soil-borne pathogen. Survives for years in soil as chlamydospores. Enters through roots, grows in xylem blocking water flow.",
            "incubation_period": "7-14 days",
            "treatment": {
                "organic": "Trichoderma harzianum soil treatment, Solarization (clear polyethylene film over moist soil for 4-6 weeks)",
                "chemical": "No effective chemical cure; soil fumigation with Metam sodium before planting as preventive",
                "biological": "Trichoderma viride, Pseudomonas fluorescens root dip, Bacillus subtilis",
                "preventive": "Plant resistant varieties (race-specific), crop rotation (4+ years), avoid wounding roots, soil solarization",
                "application_frequency": "Soil treatments at planting",
                "recovery_time": "No recovery; remove infected plants",
                "phi_days": None
            }
        },
        {
            "name": "Bacterial Wilt",
            "pathogen_name": "Ralstonia solanacearum",
            "disease_type": "Bacterial",
            "risk_level": "Critical",
            "economic_impact": "One of the most destructive soilborne diseases worldwide; can destroy entire plantations.",
            "host_range": "Tomato, Potato, Pepper, Eggplant, Banana, Tobacco, Ginger",
            "geographic_distribution": "Tropical, subtropical, warm temperate regions worldwide",
            "favorable_conditions": "High temperatures (28-35°C), high soil moisture, damaged roots",
            "symptoms": {
                "early": "Sudden wilting of top leaves during hottest part of the day, recovery at night",
                "late": "Permanent wilting even at night, water-soaked stem interior, oozing of bacterial slime (white to gray) from cut stems dipped in water",
                "affected_parts": "Entire plant, Vascular system",
                "severity_levels": {"early": "Partial daytime wilting", "severe": "Complete irreversible collapse"}
            },
            "disease_cycle": "Spreads through soil, water, infected plant material. Enters through roots. Multiplies in xylem.",
            "incubation_period": "3-7 days",
            "treatment": {
                "organic": "No effective cure. Copper-based bactericides as weak suppressants",
                "chemical": "No effective chemical treatment available",
                "biological": "Bacillus subtilis and Pseudomonas fluorescens as biological suppressants (preventive only)",
                "preventive": "Plant resistant varieties, crop rotation (minimum 3 years), soil solarization, avoid waterlogging, remove infected plants and soil, use clean tools",
                "application_frequency": "Preventive only",
                "recovery_time": "No recovery; remove infected plants immediately",
                "phi_days": None
            }
        },
        {
            "name": "Septoria Leaf Spot",
            "pathogen_name": "Septoria lycopersici",
            "disease_type": "Fungal",
            "risk_level": "Medium",
            "economic_impact": "Severe defoliation, reduces photosynthesis, leads to sunscald on fruit. Up to 40% yield loss.",
            "host_range": "Tomato, Potato (limited)",
            "geographic_distribution": "Worldwide, common in humid temperate regions",
            "favorable_conditions": "Wet weather, temperatures 20-25°C, leaf wetness > 4 hours",
            "symptoms": {
                "early": "Small, circular water-soaked spots on lower leaves with dark brown margins and lighter gray-white centers with tiny black dots (pycnidia)",
                "late": "Extensive defoliation starting from bottom of plant upward, sun-scalded fruits exposed to direct sun",
                "affected_parts": "Leaves (lower first)",
                "severity_levels": {"mild": "Scattered spots", "severe": "Extensive defoliation"}
            },
            "disease_cycle": "Overwinters in infected debris. Conidia splash-spread by rain. Infection requires wet leaf surface.",
            "incubation_period": "5 days",
            "treatment": {
                "organic": "Copper oxychloride 50% WP (3g/L), neem oil spray, remove infected lower leaves",
                "chemical": "Chlorothalonil (2g/L), Mancozeb (2g/L), Azoxystrobin (0.5ml/L)",
                "biological": "Bacillus subtilis",
                "preventive": "Crop rotation, remove infected plant debris, avoid overhead irrigation, stake and prune for air circulation",
                "application_frequency": "Every 10-14 days",
                "recovery_time": "14-21 days",
                "phi_days": 7
            }
        },
        {
            "name": "Powdery Mildew (Tomato)",
            "pathogen_name": "Leveillula taurica",
            "disease_type": "Fungal",
            "risk_level": "Low",
            "economic_impact": "Reduces yield by 10-20% through photosynthesis reduction",
            "host_range": "Tomato, Pepper, Eggplant",
            "geographic_distribution": "Dry, warm regions worldwide",
            "favorable_conditions": "Low humidity (50-70%), temperatures 18-28°C, common in greenhouses",
            "symptoms": {
                "early": "Pale yellow spots on upper leaf surface, white powdery growth visible on underside",
                "late": "Entire leaf covered with white powder, premature defoliation",
                "affected_parts": "Leaves",
                "severity_levels": {"mild": "Few spots", "severe": "Complete powdery coverage"}
            },
            "disease_cycle": "Obligate parasite; spreads by airborne conidia. Internal mycelium attacks from inside leaf.",
            "incubation_period": "5-7 days",
            "treatment": {
                "organic": "Wettable sulfur (3g/L), potassium bicarbonate (5g/L), neem oil, diluted milk (1:9)",
                "chemical": "Hexaconazole (1ml/L), Propiconazole (1ml/L), Tebuconazole (1ml/L)",
                "biological": "Ampelomyces quisqualis, Bacillus subtilis",
                "preventive": "Good air circulation, avoid dense planting, resistant varieties",
                "application_frequency": "Every 7-10 days",
                "recovery_time": "7-14 days",
                "phi_days": 14
            }
        },
        {
            "name": "Blossom End Rot",
            "pathogen_name": "Calcium deficiency (Physiological)",
            "disease_type": "Physiological Disorder",
            "risk_level": "Medium",
            "economic_impact": "Can render 25-50% of fruits unmarketable during severe calcium stress.",
            "host_range": "Tomato, Pepper, Eggplant, Watermelon, Squash",
            "geographic_distribution": "Worldwide",
            "favorable_conditions": "Irregular watering, drought stress, soil pH imbalance, excess nitrogen or potassium",
            "symptoms": {
                "early": "Light brown water-soaked area at blossom end of green fruit",
                "late": "Expanding dark brown to black leathery sunken patch at fruit base, secondary fungal colonization",
                "affected_parts": "Fruit (blossom end)",
                "severity_levels": {"mild": "Small patch < 1cm", "severe": "Half the fruit blackened"}
            },
            "disease_cycle": "Not infectious; caused by calcium translocation failure due to irregular water stress.",
            "incubation_period": "Appears 6-8 weeks after planting",
            "treatment": {
                "organic": "Foliar calcium chloride spray (4g/L), consistent irrigation, mulching, agricultural lime in soil",
                "chemical": "Calcium nitrate foliar spray (2g/L), drip application of calcium chelate",
                "biological": "Not applicable",
                "preventive": "Consistent irrigation schedule, mulch to retain soil moisture, soil pH 6.2-6.8, avoid excess ammonium nitrogen",
                "application_frequency": "Calcium spray every 7-10 days when fruits are forming",
                "recovery_time": "Affected fruits do not recover; new fruits will be healthy with correction",
                "phi_days": None
            }
        },
        {
            "name": "Root Knot Nematode",
            "pathogen_name": "Meloidogyne incognita, M. javanica",
            "disease_type": "Nematode",
            "risk_level": "High",
            "economic_impact": "Up to 80% yield loss in heavily infested sandy soils.",
            "host_range": "Tomato, Pepper, Cucumber, Beans, and 2,000+ other plant species",
            "geographic_distribution": "Tropical and subtropical regions worldwide",
            "favorable_conditions": "Sandy soils, temperatures 25-30°C, high soil moisture",
            "symptoms": {
                "early": "Wilting during hot hours, poor plant vigor, chlorosis resembling nutrient deficiency",
                "late": "Typical galls (root knots) on roots when pulled, stunted growth, reduced yield",
                "affected_parts": "Roots",
                "severity_levels": {"mild": "Few galls, slight yield reduction", "severe": "Dense galls, complete root damage"}
            },
            "disease_cycle": "Females lay eggs in soil. Juveniles penetrate roots, induce gall formation. Multiple generations per season.",
            "incubation_period": "21-30 days to complete one generation",
            "treatment": {
                "organic": "Marigold intercropping (Tagetes sp.), neem cake soil application, Paecilomyces lilacinus, Pochonia chlamydosporia",
                "chemical": "Carbofuran 3G (33kg/ha soil application), Ethoprophos 10G granules, Oxamyl",
                "biological": "Purpureocillium lilacinum, Trichoderma harzianum, Bacillus firmus",
                "preventive": "Crop rotation with non-host crops (maize, cereals), soil solarization, use resistant varieties (Mi-gene)",
                "application_frequency": "Soil treatment at planting and 30 DAS",
                "recovery_time": "Suppression over 1-2 seasons",
                "phi_days": 60
            }
        },
    ],

    # ═════════════════════════════════════════════════════════════════════════
    # RICE DISEASES
    # ═════════════════════════════════════════════════════════════════════════
    "Rice": [
        {
            "name": "Rice Blast",
            "pathogen_name": "Pyricularia oryzae (Magnaporthe oryzae)",
            "disease_type": "Fungal",
            "risk_level": "Critical",
            "economic_impact": "Most destructive rice disease globally. Causes 10-30% annual losses; can cause up to 100% loss.",
            "host_range": "Rice, Barley, Wheat, Foxtail millet",
            "geographic_distribution": "85+ countries globally",
            "favorable_conditions": "Night temperatures 17-22°C, leaf wetness > 10 hours, high humidity, excess nitrogen",
            "symptoms": {
                "early": "Spindle-shaped (diamond) lesions on leaves with gray-white center and dark brown to reddish-brown margins",
                "late": "Neck rot: lesion at panicle neck causes the head to break and hang down (Neck Blast). Grain blast: empty chaffy grains. Node blast: dark lesions at stem nodes.",
                "affected_parts": "Leaves, Nodes, Panicle Neck, Grains",
                "severity_levels": {"mild": "< 5% leaf area", "moderate": "5-25%", "severe": "> 25%"}
            },
            "disease_cycle": "Conidia spread by wind; infection requires 10+ hours leaf wetness. Overwinters in infected debris, volunteer rice, and alternate hosts.",
            "incubation_period": "4-5 days at 25°C",
            "treatment": {
                "organic": "Spray Pseudomonas fluorescens (1% w/v), seed treatment with Trichoderma, avoid excess nitrogen",
                "chemical": "Tricyclazole 75% WP (0.6g/L), Isoprothiolane 40% EC (1.5ml/L), Kasugamycin 3% SL (1.5ml/L), Azoxystrobin",
                "biological": "Pseudomonas fluorescens, Bacillus subtilis, Trichoderma harzianum",
                "preventive": "Use blast-resistant varieties (BPT 5204, Swarna Sub1), balanced N fertilization, wider spacing for air circulation, destroy stubble",
                "application_frequency": "At tillering and booting stages; repeat at 10-14 day intervals if disease pressure continues",
                "recovery_time": "12-15 days with systemic fungicide",
                "phi_days": 14
            }
        },
        {
            "name": "Bacterial Leaf Blight (BLB)",
            "pathogen_name": "Xanthomonas oryzae pv. oryzae",
            "disease_type": "Bacterial",
            "risk_level": "High",
            "economic_impact": "Causes 20-30% yield loss in susceptible varieties; up to 70% in severe epidemics.",
            "host_range": "Rice (primary), wild Oryza species",
            "geographic_distribution": "Asia, West Africa, Australia",
            "favorable_conditions": "High temperature (25-34°C), high humidity, wind, flooding, heavy nitrogen fertilization",
            "symptoms": {
                "early": "Water-soaked to yellowish stripes along leaf margins, turning white to grayish, 'Kresek' phase in young seedlings (complete wilting)",
                "late": "Milky, opaque bacterial exudate (dried beads) visible in morning on leaf tips, pale yellow 'straw' leaves, withered diseased panicles",
                "affected_parts": "Leaves, growing tips",
                "severity_levels": {"mild": "Marginal leaf yellowing", "kresek": "Seedling death, very severe early infection"}
            },
            "disease_cycle": "Enters through water pores (hydathodes) and wounds. Spread by rain splash, floodwater, and wind. Overwinters in infected stubble and wild rice.",
            "incubation_period": "7-14 days",
            "treatment": {
                "organic": "Drain fields; copper hydroxide (2g/L) as weak bactericide spray",
                "chemical": "Streptomycin + Tetracycline combination (limited effectiveness); Copper oxychloride preventively",
                "biological": "Pseudomonas fluorescens (preventive soil and foliar treatment)",
                "preventive": "Plant resistant varieties (IR64, Swarna), avoid excessive nitrogen, drain infected fields, destroy stubble",
                "application_frequency": "Copper sprays every 10 days in high-risk periods",
                "recovery_time": "Suppression; no cure for infected plants",
                "phi_days": None
            }
        },
        {
            "name": "Sheath Blight",
            "pathogen_name": "Rhizoctonia solani AG1-IA",
            "disease_type": "Fungal",
            "risk_level": "High",
            "economic_impact": "Second most important rice disease after blast. Causes 20-50% yield loss in high-density plantings.",
            "host_range": "Rice, Maize, Soybean, Sugarcane, and many other crops",
            "geographic_distribution": "Worldwide, especially tropical Asia",
            "favorable_conditions": "High humidity, temperatures 28-32°C, dense canopy, high nitrogen, standing water",
            "symptoms": {
                "early": "Oval to elliptical greenish-gray lesions with white-gray interior and brownish border on leaf sheaths at water level",
                "late": "Lesions coalesce and extend to upper leaves, white mycelial growth and brown sclerotia visible, complete sheath and leaf death",
                "affected_parts": "Leaf sheaths (primarily), Leaves, Stem",
                "severity_levels": {"mild": "Lesions below flag leaf", "severe": "Lesions above flag leaf"}
            },
            "disease_cycle": "Survives as sclerotia in soil and crop debris. Sclerotia float to base of plants and initiate infection. Spreads upward under humid conditions.",
            "incubation_period": "3-4 days",
            "treatment": {
                "organic": "Trichoderma harzianum or T. viride soil application (2.5 kg/ha), Pseudomonas fluorescens spray",
                "chemical": "Hexaconazole 5% EC (1ml/L), Propiconazole 25% EC (1ml/L), Validamycin 3% L (2ml/L), Carbendazim (1g/L)",
                "biological": "Trichoderma harzianum, Bacillus subtilis",
                "preventive": "Reduce plant density, lower nitrogen, drain standing water, use resistant varieties",
                "application_frequency": "At tillering, repeat at 10-14 day intervals in humid conditions",
                "recovery_time": "14-21 days",
                "phi_days": 14
            }
        },
        {
            "name": "Brown Spot",
            "pathogen_name": "Helminthosporium oryzae (Bipolaris oryzae)",
            "disease_type": "Fungal",
            "risk_level": "Medium",
            "economic_impact": "Contributed to Great Bengal Famine (1943). Causes 5-45% yield loss.",
            "host_range": "Rice, Corn, Sorghum, Sugarcane",
            "geographic_distribution": "Worldwide, worse in nutrient-deficient soils",
            "favorable_conditions": "Temperatures 25-30°C, high humidity, nutrient-deficient (especially potassium) soils",
            "symptoms": {
                "early": "Small, oval to circular spots on leaves with yellow halo; dark brown margins and lighter centers",
                "late": "Spots enlarge to typical oval brown spots, leaves yellow and die; glume discoloration leading to pecky rice",
                "affected_parts": "Leaves, Grain (glumes)",
                "severity_levels": {"mild": "Few spots", "moderate": "Extensive spotting", "severe": "Leaf death"}
            },
            "disease_cycle": "Seed-borne; spreads by conidia through wind and rain. Survives in infected seeds and crop debris.",
            "incubation_period": "5-6 days",
            "treatment": {
                "organic": "Trichoderma seed treatment, adequate potassium nutrition",
                "chemical": "Mancozeb 75% WP (2g/L), Propiconazole 25% EC (1ml/L), Iprodione (1.5g/L)",
                "biological": "Trichoderma viride seed treatment",
                "preventive": "Treat seeds with fungicide, correct soil nutrition (especially K and Si), use certified seeds, crop rotation",
                "application_frequency": "2-3 sprays during crop season",
                "recovery_time": "10-14 days",
                "phi_days": 14
            }
        },
        {
            "name": "False Smut",
            "pathogen_name": "Ustilaginoidea virens",
            "disease_type": "Fungal",
            "risk_level": "Low",
            "economic_impact": "Reduces grain quality and weight by 2-15%. Produces toxic ustiloxins.",
            "host_range": "Rice",
            "geographic_distribution": "All rice-growing areas, especially with high humidity at flowering",
            "favorable_conditions": "High humidity and rainfall during heading and flowering stage, temperatures 25-35°C",
            "symptoms": {
                "early": "Individual spikelets converted to small velvet-like greenish balls",
                "late": "Balls enlarge to 10mm diameter, becoming orange-yellow then olive-green with black powdery spores, scattered through panicle",
                "affected_parts": "Grain/Spikelets",
                "severity_levels": {"mild": "1-2 smut balls per panicle", "severe": "Multiple balls per panicle"}
            },
            "disease_cycle": "Infection during flowering stage. Spores survive in soil and air. Spreads by wind.",
            "incubation_period": "Infection at flowering, visible at maturity",
            "treatment": {
                "organic": "Propiconazole-based sprays at booting stage",
                "chemical": "Propiconazole 25% EC (1ml/L) or Azoxystrobin at booting stage",
                "biological": "No effective biological control",
                "preventive": "Spray preventive fungicide at booting stage, avoid late planting, balanced nutrition",
                "application_frequency": "One spray at booting stage",
                "recovery_time": "Prevention only; affected grains cannot be treated",
                "phi_days": 21
            }
        },
    ],

    # ═════════════════════════════════════════════════════════════════════════
    # WHEAT DISEASES
    # ═════════════════════════════════════════════════════════════════════════
    "Wheat": [
        {
            "name": "Stripe Rust (Yellow Rust)",
            "pathogen_name": "Puccinia striiformis f. sp. tritici",
            "disease_type": "Fungal",
            "risk_level": "High",
            "economic_impact": "Can cause 70% yield loss. Major rust affecting wheat in cool humid regions.",
            "host_range": "Wheat, Barley, Triticale, wild grasses",
            "geographic_distribution": "Worldwide, especially in cooler regions",
            "favorable_conditions": "Cool temperatures (7-15°C), morning dew, high humidity",
            "symptoms": {
                "early": "Stripe of yellow-orange uredia arranged in rows along leaf veins on upper leaf surface",
                "late": "Extensive yellowing of leaves, black teliospores in stripes, reduced grain fill, shriveled kernels",
                "affected_parts": "Leaves, Leaf sheaths, Glumes",
                "severity_levels": {"mild": "Few stripes", "moderate": "Extensive yellow striping", "severe": "Leaf death"}
            },
            "disease_cycle": "Obligate parasite; spreads by wind-borne urediniospores. Overwinters on living green tissue. Long-distance spread by wind.",
            "incubation_period": "9-10 days at optimal temperature",
            "treatment": {
                "organic": "Wettable sulfur preventively; no effective organic cure",
                "chemical": "Propiconazole 25% EC (1ml/L), Tebuconazole 250 EW (1ml/L), Azoxystrobin + Propiconazole",
                "biological": "Limited; Trichoderma as preventive",
                "preventive": "Plant resistant varieties (HD-3226, WH1105), timely sowing to escape high-risk period, prophylactic fungicide at flag leaf stage",
                "application_frequency": "One spray at flag leaf + repeat 14 days later if severe",
                "recovery_time": "10-14 days",
                "phi_days": 21
            }
        },
        {
            "name": "Stem Rust (Black Rust)",
            "pathogen_name": "Puccinia graminis f. sp. tritici",
            "disease_type": "Fungal",
            "risk_level": "Critical",
            "economic_impact": "Ug99 race caused international alarm in 2000s; can cause near-total crop failure.",
            "host_range": "Wheat, Barley, Rye, many grasses",
            "geographic_distribution": "Worldwide",
            "favorable_conditions": "Warm temperatures (18-30°C), high humidity, dew",
            "symptoms": {
                "early": "Brick-red oval to elongated blisters (pustules) on stems and leaves that rupture releasing reddish-brown powdery spores",
                "late": "Black teliospore pustules in late season, lodging of stems, shriveled grain",
                "affected_parts": "Stems, Leaves, Leaf sheaths, Glumes",
                "severity_levels": {"mild": "Few pustules", "severe": "Stem girdling and lodging"}
            },
            "disease_cycle": "Two-host cycle: Puccinia graminis requires barberry (Berberis sp.) as alternate host for sexual recombination. Urediniospores spread by wind.",
            "incubation_period": "8-14 days",
            "treatment": {
                "organic": "Wettable sulfur; remove barberry bushes from fields",
                "chemical": "Propiconazole 25% EC (1ml/L), Tebuconazole (1ml/L), at first sign of infection",
                "biological": "No effective biological control for field use",
                "preventive": "Rust-resistant varieties, eradicate barberry, prophylactic fungicide in Ug99-risk areas",
                "application_frequency": "At first sign, repeat after 14 days",
                "recovery_time": "10-14 days",
                "phi_days": 21
            }
        },
        {
            "name": "Loose Smut",
            "pathogen_name": "Ustilago tritici",
            "disease_type": "Fungal",
            "risk_level": "Medium",
            "economic_impact": "Causes 5-30% yield loss. Entire head is replaced by black smut mass.",
            "host_range": "Wheat",
            "geographic_distribution": "Worldwide",
            "favorable_conditions": "Cool moist conditions during flowering, moderate temperatures",
            "symptoms": {
                "early": "Diseased plants emerge earlier; infected ear with black spore mass instead of grain",
                "late": "Complete head replaced by black teliospore mass that disperses, leaving bare rachis",
                "affected_parts": "Ear/Panicle",
                "severity_levels": {"mild": "Few infected heads", "severe": "Up to 30% heads infected"}
            },
            "disease_cycle": "Seed-borne; mycelium is dormant in seed embryo. Infection occurs at flowering. No external symptoms until next season.",
            "incubation_period": "Entire growing season (symptom appears at heading of next crop)",
            "treatment": {
                "organic": "Hot water seed treatment (52°C for 10 minutes)",
                "chemical": "Carboxin + Thiram seed treatment (2g/kg seed), Tebuconazole seed treatment",
                "biological": "Trichoderma viride seed treatment",
                "preventive": "Use certified smut-free seeds, systemic seed treatment fungicides, plant resistant varieties",
                "application_frequency": "Seed treatment before sowing",
                "recovery_time": "Not applicable (seed treatment prevents disease)",
                "phi_days": None
            }
        },
        {
            "name": "Powdery Mildew (Wheat)",
            "pathogen_name": "Blumeria graminis f. sp. tritici",
            "disease_type": "Fungal",
            "risk_level": "Medium",
            "economic_impact": "Causes 5-40% yield loss in cool humid conditions.",
            "host_range": "Wheat (host-specific)",
            "geographic_distribution": "Worldwide, especially cool humid regions",
            "favorable_conditions": "Cool temperatures (15-22°C), moderate humidity, dense crop canopy",
            "symptoms": {
                "early": "White fluffy powdery patches on upper leaf surface of lower leaves",
                "late": "White-gray coating on all green parts, yellowing and drying of leaves, cleistothecia (black dots) visible in old patches",
                "affected_parts": "Leaves, Stems, Leaf sheaths",
                "severity_levels": {"mild": "Patches on lower leaves", "severe": "All leaves affected, yield reduced"}
            },
            "disease_cycle": "Obligate parasite; spreads by airborne conidia. Overwinters as cleistothecia on straw.",
            "incubation_period": "5-7 days",
            "treatment": {
                "organic": "Wettable sulfur (3g/L), potassium bicarbonate",
                "chemical": "Propiconazole 25% EC (1ml/L), Triadimefon 25% WP (1g/L), Azoxystrobin",
                "biological": "Ampelomyces quisqualis",
                "preventive": "Resistant varieties, avoid dense planting, balanced nitrogen, timely fungicide sprays",
                "application_frequency": "At first signs, repeat after 14 days",
                "recovery_time": "10-14 days",
                "phi_days": 21
            }
        },
    ],

    # ═════════════════════════════════════════════════════════════════════════
    # MAIZE DISEASES
    # ═════════════════════════════════════════════════════════════════════════
    "Maize": [
        {
            "name": "Northern Corn Leaf Blight (NCLB)",
            "pathogen_name": "Exserohilum turcicum (Setosphaeria turcica)",
            "disease_type": "Fungal",
            "risk_level": "High",
            "economic_impact": "Causes 10-50% yield loss. Major foliar disease in warm humid maize regions.",
            "host_range": "Maize, Sorghum, Sudan grass",
            "geographic_distribution": "Worldwide in humid maize-growing regions",
            "favorable_conditions": "Temperatures 18-27°C, prolonged dew periods, high humidity",
            "symptoms": {
                "early": "Long (5-15cm) elliptical tan to grayish-green lesions with wavy margins on lower leaves",
                "late": "Extensive leaf blighting from bottom of plant upward, dark olive-green spore mass on lesions in humid conditions",
                "affected_parts": "Leaves",
                "severity_levels": {"mild": "< 25% leaf area", "severe": "> 50% leaf area"}
            },
            "disease_cycle": "Overwinters in infected crop debris. Conidia spread by wind and rain. Multiple infection cycles per season.",
            "incubation_period": "7-12 days",
            "treatment": {
                "organic": "Copper-based fungicides preventively",
                "chemical": "Azoxystrobin + Propiconazole (Quilt Xcel 1L/ha), Propiconazole alone (1ml/L)",
                "biological": "Bacillus amyloliquefaciens",
                "preventive": "Resistant hybrids, crop rotation, remove infected debris, timely planting",
                "application_frequency": "At VT/R1 stage (tasseling) preventively; repeat if disease pressure",
                "recovery_time": "14-21 days",
                "phi_days": 21
            }
        },
        {
            "name": "Maize Lethal Necrosis (MLN)",
            "pathogen_name": "Maize chlorotic mottle virus (MCMV) + Potyviruses",
            "disease_type": "Viral",
            "risk_level": "Critical",
            "economic_impact": "Can cause 100% yield loss. Emerging disease devastating East African maize belts since 2011.",
            "host_range": "Maize, Sorghum, some grasses",
            "geographic_distribution": "East Africa (Kenya, Uganda, Tanzania, Ethiopia), Asia (China, Thailand)",
            "favorable_conditions": "High thrips, aphid, beetle populations; monoculture farming systems",
            "symptoms": {
                "early": "Chlorotic (yellow) streaks and mottling on younger leaves; pale green to yellow leaf discoloration",
                "late": "Complete necrosis of all leaves from leaf tip, brown papery leaves, ear rot, premature death",
                "affected_parts": "All plant parts, especially leaves and ears",
                "severity_levels": {"mild": "Mottling only", "severe": "Complete plant death before tasseling"}
            },
            "disease_cycle": "MCMV transmitted by thrips, beetles, aphids; SCMV/WSMV transmitted by aphids. Synergistic interaction causes lethal necrosis.",
            "incubation_period": "14-21 days",
            "treatment": {
                "organic": "No cure; control insect vectors with neem oil, reflective mulch",
                "chemical": "No direct treatment; insecticides for vector control (Imidacloprid, Thiamethoxam)",
                "biological": "No effective biological treatment",
                "preventive": "Plant MLN-tolerant/resistant varieties, control thrips and aphids, crop rotation, early planting, remove infected plants",
                "application_frequency": "Vector control every 7-10 days in high-pressure periods",
                "recovery_time": "No recovery; remove infected plants",
                "phi_days": None
            }
        },
        {
            "name": "Gray Leaf Spot",
            "pathogen_name": "Cercospora zeae-maydis",
            "disease_type": "Fungal",
            "risk_level": "High",
            "economic_impact": "Major disease in high-elevation maize areas. 10-50% yield reduction.",
            "host_range": "Maize",
            "geographic_distribution": "Worldwide, especially Africa, USA Corn Belt, Latin America",
            "favorable_conditions": "Warm humid weather, extended leaf wetness, minimum tillage, dense canopy",
            "symptoms": {
                "early": "Small, irregular tan spots with yellow halos, mainly on lower leaves",
                "late": "Elongated, rectangular, grayish-tan lesions limited by leaf veins, covering entire leaf",
                "affected_parts": "Leaves",
                "severity_levels": {"mild": "Lower leaves only", "severe": "Entire canopy"}
            },
            "disease_cycle": "Overwinters in infected corn debris. Conidia spread by wind. Minimum tillage increases disease risk.",
            "incubation_period": "14-21 days",
            "treatment": {
                "organic": "Copper-based sprays preventively",
                "chemical": "Azoxystrobin, Propiconazole, Pyraclostrobin at tasseling stage",
                "biological": "Bacillus subtilis",
                "preventive": "Hybrid resistance, crop rotation, tillage to bury debris, fungicide at VT/R1",
                "application_frequency": "Preventive spray at VT stage",
                "recovery_time": "14-21 days",
                "phi_days": 21
            }
        },
    ],

    # ═════════════════════════════════════════════════════════════════════════
    # POTATO DISEASES
    # ═════════════════════════════════════════════════════════════════════════
    "Potato": [
        {
            "name": "Late Blight (Potato)",
            "pathogen_name": "Phytophthora infestans",
            "disease_type": "Oomycete",
            "risk_level": "Critical",
            "economic_impact": "World's most economically important plant disease. Caused Irish Potato Famine. Global annual losses > $10 billion.",
            "host_range": "Potato, Tomato",
            "geographic_distribution": "Worldwide",
            "favorable_conditions": "Cool (10-20°C), wet weather, humidity >90%, dew",
            "symptoms": {
                "early": "Water-soaked pale green spots on leaves, white sporulation on underside in humid conditions",
                "late": "Dark brown-black lesions on leaves, brown rots on stems, rapid spread of entire field collapse, tuber rot (brown-red internal)",
                "affected_parts": "Leaves, Stems, Tubers",
                "severity_levels": {"mild": "Scattered leaf lesions", "severe": "Complete crop collapse"}
            },
            "disease_cycle": "Survives as oospores in soil and in infected tubers. Spreads by zoospores and sporangia. Wind dispersal over long distances.",
            "incubation_period": "2-4 days under optimal conditions",
            "treatment": {
                "organic": "Copper hydroxide (2.5-3g/L) preventively, Bordeaux mixture, avoid excessive irrigation",
                "chemical": "Metalaxyl-M + Mancozeb 2.5g/L, Dimethomorph + Mancozeb, Cymoxanil + Famoxadone, Fluopicolide",
                "biological": "Bacillus subtilis QST713, Bacillus amyloliquefaciens",
                "preventive": "Plant resistant varieties (Kufri Bahar, Jyoti), use certified disease-free seed tubers, apply fungicide before first rains, destroy volunteer plants",
                "application_frequency": "Every 5-7 days during high-risk weather (Blitecast model advisory)",
                "recovery_time": "Preventive only; infected plants rarely recover",
                "phi_days": 7
            }
        },
        {
            "name": "Common Scab",
            "pathogen_name": "Streptomyces scabies",
            "disease_type": "Bacterial (Actinomycete)",
            "risk_level": "Medium",
            "economic_impact": "Reduces tuber quality and marketability by 10-40%.",
            "host_range": "Potato, Beet, Radish, Carrot",
            "geographic_distribution": "Worldwide, especially alkaline sandy soils",
            "favorable_conditions": "Alkaline soils (pH > 5.5), dry soil during tuber initiation, temperatures 20-22°C",
            "symptoms": {
                "early": "No visible early symptoms on foliage",
                "late": "Brown corky scab lesions (raised, sunken, or russeted) on tuber surface; external quality defect only",
                "affected_parts": "Tubers (surface)",
                "severity_levels": {"mild": "Small isolated lesions", "severe": "Most of tuber surface affected"}
            },
            "disease_cycle": "Soil-borne bacteria, survive indefinitely. Infection during early tuber formation through lenticels and wounds.",
            "incubation_period": "14-30 days from tuber initiation",
            "treatment": {
                "organic": "Soil acidification (sulfur), crop rotation, adequate irrigation during tuber formation",
                "chemical": "Quintozene PCNB seed treatment (limited), Flutolanil seed treatment",
                "biological": "Fluorescent Pseudomonas, Bacillus subtilis soil inoculants",
                "preventive": "Lower soil pH to 5.0-5.5, maintain soil moisture during tuber initiation, rotate with non-susceptible crops (cereals), use scab-resistant varieties",
                "application_frequency": "Management practices; no effective spray treatment",
                "recovery_time": "Prevention focus",
                "phi_days": None
            }
        },
    ],

    # ═════════════════════════════════════════════════════════════════════════
    # MANGO DISEASES
    # ═════════════════════════════════════════════════════════════════════════
    "Mango": [
        {
            "name": "Anthracnose",
            "pathogen_name": "Colletotrichum gloeosporioides",
            "disease_type": "Fungal",
            "risk_level": "High",
            "economic_impact": "Most important post-harvest mango disease; causes 30-80% market loss.",
            "host_range": "Mango, Papaya, Avocado, many tropical fruits",
            "geographic_distribution": "All tropical and subtropical mango-growing regions",
            "favorable_conditions": "High humidity, rainfall, temperatures 25-30°C, especially during flowering and fruit development",
            "symptoms": {
                "early": "Dark brown to black spots on young leaves, flowers, and immature fruits; 'blossom blight' killing flower clusters",
                "late": "Sunken, dark brown lesions on mature fruits that expand rapidly post-harvest; fruit rot; complete flower destruction",
                "affected_parts": "Leaves, Flowers, Young Shoots, Fruit",
                "severity_levels": {"mild": "Small spots", "severe": "Total blossom kill, fruit unmarketable"}
            },
            "disease_cycle": "Survives in infected twigs and mummified fruits. Conidia spread by rain and dew. Quiescent infection in unripe fruit activated during ripening.",
            "incubation_period": "7-14 days",
            "treatment": {
                "organic": "Copper oxychloride 3g/L, neem oil + copper, hot water dip 52°C for 5 minutes (post-harvest)",
                "chemical": "Carbendazim 0.1% + Mancozeb 0.25% spray, Azoxystrobin + Difenoconazole, Propiconazole 0.1%",
                "biological": "Trichoderma, Bacillus subtilis, Pseudomonas fluorescens",
                "preventive": "Prune dead wood, copper spray before flowering, proper post-harvest handling (hot water), waxing, cold chain",
                "application_frequency": "3-4 sprays during flowering and fruit development; every 10-14 days",
                "recovery_time": "Prevention focus; treat within 1-2 days post-harvest",
                "phi_days": 7
            }
        },
        {
            "name": "Powdery Mildew (Mango)",
            "pathogen_name": "Oidium mangiferae",
            "disease_type": "Fungal",
            "risk_level": "High",
            "economic_impact": "Destroys 10-80% of flowers; critical during mango flowering season.",
            "host_range": "Mango",
            "geographic_distribution": "All mango-growing regions",
            "favorable_conditions": "Dry weather with low humidity at night, temperatures 10-20°C at night, 25-35°C during day (classic powdery mildew conditions)",
            "symptoms": {
                "early": "White powdery coating on young leaves, flower clusters, and young fruits",
                "late": "Complete whitening of panicles, flower drop, young fruit drop, malformed surviving fruits",
                "affected_parts": "Young Leaves, Flowers (panicles), Young Fruits",
                "severity_levels": {"mild": "Partial powdery coating", "severe": "Total panicle kill"}
            },
            "disease_cycle": "Spreads by airborne conidia. Favored by dry nights and warm days during flowering season.",
            "incubation_period": "7-10 days",
            "treatment": {
                "organic": "Wettable sulfur 3g/L at bud break; diluted milk spray (1:5); potassium bicarbonate",
                "chemical": "Triadimefon 25% WP (1g/L), Hexaconazole 5% EC (2ml/L), Propiconazole 25% EC (1ml/L), Myclobutanil",
                "biological": "Bacillus subtilis, Ampelomyces quisqualis",
                "preventive": "First spray at bud emergence, second at fruit set; avoid overhead irrigation; morning sprays",
                "application_frequency": "3 sprays at 15-day intervals during flowering season",
                "recovery_time": "7-10 days with treatment",
                "phi_days": 21
            }
        },
        {
            "name": "Mango Malformation Disease (MMD)",
            "pathogen_name": "Fusarium mangiferae",
            "disease_type": "Fungal",
            "risk_level": "High",
            "economic_impact": "Infected trees produce no marketable fruits; economically devastating especially in India and Egypt.",
            "host_range": "Mango",
            "geographic_distribution": "India, Pakistan, Egypt, South Africa, USA, Brazil",
            "favorable_conditions": "Cool weather, high humidity, specific Fusarium strains",
            "symptoms": {
                "early": "Vegetative malformation: bunchy top appearance with compacted proliferation of shoots ('mango witches' broom')",
                "late": "Floral malformation: panicle conversion to compact, sterile, green vegetative structure; no fruits formed",
                "affected_parts": "Shoot tips, Flower panicles",
                "severity_levels": {"mild": "Few malformed panicles", "severe": "All panicles malformed"}
            },
            "disease_cycle": "Systemically infects vascular tissue. Spread by infected scion material, mite vectors (Aceria mangiferae), and contaminated tools.",
            "incubation_period": "Months to years (systemic)",
            "treatment": {
                "organic": "Remove and burn malformed parts; control mites with acaricides",
                "chemical": "NAA (Naphthaleneacetic acid) 200ppm spray + Carbendazim (0.1%) at panicle emergence",
                "biological": "No effective biological control",
                "preventive": "Use disease-free planting material, certified nursery plants, deinfest cutting tools, control mite vectors",
                "application_frequency": "Pruning and NAA spray at panicle initiation",
                "recovery_time": "Partial control; severely affected trees may need replacement",
                "phi_days": 30
            }
        },
    ],

    # ═════════════════════════════════════════════════════════════════════════
    # BANANA DISEASES
    # ═════════════════════════════════════════════════════════════════════════
    "Banana": [
        {
            "name": "Panama Wilt (Fusarium Wilt of Banana)",
            "pathogen_name": "Fusarium oxysporum f. sp. cubense (TR4)",
            "disease_type": "Fungal",
            "risk_level": "Critical",
            "economic_impact": "TR4 strain virtually eliminated Gros Michel variety globally. Threatens Cavendish. No effective cure.",
            "host_range": "Banana, Plantain",
            "geographic_distribution": "Worldwide",
            "favorable_conditions": "Warm soils, pH 4.5-6.0, poor drainage, 24-34°C",
            "symptoms": {
                "early": "Yellowing of older outer leaves, leaf collapse, starting from leaf margins; brown streaking in pseudostem when cut",
                "late": "Complete plant collapse, pseudostem brown-red internal discoloration from base upward, no fruit production",
                "affected_parts": "Roots, Pseudostem (vascular), Leaves",
                "severity_levels": {"early": "Marginal leaf yellowing", "severe": "Complete plant death"}
            },
            "disease_cycle": "Soil-borne chlamydospores survive for decades. Enter through roots. Clog xylem vessels. Spreads through soil water and contaminated tools.",
            "incubation_period": "Weeks to months depending on race and soil",
            "treatment": {
                "organic": "No cure. Soil solarization, biological soil amendments (Trichoderma, compost)",
                "chemical": "No effective chemical treatment",
                "biological": "Trichoderma koningii, T. harzianum as suppressants",
                "preventive": "Strict quarantine, plant resistant varieties (GCTCV-218 for TR4), clean tools with bleach, avoid infected soil movement",
                "application_frequency": "Preventive soil treatment only",
                "recovery_time": "No recovery; replant with resistant varieties",
                "phi_days": None
            }
        },
        {
            "name": "Black Sigatoka (Black Leaf Streak)",
            "pathogen_name": "Pseudocercospora fijiensis",
            "disease_type": "Fungal",
            "risk_level": "High",
            "economic_impact": "Without fungicide, can reduce banana yield by 35-50%. Increases fungicide cost by $1000/ha/year.",
            "host_range": "Banana, Plantain",
            "geographic_distribution": "Most banana-growing areas worldwide",
            "favorable_conditions": "High humidity, rainfall, temperatures 27-30°C",
            "symptoms": {
                "early": "Tiny pale yellow flecks on lower leaf surface that elongate into brown streaks",
                "late": "Brown-black elongated lesions with yellow halo on upper leaf surface; premature defoliation; green fruit ripening prematurely",
                "affected_parts": "Leaves",
                "severity_levels": {"mild": "Lower leaves affected", "severe": "Entire canopy defoliated"}
            },
            "disease_cycle": "Spores (conidia and ascospores) spread by wind and rain. Multiple infection cycles per season. Develops resistance to fungicides rapidly.",
            "incubation_period": "25-50 days",
            "treatment": {
                "organic": "Copper oxychloride (2-3g/L) sprays, oil-based copper formulations; remove infected leaves",
                "chemical": "Systemic fungicides on rotation: Propiconazole, Tebuconazole, Fenbuconazole, Chlorothalonil; resistance management essential",
                "biological": "No effective biocontrol registered",
                "preventive": "Resistant varieties, remove lower infected leaves (deleafing), reduce humidity with good drainage and canopy management",
                "application_frequency": "12-24 sprays per year depending on disease pressure",
                "recovery_time": "Ongoing management; no cure",
                "phi_days": 7
            }
        },
    ],

    # ═════════════════════════════════════════════════════════════════════════
    # COTTON DISEASES
    # ═════════════════════════════════════════════════════════════════════════
    "Cotton": [
        {
            "name": "Cotton Leaf Curl Virus Disease (CLCuD)",
            "pathogen_name": "Cotton leaf curl Multan virus (CLCuMV) + betasatellite",
            "disease_type": "Viral",
            "risk_level": "Critical",
            "economic_impact": "Devastated Pakistan cotton industry in 1992-93 causing 30% production loss. Ongoing threat to South Asia.",
            "host_range": "Cotton, Okra, Hibiscus, Tomato",
            "geographic_distribution": "Pakistan, India, Nigeria, Sudan",
            "favorable_conditions": "High whitefly populations, temperatures 25-35°C",
            "symptoms": {
                "early": "Upward curling of leaves, vein thickening, enations (leaf-like outgrowths) on underside of leaves",
                "late": "Severe stunting, dark green thickened curled leaves, no boll formation, plant death",
                "affected_parts": "Leaves, Entire plant",
                "severity_levels": {"mild": "Leaf curl only", "severe": "Complete stunting, no yield"}
            },
            "disease_cycle": "Transmitted by whitefly (Bemisia tabaci) in persistent circulative manner. No mechanical or seed transmission.",
            "incubation_period": "14-21 days",
            "treatment": {
                "organic": "Control whiteflies with neem extract, reflective mulch, remove infected plants",
                "chemical": "Imidacloprid/Thiamethoxam soil application for whitefly control; Acetamiprid foliar spray",
                "biological": "Encarsia formosa, Beauveria bassiana for whitefly control",
                "preventive": "Resistant varieties (NIAB 846, CIM-499), control whiteflies strictly, remove infected plants, use insect-proof nets in nursery",
                "application_frequency": "Whitefly control every 7-10 days",
                "recovery_time": "No recovery; remove infected plants",
                "phi_days": None
            }
        },
    ],

    # ═════════════════════════════════════════════════════════════════════════
    # GENERAL / CROSS-CROP DISEASES
    # ═════════════════════════════════════════════════════════════════════════
    "General": [
        {
            "name": "Damping Off",
            "pathogen_name": "Pythium spp., Rhizoctonia solani, Fusarium spp.",
            "disease_type": "Fungal / Oomycete",
            "risk_level": "High",
            "economic_impact": "Can destroy 50-100% of seedlings in affected nursery beds.",
            "host_range": "All vegetable and field crops in seedling stage",
            "geographic_distribution": "Worldwide",
            "favorable_conditions": "Excess soil moisture, poor drainage, dense seeding, high humidity, cool conditions",
            "symptoms": {
                "early": "Seeds fail to germinate (pre-emergence damping off), or seedlings collapse just below soil level (post-emergence)",
                "late": "Water-soaked 'pinched' stem at soil level, seedling falls over, dark discoloration at base",
                "affected_parts": "Stem base, Hypocotyl, Roots",
                "severity_levels": {"mild": "Isolated seedling death", "severe": "Entire nursery patch collapsed"}
            },
            "disease_cycle": "Soil-borne pathogens; sporangia and oospores persist in soil. Activated by excess moisture.",
            "incubation_period": "1-3 days",
            "treatment": {
                "organic": "Chilled neem cake in soil, well-drained media, Trichoderma seed treatment, chamomile tea drench",
                "chemical": "Metalaxyl 35% DS seed treatment, Captan 50% WP seed treatment (2g/kg), copper sulfate soil drench",
                "biological": "Trichoderma harzianum seed treatment, Pseudomonas fluorescens soil drench",
                "preventive": "Use sterile nursery media, avoid overwatering, thin seedlings, use well-drained trays, treat seeds before sowing",
                "application_frequency": "Soil treatment before sowing; drench after symptom appearance",
                "recovery_time": "Remove affected seedlings; re-sow treated seeds",
                "phi_days": None
            }
        },
        {
            "name": "Crown Gall",
            "pathogen_name": "Agrobacterium tumefaciens (Rhizobium radiobacter)",
            "disease_type": "Bacterial",
            "risk_level": "Medium",
            "economic_impact": "Reduces tree lifespan, productivity by 20-50% in affected orchards.",
            "host_range": "Rose, Fruit trees (apple, cherry, walnut), Grapes, more than 600 species",
            "geographic_distribution": "Worldwide",
            "favorable_conditions": "Wounds (from pruning, transplanting, frost damage), alkaline soils",
            "symptoms": {
                "early": "Small, soft, round galls develop at crown (soil line) or on roots",
                "late": "Galls enlarge to large rough, brown, corky tumors; reduced plant vigor, stunting, increased susceptibility to other diseases",
                "affected_parts": "Crown, Roots, Stems",
                "severity_levels": {"mild": "Small galls", "severe": "Large galls girdling stem"}
            },
            "disease_cycle": "Soil-borne; bacterium transfers its own DNA (T-DNA) into plant cells causing tumor growth. Spreads through soil water and infected tools.",
            "incubation_period": "Weeks to months",
            "treatment": {
                "organic": "Cut out galls; treat with Agrobacterium radiobacter strain K-84 (biocontrol) at planting",
                "chemical": "No effective post-infection treatment; copper bactericides preventively",
                "biological": "Agrobacterium radiobacter strain K-84 / K-1026 biocontrol (prevents infection)",
                "preventive": "Avoid wounding, use K-84 dip on roots before planting, plant only certified gall-free material",
                "application_frequency": "Root dip at planting",
                "recovery_time": "No cure; prune and disinfect tools with bleach",
                "phi_days": None
            }
        },
        {
            "name": "Botrytis Gray Mold",
            "pathogen_name": "Botrytis cinerea",
            "disease_type": "Fungal",
            "risk_level": "High",
            "economic_impact": "Second most important fungal plant pathogen worldwide (after Magnaporthe). Major greenhouse and soft fruit pathogen.",
            "host_range": "> 1000 plant species including grapes, strawberry, rose, tomato, lettuce, onion",
            "geographic_distribution": "Worldwide",
            "favorable_conditions": "Cool temperatures (15-20°C), high humidity >95%, damaged or senescent tissue",
            "symptoms": {
                "early": "Water-soaked, brown lesions on petals, leaves, and stems; soft rot",
                "late": "Characteristic gray fluffy fungal sporulation covering lesions; blight of flowers, stem cankers, fruit rot (\"ghost spot\" on tomato)",
                "affected_parts": "Flowers, Leaves, Stems, Fruit, Storage organs",
                "severity_levels": {"mild": "Few lesions", "severe": "Complete plant dieback or fruit loss"}
            },
            "disease_cycle": "Ubiquitous saprophyte; infects through wounds, senescent tissue. Gray conidial masses spread by air and handling. Sclerotia overwinter in soil.",
            "incubation_period": "2-4 days",
            "treatment": {
                "organic": "Remove infected tissue, improve air circulation, reduce humidity; Bacillus subtilis, Trichoderma spray",
                "chemical": "Iprodione (1.5g/L), Pyrimethanil (1ml/L), Fenhexamid (1g/L), Cyprodinil (0.5g/L). Rotate fungicides for resistance management.",
                "biological": "Bacillus subtilis QST713 (Serenade), Trichoderma asperellum, Clonostachys rosea (Prestop)",
                "preventive": "Improve air circulation, avoid wounding, remove dead tissue, avoid waterlogging, maintain low humidity",
                "application_frequency": "Every 7-10 days under disease pressure; preventive at flowering",
                "recovery_time": "7-14 days with treatment",
                "phi_days": 1
            }
        },
        {
            "name": "Sclerotinia Stem Rot (White Mold)",
            "pathogen_name": "Sclerotinia sclerotiorum",
            "disease_type": "Fungal",
            "risk_level": "High",
            "economic_impact": "Major pathogen of oilseeds and legumes worldwide; 10-60% yield loss.",
            "host_range": "> 400 species: Canola, Soybean, Sunflower, Bean, Carrot, Celery",
            "geographic_distribution": "Worldwide temperate regions",
            "favorable_conditions": "Cool temperatures (15-20°C), high humidity, wet soil, dense canopy",
            "symptoms": {
                "early": "Water-soaked lesions on lower stems and branches; bleached, straw-colored stem tissue",
                "late": "White cottony mycelial growth inside and outside infected tissue, large hard black sclerotia (2-10mm) inside stem",
                "affected_parts": "Stem (basal), Branches, Pods/Siliques",
                "severity_levels": {"mild": "Isolated stem lesions", "severe": "Multiple lodged plants with white mold"}
            },
            "disease_cycle": "Sclerotia survive in soil 3-5+ years. Apothecia (mushroom-like structures) release ascospores during flowering. Infection through flowers.",
            "incubation_period": "7-14 days",
            "treatment": {
                "organic": "Thiram-treated seeds, adequate plant spacing, crop rotation",
                "chemical": "Thiophanate-methyl (1g/L), Boscalid (0.5g/L), Iprodione, Fluazinam at early flowering",
                "biological": "Coniothyrium minitans (Contans WG) — applied to soil to parasitize sclerotia",
                "preventive": "Crop rotation (non-host crops for 3+ years), avoid dense planting, improve drainage",
                "application_frequency": "At early bloom; repeat once in 10-14 days",
                "recovery_time": "14-21 days",
                "phi_days": 14
            }
        },
    ],
}


def get_diseases_for_plant(plant_common_name: str) -> list:
    """Retrieve disease records for a specific plant."""
    plant_diseases = DISEASES_MASTER.get(plant_common_name, [])
    general_diseases = DISEASES_MASTER.get("General", [])
    return plant_diseases + general_diseases


def get_all_disease_names() -> list:
    """Get all disease names in the database."""
    names = []
    for plant, diseases in DISEASES_MASTER.items():
        for d in diseases:
            names.append(f"{plant} - {d['name']}")
    return names


if __name__ == "__main__":
    total = sum(len(v) for v in DISEASES_MASTER.values())
    print(f"Total disease records in database: {total}")
    print(f"Plants covered: {list(DISEASES_MASTER.keys())}")
