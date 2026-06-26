import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    address = Column(Text, nullable=True)
    farm_size = Column(String, nullable=True)  # e.g., "5 Acres"
    state = Column(String, nullable=True)
    district = Column(String, nullable=True)
    village = Column(String, nullable=True)
    crop_types = Column(String, nullable=True) # comma separated values
    profile_photo = Column(Text, nullable=True) # Base64 or local URL
    role = Column(String, default="Farmer") # Farmer, Expert, Admin
    registration_date = Column(DateTime, default=datetime.datetime.utcnow)
    last_login = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    detections = relationship("CropDetection", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
    history_logs = relationship("CropHistory", back_populates="user", cascade="all, delete-orphan")
    audit_logs = relationship("AuditLog", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")

class CropDetection(Base):
    __tablename__ = "crop_detections"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    crop_name = Column(String, nullable=False)
    scientific_name = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    detection_time = Column(DateTime, default=datetime.datetime.utcnow)
    image_path = Column(String, nullable=True)
    
    # Advanced metrics
    health_score = Column(Integer, default=100)
    severity = Column(String, default="Low") # Healthy, Low, Medium, High, Critical
    leaf_quality = Column(String, default="Good") # Good, Fair, Damaged
    spots_count = Column(Integer, default=0)
    recovery_score = Column(Integer, default=100)
    bounding_box = Column(Text, nullable=True) # JSON string of coordinates: [x,y,w,h]
    heatmap_path = Column(String, nullable=True) # Path to Grad-CAM overlay

    # Relationships
    user = relationship("User", back_populates="detections")
    diseases = relationship("DiseaseDetection", back_populates="detection", cascade="all, delete-orphan")

class DiseaseDetection(Base):
    __tablename__ = "disease_detections"

    id = Column(Integer, primary_key=True, index=True)
    crop_detection_id = Column(Integer, ForeignKey("crop_detections.id"), nullable=False)
    disease_name = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    severity = Column(String, default="Low")
    stage = Column(String, default="Early") # Early, Middle, Late
    affected_area_percentage = Column(Float, default=0.0)
    cause = Column(Text, nullable=True)
    organic_treatment = Column(Text, nullable=True)
    chemical_treatment = Column(Text, nullable=True)
    prevention = Column(Text, nullable=True)

    # Relationships
    detection = relationship("CropDetection", back_populates="diseases")

class CropHistory(Base):
    __tablename__ = "crop_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    action = Column(String, nullable=False) # e.g. "Scanned Rose", "Purchased seeds"
    description = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="history_logs")

class KnowledgeBase(Base):
    __tablename__ = "knowledge_base"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    chunk_index = Column(Integer, default=0)
    document_type = Column(String, default="Book") # Book, Research Paper, Manual, Guide
    source = Column(String, nullable=True)
    embedding = Column(Text, nullable=True) # JSON representation of floats

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False) # Organic, Seeds, Fertilizer, Insecticide, Pesticide
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    usage = Column(Text, nullable=False)
    image = Column(String, nullable=False)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    invoice_number = Column(String, unique=True, nullable=False)
    tracking_number = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default="Processing") # Processing, Shipped, Delivered
    items = Column(Text, nullable=False) # JSON representation of ordered items

    user = relationship("User", back_populates="orders")

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    action = Column(String, nullable=False)
    details = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="audit_logs")

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="notifications")

