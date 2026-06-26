import json
from sqlalchemy.orm import Session
from models import (
    Plant, BotanicalClassification, Family, Genus, SpeciesRecord, Variety,
    ClimateRequirement, SoilRequirement, Disease, DiseaseSymptom, DiseaseTreatment,
    Pest, NutrientDeficiency, FertilizerRecommendation, IrrigationSchedule,
    HarvestInformation, GrowthStage, PlantImage
)

# Detailed data for botanical seeding
SEED_CROPS = [
    {
        "common_name": "Tomato",
        "botanical_name": "Solanum lycopersicum",
        "synonyms": "Lycopersicon esculentum",
        "local_names": "Tamatar, Tomato",
        "family": "Solanaceae",
        "genus": "Solanum",
        "species": "lycopersicum",
        "plant_authority": "L.",
        "overview": "The tomato is the edible berry of the plant Solanum lycopersicum. The species originated in western South America and Central America. Its horticultural use has spread worldwide.",
        "morphology": "Herbaceous annual or perennial, with branching hairy stems and compound leaves. Flower clusters arise opposite the leaves.",
        "leaf_desc": "Odd-pinnate, alternate, covered with fine trichomes, yielding a strong distinct aroma.",
        "flower_desc": "Yellow flowers with five petals, borne in clusters (cymes).",
        "fruit_desc": "Globose to oblate berry, fleshy, green when immature, ripening to red, yellow, or purple.",
        "seed_desc": "Small, flattened, kidney-shaped, covered in silky hairs.",
        "stem_desc": "Hairy, green, initially erect but becomes decumbent or prostrate as it grows.",
        "root_desc": "Deep taproot system reaching up to 1.5 meters, with extensive fibrous lateral roots.",
        "growth_habit": "Vining (indeterminate) or bushy (determinate)",
        "life_cycle": "Annual",
        "average_height": "1.0 - 3.0 m",
        "average_width": "0.6 - 1.2 m",
        "lifespan": "1 growing season",
        "category": "Vegetable",
        "commercial_uses": "Fresh consumption, canned products, paste, ketchup, purees, juice",
        "medicinal_uses": "Rich source of lycopene (antioxidant), vitamin C, and potassium; supports heart health and skin care",
        "industrial_uses": "Food processing industries, seed oil extraction for cosmetics",
        "food_uses": "Salads, cooking ingredient, sauces, soups",
        "toxicity": "Foliage and green stems contain solanine, a toxic glycoalkaloid, and should not be consumed.",
        "conservation_status": "Least Concern",
        "classification": {
            "kingdom": "Plantae",
            "division": "Tracheophyta",
            "class_name": "Magnoliopsida",
            "order_name": "Solanales",
            "taxonomy_hierarchy": "Plantae -> Tracheophyta -> Magnoliopsida -> Solanales -> Solanaceae -> Solanum -> Solanum lycopersicum"
        },
        "varieties": [
            {"name": "Roma", "variety_type": "Determinate Plum Tomato", "growing_period": "75 days", "yield_potential": "35-40 tons/acre"},
            {"name": "San Marzano", "variety_type": "Indeterminate Plum Tomato", "growing_period": "80 days", "yield_potential": "30-35 tons/acre"},
            {"name": "Beefsteak", "variety_type": "Indeterminate Slicing Tomato", "growing_period": "85 days", "yield_potential": "25-30 tons/acre"}
        ],
        "climate": {
            "native_region": "Andean South America",
            "countries_grown": "China, India, USA, Turkey, Egypt, Italy",
            "climatic_zones": "Warm Temperate, Subtropical, Tropical",
            "suitable_altitude": "0 - 2000 m",
            "rainfall_requirement": "600 - 800 mm",
            "temperature_requirement": "18°C - 28°C",
            "humidity_requirement": "60% - 70%"
        },
        "soil": {
            "preferred_soil": "Sandy Loam to Clay Loam",
            "soil_ph_range": "6.0 - 6.8",
            "drainage": "Well-drained",
            "organic_matter": "High (2-4%)",
            "fertility": "High",
            "texture": "Medium textured, aerated"
        },
        "diseases": [
            {
                "name": "Early Blight",
                "pathogen_name": "Alternaria solani",
                "disease_type": "Fungal",
                "risk_level": "Medium",
                "economic_impact": "Causes significant defoliation and reduces yield by 30-50% in warm, humid conditions.",
                "symptoms": {
                    "early_symptoms": "Small brown spots on older leaves developing target-like concentric rings.",
                    "late_symptoms": "Leaf yellowing, drop, and dark sunken lesions at stem-ends of fruit.",
                    "affected_parts": "Leaves, Stems, Fruits"
                },
                "treatment": {
                    "immediate_treatment": "Remove infected leaves. Apply copper oxychloride or chlorothalonil spray.",
                    "organic_treatment": "Spray neem oil solution (4ml/L) or copper-octanoate soap mix. Enhance spacing.",
                    "chemical_treatment": "Use Mancozeb (2g/L) or Azoxystrobin systemic fungicide.",
                    "biological_control": "Apply Trichoderma harzianum to the soil.",
                    "recommended_fungicides": "Mancozeb, Chlorothalonil, Azoxystrobin",
                    "recommended_organic_solutions": "Neem Oil, Copper Hydroxide, Baking Soda spray",
                    "dosage": "2 grams per Liter of water",
                    "application_frequency": "Every 7-10 days in wet conditions",
                    "safety_precautions": "Wear mask and gloves; respect 7-day pre-harvest interval for chemical sprays.",
                    "recovery_time": "10 - 14 days"
                }
            },
            {
                "name": "Late Blight",
                "pathogen_name": "Phytophthora infestans",
                "disease_type": "Fungal",
                "risk_level": "High",
                "economic_impact": "Can completely destroy a tomato crop within a few days under cool, wet weather.",
                "symptoms": {
                    "early_symptoms": "Water-soaked irregular spots on leaves and petioles that expand rapidly.",
                    "late_symptoms": "Fuzzy white mold on underside of leaves, dark greasy patches on fruits, and total plant collapse.",
                    "affected_parts": "Leaves, Stems, Fruits, Tubers"
                },
                "treatment": {
                    "immediate_treatment": "Destroy infected crops. Apply systemic metalaxyl-mancozeb combination.",
                    "organic_treatment": "Apply copper hydroxide preventive spray. Keep leaves dry by drip watering.",
                    "chemical_treatment": "Use Metalaxyl-M or Cymoxanil/Famoxadone combinations.",
                    "biological_control": "Utilize Bacillus subtilis strains for suppression.",
                    "recommended_fungicides": "Ridomil Gold, Mancozeb, Cabrio Duo",
                    "recommended_organic_solutions": "Copper Fungicides, Bacillus subtilis bio-fungicide",
                    "dosage": "2.5 grams per Liter",
                    "application_frequency": "Every 5-7 days under epidemic threat",
                    "safety_precautions": "Wash hands post-application; keep livestock away from treated plots.",
                    "recovery_time": "7 - 10 days (preventive focus)"
                }
            }
        ],
        "pests": [
            {
                "name": "Whiteflies",
                "scientific_name": "Bemisia tabaci",
                "identification": "Tiny, 1mm white-winged sap-sucking insects that fly in clouds when disturbed.",
                "damage_symptoms": "Yellowing leaves, sticky honeydew, black sooty mold growth, and vectoring Yellow Leaf Curl Virus.",
                "lifecycle": "Egg to adult in 20-30 days; multiplies rapidly in hot seasons.",
                "organic_control": "Yellow sticky cards, neem oil spray, introducing predatory lady beetles.",
                "chemical_control": "Imidacloprid or Acetamiprid systemic insecticide application.",
                "biological_control": "Encarsia formosa parasitic wasps.",
                "economic_threshold": "5 adults per leaf"
            }
        ],
        "deficiencies": [
            {
                "nutrient_name": "Nitrogen",
                "symptoms": "Overall pale green to yellow leaves, starting from the oldest bottom leaves. Stems become thin and fibrous.",
                "correction_methods": "Apply urea, ammonium nitrate, or organic blood meal/compost.",
                "recommended_fertilizers": "Urea (46% N), Ammonium Sulphate, Compost Tea"
            },
            {
                "nutrient_name": "Calcium",
                "symptoms": "Blossom End Rot: Light brown to black leathery circular patches on the bottom (blossom end) of the tomato fruit.",
                "correction_methods": "Incorporate agricultural lime or gypsum into soil, or apply foliar calcium chloride spray.",
                "recommended_fertilizers": "Calcium Nitrate, Gypsum, Bone Meal"
            }
        ],
        "fertilizer": {
            "organic_fertilizers": "Well-rotted farmyard manure, vermicompost, bone meal",
            "chemical_fertilizers": "NPK 10-26-26 at planting, Urea top-dressing at flowering",
            "npk_ratio": "5-10-10 (basal) & 46-0-0 (top-dressing)",
            "application_timing": "Basal at transplanting, top-dressing 30 and 60 days after transplanting",
            "application_qty": "50g NPK per plant at planting, 10g Urea per plant later"
        },
        "irrigation": {
            "water_requirement": "High",
            "daily_water_need": "3 - 5 Liters per plant",
            "weekly_water_need": "20 - 35 Liters per plant",
            "drip_recommendation": "Use inline drip emitters (2 L/hr), run for 1-2 hours daily or every alternate day.",
            "critical_stages": "Flowering, Fruit setting, and Fruit bulking stages"
        },
        "harvest": {
            "harvest_indicators": "Color shifts from green to pink/red; fruit yields slightly to gentle touch.",
            "harvest_time": "Morning hours to keep freshness",
            "harvest_method": "Hand plucking with calyx intact, twisting gently to detach.",
            "post_harvest_handling": "Sort by size/ripeness; pack in ventilated crates. Do not refrigerate fresh tomatoes (causes loss of flavor).",
            "storage_temp": "12°C - 15°C",
            "shelf_life": "7 - 14 days"
        },
        "stages": [
            {"name": "Germination", "description": "Seed absorbs moisture, sprouts roots, and shoots emerge.", "duration_days": 7},
            {"name": "Seedling", "description": "Development of true leaves and root consolidation in nursery.", "duration_days": 20},
            {"name": "Vegetative Growth", "description": "Rapid stem elongation, branching, and leaf canopy production.", "duration_days": 25},
            {"name": "Flowering & Fruit Set", "description": "Yellow flowers open and self-pollinate to form baby green fruits.", "duration_days": 20}
        ],
        "images": [
            {"category": "Fruit", "url": "https://images.unsplash.com/photo-1595855759920-86582396756a?auto=format&fit=crop&q=80&w=800&h=800"},
            {"category": "Leaf", "url": "https://images.unsplash.com/photo-1592982537447-7440770cbfc9?auto=format&fit=crop&q=80&w=800&h=800"}
        ]
    },
    {
        "common_name": "Rose",
        "botanical_name": "Rosa rubiginosa",
        "synonyms": "Rosa eglanteria, Sweetbriar Rose",
        "local_names": "Gulab, Rose",
        "family": "Rosaceae",
        "genus": "Rosa",
        "species": "rubiginosa",
        "plant_authority": "L.",
        "overview": "The rose is a woody perennial flowering plant of the genus Rosa, in the family Rosaceae. They form a group of plants that can be erect shrubs, climbing, or trailing, with stems that are often armed with sharp prickles.",
        "morphology": "Woody shrub with pinnate leaves, prickles on stems, and multi-petaled fragrant flowers.",
        "leaf_desc": "Pinnate, alternate, usually with 5 to 9 serrated leaflets; sweet apple-like scent in rubiginosa.",
        "flower_desc": "Showy flowers, varying from red, pink, yellow, to white, with numerous stamens and petals.",
        "fruit_desc": "Globose, red-orange berry-like structure called a rose hip.",
        "seed_desc": "Hard achenes enclosed within the fleshy rose hip.",
        "stem_desc": "Woody, armed with stiff, hooked thorns or prickles.",
        "root_desc": "Deep, woody taproot system with wide-spreading lateral roots.",
        "growth_habit": "Shrubby, climbing, or creeping",
        "life_cycle": "Perennial",
        "average_height": "1.0 - 4.0 m",
        "average_width": "1.0 - 2.0 m",
        "lifespan": "10 - 20 years",
        "category": "Ornamental",
        "commercial_uses": "Floriculture, rose oil, perfumes, herbal teas, cosmetics, rose water",
        "medicinal_uses": "Rose hips are extremely rich in vitamin C; rose water is used for anti-inflammatory skin toning.",
        "industrial_uses": "Perfumery, cosmetics, pharmaceuticals",
        "food_uses": "Rose syrup, gulkand, herbal tea flavorings",
        "toxicity": "Thorns cause mechanical injuries. Hips are safe, but seeds contain fine irritating hairs.",
        "conservation_status": "Least Concern",
        "classification": {
            "kingdom": "Plantae",
            "division": "Tracheophyta",
            "class_name": "Magnoliopsida",
            "order_name": "Rosales",
            "taxonomy_hierarchy": "Plantae -> Tracheophyta -> Magnoliopsida -> Rosales -> Rosaceae -> Rosa -> Rosa rubiginosa"
        },
        "varieties": [
            {"name": "Hybrid Tea", "variety_type": "Large single flowers", "growing_period": "Year-round", "yield_potential": "15-20 stems/plant/year"},
            {"name": "Floribunda", "variety_type": "Cluster flowering", "growing_period": "Year-round", "yield_potential": "25-35 stems/plant/year"}
        ],
        "climate": {
            "native_region": "Europe and Western Asia",
            "countries_grown": "India, Netherlands, Kenya, Ecuador, Colombia",
            "climatic_zones": "Temperate, Subtropical, Mild Tropical",
            "suitable_altitude": "500 - 2400 m",
            "rainfall_requirement": "800 - 1200 mm",
            "temperature_requirement": "15°C - 28°C",
            "humidity_requirement": "55% - 65%"
        },
        "soil": {
            "preferred_soil": "Rich, Organic clay loam or sandy loam",
            "soil_ph_range": "6.0 - 6.5",
            "drainage": "Perfectly drained",
            "organic_matter": "Very High (3-5%)",
            "fertility": "High",
            "texture": "Medium-textured loam"
        },
        "diseases": [
            {
                "name": "Black Spot",
                "pathogen_name": "Diplocarpon rosae",
                "disease_type": "Fungal",
                "risk_level": "Medium",
                "economic_impact": "Devastates aesthetic value of florist roses and reduces plant vigor via severe defoliation.",
                "symptoms": {
                    "early_symptoms": "Fringed circular black spots on upper leaf surfaces, starting on lower branches.",
                    "late_symptoms": "Leaves turn entirely yellow and drop off, leaving bare canes and weak blooms.",
                    "affected_parts": "Leaves, Canes, Petals"
                },
                "treatment": {
                    "immediate_treatment": "Prune infected leaves. Spray chlorothalonil or copper soap.",
                    "organic_treatment": "Spray neem oil or sulfur dust. Apply compost tea to soil to boost immunity.",
                    "chemical_treatment": "Use Tebuconazole, Propiconazole, or Triforine sprays.",
                    "biological_control": "Apply Bacillus subtilis formulations to leaves.",
                    "recommended_fungicides": "Bayer Advanced Disease Control, Daconil, Funginex",
                    "recommended_organic_solutions": "Copper Fungicide, Sulfur Dust, Neem Oil",
                    "dosage": "1.5ml of systemic fungicide per Liter of water",
                    "application_frequency": "Every 10-14 days during wet summer months",
                    "safety_precautions": "Avoid spraying during hot midday sun; wear safety glasses.",
                    "recovery_time": "14 - 21 days"
                }
            },
            {
                "name": "Powdery Mildew",
                "pathogen_name": "Podosphaera pannosa",
                "disease_type": "Fungal",
                "risk_level": "Medium",
                "economic_impact": "Causes leaf distortion and reduces flower quality, affecting commercial values by up to 40%.",
                "symptoms": {
                    "early_symptoms": "Slight puckering of leaves with white powdery spots on young stems and leaf undersides.",
                    "late_symptoms": "Thick white felt-like coating covering leaves, buds, and stems, preventing flower opening.",
                    "affected_parts": "Leaves, Flower Buds, Stems"
                },
                "treatment": {
                    "immediate_treatment": "Increase spacing, prune dense foliage. Spray potassium bicarbonate or sulfur.",
                    "organic_treatment": "Spray baking soda solution (3g baking soda + 1ml liquid soap in 1L water) weekly.",
                    "chemical_treatment": "Apply Triadimefon or Myclobutanil.",
                    "biological_control": "Foliar application of Ampelomyces quisqualis hyperparasite.",
                    "recommended_fungicides": "Spectracide Immunox, Sulfur spray",
                    "recommended_organic_solutions": "Potassium Bicarbonate, Neem Oil, Diluted Milk spray (1:9 ratio)",
                    "dosage": "3 grams Potassium Bicarbonate per Liter",
                    "application_frequency": "Every 7 days until clear",
                    "safety_precautions": "Apply early morning; check for leaf burn.",
                    "recovery_time": "10 - 12 days"
                }
            }
        ],
        "pests": [
            {
                "name": "Rose Aphids",
                "scientific_name": "Macrosiphum rosae",
                "identification": "Small (2-3mm) soft-bodied green or pink insects feeding in large colonies on tender shoots.",
                "damage_symptoms": "Curled leaves, stunted buds, sticky honeydew attracting ants and sooty mold.",
                "lifecycle": "Nymphs mature in 7 days; reproduce parthenogenetically in spring.",
                "organic_control": "High-pressure water spray, insecticidal soaps, encouraging ladybug larvae.",
                "chemical_control": "Imidacloprid soil drench or Malathion foliar spray.",
                "biological_control": "Ladybugs (Coccinella septempunctata), Lacewing larvae.",
                "economic_threshold": "10 aphids per flower bud"
            }
        ],
        "deficiencies": [
            {
                "nutrient_name": "Iron",
                "symptoms": "Interveinal chlorosis: leaves turn pale yellow while the veins remain dark green. Appears first on young leaves.",
                "correction_methods": "Apply chelated iron compound as a foliar spray or soil drench. Lower soil pH.",
                "recommended_fertilizers": "Iron Chelates (EDDHA or EDTA), Ferrous Sulphate"
            }
        ],
        "fertilizer": {
            "organic_fertilizers": "Bone meal, fish emulsion, alfalfa meal, neem cake",
            "chemical_fertilizers": "Specialized Rose mix NPK 8-12-4, Magnesium sulfate (Epsom salts)",
            "npk_ratio": "8-12-4 or 15-15-15",
            "application_timing": "Once at spring pruning, then monthly during the blooming season",
            "application_qty": "100g Rose food per bush, 20g Epsom salt per bush"
        },
        "irrigation": {
            "water_requirement": "Moderate",
            "daily_water_need": "2 - 3 Liters per bush",
            "weekly_water_need": "12 - 18 Liters per bush",
            "drip_recommendation": "Drip irrigation at root level. Avoid overhead sprinklers which cause black spot.",
            "critical_stages": "Bud formation and hot dry summer periods"
        },
        "harvest": {
            "harvest_indicators": "Petals start to unfurl; sepals are fully folded back.",
            "harvest_time": "Early morning before temperature rises",
            "harvest_method": "Cut at a 45-degree angle above a 5-leaflet leaf node using sharp bypass pruners.",
            "post_harvest_handling": "Place cut stems immediately into clean water with flower preservative; cool immediately.",
            "storage_temp": "2°C - 4°C",
            "shelf_life": "5 - 10 days in vase"
        },
        "stages": [
            {"name": "Dormancy & Pruning", "description": "Winter rest period where leaves fall and hard pruning is executed.", "duration_days": 60},
            {"name": "Bud Break & Foliage", "description": "New red shoots and green foliage emerge from cane nodes.", "duration_days": 30},
            {"name": "Flowering", "description": "Buds expand and bloom into fragrant blossoms.", "duration_days": 45}
        ],
        "images": [
            {"category": "Flower", "url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&q=80&w=800&h=800"}
        ]
    },
    {
        "common_name": "Rice",
        "botanical_name": "Oryza sativa",
        "synonyms": "Oryza communissima, Paddy",
        "local_names": "Dhan, Chawal, Paddy, Rice",
        "family": "Poaceae",
        "genus": "Oryza",
        "species": "sativa",
        "plant_authority": "L.",
        "overview": "Rice is the seed of the grass species Oryza sativa. As a cereal grain, it is the most widely consumed staple food for a large part of the world's human population, especially in Asia.",
        "morphology": "Annual grass with round hollow jointed stems, flat leaves, and terminal panicle inflorescence.",
        "leaf_desc": "Long, flat, linear leaves with parallel veins and a prominent ligule.",
        "flower_desc": "Panicle bearing spikelets with individual florets containing 6 stamens.",
        "fruit_desc": "Caryopsis (grain) enclosed by the hull (lemma and palea).",
        "seed_desc": "Starchy grain, elongated or round, covered by protective husk layers.",
        "stem_desc": "Culm, hollow, jointed with nodes and internodes, growing in tillers.",
        "root_desc": "Fibrous, adventitious root system forming a dense mat in waterlogged soil.",
        "growth_habit": "Graminoid (tussock forming)",
        "life_cycle": "Annual",
        "average_height": "0.8 - 1.8 m",
        "average_width": "0.2 - 0.4 m",
        "lifespan": "4 - 6 months",
        "category": "Cereal Grain",
        "commercial_uses": "Human food staple, rice bran oil, animal fodder, straw for packaging and paper, brewing (sake)",
        "medicinal_uses": "Rice water is used to treat diarrhea; brown rice supports digestion and glucose control.",
        "industrial_uses": "Starch manufacturing, ethanol production, hull fuel ash",
        "food_uses": "Boiled rice, flour, rice cakes, parboiled grains",
        "toxicity": "Raw rice husks can cause mechanical irritation; moldy rice may contain aflatoxins.",
        "conservation_status": "Least Concern",
        "classification": {
            "kingdom": "Plantae",
            "division": "Tracheophyta",
            "class_name": "Liliopsida",
            "order_name": "Poales",
            "taxonomy_hierarchy": "Plantae -> Tracheophyta -> Liliopsida -> Poales -> Poaceae -> Oryza -> Oryza sativa"
        },
        "varieties": [
            {"name": "Basmati", "variety_type": "Long Grain Aromatic", "growing_period": "135 days", "yield_potential": "1.8-2.2 tons/acre"},
            {"name": "Sonamasuri", "variety_type": "Medium Grain Non-Aromatic", "growing_period": "120 days", "yield_potential": "2.8-3.2 tons/acre"}
        ],
        "climate": {
            "native_region": "Southeast Asia and India",
            "countries_grown": "China, India, Indonesia, Vietnam, Thailand, Bangladesh",
            "climatic_zones": "Tropical, Subtropical, Warm Temperate",
            "suitable_altitude": "0 - 1500 m",
            "rainfall_requirement": "1200 - 2000 mm",
            "temperature_requirement": "20°C - 37°C",
            "humidity_requirement": "70% - 90%"
        },
        "soil": {
            "preferred_soil": "Heavy Clayey Loam or Silt Clay",
            "soil_ph_range": "5.5 - 6.5",
            "drainage": "Poorly drained (benefits from water retention)",
            "organic_matter": "Moderate (1.5-2.5%)",
            "fertility": "High",
            "texture": "Fine, clay-rich soil"
        },
        "diseases": [
            {
                "name": "Rice Blast",
                "pathogen_name": "Pyricularia oryzae",
                "disease_type": "Fungal",
                "risk_level": "High",
                "economic_impact": "One of the most destructive diseases, capable of causing up to 100% crop loss in favorable climates.",
                "symptoms": {
                    "early_symptoms": "Spindle-shaped or diamond-shaped lesions on leaves with gray centers and brown borders.",
                    "late_symptoms": "Neck rot (broken panicle neck), leading to empty white heads with no grain filling.",
                    "affected_parts": "Leaves, Nodes, Panicles, Sheaths"
                },
                "treatment": {
                    "immediate_treatment": "Apply tricyclazole spray. Maintain standing water levels.",
                    "organic_treatment": "Spray pseudomonas fluorescens liquid formulation. Avoid heavy nitrogen fertilizer.",
                    "chemical_treatment": "Use Tricyclazole 75% WP (0.6g/L) or Kitazin.",
                    "biological_control": "Deploy antagonistic bacteria like Bacillus subtilis.",
                    "recommended_fungicides": "Tricyclazole, Isoprothiolane, Kasugamycin",
                    "recommended_organic_solutions": "Pseudomonas spray, Neem seed kernel extract",
                    "dosage": "0.6 grams Tricyclazole per Liter",
                    "application_frequency": "At tillering and booting stages, if symptoms appear",
                    "safety_precautions": "Avoid direct contact; ensure 14-day safety window before harvesting.",
                    "recovery_time": "12 - 15 days"
                }
            }
        ],
        "pests": [
            {
                "name": "Yellow Stem Borer",
                "scientific_name": "Scirpophaga incertulas",
                "identification": "Yellowish-white moths whose larvae bore into the rice culm.",
                "damage_symptoms": "Dead hearts (withered central leaf whorl) in vegetative stage, and Whiteheads (empty pale panicles) during flowering.",
                "lifecycle": "Egg to adult in 40-50 days; larvae overwinter in stubble.",
                "organic_control": "Clipping leaf tips before transplanting to remove eggs, using light/pheromone traps.",
                "chemical_control": "Apply Cartap Hydrochloride 4G granules in standing water.",
                "biological_control": "Release of Trichogramma japonicum egg parasitoid wasps.",
                "economic_threshold": "10% dead hearts or 2 moths/sq meter"
            }
        ],
        "deficiencies": [
            {
                "nutrient_name": "Zinc",
                "symptoms": "Khaira Disease: Reddish-brown spots and streaks on lower leaves, starting 2-4 weeks after transplanting. Stunted growth.",
                "correction_methods": "Apply zinc sulfate to soil or spray dissolved zinc sulfate + lime on leaves.",
                "recommended_fertilizers": "Zinc Sulphate Heptahydrate (21% Zn), Zinc EDTA"
            }
        ],
        "fertilizer": {
            "organic_fertilizers": "Sesbania green manure, blue-green algae, Azolla",
            "chemical_fertilizers": "NPK 120-60-60 kg/ha, split Nitrogen in 3 doses",
            "npk_ratio": "120-60-60",
            "application_timing": "Basal NPK, urea top-dressing at active tillering and panicle initiation",
            "application_qty": "260kg Urea, 375kg Single Superphosphate, 100kg Muriate of Potash per hectare"
        },
        "irrigation": {
            "water_requirement": "Very High",
            "daily_water_need": "15 - 20 Liters per sq.m.",
            "weekly_water_need": "100 - 140 Liters per sq.m.",
            "drip_recommendation": "Not recommended for traditional paddies. If using aerobic rice, use drip lines spaced 40cm, running daily.",
            "critical_stages": "Transplanting, active tillering, panicle initiation, and flowering stages"
        },
        "harvest": {
            "harvest_indicators": "Grains turn yellow/golden brown; grain moisture drops to 20-22%.",
            "harvest_time": "Daytime, clear weather",
            "harvest_method": "Sickle harvesting by hand, or mechanical combine harvester.",
            "post_harvest_handling": "Thresh immediately; dry grain down to 14% moisture to prevent mold and grain breakage during milling.",
            "storage_temp": "15°C - 25°C",
            "shelf_life": "1 - 2 years (stored dry)"
        },
        "stages": [
            {"name": "Nursery Seedling", "description": "Seeds are sprouted and grown closely in a wet bed for 21-25 days.", "duration_days": 25},
            {"name": "Tillering Stage", "description": "Seedlings transplanted; side shoots (tillers) emerge and multiply.", "duration_days": 35},
            {"name": "Panicle Initiation", "description": "The embryonic flower head begins to develop inside the main stem.", "duration_days": 25},
            {"name": "Grain Filling", "description": "Flowers are pollinated and the milky starch accumulates inside grain hulls.", "duration_days": 30}
        ],
        "images": [
            {"category": "Entire", "url": "https://images.unsplash.com/photo-1543157148-f819d161763f?auto=format&fit=crop&q=80&w=800&h=800"}
        ]
    },
    {
        "common_name": "Wheat",
        "botanical_name": "Triticum aestivum",
        "synonyms": "Triticum vulgare, Bread Wheat",
        "local_names": "Gehun, Wheat, Kanak",
        "family": "Poaceae",
        "genus": "Triticum",
        "species": "aestivum",
        "plant_authority": "L.",
        "overview": "Wheat is a grass widely cultivated for its seed, a cereal grain which is a worldwide staple food. The taxonomic group includes multiple species, with Triticum aestivum being the most common.",
        "morphology": "Erect annual grass with hollow tillering stems, flat leaf blades, and terminal compact spike inflorescence.",
        "leaf_desc": "Flat, linear, parallel-veined leaf blades with smooth sheaths.",
        "flower_desc": "Terminal spike containing spikelets with 2-5 florets inside glumes.",
        "fruit_desc": "Caryopsis (wheat berry), oval or ellipsoidal grain with a longitudinal groove.",
        "seed_desc": "Starchy endosperm wrapped in bran, containing a nutrient-rich embryo.",
        "stem_desc": "Hollow jointed culm, carrying leaves and ending in the grain head.",
        "root_desc": "Seminal roots active early, replaced by crown roots forming a dense fibrous root system.",
        "growth_habit": "Graminoid (tussock forming)",
        "life_cycle": "Annual",
        "average_height": "0.6 - 1.2 m",
        "average_width": "0.15 - 0.3 m",
        "lifespan": "5 - 6 months",
        "category": "Cereal Grain",
        "commercial_uses": "Flour for bread, pasta, noodles, cakes; wheat germ oil, straw for livestock bedding, brewing",
        "medicinal_uses": "Wheat germ is rich in vitamin E; wheat bran provides dietary fiber for colon health.",
        "industrial_uses": "Starch pastes, adhesives, industrial alcohol, strawboard production",
        "food_uses": "Bread, chapati, couscous, semolina, breakfast cereals",
        "toxicity": "Gluten content causes celiac disease in sensitive individuals; grain dust can cause worker asthma.",
        "conservation_status": "Least Concern",
        "classification": {
            "kingdom": "Plantae",
            "division": "Tracheophyta",
            "class_name": "Liliopsida",
            "order_name": "Poales",
            "taxonomy_hierarchy": "Plantae -> Tracheophyta -> Liliopsida -> Poales -> Poaceae -> Triticum -> Triticum aestivum"
        },
        "varieties": [
            {"name": "HD-2967", "variety_type": "High Yielding Rust Resistant", "growing_period": "140 days", "yield_potential": "2.2-2.5 tons/acre"},
            {"name": "Sharbati", "variety_type": "Premium Durum/High Gluten", "growing_period": "130 days", "yield_potential": "1.6-1.8 tons/acre"}
        ],
        "climate": {
            "native_region": "Fertile Crescent (Middle East)",
            "countries_grown": "China, India, Russia, USA, Canada, France",
            "climatic_zones": "Temperate, Cool Subtropical",
            "suitable_altitude": "300 - 3000 m",
            "rainfall_requirement": "400 - 600 mm",
            "temperature_requirement": "10°C - 25°C",
            "humidity_requirement": "40% - 60%"
        },
        "soil": {
            "preferred_soil": "Loam to Clayey Loam",
            "soil_ph_range": "6.0 - 7.5",
            "drainage": "Well-drained",
            "organic_matter": "Moderate (1.5-2.0%)",
            "fertility": "Moderate to High",
            "texture": "Medium to heavy clay loam"
        },
        "diseases": [
            {
                "name": "Rust",
                "pathogen_name": "Puccinia graminis",
                "disease_type": "Fungal",
                "risk_level": "High",
                "economic_impact": "Can turn a healthy crop into a tangled mass of broken stems just weeks before harvest, causing 50-70% losses.",
                "symptoms": {
                    "early_symptoms": "Elongated reddish-orange blister-like pustules on leaves, leaf sheaths, and stems.",
                    "late_symptoms": "Pustules turn black as they produce winter spores; stems become dry, brittle, and lodge.",
                    "affected_parts": "Leaves, Stems, Leaf Sheaths"
                },
                "treatment": {
                    "immediate_treatment": "Apply Propiconazole or Tebuconazole fungicide spray.",
                    "organic_treatment": "Spray sulfur powder preventatively. Grow rust-resistant varieties.",
                    "chemical_treatment": "Foliar spray of Propiconazole 25% EC (1ml/L).",
                    "biological_control": "Use Trichoderma viride seed inoculants.",
                    "recommended_fungicides": "Tilt (Propiconazole), Folicur (Tebuconazole)",
                    "recommended_organic_solutions": "Wettable Sulfur, Trichoderma",
                    "dosage": "1.0 ml per Liter of water",
                    "application_frequency": "Once on initial symptom detection, repeat after 15 days if rust pressure continues",
                    "safety_precautions": "Do not enter field for 24 hours after chemical spraying.",
                    "recovery_time": "10 - 12 days"
                }
            }
        ],
        "pests": [
            {
                "name": "Wheat Aphids",
                "scientific_name": "Schizaphis graminum",
                "identification": "Small green bugs sucking sap from leaves and developing spikelets.",
                "damage_symptoms": "Yellowing leaves, sticky honeydew, shriveled grain kernels.",
                "lifecycle": "Reproduce parthenogenetically; lifecycle completes in 8-12 days in warm spring.",
                "organic_control": "Neem oil sprays, conservation of natural ladybug predators.",
                "chemical_control": "Apply Dimethoate or Oxydemeton-methyl insecticide.",
                "biological_control": "Parasitic wasps (Lysiphlebus testaceipes).",
                "economic_threshold": "5 aphids per spike"
            }
        ],
        "deficiencies": [
            {
                "nutrient_name": "Nitrogen",
                "symptoms": "V-shaped yellowing starting at leaf tip on older leaves. Reduced tillering and thin heads.",
                "correction_methods": "Top dress with Urea fertilizer before irrigation.",
                "recommended_fertilizers": "Urea, Ammonium Nitrate"
            }
        ],
        "fertilizer": {
            "organic_fertilizers": "Vermicompost, sheep manure",
            "chemical_fertilizers": "NPK 12:32:16 at sowing, Urea at first and second irrigations",
            "npk_ratio": "120-60-40 kg/ha",
            "application_timing": "Full dose of P and K + half N at sowing; remaining N split at Crown Root Initiation and Jointing stages",
            "application_qty": "120kg N, 60kg P2O5, 40kg K2O per hectare"
        },
        "irrigation": {
            "water_requirement": "Moderate",
            "daily_water_need": "4 - 6 mm depth",
            "weekly_water_need": "25 - 40 mm depth equivalent",
            "drip_recommendation": "Use sub-surface drip irrigation with lines at 20-30cm depth. Irrigation intervals of 3-4 days.",
            "critical_stages": "Crown Root Initiation (21 days), Jointing, Booting, Flowering, Milking, and Dough stages"
        },
        "harvest": {
            "harvest_indicators": "Stems and spikes turn dry, straw-colored, and brittle; grains cannot be dented by fingernails.",
            "harvest_time": "Dry sunny afternoon to ensure low moisture",
            "harvest_method": "Hand harvesting with sickles or combine harvesting.",
            "post_harvest_handling": "Thresh and clean; dry grain to below 12% moisture for safe bin storage.",
            "storage_temp": "15°C - 20°C",
            "shelf_life": "2 - 3 years (stored dry and insect-free)"
        },
        "stages": [
            {"name": "Germination & Emergence", "description": "Sown seeds sprout roots and coleoptile emerges above soil.", "duration_days": 10},
            {"name": "Crown Root Initiation", "description": "Secondary root system develops at the crown zone; critical stage.", "duration_days": 15},
            {"name": "Tillering", "description": "Side shoots (tillers) branch out from the crown base.", "duration_days": 30},
            {"name": "Booting & Heading", "description": "Flag leaf sheath swells with spike; spike emerges.", "duration_days": 25}
        ],
        "images": [
            {"category": "Entire", "url": "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?auto=format&fit=crop&q=80&w=800&h=800"}
        ]
    }
]

