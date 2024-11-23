from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List
import smtplib
import os

def send_email(subject: str, message_body: str, receiver_emails: List[str], additional_info: dict | None):
    """
    Sends a general-purpose notification email.

    Args:
        subject (str): The subject of the email.
        message_body (str): The main content of the email.
        receiver_emails (List[str]): List of recipient email addresses.
        additional_info (dict, optional): Dictionary with extra details to include in the email.

    Raises:
        ValueError: If required environment variables are missing or input validation fails.
        Exception: For other errors during email sending.
    """
    try:
        sender_email = os.environ.get('EMAIL')
        sender_password = os.environ.get('PASSWORDEMAIL')
        if not sender_email or not sender_password:
            print("Environment variables 'email' and 'pwdEmail' must be set.")

        if not receiver_emails or not isinstance(receiver_emails, list):
            print("Receiver emails must be provided as a list of valid email addresses.")
        if not subject or not message_body:
            print("Both 'subject' and 'message_body' must be provided.")

        full_message = f"{message_body}\n\n"
        if additional_info:
            full_message += "Additional Information:\n"
            for key, value in additional_info.items():
                full_message += f"- {key}: {value}\n"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join(receiver_emails)
        msg['Subject'] = subject
        msg.attach(MIMEText(full_message, 'plain', 'utf-8'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_emails, msg.as_string())
            #server.quit()
            
        print(f"Notification email sent successfully to {', '.join(receiver_emails)}.")

    except ValueError as ve:
        print(f"Validation error: {ve}")
        
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
