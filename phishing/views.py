from django.shortcuts import render
# EDA Packages
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
import requests
from bs4 import BeautifulSoup
import pandas as pd
from database.models import aa419
from phishing.utils import check_url

class PhishingView(viewsets.ViewSet):

    def check_url(self,response):
        data = response.data
        url = data["url"]
        print(check_url(url))
        return Response(data={'status': 'Completed'}, status=status.HTTP_200_OK)