def seed_botanical_encyclopedia(db: Session):
    print("🌱 Commencing Botanical Database Seeding...")
    
    # Iterate through crops and build normalized rows
    for crop in SEED_CROPS:
        # Check if plant already exists
        existing_plant = db.query(Plant).filter(Plant.common_name == crop["common_name"]).first()
        if existing_plant:
            print(f"   [Skip] Crop '{crop['common_name']}' already seeded in DB.")
            continue
            
        # 1. Family
        db_family = db.query(Family).filter(Family.name == crop["family"]).first()
        if not db_family:
            db_family = Family(name=crop["family"], description=f"Botanical family group of {crop['family']}")
            db.add(db_family)
            db.commit()
            db.refresh(db_family)
            
        # 2. Genus
        db_genus = db.query(Genus).filter(Genus.name == crop["genus"]).first()
        if not db_genus:
            db_genus = Genus(name=crop["genus"], description=f"Botanical genus group of {crop['genus']}")
            db.add(db_genus)
            db.commit()
            db.refresh(db_genus)
            
        # 3. SpeciesRecord
        db_spec = db.query(SpeciesRecord).filter(SpeciesRecord.name == crop["species"]).first()
        if not db_spec:
            db_spec = SpeciesRecord(name=crop["species"], description=f"Specific species identifier {crop['species']}")
            db.add(db_spec)
            db.commit()
            db.refresh(db_spec)
            
        # 4. Plant
        db_plant = Plant(
            common_name=crop["common_name"],
            botanical_name=crop["botanical_name"],
            synonyms=crop["synonyms"],
            local_names=crop["local_names"],
            family_id=db_family.id,
            genus_id=db_genus.id,
            species_id=db_spec.id,
            plant_authority=crop["plant_authority"],
            overview=crop["overview"],
            morphology=crop["morphology"],
            leaf_desc=crop["leaf_desc"],
            flower_desc=crop["flower_desc"],
            fruit_desc=crop["fruit_desc"],
            seed_desc=crop["seed_desc"],
            stem_desc=crop["stem_desc"],
            root_desc=crop["root_desc"],
            growth_habit=crop["growth_habit"],
            life_cycle=crop["life_cycle"],
            average_height=crop["average_height"],
            average_width=crop["average_width"],
            lifespan=crop["lifespan"],
            category=crop["category"],
            commercial_uses=crop["commercial_uses"],
            medicinal_uses=crop["medicinal_uses"],
            industrial_uses=crop["industrial_uses"],
            food_uses=crop["food_uses"],
            toxicity=crop["toxicity"],
            conservation_status=crop["conservation_status"]
        )
        db.add(db_plant)
        db.commit()
        db.refresh(db_plant)
        
        # 5. Botanical Classification
        cls_data = crop["classification"]
        db_classification = BotanicalClassification(
            plant_id=db_plant.id,
            kingdom=cls_data["kingdom"],
            division=cls_data["division"],
            class_name=cls_data["class_name"],
            order_name=cls_data["order_name"],
            taxonomy_hierarchy=cls_data["taxonomy_hierarchy"]
        )
        db.add(db_classification)
        
        # 6. Varieties
        for var in crop["varieties"]:
            db_var = Variety(
                plant_id=db_plant.id,
                name=var["name"],
                variety_type=var["variety_type"],
                growing_period=var["growing_period"],
                yield_potential=var["yield_potential"]
            )
            db.add(db_var)
            
        # 7. Climate Requirement
        clim = crop["climate"]
        db_climate = ClimateRequirement(
            plant_id=db_plant.id,
            native_region=clim["native_region"],
            countries_grown=clim["countries_grown"],
            climatic_zones=clim["climatic_zones"],
            suitable_altitude=clim["suitable_altitude"],
            rainfall_requirement=clim["rainfall_requirement"],
            temperature_requirement=clim["temperature_requirement"],
            humidity_requirement=clim["humidity_requirement"]
        )
        db.add(db_climate)
        
        # 8. Soil Requirement
        s_data = crop["soil"]
        db_soil = SoilRequirement(
            plant_id=db_plant.id,
            preferred_soil=s_data["preferred_soil"],
            soil_ph_range=s_data["soil_ph_range"],
            drainage=s_data["drainage"],
            organic_matter=s_data["organic_matter"],
            fertility=s_data["fertility"],
            texture=s_data["texture"]
        )
        db.add(db_soil)
        
        # 9. Fertilizer Recommendation
        f_data = crop["fertilizer"]
        db_fert = FertilizerRecommendation(
            plant_id=db_plant.id,
            organic_fertilizers=f_data["organic_fertilizers"],
            chemical_fertilizers=f_data["chemical_fertilizers"],
            npk_ratio=f_data["npk_ratio"],
            application_timing=f_data["application_timing"],
            application_qty=f_data["application_qty"]
        )
        db.add(db_fert)
        
        # 10. Irrigation Schedule
        ir_data = crop["irrigation"]
        db_irr = IrrigationSchedule(
            plant_id=db_plant.id,
            water_requirement=ir_data["water_requirement"],
            daily_water_need=ir_data["daily_water_need"],
            weekly_water_need=ir_data["weekly_water_need"],
            drip_recommendation=ir_data["drip_recommendation"],
            critical_stages=ir_data["critical_stages"]
        )
        db.add(db_irr)
        
        # 11. Harvest Information
        har_data = crop["harvest"]
        db_har = HarvestInformation(
            plant_id=db_plant.id,
            harvest_indicators=har_data["harvest_indicators"],
            harvest_time=har_data["harvest_time"],
            harvest_method=har_data["harvest_method"],
            post_harvest_handling=har_data["post_harvest_handling"],
            storage_temp=har_data["storage_temp"],
            shelf_life=har_data["shelf_life"]
        )
        db.add(db_har)
        
        # 12. Growth Stages
        for stage in crop["stages"]:
            db_stage = GrowthStage(
                plant_id=db_plant.id,
                name=stage["name"],
                description=stage["description"],
                duration_days=stage["duration_days"]
            )
            db.add(db_stage)
            
        # 13. Plant Images
        for img in crop["images"]:
            db_img = PlantImage(
                plant_id=db_plant.id,
                category=img["category"],
                url=img["url"]
            )
            db.add(db_img)
            
        # 14-16. Diseases, Symptoms, and Treatments
        for dis in crop["diseases"]:
            db_dis = Disease(
                plant_id=db_plant.id,
                name=dis["name"],
                pathogen_name=dis["pathogen_name"],
                disease_type=dis["disease_type"],
                risk_level=dis["risk_level"],
                economic_impact=dis["economic_impact"]
            )
            db.add(db_dis)
            db.commit()
            db.refresh(db_dis)
            
            # Disease Symptoms
            sym = dis["symptoms"]
            db_sym = DiseaseSymptom(
                disease_id=db_dis.id,
                early_symptoms=sym["early_symptoms"],
                late_symptoms=sym["late_symptoms"],
                affected_parts=sym["affected_parts"]
            )
            db.add(db_sym)
            
            # Disease Treatment
            tr = dis["treatment"]
            db_treat = DiseaseTreatment(
                disease_id=db_dis.id,
                immediate_treatment=tr["immediate_treatment"],
                organic_treatment=tr["organic_treatment"],
                chemical_treatment=tr["chemical_treatment"],
                biological_control=tr["biological_control"],
                recommended_fungicides=tr["recommended_fungicides"],
                recommended_organic_solutions=tr["recommended_organic_solutions"],
                dosage=tr["dosage"],
                application_frequency=tr["application_frequency"],
                safety_precautions=tr["safety_precautions"],
                recovery_time=tr["recovery_time"]
            )
            db.add(db_treat)
            
        # 17. Pests
        for pst in crop["pests"]:
            db_pest = Pest(
                plant_id=db_plant.id,
                name=pst["name"],
                scientific_name=pst["scientific_name"],
                identification=pst["identification"],
                damage_symptoms=pst["damage_symptoms"],
                lifecycle=pst["lifecycle"],
                organic_control=pst["organic_control"],
                chemical_control=pst["chemical_control"],
                biological_control=pst["biological_control"],
                economic_threshold=pst["economic_threshold"]
            )
            db.add(db_pest)
            
        # 18. Deficiencies
        for df in crop["deficiencies"]:
            db_df = NutrientDeficiency(
                plant_id=db_plant.id,
                nutrient_name=df["nutrient_name"],
                symptoms=df["symptoms"],
                correction_methods=df["correction_methods"],
                recommended_fertilizers=df["recommended_fertilizers"]
            )
            db.add(db_df)
            
        db.commit()
        print(f"   [Done] Seeded crop: '{crop['common_name']}'")
        
    print("✅ Botanical Database Seeding Completed successfully!")
