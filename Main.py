import smtplib
from utils.Env import MailTo
from utils.HTMLGenerator import msg

# Settings
from_mail = MailTo
to_mail = MailTo

smtp_server = "smtpgw.chec.local"
smtp_port = 25
# Create the email message

msg['Subject'] = 'Status On Production Blobs'
msg['From'] = from_mail
msg['To'] = to_mail

# Send mail
try:
    smtpObj = smtplib.SMTP(smtp_server)
    smtpObj.sendmail(from_mail, to_mail, msg.as_string())
    print("Successfully sent email")
except smtplib.SMTPException:
    print("Error: unable to send email")

