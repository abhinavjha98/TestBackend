from django.contrib import admin
from django.urls import path
from account import views
from phishing.views import *

urlpatterns = [
  path('checkurl/',PhishingView.as_view({'get':'check_url'})),
]