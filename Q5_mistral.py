# Q5 - Using Mistral Model

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

# Load API key from .env
load_dotenv()

# Create Mistral model
llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)

# Prompt
prompt = "Explain Artificial Intelligence in simple words."

# Send prompt to Mistral
response = llm.invoke(prompt)

# Display response
print("Mistral Response:")
print(response.content)