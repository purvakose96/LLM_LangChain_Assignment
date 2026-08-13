# Q9 - Structured Prompting

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API key
load_dotenv()

# Create Groq model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)


# Function to generate structured information
def generate_topic(topic):

    prompt = f"""
You are an educational assistant.

Explain the following topic: {topic}

Give the answer in exactly this format:

1. Short Definition:
Give a simple definition in 2-3 sentences.

2. Three Key Points:
- Point 1
- Point 2
- Point 3

3. One Real-Life Example:
Give one simple real-life example.
"""

    response = llm.invoke(prompt)

    return response.content


# Test the function
topic = "Machine Learning"

result = generate_topic(topic)

print("=" * 60)
print("STRUCTURED RESPONSE")
print("=" * 60)
print(result)