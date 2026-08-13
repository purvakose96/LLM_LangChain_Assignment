# Q2 - API Key Management

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read API keys
groq_api_key = os.getenv("GROQ_API_KEY")
mistral_api_key = os.getenv("MISTRAL_API_KEY")

# Confirm Groq key
if groq_api_key:
    print("GROQ_API_KEY loaded successfully")
else:
    print("GROQ_API_KEY not found")

# Confirm Mistral key
if mistral_api_key:
    print("MISTRAL_API_KEY loaded successfully")
else:
    print("MISTRAL_API_KEY not found")

# Actual keys are NOT printed for security.