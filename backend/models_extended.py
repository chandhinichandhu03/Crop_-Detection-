"""
Extended SQLAlchemy Models for Agro Doctor
World's Largest Offline Botanical Intelligence Dataset
Adds 15 new normalized tables beyond the base models.py
"""
import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean, JSON
from sqlalchemy.orm import relationship
from database import Base


# ─────────────────────────────────────────────────────────────────────────────
# 1. FULL 14-RANK TAXONOMY TABLE
# ─────────────────────────────────────────────────────────────────────────────
class TaxonomyFull(Base):
    __tablename__ = "taxonomy_full"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False, index=True)

    # 14-rank taxonomy
    kingdom = Column(String, default="Plantae")
    subkingdom = Column(String, nullable=True)
    division = Column(String, nullable=True)          # Phylum
    subdivision = Column(String, nullable=True)
    class_name = Column(String, nullable=True)
    subclass = Column(String, nullable=True)
    order_name = Column(String, nullable=True)
    family_name = Column(String, nullable=True)
    subfamily = Column(String, nullable=True)
    tribe = Column(String, nullable=True)
    subtribe = Column(String, nullable=True)
    genus = Column(String, nullable=True)
    species = Column(String, nullable=True)
    subspecies = Column(String, nullable=True)
    variety = Column(String, nullable=True)
    cultivar = Column(String, nullable=True)
    hybrid = Column(String, nullable=True)

    # Name authority
    scientific_name = Column(String, nullable=True)
    botanical_name = Column(String, nullable=True)
    author_citation = Column(String, nullable=True)
    accepted_name = Column(String, nullable=True)
    ipni_id = Column(String, nullable=True)           # IPNI reference
    wfo_id = Column(String, nullable=True)            # World Flora Online ID
    gbif_id = Column(String, nullable=True)           # GBIF ID
    ncbi_taxon_id = Column(String, nullable=True)     # NCBI Taxonomy ID
    usda_plants_code = Column(String, nullable=True)  # USDA PLANTS symbol

    taxonomy_hierarchy = Column(Text, nullable=True)  # Full lineage string
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# ─────────────────────────────────────────────────────────────────────────────
# 2. SCIENTIFIC SYNONYMS TABLE
# ─────────────────────────────────────────────────────────────────────────────
class PlantSynonym(Base):
    __tablename__ = "plant_synonyms"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False, index=True)
    synonym_name = Column(String, nullable=False)
    synonym_type = Column(String, default="Scientific")  # Scientific, Trade, Horticultural
    source = Column(String, nullable=True)               # IPNI, WFO, GRIN-Global, etc.
    is_accepted = Column(Boolean, default=False)


# ─────────────────────────────────────────────────────────────────────────────
# 3. MULTILINGUAL LOCAL NAMES TABLE
# ─────────────────────────────────────────────────────────────────────────────
class LocalName(Base):
    __tablename__ = "local_names"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False, index=True)
    language = Column(String, nullable=False)            # e.g., "Hindi", "Tamil", "Spanish"
    language_code = Column(String, nullable=True)        # ISO 639-1 code e.g., "hi", "ta", "es"
    script = Column(String, nullable=True)               # Latin, Devanagari, Arabic, etc.
    local_name = Column(String, nullable=False)
    transliteration = Column(String, nullable=True)      # Roman transliteration if non-Latin
    region = Column(String, nullable=True)               # Specific region where this name is used
    name_type = Column(String, default="Common")         # Common, Folk, Market, Sacred


