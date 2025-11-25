import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / "config/.env"

load_dotenv(ENV_PATH)

class config:
    DB_URL = os.getenv("DATABASE_URL", None)

    LLM1 = "Groq"
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", None)
    GROQ_MODEL_SMALL = "llama-3.1-8b-instant"
    GROQ_MODEL_LARGE = "meta-llama/llama-4-maverick-17b-128e-instruct"

    LLM2 = "Gemini"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", None)
    GEMINI_MODEL = "gemini-2.5-flash"

    SCHEMA_FILE = "schema/db_schema.json"
    RESPONSE_FILE = "schema/questions_answers.json"

settings = config()