"""
master_generator.py
Botanical Intelligence Master Dataset Generator
Combines all data modules and seeds the database
"""

import sys
import os
import json
import logging
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base

# Import all botanical data modules
from botanical_dataset.plant_taxonomy import FLAGSHIP_PLANTS, PLANT_FAMILIES, PLANT_GENERA, get_taxonomy_for_plant
from botanical_dataset.diseases_db import DISEASES_MASTER
from botanical_dataset.pests_db import PESTS_MASTER
from botanical_dataset.nutrients_db import ESSENTIAL_NUTRIENTS, CROP_FERTILIZER_RECOMMENDATIONS, DEFICIENCY_DIAGNOSIS_GUIDE
from botanical_dataset.multilingual_db import MULTILINGUAL_NAMES, LANGUAGE_CODES
from botanical_dataset.cultivation_db import CULTIVATION_DATA

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# IMPORT MODELS
# ─────────────────────────────────────────────────────────────────────────────

def get_models():
    """Import models dynamically to avoid circular imports."""
    try:
        from models_botanical import (
            TaxonomyFull, PlantDisease, PlantPest, NutritionFacts,
            MedicinalKnowledge, CultivationGuide, MultilingualName,
            RagDocument, NutrientDeficiency
        )
        return {
            'TaxonomyFull': TaxonomyFull,
            'PlantDisease': PlantDisease,
            'PlantPest': PlantPest,
            'NutritionFacts': NutritionFacts,
            'MedicinalKnowledge': MedicinalKnowledge,
            'CultivationGuide': CultivationGuide,
            'MultilingualName': MultilingualName,
            'RagDocument': RagDocument,
            'NutrientDeficiency': NutrientDeficiency,
        }
    except ImportError as e:
        logger.error(f"Failed to import models: {e}")
        return None


# ─────────────────────────────────────────────────────────────────────────────
# SEEDING FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def seed_taxonomy(db: Session, models: dict) -> int:
    """Seed the taxonomy database from plant taxonomy module."""
    TaxonomyFull = models['TaxonomyFull']
    count = 0
    seen = set()

    try:
        for plant in FLAGSHIP_PLANTS:
            botanical_name = plant.get("botanical_name", "")
            if not botanical_name or botanical_name in seen:
                continue
            seen.add(botanical_name)

            # Check if record exists
            existing = db.query(TaxonomyFull).filter_by(
                botanical_name=botanical_name
            ).first()

            if not existing:
                taxonomy = get_taxonomy_for_plant(plant)
                family_info = PLANT_FAMILIES.get(plant.get("family", ""), {})
                genera_info = PLANT_GENERA.get(plant.get("genus", ""), {})

                record = {
                    "kingdom": "Plantae",
                    "subkingdom": taxonomy.get("subkingdom", "Viridaeplantae"),
                    "division": taxonomy.get("division", "Tracheophyta"),
                    "subdivision": taxonomy.get("subdivision"),
                    "class_name": taxonomy.get("class_name", "Magnoliopsida"),
                    "subclass": taxonomy.get("subclass"),
                    "order_name": taxonomy.get("order_name", "Unknown"),
                    "family_name": plant.get("family", ""),
                    "subfamily": taxonomy.get("subfamily"),
                    "tribe": None,
                    "genus": plant.get("genus", ""),
                    "species": plant.get("species", ""),
                    "common_name": plant.get("common_name", ""),
                    "botanical_name": botanical_name,
                    "author_citation": taxonomy.get("author_citation", ""),
                    "iucn_status": taxonomy.get("iucn_status", "LC"),
                    "category": plant.get("category", ""),
                    "family_description": family_info.get("description", ""),
                    "genera_species_count": genera_info.get("species_count", 0),
                }
                db_record = TaxonomyFull(**record)
                db.add(db_record)
                count += 1

        db.commit()
        logger.info(f"✅ Seeded {count} taxonomy records")
        return count

    except Exception as e:
        db.rollback()
        logger.error(f"Error seeding taxonomy: {e}")
        raise


