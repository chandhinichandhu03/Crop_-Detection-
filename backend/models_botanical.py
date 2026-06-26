"""
models_botanical.py
Self-contained SQLAlchemy Models for the Botanical Intelligence Dataset
These tables do NOT require foreign keys to the plants table — standalone operation
"""
import datetime
import json
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from database import Base


# ─────────────────────────────────────────────────────────────────────────────
# 1. FULL 14-RANK TAXONOMY TABLE (Standalone)
# ─────────────────────────────────────────────────────────────────────────────
class TaxonomyFull(Base):
    __tablename__ = "taxonomy_full"

    id = Column(Integer, primary_key=True, index=True)

    # 14-Rank Taxonomy
    kingdom = Column(String(100), default="Plantae")
    subkingdom = Column(String(100), nullable=True)
    division = Column(String(100), nullable=True)
    subdivision = Column(String(100), nullable=True)
    class_name = Column(String(100), nullable=True)
    subclass = Column(String(100), nullable=True)
    order_name = Column(String(100), nullable=True, index=True)
    family_name = Column(String(100), nullable=True, index=True)
    subfamily = Column(String(100), nullable=True)
    tribe = Column(String(100), nullable=True)
    genus = Column(String(200), nullable=True, index=True)
    species = Column(String(200), nullable=True)

    # Identity
    common_name = Column(String(200), nullable=True, index=True)
    botanical_name = Column(String(300), nullable=True, index=True, unique=True)
    author_citation = Column(String(200), nullable=True)
    iucn_status = Column(String(10), default="LC")

    # Classification
    category = Column(String(100), nullable=True)  # Cereal, Fruit, Vegetable, etc.
    family_description = Column(Text, nullable=True)
    genera_species_count = Column(Integer, default=0)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# ─────────────────────────────────────────────────────────────────────────────
# 2. PLANT DISEASES TABLE
# ─────────────────────────────────────────────────────────────────────────────
class PlantDisease(Base):
    __tablename__ = "plant_diseases"

    id = Column(Integer, primary_key=True, index=True)
    disease_name = Column(String(200), nullable=False, index=True)
    pathogen_name = Column(String(300), nullable=True)
    disease_type = Column(String(100), nullable=True)  # Fungal, Bacterial, Viral, etc.
    affected_plant = Column(String(200), nullable=True, index=True)
    host_range = Column(Text, nullable=True)
    risk_level = Column(String(50), default="Medium")  # Low, Medium, High, Critical
    economic_impact = Column(Text, nullable=True)
    geographic_distribution = Column(Text, nullable=True)
    favorable_conditions = Column(Text, nullable=True)

    # Symptoms
    early_symptoms = Column(Text, nullable=True)
    late_symptoms = Column(Text, nullable=True)
    affected_parts = Column(String(300), nullable=True)
    disease_cycle = Column(Text, nullable=True)
    incubation_period = Column(String(100), nullable=True)

    # Treatment
    organic_treatment = Column(Text, nullable=True)
    chemical_treatment = Column(Text, nullable=True)
    biological_treatment = Column(Text, nullable=True)
    preventive_measures = Column(Text, nullable=True)
    application_frequency = Column(String(200), nullable=True)
    recovery_time = Column(String(200), nullable=True)
    phi_days = Column(Integer, nullable=True)  # Pre-Harvest Interval

    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# ─────────────────────────────────────────────────────────────────────────────
# 3. PLANT PESTS TABLE
# ─────────────────────────────────────────────────────────────────────────────
class PlantPest(Base):
    __tablename__ = "plant_pests"

    id = Column(Integer, primary_key=True, index=True)
    pest_name = Column(String(200), nullable=False, index=True)
    scientific_name = Column(String(300), nullable=True)
    order_name = Column(String(100), nullable=True)
    family_name = Column(String(100), nullable=True)
    pest_category = Column(String(100), nullable=True, index=True)  # Sucking, Chewing, etc.
    host_plants = Column(Text, nullable=True)
    geographic_distribution = Column(Text, nullable=True)
    damage_type = Column(String(200), nullable=True)
    identification_tips = Column(Text, nullable=True)
    damage_symptoms = Column(Text, nullable=True)
    lifecycle_summary = Column(Text, nullable=True)  # JSON string
    seasonal_peak = Column(String(200), nullable=True)
    economic_threshold = Column(String(200), nullable=True)
    organic_control = Column(Text, nullable=True)
    chemical_control = Column(Text, nullable=True)
    biological_control = Column(Text, nullable=True)
    ipm_notes = Column(Text, nullable=True)
    natural_predators = Column(Text, nullable=True)
    resistance_issues = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# ─────────────────────────────────────────────────────────────────────────────