# ─────────────────────────────────────────────────────────────────────────────
# 4. SEED MORPHOLOGY & GERMINATION TABLE
# ─────────────────────────────────────────────────────────────────────────────
class SeedData(Base):
    __tablename__ = "seed_data"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False, index=True)

    seed_name = Column(String, nullable=True)
    seed_type = Column(String, nullable=True)           # Dicot, Monocot, Gymnosperm
    seed_shape = Column(String, nullable=True)          # Round, Oval, Kidney, Oblong, Flat
    seed_color = Column(String, nullable=True)
    seed_surface = Column(String, nullable=True)        # Smooth, Rough, Hairy, Winged
    seed_size_mm = Column(String, nullable=True)        # "2-3 mm"
    thousand_seed_weight_g = Column(Float, nullable=True)  # TSW in grams
    seeds_per_gram = Column(Float, nullable=True)

    # Germination
    germination_rate_pct = Column(Float, nullable=True)
    germination_days_min = Column(Integer, nullable=True)
    germination_days_max = Column(Integer, nullable=True)
    germination_temp_min_c = Column(Float, nullable=True)
    germination_temp_max_c = Column(Float, nullable=True)
    germination_temp_optimal_c = Column(Float, nullable=True)

    # Dormancy & Viability
    dormancy_type = Column(String, nullable=True)       # None, Physical, Physiological, Morphological
    dormancy_period_days = Column(Integer, nullable=True)
    seed_treatment = Column(Text, nullable=True)        # Scarification, stratification, soaking
    viability_years = Column(Float, nullable=True)
    orthodox_seed = Column(Boolean, default=True)       # Orthodox vs Recalcitrant

    # Storage
    storage_temp_c = Column(Float, nullable=True)
    storage_humidity_pct = Column(Float, nullable=True)
    storage_conditions = Column(Text, nullable=True)

    # Propagation
    propagation_methods = Column(Text, nullable=True)   # Seed, Cutting, Grafting, Division
    sowing_depth_cm = Column(Float, nullable=True)
    sowing_season = Column(String, nullable=True)
    seed_rate_kg_per_ha = Column(Float, nullable=True)

    # Quality Standards
    purity_standard_pct = Column(Float, nullable=True)
    germination_standard_pct = Column(Float, nullable=True)
    moisture_standard_pct = Column(Float, nullable=True)
    certification_body = Column(String, nullable=True)  # ISTA, NSA, etc.


# ─────────────────────────────────────────────────────────────────────────────
# 5. COMPREHENSIVE NUTRITION TABLE
# ─────────────────────────────────────────────────────────────────────────────
class NutritionFacts(Base):
    __tablename__ = "nutrition_facts"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False, index=True)
    serving_size_g = Column(Float, default=100.0)
    edible_part = Column(String, nullable=True)         # Fruit, Leaf, Root, Seed, Stem, Flower

    # Macronutrients (per 100g)
    calories_kcal = Column(Float, nullable=True)
    water_g = Column(Float, nullable=True)
    protein_g = Column(Float, nullable=True)
    fat_total_g = Column(Float, nullable=True)
    fat_saturated_g = Column(Float, nullable=True)
    fat_monounsaturated_g = Column(Float, nullable=True)
    fat_polyunsaturated_g = Column(Float, nullable=True)
    carbohydrates_g = Column(Float, nullable=True)
    dietary_fiber_g = Column(Float, nullable=True)
    sugars_g = Column(Float, nullable=True)
    starch_g = Column(Float, nullable=True)

    # Fat-Soluble Vitamins
    vitamin_a_iu = Column(Float, nullable=True)
    beta_carotene_mcg = Column(Float, nullable=True)
    vitamin_d_mcg = Column(Float, nullable=True)
    vitamin_e_mg = Column(Float, nullable=True)
    vitamin_k_mcg = Column(Float, nullable=True)

    # Water-Soluble Vitamins
    vitamin_b1_thiamine_mg = Column(Float, nullable=True)
    vitamin_b2_riboflavin_mg = Column(Float, nullable=True)
    vitamin_b3_niacin_mg = Column(Float, nullable=True)
    vitamin_b5_pantothenic_mg = Column(Float, nullable=True)
    vitamin_b6_mg = Column(Float, nullable=True)
    vitamin_b7_biotin_mcg = Column(Float, nullable=True)
    vitamin_b9_folate_mcg = Column(Float, nullable=True)
    vitamin_b12_mcg = Column(Float, nullable=True)
    vitamin_c_mg = Column(Float, nullable=True)

    # Minerals
    calcium_mg = Column(Float, nullable=True)
    iron_mg = Column(Float, nullable=True)
    magnesium_mg = Column(Float, nullable=True)
    phosphorus_mg = Column(Float, nullable=True)
    potassium_mg = Column(Float, nullable=True)
    sodium_mg = Column(Float, nullable=True)
    zinc_mg = Column(Float, nullable=True)
    copper_mg = Column(Float, nullable=True)
    manganese_mg = Column(Float, nullable=True)
    selenium_mcg = Column(Float, nullable=True)
    fluoride_mg = Column(Float, nullable=True)
    chromium_mcg = Column(Float, nullable=True)

    # Phytochemicals
    lycopene_mcg = Column(Float, nullable=True)
    lutein_zeaxanthin_mcg = Column(Float, nullable=True)
    anthocyanins_mg = Column(Float, nullable=True)
    flavonoids_mg = Column(Float, nullable=True)
    polyphenols_mg = Column(Float, nullable=True)
    tannins_mg = Column(Float, nullable=True)
    saponins_mg = Column(Float, nullable=True)

    # Special compounds
    omega3_g = Column(Float, nullable=True)
    omega6_g = Column(Float, nullable=True)
    glycemic_index = Column(Integer, nullable=True)
    antioxidant_capacity_orac = Column(Float, nullable=True)

    data_source = Column(String, nullable=True)         # USDA FDC, IFCT, etc.