def seed_diseases(db: Session, models: dict) -> int:
    """Seed plant diseases from diseases_db module."""
    PlantDisease = models['PlantDisease']
    RagDocument = models['RagDocument']
    count = 0

    try:
        for plant_name, diseases in DISEASES_MASTER.items():
            for disease in diseases:
                symptoms = disease.get("symptoms", {})
                treatment = disease.get("treatment", {})

                record = {
                    "disease_name": disease.get("name", ""),
                    "pathogen_name": disease.get("pathogen_name", ""),
                    "disease_type": disease.get("disease_type", ""),
                    "affected_plant": plant_name if plant_name != "General" else disease.get("host_range", "Multiple"),
                    "host_range": disease.get("host_range", ""),
                    "risk_level": disease.get("risk_level", "Medium"),
                    "economic_impact": disease.get("economic_impact", ""),
                    "geographic_distribution": disease.get("geographic_distribution", ""),
                    "favorable_conditions": disease.get("favorable_conditions", ""),
                    "early_symptoms": symptoms.get("early", ""),
                    "late_symptoms": symptoms.get("late", ""),
                    "affected_parts": symptoms.get("affected_parts", ""),
                    "disease_cycle": disease.get("disease_cycle", ""),
                    "incubation_period": disease.get("incubation_period", ""),
                    "organic_treatment": treatment.get("organic", ""),
                    "chemical_treatment": treatment.get("chemical", ""),
                    "biological_treatment": treatment.get("biological", ""),
                    "preventive_measures": treatment.get("preventive", ""),
                    "application_frequency": treatment.get("application_frequency", ""),
                    "recovery_time": treatment.get("recovery_time", ""),
                    "phi_days": treatment.get("phi_days"),
                }

                existing = db.query(PlantDisease).filter_by(
                    disease_name=record["disease_name"],
                    affected_plant=record["affected_plant"]
                ).first()

                if not existing:
                    db_record = PlantDisease(**record)
                    db.add(db_record)

                    # Also add to RAG documents for semantic search
                    rag_content = f"""
Disease: {disease.get('name')}
Pathogen: {disease.get('pathogen_name')}
Type: {disease.get('disease_type')}
Affected Plant: {plant_name}
Host Range: {disease.get('host_range', '')}
Symptoms: {symptoms.get('early', '')}. {symptoms.get('late', '')}
Treatment: {treatment.get('organic', '')}. {treatment.get('chemical', '')}
Prevention: {treatment.get('preventive', '')}
                    """.strip()

                    rag_record = {
                        "document_type": "disease",
                        "title": f"{disease.get('name')} in {plant_name}",
                        "content": rag_content,
                        "source_module": "diseases_db",
                        "plant_name": plant_name,
                        "tags": f"{disease.get('disease_type')},{plant_name},{disease.get('pathogen_name', '')}",
                    }
                    db.add(RagDocument(**rag_record))
                    count += 1

        db.commit()
        logger.info(f"✅ Seeded {count} disease records")
        return count

    except Exception as e:
        db.rollback()
        logger.error(f"Error seeding diseases: {e}")
        raise


