from network.serializers import TrustedNetworkSerializers
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
# Create your views here.
class Network(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def add_network(self,request):
        user = request.user
        data = request.data 
        email = data.get('email')
        domain = re.search('@.*', email).group()

        if(TrustedNetwork.objects.filter(user=user,email=email).exists()):
            return Response(data={'status': False,'message':'domain is already registered'}, status=status.HTTP_200_OK)
        else:
            network = TrustedNetwork(
                user = user,
                domain = domain.split("@")[1],
                email=email,
            )
            network.save()
        return Response(data={'status': True,'message':'domain saved sucessfully'}, status=status.HTTP_200_OK)

    def check_domain(self,request):
        user = request.user
        data = request.data 
        email = data.get('email')
        domain = re.search('@.*', email).group()

        if(TrustedNetwork.objects.filter(user=user,domain=domain.split("@")[1]).exists()):
            return Response(data={'status': True}, status=status.HTTP_200_OK)
        else:
            return Response(data={'status': False}, status=status.HTTP_200_OK)

    def get_network(self,request):
        user = request.user
        if(TrustedNetwork.objects.filter(user=user).exists()):
            trustedNetwork = TrustedNetwork.objects.filter(user=user)
            res = TrustedNetworkSerializers(trustedNetwork, many=True).data
            return Response(data={'status': True,'data':res}, status=status.HTTP_200_OK)
