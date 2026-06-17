import os
from dotenv import load_dotenv

# Parse the .env file and assign variables to os.environ
load_dotenv() 

# Access your keys safely
HF_TOKEN = os.getenv("HF_TOKEN")

# in mode_loader.py (top)
import os
os.environ["TRANSFORMERS_NO_TORCHVISION"] = "1"

if HF_TOKEN:
    os.environ["HF_TOKEN"] = HF_TOKEN


from sentence_transformers import SentenceTransformer

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model