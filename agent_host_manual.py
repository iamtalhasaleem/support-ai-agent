import asyncio
import json
from openai import OpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 1. Initialize OpenAI Client
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# 2. Connection details for your MCP Server
server_params = StdioServerParameters(
    command="python",
    args=["mcp_server.py"]
)

async def run_agent(ticket_text: str):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # --- STEP A: Get Tools from MCP Server ---
            mcp_tools = await session.list_tools()
            
            # Convert MCP tools into OpenAI Function format
            openai_tools = [
                {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.inputSchema # FastMCP generates this automatically!
                    }
                } for tool in mcp_tools.tools
            ]

            # --- STEP B: Ask the AI what to do ---
            messages = [
                {"role": "system", "content": "You are a Server Admin Agent. Use the provided tools to resolve client tickets."},
                {"role": "user", "content": ticket_text}
            ]

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                tools=openai_tools,
                tool_choice="auto"
            )

            response_message = response.choices[0].message
            tool_calls = response_message.tool_calls

            # --- STEP C: Execute Tool (if the AI asked to) ---
            if tool_calls:
                messages.append(response_message)
                
                for tool_call in tool_calls:
                    function_name = tool_call.function.name
                    args = json.loads(tool_call.function.arguments)
                    
                    print(f"AI requested tool: {function_name} with {args}")

                    # Call the ACTUAL MCP tool
                    result = await session.call_tool(function_name, args)
                    tool_output = result.content[0].text

                    # Give the result back to the AI
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": function_name,
                        "content": tool_output
                    })

                # --- STEP D: Final AI Response ---
                final_response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages
                )
                print(f"\nAI Final Reply: {final_response.choices[0].message.content}")

if __name__ == "__main__":
    ticket = "My website is slow, can you check the server status and restart the web service if needed?"
    asyncio.run(run_agent(ticket))