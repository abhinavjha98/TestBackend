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
# Create your views here.

urls_data = pd.read_csv("datasets/urldata.csv")
y = urls_data["label"]
url_list = urls_data["url"]
vectorizer = TfidfVectorizer(tokenizer=makeTokens)
X = vectorizer.fit_transform(url_list)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

logit = LogisticRegression()	
logit.fit(X_train, y_train)

print("Accuracy ",logit.score(X_test, y_test))

