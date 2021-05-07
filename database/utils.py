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
def cron_scrapy():
    URL = 'https://db.aa419.org/fakebankslist.php'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    url_list = []
    j=0
    while(j<500):
        if j<500:
            URL = 'https://db.aa419.org/fakebankslist.php?start='+str(j)
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            tablerow = soup.find_all('tr', class_='ewTableRow')
            table_alt_row = soup.find_all('tr', class_='ewTableAltRow')
            
            tablerow = table_alt_row + tablerow
            for i in tablerow:
                for link in i.find_all('a', href=True):
                    if "http" in link['href']:
                        print(link['href'])
                        break
                        dbaa419 = aa419(
                            url = link['href'],
                            label = 'bad'
                        )
                        dbaa419.save()
                        url_list.append(link['href'])
            j+=20
    