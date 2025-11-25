import os
import json

from config.config import settings

# -----
# Load Configuration
SCHEMA_FILE_PATH = settings.SCHEMA_FILE
# -----

# ----------------------------
# Helper: load schema
# ----------------------------
def load_schema():
    # 1. Check if file exists
    if not os.path.exists(SCHEMA_FILE_PATH):
        print(f"Warning: {SCHEMA_FILE_PATH} does not exist.")
        return {}

    # 2. Check if file is empty
    if os.path.getsize(SCHEMA_FILE_PATH) == 0:
        print(f"Warning: {SCHEMA_FILE_PATH} is empty.")
        return {}

    # 3. Safe Load
    try:
        with open(SCHEMA_FILE_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: {SCHEMA_FILE_PATH} contains invalid JSON.")
        return {}

# ----------------------------
# Tool: read schema
# ----------------------------
def read_schema():
    schema = load_schema()
    return json.dumps(schema, indent=2) if schema else "Schema is empty."