# ─────────────────────────────────────────────────────────────────────────────
# 6. MEDICINAL KNOWLEDGE TABLE
# ─────────────────────────────────────────────────────────────────────────────
class MedicinalKnowledge(Base):
    __tablename__ = "medicinal_knowledge"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False, index=True)

    # Medicinal Systems
    ayurvedic_name = Column(String, nullable=True)
    ayurvedic_rasa = Column(String, nullable=True)       # Taste: Sweet, Sour, Salty, Pungent, Bitter, Astringent
    ayurvedic_guna = Column(String, nullable=True)       # Property: Light, Heavy, Dry, Oily...
    ayurvedic_virya = Column(String, nullable=True)      # Potency: Hot, Cold
    ayurvedic_vipaka = Column(String, nullable=True)     # Post-digestive taste
    ayurvedic_dosha = Column(String, nullable=True)      # Vata, Pitta, Kapha balancing
    ayurvedic_uses = Column(Text, nullable=True)

    tcm_name = Column(String, nullable=True)             # Traditional Chinese Medicine name
    tcm_nature = Column(String, nullable=True)           # Hot, Warm, Neutral, Cool, Cold
    tcm_flavor = Column(String, nullable=True)           # Bitter, Sweet, Sour, Pungent, Salty
    tcm_meridian = Column(String, nullable=True)         # Target organ meridians
    tcm_uses = Column(Text, nullable=True)

    unani_name = Column(String, nullable=True)
    unani_uses = Column(Text, nullable=True)

    western_herbal_uses = Column(Text, nullable=True)    # European Pharmacopoeia
    folk_medicine_uses = Column(Text, nullable=True)

    # Modern Pharmacology
    pharmacological_actions = Column(Text, nullable=True) # Antimicrobial, Antioxidant, etc.
    clinical_studies_summary = Column(Text, nullable=True)
    health_benefits = Column(Text, nullable=True)

    # Safety
    contraindications = Column(Text, nullable=True)
    drug_interactions = Column(Text, nullable=True)
    side_effects = Column(Text, nullable=True)
    toxicity_level = Column(String, nullable=True)       # None, Low, Moderate, High
    ld50 = Column(String, nullable=True)                 # Lethal dose in animal studies
    safe_dosage = Column(Text, nullable=True)
    pregnancy_safety = Column(String, nullable=True)     # Safe, Avoid, Consult Doctor

    # Medicinal parts
    medicinal_parts_used = Column(Text, nullable=True)   # Root, Bark, Leaf, Flower, Seed, etc.
    preparation_methods = Column(Text, nullable=True)    # Decoction, Tincture, Powder, Oil

    research_references = Column(Text, nullable=True)    # PubMed DOIs


