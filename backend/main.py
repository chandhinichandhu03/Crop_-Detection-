import os
import shutil
import json
import datetime
from typing import Optional, List
from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import engine, get_db, Base
from models import (
    User, CropDetection, DiseaseDetection, CropHistory, KnowledgeBase, Product, Order, AuditLog, Notification,
    Plant, BotanicalClassification, Family, Genus, SpeciesRecord, Variety, ClimateRequirement, SoilRequirement,
    Disease, DiseaseSymptom, DiseaseTreatment, Pest, NutrientDeficiency, FertilizerRecommendation,
    IrrigationSchedule, HarvestInformation, GrowthStage, PlantImage, KnowledgeBaseDocument, UserBookmark, Note
)
from auth import hash_password, verify_password, create_access_token, get_current_user, RoleChecker
from ai_model import analyze_crop_image, CROP_DATASET
from rag import search_knowledge_base, build_rag_index

# Initialize FastAPI App
app = FastAPI(title="Agro Doctor Unified Backend", version="2.0.0")

# Enable CORS for Next.js frontend on port 3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure database tables exist
Base.metadata.create_all(bind=engine)

# Prepopulate database with default admin user and products on start
def prepopulate_db():
    db = next(get_db())
    # 1. Create Default Admin User
    admin_user = db.query(User).filter(User.email == "admin@agro.com").first()
    if not admin_user:
        admin = User(
            name="Agro Admin",
            email="admin@agro.com",
            password_hash=hash_password("agro123"),
            phone="9876543210",
            address="National Agro HQ, New Delhi",
            farm_size="10 Acres",
            state="Delhi",
            district="New Delhi",
            village="HQ Village",
            crop_types="Tomato, Potato, Wheat, Rice",
            role="Admin"
        )
        db.add(admin)
        db.commit()

    # Also check generic 'admin' username mapping for easy UI logging
    ui_admin = db.query(User).filter(User.email == "admin").first()
    if not ui_admin:
        u_admin = User(
            name="System Administrator",
            email="admin",
            password_hash=hash_password("agro123"),
            role="Admin"
        )
        db.add(u_admin)
        db.commit()

    # 2. Create Default Products
    if db.query(Product).count() == 0:
        default_products = [
            {
                "id": 1,
                "name": "Organic Pesticide (Neem Extract)",
                "category": "Organic",
                "price": 450.0,
                "description": "Pure biological pesticide derived from organic neem tree extracts, highly effective against sucking pests, thrips, and whiteflies.",
                "usage": "Mix 5ml with 1 Liter of water. Spray on crop foliage early mornings or late evenings when pests are active.",
                "image": "https://images.unsplash.com/photo-1592982537447-7440770cbfc9?auto=format&fit=crop&q=80&w=800&h=800"
            },
            {
                "id": 2,
                "name": "Hybrid Disease-Resistant Tomato Seeds",
                "category": "Seeds",
                "price": 850.0,
                "description": "Premium F1 hybrid tomato seeds bred for outstanding resistance to early/late blights and leaf spot diseases. Yields uniform, robust tomatoes.",
                "usage": "Sow 1/4 inch deep in seed starting trays. Water daily and transplant outdoors after 25 days into well-drained soil.",
                "image": "https://images.unsplash.com/photo-1542332213-9b5a5a3fad35?auto=format&fit=crop&q=80&w=800&h=800"
            },
            {
                "id": 3,
                "name": "Cold-Pressed Neem Oil Spray",
                "category": "Organic",
                "price": 200.0,
                "description": "Natural triple-action insecticide, fungicide, and miticide for organic gardening. Prevents powdery mildew, rust, and leaf spots.",
                "usage": "Mix 4ml of neem oil and 1ml of liquid dish soap in 1 Liter of warm water. Spray entire plant surface once every 14 days.",
                "image": "https://images.unsplash.com/photo-1628352081506-83c43123ed6d?auto=format&fit=crop&q=80&w=800&h=800"
            },
            {
                "id": 4,
                "name": "NPK 19-19-19 Soluble Fertilizer",
                "category": "Fertilizer",
                "price": 350.0,
                "description": "Balanced mineral plant food containing 19% Nitrogen, 19% Phosphorus, and 19% Potassium. Dissolves completely in water for root drenching.",
                "usage": "Mix 5 grams in 2 Liters of water. Apply around root zones once every 15 days during vegetative growth.",
                "image": "https://images.unsplash.com/photo-1581093191140-5e6402ec9f44?auto=format&fit=crop&q=80&w=800&h=800"
            },
            {
                "id": 5,
                "name": "Bio-Fertilizer (Blue Green Algae)",
                "category": "Fertilizer",
                "price": 150.0,
                "description": "All-natural cyanobacteria bio-fertilizer that fixes atmospheric nitrogen in rice paddies and moisture-rich soils, improving organic content.",
                "usage": "Apply 10kg per acre uniformly in standing water fields 7-10 days after transplanting crop seedlings.",
                "image": "https://images.unsplash.com/photo-1589923188900-85dae523342b?auto=format&fit=crop&q=80&w=800&h=800"
            },
            {
                "id": 6,
                "name": "Sonamasuri Premium Paddy Seeds",
                "category": "Seeds",
                "price": 1200.0,
                "description": "Certified fine grain variety paddy seeds. High germination rate, medium maturity duration, and excellent cooking quality.",
                "usage": "Soak seeds in water for 24 hours. Sow in nursery beds. Transplant 25-day old seedlings with 3-4 leaves to main field.",
                "image": "https://images.unsplash.com/photo-1543157148-f819d161763f?auto=format&fit=crop&q=80&w=800&h=800"
            },
            {
                "id": 7,
                "name": "Trichoderma Viride Bio-Fungicide",
                "category": "Organic",
                "price": 280.0,
                "description": "Biological control agent highly effective against root rots, wilts, damping off, and other soil-borne fungal pathogens.",
                "usage": "Soil treatment: Mix 1kg with 50kg farmyard manure and apply to soil. Seed treatment: Mix 10g per kg of seeds.",
                "image": "https://images.unsplash.com/photo-1595273670150-bd0c3c392e46?auto=format&fit=crop&q=80&w=800&h=800"
            },
            {
                "id": 8,
                "name": "Systemic Insecticide (Acephate)",
                "category": "Insecticide",
                "price": 550.0,
                "description": "Broad spectrum systemic insecticide for effective control of chewing and sucking insect pests including stem borers, aphids, and jassids.",
                "usage": "Dissolve 2 grams per Liter of clean water. Spray thoroughly on crop foliage. Repeat if pest threshold rises.",
                "image": "https://images.unsplash.com/photo-1585314062340-f1a5a7c9328d?auto=format&fit=crop&q=80&w=800&h=800"
            },
            {
                "id": 9,
                "name": "Broad-Spectrum Copper Fungicide",
                "category": "Pesticide",
                "price": 680.0,
                "description": "Protective copper fungicide controlling blight, anthracnose, downy mildew, leaf curl, and bacterial spots on leaves.",
                "usage": "Dilute 3 grams in 1 Liter of water. Spray on plant stems and leaf surfaces. Repeat every 10-14 days.",
                "image": "https://images.unsplash.com/photo-1605000797499-95a51c5269ae?auto=format&fit=crop&q=80&w=800&h=800"
            }
        ]
        for p in default_products:
            db_p = Product(**p)
            db.add(db_p)
        db.commit()

    # 2.5 Seed Botanical Encyclopedia (Huge dataset)
    if db.query(Plant).count() < 100000:
        print("🌱 Seeding huge botanical dataset...")
        from huge_seeder import seed_huge_dataset
        seed_huge_dataset(db)
    else:
        print("🌿 Huge botanical dataset already seeded in DB.")
    
    # 3. Populate RAG database initial docs
    build_rag_index(db)
    db.close()

