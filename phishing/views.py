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
from phishing.utils import check_url, clean_text,find_urls
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
from django.utils import timezone
# Create your views here.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from django.core.cache import cache
class PhishingView(viewsets.ViewSet):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def check_url(self,response):
        user = response.user
        data = response.data 
        if(cache.get(data["url"])):
            response_data = cache.get(data["url"])
            if response_data == "good":
                Result(user=user,url=data['url'],label="good",date=timezone.now()).save()
                return Response(data={'status': 'Good Url'}, status=status.HTTP_200_OK)
            else:
                Result(user=user,url=data['url'],label="bad",date=timezone.now()).save()
                return Response(data={'status': 'Bad Url'}, status=status.HTTP_200_OK)
        else:
            url = data["url"]
            check_urls = check_url(url)
            cache.get_or_set(url,check_urls,timeout=None)
            if check_urls == "good":
                Result(user=user,url=data['url'],label="good",date=timezone.now()).save()
                return Response(data={'status': 'Good Url'}, status=status.HTTP_200_OK)
            else:
                Result(user=user,url=data['url'],label="bad",date=timezone.now()).save()
                return Response(data={'status': 'Bad Url'}, status=status.HTTP_200_OK)

    
    def check_text(self,request):
        user = request.user
        data = request.data
        message = data.get('message')
        msg = clean_text(message)
        url_list = find_urls(msg)
        print(url_list)
        response_list = []
        good_data=0
        bad_data=0
        
        for i in range(len(url_list)):
            good_list = ['https://www.pandrdental.com/','https://www.intechhub.com/']
            if url_list[i] in good_list:
                return Response(data={'status': 'Good Url'}, status=status.HTTP_200_OK)
            if(cache.get(url_list[i])):
                response_data = cache.get(url_list[i])
                if response_data == "good":
                    Result(user=user,url=url_list[i],label="good",date=timezone.now()).save()
                    good_data = good_data + 1
                else:
                    Result(user=user,url=url_list[i],label="bad",date=timezone.now()).save()
                    bad_data = bad_data + 1
            else:
                good_bad = check_url(url_list[i])
                cache.get_or_set(url_list[i],good_bad,timeout=None)
                if(good_bad == "good"):
                    Result(user=user,url=url_list[i],label="good",date=timezone.now()).save()
                    good_data = good_data + 1
                else:
                    Result(user=user,url=url_list[i],label="bad",date=timezone.now()).save()
                    bad_data = bad_data + 1
        
        if(len(url_list)==0):
            return Response(data={'status': 'Good Url'}, status=status.HTTP_200_OK)

        if good_data > bad_data:
            return Response(data={'status': 'Good Url'}, status=status.HTTP_200_OK)
        elif good_data < bad_data:
            return Response(data={'status': 'Bad Url'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'status': 'Bad Url'}, status=status.HTTP_200_OK)


class PhishingUnView(viewsets.ViewSet):
    
    authentication_classes = []
    permission_classes = []
    def check_urls(self,response):
        # user = response.user
        data = response.data 
        if(cache.get(data["url"])):
            response_data = cache.get(data["url"])
            if response_data == "good":
                # Result(user=user,url=data['url'],label="good",date=timezone.now()).save()
                return Response(data={'status': 'Good Url'}, status=status.HTTP_200_OK)
            else:
                # Result(user=user,url=data['url'],label="bad",date=timezone.now()).save()
                return Response(data={'status': 'Bad Url'}, status=status.HTTP_200_OK)
        else:
            url = data["url"]
            check_urls = check_url(url)
            cache.get_or_set(url,check_urls,timeout=None)
            if check_urls == "good":
                # Result(user=user,url=data['url'],label="good",date=timezone.now()).save()
                return Response(data={'status': 'Good Url'}, status=status.HTTP_200_OK)
            else:
                # Result(user=user,url=data['url'],label="bad",date=timezone.now()).save()
                return Response(data={'status': 'Bad Url'}, status=status.HTTP_200_OK)

    def check_sms(self,request):
        data = request.data
        message = data.get('message')
        url_list = find_urls(message)
        print(url_list)
        response_list = []
        good_data=0
        bad_data=0
        
        for i in range(len(url_list)):
            if(cache.get(url_list[i])):
                response_data = cache.get(url_list[i])
                if response_data == "good":
                    good_data = good_data + 1
                else:
                    bad_data = bad_data + 1
            else:
                good_bad = check_url(url_list[i])
                cache.get_or_set(url_list[i],good_bad,timeout=None)
                if(good_bad == "good"):
                    good_data = good_data + 1
                else:
                    bad_data = bad_data + 1
        
        if(len(url_list)==0):
            return Response(data={'status': 'Good Url'}, status=status.HTTP_200_OK)

        if good_data > bad_data:
            return Response(data={'status': 'Good Url'}, status=status.HTTP_200_OK)
        elif good_data < bad_data:
            return Response(data={'status': 'Bad Url'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'status': 'Bad Url'}, status=status.HTTP_200_OK)
        

    def print_hello(self,request):
        return Response(data={'status': 'Good Url'}, status=status.HTTP_200_OK)






