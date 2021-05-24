from django.contrib import admin
from django.urls import path
from elasticsearch.views import *
urlpatterns = [
    
    path('search/' , PublisherDocumentView.as_view({'get': 'list'})),
    
]