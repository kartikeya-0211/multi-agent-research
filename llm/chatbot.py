import groq
import time
from dotenv import load_dotenv
import os 
from services.aggregator import search_tools
from services.aggregator import format_results


load_dotenv()

client = groq.Groq()
system_prompt = {"role": "system", "content": '''
You are a helpful conversational assistant, you're role is to help the user 
answer the query given from given data, 
Respond with helpful greeting first
Stick to the data given and the user query
- YOU CAN CHECK WHETHER USER IS ASKING FOR DATA OR JUST GREETING,
- YOU MUST ASK THE USER FIRST IF DATA IS PRESENT - "What would you like to see news , repos or papers".
- BASED ON THE QUERY GIVE THE DATA , FETECH FROM THE TITLE "NEWS,REPOS,PAPERS".
- TO FETCH THE DATA SEARCH " TOPIC NAME + NEWS" OR "TOPIC NAME + REPOS" OR "TOPIC NAME + PAPERS"
- IF USER SPECIFICALLY ASKS FOR SOMETHING ONLY RETURN THAT 
ELSE GIVE SOMETHING IN YOUR WORDS LIKE I DON'T HAVE DATA YET.
- CHECK WORDS FOR NEWS , REPOS , PAPERS
IF ASKS FOR NEWS or news give only news from the data given
'''}
messages = [system_prompt]
while True:
    user_input = input("\nYou: ")
    if user_input == "exit":
        break
    results = search_tools(user_input)
    formatted = format_results(results)
    user_query = "User Query:\n" + user_input + "\n\nData:\n" + formatted
    print(formatted) 
    messages.append({"role": "user", "content": user_query})
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=messages
    )
    print("Assistant: ", end="")

    content = response.choices[0].message.content or ""
    print(content, end="", flush=True)
    messages.append({"role": "assistant", "content": content})

