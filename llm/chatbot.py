import groq 
import os
from dotenv import load_dotenv
from services.aggregator import search_tools, format_results
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
  if user_input.lower() == "exit":
     break 
  
  topic = extract_topic(user_input)
  results = search_tools(topic)
  formatted = format_results(results)
  
  user_query = "User Query: \n" + user_input + "\n\nData:\n" + formatted
  current_messages = messages + [{"role": "user", "content": user_query}]
  
  response = client.chat.completions.create(
	model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=current_messages
  )
  content = response.choices[0].message.content or ""
  print("Assistant: "+ content)
  
  messages.append({"role": "user", "content": user_input})
  messages.append({"role": "assistant", "content": content})