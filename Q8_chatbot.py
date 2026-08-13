# Q8 - Simple Chatbot

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API key
load_dotenv()

# Create Groq model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

print("=" * 50)
print("       SIMPLE GROQ CHATBOT")
print("=" * 50)
print("Type 'exit' to stop the chatbot.")

# Chat loop
while True:

    user_input = input("\nYou: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Check empty input
    if user_input.strip() == "":
        print("Chatbot: Please enter a question.")
        continue

    try:
        # Send user input to Groq
        response = llm.invoke(user_input)

        # Display response
        print("Chatbot:", response.content)

    except Exception as e:
        print("Error:", e)