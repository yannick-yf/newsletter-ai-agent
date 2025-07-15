"""Prompts collection used by the agent"""

NBA_WEB_SEARCH_PROMPT = """
    Give me the nba games results for the game of {yesterday_date}.
"""

NBA_WEB_SEARCH_PROMPT_OLD = """
    Give me the nba games results for the game of the 19th of March 2025.
"""

SPORTS_RESULTS_WEB_SEARCH_PROMPT = """
    Provide me a summary of the sports events of {yesterday_date}. Exclude NBA results from this research.
    Key and core focus on Soccer in Europe (France, England, Spain), and on international sports competitions.
"""

FINAL_SUMMARY_PROMPT = """\
        You are a sports news reporter.

        Your task is to write an article-style summary of the NBA and Sports event results from yesterday.
        Create two distinct section: One for NBA results and one for other sports results.
        The output should be formatted in HTML and include the date (yesterday) right after the article title.

        Use a journalistic tone suitable for a sports news website.

        Yesterday's date: {yesterday_date}
        NBA results: {nba_results}
        Sports Summary: {sports_summary}
    """

TEMPLATE_HTML = """
Template to use
```html
NBA Results Summary - 14/07/2025
Yesterday's NBA action featured several thrilling matchups, showcasing both exciting finishes and standout performances across the league.

Game Results from March 19, 2025
Mavericks (DAL) @ Pacers (IND): Final Score - DAL 131, IND 135
Rockets (HOU) @ Magic (ORL): Final Score - HOU 116, ORL 108
Pistons (DET) @ Heat (MIA): Final Score - DET 116, MIA 113
76ers (PHI) @ Thunder (OKC): Final Score - PHI 100, OKC 133
Knicks (NYK) @ Spurs (SAS): Final Score - NYK 105, SAS 120
Pelicans (NOP) @ Timberwolves (MIN): Final Score - NOP 119, MIN 115
Wizards (WAS) @ Jazz (UTA): Final Score - WAS 112, UTA 128
Grizzlies (MEM) @ Trail Blazers (POR): Final Score - MEM 99, POR 115
Bulls (CHI) @ Suns (PHX): Final Score - CHI 121, PHX 127
Cavaliers (CLE) @ Kings (SAC): Final Score - CLE 119, SAC 123
Nuggets (DEN) @ Lakers (LAL): Final Score - DEN 108, LAL 120
Notable Performances
Devin Booker of the Phoenix Suns scored 41 points, leading his team to a 127-121 victory over the Chicago Bulls. Read More
Cade Cunningham of the Detroit Pistons secured a triple-double with 25 points, 12 rebounds, and 11 assists, including a game-winning 3-pointer with 0.6 seconds left in a 116-113 win over the Miami Heat. Read More
Aaron Wiggins of the Oklahoma City Thunder led his team with 26 points in a decisive 133-100 win over the Philadelphia 76ers, clinching the Northwest Division title for the Thunder. Read More
Ivica Zubac of the Los Angeles Clippers celebrated his 28th birthday with a double-double, scoring 28 points and pulling down 20 rebounds in a 132-119 victory over the Cleveland Cavaliers. Read More
Jimmy Butler III of the Golden State Warriors contributed 24 points, 8 rebounds, and 10 assists, leading his team to a 104-93 win over the Milwaukee Bucks. Read More
These performances highlight the competitive nature of the league as teams continue to vie for playoff positioning, setting the stage for an exciting conclusion to the regular season.

```
"""