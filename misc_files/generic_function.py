from email.message import EmailMessage
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def otp_generate():
    otp= random.randint(100000,1000000)
    return otp

def otp_send(otp, email):
    your_email = "mansimehndiratta28@gmail.com"
    your_password = "mywebsite@personal"

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(your_email, your_password)

    msg = MIMEMultipart()
    msg['To'] = email
    msg['From'] = your_email
    msg['Subject']="Mansi Mehndiratta"
    body1="Welcome to Mansi Mehndiratta's Website for blogging\n"
    bodyHTML="Your OTP to Confirm Sign Up is <b>"+str(otp)+"</b>."
    body2= "\nThanks for Joining!\n\nRegards,\nMansi Mehndiratta"
    msg.attach(MIMEText(body1,'plain'))
    msg.attach(MIMEText(bodyHTML,'HTML'))
    msg.attach(MIMEText(body2,'plain'))
    s.sendmail(your_email,email,str(msg))
    s.quit()