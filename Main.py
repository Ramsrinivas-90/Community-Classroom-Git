import win32com.client as client
from HTML import *

outlook = client.Dispatch("Outlook.Application")
mail = outlook.CreateItem(0)
mail.display()
mail.To = "Aravinth Kumar"
mail.Subject = "Pyro BV"
mail.htmlbody = HTMLBody
mail.Attachments.Add(
    'C:/Users/akumar45/OneDrive - Mr. Cooper/PYROBVMailScript/body.txt')
if mail.send:
    print("Mail Sent")
