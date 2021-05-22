import datetime
from .models import CronData,aa419
def my_scheduled_job():
    aa419.objects.create(url = "hello",label=str(datetime.datetime.now()))
    print("Hello")