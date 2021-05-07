from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    username = models.CharField(max_length=150, null=True, blank=True,unique=True)
    email = models.EmailField(max_length=150, blank=True, null=True, unique=True)
    mobile = models.CharField(max_length=15, null=True, blank=True, unique=True)
    dob = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