class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, index=True)
    common_name = Column(String, unique=True, index=True, nullable=False)
    botanical_name = Column(String, unique=True, index=True, nullable=False)
    synonyms = Column(String, nullable=True) # Comma separated
    local_names = Column(String, nullable=True) # Comma separated
    family_id = Column(Integer, ForeignKey("families.id"), nullable=True)
    genus_id = Column(Integer, ForeignKey("genera.id"), nullable=True)
    species_id = Column(Integer, ForeignKey("species_records.id"), nullable=True)
    plant_authority = Column(String, nullable=True)
    overview = Column(Text, nullable=True)
    morphology = Column(Text, nullable=True)
    leaf_desc = Column(Text, nullable=True)
    flower_desc = Column(Text, nullable=True)
    fruit_desc = Column(Text, nullable=True)
    seed_desc = Column(Text, nullable=True)
    stem_desc = Column(Text, nullable=True)
    root_desc = Column(Text, nullable=True)
    growth_habit = Column(String, nullable=True)
    life_cycle = Column(String, nullable=True) # Annual, Perennial, Biennial
    average_height = Column(String, nullable=True)
    average_width = Column(String, nullable=True)
    lifespan = Column(String, nullable=True)
    category = Column(String, nullable=True) # Fruit, Vegetable, Spice, Ornamental...
    commercial_uses = Column(Text, nullable=True)
    medicinal_uses = Column(Text, nullable=True)
    industrial_uses = Column(Text, nullable=True)
    food_uses = Column(Text, nullable=True)
    toxicity = Column(Text, nullable=True)
    conservation_status = Column(String, default="Least Concern")

    # Relationships
    classification = relationship("BotanicalClassification", uselist=False, back_populates="plant", cascade="all, delete-orphan")
    family = relationship("Family", back_populates="plants")
    genus = relationship("Genus", back_populates="plants")
    species_rec = relationship("SpeciesRecord", back_populates="plants")
    varieties = relationship("Variety", back_populates="plant", cascade="all, delete-orphan")
    diseases_list = relationship("Disease", back_populates="plant", cascade="all, delete-orphan")
    pests_list = relationship("Pest", back_populates="plant", cascade="all, delete-orphan")
    nutrient_deficiencies = relationship("NutrientDeficiency", back_populates="plant", cascade="all, delete-orphan")
    climate = relationship("ClimateRequirement", uselist=False, back_populates="plant", cascade="all, delete-orphan")
    soil = relationship("SoilRequirement", uselist=False, back_populates="plant", cascade="all, delete-orphan")
    irrigation = relationship("IrrigationSchedule", uselist=False, back_populates="plant", cascade="all, delete-orphan")
    harvest = relationship("HarvestInformation", uselist=False, back_populates="plant", cascade="all, delete-orphan")
    growth_stages = relationship("GrowthStage", back_populates="plant", cascade="all, delete-orphan")
    plant_images = relationship("PlantImage", back_populates="plant", cascade="all, delete-orphan")
    bookmarks = relationship("UserBookmark", back_populates="plant", cascade="all, delete-orphan")
    notes = relationship("Note", back_populates="plant", cascade="all, delete-orphan")

class BotanicalClassification(Base):
    __tablename__ = "botanical_classifications"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    kingdom = Column(String, default="Plantae")
    division = Column(String, nullable=True)
    class_name = Column(String, nullable=True)
    order_name = Column(String, nullable=True)
    taxonomy_hierarchy = Column(Text, nullable=True)

    plant = relationship("Plant", back_populates="classification")

class Family(Base):
    __tablename__ = "families"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)

    plants = relationship("Plant", back_populates="family")

class Genus(Base):
    __tablename__ = "genera"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)

    plants = relationship("Plant", back_populates="genus")

class SpeciesRecord(Base):
    __tablename__ = "species_records"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False) # e.g. "lycopersicum"
    description = Column(Text, nullable=True)

    plants = relationship("Plant", back_populates="species_rec")

class Variety(Base):
    __tablename__ = "varieties"
    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    name = Column(String, nullable=False)
    variety_type = Column(String, nullable=True) # Hybrid, Heirloom, Commercial
    growing_period = Column(String, nullable=True)
    yield_potential = Column(String, nullable=True)

    plant = relationship("Plant", back_populates="varieties")

class ClimateRequirement(Base):
    __tablename__ = "climate_requirements"
    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    native_region = Column(String, nullable=True)
    countries_grown = Column(Text, nullable=True) # Comma separated
    climatic_zones = Column(String, nullable=True)
    suitable_altitude = Column(String, nullable=True)
    rainfall_requirement = Column(String, nullable=True)
    temperature_requirement = Column(String, nullable=True)
    humidity_requirement = Column(String, nullable=True)

    plant = relationship("Plant", back_populates="climate")

class SoilRequirement(Base):
    __tablename__ = "soil_requirements"
    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    preferred_soil = Column(String, nullable=True)
    soil_ph_range = Column(String, nullable=True)
    drainage = Column(String, nullable=True)
    organic_matter = Column(String, nullable=True)
    fertility = Column(String, nullable=True)
    texture = Column(String, nullable=True)

    plant = relationship("Plant", back_populates="soil")

class Disease(Base):
    __tablename__ = "diseases"
    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    name = Column(String, nullable=False)
    pathogen_name = Column(String, nullable=True)
    disease_type = Column(String, nullable=True) # Fungal, Bacterial, Viral, Pest, Deficiency
    risk_level = Column(String, default="Medium") # Low, Medium, High, Critical
    economic_impact = Column(Text, nullable=True)

    plant = relationship("Plant", back_populates="diseases_list")
    symptoms = relationship("DiseaseSymptom", back_populates="disease", cascade="all, delete-orphan")
    treatments = relationship("DiseaseTreatment", back_populates="disease", cascade="all, delete-orphan")

