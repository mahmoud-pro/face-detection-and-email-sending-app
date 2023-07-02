import smtplib
from dotenv import dotenv_values, load_dotenv
import os
import imghdr

from email.message import EmailMessage

load_dotenv()
config = dotenv_values(".env")

PASSWORD = os.getenv("APP_PASS")
SENDER = os.getenv("EMAIL")
RECEIVER = os.getenv("EMAIL")


def send_email(image_path):
    print("Send email start...")
    email_message = EmailMessage()
    email_message["Subject"] = "New Person!"
    email_message.set_content("Hi, We just saw a new person!")

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gamil.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, password=PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

    print("Send email end...")


if __name__ == "__main__":
    send_email(image_path="images/20.png")
