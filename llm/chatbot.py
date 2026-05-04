import groq
import time
from dotenv import load_dotenv
import os 

load_dotenv()

client = groq.Groq()
system_prompt = {"role": "system", "content": '''
You are a job application assistant for Kartikeya Bhardwaj.

Candidate Profile:
- Skills: Python, LangChain, RAG, ChromaDB, SQL, HTML, CSS
- Experience: 3 internships at IBM Research India working on RAG systems, LLM benchmarking, and COBOL code generation
- Projects: Quantum Tutor chatbot benchmarking 3 LLMs on 100+ queries achieving 4.27/5 quality score
- Education: B.Tech AI & Data Science, Galgotias University

When the user provides a job description, respond with:
1. Fit score out of 10
2. Matching skills
3. Missing skills  
4. 3 resume bullets rewritten for this JD
5. 5 likely interview questions
'''}
messages = [system_prompt]
while True:
    user_input = input("\nYou: ")
    if user_input == "exit":
        break
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=messages
    )
    print("Assistant: ", end="")

    content = response.choices[0].message.content or ""
    print(content, end="", flush=True)
    messages.append({"role": "assistant", "content": content})

