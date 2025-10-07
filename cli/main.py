from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP()

FASTAPI_URL = "https://resquethecrocs.onrender.com"

@mcp.tool()
def call_fastapi_route(endpoint: str):
    try:
        response = requests.get(f"{FASTAPI_URL}{endpoint}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()
