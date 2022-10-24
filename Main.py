import win32com.client as client
from HTML import *

outlook = client.Dispatch("Outlook.Application")
mail = outlook.CreateItem(0)
mail.display()
mail.To = "pyrosupportinternal"
mail.CC = "Aravinth Kumar;"
mail.Subject = "Pyro BV"
mail.htmlbody = HTMLBody
mail.Attachments.Add('C:/Users/akumar45/Downloads/Pyro BV Mail/body.txt')
mail.send
