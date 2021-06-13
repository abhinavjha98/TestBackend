from django.db import models
from database.models import Base
# Create your models here.
class Result(Base):
    url = models.CharField(max_length=200, null=True)
    label = models.CharField(max_length=50,null=True)