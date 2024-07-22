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