def seed_pests(db: Session, models: dict) -> int:
    """Seed plant pests from pests_db module."""
    PlantPest = models['PlantPest']
    RagDocument = models['RagDocument']
    count = 0

    try:
        for category, pests in PESTS_MASTER.items():
            for pest in pests:
                lifecycle = pest.get("lifecycle", {})

                record = {
                    "pest_name": pest.get("name", ""),
                    "scientific_name": pest.get("scientific_name", ""),
                    "order_name": pest.get("order", ""),
                    "family_name": pest.get("family", ""),
                    "pest_category": category,
                    "host_plants": pest.get("host_plants", ""),
                    "geographic_distribution": pest.get("geographic_distribution", ""),
                    "damage_type": pest.get("damage_type", ""),
                    "identification_tips": pest.get("identification", ""),
                    "damage_symptoms": pest.get("damage_symptoms", ""),
                    "lifecycle_summary": json.dumps(lifecycle),
                    "seasonal_peak": pest.get("seasonal_peak", ""),
                    "economic_threshold": pest.get("economic_threshold", ""),
                    "organic_control": pest.get("organic_control", ""),
                    "chemical_control": pest.get("chemical_control", ""),
                    "biological_control": pest.get("biological_control", ""),
                    "ipm_notes": pest.get("ipm_notes", ""),
                    "natural_predators": ", ".join(pest.get("natural_predators", [])),
                    "resistance_issues": pest.get("resistance_issues", ""),
                }

                existing = db.query(PlantPest).filter_by(
                    pest_name=record["pest_name"],
                    pest_category=record["pest_category"]
                ).first()

                if not existing:
                    db_record = PlantPest(**record)
                    db.add(db_record)

                    # RAG document
                    rag_content = f"""
Pest: {pest.get('name')} ({pest.get('scientific_name')})
Category: {category}
Host Plants: {pest.get('host_plants', '')}
Damage: {pest.get('damage_symptoms', '')}
Identification: {pest.get('identification', '')}
Organic Control: {pest.get('organic_control', '')}
Chemical Control: {pest.get('chemical_control', '')}
Biological Control: {pest.get('biological_control', '')}
IPM Notes: {pest.get('ipm_notes', '')}
                    """.strip()

                    rag_record = {
                        "document_type": "pest",
                        "title": f"{pest.get('name')} - {category}",
                        "content": rag_content,
                        "source_module": "pests_db",
                        "plant_name": pest.get("host_plants", "")[:100],
                        "tags": f"{category},{pest.get('scientific_name', '')}",
                    }
                    db.add(RagDocument(**rag_record))
                    count += 1

        db.commit()
        logger.info(f"✅ Seeded {count} pest records")
        return count

    except Exception as e:
        db.rollback()
        logger.error(f"Error seeding pests: {e}")
        raise


