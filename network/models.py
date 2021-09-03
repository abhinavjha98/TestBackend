from django.db import models
from database.models import Base
from account.models import User
# Create your models here.
class TrustedNetwork(Base):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    domain = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)