import win32com.client as client
from HTMLBody import htmlbody

outlook = client.Dispatch('Outlook.Application')
mail = outlook.CreateItem(0)
mail.display()
mail.To = 'Aravinth Kumar'
mail.Subject = 'Pyro BV Flow'
mail.htmlbody = htmlbody

if mail.send:
    print('Mail Sent')