prepopulate_db()

# --- ROUTES ---

@app.get("/")
def root():
    return {
        "status": "Ecosystem Online",
        "database": "SQLite Local Active",
        "engine": "FastAPI + OpenCV Image Pipeline"
    }

# 1. AUTHENTICATION ROUTING

@app.post("/api/auth/register")
def register(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    phone: Optional[str] = Form(None),
    address: Optional[str] = Form(None),
    farm_size: Optional[str] = Form(None),
    state: Optional[str] = Form(None),
    district: Optional[str] = Form(None),
    village: Optional[str] = Form(None),
    crop_types: Optional[str] = Form(None),
    role: Optional[str] = Form("Farmer"),
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email address already registered"
        )
    
    new_user = User(
        name=name,
        email=email,
        password_hash=hash_password(password),
        phone=phone,
        address=address,
        farm_size=farm_size,
        state=state,
        district=district,
        village=village,
        crop_types=crop_types,
        role=role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Log initial register
    log = AuditLog(user_id=new_user.id, action="Register", details=f"Farmer {new_user.name} joined.")
    db.add(log)
    
    # Send welcome notification
    notification = Notification(user_id=new_user.id, message=f"Welcome {new_user.name}! Your farming profile has been successfully configured.")
    db.add(notification)
    
    db.commit()
    
    token = create_access_token({"sub": new_user.email})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "role": new_user.role
        }
    }

@app.post("/api/auth/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email or password"
        )
    
    user.last_login = datetime.datetime.utcnow()
    db.commit()
    
    token = create_access_token({"sub": user.email})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }

@app.get("/api/auth/profile")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "phone": current_user.phone,
        "address": current_user.address,
        "farm_size": current_user.farm_size,
        "state": current_user.state,
        "district": current_user.district,
        "village": current_user.village,
        "crop_types": current_user.crop_types,
        "role": current_user.role,
        "registration_date": current_user.registration_date,
        "last_login": current_user.last_login
    }

