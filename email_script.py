import smtplib
from email.message import EmailMessage

print("Welcome to the email sender")


email = EmailMessage()
email['from'] = str(input('FROM: '))
email['to'] = str(input('TO (EMAIL):  '))
email['subject'] = str(input('SUBJECT: '))
email.set_content(str(input("MESSAGE: ")))

with smtplib.SMTP(host='smtp.gmail.com', port= 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(str(input('Your gmail acct email: ')), str(input('Your gmail acct password: ')))
    smtp.send_message(email)
    print('Message Sucessfully Sent !')
