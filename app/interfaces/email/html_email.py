from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List
import smtplib
import os

def send_html_email(subject: str, message_body: str, receiver_emails: List[str], additional_info: dict | None):
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
            print("Environment variables 'EMAIL' and 'PASSWORDEMAIL' must be set.")

        if not receiver_emails or not isinstance(receiver_emails, list):
            print("Receiver emails must be provided as a list of valid email addresses.")
        if not subject or not message_body:
            print("Both 'subject' and 'message_body' must be provided.")

        # Build additional information for plain text
        plain_text_message = f"{message_body}\n\n"
        if additional_info:
            plain_text_message += "Additional Information:\n"
            for key, value in additional_info.items():
                plain_text_message += f"- {key}: {value}\n"
        
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f5f5f5;
                }
                .email-container {
                    max-width: 600px;
                    margin: 20px auto;
                    background-color: #ffffff;
                    border-radius: 8px;
                    overflow: hidden;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                }
                .header {
                    background-color: #f1f3f4;
                    padding: 20px;
                    text-align: center;
                }
                .header img {
                    max-width: 100px;
                    margin-bottom: 10px;
                }
                .content {
                    padding: 20px;
                }
                .content h1 {
                    font-size: 20px;
                    color: #333333;
                    margin: 0 0 10px;
                }
                .content p {
                    font-size: 16px;
                    color: #555555;
                    line-height: 1.5;
                    margin: 10px 0;
                }
                .content .action-box {
                    background-color: #f1f3f4;
                    border-left: 4px solid #4285f4;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 20px 0;
                }
                .content .action-box p {
                    margin: 0;
                    font-size: 14px;
                    color: #333333;
                }
                .button {
                    display: block;
                    text-align: center;
                    margin: 20px auto;
                }
                .button a {
                    text-decoration: none;
                    padding: 10px 20px;
                    background-color: #4285f4;
                    color: #ffffff;
                    border-radius: 5px;
                    font-size: 16px;
                }
                .footer {
                    background-color: #f1f3f4;
                    padding: 10px;
                    text-align: center;
                    font-size: 12px;
                    color: #777777;
                }
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <img src="https://example.com/icon.png" alt="Icon">
                </div>
                <div class="content">
                    <h1>Hi [Owner's Name],</h1>
                    <p>We’re reaching out to let you know that a client is ready to close a deal. The chatbot has identified this opportunity based on recent interactions.</p>
                    <p>Please follow up promptly with the client to finalize the agreement.</p>
                    <div class="action-box">
                        <p><strong>Client Details:</strong></p>
                        <p>
                            <strong>Name:</strong> [Client Name] <br>
                            <strong>Phone Number:</strong> [Client Phone] <br>
                            <strong>WhatsApp Link:</strong> <a href="https://wa.me/[Client Phone]">Chat Now</a>
                        </p>
                    </div>
                    <div class="button">
                        <a href="https://yourcrmtool.com">View Full Details</a>
                    </div>
                </div>
                <div class="footer">
                    <p>© 2024 Your Company. All rights reserved.</p>
                </div>
            </div>
        </body>
        </html>
        """
        msg = MIMEMultipart("alternative")
        msg['From'] = sender_email
        msg['To'] = ', '.join(receiver_emails)
        msg['Subject'] = subject
        msg.attach(MIMEText(plain_text_message, 'plain'))
        msg.attach(MIMEText(html_content, 'html'))

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