# ─────────────────────────────────────────────────────────────────────────────
# 7. BIOACTIVE COMPOUNDS TABLE
# ─────────────────────────────────────────────────────────────────────────────
class BioactiveCompound(Base):
    __tablename__ = "bioactive_compounds"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False, index=True)
    compound_name = Column(String, nullable=False)
    compound_class = Column(String, nullable=True)       # Alkaloid, Terpenoid, Flavonoid, Glycoside, etc.
    cas_number = Column(String, nullable=True)
    molecular_formula = Column(String, nullable=True)
    concentration = Column(String, nullable=True)        # e.g., "2-5 mg/100g"
    plant_part = Column(String, nullable=True)           # Where it's found
    biological_activity = Column(Text, nullable=True)
    mode_of_action = Column(Text, nullable=True)


# ─────────────────────────────────────────────────────────────────────────────
# 8. GEOGRAPHIC DISTRIBUTION TABLE
# ─────────────────────────────────────────────────────────────────────────────
class GeographicDistribution(Base):
    __tablename__ = "geographic_distribution"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False, index=True)

    native_country = Column(String, nullable=True)
    native_region = Column(String, nullable=True)
    native_continent = Column(String, nullable=True)
    native_biome = Column(String, nullable=True)         # Tropical Rainforest, Savanna, etc.

    # Global distribution
    distribution_countries = Column(Text, nullable=True) # Comma-separated list
    distribution_continents = Column(Text, nullable=True)
    introduced_countries = Column(Text, nullable=True)   # Where it's been introduced

    # Geographic coordinates of native range
    latitude_range = Column(String, nullable=True)       # "23°S - 23°N"
    longitude_range = Column(String, nullable=True)
    elevation_range_m = Column(String, nullable=True)

    # Classification systems
    usda_hardiness_zones = Column(String, nullable=True) # "7-11"
    koppen_climate = Column(String, nullable=True)        # Af, Am, As, Aw, etc.
    fao_ecozones = Column(String, nullable=True)
    iucn_habitat = Column(String, nullable=True)

    # India-specific
    india_states = Column(Text, nullable=True)
    india_districts = Column(Text, nullable=True)
    india_agroclimatic_zone = Column(String, nullable=True)


# ─────────────────────────────────────────────────────────────────────────────
# 9. ECOLOGICAL DATA TABLE
# ─────────────────────────────────────────────────────────────────────────────
class EcologicalData(Base):
    __tablename__ = "ecological_data"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False, index=True)

    # Pollination
    pollinator_type = Column(String, nullable=True)      # Wind, Bee, Butterfly, Bat, Self, etc.
    pollinators = Column(Text, nullable=True)
    pollination_season = Column(String, nullable=True)
    cross_pollination_required = Column(Boolean, default=False)

    # Relationships
    companion_plants = Column(Text, nullable=True)
    allelopathic_plants = Column(Text, nullable=True)    # Plants it inhibits
    host_plants = Column(Text, nullable=True)            # For parasitic plants
    mycorrhizal_association = Column(Text, nullable=True)
    nitrogen_fixing = Column(Boolean, default=False)
    nitrogen_fixation_kg_per_ha = Column(Float, nullable=True)

    # Ecosystem services
    carbon_sequestration_t_per_ha = Column(Float, nullable=True)
    soil_erosion_control = Column(Boolean, default=False)
    windbreak_value = Column(Boolean, default=False)
    wildlife_habitat = Column(Text, nullable=True)
    biodiversity_importance = Column(Text, nullable=True)

    # Conservation
    iucn_status = Column(String, nullable=True)          # LC, NT, VU, EN, CR, EW, EX
    iucn_criteria = Column(String, nullable=True)
    population_trend = Column(String, nullable=True)     # Increasing, Stable, Decreasing, Unknown
    threats = Column(Text, nullable=True)
    conservation_actions = Column(Text, nullable=True)
    invasive_status = Column(String, nullable=True)      # Invasive, Potentially Invasive, Non-invasive


