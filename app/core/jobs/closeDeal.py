from app.interfaces.email.notification_email import send_email


def notify_owner_about_deal(client_name: str, client_number: str, owner_email: str):
    """
    Notify the owner via email that a specific client is ready to close a deal.

    Args:
        client_name (str): Name of the client.
        client_number (str): Phone number of the client.
        owner_email (str): Email of the owner to notify.
    """
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

    # Use the general-purpose function
    send_email(
        subject=subject,
        message_body=message_body,
        receiver_emails=[owner_email],
        additional_info=additional_info
    )

# Example usage
notify_owner_about_deal("John Doe", "123456789", "owner@example.com")