@app.put("/api/auth/profile")
def update_profile(
    name: str = Form(...),
    phone: Optional[str] = Form(None),
    address: Optional[str] = Form(None),
    farm_size: Optional[str] = Form(None),
    state: Optional[str] = Form(None),
    district: Optional[str] = Form(None),
    village: Optional[str] = Form(None),
    crop_types: Optional[str] = Form(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    current_user.name = name
    current_user.phone = phone
    current_user.address = address
    current_user.farm_size = farm_size
    current_user.state = state
    current_user.district = district
    current_user.village = village
    current_user.crop_types = crop_types
    
    db.commit()
    return {"message": "Profile updated successfully"}

# 2. IMAGE PREDICTION & COMPUTER VISION

@app.post("/predict")
async def predict_crop_disease(
    file: UploadFile = File(...),
    token: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    # Attempt to resolve current user if token is present
    user = None
    if token:
        try:
            from .auth import SECRET_KEY, ALGORITHM
            import jwt
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email = payload.get("sub")
            user = db.query(User).filter(User.email == email).first()
        except Exception:
            pass

    # Read image contents
    image_bytes = await file.read()
    
    # Process image using local OpenCV/Pillow/PyTorch models
    cv_res = analyze_crop_image(image_bytes, file.filename)
    
    if "error" in cv_res and cv_res["error"]:
        return {"error": True, "message": cv_res["message"]}

    # Check for animal detection
    if "is_animal" in cv_res and cv_res["is_animal"]:
        return {
            "error": False,
            "is_animal": True,
            "detected_animal": cv_res["detected_animal"],
            "confidence": f"{cv_res['confidence_score']:.1%}",
            "message": "This image is not a plant."
        }

    # Check for unknown plant detection (low confidence < 70%)
    if "is_unknown" in cv_res and cv_res["is_unknown"]:
        top_preds = [
            {
                "name": p["name"],
                "scientific_name": p["scientific_name"],
                "confidence": f"{p['confidence']:.1%}"
            }
            for p in cv_res["top_predictions"]
        ]
        return {
            "error": False,
            "is_unknown": True,
            "crop": "Unknown Plant",
            "confidence": f"{cv_res['confidence_score']:.1%}",
            "top_predictions": top_preds,
            "message": "Please upload a clearer image."
        }

    # Retrieve Scientific knowledge context using offline RAG matrix
    rag_query = f"{cv_res['crop']} {cv_res['disease']} cause and organic treatments"
    rag_citations = search_knowledge_base(rag_query, db, limit=2)

    # Retrieve details from localized relational database if available
    plant_db = db.query(Plant).filter(Plant.common_name.ilike(cv_res["crop"])).first()
    db_disease_rec = None
    if plant_db:
        db_disease_rec = db.query(Disease).filter(
            Disease.plant_id == plant_db.id,
            Disease.name.ilike(cv_res["disease"])
        ).first()

    # Compile treatments description from database primarily, falling back to RAG
    cause = cv_res["location"]  # default
    organic_treatment = "Apply neem seed kernel extract organically."
    chemical_treatment = "Spray copper-based compounds."
    prevention = "Implement proper space ventilation and avoid overhead watering."

    if db_disease_rec:
        if db_disease_rec.symptoms:
            syms = db_disease_rec.symptoms[0]
            cause = f"Symptomatology: Early symptoms show {syms.early_symptoms}. Late stages progress to {syms.late_symptoms} on affected parts: {syms.affected_parts}."
        else:
            cause = f"Pathogenic condition matching {cv_res['disease']} on {cv_res['crop']}."
            
        if db_disease_rec.treatments:
            t = db_disease_rec.treatments[0]
            organic_treatment = t.organic_treatment or f"Apply organic solution: {t.recommended_organic_solutions or 'Neem Oil spray'}"
            chemical_treatment = t.chemical_treatment or f"Apply chemical fungicide: {t.recommended_fungicides or 'Copper Fungicide'}"
            prevention = f"Immediate treatment: {t.immediate_treatment}. Precautions: {t.safety_precautions}. Recovery period: {t.recovery_time}."
    elif rag_citations:
        matched_content = rag_citations[0]["content"]
        if "cause" in cv_res["disease"].lower() or "fungus" in matched_content.lower():
            cause = matched_content
        else:
            cause = f"Pathogenic condition matching {cv_res['disease']} on {cv_res['crop']}. " + matched_content[:150]
            
        organic_treatment = f"RAG Recommended Organic Cure: " + (
            "Spray baking soda and oil solution" if "mildew" in cv_res['disease'].lower() 
            else "Use neem oil (4-5ml/L) and remove infected leaves."
        )
        chemical_treatment = f"RAG Recommended Chemical Compound: " + (
            "Chlorothalonil or Mancozeb fungicide." if "blight" in cv_res['disease'].lower()
            else "Tricyclazole or copper oxychloride."
        )
        prevention = f"RAG Suggested Prevention: Keep crop rows aerated, rotate cultivars regularly, and maintain soil pH 6.0-7.0."

    # Save to history database if user is logged in
    db_detection = None
    if user:
        db_detection = CropDetection(
            user_id=user.id,
            crop_name=cv_res["crop"],
            scientific_name=cv_res["scientific_name"],
            confidence=cv_res["confidence_score"],
            health_score=cv_res["health_score"],
            severity=cv_res["severity"],
            leaf_quality=cv_res["leaf_quality"],
            spots_count=cv_res["spots_count"],
            recovery_score=cv_res["recovery_score"],
            bounding_box=json.dumps(cv_res["bounding_box"]),
            heatmap_path=cv_res["heatmap_overlay"]
        )
        db.add(db_detection)
        db.commit()
        db.refresh(db_detection)
        
        db_disease = DiseaseDetection(
            crop_detection_id=db_detection.id,
            disease_name=cv_res["disease"],
            confidence=cv_res["confidence_score"],
            severity=cv_res["severity"],
            stage="Early" if cv_res["severity"] in ["Healthy", "Low"] else "Middle",
            affected_area_percentage=cv_res["affected_area_percentage"],
            cause=cause,
            organic_treatment=organic_treatment,
            chemical_treatment=chemical_treatment,
            prevention=prevention
        )
        db.add(db_disease)
        
        history_log = CropHistory(
            user_id=user.id,
            action="Crop Scan",
            description=f"Diagnosed {cv_res['crop']} with {cv_res['disease']} ({cv_res['severity']} Severity)"
        )
        db.add(history_log)
        
        if cv_res["severity"] in ["High", "Critical"]:
            warn_noti = Notification(
                user_id=user.id,
                message=f"CRITICAL HEALTH WARNING: {cv_res['crop']} diagnosed with {cv_res['disease']} at {cv_res['severity']} severity levels!"
            )
            db.add(warn_noti)
            
        db.commit()

    # Format top predictions for response
    top_preds_formatted = [
        {
            "name": p["name"],
            "scientific_name": p["scientific_name"],
            "confidence": f"{p['confidence']:.1%}"
        }
        for p in cv_res.get("top_predictions", [])
    ]

    # Get alternative candidates for 70-90% confidence
    alternative_candidates = []
    if 0.70 <= cv_res["confidence_score"] < 0.90:
        alternative_candidates = top_preds_formatted[1:4]

    warning_message = None
    if 0.90 <= cv_res["confidence_score"] < 0.95:
        warning_message = "⚠️ Moderate confidence match. Please verify details."

    return {
        "crop": cv_res["crop"],
        "scientific_name": cv_res["scientific_name"],
        "season": cv_res["season"],
        "location": cv_res["location"],
        "disease": cv_res["disease"],
        "confidence": f"{cv_res['confidence_score']:.1%}",
        "confidence_value": cv_res["confidence_score"],
        "severity": cv_res["severity"],
        "affected_area_percentage": f"{cv_res['affected_area_percentage']}%",
        "health_score": cv_res["health_score"],
        "leaf_quality": cv_res["leaf_quality"],
        "spots_count": cv_res["spots_count"],
        "recovery_score": cv_res["recovery_score"],
        "bounding_box": cv_res["bounding_box"],
        "spots_boxes": cv_res["spots_boxes"],
        "visual_overlay": cv_res["visual_overlay"],
        "heatmap_overlay": cv_res["heatmap_overlay"],
        "cause": cause,
        "organic_remedy": organic_treatment,
        "chemical_remedy": chemical_treatment,
        "prevention": prevention,
        "rag_citations": rag_citations,
        "plant_id": plant_db.id if plant_db else None,
        "alternative_candidates": alternative_candidates,
        "warning": warning_message,
        "top_predictions": top_preds_formatted
    }


# 3. RAG OFFLINE CHATBOT

@app.post("/api/chat")
def chat_with_bot(
    message: str = Form(...),
    db: Session = Depends(get_db)
):
    # Perform RAG matching over user query
    citations = search_knowledge_base(message, db, limit=2)
    
    if citations:
        # Construct helpful response backed by citations
        top_cit = citations[0]
        bot_response = f"According to local knowledge bulletin '{top_cit['title']}' ({top_cit['source']}):\n\n{top_cit['content']}\n\n[Similarity Match: {top_cit['similarity_score']}]"
    else:
        bot_response = "I did not find a direct citation in our offline agricultural database regarding that query. Generally, we recommend maintaining soil moisture, using well-composted organic fertilizer, and monitoring leaf surfaces weekly for mildew or blight. Try asking about 'Early Blight', 'npk fertilizer', or 'cow dung manure'."
        
    return {
        "message": bot_response,
        "citations": citations
    }

# 4. PRODUCTS & MARKETPLACE

@app.get("/api/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@app.post("/api/products/order")
def place_order(
    items: str = Form(...), # JSON string of items
    total_amount: float = Form(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    invoice_no = f"AD-{datetime.datetime.utcnow().strftime('%y%m%d%H%M%S')}"
    tracking_no = f"AGRO-{datetime.datetime.utcnow().strftime('%S%M%H%f')[:8]}"
    
    order = Order(
        user_id=current_user.id,
        invoice_number=invoice_no,
        tracking_number=tracking_no,
        total_amount=total_amount,
        items=items
    )
    db.add(order)
    
    # Save to crop activity log
    log = CropHistory(
        user_id=current_user.id,
        action="Purchase",
        description=f"Ordered fertilizer/seeds. Invoice: {invoice_no}"
    )
    db.add(log)
    
    db.commit()
    return {
        "invoice_number": invoice_no,
        "tracking_number": tracking_no,
        "delivery_days": 3
    }

# 5. USER HISTORY & NOTIFICATIONS

@app.get("/api/history")
def get_user_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    detections = db.query(CropDetection).filter(CropDetection.user_id == current_user.id).order_by(CropDetection.detection_time.desc()).all()
    history_list = []
    
    for d in detections:
        # Get matching disease
        dis = db.query(DiseaseDetection).filter(DiseaseDetection.crop_detection_id == d.id).first()
        history_list.append({
            "id": d.id,
            "crop": d.crop_name,
            "scientific_name": d.scientific_name,
            "confidence": f"{d.confidence:.1%}" if d.confidence <= 1 else f"{d.confidence}%",
            "health_score": d.health_score,
            "severity": d.severity,
            "leaf_quality": d.leaf_quality,
            "spots_count": d.spots_count,
            "recovery_score": d.recovery_score,
            "detection_time": d.detection_time.strftime("%d %b %Y, %I:%M %p"),
            "disease": dis.disease_name if dis else "Healthy",
            "cause": dis.cause if dis else "",
            "organic_remedy": dis.organic_treatment if dis else "",
            "chemical_remedy": dis.chemical_treatment if dis else "",
            "prevention": dis.prevention if dis else "",
            "heatmap": d.heatmap_path
        })
        
    return history_list

@app.get("/api/notifications")
def get_notifications(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    notis = db.query(Notification).filter(Notification.user_id == current_user.id).order_by(Notification.timestamp.desc()).all()
    return [{"id": n.id, "message": n.message, "is_read": n.is_read, "time": n.timestamp.strftime("%I:%M %p")} for n in notis]

@app.post("/api/notifications/read")
def mark_read(
    noti_id: int = Form(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    n = db.query(Notification).filter(Notification.id == noti_id, Notification.user_id == current_user.id).first()
    if n:
        n.is_read = True
        db.commit()
    return {"status": "success"}

# 6. ANALYTICS & VISUALIZATIONS DATA SOURCE

@app.get("/api/analytics")
def get_analytics(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Retrieve user's detections
    detections = db.query(CropDetection).filter(CropDetection.user_id == current_user.id).all()
    
    # 1. Disease vs Healthy Ratio
    healthy_count = sum(1 for d in detections if d.severity == "Healthy")
    diseased_count = len(detections) - healthy_count
    
    # 2. Crop Distribution
    crop_counts = {}
    for d in detections:
        crop_counts[d.crop_name] = crop_counts.get(d.crop_name, 0) + 1
        
    crop_dist = [{"name": k, "value": v} for k, v in crop_counts.items()]
    
    # 3. Severity trends
    severity_counts = {"Low": 0, "Medium": 0, "High": 0, "Critical": 0, "Healthy": 0}
    for d in detections:
        severity_counts[d.severity] = severity_counts.get(d.severity, 0) + 1
        
    severity_dist = [{"name": k, "value": v} for k, v in severity_counts.items()]

    # 4. Timeline Monthly scans (mocked historical or based on db timestamps)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthly_scans = {m: 0 for m in months}
    for d in detections:
        m_str = d.detection_time.strftime("%b")
        if m_str in monthly_scans:
            monthly_scans[m_str] += 1
            
    scans_trend = [{"month": m, "scans": monthly_scans[m]} for m in months]

    # Prepopulate values if history is empty to make charts instantly attractive
    if len(detections) == 0:
        crop_dist = [
            {"name": "Tomato", "value": 12},
            {"name": "Rose", "value": 8},
            {"name": "Rice", "value": 5},
            {"name": "Potato", "value": 3}
        ]
        severity_dist = [
            {"name": "Healthy", "value": 15},
            {"name": "Low", "value": 7},
            {"name": "Medium", "value": 4},
            {"name": "High", "value": 2}
        ]
        scans_trend = [
            {"month": "Jan", "scans": 2},
            {"month": "Feb", "scans": 5},
            {"month": "Mar", "scans": 8},
            {"month": "Apr", "scans": 12},
            {"month": "May", "scans": 18},
            {"month": "Jun", "scans": 28}
        ]
        healthy_count = 15
        diseased_count = 13

    return {
        "healthy_count": healthy_count,
        "diseased_count": diseased_count,
        "crop_distribution": crop_dist,
        "severity_distribution": severity_dist,
        "scans_trend": scans_trend,
        "total_scans": len(detections) if len(detections) > 0 else 28
    }

# 7. ADMIN DASHBOARD & SYSTEM UTILITIES

@app.get("/api/admin/logs", dependencies=[Depends(RoleChecker(["Admin"]))])
def get_system_logs(db: Session = Depends(get_db)):
    logs = db.query(AuditLog).order_by(AuditLog.timestamp.desc()).limit(100).all()
    logs_data = []
    for l in logs:
        user_name = "System"
        if l.user_id:
            u = db.query(User).filter(User.id == l.user_id).first()
            if u: user_name = u.name
        logs_data.append({
            "id": l.id,
            "user": user_name,
            "action": l.action,
            "details": l.details,
            "time": l.timestamp.strftime("%Y-%m-%d %I:%M %p")
        })
    return logs_data

@app.post("/api/admin/backup", dependencies=[Depends(RoleChecker(["Admin"]))])
def backup_database():
    try:
        from database import DB_PATH
        backup_dir = os.path.dirname(DB_PATH)
        backup_path = os.path.join(backup_dir, f"backup_agro_{datetime.datetime.utcnow().strftime('%y%m%d_%H%M%S')}.db")
        shutil.copy2(DB_PATH, backup_path)
        return {"status": "success", "message": f"Database backup completed: {os.path.basename(backup_path)}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Backup failed: {str(e)}")

@app.post("/api/admin/restore", dependencies=[Depends(RoleChecker(["Admin"]))])
def restore_database(backup_name: str = Form(...)):
    try:
        from database import DB_PATH
        backup_dir = os.path.dirname(DB_PATH)
        target_backup = os.path.join(backup_dir, backup_name)
        if not os.path.exists(target_backup):
            raise HTTPException(status_code=404, detail="Selected backup file not found")
        
        # Close connection and overwrite
        engine.dispose()
        shutil.copy2(target_backup, DB_PATH)
        return {"status": "success", "message": "Database restored successfully. Please restart/reload portal."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Restore failed: {str(e)}")

@app.post("/api/admin/upload-kb", dependencies=[Depends(RoleChecker(["Admin"]))])
def upload_knowledge_manual(
    title: str = Form(...),
    content: str = Form(...),
    document_type: str = Form(...),
    source: str = Form(...),
    db: Session = Depends(get_db)
):
    doc = KnowledgeBase(
        title=title,
        content=content,
        document_type=document_type,
        source=source,
        chunk_index=0
    )
    db.add(doc)
    db.commit()
    return {"status": "success", "message": f"Manual '{title}' added to the offline RAG index."}

@app.get("/api/crops")
def get_crops(q: Optional[str] = None, limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    """Search and list plants from the local database with pagination."""
    query = db.query(Plant)
    if q:
        search_pattern = f"%{q}%"
        query = query.outerjoin(Family).outerjoin(Genus).outerjoin(SpeciesRecord).outerjoin(SoilRequirement)
        query = query.filter(
            (Plant.common_name.ilike(search_pattern)) |
            (Plant.botanical_name.ilike(search_pattern)) |
            (Plant.synonyms.ilike(search_pattern)) |
            (Plant.local_names.ilike(search_pattern)) |
            (Plant.category.ilike(search_pattern)) |
            (Plant.commercial_uses.ilike(search_pattern)) |
            (Plant.medicinal_uses.ilike(search_pattern)) |
            (Family.name.ilike(search_pattern)) |
            (Genus.name.ilike(search_pattern)) |
            (SpeciesRecord.name.ilike(search_pattern)) |
            (SoilRequirement.preferred_soil.ilike(search_pattern))
        )

    total = query.count()
    plants = query.offset(offset).limit(limit).all()

    # Only fall back to hardcoded CROP_DATASET if the entire plants table is empty
    if not plants and total == 0 and not q:
        return [{"name": name, "scientific_name": meta["scientific_name"]} for name, meta in list(CROP_DATASET.items())[:limit]]

    return {
        "total": total,
        "offset": offset,
        "limit": limit,
        "results": [{
            "id": p.id,
            "name": p.common_name,
            "scientific_name": p.botanical_name,
            "category": p.category,
            "family": p.family.name if p.family else None,
            "genus": p.genus.name if p.genus else None
        } for p in plants]
    }

@app.get("/api/crops/{name}")
def get_crop_details(name: str, db: Session = Depends(get_db)):
    """Retrieve full botanical details for a plant by ID, common name, scientific name, synonym, or local name."""
    plant = None

    # --- Step 1: Exact ID lookup ---
    if name.isdigit():
        plant = db.query(Plant).filter(Plant.id == int(name)).first()

    # --- Step 2: Exact common name (case-insensitive) ---
    if not plant:
        plant = db.query(Plant).filter(Plant.common_name.ilike(name)).first()

    # --- Step 3: Exact botanical name (case-insensitive) ---
    if not plant:
        plant = db.query(Plant).filter(Plant.botanical_name.ilike(name)).first()

    # --- Step 4: Partial / fuzzy match across all name fields ---
    if not plant:
        fuzzy = f"%{name}%"
        plant = db.query(Plant).filter(
            (Plant.common_name.ilike(fuzzy)) |
            (Plant.botanical_name.ilike(fuzzy)) |
            (Plant.synonyms.ilike(fuzzy)) |
            (Plant.local_names.ilike(fuzzy))
        ).first()

    # --- Step 5: Fallback to legacy hardcoded CROP_DATASET ---
    if not plant:
        matched_name = next((k for k in CROP_DATASET if k.lower() == name.lower()), None)
        if not matched_name:
            # also try partial match in CROP_DATASET
            matched_name = next((k for k in CROP_DATASET if name.lower() in k.lower() or k.lower() in name.lower()), None)
        if matched_name:
            meta = CROP_DATASET[matched_name]
            return {
                "id": None,
                "name": matched_name,
                "scientific_name": meta["scientific_name"],
                "synonyms": None,
                "local_names": None,
                "plant_authority": None,
                "overview": meta["location"],
                "morphology": None,
                "leaf_desc": None,
                "flower_desc": None,
                "fruit_desc": None,
                "seed_desc": None,
                "stem_desc": None,
                "root_desc": None,
                "growth_habit": None,
                "life_cycle": "Annual",
                "average_height": None,
                "average_width": None,
                "lifespan": None,
                "category": "Crop",
                "commercial_uses": None,
                "medicinal_uses": None,
                "industrial_uses": None,
                "food_uses": None,
                "toxicity": None,
                "conservation_status": "Least Concern",
                "family": None,
                "genus": None,
                "species": None,
                "classification": None,
                "varieties": [],
                "climate": {
                    "native_region": None,
                    "countries_grown": meta["location"],
                    "climatic_zones": None,
                    "suitable_altitude": None,
                    "rainfall_requirement": None,
                    "temperature_requirement": None,
                    "humidity_requirement": None
                },
                "soil": None,
                "diseases": [{"id": i, "name": d, "pathogen_name": None, "disease_type": None, "risk_level": "Medium", "economic_impact": None, "symptoms": [], "treatments": []} for i, d in enumerate(meta["diseases"])],
                "pests": [],
                "deficiencies": [],
                "irrigation": None,
                "harvest": {
                    "harvest_indicators": None,
                    "harvest_time": meta["season"],
                    "harvest_method": None,
                    "post_harvest_handling": None,
                    "storage_temp": None,
                    "shelf_life": None
                },
                "stages": [],
                "images": []
            }

        # No match anywhere – return a descriptive 404 (never blame the user)
        raise HTTPException(
            status_code=404,
            detail=f"Plant '{name}' was not found in the botanical database. "
                   "This may mean the species has not yet been added to the local knowledge base. "
                   "Try a different spelling, scientific name, or synonym."
        )

    return {
        "id": plant.id,
        "name": plant.common_name,
        "scientific_name": plant.botanical_name,
        "synonyms": plant.synonyms,
        "local_names": plant.local_names,
        "plant_authority": plant.plant_authority,
        "overview": plant.overview,
        "morphology": plant.morphology,
        "leaf_desc": plant.leaf_desc,
        "flower_desc": plant.flower_desc,
        "fruit_desc": plant.fruit_desc,
        "seed_desc": plant.seed_desc,
        "stem_desc": plant.stem_desc,
        "root_desc": plant.root_desc,
        "growth_habit": plant.growth_habit,
        "life_cycle": plant.life_cycle,
        "average_height": plant.average_height,
        "average_width": plant.average_width,
        "lifespan": plant.lifespan,
        "category": plant.category,
        "commercial_uses": plant.commercial_uses,
        "medicinal_uses": plant.medicinal_uses,
        "industrial_uses": plant.industrial_uses,
        "food_uses": plant.food_uses,
        "toxicity": plant.toxicity,
        "conservation_status": plant.conservation_status,
        
        "family": {
            "name": plant.family.name,
            "description": plant.family.description
        } if plant.family else None,
        
        "genus": {
            "name": plant.genus.name,
            "description": plant.genus.description
        } if plant.genus else None,
        
        "species": {
            "name": plant.species_rec.name,
            "description": plant.species_rec.description
        } if plant.species_rec else None,
        
        "classification": {
            "kingdom": plant.classification.kingdom,
            "division": plant.classification.division,
            "class_name": plant.classification.class_name,
            "order_name": plant.classification.order_name,
            "taxonomy_hierarchy": plant.classification.taxonomy_hierarchy
        } if plant.classification else None,
        
        "varieties": [
            {
                "name": v.name,
                "variety_type": v.variety_type,
                "growing_period": v.growing_period,
                "yield_potential": v.yield_potential
            } for v in plant.varieties
        ],
        
        "climate": {
            "native_region": plant.climate.native_region,
            "countries_grown": plant.climate.countries_grown,
            "climatic_zones": plant.climate.climatic_zones,
            "suitable_altitude": plant.climate.suitable_altitude,
            "rainfall_requirement": plant.climate.rainfall_requirement,
            "temperature_requirement": plant.climate.temperature_requirement,
            "humidity_requirement": plant.climate.humidity_requirement
        } if plant.climate else None,
        
        "soil": {
            "preferred_soil": plant.soil.preferred_soil,
            "soil_ph_range": plant.soil.soil_ph_range,
            "drainage": plant.soil.drainage,
            "organic_matter": plant.soil.organic_matter,
            "fertility": plant.soil.fertility,
            "texture": plant.soil.texture
        } if plant.soil else None,
        
        "diseases": [
            {
                "id": d.id,
                "name": d.name,
                "pathogen_name": d.pathogen_name,
                "disease_type": d.disease_type,
                "risk_level": d.risk_level,
                "economic_impact": d.economic_impact,
                "symptoms": [
                    {
                        "early_symptoms": s.early_symptoms,
                        "late_symptoms": s.late_symptoms,
                        "affected_parts": s.affected_parts
                    } for s in d.symptoms
                ],
                "treatments": [
                    {
                        "immediate_treatment": t.immediate_treatment,
                        "organic_treatment": t.organic_treatment,
                        "chemical_treatment": t.chemical_treatment,
                        "biological_control": t.biological_control,
                        "recommended_fungicides": t.recommended_fungicides,
                        "recommended_organic_solutions": t.recommended_organic_solutions,
                        "dosage": t.dosage,
                        "application_frequency": t.application_frequency,
                        "safety_precautions": t.safety_precautions,
                        "recovery_time": t.recovery_time
                    } for t in d.treatments
                ]
            } for d in plant.diseases_list
        ],
        
        "pests": [
            {
                "id": pst.id,
                "name": pst.name,
                "scientific_name": pst.scientific_name,
                "identification": pst.identification,
                "damage_symptoms": pst.damage_symptoms,
                "lifecycle": pst.lifecycle,
                "organic_control": pst.organic_control,
                "chemical_control": pst.chemical_control,
                "biological_control": pst.biological_control,
                "economic_threshold": pst.economic_threshold
            } for pst in plant.pests_list
        ],
        
        "deficiencies": [
            {
                "id": df.id,
                "nutrient_name": df.nutrient_name,
                "symptoms": df.symptoms,
                "correction_methods": df.correction_methods,
                "recommended_fertilizers": df.recommended_fertilizers
            } for df in plant.nutrient_deficiencies
        ],
        
        "irrigation": {
            "water_requirement": plant.irrigation.water_requirement,
            "daily_water_need": plant.irrigation.daily_water_need,
            "weekly_water_need": plant.irrigation.weekly_water_need,
            "drip_recommendation": plant.irrigation.drip_recommendation,
            "critical_stages": plant.irrigation.critical_stages
        } if plant.irrigation else None,
        
        "harvest": {
            "harvest_indicators": plant.harvest.harvest_indicators,
            "harvest_time": plant.harvest.harvest_time,
            "harvest_method": plant.harvest.harvest_method,
            "post_harvest_handling": plant.harvest.post_harvest_handling,
            "storage_temp": plant.harvest.storage_temp,
            "shelf_life": plant.harvest.shelf_life
        } if plant.harvest else None,
        
        "stages": [
            {
                "name": stg.name,
                "description": stg.description,
                "duration_days": stg.duration_days
            } for stg in plant.growth_stages
        ],
        
        "images": [
            {
                "category": img.category,
                "url": img.url
            } for img in plant.plant_images
        ]
    }


# ─────────────────────────────────────────────────────────────────────────────
# BOTANICAL INTELLIGENCE DATASET ENDPOINTS (Phase 6)
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/api/botanical/search")
def api_botanical_search(q: str, doc_type: Optional[str] = None, limit: int = 10):
    """
    Search the offline botanical intelligence database using the hybrid RAG engine.
    """
    try:
        from botanical_dataset.rag_search_engine import get_search_engine
        engine = get_search_engine()
        results = engine.search(q, top_k=limit, doc_type_filter=doc_type)
        return {
            "status": "success",
            "query": q,
            "doc_type_filter": doc_type,
            "total_results": len(results),
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.get("/api/botanical/disease")
def api_botanical_disease(crop: str, symptoms: str, db: Session = Depends(get_db)):
    """
    Diagnose or retrieve detailed information about plant diseases affecting a crop.
    """
    try:
        from botanical_dataset.rag_search_engine import get_search_engine
        from models_botanical import PlantDisease
        
        engine = get_search_engine()
        query = f"{crop} {symptoms}"
        rag_results = engine.search_diseases(query, top_k=5)
        
        detailed_results = []
        for doc in rag_results:
            # Extract disease name from RAG title
            disease_name = doc.get("title", "").split(" (")[0]
            
            db_disease = db.query(PlantDisease).filter(
                (PlantDisease.disease_name.ilike(disease_name)) |
                (PlantDisease.disease_name.ilike(f"%{disease_name}%"))
            ).first()
            
            detail = {
                "rag_score": doc.get("rrf_score", 0),
                "title": doc.get("title"),
                "summary": doc.get("content"),
                "plant_name": doc.get("plant_name"),
                "tags": doc.get("tags")
            }
            if db_disease:
                detail.update({
                    "id": db_disease.id,
                    "disease_name": db_disease.disease_name,
                    "pathogen_name": db_disease.pathogen_name,
                    "disease_type": db_disease.disease_type,
                    "affected_plant": db_disease.affected_plant,
                    "host_range": db_disease.host_range,
                    "risk_level": db_disease.risk_level,
                    "economic_impact": db_disease.economic_impact,
                    "geographic_distribution": db_disease.geographic_distribution,
                    "favorable_conditions": db_disease.favorable_conditions,
                    "early_symptoms": db_disease.early_symptoms,
                    "late_symptoms": db_disease.late_symptoms,
                    "affected_parts": db_disease.affected_parts,
                    "disease_cycle": db_disease.disease_cycle,
                    "incubation_period": db_disease.incubation_period,
                    "organic_treatment": db_disease.organic_treatment,
                    "chemical_treatment": db_disease.chemical_treatment,
                    "biological_treatment": db_disease.biological_treatment,
                    "preventive_measures": db_disease.preventive_measures,
                    "application_frequency": db_disease.application_frequency,
                    "recovery_time": db_disease.recovery_time,
                    "phi_days": db_disease.phi_days
                })
            detailed_results.append(detail)
            
        return {
            "status": "success",
            "crop": crop,
            "symptoms": symptoms,
            "diagnoses": detailed_results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Disease retrieval failed: {str(e)}")


@app.get("/api/botanical/pest")
def api_botanical_pest(crop: str, description: str, db: Session = Depends(get_db)):
    """
    Search and retrieve information about plant pests affecting a crop.
    """
    try:
        from botanical_dataset.rag_search_engine import get_search_engine
        from models_botanical import PlantPest
        
        engine = get_search_engine()
        query = f"{crop} {description}"
        rag_results = engine.search_pests(query, top_k=5)
        
        detailed_results = []
        for doc in rag_results:
            pest_title = doc.get("title", "")
            pest_name = pest_title.split(" - ")[0] if " - " in pest_title else pest_title
            
            db_pest = db.query(PlantPest).filter(
                (PlantPest.pest_name.ilike(pest_name)) |
                (PlantPest.pest_name.ilike(f"%{pest_name}%"))
            ).first()
            
            detail = {
                "rag_score": doc.get("rrf_score", 0),
                "title": doc.get("title"),
                "summary": doc.get("content"),
                "plant_name": doc.get("plant_name"),
                "tags": doc.get("tags")
            }
            if db_pest:
                detail.update({
                    "id": db_pest.id,
                    "pest_name": db_pest.pest_name,
                    "scientific_name": db_pest.scientific_name,
                    "order_name": db_pest.order_name,
                    "family_name": db_pest.family_name,
                    "pest_category": db_pest.pest_category,
                    "host_plants": db_pest.host_plants,
                    "geographic_distribution": db_pest.geographic_distribution,
                    "damage_type": db_pest.damage_type,
                    "identification_tips": db_pest.identification_tips,
                    "damage_symptoms": db_pest.damage_symptoms,
                    "lifecycle_summary": db_pest.lifecycle_summary,
                    "seasonal_peak": db_pest.seasonal_peak,
                    "economic_threshold": db_pest.economic_threshold,
                    "organic_control": db_pest.organic_control,
                    "chemical_control": db_pest.chemical_control,
                    "biological_control": db_pest.biological_control,
                    "ipm_notes": db_pest.ipm_notes,
                    "natural_predators": db_pest.natural_predators,
                    "resistance_issues": db_pest.resistance_issues
                })
            detailed_results.append(detail)
            
        return {
            "status": "success",
            "crop": crop,
            "description": description,
            "pests": detailed_results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pest retrieval failed: {str(e)}")


@app.get("/api/botanical/nutrient")
def api_botanical_nutrient(symptoms: str, db: Session = Depends(get_db)):
    """
    Diagnose nutrient deficiencies based on leaf/symptom description.
    """
    try:
        from botanical_dataset.rag_search_engine import get_search_engine
        from models_botanical import NutrientDeficiency
        
        engine = get_search_engine()
        rag_results = engine.search_nutrients(symptoms, top_k=3)
        
        detailed_results = []
        for doc in rag_results:
            title = doc.get("title", "")
            nutrient_name = title.split(" (")[0] if " (" in title else title
            nutrient_name = nutrient_name.split(" - ")[0] if " - " in nutrient_name else nutrient_name
            
            db_nutrient = db.query(NutrientDeficiency).filter(
                NutrientDeficiency.nutrient_name.ilike(nutrient_name)
            ).first()
            
            detail = {
                "rag_score": doc.get("rrf_score", 0),
                "title": doc.get("title"),
                "summary": doc.get("content"),
                "plant_name": doc.get("plant_name"),
                "tags": doc.get("tags")
            }
            if db_nutrient:
                detail.update({
                    "id": db_nutrient.id,
                    "nutrient_name": db_nutrient.nutrient_name,
                    "symbol": db_nutrient.symbol,
                    "element_type": db_nutrient.element_type,
                    "plant_content_range": db_nutrient.plant_content_range,
                    "functions": db_nutrient.functions,
                    "deficiency_name": db_nutrient.deficiency_name,
                    "deficiency_visual_signs": db_nutrient.deficiency_visual_signs,
                    "affected_leaves": db_nutrient.affected_leaves,
                    "deficiency_crop_specific": db_nutrient.deficiency_crop_specific,
                    "toxicity_symptoms": db_nutrient.toxicity_symptoms,
                    "toxicity_threshold": db_nutrient.toxicity_threshold,
                    "forms_in_soil": db_nutrient.forms_in_soil,
                    "mobility_in_plant": db_nutrient.mobility_in_plant,
                    "optimal_soil_ph": db_nutrient.optimal_soil_ph,
                    "fertilizer_sources": db_nutrient.fertilizer_sources,
                    "critical_crops": db_nutrient.critical_crops
                })
            detailed_results.append(detail)
            
        return {
            "status": "success",
            "symptoms": symptoms,
            "deficiencies": detailed_results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Nutrient retrieval failed: {str(e)}")
