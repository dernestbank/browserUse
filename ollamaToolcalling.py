from langchain_ollama import ChatOllama
from browser_use import Agent
from pydantic import SecretStr

from dotenv import load_dotenv
load_dotenv()
import os
os.environ["ANONYMIZED_TELEMETRY"] = "false"

llm_model = "qwen2.5:latest"
#qwne2.5
# "qwen2.5:7b"

# Initialize the model
llm=ChatOllama(model=llm_model, num_ctx=32000)


perplexity_prompt = f"""
Go to https://www.perplexity.ai/finance/TSLA and extract information about their most recent earnings.
"""
promt2= f"""
got to url https://www.forexfactory.com/calendar and report on what you see
"""

# Create agent with the model
# agent = Agent(
#     task= perplexity_prompt,
#     llm=llm
# )

import asyncio, time
async def main():
    agent = Agent(
        task=perplexity_prompt,
        llm=llm,
        
        max_actions_per_step = 1,
        max_failures= 3,
        
        tool_call_in_content = False,

    )
    result = await agent.run()
    
    print(result)

		
asyncio.run(main())