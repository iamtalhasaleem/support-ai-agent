import asyncio
import os
from aioconsole import ainput
from openai import AsyncOpenAI  # Import OpenAI client
from agents import Agent, Runner
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv

load_dotenv()

# Initialize the OpenAI client to manage conversations
openai_client = AsyncOpenAI()

# 1. Server Configuration
mcp_config = MCPServerStdio(
    name="Hosting-Ops",
    params={
        "command": "python",
        "args": ["mcp_server.py"]
    },
    client_session_timeout_seconds=60.0,
    max_retry_attempts=0
)

# 2. Agent Definition
admin_agent = Agent(
    name="Hosting Support Agent",
    model="gpt-5-mini",
    instructions="""You are a technical support agent for a hosting company. 
    Use the provided tools to check server status or restart services.""",
    mcp_servers=[mcp_config]
)
async def main():
    print("Connecting to MCP Server...")
    await mcp_config.connect() 

    # --- MEMORY FIX START ---
    print("Initializing Conversation Memory...")
    conversation = await openai_client.conversations.create()
    conv_id = conversation.id
    # --- MEMORY FIX END ---

    print("--- 🤖 AI Hosting Agent Ready ---")
    print(f"Session ID: {conv_id}")
    
    # WRAP THE ENTIRE LOOP IN A TRY/FINALLY
    try:
        while True:
            try:
                user_ticket = await ainput("\nTicket > ")
            except EOFError:
                break 
            
            if user_ticket.lower() in ["exit", "quit", "q"]:
                print("Shutting down safely...")
                break
            
            if not user_ticket.strip():
                continue

            print("=========================================================")
            print("Agent is thinking...")
            print("=========================================================")

            try:
                result = await Runner.run(
                    admin_agent, 
                    input=user_ticket,
                    conversation_id=conv_id
                )
                print(f"\n[Agent]: {result.final_output}")
                print("=========================================================")
            except Exception as e:
                print(f"Agent Error: {e}")

    finally:
        # MOVE THIS HERE: It only runs once when you exit the while loop
        print("\nCleaning up MCP connection...")
        try:
            await mcp_config.cleanup()
            # Small sleep to let Windows release file handles
            await asyncio.sleep(0.1) 
        except Exception as e:
            print(f"Cleanup error (non-fatal): {e}")
        
        print("--- 🤖 Session Ended ---")

if __name__ == "__main__":
    import sys
    import asyncio
    import os

    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass