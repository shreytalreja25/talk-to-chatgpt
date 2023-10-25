import openai
import requests
import re
from colorama import Fore, Style, init
import datetime

init()

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

api_key = "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"  # Replace with your OpenAI API key (enclosed in double quotes)
chatbot_rules = open_file('chatbot1.txt')

def chatgpt(api_key, chatbot_rules, user_prompt, temperature=0.9, frequency_penalty=0.2, presence_penalty=0):
    openai.api_key = api_key
    conversation = f"User: {user_prompt}\nChatbot:{chatbot_rules}\n"
    
    completion = openai.Completion.create(
        engine="text-davinci-003",  # You can specify a different engine if needed
        prompt=conversation,
        temperature=temperature,
        max_tokens=150  # Adjust the maximum response length as needed
    )
    
    chat_response = completion.choices[0].text
    return chat_response

def print_colored(agent, text):
    agent_colors = {
        "Chatbot:": Fore.YELLOW,
    }
    color = agent_colors.get(agent, "")
    print(color + f"{agent} {text}" + Style.RESET_ALL)

while True:
    user_prompt = input("You: ")
    response = chatgpt(api_key, chatbot_rules, user_prompt)
    print_colored("Chatbot:", response)