# ─────────────────────────────────────────────────────────────────────────────
# 10. RESEARCH REFERENCES TABLE
# ─────────────────────────────────────────────────────────────────────────────
class ResearchReference(Base):
    __tablename__ = "research_references"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=True, index=True)
    disease_id = Column(Integer, ForeignKey("diseases.id"), nullable=True)

    title = Column(Text, nullable=False)
    authors = Column(Text, nullable=True)
    journal = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    volume = Column(String, nullable=True)
    pages = Column(String, nullable=True)
    doi = Column(String, nullable=True)
    pubmed_id = Column(String, nullable=True)
    abstract = Column(Text, nullable=True)
    research_type = Column(String, nullable=True)        # Field Study, Lab Study, Review, Meta-analysis
    database_source = Column(String, nullable=True)      # PubMed, CABI, FAO, Kew, WFO


# ─────────────────────────────────────────────────────────────────────────────
# 11. RAG EMBEDDINGS TABLE (Offline Vector Store)
# ─────────────────────────────────────────────────────────────────────────────
class RagEmbedding(Base):
    __tablename__ = "rag_embeddings"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=True, index=True)
    chunk_type = Column(String, nullable=False)          # plant_profile, disease, pest, medicinal, cultivation
    chunk_text = Column(Text, nullable=False)            # The actual text chunk for RAG
    tfidf_vector = Column(Text, nullable=True)           # JSON-serialized sparse TF-IDF vector
    bm25_terms = Column(Text, nullable=True)             # JSON-serialized BM25 term weights
    keywords = Column(Text, nullable=True)               # Comma-separated key terms for fast matching
    language = Column(String, default="en")


# ─────────────────────────────────────────────────────────────────────────────
# 12. IMAGE METADATA TABLE (Offline Catalogue)
# ─────────────────────────────────────────────────────────────────────────────
class ImageMetadata(Base):
    __tablename__ = "image_metadata"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=True, index=True)
    disease_id = Column(Integer, ForeignKey("diseases.id"), nullable=True)
    pest_id = Column(Integer, ForeignKey("pests.id"), nullable=True)

    category = Column(String, nullable=False)            # Leaf, Flower, Fruit, Seed, Stem, Bark, Root, Disease, Pest
    subcategory = Column(String, nullable=True)          # Young, Mature, Old, Early-stage, Late-stage
    health_status = Column(String, default="Healthy")    # Healthy, Diseased, Deficient, Pest-Damaged
    local_path = Column(String, nullable=True)           # Relative local file path
    filename = Column(String, nullable=True)
    resolution = Column(String, nullable=True)           # "1920x1080"
    file_size_kb = Column(Integer, nullable=True)
    format = Column(String, nullable=True)               # JPG, PNG, TIFF
    description = Column(Text, nullable=True)
    bounding_box = Column(Text, nullable=True)           # JSON: {x, y, w, h}
    labels = Column(Text, nullable=True)                 # Comma-separated class labels for ML
    data_source = Column(String, nullable=True)          # PlantVillage, iNaturalist, Kew, etc.
    license = Column(String, nullable=True)


