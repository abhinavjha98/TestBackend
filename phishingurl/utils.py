from django.shortcuts import render
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

# Machine Learning Packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def makeTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')	# make tokens after splitting by slash
    total_Tokens = []
    for i in tkns_BySlash:
        tokens = str(i).split('-')	# make tokens after splitting by dash
        tkns_ByDot = []
        for j in range(0,len(tokens)):
            temp_Tokens = str(tokens[j]).split('.')	# make tokens after splitting by dot
            tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
    total_Tokens = list(set(total_Tokens))	#remove redundant tokens
    if 'com' in total_Tokens:
        total_Tokens.remove('com')	#removing .com since it occurs a lot of times and it should not be included in our features
    return total_Tokens

def find_date(url):
    who_is = whois.whois(url)
    if type(who_is.creation_date) is list:
        date_ip_address = who_is.creation_date[0]
    else:
        date_ip_address = who_is.creation_date

    # print(date_ip_address)
    current_time = datetime.datetime.now()
    if date_ip_address is None:

        days = 0
    else:
        actual_time = current_time-date_ip_address
        # print(actual_time)
        days = int(actual_time.days)
        # print(days)
    return days