def seed_nutrients(db: Session, models: dict) -> int:
    """Seed plant nutrients and deficiency data."""
    NutrientDeficiency = models['NutrientDeficiency']
    RagDocument = models['RagDocument']
    count = 0

    try:
        for nutrient_name, nutrient_data in ESSENTIAL_NUTRIENTS.items():
            deficiency = nutrient_data.get("deficiency", {})
            toxicity = nutrient_data.get("toxicity", {})

            record = {
                "nutrient_name": nutrient_name,
                "symbol": nutrient_data.get("symbol", ""),
                "element_type": nutrient_data.get("element_type", ""),
                "plant_content_range": nutrient_data.get("plant_content_range", ""),
                "functions": json.dumps(nutrient_data.get("functions", [])),
                "deficiency_name": deficiency.get("name", f"{nutrient_name} Deficiency"),
                "deficiency_visual_signs": deficiency.get("visual_signs", ""),
                "affected_leaves": deficiency.get("affected_leaves", ""),
                "deficiency_crop_specific": json.dumps(deficiency.get("crop_specific", {})),
                "toxicity_symptoms": toxicity.get("visual_signs", ""),
                "toxicity_threshold": toxicity.get("threshold", ""),
                "forms_in_soil": json.dumps(nutrient_data.get("forms_in_soil", [])),
                "mobility_in_plant": nutrient_data.get("mobility_in_plant", ""),
                "optimal_soil_ph": nutrient_data.get("optimal_soil_ph", ""),
                "fertilizer_sources": json.dumps(nutrient_data.get("fertilizer_sources", [])),
                "critical_crops": nutrient_data.get("critical_crops", ""),
            }

            existing = db.query(NutrientDeficiency).filter_by(
                nutrient_name=nutrient_name
            ).first()

            if not existing:
                db_record = NutrientDeficiency(**record)
                db.add(db_record)

                # RAG document for nutrient
                rag_content = f"""
Nutrient: {nutrient_name} ({nutrient_data.get('symbol', '')})
Type: {nutrient_data.get('element_type', '')}
Functions: {', '.join(nutrient_data.get('functions', []))}
Deficiency Name: {deficiency.get('name', '')}
Deficiency Signs: {deficiency.get('visual_signs', '')}
Affected Leaf Position: {deficiency.get('affected_leaves', '')}
Toxicity: {toxicity.get('visual_signs', '')}
Fertilizer Sources: {', '.join(str(s) for s in nutrient_data.get('fertilizer_sources', []))}
Critical Crops: {nutrient_data.get('critical_crops', '')}
                """.strip()

                rag_record = {
                    "document_type": "nutrient",
                    "title": f"{nutrient_name} ({nutrient_data.get('symbol', '')}) - Plant Nutrition",
                    "content": rag_content,
                    "source_module": "nutrients_db",
                    "plant_name": "All crops",
                    "tags": f"nutrition,{nutrient_name},{nutrient_data.get('symbol', '')}",
                }
                db.add(RagDocument(**rag_record))
                count += 1

        # Seed crop fertilizer recommendations as RAG documents
        for crop, rec in CROP_FERTILIZER_RECOMMENDATIONS.items():
            rag_content = f"""
Crop: {crop}
Fertilizer Recommendation:
General NPK: {rec.get('general_npk', '')}
N Application: {rec.get('n_application', '')}
Special Notes: {rec.get('special_notes', rec.get('notes', ''))}
Critical Deficiencies: {', '.join(rec.get('critical_deficiencies', []))}
            """.strip()

            existing_rag = db.query(RagDocument).filter_by(
                title=f"{crop} Fertilizer Recommendation"
            ).first()

            if not existing_rag:
                rag_record = {
                    "document_type": "fertilizer_recommendation",
                    "title": f"{crop} Fertilizer Recommendation",
                    "content": rag_content,
                    "source_module": "nutrients_db",
                    "plant_name": crop,
                    "tags": f"fertilizer,{crop},nutrition",
                }
                db.add(RagDocument(**rag_record))
                count += 1

        db.commit()
        logger.info(f"✅ Seeded {count} nutrient records")
        return count

    except Exception as e:
        db.rollback()
        logger.error(f"Error seeding nutrients: {e}")
        raise


def seed_multilingual_names(db: Session, models: dict) -> int:
    """Seed multilingual plant names."""
    MultilingualName = models['MultilingualName']
    count = 0

    try:
        for botanical_name, translations in MULTILINGUAL_NAMES.items():
            for lang_code, local_name in translations.items():
                if lang_code == "en_alternate":
                    continue  # Skip alternate English names

                language_name = LANGUAGE_CODES.get(lang_code, lang_code)

                record = {
                    "botanical_name": botanical_name,
                    "language_code": lang_code,
                    "language_name": language_name,
                    "local_name": local_name,
                    "script": "Latin" if lang_code in ["en", "es", "fr", "de", "id", "ms", "pt", "sw", "ha", "yo", "tl", "vi", "tr"] else "Native",
                }

                existing = db.query(MultilingualName).filter_by(
                    botanical_name=botanical_name,
                    language_code=lang_code
                ).first()

                if not existing:
                    db_record = MultilingualName(**record)
                    db.add(db_record)
                    count += 1

        db.commit()
        logger.info(f"✅ Seeded {count} multilingual name records")
        return count

    except Exception as e:
        db.rollback()
        logger.error(f"Error seeding multilingual names: {e}")
        raise