# ─────────────────────────────────────────────────────────────────────────────
# 13. CROP CALENDAR TABLE
# ─────────────────────────────────────────────────────────────────────────────
class CropCalendar(Base):
    __tablename__ = "crop_calendars"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False, index=True)
    region = Column(String, nullable=True)               # North India, South India, USA-Midwest, etc.
    climate_zone = Column(String, nullable=True)
    season_name = Column(String, nullable=True)          # Kharif, Rabi, Zaid, Spring, Summer, Fall, Winter

    # Month-by-month calendar (1 = yes, 0 = no)
    jan = Column(String, nullable=True)                  # Activity in January
    feb = Column(String, nullable=True)
    mar = Column(String, nullable=True)
    apr = Column(String, nullable=True)
    may = Column(String, nullable=True)
    jun = Column(String, nullable=True)
    jul = Column(String, nullable=True)
    aug = Column(String, nullable=True)
    sep = Column(String, nullable=True)
    oct = Column(String, nullable=True)
    nov = Column(String, nullable=True)
    dec = Column(String, nullable=True)

    sowing_months = Column(String, nullable=True)        # "June-July"
    transplanting_months = Column(String, nullable=True)
    harvesting_months = Column(String, nullable=True)
    total_duration_days = Column(Integer, nullable=True)
    notes = Column(Text, nullable=True)


# ─────────────────────────────────────────────────────────────────────────────
# 14. COMPANION PLANTING TABLE
# ─────────────────────────────────────────────────────────────────────────────
class CompanionPlanting(Base):
    __tablename__ = "companion_planting"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False, index=True)
    companion_plant_name = Column(String, nullable=False)
    companion_plant_id = Column(Integer, ForeignKey("plants.id"), nullable=True)
    relationship_type = Column(String, nullable=False)   # Beneficial, Antagonistic, Neutral
    benefit_description = Column(Text, nullable=True)
    mechanism = Column(Text, nullable=True)              # How the relationship works


# ─────────────────────────────────────────────────────────────────────────────
# 15. AGRONOMIC PRACTICES TABLE
# ─────────────────────────────────────────────────────────────────────────────
class AgronomicPractice(Base):
    __tablename__ = "agronomic_practices"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False, index=True)

    # Land Preparation
    land_preparation = Column(Text, nullable=True)
    tillage_type = Column(String, nullable=True)         # Deep Ploughing, Minimal Tillage, No-till
    field_leveling = Column(Text, nullable=True)

    # Planting
    planting_method = Column(String, nullable=True)      # Direct Seeding, Transplanting, Dibbling
    plant_spacing_cm = Column(String, nullable=True)     # "60x30 cm"
    row_spacing_cm = Column(Float, nullable=True)
    plant_spacing_cm_within = Column(Float, nullable=True)
    planting_density_per_ha = Column(Integer, nullable=True)
    planting_depth_cm = Column(Float, nullable=True)

    # Crop Management
    thinning = Column(Text, nullable=True)
    mulching = Column(Text, nullable=True)
    staking_trellising = Column(Text, nullable=True)
    pruning_schedule = Column(Text, nullable=True)
    training_system = Column(Text, nullable=True)        # Bush, Cordon, Espalier
    intercropping = Column(Text, nullable=True)
    crop_rotation_years = Column(Integer, nullable=True)
    rotation_crops = Column(Text, nullable=True)         # What to rotate with

    # Weed Management
    critical_weed_free_period_days = Column(Integer, nullable=True)
    common_weeds = Column(Text, nullable=True)
    herbicide_schedule = Column(Text, nullable=True)
    organic_weed_management = Column(Text, nullable=True)

    # Harvesting
    maturity_indices = Column(Text, nullable=True)
    harvest_index = Column(Float, nullable=True)         # Grain weight / Total dry matter
    expected_yield_t_per_ha = Column(String, nullable=True)
    harvest_losses_pct = Column(Float, nullable=True)

    # Post-Harvest
    grading_standards = Column(Text, nullable=True)
    packaging_method = Column(Text, nullable=True)
    transport_conditions = Column(Text, Column)
    cold_chain_temp_c = Column(Float, nullable=True)
    controlled_atmosphere = Column(Text, nullable=True)  # CA storage gas composition
    shelf_life_days = Column(Integer, nullable=True)
    value_added_products = Column(Text, nullable=True)
