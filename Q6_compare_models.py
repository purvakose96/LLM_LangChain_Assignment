# Q6 - Compare Groq and Mistral

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI

# Load API keys
load_dotenv()

# Create Groq model
groq_model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# Create Mistral model
mistral_model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)

# Same question for both models
question = "What are the advantages of using LangChain?"

# Get Groq response
groq_response = groq_model.invoke(question)

# Get Mistral response
mistral_response = mistral_model.invoke(question)

# Display Groq response
print("=" * 60)
print("GROQ RESPONSE")
print("=" * 60)
print(groq_response.content)

# Display Mistral response
print("\n" + "=" * 60)
print("MISTRAL RESPONSE")
print("=" * 60)
print(mistral_response.content)