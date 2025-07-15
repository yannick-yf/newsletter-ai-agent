from os import getenv
from agno.agent import Agent, RunResponse
from agno.models.openai.like import OpenAILike

import os
from dotenv import load_dotenv

from newsletter_agent.agent.prompt import PROMPT
# from prompt import PROMPT

load_dotenv()

def agent_pipeline_execution():

    agent = Agent(
        model=OpenAILike(
            id="gpt-4o-mini-search-preview",
            api_key=os.getenv("OPENAI_API_KEY")
        )
    )

    response = agent.run(PROMPT)

    # Now you can access the response content
    output = response.content  # or response.text, depending on the agno API

    return output

    # # Save to a variable or process as needed
    # print(f"Response saved: {output}")

    # # Save to file
    # with open("agent_output.txt", "w", encoding="utf-8") as f:
    #     f.write(response.content)