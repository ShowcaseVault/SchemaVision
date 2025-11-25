
from langchain_groq import ChatGroq

from config.config import settings
# -----
# Load Configuration
GROQ_API_KEY = settings.GROQ_API_KEY
GROQ_MODEL = settings.GROQ_MODEL_LARGE
# -----

# ----------------------------
# Initialize LLM
groq = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=GROQ_MODEL,
    temperature=0
)
# ----------------------------
