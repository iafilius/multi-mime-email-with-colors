import os
import smtplib
import dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

def send_mail_gmail(username,password,toaddrs_list,msg_text,fromaddr=None,subject="Test mail",attachment_path_list=None):

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(username, password)
    s.set_debuglevel(1)
    msg = MIMEMultipart()
    sender = fromaddr
    recipients = toaddrs_list
    msg['Subject'] = subject
    if fromaddr is not None:
        msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    if attachment_path_list is not None:
        for each_file_path in attachment_path_list:
            try:
                file_name=each_file_path.split("/")[-1]
                part = MIMEBase('application', "octet-stream")
                part.set_payload(open(each_file_path, "rb").read())

                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment' ,filename=file_name)
                msg.attach(part)
            except:
                print("could not attache file")
    msg.attach(MIMEText(msg_text,'html'))
    s.sendmail(sender, recipients, msg.as_string())
    s.quit()
    

load_dotenv() # take environment variables from .env.

# load environment variables
gmail_username=os.getenv("GMAIL_USERNAME")
gmail_app_key=os.getenv("GMAIL_APP_KEY")
gmail_fromaddr=os.getenv("GMAIL_FROMADDR")
gmail_toaddrs_list=os.environ.get("GMAIL_TOADDRS_LIST").split(" ")
gmail_attachements_list=os.environ.get("GMAIL_ATTACHMENTS_LIST").split(" ")

send_mail_gmail(username=gmail_username,password=gmail_app_key,toaddrs_list=gmail_toaddrs_list,msg_text="<p style=\"color:red;\">Red text</p>.",fromaddr=gmail_fromaddr,subject="Test mail",attachment_path_list=gmail_attachements_list)

