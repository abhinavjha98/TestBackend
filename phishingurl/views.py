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
