"""Agent Tool summerizing information gather by agent tools"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat

import os
from dotenv import load_dotenv

from textwrap import dedent

from newsletter_agent.agent.prompts import FINAL_SUMMARY_PROMPT
from newsletter_agent.agent.web_search import nba_results_web_search_tool, general_sports_results_web_search_tool
from newsletter_agent.utilis.get_date import get_date_of_yesterday

load_dotenv()

def output_formating():

    yesterday_date = get_date_of_yesterday()
    nba_results = nba_results_web_search_tool()
    sports_summary = general_sports_results_web_search_tool()

    # Prompt
    prompt = dedent(FINAL_SUMMARY_PROMPT).format(yesterday_date=yesterday_date, nba_results=nba_results, sports_summary=sports_summary)

    agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        markdown=False,
    )

    response = agent.run(prompt)
    output = response.content  

    return output