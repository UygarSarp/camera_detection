import os
import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = os.getenv("PASS3")
SENDER = "infocukamuran@gmail.com"
RECIEVER = "infocukamuran@gmail.com"


def send_email(filepath):
    email_message = EmailMessage()
    email_message["Subject"] = "WARNING"
    email_message.set_content("Somebody just entered your room!")

    with open(filepath, "rb") as file:
        image = file.read()
    email_message.add_attachment(image, maintype="image", subtype=imghdr.what(None, image))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECIEVER, email_message.as_string())
    gmail.quit()



if __name__ == "__main__":
    print(PASSWORD)