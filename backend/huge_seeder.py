import os
import sys
import json
import random
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import SessionLocal
from models import (
    Plant, BotanicalClassification, Family, Genus, SpeciesRecord, Variety,
    ClimateRequirement, SoilRequirement, FertilizerRecommendation,
    IrrigationSchedule, HarvestInformation, GrowthStage, PlantImage,
    Disease, DiseaseSymptom, DiseaseTreatment, Pest, NutrientDeficiency
)
from seeding_data import SEED_CROPS

# Programmatic lists for combinatorial generation
FAMILIES_POOL = [
    "Rosaceae", "Solanaceae", "Poaceae", "Fabaceae", "Brassicaceae", "Asteraceae", "Orchidaceae", 
    "Pinaceae", "Cactaceae", "Rutaceae", "Apiaceae", "Lamiaceae", "Arecaceae", "Rubiaceae", 
    "Theaceae", "Liliaceae", "Cupressaceae", "Araceae", "Bromeliaceae", "Myrtaceae", "Malvaceae", 
    "Lauraceae", "Zingiberaceae", "Piperaceae", "Apocynaceae", "Ranunculaceae", "Cucurbitaceae", 
    "Euphorbiaceae", "Ericaceae", "Anacardiaceae", "Amaranthaceae", "Caryophyllaceae", "Convolvulaceae", 
    "Moraceae", "Musaceae", "Oleaceae", "Papaveraceae", "Polygonaceae", "Portulacaceae", "Primulaceae"
]

GENERA_POOL = [
    "Rosa", "Solanum", "Triticum", "Oryza", "Citrus", "Brassica", "Helianthus", "Malus", "Fragaria", 
    "Prunus", "Phaseolus", "Pisum", "Capsicum", "Allium", "Mentha", "Ocimum", "Aloe", "Pinus", "Ficus", 
    "Coffea", "Camellia", "Phoenix", "Cocos", "Piper", "Zingiber", "Eucalyptus", "Acacia", "Bambusa", 
    "Nephrolepis", "Sphagnum", "Begonia", "Chrysanthemum", "Dahlia", "Echinacea", "Fuchsia", "Geranium", 
    "Hydrangea", "Impatiens", "Jasminum", "Kalanchoe", "Lavandula", "Magnolia", "Narcissus", "Origanum", 
    "Petunia", "Quercus", "Rhododendron", "Salvia", "Tulipa", "Ulmus", "Vaccinium", "Wisteria", 
    "Xanthorrhoea", "Yucca", "Zinnia", "Abies", "Betula", "Cedrus", "Daucus", "Euphorbia"
]

SPECIES_POOL = [
    "rubiginosa", "lycopersicum", "tuberosum", "aestivum", "sativa", "mays", "sinensis", "limon", 
    "reticulata", "maxima", "oleracea", "annuus", "domestica", "ananassa", "avium", "vulgaris", 
    "sativum", "piperita", "basilicum", "vera", "sylvestris", "robusta", "dactylifera", "nucifera", 
    "nigrum", "officinale", "globulus", "nilotica", "vulgaris", "sempervirens", "alba", "nigra", 
    "rubra", "grandiflora", "odorata", "officinalis", "indica", "japonica", "canadensis", "americana", 
    "europaea", "communis", "edulis", "carota", "spinosus", "aquatica", "chinensis", "germanica", 
    "officinarum", "maxima", "orientalis", "occidentalis", "pendula", "sylvatica", "campestris", 
    "pratensis", "arvensis", "montana", "palustris", "maritima"
]

CATEGORIES = [
    "Flowering", "Fruit", "Vegetable", "Cereal", "Pulse", "Herb", "Spice", "Medicinal", 
    "Shrub", "Tree", "Indoor", "Outdoor", "Aquatic", "Desert", "Forest", "Grass", 
    "Bamboo", "Fern", "Moss", "Gymnosperm", "Angiosperm", "Ornamental", "Wild", 
    "Endangered", "Invasive", "Cash Crop", "Succulent", "Cactus", "Vine", "Climber", "Creeper"
]

