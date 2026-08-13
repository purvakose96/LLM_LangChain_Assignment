# Q3 - Basic LLM Call Using Groq

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API key from .env
load_dotenv()

# Create Groq model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# Prompt
prompt = "Introduce yourself in 3 sentences."

# Send prompt to Groq
response = llm.invoke(prompt)

# Display response
print("Groq Response:")
print(response.content)