# 4. NUTRIENT DEFICIENCY TABLE
# ─────────────────────────────────────────────────────────────────────────────
class NutrientDeficiency(Base):
    __tablename__ = "botanical_nutrients"

    id = Column(Integer, primary_key=True, index=True)
    nutrient_name = Column(String(100), nullable=False, index=True, unique=True)
    symbol = Column(String(10), nullable=True)
    element_type = Column(String(100), nullable=True)  # Primary Macro, Secondary Macro, Micro
    plant_content_range = Column(String(100), nullable=True)
    functions = Column(Text, nullable=True)  # JSON list of functions
    deficiency_name = Column(String(200), nullable=True)
    deficiency_visual_signs = Column(Text, nullable=True)
    affected_leaves = Column(String(200), nullable=True)  # Old vs New leaves
    deficiency_crop_specific = Column(Text, nullable=True)  # JSON dict
    toxicity_symptoms = Column(Text, nullable=True)
    toxicity_threshold = Column(String(200), nullable=True)
    forms_in_soil = Column(Text, nullable=True)  # JSON list
    mobility_in_plant = Column(String(100), nullable=True)
    optimal_soil_ph = Column(String(50), nullable=True)
    fertilizer_sources = Column(Text, nullable=True)  # JSON list
    critical_crops = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# ─────────────────────────────────────────────────────────────────────────────
# 5. MULTILINGUAL PLANT NAMES TABLE
# ─────────────────────────────────────────────────────────────────────────────
class MultilingualName(Base):
    __tablename__ = "multilingual_names"

    id = Column(Integer, primary_key=True, index=True)
    botanical_name = Column(String(300), nullable=False, index=True)
    language_code = Column(String(10), nullable=False, index=True)
    language_name = Column(String(100), nullable=True)
    local_name = Column(String(300), nullable=False)
    script = Column(String(50), nullable=True)  # Latin, Devanagari, Arabic, etc.

    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# ─────────────────────────────────────────────────────────────────────────────
# 6. CULTIVATION GUIDE TABLE
# ─────────────────────────────────────────────────────────────────────────────
class CultivationGuide(Base):
    __tablename__ = "cultivation_guides"

    id = Column(Integer, primary_key=True, index=True)
    crop_name = Column(String(200), nullable=False, index=True, unique=True)
    botanical_name = Column(String(300), nullable=True)
    crop_origin = Column(String(300), nullable=True)

    # Climate
    climate_type = Column(String(200), nullable=True)
    temp_optimum = Column(String(100), nullable=True)
    rainfall_requirement = Column(String(100), nullable=True)

    # Soil
    soil_type = Column(String(300), nullable=True)
    soil_ph_range = Column(String(50), nullable=True)
    soil_special_requirements = Column(Text, nullable=True)

    # Planting
    seed_rate = Column(String(200), nullable=True)
    spacing = Column(String(200), nullable=True)

    # Irrigation
    irrigation_method = Column(String(200), nullable=True)
    irrigation_critical_stages = Column(Text, nullable=True)
    water_requirement_mm = Column(String(100), nullable=True)

    # Fertilization
    npk_recommendation = Column(String(200), nullable=True)
    fertilization_schedule = Column(Text, nullable=True)

    # Harvesting
    harvest_maturity_indicator = Column(Text, nullable=True)
    harvest_method = Column(String(300), nullable=True)
    yield_per_ha = Column(String(200), nullable=True)

    # Complete guide in JSON
    full_guide_json = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# ─────────────────────────────────────────────────────────────────────────────
# 7. RAG DOCUMENTS TABLE (For Offline Semantic Search)
# ─────────────────────────────────────────────────────────────────────────────
class RagDocument(Base):
    __tablename__ = "rag_documents"

    id = Column(Integer, primary_key=True, index=True)
    document_type = Column(String(100), nullable=False, index=True)  # disease, pest, nutrient, cultivation
    title = Column(String(500), nullable=False, index=True)
    content = Column(Text, nullable=False)
    source_module = Column(String(100), nullable=True)
    plant_name = Column(String(200), nullable=True, index=True)
    tags = Column(String(500), nullable=True)  # Comma-separated tags

    # TF-IDF vector data (stored as JSON string of {term: weight} pairs)
    tfidf_vector = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


