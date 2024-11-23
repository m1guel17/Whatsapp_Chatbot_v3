from app.interfaces.email.notification_email import send_email
from app.interfaces.email.html_email import send_html_email

def notify_owner_about_deal(client_name: str, client_number: str, owner_email: str):
    subject = f"Deal Ready to Close: {client_name}"
    
    message_body = (
        f"Dear Owner,\n\n"
        f"The client {client_name} with phone number {client_number} is ready to close a deal.\n"
        f"Please follow up promptly to finalize the agreement.\n\n"
        f"Regards,\nChatbot Notification System"
    )
    
    additional_info = {
        "WhatsApp Link": f"https://wa.me/{client_number}",
        "Client Name": client_name,
        "Client Phone": client_number,
    }

    send_email(subject=subject, message_body=message_body, receiver_emails=[owner_email], additional_info=additional_info)
    send_html_email(subject=subject, message_body=message_body, receiver_emails=[owner_email], additional_info=additional_info)

