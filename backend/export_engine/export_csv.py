"""
export_csv.py
Exports all botanical intelligence dataset tables to CSV format.
"""

import os
import csv
import sys
import logging
from sqlalchemy.inspection import inspect

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal
from models_botanical import (
    TaxonomyFull, PlantDisease, PlantPest, NutrientDeficiency,
    MultilingualName, CultivationGuide, RagDocument,
    MedicinalKnowledge, NutritionFacts, SeedData
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

EXPORT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "dataset", "exports", "csv"))

TABLES_TO_EXPORT = {
    "taxonomy_full": TaxonomyFull,
    "plant_diseases": PlantDisease,
    "plant_pests": PlantPest,
    "botanical_nutrients": NutrientDeficiency,
    "multilingual_names": MultilingualName,
    "cultivation_guides": CultivationGuide,
    "rag_documents": RagDocument,
    "medicinal_knowledge": MedicinalKnowledge,
    "nutrition_facts": NutritionFacts,
    "seed_data": SeedData
}

def export_all_to_csv():
    """Export all botanical tables to CSV."""
    db = SessionLocal()
    os.makedirs(EXPORT_DIR, exist_ok=True)
    
    logger.info(f"Starting CSV exports to: {EXPORT_DIR}")
    
    for table_name, model in TABLES_TO_EXPORT.items():
        csv_file_path = os.path.join(EXPORT_DIR, f"{table_name}.csv")
        try:
            # Get model column names
            columns = [c.key for c in inspect(model).mapper.column_attrs]
            
            # Query all records
            records = db.query(model).all()
            
            with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
                # Write header
                writer.writerow(columns)
                
                # Write data rows
                for r in records:
                    row = [getattr(r, col) for col in columns]
                    # Format None or lists/dicts
                    formatted_row = []
                    for val in row:
                        if val is None:
                            formatted_row.append("")
                        elif isinstance(val, (list, dict)):
                            import json
                            formatted_row.append(json.dumps(val))
                        else:
                            formatted_row.append(str(val))
                    writer.writerow(formatted_row)
                    
            logger.info(f"✅ Exported {len(records)} records to {table_name}.csv")
            
        except Exception as e:
            logger.error(f"❌ Failed to export table {table_name}: {e}")
            
    db.close()

if __name__ == "__main__":
    export_all_to_csv()
