"""Utils function to get html strucutre content"""

from newsletter_agent.utilis.get_date import get_date_of_yesterday
from newsletter_agent.agent.web_search import agent_web_search

def get_html_content():
    html_content = f"""
    <html>
        <body>
            <h2>Hello!</h2>
            <p>This is an <b>HTML</b> email and the date of yesterday was {get_date_of_yesterday()}.</p>
            <p> {agent_web_search()} <p>
        </body>
    </html>
    """

    return html_content