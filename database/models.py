from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class aa419(Base):
    url = models.CharField(max_length=200, null=True)
    label = models.CharField(max_length=50,null=True)

class MillionURL(Base):
    url = models.CharField(max_length=200, null=True)
    label = models.CharField(max_length=50,null=True)

class CronData(models.Model):
    time = models.CharField(max_length=100)
