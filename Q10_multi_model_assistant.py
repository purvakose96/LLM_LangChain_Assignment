# Q10 - Multi-Model Assistant

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI

# Load API keys
load_dotenv()


# -------------------------------------------------
# Create Groq Model
# -------------------------------------------------

groq_model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)


# -------------------------------------------------
# Create Mistral Model
# -------------------------------------------------

mistral_model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7
)


# -------------------------------------------------
# Display Application
# -------------------------------------------------

print("=" * 60)
print("             MULTI-MODEL LLM ASSISTANT")
print("=" * 60)

print("\nAvailable Models:")
print("1. Groq")
print("2. Mistral")
print("Type 'quit' to exit.")


# -------------------------------------------------
# Main Chat Loop
# -------------------------------------------------

while True:

    print("\n" + "-" * 60)

    # Select model
    choice = input("Select model (1-Groq / 2-Mistral): ").strip()

    # Exit
    if choice.lower() == "quit":
        print("\nAssistant: Goodbye!")
        break

    # Select the model
    if choice == "1":
        model = groq_model
        model_name = "Groq"

    elif choice == "2":
        model = mistral_model
        model_name = "Mistral"

    else:
        print("Invalid choice. Please enter 1 or 2.")
        continue


    # -------------------------------------------------
    # Get User Question
    # -------------------------------------------------

    question = input("Enter your question: ").strip()

    # Exit
    if question.lower() == "quit":
        print("\nAssistant: Goodbye!")
        break

    # Empty question
    if not question:
        print("Please enter a question.")
        continue


    # -------------------------------------------------
    # Generate Response
    # -------------------------------------------------

    try:

        print(f"\nUsing {model_name} model...")

        response = model.invoke(question)

        print("\n" + "=" * 60)
        print(f"{model_name} RESPONSE")
        print("=" * 60)

        print(response.content)

    except Exception as e:

        print("\nError while calling the model:")
        print(e)