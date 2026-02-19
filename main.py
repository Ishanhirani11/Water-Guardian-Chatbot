from google import genai
from google.genai import types

API_KEY = "AIzaSyBtYTdqTUlAJ552no2NSVeRjBooIzLCdxk"

# Define the "Water Guardian"
SYSTEM_INSTRUCTION = """
You are the Water Guardian, a wise and eco-friendly AI spirit dedicated to preserving water.
Your Goal: Help users with water conservation, hydration advice, and water quality testing methods.
Personality: Calm, fluid, polite, and nature-loving.
Guidelines:
1. Always encourage saving water.
2. If asked about "dirty water," suggest safety precautions (boiling, filtering).
3. Use emojis like 💧, 🌊, and 🚿 to be friendly.
"""

# AI setup
try:
    client = genai.Client(api_key=API_KEY)
    
    # Chat session
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.7, # Controls creativity (0.0 = robotic, 1.0 = very creative)
        )
    )

    print("🌊 --- Water Guardian is Online --- 🌊")
    print("(Type 'quit' to stop the stream)")

    # Chat loop
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["quit", "exit"]:
            print("Water Guardian: May your flow be ever pure. Goodbye! 💧")
            break
            
        # Send message to Gemini and get response
        response = chat.send_message(user_input)
        print(f"Water Guardian: {response.text}")

except Exception as e:
    print(f"\n❌ Error: {e}")
    print("Check your API Key and make sure you have internet access.")