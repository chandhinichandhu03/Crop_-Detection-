"""
export_sql.py
Generates a complete PostgreSQL-compatible SQL dump file.
"""

import os
import sys
import logging
from datetime import datetime
from sqlalchemy.inspection import inspect
from sqlalchemy.sql.sqltypes import Integer, String, Float, Text, Boolean, DateTime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal
from models_botanical import (
    TaxonomyFull, PlantDisease, PlantPest, NutrientDeficiency,
    MultilingualName, CultivationGuide, RagDocument,
    MedicinalKnowledge, NutritionFacts, SeedData
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

SQL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "dataset", "exports", "sql"))

TABLES_TO_EXPORT = [
    ("taxonomy_full", TaxonomyFull),
    ("plant_diseases", PlantDisease),
    ("plant_pests", PlantPest),
    ("botanical_nutrients", NutrientDeficiency),
    ("multilingual_names", MultilingualName),
    ("cultivation_guides", CultivationGuide),
    ("rag_documents", RagDocument),
    ("medicinal_knowledge", MedicinalKnowledge),
    ("nutrition_facts", NutritionFacts),
    ("seed_data", SeedData)
]

def map_type_to_postgres(col_type) -> str:
    """Map SQLAlchemy types to Postgres SQL types."""
    if isinstance(col_type, Integer):
        return "INTEGER"
    elif isinstance(col_type, Float):
        return "DOUBLE PRECISION"
    elif isinstance(col_type, String):
        length = getattr(col_type, 'length', 255)
        return f"VARCHAR({length or 255})"
    elif isinstance(col_type, Text):
        return "TEXT"
    elif isinstance(col_type, Boolean):
        return "BOOLEAN"
    elif isinstance(col_type, DateTime):
        return "TIMESTAMP"
    return "TEXT"

def clean_sql_val(val) -> str:
    """Escape and format value for INSERT statements."""
    if val is None:
        return "NULL"
    if isinstance(val, bool):
        return "TRUE" if val else "FALSE"
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, datetime):
        return f"'{val.strftime('%Y-%m-%d %H:%M:%S')}'"
    if isinstance(val, (list, dict)):
        import json
        escaped = json.dumps(val).replace("'", "''")
        return f"'{escaped}'"
        
    escaped = str(val).replace("'", "''")
    return f"'{escaped}'"

def export_all_to_sql():
    """Generate PostgreSQL SQL dump file."""
    db = SessionLocal()
    os.makedirs(SQL_DIR, exist_ok=True)
    sql_file_path = os.path.join(SQL_DIR, "botanical_dataset_postgres.sql")
    
    logger.info(f"Generating Postgres SQL dump at: {sql_file_path}")
    
    try:
        with open(sql_file_path, "w", encoding="utf-8") as f:
            f.write("-- Agro Doctor Botanical Intelligence Dataset PostgreSQL Dump\n")
            f.write(f"-- Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("BEGIN;\n\n")
            
            for table_name, model in TABLES_TO_EXPORT:
                logger.info(f"Generating SQL schema and inserts for {table_name}...")
                
                # Get column details
                columns = inspect(model).columns
                
                # Write DROP/CREATE TABLE
                f.write(f"DROP TABLE IF EXISTS {table_name} CASCADE;\n")
                f.write(f"CREATE TABLE {table_name} (\n")
                
                col_defs = []
                for col in columns:
                    pg_type = map_type_to_postgres(col.type)
                    primary_key = " PRIMARY KEY" if col.primary_key else ""
                    nullable = " NULL" if col.nullable else " NOT NULL"
                    col_defs.append(f"    {col.name} {pg_type}{primary_key}{nullable}")
                    
                f.write(",\n".join(col_defs))
                f.write("\n);\n\n")
                
                # Query all records
                records = db.query(model).all()
                if records:
                    col_names = [col.name for col in columns]
                    f.write(f"-- Data for {table_name} ({len(records)} rows)\n")
                    
                    # Batch inserts to keep the SQL file size reasonable and fast to parse
                    batch_size = 100
                    for i in range(0, len(records), batch_size):
                        batch = records[i:i+batch_size]
                        cols_str = ", ".join(col_names)
                        f.write(f"INSERT INTO {table_name} ({cols_str}) VALUES\n")
                        
                        rows_str = []
                        for r in batch:
                            vals = [clean_sql_val(getattr(r, col_name)) for col_name in col_names]
                            rows_str.append("    (" + ", ".join(vals) + ")")
                        
                        f.write(",\n".join(rows_str) + ";\n")
                    f.write("\n")
                    
            f.write("COMMIT;\n")
            logger.info("✅ Postgres SQL dump generated successfully!")
            
    except Exception as e:
        logger.error(f"❌ Failed to generate SQL dump: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    export_all_to_sql()
