from django.db import models
from database.models import Base
from account.models import User
# Create your models here.
class Result(Base):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, null=True)
    label = models.CharField(max_length=50,null=True)