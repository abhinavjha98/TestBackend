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
from rest_framework.parsers import MultiPartParser, FileUploadParser
import pathlib
import os
from django.core.files.storage import default_storage
from pdf2image import convert_from_path
import os
import PyPDF2
from django.core.files.base import ContentFile
import easyocr
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
        endpoint = data.get('endpoint')
        print(message)
        msg = clean_text(message)
        url_list = find_urls(msg)
        print(url_list)
        response_list = []
        sub=[]
        good_data=0
        bad_data=0
        category = ""
        if endpoint == 'mobile':
            category = 'Smishing'
        elif endpoint == 'url':
            category = 'Phishing Links'
        else:
            category = 'Email Phishing'
        good_bad=[]
        for i in range(len(url_list)):
            good_list = ['https://www.pandrdental.com/','https://www.intechhub.com/']
            if url_list[i] in good_list:
                good_data = good_data + 1
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
                print("H")
                print(good_bad)
                cache.get_or_set(url_list[i],good_bad,timeout=None)
                if(good_bad[0] == "good"):
                    Result(user=user,url=url_list[i],label="good",date=timezone.now()).save()
                    good_data = good_data + 1
                else:
                    Result(user=user,url=url_list[i],label="bad",date=timezone.now()).save()
                    bad_data = bad_data + 1
        
        if(len(url_list)==0):
            return Response(data={'status': 'Good Url','endpoint':endpoint,'category':None,'subcategory':None}, status=status.HTTP_200_OK)
        print(good_data)
        print(bad_data)
        if good_data > bad_data:
            return Response(data={'status': 'Good Url','endpoint':endpoint,'category':None,'subcategory':None}, status=status.HTTP_200_OK)
        elif good_data < bad_data:
            return Response(data={'status': 'Bad Url','endpoint':endpoint,'category':category,'subcategory':good_bad[1]}, status=status.HTTP_200_OK)
        else:
            return Response(data={'status': 'Bad Url','endpoint':endpoint,'category':category,'subcategory':good_bad[1]}, status=status.HTTP_200_OK)

    def check_attachment(self,request):
        user = request.user
        data = request.data
        message = data.get('message')
        parser_classes = [MultiPartParser, FileUploadParser]
        multiple_files = request.FILES
        attach_file = multiple_files.getlist("attach_file")
        print(attach_file)
        reader = easyocr.Reader(['en'])
        good_data=0
        bad_data=0
        if(message is None):
            pass
        else:
            msg = clean_text(message)
            url_list = find_urls(msg)
            print(url_list)
            if(len(url_list)==0):
                pass
            else:
                for i in range(len(url_list)):
                    good_list = ['https://www.pandrdental.com/','https://www.intechhub.com/']
                    if url_list[i] in good_list:
                        good_data+=1
                    elif(cache.get(url_list[i])):
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
        print(good_data)
        print(bad_data)
        for i in attach_file:
            file_name = i.name.split(".")[0]
            extension = i.name.split(".")[1]
            print(i)
            pdfs = str(i)
            path = default_storage.save('tmp/'+file_name+extension, ContentFile(i.read()))
            
            if extension == "pdf":
                pdfFileObj = open('tmp/'+file_name+extension, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                print(pdfReader.numPages) 
                pages = pdfReader.numPages
                text=""
                
                for j in range(pages):
                    pageObj = pdfReader.getPage(j)
                    text += pageObj.extractText()
                # pages = convert_from_path('tmp/'+file_name+extension, 350)
                # for page in pages:
                #     text = ""
                #     image_name = "Page_" + str(i.name) + ".jpg"  
                #     page.save(image_name, "JPEG")
                #     output = reader.readtext("Page_" + str(i.o9) + ".jpg")
                #     for detection in output:
                #         text += detection[1]
                #     print(text)
            else:
                output = reader.readtext('tmp/'+file_name+extension)
                text = ""
                for detection in output:
                    text += detection[1] + ""
                print(text)
        msg = ""
        url_list=[]
        msg = clean_text(text)
        url_list = find_urls(msg)
        print(url_list)
        response_list = []
        
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
        
        print(good_data)
        print(bad_data)
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
        
        for i in url_list:
            inner_text = """<a target=\"_blank\" href =\""""
            outer_text = """\">"""
            outer = """</a>"""
            message = message.replace(i,inner_text+i+outer_text+i+outer)
        message = "<p> "+message+" </p>"
        if(len(url_list)==0):
            return Response(data=[{'status': 'Good Url','message':message}], status=status.HTTP_200_OK)

        if good_data > bad_data:
            return Response(data=[{'status': 'Good Url','message':message}], status=status.HTTP_200_OK)
        elif good_data < bad_data:
            return Response(data=[{'status': 'Bad Url','message':message}], status=status.HTTP_200_OK)
        else:
            return Response(data=[{'status': 'Bad Url','message':message}], status=status.HTTP_200_OK)
        

    def print_hello(self,request):
        return Response(data={'status': 'Good Url'}, status=status.HTTP_200_OK)






