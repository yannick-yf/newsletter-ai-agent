"""Prompts collection used by the agent"""

NBA_WEB_SEARCH_PROMPT = """
    Give me the nba games results for the game of the 19th of March 2025.
"""

FINAL_SUMMARY_PROMPT = """\
        You are a sports news reporter.

        Your task is to write an article-style summary of the NBA results from yesterday. 
        The output should be formatted in HTML and include the date (yesterday) right after the article title.

        Use a journalistic tone suitable for a sports news website.

        Yesterday's date: {yesterday_date}
        NBA results: {nba_results}
    """