"""
nutrients_db.py
Complete Plant Nutrient Database — All 17 Essential Plant Nutrients
Deficiency symptoms, toxicity, soil interactions, and crop-specific recommendations
Sources: FAO Fertilizer Use Recommendations, IPNI, IPI, Fertilizer Association guides
"""

# ─────────────────────────────────────────────────────────────────────────────
# 17 ESSENTIAL PLANT NUTRIENTS
# ─────────────────────────────────────────────────────────────────────────────

ESSENTIAL_NUTRIENTS = {

    # ═══════════════════════════════════════════════════════════════════════
    # MACRONUTRIENTS — FROM ATMOSPHERE & WATER
    # ═══════════════════════════════════════════════════════════════════════
    "Carbon": {
        "symbol": "C", "element_type": "Non-mineral macronutrient", "source": "CO2 from atmosphere",
        "functions": ["Primary component of all organic molecules", "Photosynthesis (CO2 fixation)", "Structural component of plant body"],
        "deficiency": {"symptoms": "Not applicable — plant cannot grow without C", "visual_signs": "None (CO2 naturally available)", "soil_ph_effects": "None"},
        "toxicity": {"symptoms": "Elevated CO2 (>1000ppm) can increase plant growth (CO2 fertilization effect)", "threshold": "Beneficial up to 1200ppm in controlled environments"},
        "forms_in_soil": "CO2 in soil air and water",
        "mobility_in_plant": "Highly mobile",
        "interactions": "Increases with temperature; CO2 enrichment increases yields",
        "fertilizer_sources": ["CO2 enrichment in greenhouses"],
        "critical_crops": "All crops"
    },
    "Hydrogen": {
        "symbol": "H", "element_type": "Non-mineral macronutrient", "source": "Water",
        "functions": ["Component of all organic molecules", "Water transport", "pH regulation in cells"],
        "deficiency": {"symptoms": "Drought stress (indirect)", "visual_signs": "Wilting, leaf roll", "soil_ph_effects": "None"},
        "toxicity": {"symptoms": "Waterlogging effects", "threshold": "Flooding conditions"},
        "forms_in_soil": "H2O", "mobility_in_plant": "High",
        "interactions": "Water uptake; stomatal function",
        "fertilizer_sources": ["Irrigation water"],
        "critical_crops": "All crops"
    },
    "Oxygen": {
        "symbol": "O", "element_type": "Non-mineral macronutrient", "source": "Atmosphere and Water",
        "functions": ["Aerobic respiration", "Component of all organic molecules", "Root aeration"],
        "deficiency": {"symptoms": "Waterlogging: anaerobic conditions cause root death", "visual_signs": "Yellow leaves, root browning, sulfide smell", "soil_ph_effects": "Waterlogging reduces O2"},
        "toxicity": {"symptoms": "Not applicable at normal atmospheric levels", "threshold": "Not applicable"},
        "forms_in_soil": "O2 in soil air", "mobility_in_plant": "High",
        "interactions": "Essential for aerobic root respiration",
        "fertilizer_sources": ["Drainage improvement", "Raised beds"],
        "critical_crops": "All crops, especially in waterlogged areas"
    },

    # ═══════════════════════════════════════════════════════════════════════
    # PRIMARY MACRONUTRIENTS
    # ═══════════════════════════════════════════════════════════════════════
    "Nitrogen": {
        "symbol": "N", "element_type": "Primary Macronutrient",
        "plant_content_range": "1.5-4% dry weight",
        "source": "Soil organic matter mineralization, fertilizers, biological fixation",
        "functions": [
            "Component of amino acids, proteins, enzymes",
            "Chlorophyll synthesis (green color)",
            "Nucleic acid component (DNA, RNA)",
            "Promotes vegetative growth",
            "Enzyme activation"
        ],
        "deficiency": {
            "name": "Nitrogen Deficiency (Chlorosis)",
            "visual_signs": "Pale yellow-green color starting from older leaves (lower); progresses upward; stunted growth; thin spindly stems; early maturity",
            "affected_leaves": "Older/Lower leaves first (N is mobile, remobilized to young leaves)",
            "when_visible": "Commonly visible 2-4 weeks after deficiency begins",
            "soil_ph_effects": "Worse in acidic soils (mineralization slow), wet soils, sandy soils",
            "crop_specific": {
                "rice": "Pale yellow older leaves; reduced tillering; small, thin panicles",
                "maize": "Yellow stripe from tip of leaves (\"nitrogen streak\"), lower leaves yellow-brown",
                "wheat": "Pale green plants, purple tinting in some varieties, thin tillers",
                "tomato": "Light green plants, light purple tinting on stems"
            }
        },
        "toxicity": {
            "visual_signs": "Dark green, lodging, delayed maturity, reduced grain quality, excessive vegetative growth, hollow stems",
            "crop_effects": "Succulence, increased pest and disease susceptibility, pollen sterility",
            "threshold": "Varies widely by crop; depends on N form (ammonium vs nitrate)"
        },
        "forms_in_soil": ["Nitrate (NO3-) — mobile, leaches", "Ammonium (NH4+) — adsorbed on soil, less mobile", "Organic N — must mineralize first"],
        "mobility_in_plant": "Highly mobile — remobilized from old to young leaves",
        "optimal_soil_ph": "6.0-7.0 (best mineralization)",
        "interactions": {
            "positive": ["Phosphorus increases N uptake efficiency", "Sulfur needed for amino acid synthesis with N"],
            "negative": ["Excess K reduces N uptake", "Excess N reduces P and Zn uptake", "Waterlogging causes denitrification (N loss)"]
        },
        "fertilizer_sources": [
            "Urea (46% N) — most common",
            "Ammonium Nitrate (34% N)",
            "Ammonium Sulphate (21% N, 24% S)",
            "Calcium Ammonium Nitrate (25% N)",
            "DAP (18% N, 46% P2O5)",
            "Legume green manure (biological fixation)",
            "FYM (0.5-1.5% N)"
        ],
        "critical_growth_stage": "Vegetative stage, tillering (cereals), early fruit set",
        "soil_test_critical_level": "Available N > 50 kg/ha for cereals",
        "application_method": "Split application: 50% basal + 25% tillering + 25% PI for rice/wheat",
        "critical_crops": "Rice, Wheat, Maize, Vegetables, Cotton"
    },

    "Phosphorus": {
        "symbol": "P", "element_type": "Primary Macronutrient",
        "plant_content_range": "0.1-0.5% dry weight",
        "source": "Soil mineral weathering, organic matter, fertilizers",
        "functions": [
            "Root development and growth",
            "Energy transfer (ATP, ADP)",
            "Nucleic acid component (DNA, RNA)",
            "Cell membrane phospholipids",
            "Early plant establishment and tillering",
            "Seed and fruit development"
        ],
        "deficiency": {
            "name": "Phosphorus Deficiency (Purpling)",
            "visual_signs": "Dark green to purple/red color on older leaves and stems (anthocyanin accumulation); thin, weak roots; delayed maturity; small seeds",
            "affected_leaves": "Older leaves first (P is mobile)",
            "when_visible": "Early in season, especially in cold soils",
            "soil_ph_effects": "Severely limited availability in pH < 5.5 (Fe, Al fixation) and pH > 7.5 (Ca fixation); optimal pH 6.0-7.0",
            "crop_specific": {
                "maize": "Purple/red color on underside of leaves and stems — classic P deficiency sign",
                "tomato": "Purple undersides of leaves, bluish-green color, thin stems",
                "wheat": "Dark green to bluish, purple tinges, delayed maturity",
                "rice": "Thin, upright dark green or purple tinged leaves; reduced tillering"
            }
        },
        "toxicity": {
            "visual_signs": "Zinc and iron deficiency symptoms (P-induced micronutrient deficiency); stunted growth when soil P very high",
            "crop_effects": "Reduces Zn and Fe availability; root growth inhibited at very high P",
            "threshold": "Soil Olsen P > 40ppm can induce Zn deficiency in some crops"
        },
        "forms_in_soil": ["Orthophosphate ions (H2PO4-, HPO42-) — plant-available", "Organic P — must mineralize", "Fixed P (Al, Fe, Ca phosphates) — unavailable"],
        "mobility_in_plant": "Mobile — remobilized from old to young tissue",
        "optimal_soil_ph": "6.0-7.0",
        "interactions": {
            "positive": ["Mycorrhizal fungi dramatically increase P uptake", "Zinc must be balanced with P"],
            "negative": ["High P fixes Zn and Fe", "High Fe/Al soils fix P strongly (acid soils)", "Calcification in calcareous soils"]
        },
        "fertilizer_sources": [
            "DAP — Diammonium Phosphate (46% P2O5, 18% N)",
            "SSP — Single Super Phosphate (16% P2O5, 11% S, 20% Ca)",
            "TSP — Triple Super Phosphate (46% P2O5)",
            "Rock Phosphate (28-35% P2O5) — slow release in acid soils",
            "Ammonium Polyphosphate",
            "Bone meal (20-25% P2O5)"
        ],
        "critical_growth_stage": "Germination, early root development, flowering",
        "soil_test_critical_level": "Olsen P > 10-15 ppm for most crops",
        "application_method": "Basal application preferred; band application more efficient than broadcast",
        "critical_crops": "All crops; especially legumes, root crops, cereals"
    },

    "Potassium": {
        "symbol": "K", "element_type": "Primary Macronutrient",
        "plant_content_range": "1-4% dry weight",
        "source": "Soil minerals (feldspar, mica), organic matter, fertilizers",
        "functions": [
            "Stomatal regulation (drought resistance)",
            "Enzyme activation (>60 enzymes)",
            "Protein synthesis",
            "Disease resistance and strong cell walls",
            "Transport of sugars and nutrients in phloem",
            "Quality improvement (sugar content, fruit firmness, starch)"
        ],
        "deficiency": {
            "name": "Potassium Deficiency (Potash Starvation)",
            "visual_signs": "Brown scorching and curling of leaf tips and margins (leaf scorch/marginal necrosis) starting on older leaves; brown spots inside leaf margin; weak stems; lodging in cereals",
            "affected_leaves": "Older/Lower leaves first (K is mobile)",
            "when_visible": "Mid-season, especially in sandy soils or high-yield situations",
            "soil_ph_effects": "Reduced in waterlogged soils; depleted in sandy, leached soils; high Ca or Mg can reduce K uptake",
            "crop_specific": {
                "potato": "Marginal necrosis on older leaves; small irregular tubers; reduced specific gravity",
                "banana": "Marginal leaf scorch, orange-yellow margins; bent leaf midribs; reduced bunch weight",
                "tomato": "Marginal leaf burn, blossom end rot aggravated; poor fruit color",
                "rice": "Brown spots on older leaves from tip, leaves with rusty-dark brown margins"
            }
        },
        "toxicity": {
            "visual_signs": "Calcium and magnesium deficiency symptoms (K antagonism); salt effects in sandy soils",
            "crop_effects": "Reduces Ca and Mg uptake; blossom end rot in tomatoes; milk fever in animals consuming high-K crops",
            "threshold": "Soil K > 800 ppm can cause Mg deficiency in some crops"
        },
        "forms_in_soil": ["Exchangeable K (plant-available)", "Non-exchangeable K (in minerals — slowly available)", "Solution K (immediately available, small pool)"],
        "mobility_in_plant": "Highly mobile",
        "optimal_soil_ph": "6.0-7.5",
        "interactions": {
            "positive": ["Adequate K improves N use efficiency", "K improves water use efficiency", "K improves quality traits (Brix, firmness)"],
            "negative": ["High K reduces Ca and Mg uptake (antagonism)", "Na competes with K in salt-affected soils"]
        },
        "fertilizer_sources": [
            "Muriate of Potash / MOP (60% K2O) — most common",
            "Sulphate of Potash / SOP (50% K2O, 18% S) — premium for Cl-sensitive crops",
            "Potassium Nitrate (44% K2O, 13% N) — for fertigation",
            "Potassium Chloride (KCl)",
            "Wood ash (5-10% K2O) — organic source"
        ],
        "critical_growth_stage": "Fruiting, tuber development, grain filling",
        "soil_test_critical_level": "Exchangeable K > 120 kg/ha for most crops",
        "application_method": "Split application; avoid high rates at sowing (salt effect); good for top-dressing",
        "critical_crops": "Potato, Banana, Sugarcane, Tobacco, Cotton, Tomato"
    },

    # ═══════════════════════════════════════════════════════════════════════
    # SECONDARY MACRONUTRIENTS
    # ═══════════════════════════════════════════════════════════════════════
    "Calcium": {
        "symbol": "Ca", "element_type": "Secondary Macronutrient",
        "plant_content_range": "0.1-2% dry weight",
        "source": "Soil minerals, lime, gypsum, fertilizers",
        "functions": ["Cell wall structure (calcium pectate in middle lamella)", "Cell membrane integrity", "Signal transduction", "Enzyme activation", "Root tip and young leaf development"],
        "deficiency": {
            "name": "Calcium Deficiency",
            "visual_signs": "Affects only new/young leaves and growing points (Ca is immobile); tip burn (leaf tips die), blossom end rot in tomato/pepper, bitter pit in apple, tip burn in lettuce and cabbage, hollow heart in brassica",
            "affected_leaves": "Young/new leaves and growing points (Ca is IMMOBILE — not remobilized)",
            "when_visible": "During rapid growth periods; stress from irregular watering",
            "soil_ph_effects": "Severely deficient in strongly acid soils (pH < 5.0); excess K, Mg or ammonium reduces Ca uptake",
            "crop_specific": {
                "tomato": "Blossom End Rot (BER) — dark leathery patch at fruit base",
                "apple": "Bitter pit — dark depressions/spots in flesh, internal browning",
                "lettuce": "Tip burn — marginal leaf necrosis",
                "potato": "Internal brown rust — discolored vascular tissue",
                "celery": "Blackheart — inner leaf death"
            }
        },
        "toxicity": {"visual_signs": "Rare; reduces Mg, K, Zn uptake at very high Ca", "threshold": "pH > 8.0 with high Ca"},
        "forms_in_soil": ["Exchangeable Ca (most important)", "Solution Ca", "Mineral Ca (calcite, etc.)"],
        "mobility_in_plant": "Immobile — does not move from old to young tissue",
        "optimal_soil_ph": "6.0-7.5 (Ca naturally adequate at these levels)",
        "interactions": {
            "positive": ["Improves soil structure", "Reduces Al toxicity in acid soils (liming)"],
            "negative": ["High Ca reduces Mg and K (antagonism)", "High Na reduces Ca uptake in saline soils"]
        },
        "fertilizer_sources": [
            "Agricultural Lime CaCO3 (36-40% Ca) — pH correction",
            "Dolomitic Lime — CaMg(CO3)2 — provides Ca + Mg",
            "Gypsum CaSO4 (23% Ca, 18% S) — for sodic soils; doesn't raise pH",
            "Calcium Nitrate (19% Ca, 15.5% N) — for fertigation",
            "SSP (20% Ca, 16% P2O5)"
        ],
        "critical_growth_stage": "Fruit set and development; rapid growth phases",
        "soil_test_critical_level": "Exchangeable Ca > 600 kg/ha",
        "critical_crops": "Tomato, Pepper, Apple, Celery, Lettuce, Brassicas"
    },

    "Magnesium": {
        "symbol": "Mg", "element_type": "Secondary Macronutrient",
        "plant_content_range": "0.05-0.5% dry weight",
        "source": "Soil minerals, dolomite, fertilizers",
        "functions": ["Central atom of chlorophyll molecule", "Enzyme activation (100+ enzymes)", "Phosphate transport within plant", "Sugar and protein synthesis", "Activates photosynthesis"],
        "deficiency": {
            "name": "Magnesium Deficiency (Interveinal Chlorosis)",
            "visual_signs": "Interveinal chlorosis on older leaves — yellowing between the veins while veins remain green; often starts as pale green, then yellow, then reddish-purple margins; leaves may curl upward",
            "affected_leaves": "Older/Lower leaves first (Mg is mobile)",
            "when_visible": "Mid-season; worse in acid, sandy, or highly leached soils",
            "soil_ph_effects": "Deficient in acid soils, sandy soils, high rainfall areas; high K, Ca, NH4 reduce Mg uptake",
            "crop_specific": {
                "apple": "Interveinal scorching of older leaves; premature defoliation",
                "maize": "Yellow/white stripes on older leaves, especially mid-rib area",
                "tomato": "Interveinal yellowing; older leaves affected; inside dark stripe on leaf",
                "sugarcane": "Yellow stripes on older leaves from tip to base"
            }
        },
        "toxicity": {"visual_signs": "Rare outdoors; possible in greenhouse soils; reduces Ca uptake at very high Mg"},
        "forms_in_soil": ["Exchangeable Mg", "Solution Mg", "Mineral Mg (primary minerals)"],
        "mobility_in_plant": "Mobile",
        "optimal_soil_ph": "6.0-7.0",
        "interactions": {
            "positive": ["Essential partner with phosphorus in photosynthesis"],
            "negative": ["High K and Ca strongly antagonize Mg uptake", "Sandy, acidic soils prone to Mg leaching"]
        },
        "fertilizer_sources": [
            "Kieserite — Magnesium Sulphate (16% Mg, 22% S)",
            "Magnesium Sulphate (Epsom Salt) — (10% Mg) for foliar spray",
            "Dolomitic Lime — CaMg(CO3)2",
            "Magnesia (MgO)",
            "Langbeinite (K2Mg2(SO4)3)"
        ],
        "critical_growth_stage": "Vegetative growth, chlorophyll-intense periods",
        "foliar_spray": "Magnesium Sulphate (2-3% = 20-30g/L) as foliar spray is highly effective",
        "critical_crops": "Apple, Maize, Potato, Tomato, Grapes"
    },

    "Sulfur": {
        "symbol": "S", "element_type": "Secondary Macronutrient",
        "plant_content_range": "0.05-0.5% dry weight",
        "source": "Soil organic matter, atmosphere (SO2), fertilizers",
        "functions": ["Component of amino acids (cysteine, methionine)", "Protein synthesis", "Enzyme cofactor", "Glucosinolate synthesis (brassicas)", "Chlorophyll synthesis support", "Flavor compounds in Alliums"],
        "deficiency": {
            "name": "Sulfur Deficiency",
            "visual_signs": "Interveinal chlorosis of YOUNG/NEW leaves (unlike Mg which affects old leaves) — pale yellow-green color of new leaves while old leaves remain green; stunted growth",
            "affected_leaves": "Young/New leaves first (S is relatively immobile)",
            "when_visible": "Early season; intensifies in vegetative stage",
            "soil_ph_effects": "Worse in coarse-textured, low organic matter, highly leached soils; reduced acid rain deposition now causing more deficiency worldwide",
            "crop_specific": {
                "brassica": "Cupping of leaves; pale yellow-green new leaves; reduced glucosinolate content",
                "onion": "Pale yellow-green young leaves; reduced pungency",
                "mustard": "Interveinal chlorosis of younger leaves",
                "oilpalm": "Chlorosis of leaflets; reduced yield"
            }
        },
        "toxicity": {"visual_signs": "Sulfur toxicity rare in soils; atmospheric SO2 damage shows as leaf spots and margin burn"},
        "forms_in_soil": ["Sulphate ion SO42- (plant-available)", "Organic S (must mineralize)", "Pyritic S (in waterlogged soils)"],
        "mobility_in_plant": "Moderately mobile",
        "optimal_soil_ph": "6.0-7.5",
        "interactions": {
            "positive": ["S synergizes N in amino acid synthesis", "Works with Se in some metabolic pathways"],
            "negative": ["High Cl reduces S uptake"]
        },
        "fertilizer_sources": [
            "Ammonium Sulphate (24% S, 21% N)",
            "SSP (11% S)",
            "Kieserite (22% S, 16% Mg)",
            "Sulphate of Potash (18% S, 50% K2O)",
            "Gypsum CaSO4 (18% S)",
            "Wettable Sulfur (90-98% S) — fungicide + nutrient",
            "Elemental Sulfur (90-100% S) — acidifier, slow release"
        ],
        "critical_growth_stage": "Vegetative growth; bulb/head formation in Alliums and Brassicas",
        "critical_crops": "Onion, Garlic, Mustard, Canola, Sunflower, Sugarcane"
    },

    # ═══════════════════════════════════════════════════════════════════════
    # MICRONUTRIENTS (Trace Elements)
    # ═══════════════════════════════════════════════════════════════════════
    "Iron": {
        "symbol": "Fe", "element_type": "Micronutrient",
        "plant_content_range": "50-300 ppm dry weight",
        "source": "Soil minerals, organic matter, iron fertilizers",
        "functions": ["Chlorophyll synthesis (not structural)", "Electron carrier in photosynthesis and respiration", "Enzyme cofactor (catalase, peroxidase)", "Nitrogen fixation in legumes", "Nitrate reduction"],
        "deficiency": {
            "name": "Iron Chlorosis (Lime-induced Chlorosis)",
            "visual_signs": "Interveinal chlorosis on YOUNG leaves — bright yellow leaves with dark green veins; in severe cases entire leaf turns yellow then white; known as 'lime-induced chlorosis' on calcareous soils",
            "affected_leaves": "Young/New leaves first (Fe is immobile)",
            "when_visible": "Often appears on calcareous, waterlogged, or high phosphorus soils in spring",
            "soil_ph_effects": "Severely limited at pH > 7.5 (becomes insoluble); root zone waterlogging reduces Fe uptake; high P fixes Fe",
            "crop_specific": {
                "soybean": "Interveinal yellowing of new trifoliates; 'iron deficiency chlorosis (IDC)'",
                "groundnut": "Young leaf chlorosis in calcareous soils",
                "citrus": "Young leaf pale yellow with green veins — classic sign",
                "rice": "Iron toxicity (not deficiency) is common in acid waterlogged soils: bronzing of leaves"
            }
        },
        "toxicity": {
            "name": "Iron Toxicity (Bronzing in Rice)",
            "visual_signs": "In waterlogged rice soils: bronze-brown speckling of leaf surface starting from tips; 'bronzing'; roots become brown and rotten; Reduced tillering",
            "threshold": "Fe > 300 ppm in plant tissue"
        },
        "forms_in_soil": ["Fe3+ (oxidized — insoluble in high pH soils)", "Fe2+ (reduced — soluble in waterlogged conditions)", "Fe chelates in organic matter"],
        "mobility_in_plant": "Immobile",
        "optimal_soil_ph": "5.5-6.5 (best Fe availability)",
        "interactions": {
            "negative": ["High P reduces Fe uptake", "High bicarbonate (calcareous soils) immobilizes Fe", "Waterlogging causes Fe toxicity in rice"]
        },
        "fertilizer_sources": [
            "FeSO4 (Iron Sulphate) — soil application 25-50 kg/ha",
            "Fe-EDTA, Fe-DTPA, Fe-EDDHA — chelated iron (most effective, especially at high pH)",
            "Fe-EDDHA — most stable in high pH soils (most expensive)",
            "Foliar spray: FeSO4 0.5-1% (5-10g/L)"
        ],
        "critical_crops": "Soybean, Groundnut, Citrus, Grapes, Sorghum (in calcareous soils)"
    },

    "Zinc": {
        "symbol": "Zn", "element_type": "Micronutrient",
        "plant_content_range": "20-100 ppm dry weight",
        "source": "Soil minerals, organic matter, fertilizers",
        "functions": ["Enzyme activation (300+ enzymes)", "Auxin synthesis (growth hormone)", "Protein synthesis", "Chlorophyll formation", "Carbohydrate metabolism", "Pollen viability"],
        "deficiency": {
            "name": "Zinc Deficiency (Khaira Disease in Rice; Little Leaf in Fruits)",
            "visual_signs": "In cereals: pale brown spots on mid-leaf, interveinal chlorosis; In fruits: small leaves (little leaf), shortened internodes (rosetting); In maize: broad white/yellow bands (white bud); Rice: 'khaira disease' — pale orange-brown blotching of older leaves",
            "affected_leaves": "Older to young leaves depending on crop",
            "when_visible": "2-4 weeks after emergence; worse in alkaline soils after flooding",
            "soil_ph_effects": "Worst in pH > 7.5 (calcareous soils); high P soils; sandy soils; flooded rice soils (Zn becomes unavailable)",
            "crop_specific": {
                "rice": "Khaira disease: brown rusty spots; reduced tillering; 'paddystraw' leaves",
                "maize": "White bud: broad white band on leaf; severe growth stunting",
                "citrus": "Little leaf and rosette: small, narrow leaves; mottle leaf",
                "apple": "Rosette: shortened internodes; small mottled leaves"
            }
        },
        "toxicity": {
            "visual_signs": "Root growth inhibition; interveinal chlorosis (Fe/Mn deficiency induced); common on contaminated soils",
            "threshold": "Plant Zn > 400 ppm is phytotoxic"
        },
        "forms_in_soil": ["Zn2+ ion (available)", "Organic complexes", "Zinc oxide, sulphide (insoluble at high pH)"],
        "mobility_in_plant": "Low mobility",
        "optimal_soil_ph": "5.5-7.0",
        "interactions": {
            "negative": ["High P strongly reduces Zn availability and uptake", "High Fe competes with Zn", "Calcareous soils fix Zn strongly"]
        },
        "fertilizer_sources": [
            "Zinc Sulphate Monohydrate (35% Zn) — most common; soil application 25 kg/ha",
            "Zinc Sulphate Heptahydrate (21% Zn)",
            "Zinc Oxide (80% Zn) — slow release",
            "Zinc Chelate (EDTA) — for fertigation",
            "Foliar spray: ZnSO4 0.5% + lime 0.25%",
            "Seed treatment: ZnSO4 solution soaking"
        ],
        "critical_crops": "Rice (Khaira), Maize (white bud), Citrus, Apple, Cotton, Legumes"
    },

    "Manganese": {
        "symbol": "Mn", "element_type": "Micronutrient",
        "plant_content_range": "20-500 ppm dry weight",
        "source": "Soil minerals, organic matter",
        "functions": ["Photosystem II water splitting (oxygen evolution)", "Enzyme activation (Mn-SOD)", "Nitrogen assimilation", "Shikimate pathway (phenol synthesis)"],
        "deficiency": {
            "name": "Manganese Deficiency (Grey Speck in Oat; Pahala Blight in Sugarcane)",
            "visual_signs": "Interveinal chlorosis of younger leaves; grey-green patches between veins; tissue may remain light green with distinct green veins; eventually necrosis; oat: 'grey speck'; cereals: stripe patterns; sugarcane: 'pahala blight'",
            "affected_leaves": "Young/New leaves first (Mn is immobile)",
            "when_visible": "In alkaline or organic soils during dry, hot periods",
            "soil_ph_effects": "Worst at pH > 6.5; high organic matter soils (Mn immobilized); waterlogging causes Mn excess"
        },
        "toxicity": {
            "name": "Manganese Toxicity",
            "visual_signs": "Brown speckling of older leaves, irregular brown spots; marginal necrosis; symptoms of Fe and Ca deficiency (Mn-induced); common in acid soils",
            "threshold": "Mn > 300 ppm in plant tissue; worst in acid soils (pH < 5.5)"
        },
        "forms_in_soil": ["Mn2+ (available — increases in acid/waterlogged soils)", "MnO2 (insoluble in alkaline, well-aerated soils)"],
        "mobility_in_plant": "Low",
        "fertilizer_sources": ["MnSO4 (32% Mn) — soil or foliar", "Mn chelates — for high pH soils", "Foliar spray: MnSO4 0.5% (5g/L)"],
        "critical_crops": "Oat, Sugar Beet, Soybean, Legumes, Fruit trees"
    },

    "Boron": {
        "symbol": "B", "element_type": "Micronutrient",
        "plant_content_range": "5-75 ppm dry weight",
        "source": "Soil minerals (tourmaline), organic matter",
        "functions": ["Cell wall structure (cross-links pectins)", "Reproduction (pollen tube growth, fertilization)", "Sugar translocation", "Calcium utilization", "Membrane integrity"],
        "deficiency": {
            "name": "Boron Deficiency (Hollow Heart, Heart Rot)",
            "visual_signs": "Death of growing points (apical meristem); distorted, thick, brittle, curled young leaves; hollow heart in beet/turnip; sunflower head sterility; poor fruit set; corky/cracked fruits; hollow stem in brassica",
            "affected_leaves": "Young leaves and growing points (B is immobile)",
            "when_visible": "New growth stage; especially under drought stress",
            "soil_ph_effects": "Worst in acidic, sandy, leached soils; exacerbated by drought; high Ca soils reduce B uptake",
            "crop_specific": {
                "sunflower": "Hollow head: empty pith, no seeds formed",
                "cauliflower": "Brown curd, hollow stem",
                "apple": "Internal cork (brown cork-like tissue inside fruit)",
                "sugar_beet": "Heart rot: black necrosis of growing point"
            }
        },
        "toxicity": {
            "visual_signs": "Marginal leaf burn of older leaves; yellow tips and margins; root damage; B has very narrow range between deficiency and toxicity",
            "threshold": "Foliar B > 200 ppm; soil > 2 ppm available B can be toxic to sensitive crops"
        },
        "forms_in_soil": ["Boric acid H3BO3 (main available form)", "Adsorbed B on clay and organic matter"],
        "mobility_in_plant": "Low (except in crops that synthesize sorbitol/mannitol)",
        "fertilizer_sources": [
            "Borax Na2B4O7.10H2O (11% B) — soil application 0.5-1 kg/ha",
            "Boric acid H3BO3 (17% B) — foliar spray 0.2-0.3%",
            "Solubor (20% B) — soluble for spraying",
            "Boron fertilizer granules — for mixed fertilizers"
        ],
        "critical_crops": "Sunflower, Brassicas, Sugar Beet, Apple, Groundnut, Cotton"
    },

    "Copper": {
        "symbol": "Cu", "element_type": "Micronutrient",
        "plant_content_range": "2-20 ppm dry weight",
        "source": "Soil minerals, organic matter",
        "functions": ["Photosynthesis (plastocyanin)", "Enzyme activation (polyphenol oxidase, ascorbate oxidase)", "Lignin synthesis (cell wall strength)", "Pollen tube growth"],
        "deficiency": {
            "name": "Copper Deficiency (Reclamation Disease)",
            "visual_signs": "Wilting and dieback of growing tips ('die-back'); young leaves twisted, cup-shaped; pale blue-green color; in cereals: 'blind ear' — twisted leaf sheaths preventing ear emergence; bluish-green hue",
            "affected_leaves": "Young leaves and growing tips",
            "when_visible": "Especially on organic soils (histosols), peaty soils, and highly alkaline soils",
            "soil_ph_effects": "Worst on peaty, organic soils; high pH, high P, high Zn reduce Cu availability"
        },
        "toxicity": {
            "visual_signs": "Brown root discoloration; inhibited root growth; chlorosis; Fe deficiency symptoms",
            "threshold": "Soil Cu > 100 ppm is toxic to plants; vineyard soils with historical Bordeaux use are often Cu-toxic"
        },
        "forms_in_soil": ["Cu2+ and Cu+ ions (available)", "Organic Cu complexes (very stable)"],
        "mobility_in_plant": "Low",
        "fertilizer_sources": ["CuSO4 (25% Cu) — soil application 5-10 kg/ha", "Cu chelates", "Copper oxychloride (fungicide + nutrient)", "Foliar CuSO4 0.2% spray"],
        "critical_crops": "Wheat, Oat, Rye, Spinach, Onion, Fruit trees on organic soils"
    },

    "Molybdenum": {
        "symbol": "Mo", "element_type": "Micronutrient",
        "plant_content_range": "0.1-1 ppm dry weight",
        "source": "Soil minerals",
        "functions": ["Nitrate reductase (NO3 to NH4 conversion)", "Nitrogen fixation in legumes (nitrogenase)", "Sulfite oxidase activity"],
        "deficiency": {
            "name": "Molybdenum Deficiency (Whiptail in Cauliflower)",
            "visual_signs": "Interveinal chlorosis of older leaves; 'whiptail' in cauliflower/broccoli — leaves fail to unfurl properly, look like a whip; marginal scorch; in legumes: poor nodulation and N fixation",
            "affected_leaves": "Young leaves in brassica; older leaves in other crops",
            "soil_ph_effects": "Worst in acid soils (pH < 5.5); Mo becomes unavailable; LIMING is the best remedy"
        },
        "toxicity": {"visual_signs": "Very rare; excess Mo causes Cu deficiency; plants may appear Cu-deficient"},
        "forms_in_soil": ["MoO42- (molybdate — available in neutral to alkaline soils)"],
        "fertilizer_sources": ["Ammonium Molybdate (54% Mo) — tiny amounts needed 0.1-0.5 g/L foliar spray or seed treatment"],
        "critical_crops": "Cauliflower, Broccoli, Legumes (for N fixation), Maize"
    },

    "Chlorine": {
        "symbol": "Cl", "element_type": "Micronutrient",
        "plant_content_range": "100-10,000 ppm dry weight",
        "source": "Atmosphere, rain, irrigation water, fertilizers (KCl)",
        "functions": ["Photosystem II water splitting", "Stomatal regulation", "Osmotic adjustment", "Disease suppression"],
        "deficiency": {
            "name": "Chlorine Deficiency (Very Rare)",
            "visual_signs": "Wilting; leaf bronzing; chlorosis; reduced growth — rarely seen in field crops as Cl is ubiquitous",
            "affected_leaves": "Young leaves",
            "soil_ph_effects": "Not a limiting factor in most soils"
        },
        "toxicity": {"visual_signs": "Marginal leaf burn; bronze patches; premature leaf drop; salt stress symptoms", "threshold": "Soil ECe > 2 dS/m for sensitive crops"},
        "forms_in_soil": ["Cl- ion (mobile, easily leached)"],
        "critical_crops": "Coconut (Cl responsive crop), Banana, Sugar Beet; Tobacco, Potato sensitive to Cl excess"
    },

    "Nickel": {
        "symbol": "Ni", "element_type": "Micronutrient",
        "plant_content_range": "0.05-5 ppm dry weight",
        "source": "Soil minerals",
        "functions": ["Urease enzyme component (urea breakdown)", "Nitrogen metabolism", "Seed germination and early vigor"],
        "deficiency": {
            "name": "Nickel Deficiency (Mouse Ear Disease in Pecan)",
            "visual_signs": "Accumulation of urea in leaf tips (tissue damage); 'mouse ear' in pecan (small stunted rounded leaflets); leaf tip necrosis; poor seed viability",
            "crop_specific": {"pecan": "Mouse ear — small rounded deformed leaflets", "wheat": "Urea accumulation and necrotic leaf tips"}
        },
        "toxicity": {"visual_signs": "Chlorosis; stunted growth; Fe deficiency induction; very toxic in acid soils", "threshold": "Soil Ni > 25 ppm phytotoxic"},
        "fertilizer_sources": ["Nickel sulphate (very small amounts)"],
        "critical_crops": "Pecan, Wheat, Legumes"
    },

    "Cobalt": {
        "symbol": "Co", "element_type": "Beneficial Micronutrient (Legumes)",
        "plant_content_range": "0.01-0.5 ppm",
        "source": "Soil minerals",
        "functions": ["Component of vitamin B12 in Rhizobium bacteria", "Essential for nitrogen fixation in legumes (indirect)", "Drought resistance"],
        "deficiency": {
            "name": "Cobalt Deficiency (affects legume N fixation)",
            "visual_signs": "Legumes: poor nodulation and N fixation; symptoms mimic N deficiency; pale green plants; mostly on severely leached or coarse-textured soils",
            "crop_specific": {"legumes": "Poor nodulation, yellowish small plants (like N deficiency)"}
        },
        "fertilizer_sources": ["CoSO4 at 0.1-0.2 kg/ha very small dose"],
        "critical_crops": "Soybean, Clover, Alfalfa, Peanut (through Rhizobium)"
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# CROP-SPECIFIC FERTILIZER RECOMMENDATIONS (MAJOR CROPS)
# ─────────────────────────────────────────────────────────────────────────────

CROP_FERTILIZER_RECOMMENDATIONS = {
    "Rice": {
        "general_npk": "N120-P60-K60 kg/ha for irrigated; N60-P30-K30 for rainfed",
        "n_application": "Split: 50% basal + 25% active tillering + 25% panicle initiation",
        "p_application": "All basal as DAP or SSP",
        "k_application": "50% basal + 50% at panicle initiation",
        "zinc": "ZnSO4 25 kg/ha basal if soil Zn < 0.6 ppm; seedling zinc dip (2% ZnSO4 for 5 min)",
        "silicon": "200-300 kg/ha Ca silicate for lodging resistance and blast tolerance",
        "special_notes": "Urea use efficiency improved by LCC (Leaf Color Chart) monitoring; split N avoids luxury N and BLB risk",
        "critical_deficiencies": ["Zinc (Khaira)", "Iron toxicity in acid soils", "Potassium in sandy soils"]
    },
    "Wheat": {
        "general_npk": "N120-P60-K40 kg/ha for HYV; N60-P30-K20 for local varieties",
        "n_application": "50% basal + 25% CRI (crown root initiation) + 25% ear emergence",
        "p_application": "100% basal",
        "k_application": "100% basal in K-deficient soils",
        "zinc": "ZnSO4 25 kg/ha basal every 3 years",
        "sulfur": "15-20 kg S/ha as ammonium sulphate or SSP",
        "critical_deficiencies": ["Zinc", "Sulfur", "Iron (in calcareous soils)"]
    },
    "Maize": {
        "general_npk": "N180-P80-K60 kg/ha for high-yielding hybrids",
        "n_application": "33% basal + 33% V6 (knee high) + 33% tasseling",
        "p_application": "All basal",
        "zinc": "ZnSO4 25 kg/ha basal; foliar ZnSO4 0.5% if deficiency appears",
        "critical_deficiencies": ["Zinc (white bud)", "Nitrogen (main limiter)"]
    },
    "Tomato": {
        "general_npk": "N180-P120-K180 kg/ha typical for greenhouse/high-yield",
        "n_application": "Split through fertigation: 20% at transplanting, 30% vegetative, 30% fruiting, 20% late",
        "calcium": "Calcium nitrate fertigation critical during fruit set to prevent BER; spray CaCl2 0.4% when fruits marble size",
        "magnesium": "Kieserite 25 kg/ha basal or MgSO4 1% foliar",
        "special_notes": "EC of fertigation solution: 1.5-3.5 dS/m; balanced Ca:K ratio in fertigation crucial for quality",
        "critical_deficiencies": ["Calcium (BER)", "Magnesium", "Potassium"]
    },
    "Potato": {
        "general_npk": "N180-P100-K200 kg/ha — high K requirement for starch quality",
        "n_application": "50% basal + 50% at hilling; avoid late N (reduces specific gravity)",
        "calcium": "Gypsum 200-400 kg/ha or lime for scab control; Ca crucial for internal quality",
        "special_notes": "Chloride (MOP) acceptable, but SOP preferred for better specific gravity and taste; use sulfate forms",
        "critical_deficiencies": ["Calcium", "Magnesium", "Boron"]
    },
    "Cotton": {
        "general_npk": "N150-P60-K60 kg/ha for irrigated; N100-P40-K40 for rainfed",
        "n_application": "1/3 basal + 1/3 at first square + 1/3 at first flower",
        "potassium": "Higher K essential for boll load and fiber quality",
        "boron": "0.5-1 kg B/ha basal or 0.1% foliar spray at squaring and flowering",
        "critical_deficiencies": ["Potassium (fiber quality)", "Boron (boll setting)", "Zinc"]
    },
    "Sugarcane": {
        "general_npk": "N280-P120-K160 kg/ha planted crop; ratoon: N240-P80-K140",
        "n_application": "Split every 45-60 days; last application before 150 days",
        "silicon": "150-300 kg Si/ha as wollastonite or slag (reduces borer damage)",
        "critical_deficiencies": ["Zinc", "Iron", "Sulfur", "Silicon"]
    },
    "Mango": {
        "fertilizer_schedule": "Young trees: N50-P25-K25 per tree/year. Bearing trees: N1000g-P500g-K1000g per tree/year, divided twice (April + Oct)",
        "foliar_sprays": "KNO3 1% at panicle initiation; ZnSO4 0.5% after harvest; Urea 1% before flowering for fruitfulness",
        "critical_deficiencies": ["Zinc", "Boron", "Potassium"]
    },
    "Banana": {
        "general_npk": "N200-P100-K300 g/plant/year (high K crops)",
        "n_application": "Monthly split applications: 50g N every 2 months from planting",
        "k_application": "Monthly fertigation; K2O:N ratio of 2:1",
        "magnesium": "MgSO4 100g/plant/year — common deficiency in acid, sandy soils",
        "critical_deficiencies": ["Potassium (most critical)", "Magnesium", "Zinc", "Boron"]
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# VISUAL DEFICIENCY DIAGNOSIS QUICK GUIDE
# ─────────────────────────────────────────────────────────────────────────────

DEFICIENCY_DIAGNOSIS_GUIDE = {
    "Young leaves chlorotic (green veins, yellow between)": "Iron (Fe) or Manganese (Mn) deficiency",
    "Young leaves chlorotic (entire pale yellow-green)": "Sulfur (S) deficiency",
    "Older leaves chlorotic (green veins, yellow between)": "Magnesium (Mg) deficiency",
    "Older leaves uniformly pale green-yellow": "Nitrogen (N) deficiency",
    "Older leaves purple-reddish color": "Phosphorus (P) deficiency",
    "Older leaf margins brown-scorched": "Potassium (K) deficiency or Chloride toxicity",
    "Growing tip death, distorted young leaves": "Boron (B) or Calcium (Ca) deficiency",
    "Brown spots/tips on young leaves": "Calcium (Ca) deficiency",
    "Fruit blossom end rot": "Calcium (Ca) deficiency (physiological)",
    "Interveinal yellow/white on young maize leaves": "Zinc (Zn) deficiency — White Bud",
    "Distorted/small new leaves (rosetting)": "Zinc (Zn) deficiency in trees",
    "Whiptail in cauliflower": "Molybdenum (Mo) deficiency",
    "Leaf tip/margin burn starting lower leaves": "Potassium (K) deficiency",
    "Necrotic tips in grass seedlings": "Boron (B) or Copper (Cu) deficiency",
    "Blue-green, delayed emergence": "Phosphorus (P) deficiency",
    "Hollow/cracked fruits": "Boron (B) deficiency",
    "Rusty-brown lower leaf spots in rice": "Zinc (Zn) — Khaira disease"
}


def diagnose_deficiency_by_symptom(symptom: str) -> str:
    """Simple diagnosis by visual symptom."""
    symptom_lower = symptom.lower()
    for key, diagnosis in DEFICIENCY_DIAGNOSIS_GUIDE.items():
        if any(word in symptom_lower for word in key.lower().split()):
            return diagnosis
    return "Multiple possibilities — soil test recommended"


if __name__ == "__main__":
    print(f"Total essential nutrients documented: {len(ESSENTIAL_NUTRIENTS)}")
    print(f"Crop fertilizer recommendations: {len(CROP_FERTILIZER_RECOMMENDATIONS)}")
    print(f"Visual diagnosis entries: {len(DEFICIENCY_DIAGNOSIS_GUIDE)}")
