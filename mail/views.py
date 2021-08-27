
# from mail import models
# from django.shortcuts import render
# import win32com.client as client
# import pythoncom

# # Create your views here.
# def send_mails(category,subject,html_body,body):
#     print('hello')
    
#     pythoncom.CoInitialize()
#     user = models.MailUser.objects.filter(category__name=category)
#     for i in user:
#         if i.user.email is None:
#             pass
#         else:
#             outlook = client.Dispatch("Outlook.Application")
#             oLNS = outlook.GetNameSpace('MAPI')
    
#             message = outlook.CreateItem(0)
#             message._oleobj_.Invoke(*(64209,0,8,0,oLNS.Accounts.Item('abhinav.jha@intechhub.com')))
#             message.Display()
#             message.To = i.user.email
#             message.subject = subject
#             if html_body is None:
#                 message.Body = body
#             else:
#                 message.HTMLBody = html_body
#             message.Save()
#             message.Send()
#             print(i.user.email)