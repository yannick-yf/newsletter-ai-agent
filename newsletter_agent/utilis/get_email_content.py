from newsletter_agent.utilis.get_date import get_date_of_yesterday

def get_html_content():
    html_content = f"""
    <html>
        <body>
            <h2>Hello!</h2>
            <p>This is an <b>HTML</b> email and the date of yesterday was {get_date_of_yesterday()}.</p>
            <p>Visit <a href="https://www.python.org">Python.org</a></p>
        </body>
    </html>
    """

    return html_content