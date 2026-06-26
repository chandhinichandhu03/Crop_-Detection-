"""
export_markdown.py
Generates beautifully formatted Markdown documentation files for all categories.
"""

import os
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

MARKDOWN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "dataset", "exports", "markdown"))

def export_all_to_markdown():
    """Generate Markdown documentation per category."""
    db = SessionLocal()
    os.makedirs(MARKDOWN_DIR, exist_ok=True)
    
    logger.info(f"Generating Markdown files in: {MARKDOWN_DIR}")
    
    # Load data
    taxonomy_records = db.query(TaxonomyFull).all()
    diseases = db.query(PlantDisease).all()
    pests = db.query(PlantPest).all()
    multilingual = db.query(MultilingualName).all()
    cultivation = db.query(CultivationGuide).all()
    medicinal = db.query(MedicinalKnowledge).all()
    nutrition = db.query(NutritionFacts).all()
    seeds = db.query(SeedData).all()
    
    # Pre-map data
    diseases_by_plant = defaultdict(list)
    for d in diseases:
        diseases_by_plant[d.affected_plant.lower()].append(d)
        
    pests_by_plant = defaultdict(list)
    for p in pests:
        host_str = (p.host_plants or "").lower()
        pests_by_plant[host_str].append(p)
        
    multi_by_plant = defaultdict(list)
    for m in multilingual:
        multi_by_plant[m.botanical_name.lower()].append(m)
        
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
        
    # Group plants by category
    by_category = defaultdict(list)
    for plant in taxonomy_records:
        cat = plant.category or "Other"
        by_category[cat].append(plant)
        
    for category, plants in by_category.items():
        file_cat_name = category.replace("/", "_").replace(" ", "_").lower()
        md_file_path = os.path.join(MARKDOWN_DIR, f"{file_cat_name}.md")
        
        logger.info(f"Generating {file_cat_name}.md ({len(plants)} plants)...")
        
        try:
            with open(md_file_path, "w", encoding="utf-8") as f:
                f.write(f"# Agro Doctor Botanical Manual: {category.title()}\n\n")
                f.write(f"This document contains comprehensive offline botanical classification, cultivation guides, diseases, and agricultural practices for all major crops in the **{category}** category.\n\n")
                
                # Table of Contents
                f.write("## Table of Contents\n")
                for p in sorted(plants, key=lambda x: x.common_name or x.botanical_name):
                    p_name = p.common_name or p.botanical_name
                    anchor = p_name.lower().replace(" ", "-").replace(".", "").replace("(", "").replace(")", "")
                    f.write(f"- [{p_name}](#{anchor})\n")
                f.write("\n---\n\n")
                
                # Detailed profiles
                for p in sorted(plants, key=lambda x: x.common_name or x.botanical_name):
                    bot_name = p.botanical_name.lower()
                    common_name = p.common_name.lower()
                    
                    f.write(f"## {p.common_name or p.botanical_name}\n\n")
                    f.write(f"**Scientific Name**: *{p.botanical_name}* {p.author_citation or ''}\n")
                    f.write(f"**IUCN Conservation Status**: `{p.iucn_status or 'LC'}`\n\n")
                    
                    # 1. Taxonomy Table
                    f.write("### 📋 Botanical Taxonomy Hierarchy\n\n")
                    f.write("| Rank | Name | Description |\n")
                    f.write("| --- | --- | --- |\n")
                    f.write(f"| **Kingdom** | {p.kingdom} | Plant kingdom |\n")
                    f.write(f"| **Division** | {p.division} | Vascular/Non-vascular division |\n")
                    f.write(f"| **Class** | {p.class_name} | Class classification |\n")
                    f.write(f"| **Order** | {p.order_name} | Order grouping |\n")
                    f.write(f"| **Family** | {p.family_name} | {p.family_description or ''} |\n")
                    f.write(f"| **Genus** | {p.genus} | Genus grouping |\n")
                    f.write(f"| **Species** | *{p.species}* | Species epithet |\n\n")
                    
                    # 2. Local names
                    local_names_list = multi_by_plant[bot_name]
                    if local_names_list:
                        f.write("### 🌍 Multilingual Translations\n\n")
                        for l in local_names_list:
                            f.write(f"- **{l.language_name}** ({l.language_code}): {l.local_name}\n")
                        f.write("\n")
                        
                    # 3. Cultivation guide
                    cg = cultivation_by_plant.get(bot_name) or cultivation_by_plant.get(common_name)
                    if cg:
                        f.write("### 🌾 Crop Cultivation & Agronomy Guide\n\n")
                        f.write(f"- **Origin**: {cg.crop_origin or 'Unknown'}\n")
                        f.write(f"- **Climatic Preference**: {cg.climate_type} (Temp: {cg.temp_optimum}, Rainfall: {cg.rainfall_requirement})\n")
                        f.write(f"- **Soil Requirements**: {cg.soil_type} (pH: {cg.soil_ph_range})\n")
                        if cg.soil_special_requirements:
                            f.write(f"  *Special Note: {cg.soil_special_requirements}*\n")
                        f.write(f"- **Sowing Details**: Seed rate: {cg.seed_rate}, Spacing: {cg.spacing}\n")
                        f.write(f"- **Irrigation Needs**: Method: {cg.irrigation_method}, Critical Stages: {cg.irrigation_critical_stages}\n")
                        f.write(f"- **Fertilizer Strategy**: NPK recommendations: `{cg.npk_recommendation}`\n")
                        if cg.fertilization_schedule:
                            f.write(f"  *Schedule: {cg.fertilization_schedule}*\n")
                        f.write(f"- **Harvesting**: Maturity indices: {cg.harvest_maturity_indicator}, Method: {cg.harvest_method}, Expected Yield: {cg.yield_per_ha}\n\n")
                        
                    # 4. Medicinal & Bioactive
                    med = medicinal_by_plant.get(bot_name)
                    if med:
                        f.write("### 🌿 Pharmacological & Traditional Uses\n\n")
                        f.write(f"- **Traditional Medicine (Ayurveda)**: Rasa: {med.rasa}, Guna: {med.guna}, Virya: {med.virya}, Vipaka: {med.vipaka}\n")
                        f.write(f"- **Traditional Applications**: {med.traditional_uses}\n")
                        f.write(f"- **Bioactive Phytochemicals**: {med.active_compounds}\n")
                        f.write(f"- **Modern Scientific/Pharmacological Effects**: {med.pharmacological_effects}\n")
                        f.write(f"- **Contraindications / Safety**: {med.contraindications}\n\n")
                        
                    # 5. Nutrition Facts
                    nut = nutrition_by_plant.get(bot_name)
                    if nut:
                        f.write("### 🍎 Nutritional Profile (per 100g serving)\n\n")
                        f.write(f"- **Energy**: {nut.energy_kcal} kcal\n")
                        f.write(f"- **Macronutrients**: Protein: {nut.protein_g}g, Fat: {nut.fat_g}g, Carbohydrates: {nut.carbohydrates_g}g, Fiber: {nut.fiber_g}g\n")
                        f.write(f"- **Key Vitamins & Minerals**:\n")
                        f.write(f"  * Calcium: {nut.calcium_mg}mg \| Iron: {nut.iron_mg}mg \| Potassium: {nut.potassium_mg}mg \| Zinc: {nut.zinc_mg}mg\n")
                        f.write(f"  * Vitamin C: {nut.vitamin_c_mg}mg \| Folate: {nut.folate_mcg}mcg \| Vitamin A (RAE): {nut.vitamin_a_rae_mcg}mcg\n\n")
                        
                    # 6. Seed properties
                    sd = seeds_by_plant.get(bot_name)
                    if sd:
                        f.write("### 🌰 Seed Morphology & Germination\n\n")
                        f.write(f"- **Seed Profile**: Color: {sd.seed_color}, Shape: {sd.seed_shape}, Size: {sd.seed_size_mm} mm, 1000-Seed Weight: {sd.weight_g_1000}g\n")
                        f.write(f"- **Germination Criteria**: Type: {sd.germination_type}, Temp: {sd.germination_temp_C}°C, Germination period: {sd.germination_days} days\n")
                        f.write(f"- **Storage & Viability**: Viability: {sd.viability_years} years under: {sd.storage_conditions}\n\n")
                        
                    # 7. Diseases
                    plant_diseases = diseases_by_plant[bot_name] or diseases_by_plant[common_name]
                    if not plant_diseases:
                        # Fallback fuzzy match
                        for p_key, ds in diseases_by_plant.items():
                            if p_key in bot_name or p_key in common_name or bot_name in p_key or common_name in p_key:
                                plant_diseases.extend(ds)
                                
                    plant_diseases = list(set(plant_diseases))
                    if plant_diseases:
                        f.write("### 🦠 Pathological Diagnosis (Diseases)\n\n")
                        for d in plant_diseases:
                            f.write(f"#### {d.disease_name} ({d.disease_type})\n")
                            f.write(f"- **Pathogen**: *{d.pathogen_name}*\n")
                            f.write(f"- **Symptoms**: {d.early_symptoms or d.late_symptoms}\n")
                            f.write(f"- **Treatment Protocols**:\n")
                            if d.organic_treatment:
                                f.write(f"  * **Organic**: {d.organic_treatment}\n")
                            if d.chemical_treatment:
                                f.write(f"  * **Chemical**: {d.chemical_treatment}\n")
                            if d.preventive_measures:
                                f.write(f"  * **Prevention**: {d.preventive_measures}\n")
                            f.write("\n")
                            
                    # 8. Pests
                    plant_pests = []
                    for host_str, ps in pests_by_plant.items():
                        if bot_name in host_str or common_name in host_str or host_str in bot_name or host_str in common_name:
                            plant_pests.extend(ps)
                            
                    plant_pests = list(set(plant_pests))
                    if plant_pests:
                        f.write("### 🐛 Entomological Threats (Pests)\n\n")
                        for p_p in plant_pests:
                            f.write(f"#### {p_p.pest_name} (*{p_p.scientific_name}*)\n")
                            f.write(f"- **Damage Symptoms**: {p_p.damage_symptoms}\n")
                            f.write(f"- **IPM & Control Measures**:\n")
                            if p_p.organic_control:
                                f.write(f"  * **Organic/IPM**: {p_p.organic_control}\n")
                            if p_p.chemical_control:
                                f.write(f"  * **Chemical**: {p_p.chemical_control}\n")
                            if p_p.biological_control:
                                f.write(f"  * **Biological**: {p_p.biological_control}\n")
                            f.write("\n")
                            
                    f.write("\n---\n\n")
                    
            logger.info(f"✅ Generated Markdown file for {category}")
        except Exception as e:
            logger.error(f"❌ Failed to generate Markdown for {category}: {e}")
            import traceback
            traceback.print_exc()
            
    db.close()

if __name__ == "__main__":
    export_all_to_markdown()
