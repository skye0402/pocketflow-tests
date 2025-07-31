from openai import OpenAI
import os
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

def get_tools(server_script_path=None):
    """Get available tools, either from MCP server or locally based on MCP global setting."""
    return mcp_get_tools(server_script_path)
    
def mcp_get_tools(server_script_path):
    """Get available tools from an MCP server.
    """
    async def _get_tools():
        server_params = StdioServerParameters(
            command="python",
            args=[server_script_path]
        )
        
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools_response = await session.list_tools()
                return tools_response.tools
    
    return asyncio.run(_get_tools())

def call_tool(server_script_path=None, tool_name=None, arguments=None):
    """Call a tool, either from MCP server or locally based on MCP global setting."""
    return mcp_call_tool(server_script_path, tool_name, arguments)
    
def mcp_call_tool(server_script_path=None, tool_name=None, arguments=None):
    """Call a tool on an MCP server.
    """
    async def _call_tool():
        server_params = StdioServerParameters(
            command="python",
            args=[server_script_path]
        )
        
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(tool_name, arguments)
                return result.content[0].text
    
    return asyncio.run(_call_tool())

if __name__ == "__main__":
    print("=== Testing call_llm ===")
    prompt = "In a few words, what is the meaning of life?"
    print(f"Prompt: {prompt}")
    response = call_llm(prompt)
    print(f"Response: {response}")

        # Find available tools
    print("=== Finding available tools ===")
    tools = get_tools("simple_server.py")
    
    # Print tool information nicely formatted
    for i, tool in enumerate(tools, 1):
        print(f"\nTool {i}: {tool.name}")
        print("=" * (len(tool.name) + 8))
        print(f"Description: {tool.description}")
        
        # Parameters section
        print("Parameters:")
        properties = tool.inputSchema.get('properties', {})
        required = tool.inputSchema.get('required', [])
        
        # No parameters case
        if not properties:
            print("  None")
        
        # Print each parameter with its details
        for param_name, param_info in properties.items():
            param_type = param_info.get('type', 'unknown')
            req_status = "(Required)" if param_name in required else "(Optional)"
            print(f"  • {param_name}: {param_type} {req_status}")
    
    # Call a tool
    print("\n=== Calling the add tool ===")
    a, b = 5, 3
    result = call_tool("simple_server.py", "add", {"a": a, "b": b})
    print(f"Result of {a} + {b} = {result}")
    
    # You can easily call with different parameters
    a, b = 10, 20
    result = call_tool("simple_server.py", "add", {"a": a, "b": b})
    print(f"Result of {a} + {b} = {result}")
