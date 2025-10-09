from mcp import MCPClient
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Start MCP Client
conservation_status_mcp = MCPClient("https://resquethecrocs.onrender.com")
print("Tools:", list(conservation_status_mcp.tools.keys()))

# Prompt
prompt = """
A crocodile weighs 40 kg, is 2.8 meters long, is male, and lives in a freshwater habitat. Its species is Crocodylus niloticus. What is its conservation status?
"""

# OpenAI GPT-4o request function
def stream_llm_response(prompt):
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an assistant that works with ResqueTheCrocs MCP API."},
            {"role": "user", "content": prompt},      
        ],
        stream=True
    )
    for chunk in response:
        delta = chunk.choices[0].delta
        if delta and getattr(delta, "content", None):
            yield delta.content

# usage
print("LLM answer (streaming):\n")
for token in stream_llm_response(prompt):
    print(token, end="", flush=True)
print("\n---\n")

