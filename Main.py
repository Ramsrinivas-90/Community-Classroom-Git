import win32com.client as client
from utils.htmlGenerator import htmlbody

outlook = client.Dispatch('Outlook.Application')
mail = outlook.CreateItem(0)
mail.display()
mail.To = 'Aravinth Kumar'
mail.Subject = 'Status On Production Blobs'
mail.htmlbody = htmlbody

if mail.send:
    print('Mail Sent')
