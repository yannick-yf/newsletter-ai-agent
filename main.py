"""Main function executing Agentic Workflow and sending email"""

import os
from dotenv import load_dotenv

from newsletter_agent.utilis.send_email import send_gmail

load_dotenv()

from newsletter_agent.agent.output_formating import output_formating

success = send_gmail(
    sender_email=os.getenv('GMAIL_EMAIL'),
    sender_password=os.getenv('GMAIL_APP_PASSWORD'),
    recipient_email=["ipfy.solutions@gmail.com", 'yannick.flores1992@gmail.com'],
    subject="Email Test",
    body="This is the plain text version.",
    html_body=output_formating()
)
