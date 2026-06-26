"""
rag_search_engine.py
Offline RAG (Retrieval-Augmented Generation) Search Engine for Agro Doctor
Uses TF-IDF + BM25 for document retrieval — NO external APIs required
"""

import re
import math
import json
import logging
from collections import Counter, defaultdict
from typing import List, Dict, Tuple, Optional
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# STOP WORDS (English + agricultural terms to exclude)
# ─────────────────────────────────────────────────────────────────────────────
STOP_WORDS = set([
    # Common English stop words
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "being", "have", "has", "had", "do", "does", "did", "will", "would",
    "could", "should", "may", "might", "can", "shall", "it", "its", "this",
    "that", "these", "those", "i", "you", "he", "she", "we", "they", "me",
    "him", "her", "us", "them", "my", "your", "his", "our", "their",
    "what", "which", "who", "when", "where", "why", "how", "all", "both",
    "each", "few", "more", "most", "other", "some", "such", "no", "nor",
    "not", "only", "same", "so", "than", "too", "very", "just", "as",
    "if", "about", "per", "into", "up", "out", "through", "during",
    # Common agricultural words that are too generic
    "crop", "plant", "plants", "growth", "also", "well", "using", "used",
    "use", "one", "two", "three", "four", "five", "six"
])

# ─────────────────────────────────────────────────────────────────────────────
# TEXT PREPROCESSING
# ─────────────────────────────────────────────────────────────────────────────

def preprocess_text(text: str) -> List[str]:
    """Tokenize and preprocess text for TF-IDF."""
    # Lowercase
    text = text.lower()
    # Replace special chars with space (but keep hyphens in compound words)
    text = re.sub(r'[^a-z0-9\s\-]', ' ', text)
    # Split on whitespace
    tokens = text.split()
    # Filter stop words and short tokens
    tokens = [t for t in tokens if t not in STOP_WORDS and len(t) > 2]
    # Simple stemming: remove common suffixes
    stemmed = [simple_stem(t) for t in tokens]
    return stemmed


def simple_stem(word: str) -> str:
    """Simple rule-based stemmer for agricultural terms."""
    # Handle common suffixes
    if word.endswith('ically'):
        return word[:-4]
    if word.endswith('ical'):
        return word[:-3]
    if word.endswith('tion') and len(word) > 7:
        return word[:-4]
    if word.endswith('ing') and len(word) > 6:
        return word[:-3]
    if word.endswith('ed') and len(word) > 5:
        return word[:-2]
    if word.endswith('er') and len(word) > 5:
        return word[:-2]
    if word.endswith('es') and len(word) > 5:
        return word[:-2]
    if word.endswith('s') and len(word) > 4 and not word.endswith('ss'):
        return word[:-1]
    if word.endswith('ous') and len(word) > 6:
        return word[:-3]
    return word


# ─────────────────────────────────────────────────────────────────────────────
# IN-MEMORY TF-IDF INDEX
# ─────────────────────────────────────────────────────────────────────────────

