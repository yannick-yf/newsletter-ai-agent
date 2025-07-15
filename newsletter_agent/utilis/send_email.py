import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from typing import List, Optional

from dotenv import load_dotenv
load_dotenv()  

def send_gmail(
    sender_email: str,
    sender_password: str,
    recipient_email: List[str],
    subject: str,
    body: str,
    html_body: Optional[str] = None,
    attachments: Optional[List[str]] = None,
    cc: Optional[List[str]] = None,
    bcc: Optional[List[str]] = None
) -> bool:
    """
    Send an email using Gmail SMTP server.
    
    Args:
        sender_email (str): Your Gmail address
        sender_password (str): Your Gmail app password (not regular password)
        recipient_email (List): Recipient's email address
        subject (str): Email subject
        body (str): Plain text email body
        html_body (str, optional): HTML email body
        attachments (List[str], optional): List of file paths to attach
        cc (List[str], optional): List of CC recipients
        bcc (List[str], optional): List of BCC recipients
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    
    try:
        # Create message container
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipient_email)
        msg['Subject'] = subject
        
        # Add CC and BCC if provided
        if cc:
            msg['Cc'] = ', '.join(cc)
        if bcc:
            msg['Bcc'] = ', '.join(bcc)
        
        # Add plain text part
        text_part = MIMEText(body, 'plain')
        msg.attach(text_part)
        
        # Add HTML part if provided
        if html_body:
            html_part = MIMEText(html_body, 'html')
            msg.attach(html_part)
        
        # Add attachments if provided
        if attachments:
            for file_path in attachments:
                if os.path.isfile(file_path):
                    with open(file_path, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                    
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename= {os.path.basename(file_path)}'
                    )
                    msg.attach(part)
        
        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable TLS encryption
        server.login(sender_email, sender_password)
        
        # Prepare recipient list
        recipients = [', '.join(recipient_email)]
        if cc:
            recipients.extend(cc)
        if bcc:
            recipients.extend(bcc)
        
        # Send email
        text = msg.as_string()
        server.sendmail(sender_email, recipients, text)
        server.quit()
        
        print(f"Email sent successfully to {', '.join(recipient_email)}")
        return True
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False


# Example usage function
def main():
    """Example of how to use the send_gmail function"""
    
    # Email with HTML content and attachments
    html_content = """
    <html>
        <body>
            <h2>Hello!</h2>
            <p>This is an <b>HTML</b> email.</p>
            <p>Visit <a href="https://www.python.org">Python.org</a></p>
        </body>
    </html>
    """
    
    success = send_gmail(
        sender_email=os.getenv('GMAIL_EMAIL'),
        sender_password=os.getenv('GMAIL_APP_PASSWORD'),
        recipient_email=["ipfy.solutions@gmail.com", 'yannick.flores1992@gmail.com'],
        subject="Email Test",
        body="This is the plain text version.",
        html_body=html_content,
        # attachments=["path/to/file.pdf", "path/to/image.jpg"],
        # attachments=["path/to/file.pdf", "path/to/image.jpg"],
        #cc=["cc_recipient@example.com"],
        #bcc=["bcc_recipient@example.com"]
    )


if __name__ == "__main__":
    main()