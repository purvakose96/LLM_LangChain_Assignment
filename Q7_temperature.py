# Q7 - Temperature Experiment

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API key
load_dotenv()

# Same prompt for all experiments
prompt = "Write a short creative story about a robot learning to cook."

# Temperature values
temperatures = [0.1, 0.7, 1.2]

# Run the prompt with different temperatures
for temp in temperatures:

    print("\n" + "=" * 60)
    print("TEMPERATURE:", temp)
    print("=" * 60)

    # Create model
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=temp
    )

    # Generate response
    response = llm.invoke(prompt)

    # Display response
    print(response.content)