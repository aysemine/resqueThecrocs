import requests

# MCP Client 
class MCPClient:
    def __init__(self, server_url):
        self.server_url = server_url
        self.manifest = requests.get(f"{server_url}/.well-known/mcp.json").json()
        self.tools = {tool["name"]: tool for tool in self.manifest.get("tools", [])}

    def call_tool(self, tool_name, args):
        if tool_name not in self.tools:
            raise ValueError(f"Tool {tool_name} was not found.")
        endpoint = f"/{tool_name}"
        resp = requests.post(f"{self.server_url}{endpoint}", json=args)
        return resp.json()



