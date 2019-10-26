import smtplib
import ssl
from email import encoders
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Gmail login

sender_email = "yourGmailAccount@gmail.com"
password = "yourPassword"


# Choose receiver

print("\nContacts: "
      "\n 1 - optionalRecipient1@gmail.com"
      "\n 2 - optionalRecipient2@gmail.com "
      "\n 3 - optionalRecipient3@gmail.com "
      "\n 4 - CUSTOM in next step"
      )

receiverInput = input("Enter account number: ")

if receiverInput == "1":
    receiver_email = "optionalRecipient1@gmail.com"
elif receiverInput == "2": receiver_email = 'optionalRecipient2@gmail.com'
elif receiverInput == "3": receiver_email = 'optionalRecipient2@gmail.com'
else: receiver_email = input('Enter custom mail address: ')
print('Receiver is: ' + receiver_email)


# Choose picture attachment

print('\nAttachments: '
      '\n 1 - Big picture (6MB)'
      '\n 2 - Small picture (few Kb)'
      )


fileInput = input("Enter picture number: ")
if fileInput == '1': filename = "nightSky.jpg"
else: filename = 'bugpic2.jpg'

# Set subject

subj = input("\nEnter Subject: ")
messageText = "Hi Human. I am Python. How is it going?"
amount = int(input("\nEnter mails amount: "))

# Sending

x = 1
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    while x <= amount:

        message = MIMEMultipart("alternative")
        message["Subject"] = subj + " " + str(x)
        message["From"] = sender_email
        message["To"] = receiver_email
        text = messageText
        part1 = MIMEText(text, "plain")
        message.attach(part1)


        # adding attachment




        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        server.sendmail(
            sender_email, receiver_email, message.as_string())

        print(x)
        x += 1

print('Done...',amount, 'mail/s was sent...')