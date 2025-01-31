# API Keys and Configuration
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Raise error if API key is missing
if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key. Set it in .env file.")
