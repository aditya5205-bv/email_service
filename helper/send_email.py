import yagmail
from settings import MY_EMAIL, MY_PASSWORD
from logs.custom_logger import custom_logging

def send_email(email: str, email_body: str):

    receiver = email
    body = email_body

    try:
        yag = yagmail.SMTP(MY_EMAIL, MY_PASSWORD)

        yag.send(
            to=receiver,
            subject="Task Email",
            contents=body, 
        )
        
        custom_logging.info("Sent email successfully")

    except Exception as e:
        custom_logging.error(f"Email sending error: {e}", exc_info=True)