import os
from dotenv import load_dotenv

from send_email import send_gmail
from get_email_content import get_html_content

load_dotenv()

success = send_gmail(
    sender_email=os.getenv('GMAIL_EMAIL'),
    sender_password=os.getenv('GMAIL_APP_PASSWORD'),
    recipient_email=["ipfy.solutions@gmail.com", 'yannick.flores1992@gmail.com'],
    subject="Email Test",
    body="This is the plain text version.",
    html_body=get_html_content()
)
