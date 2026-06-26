"""
export_json.py
Exports rich nested JSON (grouped by category) and JSONL streaming files.
"""

import os
import json
import sys
import logging
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal
from models_botanical import (
    TaxonomyFull, PlantDisease, PlantPest, NutrientDeficiency,
    MultilingualName, CultivationGuide, MedicinalKnowledge, NutritionFacts, SeedData
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

JSON_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "dataset", "exports", "json"))
JSONL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "dataset", "exports", "jsonl"))

def export_all_to_json():
    """Build and write rich nested JSON & JSONL files."""
    db = SessionLocal()
    os.makedirs(JSON_DIR, exist_ok=True)
    os.makedirs(JSONL_DIR, exist_ok=True)
    
    logger.info("Building nested botanical profile documents...")
    
    # Load all records into memory for fast mapping
    taxonomy_records = db.query(TaxonomyFull).all()
    diseases = db.query(PlantDisease).all()
    pests = db.query(PlantPest).all()
    multilingual = db.query(MultilingualName).all()
    cultivation = db.query(CultivationGuide).all()
    medicinal = db.query(MedicinalKnowledge).all()
    nutrition = db.query(NutritionFacts).all()
    seeds = db.query(SeedData).all()
    
    # Maps for fast lookup by plant/botanical name
    diseases_by_plant = defaultdict(list)
    for d in diseases:
        diseases_by_plant[d.affected_plant.lower()].append(d)
        
    pests_by_plant = defaultdict(list)
    for p in pests:
        # Check if crop name is in host_plants string
        host_str = (p.host_plants or "").lower()
        pests_by_plant[host_str].append(p)
        
    multi_by_plant = defaultdict(dict)
    for m in multilingual:
        multi_by_plant[m.botanical_name.lower()][m.language_code] = {
            "language_name": m.language_name,
            "local_name": m.local_name,
            "script": m.script
        }
        
    cultivation_by_plant = {}
    for c in cultivation:
        cultivation_by_plant[c.crop_name.lower()] = c
        if c.botanical_name:
            cultivation_by_plant[c.botanical_name.lower()] = c
            
    medicinal_by_plant = {}
    for m in medicinal:
        medicinal_by_plant[m.botanical_name.lower()] = m
        
    nutrition_by_plant = {}
    for n in nutrition:
        nutrition_by_plant[n.botanical_name.lower()] = n
        
    seeds_by_plant = {}
    for s in seeds:
        seeds_by_plant[s.botanical_name.lower()] = s
        
    nested_docs = []
    category_docs = defaultdict(list)
    
    for plant in taxonomy_records:
        bot_name = plant.botanical_name.lower()
        common_name = plant.common_name.lower()
        
        # 1. Gather Diseases
        plant_diseases = []
        # Exact match or substring match
        matched_diseases = diseases_by_plant[bot_name] or diseases_by_plant[common_name]
        if not matched_diseases:
            # Fallback fuzzy check
            for p_key, ds in diseases_by_plant.items():
                if p_key in bot_name or p_key in common_name or bot_name in p_key or common_name in p_key:
                    plant_diseases.extend(ds)
        else:
            plant_diseases = matched_diseases
            
        diseases_list = [{
            "id": d.id,
            "disease_name": d.disease_name,
            "pathogen_name": d.pathogen_name,
            "disease_type": d.disease_type,
            "risk_level": d.risk_level,
            "symptoms": {
                "early": d.early_symptoms,
                "late": d.late_symptoms,
                "affected_parts": d.affected_parts
            },
            "treatment": {
                "organic": d.organic_treatment,
                "chemical": d.chemical_treatment,
                "biological": d.biological_treatment,
                "preventive": d.preventive_measures
            }
        } for d in set(plant_diseases)]
        
        # 2. Gather Pests
        plant_pests = []
        for host_str, ps in pests_by_plant.items():
            if bot_name in host_str or common_name in host_str or host_str in bot_name or host_str in common_name:
                plant_pests.extend(ps)
                
        pests_list = [{
            "id": p.id,
            "pest_name": p.pest_name,
            "scientific_name": p.scientific_name,
            "pest_category": p.pest_category,
            "damage_type": p.damage_type,
            "control": {
                "organic": p.organic_control,
                "chemical": p.chemical_control,
                "biological": p.biological_control
            }
        } for p in set(plant_pests)]
        
        # 3. Cultivation guide
        cg = cultivation_by_plant.get(bot_name) or cultivation_by_plant.get(common_name)
        cultivation_guide = {}
        if cg:
            cultivation_guide = {
                "climate": {
                    "type": cg.climate_type,
                    "temp_optimum": cg.temp_optimum,
                    "rainfall": cg.rainfall_requirement
                },
                "soil": {
                    "type": cg.soil_type,
                    "ph_range": cg.soil_ph_range,
                    "special_requirements": cg.soil_special_requirements
                },
                "planting": {
                    "seed_rate": cg.seed_rate,
                    "spacing": cg.spacing
                },
                "irrigation": {
                    "method": cg.irrigation_method,
                    "critical_stages": cg.irrigation_critical_stages,
                    "water_requirement_mm": cg.water_requirement_mm
                },
                "fertilization": {
                    "npk": cg.npk_recommendation,
                    "schedule": cg.fertilization_schedule
                },
                "harvesting": {
                    "maturity_indicator": cg.harvest_maturity_indicator,
                    "method": cg.harvest_method,
                    "yield_per_ha": cg.yield_per_ha
                }
            }
            
        # 4. Medicinal
        med = medicinal_by_plant.get(bot_name)
        medicinal_knowledge = {}
        if med:
            medicinal_knowledge = {
                "ayurvedic_properties": {
                    "rasa": med.rasa,
                    "guna": med.guna,
                    "virya": med.virya,
                    "vipaka": med.vipaka,
                    "dosha_karma": med.dosha_karma
                },
                "traditional_uses": med.traditional_uses,
                "active_compounds": med.active_compounds,
                "pharmacological_effects": med.pharmacological_effects,
                "dosage_formulations": med.dosage_formulations,
                "contraindications": med.contraindications
            }
            
        # 5. Nutrition
        nut = nutrition_by_plant.get(bot_name)
        nutrition_facts = {}
        if nut:
            nutrition_facts = {
                "energy_kcal": nut.energy_kcal,
                "protein_g": nut.protein_g,
                "fat_g": nut.fat_g,
                "carbohydrates_g": nut.carbohydrates_g,
                "fiber_g": nut.fiber_g,
                "minerals_mg": {
                    "calcium": nut.calcium_mg,
                    "iron": nut.iron_mg,
                    "magnesium": nut.magnesium_mg,
                    "phosphorus": nut.phosphorus_mg,
                    "potassium": nut.potassium_mg,
                    "zinc": nut.zinc_mg
                },
                "vitamins_mg": {
                    "vitamin_c": nut.vitamin_c_mg,
                    "thiamin": nut.thiamin_mg,
                    "riboflavin": nut.riboflavin_mg,
                    "niacin": nut.niacin_mg,
                    "folate_mcg": nut.folate_mcg,
                    "vitamin_a_rae_mcg": nut.vitamin_a_rae_mcg
                }
            }
            
        # 6. Seed morphology
        sd = seeds_by_plant.get(bot_name)
        seed_data = {}
        if sd:
            seed_data = {
                "color": sd.seed_color,
                "shape": sd.seed_shape,
                "size_mm": sd.seed_size_mm,
                "weight_g_1000": sd.weight_g_1000,
                "germination_type": sd.germination_type,
                "germination_temp_C": sd.germination_temp_C,
                "germination_days": sd.germination_days,
                "viability_years": sd.viability_years,
                "storage_conditions": sd.storage_conditions
            }
            
        doc = {
            "id": plant.id,
            "common_name": plant.common_name,
            "botanical_name": plant.botanical_name,
            "author_citation": plant.author_citation,
            "iucn_status": plant.iucn_status,
            "category": plant.category or "Other",
            "taxonomy": {
                "kingdom": plant.kingdom,
                "subkingdom": plant.subkingdom,
                "division": plant.division,
                "subdivision": plant.subdivision,
                "class": plant.class_name,
                "subclass": plant.subclass,
                "order": plant.order_name,
                "family": plant.family_name,
                "subfamily": plant.subfamily,
                "genus": plant.genus,
                "species": plant.species,
                "family_description": plant.family_description,
                "genus_species_count": plant.genera_species_count
            },
            "multilingual_names": multi_by_plant.get(bot_name, {}),
            "cultivation": cultivation_guide,
            "diseases": diseases_list,
            "pests": pests_list,
            "medicinal": medicinal_knowledge,
            "nutrition": nutrition_facts,
            "seeds": seed_data
        }
        
        nested_docs.append(doc)
        category_docs[doc["category"].replace("/", "_").replace(" ", "_")].append(doc)
        
    # Write individual category files
    for cat_name, docs in category_docs.items():
        json_file_path = os.path.join(JSON_DIR, f"{cat_name.lower()}.json")
        with open(json_file_path, "w", encoding="utf-8") as f:
            json.dump(docs, f, indent=2, ensure_ascii=False)
        logger.info(f"✅ Exported {len(docs)} documents to {cat_name.lower()}.json")
        
    # Write master JSON file
    master_json_path = os.path.join(JSON_DIR, "master_botanical_dataset.json")
    with open(master_json_path, "w", encoding="utf-8") as f:
        json.dump(nested_docs, f, indent=2, ensure_ascii=False)
    logger.info(f"✅ Exported all {len(nested_docs)} documents to master_botanical_dataset.json")
    
    # Write streaming JSONL file
    jsonl_file_path = os.path.join(JSONL_DIR, "master_botanical_dataset.jsonl")
    with open(jsonl_file_path, "w", encoding="utf-8") as f:
        for doc in nested_docs:
            f.write(json.dumps(doc, ensure_ascii=False) + "\n")
    logger.info(f"✅ Exported master_botanical_dataset.jsonl")
    
    db.close()

if __name__ == "__main__":
    export_all_to_json()
