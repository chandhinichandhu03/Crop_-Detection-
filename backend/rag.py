import re
import numpy as np
from sqlalchemy.orm import Session
from models import KnowledgeBase, Plant, Disease, Pest, Family, Genus

# Static RAG agricultural manuals for initial DB population
INITIAL_DOCUMENTS = [
    {
        "title": "Integrated Pest Management for Solanaceous Crops (Tomato/Potato)",
        "document_type": "Manual",
        "source": "ICAR Extension Bulletin",
        "content": "Early Blight caused by Alternaria solani manifests as concentric rings on older leaves first. Treatment involves applying chlorothalonil or copper oxychloride fungicide. Organic farming alternatives include spraying cold-pressed neem oil (4-5 ml/L) mixed with liquid soap, and maintaining strict crop rotation. Late Blight caused by Phytophthora infestans spreads rapidly in high humidity. Remove infected foliage and apply Mancozeb or systemic metalaxyl."
    },
    {
        "title": "Organic Farming & Soil Nutrition Guide",
        "document_type": "Guide",
        "source": "Organic Agriculture Institute",
        "content": "Cow dung manure contains 0.5% Nitrogen, 0.2% Phosphorus, and 0.5% Potassium. For optimal root development, apply well-rotted compost (gobar manure) 15-20 days before sowing. Bio-fertilizers like Blue-Green Algae (BGA) and Azotobacter fix atmospheric nitrogen in standing water fields, saving up to 20-30% chemical nitrogen. Yellowing of leaves indicates nitrogen deficiency, which can be cured by compost tea or urea application."
    },
    {
        "title": "Fungal Disease Control in Rose & Flower Plants",
        "document_type": "Disease Manual",
        "source": "Horticultural Society India",
        "content": "Black Spot (Diplocarpon rosae) is a wet-weather disease in Rose. Prune dead wood and collect fallen leaves. Spray sulfur or potassium bicarbonate organically. Powdery Mildew appears as a white powder on leaves when days are warm and nights are cool. Cure using a baking soda and oil spray (1 tbsp baking soda, 1 tsp soap, 1 gallon water) or organic milk-water sprays (40% milk, 60% water)."
    },
    {
        "title": "Rice Blast and Bacterial Blight Management",
        "document_type": "Research Paper",
        "source": "National Rice Research Institute",
        "content": "Rice Blast (Magnaporthe oryzae) causes spindle-shaped lesions with grey centers. Avoid excessive urea. Seed treatment with Trichoderma viride at 10g/kg controls early outbreaks. Chemical spraying of Tricyclazole at 0.6g/L is recommended at boot stage. Bacterial Leaf Blight produces wavy yellow stripes from leaf tips; treat with copper hydroxide or Streptocycline antibiotics."
    },
    {
        "title": "Fertilizer Schedule and Soil pH Management",
        "document_type": "Fertilizer Manual",
        "source": "Soil Health Association",
        "content": "NPK fertilizer ratios represent Nitrogen (leaves), Phosphorus (roots), and Potassium (blooms/fruits). Soil pH should be managed between 6.0 and 7.0 for most agricultural crops. To reduce soil alkalinity, apply gypsum or sulfur. To correct acidic soil, apply Agricultural Lime (Calcium Carbonate). Micronutrient deficiencies of Zinc and Iron can be corrected with Zinc Sulfate spray (0.5%)."
    },
    {
        "title": "Cotton Leaf Curl and Pest Control",
        "document_type": "Guide",
        "source": "Central Cotton Research Institute",
        "content": "Cotton Leaf Curl Virus is transmitted by Whiteflies. Controlling the vector is key. Spray neem seed kernel extract (5%) or systemics like Imidacloprid. Boll Rot is caused by fungal complexes under damp weather. Space crops properly to allow light penetration. Use copper oxychloride (3g/L) to prevent rot spreading."
    }
]

