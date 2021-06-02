from django.shortcuts import render
# EDA Packages
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication, viewsets
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
import pandas as pd
import numpy as np
import random
import pickle
import whois
import datetime
import re
from bs4 import BeautifulSoup
import whois
import urllib
import urllib.request
from urllib.parse import urlparse,urlencode
import ipaddress
import requests
from phishing.utils import makeTokens
# Create your views here.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from rest_framework_simplejwt.authentication import JWTAuthentication
class PhishingView(viewsets.ViewSet):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def check_url(self,response):
        data = response.data 
        url = data["url"]
        check_urls = check_url(url)
        if check_urls == "good":
            return Response(data={'status': 'Good Url'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'status': 'Bad Url'}, status=status.HTTP_200_OK)
      







