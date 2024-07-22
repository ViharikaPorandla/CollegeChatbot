# 🎓 College Query Chatbot

This chatbot is designed to help students clear their doubts about college-related queries using Natural Language Processing (NLP) and Machine Learning techniques.

## 📚 Project Overview

The project involved:
- 🗂️ Collecting data related to common college queries.
- 📝 Converting the data into a JSON file format.
- 🤖 Using the NLTK library to process the data and train the model.
- 🧪 Testing the chatbot with various questions to ensure accurate responses.

## 🚀 Features

- **Interactive Chatbot**: Responds to college-related queries.
- **NLP Processing**: Utilizes the NLTK library for natural language understanding.
- **JSON Data Handling**: Stores and processes data in JSON format.

## 📦 Installation

### Prerequisites

- 🐍 Python 3.x
- 📦 pip (Python package installer)

### Steps

pip install nltk

Download NLTK Data:

Open a Python shell or create a Python script and run the following code to download the necessary NLTK data files:


import nltk
nltk.download('punkt')
📝 Create and Run the Chatbot Script
Create the chatbot.py Script:

Save the following code into a file named chatbot.py:

import random
import nltk
from nltk.tokenize import word_tokenize
import json

# Download NLTK data (only need to run this once)
nltk.download('punkt')

# Load JSON data
with open('data.json') as f:
    data = json.load(f)

def get_response(user_input):
    tokens = word_tokenize(user_input.lower())
    for item in data:
        if any(word in tokens for word in item['keywords']):
            return item['response']
    return "I'm not sure how to respond to that. Can you ask something else?"

def chatbot():
    print("Hello! I'm here to help you with your college queries. How can I assist you today?")

    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")

# Run the chatbot function
chatbot()
Create the data.json File:
Create a file named data.json and populate it with your college-related query data.
Here's an example structure:

json
[
    {
        "keywords": ["admission", "apply"],
        "response": "You can apply for admission through our online portal. Visit our website for more details."
    },
    {
        "keywords": ["courses", "programs"],
        "response": "We offer a variety of courses in multiple disciplines. Check out our course catalog on the website."
    },
    {
        "keywords": ["fees", "tuition"],
        "response": "The tuition fees vary by program. Please visit the fees section on our website for detailed information."
    }
]
Run the Chatbot:
In your command prompt or terminal, navigate to the project directory and run the script:
python chatbot.py
