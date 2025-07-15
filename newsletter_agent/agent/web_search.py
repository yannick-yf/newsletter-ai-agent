"""Agent Tool performing Web Search"""

from agno.agent import Agent
from agno.models.openai.like import OpenAILike

import os
from dotenv import load_dotenv

from newsletter_agent.agent.prompts import NBA_WEB_SEARCH_PROMPT, SPORTS_RESULTS_WEB_SEARCH_PROMPT
from newsletter_agent.utilis.get_date import get_date_of_yesterday
load_dotenv()

def nba_results_web_search_tool():

    yesterday_date = get_date_of_yesterday()

    agent = Agent(
        model=OpenAILike(
            id="gpt-4o-mini-search-preview",
            api_key=os.getenv("OPENAI_API_KEY")
        )
    )

    response = agent.run(NBA_WEB_SEARCH_PROMPT.format(yesterday_date=yesterday_date))
    output = response.content  

    return output