import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Missing Groq API Key. Please add it to the .env file.")
