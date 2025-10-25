import smtplib
from email.message import EmailMessage



def send_email(subject, hr_email, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'insert here your bot email'
    msg['To'] = hr_email
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('insert here your bot email',"insert here your bot password")
        smtp.send_message(msg)