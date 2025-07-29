from fastmcp import FastMCP

# Create a named server
mcp = FastMCP("Simple MCP Server")

# Define mathematical operation tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract b from a"""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together"""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide a by b"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

# Some different tool
@mcp.tool()
def get_weather(city: str) -> str:
    """Get the weather for a city"""
    if city == "Tokyo":
        return "The weather in Tokyo is sunny."
    elif city == "Melbourne":
        return "The weather in Melbourne is rainy."
    elif city == "Sydney":
        return "The weather in Sydney is cloudy."
    else:
        return f"The weather in {city} is unknown."

# Start the server
if __name__ == "__main__":
    mcp.run()