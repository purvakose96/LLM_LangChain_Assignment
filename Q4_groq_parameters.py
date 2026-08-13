# Q4 - Controlling LLM Output with Parameters

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API key
load_dotenv()

# Create Groq model with parameters
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=50
)

# Prompt
prompt = "Introduce yourself in 3 sentences."

# Get response
response = llm.invoke(prompt)

# Display response
print("Groq Response:")
print(response.content)

print("\nParameters Used:")
print("Temperature: 0.2")
print("Max Tokens: 50")