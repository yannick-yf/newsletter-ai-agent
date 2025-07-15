"""Agent Tool performing Web Search"""

from agno.agent import Agent
from agno.models.openai.like import OpenAILike

import os
from dotenv import load_dotenv

from newsletter_agent.agent.prompts import NBA_WEB_SEARCH_PROMPT

load_dotenv()

def agent_web_search():

    agent = Agent(
        model=OpenAILike(
            id="gpt-4o-mini-search-preview",
            api_key=os.getenv("OPENAI_API_KEY")
        )
    )

    response = agent.run(NBA_WEB_SEARCH_PROMPT)
    output = response.content  

    return output