class TFIDFIndex:
    """Lightweight TF-IDF search index for offline RAG."""

    def __init__(self):
        self.documents: List[Dict] = []       # Store of raw documents
        self.term_df: Counter = Counter()     # Document frequency per term
        self.doc_vectors: List[Dict] = []     # TF-IDF vectors per document
        self.num_docs: int = 0
        self.built: bool = False

    def add_document(self, doc_id: int, title: str, content: str,
                     doc_type: str = "", plant_name: str = "", tags: str = ""):
        """Add a document to the index."""
        full_text = f"{title} {title} {content} {tags}"  # Title boosted x2
        tokens = preprocess_text(full_text)
        tf = Counter(tokens)
        self.documents.append({
            "id": doc_id,
            "title": title,
            "content": content,
            "doc_type": doc_type,
            "plant_name": plant_name,
            "tags": tags,
            "tokens": tokens,
            "tf": tf,
        })
        # Update document frequency
        for term in set(tokens):
            self.term_df[term] += 1
        self.num_docs += 1

    def build_index(self):
        """Build TF-IDF vectors for all documents."""
        if self.num_docs == 0:
            return

        self.doc_vectors = []
        for doc in self.documents:
            vector = {}
            for term, tf_count in doc["tf"].items():
                tf = tf_count / len(doc["tokens"]) if doc["tokens"] else 0
                df = self.term_df.get(term, 1)
                idf = math.log((self.num_docs + 1) / (df + 1)) + 1.0  # Smoothed IDF
                vector[term] = tf * idf
            self.doc_vectors.append(vector)

        self.built = True
        logger.info(f"TF-IDF index built: {self.num_docs} documents, "
                    f"{len(self.term_df)} unique terms")

    def search(self, query: str, top_k: int = 10, doc_type_filter: str = None) -> List[Dict]:
        """Search the index using cosine similarity with TF-IDF."""
        if not self.built:
            self.build_index()

        query_tokens = preprocess_text(query)
        if not query_tokens:
            return []

        # Build query vector
        query_tf = Counter(query_tokens)
        query_vector = {}
        for term, count in query_tf.items():
            tf = count / len(query_tokens)
            df = self.term_df.get(term, 0)
            if df > 0:
                idf = math.log((self.num_docs + 1) / (df + 1)) + 1.0
                query_vector[term] = tf * idf

        if not query_vector:
            return []

        # Compute cosine similarities
        scores = []
        query_norm = math.sqrt(sum(v**2 for v in query_vector.values()))

        for idx, doc_vector in enumerate(self.doc_vectors):
            doc = self.documents[idx]

            # Apply doc_type filter if specified
            if doc_type_filter and doc.get("doc_type") != doc_type_filter:
                continue

            # Dot product
            dot_product = sum(
                query_vector.get(term, 0) * doc_vector.get(term, 0)
                for term in query_vector
            )

            # Document norm
            doc_norm = math.sqrt(sum(v**2 for v in doc_vector.values()))

            if doc_norm > 0 and query_norm > 0:
                similarity = dot_product / (query_norm * doc_norm)
            else:
                similarity = 0.0

            if similarity > 0:
                scores.append((similarity, idx))

        # Sort by score descending
        scores.sort(reverse=True)
        results = []
        for score, idx in scores[:top_k]:
            doc = self.documents[idx]
            results.append({
                "id": doc["id"],
                "title": doc["title"],
                "content": doc["content"][:500] + "..." if len(doc["content"]) > 500 else doc["content"],
                "doc_type": doc["doc_type"],
                "plant_name": doc["plant_name"],
                "score": round(score, 4),
                "tags": doc["tags"],
            })

        return results


# ─────────────────────────────────────────────────────────────────────────────
# BM25 INDEX (Better than TF-IDF for keyword queries)
# ─────────────────────────────────────────────────────────────────────────────

class BM25Index:
    """BM25 (Best Match 25) ranking function — industry-standard offline retrieval."""

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1  # Term frequency saturation
        self.b = b    # Length normalization
        self.documents: List[Dict] = []
        self.doc_tokens: List[List[str]] = []
        self.term_df: Counter = Counter()
        self.avg_dl: float = 0
        self.num_docs: int = 0
        self.built: bool = False

    def add_document(self, doc_id: int, title: str, content: str,
                     doc_type: str = "", plant_name: str = "", tags: str = ""):
        """Add a document to BM25 index."""
        full_text = f"{title} {title} {content} {tags}"
        tokens = preprocess_text(full_text)
        self.doc_tokens.append(tokens)
        self.documents.append({
            "id": doc_id,
            "title": title,
            "content": content,
            "doc_type": doc_type,
            "plant_name": plant_name,
            "tags": tags,
        })
        for term in set(tokens):
            self.term_df[term] += 1
        self.num_docs += 1

    def build_index(self):
        """Compute average document length."""
        if self.num_docs == 0:
            return
        total_len = sum(len(tokens) for tokens in self.doc_tokens)
        self.avg_dl = total_len / self.num_docs
        self.built = True
        logger.info(f"BM25 index built: {self.num_docs} docs, avg length: {self.avg_dl:.1f} tokens")

    def _bm25_score(self, query_tokens: List[str], doc_idx: int) -> float:
        """Compute BM25 score for a query against a document."""
        tokens = self.doc_tokens[doc_idx]
        dl = len(tokens)
        tf_map = Counter(tokens)
        score = 0.0

        for term in query_tokens:
            if term not in tf_map:
                continue
            tf = tf_map[term]
            df = self.term_df.get(term, 0)
            if df == 0:
                continue
            idf = math.log((self.num_docs - df + 0.5) / (df + 0.5) + 1.0)
            numerator = tf * (self.k1 + 1)
            denominator = tf + self.k1 * (1 - self.b + self.b * dl / self.avg_dl)
            score += idf * (numerator / denominator)

        return score

    def search(self, query: str, top_k: int = 10, doc_type_filter: str = None) -> List[Dict]:
        """BM25 search with optional document type filter."""
        if not self.built:
            self.build_index()

        query_tokens = preprocess_text(query)
        if not query_tokens:
            return []

        scores = []
        for idx, doc in enumerate(self.documents):
            if doc_type_filter and doc.get("doc_type") != doc_type_filter:
                continue
            score = self._bm25_score(query_tokens, idx)
            if score > 0:
                scores.append((score, idx))

        scores.sort(reverse=True)
        results = []
        for score, idx in scores[:top_k]:
            doc = self.documents[idx]
            results.append({
                "id": doc["id"],
                "title": doc["title"],
                "content": doc["content"][:600] + "..." if len(doc["content"]) > 600 else doc["content"],
                "doc_type": doc["doc_type"],
                "plant_name": doc["plant_name"],
                "score": round(score, 4),
                "tags": doc["tags"],
            })

        return results