# ─────────────────────────────────────────────────────────────────────────────
# 8. MEDICINAL KNOWLEDGE TABLE
# ─────────────────────────────────────────────────────────────────────────────
class MedicinalKnowledge(Base):
    __tablename__ = "medicinal_knowledge"

    id = Column(Integer, primary_key=True, index=True)
    plant_name = Column(String(200), nullable=False, index=True)
    botanical_name = Column(String(300), nullable=True)
    family_name = Column(String(100), nullable=True)

    # Traditional medicine systems
    ayurvedic_name = Column(String(200), nullable=True)
    ayurvedic_uses = Column(Text, nullable=True)
    unani_name = Column(String(200), nullable=True)
    tcm_name = Column(String(200), nullable=True)  # Traditional Chinese Medicine
    homeopathic_uses = Column(Text, nullable=True)

    # Pharmacological data
    active_compounds = Column(Text, nullable=True)  # JSON list
    pharmacological_actions = Column(Text, nullable=True)  # JSON list
    therapeutic_uses = Column(Text, nullable=True)
    contraindications = Column(Text, nullable=True)
    dosage_forms = Column(Text, nullable=True)

    # Part used
    plant_parts_used = Column(String(300), nullable=True)  # Leaf, Root, Bark, Seed, etc.

    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# ─────────────────────────────────────────────────────────────────────────────
# 9. NUTRITION FACTS TABLE (Food crops)
# ─────────────────────────────────────────────────────────────────────────────
class NutritionFacts(Base):
    __tablename__ = "nutrition_facts"

    id = Column(Integer, primary_key=True, index=True)
    food_name = Column(String(200), nullable=False, index=True)
    botanical_name = Column(String(300), nullable=True)
    serving_100g = Column(Float, default=100.0)

    # Macronutrients (per 100g)
    energy_kcal = Column(Float, nullable=True)
    protein_g = Column(Float, nullable=True)
    fat_g = Column(Float, nullable=True)
    carbohydrate_g = Column(Float, nullable=True)
    fiber_g = Column(Float, nullable=True)
    sugar_g = Column(Float, nullable=True)

    # Vitamins
    vitamin_c_mg = Column(Float, nullable=True)
    vitamin_a_ug = Column(Float, nullable=True)
    vitamin_b1_mg = Column(Float, nullable=True)
    vitamin_b2_mg = Column(Float, nullable=True)
    vitamin_b3_mg = Column(Float, nullable=True)
    vitamin_b6_mg = Column(Float, nullable=True)
    vitamin_b12_ug = Column(Float, nullable=True)
    vitamin_d_ug = Column(Float, nullable=True)
    vitamin_e_mg = Column(Float, nullable=True)
    vitamin_k_ug = Column(Float, nullable=True)

    # Minerals
    calcium_mg = Column(Float, nullable=True)
    iron_mg = Column(Float, nullable=True)
    magnesium_mg = Column(Float, nullable=True)
    phosphorus_mg = Column(Float, nullable=True)
    potassium_mg = Column(Float, nullable=True)
    sodium_mg = Column(Float, nullable=True)
    zinc_mg = Column(Float, nullable=True)

    # Special compounds
    antioxidants = Column(Text, nullable=True)
    phytonutrients = Column(Text, nullable=True)
    glycemic_index = Column(Integer, nullable=True)

    data_source = Column(String(100), default="USDA FoodData Central")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# ─────────────────────────────────────────────────────────────────────────────
# 10. SEED DATA TABLE
# ─────────────────────────────────────────────────────────────────────────────
class SeedData(Base):
    __tablename__ = "seed_data"

    id = Column(Integer, primary_key=True, index=True)
    crop_name = Column(String(200), nullable=False, index=True)
    botanical_name = Column(String(300), nullable=True)
    variety_name = Column(String(200), nullable=True)

    # Seed characteristics
    seed_color = Column(String(100), nullable=True)
    seed_shape = Column(String(100), nullable=True)
    seed_weight_g_1000 = Column(Float, nullable=True)  # 1000-seed weight
    seed_rate_kg_ha = Column(Float, nullable=True)
    germination_pct = Column(Float, nullable=True)
    germination_temp_C = Column(String(50), nullable=True)

    # Seed treatment
    seed_treatment_fungicide = Column(String(200), nullable=True)
    seed_treatment_bioagent = Column(String(200), nullable=True)
    seed_treatment_insecticide = Column(String(200), nullable=True)
    pelleting = Column(Boolean, default=False)

    # Storage
    storage_temp_C = Column(String(50), nullable=True)
    storage_humidity_pct = Column(String(50), nullable=True)
    seed_viability_years = Column(Integer, nullable=True)

    # Source
    breeder_institute = Column(String(200), nullable=True)
    release_year = Column(Integer, nullable=True)
    dte_days = Column(Integer, nullable=True)  # Days to emergence

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
