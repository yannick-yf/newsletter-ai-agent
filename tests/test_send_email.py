import unittest
from unittest.mock import patch, MagicMock, mock_open
import smtplib
from send_email import send_gmail

class TestGmailSender(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.sender_email = "test@gmail.com"
        self.sender_password = "test_password"
        self.recipient_email = ["recipient@example.com"]
        self.subject = "Test Subject"
        self.body = "Test body content"
        self.html_body = "<h1>Test HTML</h1>"
    
    @patch('smtplib.SMTP')
    def test_send_basic_email_success(self, mock_smtp):
        """Test sending a basic email successfully."""
        # Mock the SMTP server
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server
        
        # Call the function
        result = send_gmail(
            sender_email=self.sender_email,
            sender_password=self.sender_password,
            recipient_email=self.recipient_email,
            subject=self.subject,
            body=self.body
        )
        
        # Assertions
        self.assertTrue(result)
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once_with(self.sender_email, self.sender_password)
        mock_server.sendmail.assert_called_once()
        mock_server.quit.assert_called_once()
    
    @patch('smtplib.SMTP')
    def test_send_email_with_html_body(self, mock_smtp):
        """Test sending email with HTML body."""
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server
        
        result = send_gmail(
            sender_email=self.sender_email,
            sender_password=self.sender_password,
            recipient_email=self.recipient_email,
            subject=self.subject,
            body=self.body,
            html_body=self.html_body
        )
        
        self.assertTrue(result)
        mock_server.sendmail.assert_called_once()
    
    @patch('smtplib.SMTP')
    def test_send_email_with_cc_and_bcc(self, mock_smtp):
        """Test sending email with CC and BCC recipients."""
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server
        
        cc_list = ["cc1@example.com", "cc2@example.com"]
        bcc_list = ["bcc1@example.com"]
        
        result = send_gmail(
            sender_email=self.sender_email,
            sender_password=self.sender_password,
            recipient_email=self.recipient_email,
            subject=self.subject,
            body=self.body,
            cc=cc_list,
            bcc=bcc_list
        )
        
        self.assertTrue(result)
        mock_server.sendmail.assert_called_once()
    
    @patch('smtplib.SMTP')
    @patch('os.path.isfile')
    @patch('builtins.open', new_callable=mock_open, read_data=b"file content")
    def test_send_email_with_attachments(self, mock_file, mock_isfile, mock_smtp):
        """Test sending email with attachments."""
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server
        mock_isfile.return_value = True
        
        attachments = ["test_file.txt", "test_image.jpg"]
        
        result = send_gmail(
            sender_email=self.sender_email,
            sender_password=self.sender_password,
            recipient_email=self.recipient_email,
            subject=self.subject,
            body=self.body,
            attachments=attachments
        )
        
        self.assertTrue(result)
        mock_server.sendmail.assert_called_once()
        # Check that files were opened for each attachment
        self.assertEqual(mock_file.call_count, len(attachments))
    
    @patch('smtplib.SMTP')
    @patch('os.path.isfile')
    def test_send_email_with_non_existent_attachment(self, mock_isfile, mock_smtp):
        """Test sending email with non-existent attachment file."""
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server
        mock_isfile.return_value = False
        
        attachments = ["non_existent_file.txt"]
        
        result = send_gmail(
            sender_email=self.sender_email,
            sender_password=self.sender_password,
            recipient_email=self.recipient_email,
            subject=self.subject,
            body=self.body,
            attachments=attachments
        )
        
        self.assertTrue(result)
        mock_server.sendmail.assert_called_once()
    
    @patch('smtplib.SMTP')
    def test_send_email_multiple_recipients(self, mock_smtp):
        """Test sending email to multiple recipients."""
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server
        
        multiple_recipients = ["recipient1@example.com", "recipient2@example.com"]
        
        result = send_gmail(
            sender_email=self.sender_email,
            sender_password=self.sender_password,
            recipient_email=multiple_recipients,
            subject=self.subject,
            body=self.body
        )
        
        self.assertTrue(result)
        mock_server.sendmail.assert_called_once()
    
    @patch('smtplib.SMTP')
    def test_send_email_authentication_error(self, mock_smtp):
        """Test handling authentication error."""
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server
        mock_server.login.side_effect = smtplib.SMTPAuthenticationError(535, "Authentication failed")
        
        result = send_gmail(
            sender_email=self.sender_email,
            sender_password=self.sender_password,
            recipient_email=self.recipient_email,
            subject=self.subject,
            body=self.body
        )
        
        self.assertFalse(result)
    
    @patch('smtplib.SMTP')
    def test_send_email_general_exception(self, mock_smtp):
        """Test handling general exception."""
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server
        mock_server.sendmail.side_effect = Exception("General error")
        
        result = send_gmail(
            sender_email=self.sender_email,
            sender_password=self.sender_password,
            recipient_email=self.recipient_email,
            subject=self.subject,
            body=self.body
        )
        
        self.assertFalse(result)
    
    @patch('smtplib.SMTP')
    def test_send_email_empty_recipient_list(self, mock_smtp):
        """Test sending email with empty recipient list."""
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server
        
        result = send_gmail(
            sender_email=self.sender_email,
            sender_password=self.sender_password,
            recipient_email=[],
            subject=self.subject,
            body=self.body
        )
        
        self.assertTrue(result)
        mock_server.sendmail.assert_called_once()


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)