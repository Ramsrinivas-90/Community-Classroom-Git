import win32com.client as client

from utils.Env import MailTo
from utils.HTMLGenerator import htmlbody

outlook = client.Dispatch('Outlook.Application')
mail = outlook.CreateItem(0)
mail.display()
mail.To = MailTo
mail.Subject = 'Status On Production Blobs'
mail.htmlbody = htmlbody

if mail.send:
    print('Mail Sent')