def seed_cultivation_guides(db: Session, models: dict) -> int:
    """Seed crop cultivation guides."""
    CultivationGuide = models['CultivationGuide']
    RagDocument = models['RagDocument']
    count = 0

    try:
        for crop_name, guide in CULTIVATION_DATA.items():
            climate = guide.get("climate", {})
            soil = guide.get("soil", {})
            irrigation = guide.get("irrigation", {})
            fertilization = guide.get("fertilization", {})
            harvesting = guide.get("harvesting", {})

            record = {
                "crop_name": crop_name,
                "botanical_name": guide.get("botanical_name", ""),
                "crop_origin": guide.get("origin", ""),
                "climate_type": climate.get("type", ""),
                "temp_optimum": climate.get("temp_optimum_C", ""),
                "rainfall_requirement": climate.get("rainfall_mm", ""),
                "soil_type": soil.get("type", ""),
                "soil_ph_range": soil.get("ph_range", ""),
                "soil_special_requirements": soil.get("special_requirements", ""),
                "seed_rate": guide.get("seed_rate", ""),
                "spacing": guide.get("spacing", ""),
                "irrigation_method": irrigation.get("method", ""),
                "irrigation_critical_stages": json.dumps(irrigation.get("critical_stages", [])) if isinstance(irrigation.get("critical_stages"), list) else str(irrigation.get("critical_stages", "")),
                "water_requirement_mm": str(irrigation.get("water_requirement_mm", "")),
                "npk_recommendation": fertilization.get("npk_kg_ha", ""),
                "fertilization_schedule": fertilization.get("schedule", ""),
                "harvest_maturity_indicator": harvesting.get("maturity_indicator", harvesting.get("maturity", "")),
                "harvest_method": harvesting.get("method", ""),
                "yield_per_ha": str(harvesting.get("yield_t_ha", harvesting.get("yield_kg_ha", ""))),
                "full_guide_json": json.dumps(guide),
            }

            existing = db.query(CultivationGuide).filter_by(
                crop_name=crop_name
            ).first()

            if not existing:
                db_record = CultivationGuide(**record)
                db.add(db_record)

                # Comprehensive RAG document for cultivation guide
                rag_content = f"""
Crop: {crop_name} ({guide.get('botanical_name', '')})
Origin: {guide.get('origin', '')}
Climate: {climate.get('type', '')} — Temperature: {climate.get('temp_optimum_C', '')}; Rainfall: {climate.get('rainfall_mm', '')}
Soil: {soil.get('type', '')}; pH: {soil.get('ph_range', '')}
Seed Rate: {guide.get('seed_rate', '')}; Spacing: {guide.get('spacing', '')}
Irrigation: {irrigation.get('method', '')}; Water Requirement: {irrigation.get('water_requirement_mm', '')}
Fertilizer: {fertilization.get('npk_kg_ha', '')}
Harvest: {harvesting.get('method', '')}; Yield: {harvesting.get('yield_t_ha', '')} t/ha
                """.strip()

                rag_record = {
                    "document_type": "cultivation",
                    "title": f"{crop_name} Cultivation Guide",
                    "content": rag_content,
                    "source_module": "cultivation_db",
                    "plant_name": crop_name,
                    "tags": f"cultivation,{crop_name},{guide.get('botanical_name', '')}",
                }
                db.add(RagDocument(**rag_record))
                count += 1

        db.commit()
        logger.info(f"✅ Seeded {count} cultivation guide records")
        return count

    except Exception as e:
        db.rollback()
        logger.error(f"Error seeding cultivation guides: {e}")
        raise


# ─────────────────────────────────────────────────────────────────────────────
# MAIN SEEDING ORCHESTRATOR
# ─────────────────────────────────────────────────────────────────────────────

