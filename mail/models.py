from mail.views import send_mails
from django.db import models
from database.models import Base
from account.models import User
# Create your models here.

class Category(Base):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class MailUser(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True,on_delete=models.CASCADE)

class SendMail(Base):
   subject = models.CharField(max_length=200, null=True)
   category = models.ForeignKey(Category, null=True,on_delete=models.CASCADE)
   html_data = models.CharField(max_length=1000,null=True,blank=True)
   body = models.CharField(null=True,max_length=1000,blank=True)
    
   def save(self, *args, **kwargs):
       send_mails(self.category,self.subject,self.html_data,self.body)
       print(self.category)
       super(SendMail, self).save(*args, **kwargs)