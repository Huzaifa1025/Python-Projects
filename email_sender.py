# Simple Mail Transfer Protocol
import smtplib
from email.message import EmailMessage
from cred import sender_email, app_password
msg = EmailMessage()

msg["Subject"] = input("Enter a Subject:\n")
msg["From"] = sender_email
msg["To"] = sender_email
msg.set_content(input("Enter Your Message:\n"))

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender_email, app_password)
server.send_message(msg)
server.quit()
print("Message Sent Successfully")