def run_full_botanical_seed():
    """Run the complete botanical intelligence dataset seeder."""
    start_time = datetime.now()
    logger.info("=" * 70)
    logger.info("🌿 Agro Doctor — Botanical Intelligence Dataset Seeder")
    logger.info(f"Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 70)

    # Import models
    models = get_models()
    if not models:
        logger.error("Failed to import models. Aborting.")
        return False

    # Create tables if they don't exist
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Database tables verified/created")
    except Exception as e:
        logger.error(f"Failed to create tables: {e}")
        return False

    db = SessionLocal()
    results = {}

    try:
        # 1. Seed Taxonomy
        logger.info("\n📚 Step 1/6: Seeding Plant Taxonomy...")
        results['taxonomy'] = seed_taxonomy(db, models)

        # 2. Seed Diseases
        logger.info("\n🦠 Step 2/6: Seeding Plant Diseases...")
        results['diseases'] = seed_diseases(db, models)

        # 3. Seed Pests
        logger.info("\n🐛 Step 3/6: Seeding Plant Pests...")
        results['pests'] = seed_pests(db, models)

        # 4. Seed Nutrients
        logger.info("\n🌱 Step 4/6: Seeding Plant Nutrients...")
        results['nutrients'] = seed_nutrients(db, models)

        # 5. Seed Multilingual Names
        logger.info("\n🌍 Step 5/6: Seeding Multilingual Names...")
        results['multilingual'] = seed_multilingual_names(db, models)

        # 6. Seed Cultivation Guides
        logger.info("\n🌾 Step 6/6: Seeding Cultivation Guides...")
        results['cultivation'] = seed_cultivation_guides(db, models)

        # Summary
        end_time = datetime.now()
        duration = (end_time - start_time).seconds

        logger.info("\n" + "=" * 70)
        logger.info("🎉 BOTANICAL INTELLIGENCE DATASET SEEDING COMPLETE!")
        logger.info("=" * 70)
        logger.info(f"📊 Seeding Summary:")
        logger.info(f"   🌿 Taxonomy Records:      {results.get('taxonomy', 0):>6,}")
        logger.info(f"   🦠 Disease Records:       {results.get('diseases', 0):>6,}")
        logger.info(f"   🐛 Pest Records:          {results.get('pests', 0):>6,}")
        logger.info(f"   🌱 Nutrient Records:      {results.get('nutrients', 0):>6,}")
        logger.info(f"   🌍 Multilingual Names:    {results.get('multilingual', 0):>6,}")
        logger.info(f"   🌾 Cultivation Guides:    {results.get('cultivation', 0):>6,}")
        total = sum(results.values())
        logger.info(f"   ─────────────────────────────────")
        logger.info(f"   📈 TOTAL RECORDS:         {total:>6,}")
        logger.info(f"   ⏱️  Time taken:            {duration}s")
        logger.info("=" * 70)

        return True

    except Exception as e:
        logger.error(f"Critical error during seeding: {e}")
        import traceback
        traceback.print_exc()
        return False

    finally:
        db.close()


def get_dataset_stats():
    """Get statistics about the current botanical dataset."""
    db = SessionLocal()
    models = get_models()
    if not models:
        return {}

    stats = {}
    try:
        stats['taxonomy'] = db.query(models['TaxonomyFull']).count()
        stats['diseases'] = db.query(models['PlantDisease']).count()
        stats['pests'] = db.query(models['PlantPest']).count()
        stats['nutrients'] = db.query(models['NutrientDeficiency']).count()
        stats['multilingual'] = db.query(models['MultilingualName']).count()
        stats['cultivation'] = db.query(models['CultivationGuide']).count()
        stats['rag_docs'] = db.query(models['RagDocument']).count()
        stats['total'] = sum(stats.values())
    except Exception as e:
        logger.error(f"Error getting stats: {e}")
    finally:
        db.close()

    return stats


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Agro Doctor Botanical Dataset Seeder")
    parser.add_argument("--stats", action="store_true", help="Show dataset statistics only")
    parser.add_argument("--force", action="store_true", help="Force re-seed even if data exists")
    args = parser.parse_args()

    if args.stats:
        stats = get_dataset_stats()
        print("\n📊 Current Botanical Dataset Statistics:")
        for key, value in stats.items():
            print(f"   {key}: {value:,}")
    else:
        success = run_full_botanical_seed()
        sys.exit(0 if success else 1)
