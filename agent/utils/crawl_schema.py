import json
from sqlalchemy import create_engine, inspect

from config.config import settings

#===
database_engine = settings.DB_URL
schema_file = settings.SCHEMA_FILE
#===

engine = create_engine(database_engine)
inspector = inspect(engine)

db_schema = {"tables": {}, "relationships": []}

tables = inspector.get_table_names(schema="public")

def crawl_schema():

    for table in tables:
        columns = [col["name"] for col in inspector.get_columns(table, schema="public")]
        db_schema["tables"][table] = columns

        fks = inspector.get_foreign_keys(table, schema="public")
        for fk in fks:
            db_schema["relationships"].append({
                "from": table,
                "to": fk["referred_table"],
                "via": fk["constrained_columns"][0]
            })

    with open(schema_file, "w") as f:
        json.dump(db_schema, f, indent=4)

    return "Schema extracted successfully!"