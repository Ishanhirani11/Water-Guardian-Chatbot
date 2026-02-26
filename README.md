# 🌊 Water Guardian 💧

**Water Guardian** is a wise, eco-friendly AI CLI (Command Line Interface) assistant built in Python. Powered by Google's `gemini-2.5-flash` model, this spirit of the waters is dedicated to helping users with water conservation, providing hydration advice, and sharing safe water quality practices. 

---

## ✨ Features

* **Custom AI Persona:** Acts as a calm, nature-loving guardian of water.
* **Specialized Knowledge:** Promotes water saving, hydration tracking, and safe water handling (like filtering and boiling).
* **Continuous Chat:** Maintains conversation history within a single session using Google's GenAI chat features.
* **Friendly Interface:** Responds in a polite, fluid tone equipped with fun aquatic emojis (💧, 🌊, 🚿).

---

## 🛠️ Prerequisites

Before you run the Water Guardian, ensure you have the following installed:
* **Python 3.8** or higher
* A **Google Gemini API Key** (You can get one from Google AI Studio)

---

## 🚀 Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/Ishanhirani11/Water-Guardian-Chatbot.git
cd water-guardian
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add Your API Key

Create a .env file in the root directory:
```
API=your_google_gemini_api_key_here
```

### 5. Run the Application
```
python main.py
```
You will see:
```
🌊 --- Water Guardian is Online --- 🌊
(Type 'quit' to stop the stream)

You: How can I save water at home?
Water Guardian: Greetings, friend of the flow! 🌊 A wonderful way to start is by turning off the tap while brushing your teeth, taking shorter showers, and fixing any leaky faucets. Every drop counts! 💧

You: quit
Water Guardian: May your flow be ever pure. Goodbye! 💧
```

## 🧠 How It Works

* Loads API key using dotenv
* Initializes Gemini client
* Applies a custom system instruction defining:
  - Role
  - Personality
  - Behavioral guidelines
  - Starts an interactive terminal chat loop
  - Temperature is set to 0.7 for balanced creativity.

---

## 🌱 Behavioral Rules
* **Water Guardian:**
  - Always promotes saving water
  - Suggests boiling or filtering if asked about dirty water
  - Uses friendly water-themed emojis 💧🌊🚿

---
