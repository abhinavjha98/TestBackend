
from mail import models
from django.shortcuts import render

# Create your views here.
def send_mails(category):
    user = models.MailUser.objects.filter(category__name=category)
    for i in user:
        print(i.user.email)