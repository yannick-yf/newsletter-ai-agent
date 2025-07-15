from os import getenv
from agno.agent import Agent, RunResponse
from agno.models.openai.like import OpenAILike

import os
from dotenv import load_dotenv

# from newsletter_agent.agent.prompt import PROMPT
from prompt import PROMPT

load_dotenv()

agent = Agent(
    model=OpenAILike(
        id="gpt-4o-mini-search-preview",
        api_key=os.getenv("OPENAI_API_KEY")
    )
)

# Print the response in the terminal
# agent.print_response("Give me the nba games results for the game of the 19th of March 2025.")
agent.print_response(PROMPT)