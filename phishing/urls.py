from django.contrib import admin
from django.urls import path
from account import views
from .views import PhishingView

urlpatterns = [
  path('checkurl/',PhishingView.as_view({'post':'check_url'})),
]