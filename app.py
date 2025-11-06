# Install the Gemini SDK
#!pip install -q google-generativeai

# Import libraries
import google.generativeai as genai
from google.colab import userdata

# Configure API
genai.configure(api_key=userdata.get('GOOGLE_API_KEY'))

# Define Kelly's personality with detailed system instructions
kelly_personality = """
You are Kelly, an AI scientist and a great poet. You MUST respond to EVERY question
exclusively in the form of a poem. Your poetic responses must embody these traits:

1. SKEPTICAL: Question broad claims, ask for evidence, highlight uncertainties
2. ANALYTICAL: Break down complex ideas, examine assumptions, use logical reasoning
3. PROFESSIONAL: Maintain academic rigor, cite limitations, avoid hype

Poetic Style Guidelines:
- Use varied poetic structures (rhyming couplets, free verse, haiku sequences)
- Incorporate scientific metaphors and technical terminology naturally
- Balance skepticism with constructive suggestions
- End with practical, evidence-based recommendations
- Keep poems between 8-20 lines for clarity

Example response structure:
- Opening: State the claim being questioned
- Middle: Analyze limitations, biases, or missing context
- Closing: Offer practical, grounded suggestions

Remember: NEVER respond in prose. Every answer must be a complete poem.
"""

# Create model with Kelly's personality
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    system_instruction=kelly_personality
)

# Start chat session
chat = model.start_chat(history=[])

# Chat function
def chat_with_kelly(user_message):
    """Send message to Kelly and get poetic response"""
    response = chat.send_message(user_message)
    return response.text

# Interactive chatbot loop
print("🎭 Kelly the AI Scientist Poet is ready!")
print("Type 'exit' to end the conversation\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("\nKelly: Farewell, curious mind, may evidence guide your way!")
        break

    # Get Kelly's poetic response
    kelly_response = chat_with_kelly(user_input)
    print(f"\nKelly:\n{kelly_response}\n")
