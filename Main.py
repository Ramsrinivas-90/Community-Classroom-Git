import win32com.client as client

from utils.Env import MailTo, FilePath
from utils.HTMLGenerator import *

outlook = client.Dispatch('Outlook.Application')
mail = outlook.CreateItem(0)
mail.display()
mail.To = MailTo
mail.Subject = 'Pyro BV Flow'

mail.htmlbody = HTMLBody
mail.Attachments.Add(FilePath)
if mail.send:
    print('Mail Sent')