def clean_text(text: str) -> str:
    """Preprocess text for local vectorization."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def build_rag_index(db: Session):
    """Ensure the knowledge base is populated."""
    count = db.query(KnowledgeBase).count()
    if count == 0:
        for doc in INITIAL_DOCUMENTS:
            db_doc = KnowledgeBase(
                title=doc["title"],
                content=doc["content"],
                document_type=doc["document_type"],
                source=doc["source"],
                chunk_index=0
            )
            db.add(db_doc)
        db.commit()

def search_knowledge_base(query: str, db: Session, limit: int = 2):
    """
    Enhanced retrieval engine that searches by Scientific Name, Botanical Name,
    Genus, Family, Species, Disease, Pest, Local Name, Common Name, and Synonyms
    in the relational database tables, and falls back to TF-IDF Vector Space search.
    """
    build_rag_index(db)
    results = []
    
    # 1. Search Relational Database Tables
    query_clean = query.lower()
    words = [w for w in query_clean.split() if len(w) > 2]
    


    sql_matched_plants = []
    for word in words:
        pts = db.query(Plant).join(Family, isouter=True).join(Genus, isouter=True).filter(
            (Plant.common_name.ilike(f"%{word}%")) |
            (Plant.botanical_name.ilike(f"%{word}%")) |
            (Plant.synonyms.ilike(f"%{word}%")) |
            (Plant.local_names.ilike(f"%{word}%")) |
            (Family.name.ilike(f"%{word}%")) |
            (Genus.name.ilike(f"%{word}%"))
        ).limit(3).all()
        for p in pts:
            if p not in sql_matched_plants:
                sql_matched_plants.append(p)
                
    for p in sql_matched_plants[:3]:
        # Synthesize snippet
        content_parts = [
            f"Botanical Classification: Family {p.family.name if p.family else 'N/A'}, Genus {p.genus.name if p.genus else 'N/A'}, Species {p.species_rec.name if p.species_rec else 'N/A'}.",
            f"Overview: {p.overview or 'N/A'}",
            f"Morphology: {p.morphology or 'N/A'}",
            f"Growth Habit: {p.growth_habit or 'N/A'}, Cycle: {p.life_cycle or 'N/A'}."
        ]
        if p.soil:
            content_parts.append(f"Soil Preferred: {p.soil.preferred_soil} (pH: {p.soil.soil_ph_range}).")
        if p.irrigation:
            content_parts.append(f"Water Requirement: {p.irrigation.water_requirement} (Daily: {p.irrigation.daily_water_need}).")
            
        results.append({
            "title": f"Botanical Record: {p.common_name} ({p.botanical_name})",
            "content": " ".join(content_parts),
            "document_type": "Scientific Record",
            "source": "Local Relational Database",
            "similarity_score": 1.0
        })

    # Search Diseases
    sql_matched_diseases = []
    for word in words:
        dis = db.query(Disease).filter(
            (Disease.name.ilike(f"%{word}%")) |
            (Disease.pathogen_name.ilike(f"%{word}%"))
        ).limit(3).all()
        for d in dis:
            if d not in sql_matched_diseases:
                sql_matched_diseases.append(d)
                
    for d in sql_matched_diseases[:3]:
        content_parts = [
            f"Disease: {d.name} on host plant ID {d.plant_id}.",
            f"Pathogen: {d.pathogen_name or 'N/A'}. Disease Type: {d.disease_type or 'N/A'}."
        ]
        if d.symptoms:
            content_parts.append(f"Symptoms (Early): {d.symptoms[0].early_symptoms} (Late): {d.symptoms[0].late_symptoms}. Affected: {d.symptoms[0].affected_parts}.")
        if d.treatments:
            content_parts.append(f"Immediate Action: {d.treatments[0].immediate_treatment}. Organic: {d.treatments[0].organic_treatment}. Chemical: {d.treatments[0].chemical_treatment}.")
            
        results.append({
            "title": f"Disease Bulletin: {d.name}",
            "content": " ".join(content_parts),
            "document_type": "Disease Manual",
            "source": "Local Relational Database",
            "similarity_score": 0.98
        })

    # Search Pests
    sql_matched_pests = []
    for word in words:
        psts = db.query(Pest).filter(
            (Pest.name.ilike(f"%{word}%")) |
            (Pest.scientific_name.ilike(f"%{word}%"))
        ).limit(3).all()
        for pt in psts:
            if pt not in sql_matched_pests:
                sql_matched_pests.append(pt)
                
    for pt in sql_matched_pests[:3]:
        results.append({
            "title": f"Pest Guide: {pt.name} ({pt.scientific_name})",
            "content": f"Identification: {pt.identification}. Damage: {pt.damage_symptoms}. Lifecycle: {pt.lifecycle}. Organic Control: {pt.organic_control}. Chemical Control: {pt.chemical_control}. Predators: {pt.biological_control}.",
            "document_type": "Pest Manual",
            "source": "Local Relational Database",
            "similarity_score": 0.98
        })

    # 2. Fallback to general TF-IDF Vector Space search
    docs = db.query(KnowledgeBase).all()
    if docs:
        doc_clean_texts = [clean_text(d.content) for d in docs]
        
        # Calculate Term Frequencies (TF) for all unique words across docs
        all_words = set(query_clean.split())
        for d_text in doc_clean_texts:
            all_words.update(d_text.split())
        
        word_list = list(all_words)
        word_to_idx = {word: idx for idx, word in enumerate(word_list)}
        
        df = {}
        for word in word_list:
            df[word] = sum(1 for d_text in doc_clean_texts if word in d_text.split())
            
        num_docs = len(docs)
        idf = {}
        for word in word_list:
            idf[word] = np.log((1 + num_docs) / (1 + df[word])) + 1
            
        doc_vectors = []
        for d_text in doc_clean_texts:
            vec = np.zeros(len(word_list))
            words_in_doc = d_text.split()
            doc_len = len(words_in_doc) if len(words_in_doc) > 0 else 1
            for word in words_in_doc:
                if word in word_to_idx:
                    vec[word_to_idx[word]] += 1
            vec = vec / doc_len
            for word, idx in word_to_idx.items():
                vec[idx] *= idf[word]
            norm = np.linalg.norm(vec)
            if norm > 0:
                vec = vec / norm
            doc_vectors.append(vec)
            
        q_vec = np.zeros(len(word_list))
        q_words = query_clean.split()
        q_len = len(q_words) if len(q_words) > 0 else 1
        for word in q_words:
            if word in word_to_idx:
                q_vec[word_to_idx[word]] += 1
        q_vec = q_vec / q_len
        for word, idx in word_to_idx.items():
            q_vec[idx] *= idf[word]
        q_norm = np.linalg.norm(q_vec)
        if q_norm > 0:
            q_vec = q_vec / q_norm
            
        similarities = []
        for idx, d_vec in enumerate(doc_vectors):
            sim = float(np.dot(q_vec, d_vec))
            similarities.append((sim, docs[idx]))
            
        similarities.sort(key=lambda x: x[0], reverse=True)
        
        for sim, doc in similarities:
            if sim > 0.02:
                # Deduplicate titles
                if not any(r["title"] == doc.title for r in results):
                    results.append({
                        "title": doc.title,
                        "content": doc.content,
                        "document_type": doc.document_type,
                        "source": doc.source,
                        "similarity_score": round(sim, 2)
                    })
                    
    # Sort unified results by similarity score descending and apply limit
    results.sort(key=lambda x: x["similarity_score"], reverse=True)
    return results[:limit]

