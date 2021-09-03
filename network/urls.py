from django.contrib import admin
from django.urls import path
from account import views
from .views import Network

urlpatterns = [
  path('add/network/',Network.as_view({'post':'add_network'})),
  path('check/network/',Network.as_view({'post':'check_domain'})),
  path('get/network/',Network.as_view({'get':'get_network'})),
]