from django.contrib import admin
from django.urls import path
from account import views
from account.views import UserAuthView

urlpatterns = [
    path('signup/',UserAuthView.as_view({'post':'signup'})),
    path('login/', UserAuthView.as_view({'post': 'login'})),
]
