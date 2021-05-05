from django.contrib import admin
from django.urls import path
from account import views
from database.views import *

urlpatterns = [
    path('aa419/',FakeWebsiteView.as_view({'get':'get_data'})),
]
