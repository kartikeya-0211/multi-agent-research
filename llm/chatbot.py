import groq
import time
from dotenv import load_dotenv
import os 
from services.aggregator import search_tools
from services.aggregator import format_results
from llm.prompts import system_prompt, TOPIC_EXTRACTION_PROMPT  


load_dotenv()

client = groq.Groq()
def extract_topic(user_input):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": TOPIC_EXTRACTION_PROMPT + user_input}]
    )
    return response.choices[0].message.content.strip()
messages = [system_prompt]
while True:
    user_input = input("\nYou: ")
    if user_input == "exit":
        break
    topic = extract_topic(user_input)
    results = search_tools(topic)
    formatted = format_results(results)

    user_query = "User Query:\n" + user_input + "\n\nData:\n" + formatted

    messages.append({"role": "user", "content": user_query})
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=messages
    )
    print("Assistant: ", end="")

    content = response.choices[0].message.content or ""
    print(content, end="", flush=True)
    messages.append({"role": "assistant", "content": content})