SOIL_TYPES = ["Sandy", "Loamy", "Clay", "Silty", "Peaty", "Chalky", "Saline", "Sandy Loam", "Clay Loam"]
CLIMATES = ["Tropical", "Subtropical", "Temperate", "Arid", "Semi-arid", "Mediterranean", "Polar", "Boreal"]
DISEASE_TYPES = ["Fungal", "Bacterial", "Viral", "Nutrient Deficiency", "Physiological Disorder", "Environmental Disorder"]
PATHOGENS = ["Alternaria", "Phytophthora", "Fusarium", "Xanthomonas", "Pseudomonas", "Tobacco Mosaic Virus", "Pythium", "Rhizoctonia", "Botrytis"]

PEST_TYPES = ["Insects", "Mites", "Nematodes", "Beetles", "Borers", "Leaf miners", "Thrips", "Scale insects", "Whiteflies", "Aphids", "Fruit flies", "Armyworms", "Locusts", "Snails", "Slugs", "Rodents"]
NUTRIENTS = ["Nitrogen", "Phosphorus", "Potassium", "Calcium", "Magnesium", "Sulfur", "Iron", "Zinc", "Copper", "Boron", "Manganese", "Molybdenum"]

def seed_huge_dataset(db: Session):
    print("🧹 Cleaning database tables for clean seed...")
    tables_to_clear = [
        "botanical_classifications", "varieties", "climate_requirements", "soil_requirements",
        "fertilizer_recommendations", "irrigation_schedules", "harvest_information", "growth_stages",
        "plant_images", "disease_symptoms", "disease_treatments", "diseases", "pests",
        "nutrient_deficiencies", "user_bookmarks", "notes", "plants", "families", "genera", "species_records"
    ]
    for table in tables_to_clear:
        try:
            db.execute(text(f"DELETE FROM {table};"))
        except Exception as e:
            print(f"Error clearing {table}: {e}")
    db.commit()

    print("🌿 Seeding reference Families, Genera, and Species records...")
    # Seed Families
    family_map = {}
    for f_name in set(FAMILIES_POOL):
        db_family = Family(name=f_name, description=f"Botanical family group of {f_name}")
        db.add(db_family)
    db.commit()
    for f in db.query(Family).all():
        family_map[f.name] = f.id

    # Seed Genera
    genus_map = {}
    for g_name in set(GENERA_POOL):
        db_genus = Genus(name=g_name, description=f"Botanical genus group of {g_name}")
        db.add(db_genus)
    db.commit()
    for g in db.query(Genus).all():
        genus_map[g.name] = g.id

    # Seed Species
    species_map = {}
    for s_name in set(SPECIES_POOL):
        db_spec = SpeciesRecord(name=s_name, description=f"Specific species identifier {s_name}")
        db.add(db_spec)
    db.commit()
    for s in db.query(SpeciesRecord).all():
        species_map[s.name] = s.id


    print("📂 Seeding the 23 handcrafted primary crops...")
    from seeding_data import seed_botanical_encyclopedia
    # Let's seed the main database from seeding_data SEED_CROPS
    # (The original method imports Families, Genera, Species dynamically if they don't exist)
    seed_botanical_encyclopedia(db)

    # Let's get the starting offset ID for plants
    handcrafted_count = db.query(Plant).count()
    print(f"✅ Handcrafted crops seeded: {handcrafted_count}")

    # Generate additional plants until we reach 100,000+
    target_count = 100050
    need_to_generate = target_count - handcrafted_count
    print(f"🚀 Generating {need_to_generate} additional plants combinatorial-style...")

    batch_size = 10000
    plants_inserted = handcrafted_count

    # To avoid memory bloating, write in chunks
    plants_chunk = []
    classifications_chunk = []
    climates_chunk = []
    soils_chunk = []
    fertilizers_chunk = []
    irrigations_chunk = []
    harvests_chunk = []

    # Prepare deterministic generator for reproducible names
    random.seed(42)

    # Helper maps
    family_names = list(family_map.keys())
    genus_names = list(genus_map.keys())
    species_names = list(species_map.keys())

    # We will generate unique botanical names by using combination + index
    for i in range(1, need_to_generate + 1):
        plant_id = handcrafted_count + i
        genus_name = random.choice(genus_names)
        species_name = random.choice(species_names)
        family_name = random.choice(family_names)
        category = random.choice(CATEGORIES)
        
        botanical_name = f"{genus_name} {species_name} var. cv_{plant_id}"
        common_name = f"{genus_name} {species_name} Cultivar {plant_id}"
        
        # Build Plant Dict
        plant_dict = {
            "id": plant_id,
            "common_name": common_name,
            "botanical_name": botanical_name,
            "synonyms": f"{genus_name} {species_name} syn_{plant_id}",
            "local_names": f"Local_{genus_name}_{plant_id}",
            "family_id": family_map[family_name],
            "genus_id": genus_map[genus_name],
            "species_id": species_map[species_name],
            "plant_authority": "L.",
            "overview": f"A dynamic {category.lower()} plant variety from the {family_name} family.",
            "morphology": "Branching root system, erect nodes, alternate leaf veins.",
            "leaf_desc": "Serrated leaves with high chlorophyll density.",
            "flower_desc": "Self-pollinated blossoms yielding seeds.",
            "fruit_desc": "Fleshy drupe or dry capsule.",
            "seed_desc": "Dicotyledonous seeds, high germination rate.",
            "stem_desc": "Ligneous or herbaceous stems.",
            "root_desc": "Fibrous or taproot system.",
            "growth_habit": random.choice(["Erect", "Decumbent", "Climbing", "Prostrate", "Bushy"]),
            "life_cycle": random.choice(["Annual", "Perennial", "Biennial"]),
            "average_height": f"{random.uniform(0.2, 8.0):.2f} m",
            "average_width": f"{random.uniform(0.1, 4.0):.2f} m",
            "lifespan": f"{random.randint(1, 50)} years",
            "category": category,
            "commercial_uses": "Local market trade, fresh food supply.",
            "medicinal_uses": "Rich source of natural vitamins and antioxidants.",
            "industrial_uses": "Fibre extracts or raw processing material.",
            "food_uses": "Fresh salads, cooked dishes, spices.",
            "toxicity": "None reported, safe for standard domestic livestock.",
            "conservation_status": random.choice(["Least Concern", "Near Threatened", "Vulnerable", "Endangered"])
        }
        plants_chunk.append(plant_dict)

        # Build BotanicalClassification Dict
        classifications_chunk.append({
            "plant_id": plant_id,
            "kingdom": "Plantae",
            "division": "Tracheophyta",
            "class_name": "Magnoliopsida",
            "order_name": f"{family_name[:-5]}ales" if family_name.endswith("aceae") else "Solanales",
            "taxonomy_hierarchy": f"Plantae -> Tracheophyta -> Magnoliopsida -> {family_name} -> {genus_name} -> {botanical_name}"
        })

        # Build ClimateRequirement Dict
        climates_chunk.append({
            "plant_id": plant_id,
            "native_region": f"Originating in {random.choice(CLIMATES)} Asia/Americas",
            "countries_grown": "India, China, USA, Brazil",
            "climatic_zones": random.choice(CLIMATES),
            "suitable_altitude": "0 - 1500 m",
            "rainfall_requirement": f"{random.randint(400, 2000)} mm",
            "temperature_requirement": f"{random.randint(15, 25)}°C - {random.randint(26, 38)}°C",
            "humidity_requirement": f"{random.randint(40, 85)}%"
        })

        # Build SoilRequirement Dict
        soils_chunk.append({
            "plant_id": plant_id,
            "preferred_soil": random.choice(SOIL_TYPES),
            "soil_ph_range": f"{random.uniform(5.5, 7.5):.1f} - {random.uniform(7.6, 8.5):.1f}",
            "drainage": "Well-drained to moderate",
            "organic_matter": "Medium to High",
            "fertility": "High",
            "texture": "Sandy Loam to Clay"
        })

        # Build FertilizerRecommendation Dict
        fertilizers_chunk.append({
            "plant_id": plant_id,
            "organic_fertilizers": "Compost manure, neem cake, bone meal",
            "chemical_fertilizers": "NPK 19-19-19 water soluble compound",
            "npk_ratio": "10-10-10",
            "application_timing": "At vegetative growth phase and flowering",
            "application_qty": "20g per square meter"
        })

        # Build IrrigationSchedule Dict
        irrigations_chunk.append({
            "plant_id": plant_id,
            "water_requirement": random.choice(["Low", "Moderate", "High"]),
            "daily_water_need": f"{random.uniform(0.5, 5.0):.1f} L per plant",
            "weekly_water_need": f"{random.uniform(3.5, 35.0):.1f} L per plant",
            "drip_recommendation": "Drip irrigation for 30 minutes every morning.",
            "critical_stages": "Germination and Flowering"
        })

        # Build HarvestInformation Dict
        harvests_chunk.append({
            "plant_id": plant_id,
            "harvest_indicators": "Color shift in fruits, leaves drying slightly.",
            "harvest_time": "Early morning or late afternoon",
            "harvest_method": "Hand plucking or mechanical clipping",
            "post_harvest_handling": "Wash, sort by maturity, pack in aerated boxes.",
            "storage_temp": "10°C - 14°C",
            "shelf_life": "7 - 21 days"
        })

        # Execute Batch Insertion when size matches
        if len(plants_chunk) >= batch_size:
            db.bulk_insert_mappings(Plant, plants_chunk)
            db.bulk_insert_mappings(BotanicalClassification, classifications_chunk)
            db.bulk_insert_mappings(ClimateRequirement, climates_chunk)
            db.bulk_insert_mappings(SoilRequirement, soils_chunk)
            db.bulk_insert_mappings(FertilizerRecommendation, fertilizers_chunk)
            db.bulk_insert_mappings(IrrigationSchedule, irrigations_chunk)
            db.bulk_insert_mappings(HarvestInformation, harvests_chunk)
            db.commit()
            
            plants_inserted += len(plants_chunk)
            print(f"   [Seeded] {plants_inserted} / {target_count} plant records...")
            
            plants_chunk = []
            classifications_chunk = []
            climates_chunk = []
            soils_chunk = []
            fertilizers_chunk = []
            irrigations_chunk = []
            harvests_chunk = []

    # Final flush
    if plants_chunk:
        db.bulk_insert_mappings(Plant, plants_chunk)
        db.bulk_insert_mappings(BotanicalClassification, classifications_chunk)
        db.bulk_insert_mappings(ClimateRequirement, climates_chunk)
        db.bulk_insert_mappings(SoilRequirement, soils_chunk)
        db.bulk_insert_mappings(FertilizerRecommendation, fertilizers_chunk)
        db.bulk_insert_mappings(IrrigationSchedule, irrigations_chunk)
        db.bulk_insert_mappings(HarvestInformation, harvests_chunk)
        db.commit()
        plants_inserted += len(plants_chunk)

    print(f"✅ Seeding of plants completed: {db.query(Plant).count()} total records.")

    # 2. Seed 50,000+ Diseases
    max_disease_id = db.execute(text("SELECT COALESCE(MAX(id), 0) FROM diseases")).scalar() or 0
    print(f"Current max disease ID: {max_disease_id}")
    disease_target = 50050
    print(f"🚀 Generating {disease_target} Disease records linked to the plants...")
    
    disease_chunk = []
    symptoms_chunk = []
    treatments_chunk = []
    
    for i in range(1, disease_target + 1):
        disease_id = max_disease_id + i
        plant_id = handcrafted_count + i
        
        disease_name = f"{random.choice(['Early', 'Late', 'Downy', 'Powdery', 'Black', 'Yellow'])} {random.choice(['Blight', 'Spot', 'Mildew', 'Rot', 'Rust', 'Curl'])}"
        pathogen = f"{random.choice(PATHOGENS)} species_{i}"
        
        disease_chunk.append({
            "id": disease_id,
            "plant_id": plant_id,
            "name": disease_name,
            "pathogen_name": pathogen,
            "disease_type": random.choice(DISEASE_TYPES),
            "risk_level": random.choice(["Low", "Medium", "High", "Critical"]),
            "economic_impact": f"Reduces yield by {random.randint(15, 60)}% if untreated."
        })
        
        symptoms_chunk.append({
            "disease_id": disease_id,
            "early_symptoms": f"Tiny yellow speckles visible on outer margin of leaves.",
            "late_symptoms": f"Widespread black patches, tissue necrosis, leaf drop.",
            "affected_parts": "Leaves, Stem, Fruit"
        })
        
        treatments_chunk.append({
            "disease_id": disease_id,
            "immediate_treatment": f"Prune affected branches immediately.",
            "organic_treatment": f"Spray 5% Neem Oil solution mixed with soap water.",
            "chemical_treatment": f"Spray copper oxychloride (3g/L) or Mancozeb (2g/L).",
            "biological_control": "Introduce Bacillus subtilis bio-agent.",
            "recommended_fungicides": "Mancozeb, Copper Hydroxide",
            "recommended_organic_solutions": "Neem Oil, Baking Soda",
            "dosage": "2-3 grams per Liter",
            "application_frequency": "Every 7 days in damp seasons",
            "safety_precautions": "Wear mask and protective clothing.",
            "recovery_time": "10-15 days"
        })
        
        if len(disease_chunk) >= batch_size:
            db.bulk_insert_mappings(Disease, disease_chunk)
            db.commit()
            db.bulk_insert_mappings(DiseaseSymptom, symptoms_chunk)
            db.bulk_insert_mappings(DiseaseTreatment, treatments_chunk)
            db.commit()
            
            disease_chunk = []
            symptoms_chunk = []
            treatments_chunk = []
            print(f"   [Seeded] {disease_id} / {disease_target + max_disease_id} disease records...")

    if disease_chunk:
        db.bulk_insert_mappings(Disease, disease_chunk)
        db.bulk_insert_mappings(DiseaseSymptom, symptoms_chunk)
        db.bulk_insert_mappings(DiseaseTreatment, treatments_chunk)
        db.commit()
    print(f"✅ Seeding of diseases completed: {db.query(Disease).count()} total records.")

    # 3. Seed 25,000+ Pests
    max_pest_id = db.execute(text("SELECT COALESCE(MAX(id), 0) FROM pests")).scalar() or 0
    pest_target = 25050
    print(f"🚀 Generating {pest_target} Pest records...")
    
    pest_chunk = []
    for i in range(1, pest_target + 1):
        pest_id = max_pest_id + i
        plant_id = handcrafted_count + i
        pest_name = f"{random.choice(PEST_TYPES)} Type_{i}"
        
        pest_chunk.append({
            "id": pest_id,
            "plant_id": plant_id,
            "name": pest_name,
            "scientific_name": f"Pestscientific {pest_name.replace(' ', '')}",
            "identification": "Recognized by visual crawling traits or web coverage.",
            "damage_symptoms": "Holes in leaf margins, leaf rolling, sticky secretions.",
            "lifecycle": "Egg to pupa in 14 days, adult lifespan of 30 days.",
            "organic_control": "Install yellow sticky traps, spray neem seed extract.",
            "chemical_control": "Apply Imidacloprid systemic spray.",
            "biological_control": "Introduce ladybugs or lacewings to eat eggs.",
            "economic_threshold": "3-5 insects per branch"
        })
        
        if len(pest_chunk) >= batch_size:
            db.bulk_insert_mappings(Pest, pest_chunk)
            db.commit()
            pest_chunk = []
            print(f"   [Seeded] {pest_id} / {pest_target + max_pest_id} pest records...")
            
    if pest_chunk:
        db.bulk_insert_mappings(Pest, pest_chunk)
        db.commit()
    print(f"✅ Seeding of pests completed: {db.query(Pest).count()} total records.")

    # 4. Seed 15,000+ Nutrient Deficiencies
    max_nd_id = db.execute(text("SELECT COALESCE(MAX(id), 0) FROM nutrient_deficiencies")).scalar() or 0
    nutrient_target = 15050
    print(f"🚀 Generating {nutrient_target} Nutrient Deficiency records...")
    
    nutrient_chunk = []
    for i in range(1, nutrient_target + 1):
        nd_id = max_nd_id + i
        plant_id = handcrafted_count + i
        nutrient_name = random.choice(NUTRIENTS)
        
        nutrient_chunk.append({
            "id": nd_id,
            "plant_id": plant_id,
            "nutrient_name": nutrient_name,
            "symptoms": f"Chlorosis in older leaf regions, leaf veins turn yellow or brown. Stunted plant shoots.",
            "correction_methods": f"Apply {nutrient_name} fertilizer compounds or organic compost teas immediately.",
            "recommended_fertilizers": f"{nutrient_name} rich fertilizer mix, seaweed extract"
        })

        
        if len(nutrient_chunk) >= batch_size:
            db.bulk_insert_mappings(NutrientDeficiency, nutrient_chunk)
            db.commit()
            nutrient_chunk = []
            print(f"   [Seeded] {nd_id} / {nutrient_target} nutrient records...")
            
    if nutrient_chunk:
        db.bulk_insert_mappings(NutrientDeficiency, nutrient_chunk)
        db.commit()
    print(f"✅ Seeding of nutrients completed: {db.query(NutrientDeficiency).count()} total records.")

    # 5. Populate local dataset structure
    print("📂 Creating dataset directory structures...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_dir = os.path.join(base_dir, "dataset")
    os.makedirs(dataset_dir, exist_ok=True)
    
    # We will seed dataset/plants/orange/...
    representative_plants = ["orange", "tomato", "potato", "apple", "rose"]
    for rp in representative_plants:
        plant_path = os.path.join(dataset_dir, "plants", rp)
        os.makedirs(plant_path, exist_ok=True)
        
        # Write metadata.json
        meta_json = {
            "name": rp.capitalize(),
            "category": "Fruit" if rp in ["orange", "apple"] else ("Vegetable" if rp in ["tomato", "potato"] else "Ornamental"),
            "description": f"Offline local dataset directory for {rp.capitalize()}."
        }
        with open(os.path.join(plant_path, "metadata.json"), "w") as f:
            json.dump(meta_json, f, indent=4)
            
        # Create image directories
        images_dir = os.path.join(plant_path, "images")
        healthy_subdirs = ["leaf", "flower", "fruit", "bark", "young", "old"]
        for hs in healthy_subdirs:
            os.makedirs(os.path.join(images_dir, "healthy", hs), exist_ok=True)
            
        diseases = ["black_spot", "greening", "canker"] if rp == "orange" else ["early_blight", "late_blight"]
        for d in diseases:
            os.makedirs(os.path.join(images_dir, "diseases", d), exist_ok=True)
            
        pests = ["aphids", "fruit_fly"]
        for p in pests:
            os.makedirs(os.path.join(images_dir, "pests", p), exist_ok=True)
            
        nutrition_parts = ["leaf", "flower", "fruit"]
        for np in nutrition_parts:
            os.makedirs(os.path.join(images_dir, "nutrition", np), exist_ok=True)
            
    print("✅ Local dataset folders initialized successfully.")

if __name__ == "__main__":
    db = SessionLocal()
    try:
        seed_huge_dataset(db)
    finally:
        db.close()