class DiseaseSymptom(Base):
    __tablename__ = "disease_symptoms"
    id = Column(Integer, primary_key=True, index=True)
    disease_id = Column(Integer, ForeignKey("diseases.id"), nullable=False)
    early_symptoms = Column(Text, nullable=True)
    late_symptoms = Column(Text, nullable=True)
    affected_parts = Column(String, nullable=True)

    disease = relationship("Disease", back_populates="symptoms")

class DiseaseTreatment(Base):
    __tablename__ = "disease_treatments"
    id = Column(Integer, primary_key=True, index=True)
    disease_id = Column(Integer, ForeignKey("diseases.id"), nullable=False)
    immediate_treatment = Column(Text, nullable=True)
    organic_treatment = Column(Text, nullable=True)
    chemical_treatment = Column(Text, nullable=True)
    biological_control = Column(Text, nullable=True)
    recommended_fungicides = Column(String, nullable=True)
    recommended_organic_solutions = Column(String, nullable=True)
    dosage = Column(String, nullable=True)
    application_frequency = Column(String, nullable=True)
    safety_precautions = Column(Text, nullable=True)
    recovery_time = Column(String, nullable=True)

    disease = relationship("Disease", back_populates="treatments")

class Pest(Base):
    __tablename__ = "pests"
    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    name = Column(String, nullable=False)
    scientific_name = Column(String, nullable=True)
    identification = Column(Text, nullable=True)
    damage_symptoms = Column(Text, nullable=True)
    lifecycle = Column(Text, nullable=True)
    organic_control = Column(Text, nullable=True)
    chemical_control = Column(Text, nullable=True)
    biological_control = Column(Text, nullable=True)
    economic_threshold = Column(String, nullable=True)

    plant = relationship("Plant", back_populates="pests_list")

class NutrientDeficiency(Base):
    __tablename__ = "nutrient_deficiencies"
    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    nutrient_name = Column(String, nullable=False) # Nitrogen, Phosphorus, Potassium, Iron, etc.
    symptoms = Column(Text, nullable=False)
    correction_methods = Column(Text, nullable=True)
    recommended_fertilizers = Column(String, nullable=True)

    plant = relationship("Plant", back_populates="nutrient_deficiencies")

class FertilizerRecommendation(Base):
    __tablename__ = "fertilizer_recommendations"
    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    organic_fertilizers = Column(Text, nullable=True)
    chemical_fertilizers = Column(Text, nullable=True)
    npk_ratio = Column(String, nullable=True)
    application_timing = Column(String, nullable=True)
    application_qty = Column(String, nullable=True)

class IrrigationSchedule(Base):
    __tablename__ = "irrigation_schedules"
    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    water_requirement = Column(String, nullable=True)
    daily_water_need = Column(String, nullable=True)
    weekly_water_need = Column(String, nullable=True)
    drip_recommendation = Column(Text, nullable=True)
    critical_stages = Column(Text, nullable=True)

    plant = relationship("Plant", back_populates="irrigation")

class HarvestInformation(Base):
    __tablename__ = "harvest_information"
    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    harvest_indicators = Column(Text, nullable=True)
    harvest_time = Column(String, nullable=True)
    harvest_method = Column(Text, nullable=True)
    post_harvest_handling = Column(Text, nullable=True)
    storage_temp = Column(String, nullable=True)
    shelf_life = Column(String, nullable=True)

    plant = relationship("Plant", back_populates="harvest")

class GrowthStage(Base):
    __tablename__ = "growth_stages"
    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    duration_days = Column(Integer, nullable=True)

    plant = relationship("Plant", back_populates="growth_stages")

class PlantImage(Base):
    __tablename__ = "plant_images"
    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    category = Column(String, nullable=False) # Leaf, Flower, Fruit, Seed, Stem, Root, Entire
    url = Column(String, nullable=False)
    bounding_box = Column(Text, nullable=True) # JSON coordinates

    plant = relationship("Plant", back_populates="plant_images")

class KnowledgeBaseDocument(Base):
    __tablename__ = "knowledge_base_documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    document_type = Column(String, nullable=True)
    source = Column(String, nullable=True)

class UserBookmark(Base):
    __tablename__ = "user_bookmarks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    plant = relationship("Plant", back_populates="bookmarks")

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    plant = relationship("Plant", back_populates="notes")