# ─────────────────────────────────────────────────────────────────────────────
# HYBRID SEARCH ENGINE (TF-IDF + BM25 Ensemble)
# ─────────────────────────────────────────────────────────────────────────────

class HybridSearchEngine:
    """
    Combines TF-IDF and BM25 for more robust offline retrieval.
    - BM25 is better for keyword/specific term queries
    - TF-IDF is better for semantic topic queries
    - Ensemble scores by rank-based fusion
    """

    def __init__(self):
        self.bm25 = BM25Index(k1=1.5, b=0.75)
        self.tfidf = TFIDFIndex()
        self.doc_count = 0

    def add_document(self, doc_id: int, title: str, content: str,
                     doc_type: str = "", plant_name: str = "", tags: str = ""):
        """Add document to both indices."""
        self.bm25.add_document(doc_id, title, content, doc_type, plant_name, tags)
        self.tfidf.add_document(doc_id, title, content, doc_type, plant_name, tags)
        self.doc_count += 1

    def build(self):
        """Build both indices."""
        self.bm25.build_index()
        self.tfidf.build_index()
        logger.info(f"✅ Hybrid Search Engine built with {self.doc_count} documents")

    def search(self, query: str, top_k: int = 10,
               doc_type_filter: str = None, use_bm25: bool = True) -> List[Dict]:
        """
        Hybrid search using Reciprocal Rank Fusion (RRF).
        Combines BM25 and TF-IDF results for robustness.
        """
        k = 60  # RRF constant

        if use_bm25:
            bm25_results = self.bm25.search(query, top_k=top_k * 2, doc_type_filter=doc_type_filter)
            tfidf_results = self.tfidf.search(query, top_k=top_k * 2, doc_type_filter=doc_type_filter)

            # Build RRF score map
            rrf_scores = defaultdict(float)
            result_map = {}

            for rank, doc in enumerate(bm25_results, start=1):
                doc_key = (doc["id"], doc["title"])
                rrf_scores[doc_key] += 1.0 / (k + rank)
                result_map[doc_key] = doc

            for rank, doc in enumerate(tfidf_results, start=1):
                doc_key = (doc["id"], doc["title"])
                rrf_scores[doc_key] += 1.0 / (k + rank)
                if doc_key not in result_map:
                    result_map[doc_key] = doc

            # Sort by RRF score
            sorted_docs = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)

            results = []
            for doc_key, rrf_score in sorted_docs[:top_k]:
                doc = result_map[doc_key]
                doc["rrf_score"] = round(rrf_score, 6)
                results.append(doc)

            return results
        else:
            return self.tfidf.search(query, top_k=top_k, doc_type_filter=doc_type_filter)

    def search_diseases(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search specifically in disease documents."""
        return self.search(query, top_k=top_k, doc_type_filter="disease")

    def search_pests(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search specifically in pest documents."""
        return self.search(query, top_k=top_k, doc_type_filter="pest")

    def search_nutrients(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search specifically in nutrient documents."""
        return self.search(query, top_k=top_k, doc_type_filter="nutrient")

    def search_cultivation(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search specifically in cultivation guides."""
        return self.search(query, top_k=top_k, doc_type_filter="cultivation")


# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL INDEX MANAGER (Singleton pattern)
# ─────────────────────────────────────────────────────────────────────────────

_global_engine: Optional[HybridSearchEngine] = None


def get_search_engine() -> HybridSearchEngine:
    """Get or create the global search engine singleton."""
    global _global_engine
    if _global_engine is None:
        _global_engine = build_search_engine_from_db()
    return _global_engine


def build_search_engine_from_db() -> HybridSearchEngine:
    """Build search engine by loading RAG documents from database."""
    engine = HybridSearchEngine()

    try:
        from database import SessionLocal
        from models_botanical import RagDocument

        db = SessionLocal()
        docs = db.query(RagDocument).all()
        db.close()

        for doc in docs:
            engine.add_document(
                doc_id=doc.id,
                title=doc.title,
                content=doc.content,
                doc_type=doc.document_type,
                plant_name=doc.plant_name or "",
                tags=doc.tags or "",
            )

        engine.build()
        logger.info(f"✅ Search engine loaded {len(docs)} documents from database")

    except Exception as e:
        logger.error(f"Error loading documents from database: {e}")
        # Fall back to in-memory loading from modules
        engine = build_search_engine_from_modules()

    return engine


def build_search_engine_from_modules() -> HybridSearchEngine:
    """Build search engine directly from data modules (no DB required)."""
    from botanical_dataset.diseases_db import DISEASES_MASTER
    from botanical_dataset.pests_db import PESTS_MASTER
    from botanical_dataset.nutrients_db import ESSENTIAL_NUTRIENTS, CROP_FERTILIZER_RECOMMENDATIONS
    from botanical_dataset.cultivation_db import CULTIVATION_DATA

    engine = HybridSearchEngine()
    doc_id = 1

    # Add disease documents
    for plant_name, diseases in DISEASES_MASTER.items():
        for disease in diseases:
            symptoms = disease.get("symptoms", {})
            treatment = disease.get("treatment", {})
            content = f"""
Disease: {disease.get('name')}. Pathogen: {disease.get('pathogen_name')}.
Type: {disease.get('disease_type')}. Host: {disease.get('host_range', plant_name)}.
Symptoms: {symptoms.get('early', '')}. {symptoms.get('late', '')}.
Treatment: {treatment.get('organic', '')} {treatment.get('chemical', '')}.
Prevention: {treatment.get('preventive', '')}.
            """.strip()

            engine.add_document(
                doc_id=doc_id,
                title=f"{disease.get('name')} ({plant_name})",
                content=content,
                doc_type="disease",
                plant_name=plant_name,
                tags=f"{disease.get('disease_type', '')},{plant_name},{disease.get('pathogen_name', '')}",
            )
            doc_id += 1

    # Add pest documents
    for category, pests in PESTS_MASTER.items():
        for pest in pests:
            content = f"""
Pest: {pest.get('name')}. Scientific: {pest.get('scientific_name')}.
Category: {category}. Hosts: {pest.get('host_plants', '')}.
Damage: {pest.get('damage_symptoms', '')}.
Identification: {pest.get('identification', '')}.
Control: {pest.get('organic_control', '')} {pest.get('chemical_control', '')}.
Biological control: {pest.get('biological_control', '')}.
            """.strip()

            engine.add_document(
                doc_id=doc_id,
                title=f"{pest.get('name')} - {category}",
                content=content,
                doc_type="pest",
                plant_name=pest.get("host_plants", "")[:100],
                tags=f"{category},{pest.get('scientific_name', '')}",
            )
            doc_id += 1

    # Add nutrient documents
    for nutrient_name, nutrient in ESSENTIAL_NUTRIENTS.items():
        deficiency = nutrient.get("deficiency", {})
        content = (
            f"Nutrient: {nutrient_name} ({nutrient.get('symbol', '')}).\n"
            f"Type: {nutrient.get('element_type', '')}.\n"
            f"Functions: {', '.join(nutrient.get('functions', []))}.\n"
            f"Deficiency: {deficiency.get('visual_signs', '')}.\n"
            f"Affected leaves: {deficiency.get('affected_leaves', '')}.\n"
            f"Toxicity: {nutrient.get('toxicity', {}).get('visual_signs', '')}.\n"
            f"Fertilizers: {', '.join(str(s) for s in nutrient.get('fertilizer_sources', []))}.\n"
            f"Critical crops: {nutrient.get('critical_crops', '')}."
        ).strip()

        engine.add_document(
            doc_id=doc_id,
            title=f"{nutrient_name} Deficiency and Nutrition",
            content=content,
            doc_type="nutrient",
            plant_name="All",
            tags=f"nutrient,{nutrient_name},{nutrient.get('symbol', '')}",
        )
        doc_id += 1

    # Add cultivation guides
    for crop_name, guide in CULTIVATION_DATA.items():
        climate = guide.get("climate", {})
        soil = guide.get("soil", {})
        irrigation = guide.get("irrigation", {})
        fertilization = guide.get("fertilization", {})
        harvesting = guide.get("harvesting", {})

        content = f"""
Crop: {crop_name}. Botanical: {guide.get('botanical_name', '')}.
Origin: {guide.get('origin', '')}.
Climate: {climate.get('type', '')}. Temperature: {climate.get('temp_optimum_C', '')}.
Soil: {soil.get('type', '')}. pH: {soil.get('ph_range', '')}.
Spacing: {guide.get('spacing', '')}. Seed rate: {guide.get('seed_rate', '')}.
Irrigation: {irrigation.get('method', '')}. Water: {irrigation.get('water_requirement_mm', '')}.
Fertilizer: {fertilization.get('npk_kg_ha', '')}. Schedule: {fertilization.get('schedule', '')}.
Harvest: {harvesting.get('method', '')}. Yield: {harvesting.get('yield_t_ha', '')} t/ha.
            """.strip()

        engine.add_document(
            doc_id=doc_id,
            title=f"{crop_name} Cultivation Guide",
            content=content,
            doc_type="cultivation",
            plant_name=crop_name,
            tags=f"cultivation,{crop_name},{guide.get('botanical_name', '')}",
        )
        doc_id += 1

    engine.build()
    logger.info(f"✅ In-memory search engine built with {doc_id - 1} documents")
    return engine


# ─────────────────────────────────────────────────────────────────────────────
# QUERY EXPANSION (Improve recall with synonyms)
# ─────────────────────────────────────────────────────────────────────────────

QUERY_SYNONYMS = {
    "blast": ["pyricularia", "fungal", "blight"],
    "blight": ["phytophthora", "leaf spot", "necrosis"],
    "wilt": ["fusarium", "bacterial wilt", "ralstonia", "vascular"],
    "yellowing": ["chlorosis", "yellow leaves", "nutrient deficiency"],
    "spots": ["lesions", "pustules", "blight", "spots"],
    "aphid": ["aphids", "myzus", "plant lice"],
    "whitefly": ["bemisia", "whiteflies", "vector"],
    "thrips": ["frankliniella", "thrip", "thripidae"],
    "nematode": ["root knot", "meloidogyne", "nematodes"],
    "nitrogen": ["urea", "n deficiency", "pale green", "chlorosis"],
    "phosphorus": ["phosphate", "p deficiency", "purple leaves", "dap"],
    "potassium": ["potash", "k deficiency", "leaf scorch", "mop"],
    "irrigation": ["watering", "drip", "sprinkler", "water requirement"],
    "fertilizer": ["fertilisation", "npk", "manure", "compost"],
}


def expand_query(query: str) -> str:
    """Expand query with relevant synonyms for better recall."""
    query_lower = query.lower()
    expanded_terms = [query]

    for key, synonyms in QUERY_SYNONYMS.items():
        if key in query_lower:
            expanded_terms.extend(synonyms)

    return " ".join(expanded_terms)


# ─────────────────────────────────────────────────────────────────────────────
# SMART QUERY ROUTER
# ─────────────────────────────────────────────────────────────────────────────

def smart_search(query: str, top_k: int = 5) -> Dict:
    """
    Intelligently route query to the right sub-index and return structured results.
    """
    engine = get_search_engine()
    expanded_query = expand_query(query)
    query_lower = query.lower()

    # Detect query type
    doc_type_filter = None
    if any(word in query_lower for word in ["disease", "blight", "rust", "mold", "rot", "wilt", "virus", "fungal", "bacterial", "spot", "burn"]):
        doc_type_filter = "disease"
    elif any(word in query_lower for word in ["pest", "insect", "aphid", "whitefly", "caterpillar", "worm", "beetle", "bug", "mite", "weevil"]):
        doc_type_filter = "pest"
    elif any(word in query_lower for word in ["nutrient", "deficiency", "fertilizer", "nitrogen", "phosphorus", "potassium", "zinc", "iron", "yellow", "chlorosis"]):
        doc_type_filter = "nutrient"
    elif any(word in query_lower for word in ["grow", "cultivat", "soil", "irrigation", "harvest", "spacing", "planting", "sowing", "yield"]):
        doc_type_filter = "cultivation"

    # Execute search
    results = engine.search(expanded_query, top_k=top_k, doc_type_filter=doc_type_filter)

    # If no results with filter, search all
    if not results and doc_type_filter:
        results = engine.search(expanded_query, top_k=top_k, doc_type_filter=None)

    return {
        "query": query,
        "expanded_query": expanded_query,
        "detected_category": doc_type_filter or "general",
        "results": results,
        "total_results": len(results),
    }


# ─────────────────────────────────────────────────────────────────────────────
# API FUNCTIONS (callable from Flask routes)
# ─────────────────────────────────────────────────────────────────────────────

def search_all(query: str, top_k: int = 10) -> List[Dict]:
    """General search across all document types."""
    engine = get_search_engine()
    return engine.search(query, top_k=top_k)


def search_for_disease(crop: str, symptoms: str, top_k: int = 5) -> List[Dict]:
    """Search for diseases given a crop name and symptom description."""
    query = f"{crop} {symptoms}"
    engine = get_search_engine()
    return engine.search_diseases(query, top_k=top_k)


def search_for_pest(crop: str, pest_description: str, top_k: int = 5) -> List[Dict]:
    """Search for pests given a crop and pest description."""
    query = f"{crop} {pest_description}"
    engine = get_search_engine()
    return engine.search_pests(query, top_k=top_k)


def get_nutrient_diagnosis(symptoms: str, top_k: int = 3) -> List[Dict]:
    """Diagnose nutrient deficiency from symptom description."""
    engine = get_search_engine()
    return engine.search_nutrients(symptoms, top_k=top_k)


def get_cultivation_guide(crop: str, top_k: int = 3) -> List[Dict]:
    """Get cultivation guide for a specific crop."""
    engine = get_search_engine()
    return engine.search_cultivation(crop, top_k=top_k)


# ─────────────────────────────────────────────────────────────────────────────
# TEST AND DEMO
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info("Building search engine from modules...")

    engine = build_search_engine_from_modules()

    # Test searches
    test_queries = [
        ("blast tomato spots", "disease"),
        ("whitefly control pesticide", "pest"),
        ("yellow leaves nitrogen deficiency", "nutrient"),
        ("rice cultivation soil irrigation", "cultivation"),
        ("mango anthracnose treatment", "disease"),
        ("fall armyworm maize", "pest"),
        ("potassium leaf scorch burn", "nutrient"),
        ("cotton planting spacing fertilizer", "cultivation"),
    ]

    print("\n" + "=" * 70)
    print("🌿 AGRO DOCTOR — OFFLINE RAG SEARCH ENGINE TEST")
    print("=" * 70)

    for query, expected_type in test_queries:
        results = engine.search(query, top_k=3, doc_type_filter=expected_type)
        print(f"\n🔍 Query: '{query}' (type: {expected_type})")
        if results:
            for i, r in enumerate(results[:2], 1):
                print(f"   {i}. [{r.get('score', r.get('rrf_score', 0)):.4f}] {r['title']}")
        else:
            results_all = engine.search(query, top_k=2)
            for i, r in enumerate(results_all[:2], 1):
                print(f"   {i}. [{r.get('score', r.get('rrf_score', 0)):.4f}] {r['title']} ({r['doc_type']})")

    print("\n" + "=" * 70)
    print(f"Total indexed documents: {engine.doc_count}")
